# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What this repository is

The Pureinn product development framework published as a Claude Code plugin. Contains 42 active skills and 2 commands covering the full product lifecycle (FDD+SDD hybrid with JIT per-feature design, intuitive Feature Card lifecycle states, Figma MCP integration, a reconciliation-based Rebuild playbook for onboarding existing products, a pm-audit workspace health check, a re-runnable pm-prioritize backlog engine, and pm-process-flows user-type + process/user-flow mapping).

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

### Path conventions (workspace artifacts)

Two distinct contexts - keep them consistent in every skill:

- **File save locations** (where a skill writes output): full workspace-relative path, no leading slash - `pureinn-workspace/[project-slug]/domain/entities.md`.
- **In-document cross-references** (links between artifacts, e.g. a Feature Card pointing to a rule): workspace-root-relative with leading slash - `[BR-ORD-001](/domain/business_rules.md#br-ord-001)`, `/features/cards/FEAT-ORD-001.md`. The leading slash means "from the project workspace root".

Never use a leading slash for a save location, and always use one for a cross-reference link.

---

## Update and versioning process

### Where to edit

Edit skill files directly in this repo (`skills/[name]/SKILL.md` or `commands/[name]/COMMAND.md`). This is the master copy.

### Versioning rules (semantic versioning)

| Change type | Version bump | Examples |
|---|---|---|
| Bug fix, text correction, clarification | **patch** `1.0.x` | Fixed logic error in pm-feature-design, corrected description |
| New skill, significant skill update, new MCP integration | **minor** `1.x.0` | Added pm-competitive-analysis, updated pm-hypotheses flow |
| Renamed/removed skill, broken workflow change, structural change | **major** `x.0.0` | pm-business-model renamed, skill removed, phase restructure |

### Release process

Every release - in this order:

```bash
# 1. Make your edits to skill/command files

# 2. Run release script (handles version bump + CHANGELOG entry)
./scripts/release.sh patch "Fixed X in pm-feature-design"
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

**CRITICAL RULE - applies to every skill without exception:**
When you encounter A) B) C) D) option lists anywhere in a skill file - whether or not the skill explicitly says "use AskUserQuestion" - you MUST convert them to AskUserQuestion tool calls. NEVER output A/B/C/D options as plain text. This rule overrides everything else.

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

## Skill PREREQ block (universal standard)

Every skill that requires external input (research, documents, user data) MUST open with a prerequisite check. The goal is never to block - it is to assess and route.

**PREREQ check structure:**

1. State what the skill needs to produce its best output
2. Ask what the user has available
3. Route based on the answer:

| User has | Action |
|---|---|
| Full input ready | Proceed normally |
| Partial input | Proceed with what's there, surface gaps as assumptions |
| No input | Offer informed assumptions via AskUserQuestion, proceed with confirmed assumptions |

**Graceful degradation - when user has no data:**

Never block. Never say "go collect data first and come back." Instead:

1. State what you would normally expect as input
2. Based on context already available (product type, industry, prior intake answers), form 3-4 concrete assumptions
3. Surface them via AskUserQuestion with a recommended option
4. Proceed based on confirmed assumptions
5. Mark all assumptions in output as `[ASSUMED - replace when real data available]`

Output with explicit assumptions is better than no output. The user can substitute real data later.

**"Bring your data" skills** (pm-market-analysis, pm-personas, pm-domain-analysis, jtbd-building, etc.) always offer two paths:
- **Path A** - user has research: structure and formalize it
- **Path B** - user has nothing: AI-powered elicitation or guided AskUserQuestion assumptions

Never tell the user to go do research and return. Offer Path B immediately.

---

## Skill handoff block (universal standard)

Every skill MUST end with an explicit handoff block. No exceptions. This is not a summary of what was done - it is a forward-looking routing signal.

**Format:**

```
---
**Co si teraz má:** [1 veta - konkrétna hodnota tohto artefaktu]

**Ďalší krok:** `/[skill-name]` — [jeden dôvod prečo práve tento]
Alebo spusti `/pureinn` pre phase gate check.

**Môžeš preskočiť ak:** [konkrétna podmienka kedy nasledujúci skill nepridáva hodnotu]
```

**Rules:**
- "Čo si teraz má" is about value, not content. Not "you have a document" but "you can now [do X / decide Y / proceed with Z]"
- The next skill must be the highest-ROI move from the user's current position, not just the next in sequence
- Skip suggestion must have a concrete condition. "If [X], then [skill] adds no value because [Z]." Never vague.
- If there is genuinely no valid skip condition, omit the skip line entirely

---

## Impact over Activity principle

Pureinn does not generate files for their own sake. Every skill run must produce something that moves the project forward. This principle is active - it requires judgment at runtime, not just documentation.

**Four operational rules:**

**1. Context fit check** - Before generating, a skill must evaluate whether it applies to this specific context. If it is low-value for this user and situation, surface it proactively before generating anything:
```
Pre [context] je /[skill] pravdepodobne nízka hodnota pretože [reason].
Pokračovať napriek tomu, alebo preskočiť na [next relevant skill]?
```

**2. Depth over breadth** - Fewer high-confidence sections beat many thin placeholder sections. If a section cannot be filled with real information, either omit it or mark it explicitly as `[TODO - insufficient input]`. Never generate content to fill space.

**3. Highest-ROI next step** - The handoff always routes to the highest-impact next move, not the mechanically next skill. Sometimes the right next step is "talk to 3 customers" not "run the next skill."

**4. Skip_if conditions** - Skills that are conditionally low-value must define their skip condition explicitly. Built-in examples:
- `/pm-stakeholder-map`: Skip if solo builder with no external investors or board
- `/pm-comms-charter`: Skip if solo builder (no team to communicate with)
- `/pm-team-roster`: Skip if solo builder
- `/pm-pitch-deck`: Skip if not raising capital and not pitching to partners
- `/pm-feature-viability`: Skip if feature is already scoped, committed, or in a validated roadmap

The orchestrator (`/pureinn`) surfaces these conditions proactively during phase routing.

---

## Adaptive execution - agile, not waterfall (universal standard)

Every skill runs as an **adaptive, returnable step in an agile loop** - never as a fixed waterfall stage. This governs both how skills are written and how they execute at runtime. Four properties, required of every skill:

1. **Situation-aware + proactive.** A skill detects the current state and adapts - it does not assume a fixed entry point or run a fixed script. When the user does not know, or the document/context is thin, the skill becomes a **proactive partner**: it analyses what it has, **formulates concrete candidate assumptions**, and probes via **AskUserQuestion** to close the gap and reach the goal *together*. It never stalls on missing input. (This is the active form of the PREREQ graceful-degradation and "Handling I don't know" patterns above.)
2. **Offer, don't impose.** When there is a meaningful choice - which method to use, what scope, whether to act now - the skill **offers** it (asks + proposes options with a recommended one and the reasoning) rather than silently auto-executing a default. Example: prioritization is offered with a basis-selection, not auto-applied.
3. **Re-runnable + returnable.** Artifacts are living, not write-once. Returning to a skill **iterates and updates** - it does not start over destructively. Any skill can be revisited as new information arrives.
4. **Sequence is a default, not a mandate.** The phase/skill order is a suggested path; move between skills as the situation demands. The only hard constraints are the few **intentional gates** (Phase 3a Go/No-Go, Phase 6 Design Inspection) that exist to prevent compounding, uncorrectable waste - agile does not mean removing those.

When writing or updating any skill, check it against these four. A skill that auto-executes without offering, or that cannot be re-run without damage, violates this standard.

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
