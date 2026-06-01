---
description: Resume a paused Pureinn project. Reads state.json, restores full project context, checks artifact completion, and drops you back into the current phase dashboard. Faster than re-running /pureinn. Omit slug to list all available projects.
argument-hint: "[project-slug]"
---

# Pureinn - Resume Project

## Input

$ARGUMENTS

If $ARGUMENTS is empty: list available projects and ask which to resume.
If $ARGUMENTS is a valid slug: load that project directly.

---

## STEP 1 - Project Identification

**If no argument provided:**

Scan `pureinn-workspace/` for subdirectories containing `state.json`.

```
Available projects:

  [slug]  -  [project name]  |  Phase [N] - [phase name]  |  Last active: [created date]
  [slug]  -  [project name]  |  Phase [N] - [phase name]  |  Last active: [created date]

Which project do you want to resume? (type the slug)
```

If no projects found:
```
No existing projects found in pureinn-workspace/.

To start a new project, run /pureinn [product idea or name].
```

**If slug provided:** Skip the list. Go directly to Step 2.

---

## STEP 2 - Load State

Read `pureinn-workspace/[slug]/state.json`.

If the file does not exist or cannot be read:
```
Could not find state.json for project "[slug]".

Check the slug is correct, or run /pureinn to start a new project.
```

Parse all fields:
- `project`, `slug`, `playbook`, `guidance_mode`
- `starting_phase`, `current_phase_index`, `current_phase_name`
- `phases_completed`, `phases_skipped`
- `product_shape`, `team_structure`
- `assessment_file`

---

## STEP 3 - Restore Context Banner

Show immediately after loading state:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUMING: [project name]
PLAYBOOK: [Greenfield / Feature / Rebuild]
GUIDANCE: [On / Off]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Product type:      [type from product_shape]
Audience:          [audience from product_shape]
Platform:          [platform_strategy from product_shape]
Business model:    [business_model from product_shape]
Team:              [team_structure]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

If `assessment.md` exists at `pureinn-workspace/[slug]/assessment.md`, read it silently to rebuild product understanding. Do not display it - use it as background context for all guidance and suggestions.

---

## STEP 4 - Artifact Check

Scan `pureinn-workspace/[slug]/artifacts/` to see what has actually been produced. Compare against what the completed phases in `state.json` should have produced.

**If artifacts are present and consistent with state.json:** proceed silently to Step 5.

**If there are gaps** (state says phase is complete but expected artifacts are missing):

```
State says Phase [N] is complete, but I don't see these expected artifacts:

  - [artifact name] (expected in phase-N/)
  - [artifact name]

Options:
  A) Proceed anyway - I have the outputs, just not in this directory
  B) Re-open Phase [N] and complete the missing artifacts
```

Wait for user choice before proceeding.

**Artifact expectation map** (what each phase should produce):

| Phase | Expected artifacts |
|---|---|
| Phase 1 | artifacts/phase-1-foundation/project-charter.md (solo); + team-roster.md, comms-charter.md (small team); + stakeholder-map.md (full team/corporate) |
| Phase 2 | artifacts/phase-2-discovery/: tech-feasibility.md, domain-analysis.md, market-analysis.md, personas.md, jtbd-analysis.md, problem-validation.md |
| Phase 3 | artifacts/phase-3-define/: design-thinking-synthesis.md, north-star-metric.md, aarrr-metrics.md, okrs.md, business-case.md, product-roadmap-v1.md + product/PRD_master.md |
| Phase 4 | artifacts/phase-4-domain/: domain-model.md, pii-inventory.md, privacy-requirements.md, gdpr-action-plan.md, product-roadmap-v2.md + domain/entities.md, domain/business_rules.md, domain/decision_models.md |
| Phase 5 | artifacts/phase-5-planning/: mvp-scope.md, delivery-stripes.md, product-roadmap-v3.md + features/feature_list.md + features/cards/FEAT-*.md (stub cards) |
| Phase 6+7 (per Feature) | Feature Card Sections 1-3 complete (features/cards/FEAT-*.md status: 3_Design_Inspection_Passed or higher) |

---

## STEP 5 - Dashboard

Display the full project dashboard:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT: [product name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE STATUS
  Phase 1 - Foundation & Collaboration        [✅ Done / ⏭ Skipped / 🔲 To do / ⚠️ Incomplete]
  Phase 2 - Ideation & Discovery              [...]
  Phase 3 - Define & Validation               [...]
  Phase 4 - Domain Modeling + Register Setup  [...]
  Phase 5 - Feature Planning                  [...]
  Phase 6 + 7 - Delivery Cycle (JIT)         [...]

CURRENT: Phase [N] - [Phase Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Status logic:**
- `phases_completed` array → ✅ Done
- `phases_skipped` array → ⏭ Skipped
- `current_phase_index` → current (no marker - shown separately as CURRENT)
- Phases after current → 🔲 To do
- State says done but artifacts missing → ⚠️ Incomplete (from Step 4 check)

---

## STEP 6 - Phase Queue

If guidance mode is ON, show phase context before the queue:

```
PHASE [N] - [PHASE NAME]
[2-3 sentences: what this phase achieves, what the output is, why it matters
for what comes next. Tailored to this specific project - reference the product
and what was learned in previous phases.]
```

Then always show the skills queue for the current phase:

```
SKILLS FOR THIS PHASE

  1. /[skill-name]
     → Produces: [artifacts]
     → Input needed: [what to prepare]
     [✅ Done / 🔲 To do]

  2. /[skill-name]
     → Produces: [artifacts]
     [✅ Done / 🔲 To do]

  [👤 Human activity: [description]]
     → Before running /[next-skill]

  3. /[skill-name]
     → Produces: [artifacts]
     [🔲 To do]
```

Mark skills done if their output artifact exists in the artifacts directory.

After the queue:
```
Run /pureinn [slug] after completing this phase to run the exit gate and advance.
```

---

## STEP 7 - Options

After displaying the dashboard and queue, always offer:

```
What do you want to do?

  A) Continue from where I left off - run the next skill
  B) Review what was produced in a previous phase
  C) Something specific: [describe]
```

**If B:**
```
Which phase do you want to review?
  [List completed phases with short artifact summary]
```

After user selects: read and summarize the key artifacts from that phase. Identify anything that looks thin or outdated given what was learned later. Ask:
```
Do you want to update any of these, or continue to Phase [current]?
```

**If A or C:** route accordingly without further questions.

---

## Guidance Mode Toggle

If the user mentions wanting to change guidance mode during the session:

```
Toggle guidance mode?
  Current: [On / Off]

  A) On  - explain the why behind each phase and skill
  B) Off - just route me, no explanations
```

On change: update `guidance_mode` in state.json immediately.

---

## Exit Gate (if user says a phase is complete)

If the user states the current phase is done, or runs /pureinn-resume after announcing completion:

Run the exit gate using thresholds from the playbook file:
`Framework know-how/Upstream activities - Playbooks/Playbook [playbook].md`

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXIT GATE - Phase [N]: [Phase Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Quantitative thresholds from playbook - Phase [N] exit criteria]

| Criterion | Required | Status |
|---|---|---|
| [e.g., ≥10 customer interviews] | Yes | ✅ Met / ❌ Not met / ? Unknown |

Did you meet each criterion? (confirm, correct, or mark unknown)
```

If all critical criteria met:
```
Exit gate passed.

Type GO to advance to Phase [N+1].
```

If criteria not met:
```
Exit gate not passed. Unmet conditions:
  ❌ [Condition] - [what's missing]

  A) Go back and address the gaps
     Recommended: [skills that address the gap]
  B) Proceed anyway - I acknowledge the risk (FORCE)
```

On GO or FORCE:
1. Add current phase to `phases_completed` in state.json
2. Advance `current_phase_index` and `current_phase_name`
3. Show the dashboard for the next phase

---

## Phase 6-7 Handling (JIT Delivery mode)

When `current_phase_index` is 6 or 7, show a Stripe-level view instead of a generic phase list.

Read `current_stripes` array from state.json. Read `features/feature_list.md` for feature status.

**If stripes are active:**

Scan `features/cards/` directory. Group Feature Cards by stripe. Show status from frontmatter.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROJECT: [product name]    PHASE 6+7 - JIT DELIVERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRIPE STATUS (from features/cards/ frontmatter)
  [stripe-name]
    Active:  FEAT-[ID] - [title]  [status]
    Queue:   FEAT-[ID] - [title], FEAT-[ID] - [title]
    Done:    [N] features Promoted

  [stripe-name]
    Active:  FEAT-[ID] - [title]  [status]
    Queue:   FEAT-[ID] - [title]

REGISTERS (from domain/)
  entities.md           [✅ initialized / ❌ missing]
  business_rules.md     [✅ initialized / ❌ missing]
  decision_models.md    [✅ initialized / ❌ missing]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Run /pm-stripe for full Stripe dashboard and feature routing.
```

**If no stripes are active yet:**
```
You're in Phase 6+7 but no active Stripe is set.
Run /pm-stripe to see the stripe dashboard and advance the first feature.
```

---

## Behavioral Rules

- Read assessment.md silently on load. Use it as background context - do not display it unless asked.
- Do not re-run intake questions. The product is already defined.
- Do not re-run document scan. State is already established.
- Guidance is restored from state.json - do not ask again unless user requests toggle.
- For Phase 6-7: show Stripe-level view (above). Individual feature status lives in Notion, not in state.json.
- Always persist state changes to state.json immediately - never defer writes.
- If state.json is outdated (missing fields like `product_shape`, `current_stripes`, or `registers`): fill with defaults and continue without blocking.
