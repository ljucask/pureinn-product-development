# Testing & integrity

How to keep the framework internally consistent when using, extending, or fixing it.
There are two layers: an **automated validator** (deterministic, runs in seconds) and a
**manual scenario protocol** (behavioural, run by a human when making significant changes).
Each covers what the other cannot.

---

## Layer 1 - Automated validator (deterministic)

A structural linter that checks every skill and command against the house standards in
`CLAUDE.md`. It does **not** run skills - it checks their *form*, which is where silent
regressions hide (a broken cross-reference, a mislabelled block, a leaked path).

### Run it

```bash
./scripts/validate.sh            # exit 1 on any integrity error
./scripts/validate.sh --strict   # also exit 1 on warnings
```

It runs automatically inside `./scripts/release.sh` before the version bump, so a release
can never ship a repo that fails validation.

### What it checks (ERRORS - block release)

| Check | Catches |
|---|---|
| Frontmatter completeness | A skill missing `name`/`description`/`license` or any required `metadata.*` key |
| `name` == directory | A renamed skill whose frontmatter wasn't updated |
| `agent-mode` valid | A value that isn't `synthesis` / `decision` / `never` |
| Required blocks present | A skill missing its `## Agent mode (\`--agent\`)` or `## Handoff` block |
| agent-mode ↔ inline block | A `decision` skill whose block doesn't demand review; a `never` block that doesn't say "not supported"; a `synthesis` block missing its marker |
| `related-skills` resolve | A reference to a skill that doesn't exist (typo, or a removed/renamed skill) |
| Handoff not code-fenced | The silent-render bug: a `## Handoff` block wrapped in ` ``` ` (suppresses bold/links) |
| No cross-repo path leaks | A path into a non-distributed personal repo (`AI Workflow/`, etc.) - the plugin must be self-contained |
| No stale PRD path | `/product/PRD.md` (canonical is `/product/PRD_master.md`); `pm-audit` is exempt because it describes the pattern |

### What it checks (WARNINGS - review, non-blocking)

- A `synthesis` skill whose agent-mode block says "Review required" (likely a mislabelled `decision`).

### What it deliberately does NOT check (and why)

Being honest about the boundary matters more than a false sense of coverage:

- **Skill counts** - `release.sh` already auto-syncs the "N active skills" strings across
  `plugin.json` / `marketplace.json` / `README.md` / `CLAUDE.md`. Duplicating that here would
  fight the auto-fix.
- **A)/B)/C)/D) option lists** - these are the intended *authoring shorthand*; the runtime
  agent converts them to `AskUserQuestion` at execution time (a universal `CLAUDE.md` rule).
  Their presence is by-design, so flagging it is noise.
- **Whether the logic is any good** - the validator confirms a skill is well-*formed*, not that
  its reasoning helps the user. That is Layer 2.
- **Runtime behaviour** - routing, resume, `--agent`, the JIT cycle. A prose/LLM framework has no
  deterministic PASS/FAIL for behaviour; asserting it would need an LLM judge, which is itself
  unreliable and costs money per run. That is Layer 2, done by hand.

---

## Layer 2 - Manual scenario protocol (behavioural)

Run these by hand after any **significant** change to routing, state handling, the lifecycle, or
a skill's flow. They are not automated on purpose - each needs a live session and a human read of
whether the behaviour was right. Small copy/text edits don't need this; structural changes do.

Do each scenario in a throwaway workspace (a scratch directory, **never** a real product), watch
the actual behaviour, and confirm the expected outcome.

### S1 - New project (Greenfield entry)
`/pureinn <a product idea>` → expect: intake, a scaffolded `pureinn-workspace/<slug>/`, a written
`state.json`, and routing into Phase 1. Confirm the phase dashboard reflects an empty project.

### S2 - Resume
After S1, in a fresh session: `/pureinn-resume <slug>` (and bare `/pureinn-resume` to list projects)
→ expect: `state.json` restored, current phase re-derived, dropped back into the right dashboard.
Confirm feature status is re-derived from `features/cards/` frontmatter, **not** trusted from a stale
state.json mirror.

### S3 - Stage-keyword entry
`/pureinn model` (and `define` / `discover` / `validate` / `plan` / `build`) → expect: scaffolds a
workspace if none exists, then jumps straight into that stage. Confirm no dead-end and no reference
to a missing skill.

### S4 - Agent mode (`--agent`)
Run one `synthesis` skill and one `decision` skill with `--agent` on heavy inputs → expect: the
subagent drafts from existing inputs and returns a compact summary; missing inputs are marked
`[ASSUMED - ...]`, never invented. Confirm the `decision` skill requires review before its artifact
is treated as final, and a `never` skill refuses `--agent` and warns once.

### S5 - JIT stripe cycle
Take one feature through `pm-stripe` → `pm-feature-design` → build, then resume mid-cycle → expect:
lifecycle status advances correctly (`2_Spec_Done` → design inspection → `3_Ready_to_Build` → ...),
the design-inspection gate actually blocks `4_In_Build` until the spec passes, and the WIP guard
blocks a second active feature in the same stripe.

### S6 - The two hard gates
Confirm neither can be skipped: Phase 3a Go/No-Go cannot be bypassed with FORCE; Phase 6 Design
Inspection is a real routing step, not just prose.

### S7 - Rebuild playbook
On an existing (synthetic) codebase: `pm-reverse-extract` / `pm-reconcile` → expect: the 4 live
registers + feature inventory generate in **current** conventions (canonical statuses, single `phase`
axis, `prd_ref: /product/PRD_master.md`), and a following `pm-audit` finds zero drift.

---

## Contributor checklist - adding or editing a skill

Before you commit a skill change, in order:

1. **Frontmatter** - all required keys present; `name` matches the directory; `agent-mode` is one of
   `synthesis` / `decision` / `never` and matches the skill's real nature.
2. **Blocks** - the `## Agent mode (\`--agent\`)` inline block matches the frontmatter tag; the
   `## Handoff` block exists, is **not** code-fenced, and routes to the highest-ROI next step.
3. **References** - every `related-skills` entry and every in-body skill/path reference resolves.
   Use `/product/PRD_master.md`, never `/product/PRD.md`. No paths outside this repo.
4. **Run `./scripts/validate.sh`** - it must pass with zero errors.
5. **If you changed routing, state, the lifecycle, or a skill's flow** - run the relevant Layer 2
   scenario(s) above in a throwaway workspace.
6. **Release** via `./scripts/release.sh` (it re-runs the validator and syncs counts) - see `CLAUDE.md`.

If the framework ever grows a fixture-based harness that runs skills automatically, scenarios S1-S7
are the natural first cases to encode.
