#!/usr/bin/env python3
"""
Pureinn framework structural validator.

Deterministic integrity checks across every skill (skills/*/SKILL.md) and both
commands (commands/*/COMMAND.md). This is NOT a behavioural test - it does not
run skills. It catches the class of regression that a file-by-file human read
misses: broken cross-references, missing/mismatched required blocks, convention
drift, and self-contained-ness violations.

Two tiers:
  - ERRORS  (exit code 1): objective, unambiguous integrity failures. Block release.
  - WARNINGS (exit code 0): heuristic smells a human should eyeball. Never block.

Skill/command COUNTS are deliberately not checked here - scripts/release.sh
already auto-syncs them, so duplicating that would fight the auto-fix.

Usage:
  python3 scripts/validate.py            # full check
  python3 scripts/validate.py --strict   # treat warnings as errors too (exit 1 on any)

Run from the repo root (release.sh and validate.sh both do this).
"""

import os
import re
import sys

# ----------------------------------------------------------------------------
# Config: the invariants, derived from CLAUDE.md house standards + real files.
# ----------------------------------------------------------------------------

REQUIRED_TOP_KEYS = ["name", "description", "license"]
REQUIRED_META_KEYS = [
    "agent-mode", "author", "version", "domain",
    "triggers", "role", "scope", "output-format", "related-skills",
]
VALID_AGENT_MODES = {"synthesis", "decision", "never"}

# Agent-mode inline block must be consistent with the frontmatter tag.
# Phrases below are the load-bearing markers from the CLAUDE.md templates.
AGENT_BLOCK_MARKERS = {
    "never":     "not supported",   # "--agent is not supported"
    "decision":  "Review required", # decision blocks must demand user review
    "synthesis": "runs autonomously",
}

# Paths from the author's personal/secondary repos that must never leak into the
# distributed plugin (an end user only ever has this repo). Fixed in Phase 2/4.
CROSS_REPO_LEAKS = [
    "AI Workflow/",
    "Framework know-how/",
    "docs - product framing/",
]

# The old, broken PRD reference. Canonical is /product/PRD_master.md.
# Matches /product/PRD.md and product/PRD.md but NOT PRD_master.md / PRD_[Domain].md.
STALE_PRD_RE = re.compile(r"(?<![\w_])/?product/PRD\.md")

# Skills whose *function* is to describe/detect the old PRD path (migration skills)
# legitimately contain the stale string as a pattern-to-migrate, not as a live
# reference. They are exempt from the stale-PRD check. Keep this list minimal.
STALE_PRD_EXEMPT = {"pm-audit"}

# NOTE: We do NOT lint for A)/B)/C)/D) option lists. Per CLAUDE.md, A/B/C/D lists
# are the intended *authoring shorthand* in skill bodies; the runtime agent
# converts them to AskUserQuestion at execution time (a universal rule). So their
# presence is by-design, not a defect - flagging it produces pure noise.


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

def repo_root():
    # This file lives in <root>/scripts/, so root is one level up.
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_frontmatter(text):
    """Return (frontmatter_str, body_str). Frontmatter is the block between the
    first two '---' lines. If absent, frontmatter is '' and body is the whole text."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return "", text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return "", text  # unterminated frontmatter -> treat as none


def parse_frontmatter(fm):
    """Minimal parser for this repo's flat frontmatter shape:
        key: value
        metadata:
          subkey: value
    Returns (top_keys: dict, meta_keys: dict). Values kept as raw strings."""
    top, meta = {}, {}
    in_meta = False
    for raw in fm.split("\n"):
        if not raw.strip():
            continue
        if re.match(r"^metadata:\s*$", raw):
            in_meta = True
            continue
        m = re.match(r"^(\s*)([A-Za-z0-9_-]+):\s?(.*)$", raw)
        if not m:
            continue
        indent, key, val = m.group(1), m.group(2), m.group(3).strip()
        if in_meta and len(indent) >= 2:
            meta[key] = val
        elif len(indent) == 0:
            in_meta = False
            top[key] = val
    return top, meta


def strip_quotes(v):
    return v.strip().strip('"').strip("'")


# ----------------------------------------------------------------------------
# Checks
# ----------------------------------------------------------------------------

class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def err(self, where, msg):
        self.errors.append((where, msg))

    def warn(self, where, msg):
        self.warnings.append((where, msg))


def check_skill(name, path, existing_skill_names, rep):
    text = read(path)
    fm, body = split_frontmatter(text)
    where = f"skills/{name}"

    if not fm:
        rep.err(where, "no YAML frontmatter block found")
        return
    top, meta = parse_frontmatter(fm)

    # Required keys present
    for k in REQUIRED_TOP_KEYS:
        if k not in top:
            rep.err(where, f"missing required frontmatter key: {k}")
    for k in REQUIRED_META_KEYS:
        if k not in meta:
            rep.err(where, f"missing required metadata key: {k}")

    # name matches directory
    if top.get("name") and strip_quotes(top["name"]) != name:
        rep.err(where, f"frontmatter name '{strip_quotes(top['name'])}' != directory '{name}'")

    # agent-mode value valid
    mode = strip_quotes(meta.get("agent-mode", ""))
    if mode and mode not in VALID_AGENT_MODES:
        rep.err(where, f"invalid agent-mode '{mode}' (must be synthesis|decision|never)")

    # Required section headings present
    has_agent_block = "## Agent mode" in body
    has_handoff = "## Handoff" in body
    if not has_agent_block:
        rep.err(where, "missing '## Agent mode (`--agent`)' inline block")
    if not has_handoff:
        rep.err(where, "missing '## Handoff' block")

    # agent-mode <-> inline block consistency
    if mode in AGENT_BLOCK_MARKERS and has_agent_block:
        marker = AGENT_BLOCK_MARKERS[mode]
        # Look only inside the agent-mode block (heading to next '## ' heading).
        block = extract_section(body, "## Agent mode")
        if marker.lower() not in block.lower():
            rep.err(where, f"agent-mode is '{mode}' but inline block is missing its "
                           f"marker phrase (expected to contain '{marker}')")
        # A synthesis block that demands review is probably a mislabelled decision.
        if mode == "synthesis" and "review required" in block.lower():
            rep.warn(where, "agent-mode 'synthesis' but block says 'Review required' "
                            "- should this be 'decision'?")

    # related-skills all resolve
    rel = strip_quotes(meta.get("related-skills", ""))
    if rel:
        for r in [x.strip() for x in rel.split(",") if x.strip()]:
            if r not in existing_skill_names:
                rep.err(where, f"related-skills references non-existent skill: {r}")

    # Handoff not wrapped in a code fence (the silent-render-suppression bug)
    if has_handoff and handoff_is_fenced(body):
        rep.err(where, "Handoff block content is wrapped in a ``` code fence "
                       "(suppresses markdown rendering) - remove the fence")

    # Shared content checks (pm-audit is exempt from stale-PRD: it describes the pattern)
    check_common_body(where, text, rep, allow_stale_prd=(name in STALE_PRD_EXEMPT))


def check_command(name, path, rep):
    text = read(path)
    fm, _ = split_frontmatter(text)
    where = f"commands/{name}"
    if not fm:
        rep.err(where, "no YAML frontmatter block found")
    else:
        top, _ = parse_frontmatter(fm)
        if "description" not in top:
            rep.err(where, "missing required frontmatter key: description")
    # Commands are orchestrators - no handoff/agent-mode expected. Only content checks.
    check_common_body(where, text, rep)


def check_common_body(where, text, rep, allow_stale_prd=False):
    """Checks that apply to both skills and commands."""
    # Cross-repo path leaks
    for leak in CROSS_REPO_LEAKS:
        if leak in text:
            rep.err(where, f"cross-repo path leak: '{leak}' - plugin must be self-contained")
    # Stale PRD reference (migration skills that describe the pattern are exempt)
    if not allow_stale_prd and STALE_PRD_RE.search(text):
        rep.err(where, "stale PRD reference '/product/PRD.md' - canonical is /product/PRD_master.md")


def extract_section(body, heading):
    """Return the text from `heading` up to the next '## ' heading (exclusive)."""
    lines = body.split("\n")
    out, capturing = [], False
    for ln in lines:
        if ln.startswith(heading):
            capturing = True
            continue
        if capturing and ln.startswith("## "):
            break
        if capturing:
            out.append(ln)
    return "\n".join(out)


def handoff_is_fenced(body):
    """True if the first non-empty line after '## Handoff' opens a code fence."""
    lines = body.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("## Handoff"):
            for j in range(i + 1, min(i + 5, len(lines))):
                s = lines[j].strip()
                if not s:
                    continue
                return s.startswith("```")
    return False


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main():
    strict = "--strict" in sys.argv
    root = repo_root()
    os.chdir(root)

    skills_dir = os.path.join(root, "skills")
    commands_dir = os.path.join(root, "commands")

    skill_names = sorted(
        d for d in os.listdir(skills_dir)
        if os.path.isdir(os.path.join(skills_dir, d))
    )
    command_names = sorted(
        d for d in os.listdir(commands_dir)
        if os.path.isdir(os.path.join(commands_dir, d))
    )
    existing = set(skill_names)

    rep = Report()

    for name in skill_names:
        path = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(path):
            rep.err(f"skills/{name}", "directory has no SKILL.md")
            continue
        check_skill(name, path, existing, rep)

    for name in command_names:
        path = os.path.join(commands_dir, name, "COMMAND.md")
        if not os.path.isfile(path):
            rep.err(f"commands/{name}", "directory has no COMMAND.md")
            continue
        check_command(name, path, rep)

    # Output
    print(f"Pureinn validator - {len(skill_names)} skills, {len(command_names)} commands checked\n")

    if rep.warnings:
        print(f"WARNINGS ({len(rep.warnings)}) - review, non-blocking:")
        for where, msg in rep.warnings:
            print(f"  [warn] {where}: {msg}")
        print()

    if rep.errors:
        print(f"ERRORS ({len(rep.errors)}) - integrity failures, must fix:")
        for where, msg in rep.errors:
            print(f"  [ERR]  {where}: {msg}")
        print()
        print("FAILED.")
        return 1

    if strict and rep.warnings:
        print("FAILED (--strict: warnings treated as errors).")
        return 1

    print("PASSED - no integrity errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
