---
name: pm-reverse-extract
description: Migration path skill for products built outside the framework. Reads existing codebase, docs, and Feature Cards (if any) to extract the full feature inventory. Outputs feature_list.md (Live Register 4, FEAT-[DOMAIN]-NNN IDs) + stub Feature Cards in features/cards/ + Notion push. Run after pm-entity-registry and pm-business-rules-library have initialized the domain registers. Run instead of pm-features-list + pm-mvp-scope for existing products.
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "2.0.0"
  domain: product-management
  triggers: reverse extract, existing product, feature inventory, migration path, feature implementation onboarding, sync Notion
  role: specialist
  scope: extraction
  output-format: document
  related-skills: pm-entity-registry, pm-business-rules-library, pm-feature-design, pm-stripe
---

# PM - Reverse Extract (Existing Product Sync)


## Agent mode (`--agent`)

Podporuje `--agent`: beží autonómne v subagentovi, nadraftuje artefakt z existujúcich vstupov, vráti krátky súhrn + coverage note.

- **Bez flagu** → interaktívne (default); pri ťažkých vstupoch ponúkni agent režim.
- **`--agent`** → poslúchni. Najprv over úplnosť vstupov. Čo chýba: NEVYMÝŠĽAJ - označ `[ASSUMED - čo/prečo]` vo výstupe aj v súhrne. Nikdy nehalucinuj medzeru.

---

## What this skill does

Extracts the full feature inventory from an existing product and formalizes it into the FDD+SDD framework.

**Run order for migration path:**
1. `/pm-entity-registry` - extracts entities and state machines → `domain/entities.md`
2. `/pm-business-rules-library` - extracts business rules → `domain/business_rules.md` + `domain/decision_models.md`
3. `/pm-reverse-extract` (this skill) - extracts feature inventory → `features/feature_list.md` + stub Feature Cards

**Produces:**
1. `feature_list.md` (Live Register 4) - full feature inventory in FDD format with FEAT-[DOMAIN]-NNN IDs
2. Stub Feature Cards in `features/cards/` - one per feature, status: `1_Backlog`
3. Delivery Stripe assignment - which features go into which domain stripe
4. Notion push - Feature hierarchy pushed to Product Features database

**Claude reads directly:** codebase, existing docs, API specs, route files, controller files. This skill structures what Claude already knows - it does not hallucinate features.

Can be re-run at any point to re-sync Notion after significant state changes.

**Reconciled mode (when run by pm-reconcile):** If `reconcile/reconciliation_report.md` exists, it is the authoritative input. Derive features from the reconciled code reality, map the old feature names as aliases, include code-only features from the report, and do NOT create cards for doc-only / not-implemented items (those are backlog). Do not re-question what the report already settled.

---

## What this skill does NOT do

- Initialize domain registers - run pm-entity-registry and pm-business-rules-library first
- Run KANO Analysis or Value vs. Complexity - not applicable to features already built
- Write Feature Card Sections 1-3 (JIT design) - that is pm-feature-design, run just before build
- Run discovery or validation - this is a sync operation, not a new product workflow

---

## Dependencies

**Required before running:**
- `/pureinn` already run - workspace, state.json, and pureinn-variables.md must exist
- `domain/entities.md` - pm-entity-registry must have run (entities define domain codes for FEAT-IDs)
- At least one source accessible: existing docs (old FSD/BRD/specs), Feature Cards, codebase route/controller files

**Produces artifacts used by:**
- `pm-feature-design` - JIT design reads feature_list.md for feature context
- `pm-stripe` - stripe dashboard reads feature_list.md and Feature Card frontmatter
- Notion Product Features database - primary operational view for the team

---

## Step 0: Current state check

Check for existing artifacts:
- `domain/entities.md` - needed for domain code assignment
- `features/feature_list.md` - was this skill already run?
- `features/cards/` - any existing Feature Cards?

Also check what source material is available:
- Old spec documents (any format: FSD, BRD, PRD, user stories, Confluence pages)
- Existing Feature Cards
- Codebase: route files, controller files, API spec, schema files, test files

Show state table. Use AskUserQuestion to confirm mode and scope before proceeding.

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Gather inputs

Use AskUserQuestion for structured choices. Gather via text prompt:

```
Migration path setup - I need a few inputs before extracting the feature inventory.

1. PRODUCT AND PROJECT
   Product name and project slug (lowercase, hyphens, e.g., acme-rentals):
   [answer]

2. SOURCE MATERIAL
   What should I read to extract features? Confirm which is accessible:
   - Existing spec docs (FSD/BRD/PRD/Confluence/Notion) - paste paths or "in context"
   - Codebase - confirm accessible and key directories (e.g., src/features/, app/controllers/)
   - Existing Feature Cards - confirm accessible
   [answer]

3. CURRENT STATE
   Which features are live in production?
   Which are in progress?
   Which are planned but not started?
   (rough description is fine - I will map to statuses)
   [answer]

4. NEXT PRIORITY
   What do you want to build next?
   This determines which features/domains get JIT design first.
   [answer]

5. NOTION
   Do you have a Notion Product Features database?
   URL (or "skip - markdown only"):
   [answer]
```

---

## Step 2: Extract feature inventory

### 2a. Read source material

Read in priority order:
1. Existing Feature Cards - richest source, already in FDD format
2. Spec docs (FSD/BRD/PRD) - flow step tables and acceptance criteria reveal features
3. Codebase route/controller files - define what the system actually does
4. API spec or schema files - complement for data-layer features
5. Test files - test descriptions often enumerate features precisely

### 2b. Extract and format features

For each feature found:
- Rename to FDD format: `<Verb> <object>` (e.g., "booking creation" → "Submit booking request")
- Assign domain code from entities.md: which entity does this feature primarily affect?
  - Domain code comes from entity domain (e.g., Order entity → ORD, Payment → PAY, User → USR)
  - New domain with no entity → assign a descriptive code (e.g., NTF for notifications, SRC for search)
- Assign FEAT-[DOMAIN]-NNN ID (sequential per domain, start from 001)
- Determine status: Done / In Progress / Planned / Unclear
- Identify actor: who initiates or benefits from this feature
- Note spec coverage: does a Feature Card exist? Any spec doc section?

### 2c. Derive Delivery Stripe assignment

Group features into domain-focused Delivery Stripes:
- Each stripe = one primary domain (e.g., "Order Flow", "Payment", "User Auth")
- Features from the same domain go into the same stripe
- Cross-domain features go to the stripe that owns the primary entity

Done features: assign to their natural stripe with status = Promoted
In Progress features: assign as Active in their stripe
Planned features: assign to Queue in their stripe

### 2d. Identify what needs JIT design before next build

Flag features that are:
- Status: In Progress or Planned AND
- No Feature Card Sections 1-3 exist

These are the highest-priority candidates for pm-feature-design before the next stripe starts.

---

## Step 3: Generate artifacts

Generate in English.

---

### ARTIFACT 1: Feature List (Live Register 4)

Save to: `pureinn-workspace/[project-slug]/features/feature_list.md`

```markdown
# FDD Feature List - [Product Name]
# Live Register 4 of 4 - FDD+SDD Framework

> **Product:** [Product Name]
> **Version:** 1.0 (migration extract)
> **Last updated:** [date]
> **Source:** Reverse extract from existing product
> **Maintained by:** pm-reverse-extract (init) + pm-features-list FI Append (new initiatives)

---

> **How to read this register:**
> - FEAT-[DOMAIN]-NNN format: domain code matches entity domain in entities.md
> - Status: Done = live in production | In Progress = being built | Planned = backlog | Unclear = needs investigation
> - Spec coverage: Feature Card exists? Sections 1-3 complete? (needed before build)

---

## [Domain Name] (FEAT-[DOMAIN]-*)

### FEAT-[DOMAIN]-001: [Feature Name]
**Description:** [1-2 clear, orientational sentences - what this feature does, who uses it, and its role/value. NOT a few words restating the title. **MANDATORY for every feature, every status** (Built/Shipped and Backlog). This whole-list view is the team's first orientation; never blank or trivial.]
**Layer:** [one or more of frontend / backend / system - list all layers a cross-layer feature spans, e.g. "frontend, backend"; never "fullstack"]   ·   **Phase:** MVP / MVP+ / Phase 1 / ...   ·   **Actor:** [User / Host / Admin / System]
**KANO:** Must-be / Performance / Delighter / Indifferent   ·   **V×C:** Quick Win / Big Bet / Fill-in / Time Waster
**Status:** [canonical only: `6_Shipped` / `4_In_Build` / `1_Backlog` - the SAME vocabulary as the card frontmatter, mapped from the code reality below]   ·   **Dev Stripe:** [Dev Stripe 1 / ...]   ·   **Subtasks:** yes / no
**Build reality:** Done / In Progress / Planned / Unclear   *(human label only - the code reality that maps to the canonical Status above; not a second status axis)*
**Spec coverage:** [Feature Card exists: Yes/No | Sections 1-3: Complete/Partial/None]
**Notes:** [any relevant context]

---

## Delivery Stripe Overview

| Stripe | Domain | Features | Next priority |
|---|---|---|---|
| [Stripe name] | [Domain] | FEAT-ORD-001, FEAT-ORD-002, FEAT-ORD-003 | FEAT-ORD-004 |
| [Stripe name] | [Domain] | FEAT-PAY-001, FEAT-PAY-002 | FEAT-PAY-003 |

---

## JIT Design Queue (features needing pm-feature-design before build)

| Feature | Status | Priority | Reason |
|---|---|---|---|
| FEAT-[DOMAIN]-NNN | Planned | High | Next in stripe, no Feature Card |

---

## Changelog

| Version | Date | Change | Triggered by |
|---|---|---|---|
| 1.0 | [date] | Initial extraction from existing product | Migration path |
```

---

### ARTIFACT 2: Stub Feature Cards

For each feature with Status = In Progress or Planned (and no existing Feature Card):

Create `features/cards/FEAT-[DOMAIN]-NNN.md` with stub frontmatter:

```markdown
---
id: FEAT-[DOMAIN]-NNN
title: "[Action] [Result] [Object]"
status: 1_Backlog
stripe: [stripe-name]
feature_set: "FS-NN: [Feature Set name - group during planning]"
layer: [one or more of frontend / backend / system - from code evidence; list all layers a cross-layer feature spans (e.g. "frontend, backend"), never "fullstack"]
phase: [MVP / MVP+ / Phase 1 / ...]
actor: [User / Host / Admin / System]
owner: unassigned
priority: [P1/P2/P3 - assign during planning]
kano: [Must-be / Performance / Delighter / Indifferent]
vxc: [Quick Win / Big Bet / Fill-in / Time Waster]
estimate: "[S / M / L - informational sizing, NOT the atomicity test]"
has_subtasks: false
prd_ref: /product/PRD_master.md#[section]
feature_flag: [domain.feature-name]
flag_default: off
---

# Feature Card: {{title}}

> **Status:** 1_Backlog - stub created by pm-reverse-extract
> **Next step:** Run /pm-feature-design FEAT-[DOMAIN]-NNN to complete Sections 1-3 before build

## Description

[2-3 sentences extracted from codebase/docs: what this feature does, who uses it, and what value it delivers. Fill from extraction evidence - do not leave blank.]

## Current state (extracted)

**Implementation status:** [Done / In Progress / Planned]
**Evidence:** [where this was found - file path, doc name, or code reference]
**Known gaps:** [what is missing, unclear, or needs investigation before build]

---

## 1. Biznis Mantinely (SDD Input)
*TBD - populated by /pm-feature-design [FEAT-ID]*

## 2. Acceptance Criteria
*TBD - populated by /pm-feature-design [FEAT-ID]*

## Subtasks (helper notes)
*Granular legacy features folded here as nuance helpers (see Reconciliation Report), or added during /pm-feature-design [FEAT-ID]*

## 3. JIT Technical Design (FDD Design)
*TBD - populated by /pm-feature-design [FEAT-ID]*

## 4. Realizacny Protokol (Build Verification)
*TBD - populated after build and Code Inspection*
```

For features with Status = Done that have no Feature Card: create a minimal stub with status `6_Shipped`, **its `## Description` filled from the extraction evidence** (never blank - even shipped features need orientation), and a note that the feature is live - no JIT design needed. Backlog features that are not stubbed must still carry their **Description** in `feature_list.md` (above) - every feature is orientable regardless of card status.

---

## Step 4: Notion push

Read `pureinn-variables.md` key `Feature Backlog URL`.

If URL is blank: skip Notion push, generate markdown only. Remind user to paste the URL once they have it.

If URL is present: push feature entries to Notion Product Features database.

**Step 4a - Get data source ID:**
1. Call `mcp__claude_ai_Notion__notion-fetch` with the Feature Backlog URL
2. Extract `data_source_id` from the `<data-source url="collection://...">` tag
3. Cache in `state.json notion_ids.feature_backlog`

**Step 4b - Get Feature Card Template ID:**
From the same notion-fetch result, find the `<templates>` section.
Look for the template named `"Feature Card Template"` and extract its `id` attribute.
Example: `<template id="b8df8652-..." name="Feature Card Template"/>` → use this id.

**Step 4c - Create pages:**

Call `mcp__claude_ai_Notion__notion-create-pages` with:
- `parent.type` = `"data_source_id"`
- `parent.data_source_id` = ID from Step 4a

**Status mapping (extraction → Notion):**

| Extraction status | Notion Status |
|---|---|
| Done (live in production) | `6_Shipped` |
| In Progress (being built) | `4_In_Build` |
| Planned / Backlog | `1_Backlog` |
| Unclear | `1_Backlog` |

**Per entry - use both `properties` AND `content`. Do NOT use `template_id`:**

```
properties:
  Artefact Name: FEAT-[DOMAIN]-NNN: [Feature Name]
  Artefact Type: Feature
  FEAT-ID: FEAT-[DOMAIN]-NNN
  Short Description: [1-sentence description]
  Status: [mapped canonical status - 6_Shipped / 4_In_Build / 1_Backlog, per the mapping table above]
  Layer: [one or more of Frontend / Backend / System - multi-select; list all layers the feature spans, never "fullstack"]
  Phase: [MVP / MVP+ / Phase 1 / ...]
  KANO Category: [Must-be / Performance / Delighter / Indifferent]
  V×C Quadrant: [Quick Win / Big Bet / Fill-in / Time Waster]
  Dev Stripe: Dev Stripe [N]
  Has Subtasks: [true / false]

content:
  ## Description

  [2-3 sentence description from extraction: what it does, who uses it, value]

  ## Current state (extracted)

  **Implementation status:** [Done / In Progress / Planned]
  **Evidence:** [file path or document where this was found]
  **Known gaps:** [what is missing before build]

  ---

  ## 1. Biznis Mantinely (SDD Input)
  *TBD - populated by /pm-feature-design [FEAT-ID]*

  ## 2. Acceptance Criteria
  *TBD - populated by /pm-feature-design [FEAT-ID]*

  ## Subtasks (helper notes)
  *Granular legacy features folded here as nuance helpers, or added during /pm-feature-design [FEAT-ID]*

  ## 3. JIT Technical Design (FDD Design)
  *TBD - populated by /pm-feature-design [FEAT-ID]*

  ## 4. Realizacny Protokol (Build Verification)
  *TBD - populated after build and Code Inspection*
```

Fill from evidence/derivation: `Layer` (from code - FE routes/components → Frontend, controllers/services → Backend, jobs/cron → System), `Has Subtasks` (true if the card has any subtasks), `Dev Stripe`. Propose with reasoning (confirm via AskUserQuestion): `Phase`, `KANO Category` (a shipped feature is usually Must-be), `V×C Quadrant`, `Priority`. Leave blank only: `Feature Card URL` - filled later by pm-feature-design. Never leave Layer / Description / Has Subtasks blank.

After push, confirm count: "Pushed [N] features to Notion."

---

## Step 5: Post-extract summary

After all artifacts are generated, output:

```
EXTRACTION COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Features extracted:  [N total] ([X Done] / [Y In Progress] / [Z Planned])
Stub Feature Cards:  [N created in features/cards/]
Delivery Stripes:    [N stripes]
Notion:              [N pushed / skipped]

JIT DESIGN NEEDED BEFORE NEXT BUILD
  FEAT-[DOMAIN]-NNN - [Feature Name] (In Progress - no Section 1-3)
  FEAT-[DOMAIN]-NNN - [Feature Name] (Planned - highest priority in stripe)

NEXT STEPS
  1. /pm-feature-design FEAT-[DOMAIN]-NNN  → design first in-progress feature
  2. /pm-stripe                             → stripe dashboard and routing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Save to

```
pureinn-workspace/[project-slug]/features/feature_list.md          (Live Register 4)
pureinn-workspace/[project-slug]/features/cards/FEAT-[DOMAIN]-NNN.md  (one stub per In Progress / Planned feature)
```

State update → `state.json`: set `registers.feature_list_initialized` to `true`. Set `current_phase_index` to 6 (ready for JIT delivery cycle).

---

## Handoff

**Čo si teraz má:** `feature_list.md` (Live Register 4) + stub Feature Cards z existujúceho produktu - feature inventory zladený a pushnutý do Notion.

**Ďalší krok:** `/pm-stripe` — nastav delivery channels a choď JIT po featurach (`/pm-feature-design [FEAT-ID]` na in-progress/planned featury).

**Môžeš preskočiť ak:** Staré docs si protirečia s kódom - vtedy nepoužívaj samostatný reverse-extract, ale celý `/pm-reconcile` (rebuild s rekonciliáciou), ktorý tento skill orchestruje.
