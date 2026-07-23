---
name: pm-feature-card
description: Create and manage Feature Cards for individual features (FEAT-ID). In the FDD+SDD framework, Feature Cards are the atomic delivery unit - one card per feature, living in /features/cards/. Cards are created as stubs by pm-features-list, populated in Sections 1-3 by pm-feature-design (JIT), and completed in Section 4 after build. This skill manages the card lifecycle and can create cards manually when needed.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "2.3.0"
  domain: product-management
  triggers: feature card, FEAT-ID, feature spec, feature lifecycle, cards, in design, figma state, security review, mutex tags, delivery plan
  role: specialist
  scope: specification
  output-format: document
  related-skills: pm-feature-design, pm-features-list, pm-stripe, pm-entity-registry
---

# PM - Feature Card


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## What this skill does

Manages Feature Cards in the FDD+SDD framework. A Feature Card is the atomic delivery unit - one card per feature, progressing through a defined lifecycle from initial walkthrough to immutable post-build history.

**Card lifecycle:**

| Status | Meaning | Who sets it |
|---|---|---|
| `1_Backlog` | Stub created, feature defined | pm-features-list (auto) |
| `2_Spec_Done` | JIT spec complete (Sections 1-3 populated) | pm-feature-design |
| `2b_In_Design` | **(optional - frontend features only)** UI / Figma design being created before build | pm-feature-design / designer |
| `3_Ready_to_Build` | Human approved spec (and design, if UI) | Human (Delivery Team) / Human solo confirm |
| `4_In_Build` | Build in progress | pm-stripe |
| `5_In_Review` | Code review in progress | Human / AI guardrail |
| `6_Shipped` | Complete - immutable history | pm-stripe after CI pass |

**`2b_In_Design` is optional and layer-gated.** Only a feature whose `layer` includes `frontend` passes through it (it has a UI to design in Figma). A pure `backend` / `system` feature goes straight `2_Spec_Done → 3_Ready_to_Build` - it has nothing to design. So the path is:
- **frontend feature:** `2_Spec_Done → 2b_In_Design → 3_Ready_to_Build`
- **backend / system feature:** `2_Spec_Done → 3_Ready_to_Build` (skips design)

**This skill handles:**
- Creating stub Feature Cards manually (when not created by pm-features-list)
- Reviewing Feature Card completeness at any status
- Advancing status after human confirmation
- Creating the card template reference

**Section ownership:**
- Frontmatter: pm-features-list (init) + pm-mvp-scope (stripe assignment) + pm-feature-design (status updates)
- Section 1 (Biznis Mantinely): pm-feature-design
- Section 2 (Acceptance Criteria): pm-feature-design
- Section 3 (JIT Technical Design): pm-feature-design
- Section 4 (Realizacny Protokol): pm-stripe (after build)

---

## Dependencies

**Required before creating a stub:**
- Feature must exist in `features/feature_list.md`

**Required before Sections 1-3 are complete:**
- `pm-entity-registry` - entities.md must exist
- `pm-business-rules-library` - business_rules.md and decision_models.md must exist
- `pm-feature-design` - JIT design skill that populates Sections 1-3

**Produces artifacts used by:**
- `pm-feature-design` - reads stub, populates Sections 1-3
- Build skills - read completed Feature Card as implementation spec
- `pm-stripe` - Impact Analysis reads BR-IDs in Section 1

---

## Step 0: Current state check

Check for existing Feature Card at `/features/cards/[FEAT-ID].md`.

| Item | Status | Detail |
|---|---|---|
| Feature Card | [status from frontmatter] | [title] |
| Section 1 (Biznis Mantinely) | [populated / stub] | |
| Section 2 (Acceptance Criteria) | [populated / stub] | |
| Section 3 (JIT Technical Design) | [populated / stub] | |
| Section 4 (Realizacny Protokol) | [populated / pending] | |

**Verdict:** [One sentence - what stage the card is in, what is next]

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Gather inputs (if creating manually)

Used when creating a card that was not auto-created by pm-features-list.

```
Creating Feature Card for: [FEAT-ID]

1. FEATURE REFERENCE
   Feature ID: [FEAT-ID]
   Feature title (FDD format): "[Action] [Result] [Object]"
   Feature Set: [FS-NN: Name]
   From feature_list.md: [confirm feature exists]

2. STRIPE ASSIGNMENT
   Assigned stripe: [stripe-name]
   Priority: [P1 / P2 / P3]
   Dependencies: [FEAT-IDs this depends on, or "none"]

3. PRD REFERENCE
   Which section of PRD covers this feature's business capability?
   [/product/PRD_master.md#section or /product/PRD_[Domain].md#section]

4. FEATURE FLAG
   Flag name (format: domain.feature-name): [name]
   Default: OFF (mandatory in pureinn)
```

---

## Feature Card Template

This is the canonical template for all Feature Cards in the FDD+SDD framework.

```markdown
---
id: FEAT-[DOMAIN]-[NUMBER]
title: "[Action] [Result] [Object]"
status: 1_Backlog
stripe: [stripe-name]
feature_set: "FS-NN: [Feature Set name]"
layer: [one or more of frontend / backend / system - e.g. "backend" or "frontend, backend" for a genuinely cross-layer feature. NEVER "fullstack" - that is not a layer, list the actual layers]
phase: [MVP / MVP+ / Phase 1 / ... or a project's P0 / P1 - the SINGLE axis for MVP membership; IN-MVP = the first / MVP / P0 phase. Never a separate mvp flag]
actor: [User / Host / Admin / System]
owner: unassigned
priority: P1
kano: [Must-be / Performance / Delighter / Indifferent]
vxc: [Quick Win / Big Bet / Fill-in / Time Waster]
estimate: "[S / M / L - informational sizing for roadmap, NOT the atomicity test]"
has_subtasks: false
security_review: none    # none | build | review | both - set by pm-feature-design (Step 1.5 security dimension). Routes secure-code-guardian (build) + security-reviewer (review) in pm-stripe. Stub default: none.
mutex_tags: []           # code modules/files this feature touches - drives delivery-plan CONTENTION (two features sharing a tag can't run parallel). Set at JIT by pm-feature-design (or from real code by pm-reverse-extract/pm-reconcile). Entry: "ModuleName" or {tag: X, reason: "why"}. Empty at stub.
override: false          # break-glass. Set to {reason: "..."} to force a P0 ahead of capacity/priority/contention in the delivery plan (never past a HARD dependency - that's physics). Shown loudly in the plan rationale.
prd_ref: /product/PRD_master.md#[section]
feature_flag: [domain.feature-name]
flag_default: off
---

# Feature Card: {{title}}

---

## Description

[2-3 clear, genuinely orientational sentences - what this feature does, who uses it, and the value/role it delivers. NOT a one-liner restating the title. **MANDATORY for every card regardless of status** (even `1_Backlog` and `6_Shipped`) - this is what a teammate reads first. Never blank or trivial.]

---

## 1. Biznis Mantinely (SDD Input)

*Populated by pm-feature-design (JIT). Links to live registers as source of truth.*

**Rules enforced in this feature:**

| Rule ID | Rule | Priority | Enforcement point |
|---|---|---|---|
| [BR-XXX-001](/domain/business_rules.md#br-xxx-001) | [Rule name: one-line summary] | [Critical/High/Medium] | [Service method / middleware / DB constraint] |

**Entity guard conditions (from entities.md):**

| Entity | Transition | Guard condition |
|---|---|---|
| [Entity Name](/domain/entities.md#entity-name) | [State before] → [State after] | [exact guard expression] |

**Decision model:** [TBL-XXX-01](/domain/decision_models.md#tbl-xxx-01) - [Table name, if applicable]

**What this feature does NOT do:**
- [explicit scope exclusion]

---

## 2. Acceptance Criteria

*Derived from register state + business rules by pm-feature-design. Used for human Black-box testing.*

### AC-01: [Happy Path Name]
- **Given** [precondition: entity state, actor]
- **When** [action]
- **Then** [observable outcome: state change, event emitted, user signal]
  - **And** [secondary outcome]

### AC-02: [Guard Failure Name]
- **Given** [precondition]
- **When** [invalid condition]
- **Then** [system blocks, entity unchanged, error signal]

### AC-03: Feature Flag OFF
- **Given** flag `[feature_flag]` is OFF
- **When** [same trigger as AC-01]
- **Then** [existing behavior unchanged / feature hidden]

---

## Subtasks (helper notes)

*Lightweight nuance / spec helpers for the developer - NOT deliverables, NOT sub-features, they never break the feature's atomicity. Added during pm-feature-design discovery, by the team while writing the card, or folded from too-granular legacy features by pm-reconcile. A subtask that hardens into a testable condition becomes an AC; one that becomes reusable non-negotiable logic becomes a business rule (BR-ID).*

- [ ] [nuance / spec detail - e.g. "reset link expires in 15 min", "reuse existing EmailService", "show skeleton loader while fetching"]

> **Subtask-count signal:** more than ~6-8 subtasks on one card is usually not a detail-rich feature - it is an under-split feature wearing one FEAT-ID. Re-run the atomicity test from `pm-features-list` (one coherent result?) before adding more subtasks; if it fails, split the feature instead of growing the list.

---

## 3. JIT Technical Design (FDD Design)

*Populated by pm-feature-design just before build. Approved during Design Inspection.*

### Data flow and object interaction

```mermaid
sequenceDiagram
    %% Generated by pm-feature-design
    %% [FEAT-ID]: [title]
```

### Files to modify
- [TBD - populated by pm-feature-design]

---

## 4. Realizacny Protokol (Build Verification)

*Populated after successful build and Code Inspection. After 6_Shipped: immutable.*

- **Production code commits:**
  - `[feat: description](commit_hash_link)`

- **Test files:**
  - `tests/unit/[ServiceName]_[FEAT-ID]_spec.[ext]`

- **Feature flag OFF verification:** [yes / no]

- **Code Inspection:** [Approved by [reviewer] on YYYY-MM-DD / AI guardrail passed on YYYY-MM-DD]
```

---

## Notion push

**Runs after Feature Card Section 4 is complete (status: 6_Shipped).**

Read `pureinn-variables.md` key "Feature Backlog" → get DB URL. Find the existing Feature entry for this FEAT-ID.

Update the Feature entry via `notion-update-page`:

| Notion property | Value |
|---|---|
| `Status` | `"6_Shipped"` |
| `Dev Stripe` | `"Stripe N"` (mapped from stripe name in frontmatter - position in delivery plan) |
| `Feature Card URL` | local path to the `.md` file for reference |

Push Feature Card content as the Notion page body.

If Feature Backlog URL is blank in pureinn-variables.md: save locally, remind user to update Notion manually.

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user -->

**Stub (1_Backlog) must have:**
- [ ] All frontmatter fields populated (id, title, status, stripe, owner, priority, prd_ref, feature_flag, flag_default; `security_review: none` placeholder)
- [ ] Sections 1-4 present as stubs (not filled)

**After pm-feature-design (2_Spec_Done) must have:**
- [ ] `security_review` set from the Step 1.5 assessment (no longer the `none` stub default unless genuinely no trigger met)
- [ ] Section 1: entity, state before/after, BR-IDs linked
- [ ] Section 2: at minimum AC-01 (happy path), AC-02 (one guard failure), AC-03 (flag OFF)
- [ ] Section 3: mermaid sequenceDiagram (not empty), files to modify listed

**After build (6_Shipped) must have:**
- [ ] Section 4: at least one commit link, at least one test file path
- [ ] Section 4: flag OFF verification stated
- [ ] Section 4: Code Inspection result with date
- [ ] Status: 6_Shipped

---

## Save to

```
pureinn-workspace/[project-slug]/features/cards/[FEAT-ID].md
```

---

## Handoff

**Čo si teraz má:** Feature Card podľa kanonickej šablóny (frontmatter + sekcie 1-4) - štruktúra pripravená na JIT dizajn.

**Ďalší krok:** `/pm-feature-design [FEAT-ID]` — napĺňa sekcie 1-3 (Biznis Mantinely, ACs, sequence diagram) tesne pred buildom.

**Môžeš preskočiť ak:** Kartu vytvára automaticky `/pm-features-list` alebo `/pm-reverse-extract` - samostatne ju spúšťaj len keď chceš šablónu/referenciu.
