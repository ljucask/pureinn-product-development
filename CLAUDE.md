# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What this repository is

The Pureinn product development framework published as a Claude Code plugin. Contains 35 active skills and 2 commands covering the full product lifecycle (v3.x: FDD+SDD hybrid with JIT per-feature design).

**Plugin repo is the master copy.** The `AI Workflow/.claude/commands/` folder in the personal framework repo is secondary. Always edit here first.

---

## Repository structure

```
.claude-plugin/
  plugin.json       - Package metadata (name, version, author, paths)
  marketplace.json  - Marketplace registration metadata
commands/
  pureinn/          - Main orchestrator (entry point, routing, exit gates)
  pureinn-resume/   - Resume paused project
skills/
  [skill-name]/
    SKILL.md        - Skill content + frontmatter (name, description, triggers, metadata)
scripts/
  release.sh        - Versioning + CHANGELOG automation (run before every release)
assets/
  pureinn-banner.png
README.md           - Public-facing documentation
FRAMEWORK_GUIDE.md  - Detailed playbook and skill reference
CHANGELOG.md        - Version history
```

---

## Update and versioning process

### Where to edit

Edit skill files directly in this repo (`skills/[name]/SKILL.md` or `commands/[name]/COMMAND.md`). This is the master copy.

### Versioning rules (semantic versioning)

| Change type | Version bump | Examples |
|---|---|---|
| Bug fix, text correction, clarification | **patch** `1.0.x` | Fixed logic error in pm-brd, corrected description |
| New skill, significant skill update, new MCP integration | **minor** `1.x.0` | Added pm-competitive-analysis, updated pm-hypotheses flow |
| Renamed/removed skill, broken workflow change, structural change | **major** `x.0.0` | pm-business-model renamed, skill removed, phase restructure |

### Release process

Every release - in this order:

```bash
# 1. Make your edits to skill/command files

# 2. Run release script (handles version bump + CHANGELOG entry)
./scripts/release.sh patch "Fixed X in pm-brd"
./scripts/release.sh minor "Added pm-competitive-analysis skill"
./scripts/release.sh major "Renamed pm-business-model to pm-revenue-model"

# 3. Review the changes the script made (plugin.json, marketplace.json, CHANGELOG.md)

# 4. Commit and push
git add .
git commit -m "Release vX.Y.Z - [summary]"
git push
```

Never push a release without bumping the version. Users will not receive updates unless the version changes.

### Adding a new skill

1. Create `skills/[skill-name]/SKILL.md` with proper frontmatter:
```yaml
---
name: skill-name
description: Use when...
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: keyword1, keyword2, keyword3
  role: specialist
  scope: [analysis|specification|planning|research|validation|documentation]
  output-format: document
  related-skills: skill-a, skill-b
---
```
2. Reference the skill in `FRAMEWORK_GUIDE.md` under the correct phase
3. Add it to the skill map in `README.md`
4. Run `./scripts/release.sh minor "Added [skill-name]"`

### Updating an existing skill

1. Edit `skills/[skill-name]/SKILL.md`
2. If logic/flow changed significantly: bump `version` in the skill's own frontmatter metadata too
3. Run `./scripts/release.sh patch "Updated [skill-name]: [what changed]"` (or minor if substantial)

---

## Skill question pattern (universal standard)

When a skill needs to ask the user questions before producing an artifact, use the **grouped question pattern**:

1. Group related questions naturally (typically 2-4 per group, max 3 groups)
2. Ask all questions in the group together in one turn
3. After receiving answers, output a summary: "Here's what I understand - is this correct?"
4. Wait for confirmation. If user corrects something, update and re-confirm.
5. Move to the next group only after confirmation.
6. After the final group, show a complete summary before proceeding to artifact generation.

**When to apply:**
- >4 questions total: group them (2-3 groups), confirmation after each group
- 3-4 questions total: one group with one confirmation before proceeding
- 1-2 questions: ask directly, no grouping needed

**How to ask questions within a group:**

**Option-based questions (A/B/C/D choices): ALWAYS use the `AskUserQuestion` tool - never output them as plain text.**
- Max 4 options per question, max 4 questions per AskUserQuestion call
- Use `multiSelect: true` only when the user can legitimately pick multiple options (e.g. "which phases apply?")
- Keep option labels concise (1-5 words), use the description field for context and trade-offs
- Within one group: ask plain-text free-text questions first, then follow with AskUserQuestion for option-based questions

**Recommended option rule:**
Every AskUserQuestion call with options MUST have a recommended option, marked with "(Recommended)" at the end of the label. The recommended option is NOT the easiest or most common default - it is the option with the highest ROI given what the user is building and where they want to end up. Reason from their goal backwards: which path gets them to the outcome they described most directly, with the least waste? If two options are genuinely equivalent, mark neither - but that is rare. Never recommend an option just because it is simpler. Simpler is a trade-off, not a virtue.

**Free-text questions (open-ended):** Ask as plain text, one at a time.
- Do NOT add fake A/B/C/D options to questions that are genuinely open-ended (descriptions, priorities, constraints, names)
- This applies to: product name, problem description, custom values, anything requiring original user input

**Proactive assumption surfacing:**
Do not wait until the end to surface assumptions. Surface them at the moment they enter a decision - inline, before generating any section that depends on them. Format:

```
Assumption: [what I am assuming and why]
If this is wrong, tell me - it affects [what specifically].
```

Surface assumptions when: inferring something not explicitly stated, applying a default that might not fit their context, or proceeding despite missing input. Do not surface trivial or obvious assumptions - only ones that could meaningfully change the output.

**Handling "I don't know" / user is stuck:**

When a user responds to any question with "I don't know", "not sure", "help me", "you decide", "I have no idea", or any signal that they're stuck or uncertain:

1. **Never leave them without guidance.** Immediately pivot to proactive help.
2. **Analyze context first**: based on what you already know about their product, industry, or problem, form 3-4 concrete assumptions or candidate answers.
3. **State your reasoning explicitly**: "Based on [what you told me about X], here are the most likely options:"
4. **Use AskUserQuestion tool** to offer the structured options - turn the open-ended question into a guided choice. Apply the Recommended option rule above.
5. **Always include an "Other / I'll describe" option** so they're never locked in.
6. If no context is available yet (very first question), ask one targeted clarifying question as plain text to gather enough signal, then offer options.

This applies universally at any point in any skill - not just formal intake questions. If a user hesitates, is vague, or asks for a recommendation, stop and help them think it through before continuing.

**Summary block format:**
```
Here's what I understand:
- [key point]
- [key point]
- [key point]

Is this correct, or anything to adjust before we continue?
```

This pattern applies to all skills: intake rounds, discovery sessions, validation checks. Never dump all questions at once without a confirmation loop.

---

### Renaming or removing a skill

This is a major version change - existing users may have workflows referencing the old name.

1. Rename/remove the file
2. Update all references in `FRAMEWORK_GUIDE.md` and `README.md`
3. Add a migration note in `CHANGELOG.md` under Breaking Changes
4. Run `./scripts/release.sh major "[Old-skill] renamed to [new-skill]"`

---

## Installation

```bash
/plugin marketplace add ljucask/pureinn-product-development
/plugin install pureinn-product-development@pureinn-product-development
```

Select **user scope** for global availability across all projects.

## Updating (for end users)

```bash
/plugin update pureinn-product-development@pureinn-product-development
```
