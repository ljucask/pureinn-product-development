---
name: pm-reverse-extract
description: Sync the current state of an existing product to Notion as the operational interface. Reads existing FSD/BRD/Feature Cards/codebase (Claude has direct access), extracts the feature inventory, maps it to the MFS → FS → Feature hierarchy with accurate statuses, and pushes the full structure to Notion so the team can see where the product stands. Secondarily generates local Phase 5 artifacts as Claude context for future sessions. Can be run at any point during the project, not just at onboarding.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: reverse extract, existing product, feature inventory, migration path, feature implementation onboarding, sync Notion
  role: specialist
  scope: extraction
  output-format: document
  related-skills: pm-features-list, pm-mvp-scope, pm-fsd, pm-brd
---

# PM - Reverse Extract (Existing Product Sync)

## What this skill does

Syncs the current state of an existing product into Notion as the team's operational interface.

**Primary goal:** Notion push - the team gets a clear, accurate view of the full feature inventory: what is live, what is in progress, what is backlog, and how features are organized into Feature Sets.

**Secondary goal:** Local artifacts - features-list.md, feature-sets.md, delivery-stripes.md written to pureinn-workspace as Claude context for future sessions where the codebase or docs are not in scope.

Claude reads the existing documents and codebase directly - it already has the context. This skill structures and externalizes that context into Notion and local files.

**Produces:**
1. **Feature Inventory** - all features in FDD format, with status (Done / In Progress / Planned) and spec coverage
2. **Feature Set Map** - MFS → FS → Feature hierarchy derived from existing domain groupings (BRD/FSD structure)
3. **Delivery Baseline** - current state snapshot: live, in progress, backlog, plus next stripe recommendation
4. **Notion push** - full MFS/FS/Feature hierarchy created in the Product Features database with accurate statuses
5. **Local artifacts** - features-list.md, feature-sets.md, delivery-stripes.md for Claude context in future sessions

Can be re-run at any point to re-sync Notion after significant state changes.

---

## What this skill does NOT do

- Add context Claude does not already have - it reads and structures what exists in the docs and codebase
- Rewrite or validate BRD/FSD content - reads and maps, does not regenerate
- Run KANO Analysis or Value vs. Complexity - not applicable to features already built
- Run discovery or validation - this is a sync operation, not a new product workflow

---

## Dependencies

**Required:**
- `/pureinn` already run - workspace, state.json, and pureinn-variables.md must exist before this skill runs
- Existing docs or codebase accessible to Claude (at least one of: FSD, BRD, Feature Cards, Domain Model, route/controller files)

**Produces artifacts used by:**
- Notion Product Features database - primary output: team operational view
- `pm-brd` / `pm-fsd` / `pm-stripe` - can reference feature-sets.md and delivery-stripes.md as Claude context
- Future Claude sessions - local artifacts serve as quick-load context without full codebase scan

---

## Step 0: Current state check

Check for existing pureinn-workspace artifacts for this project:
- `state.json` - does a project already exist?
- `artifacts/phase-5/features-list.md` - was this skill already run?
- `artifacts/phase-5/feature-sets.md`
- `artifacts/phase-5/delivery-stripes.md`

Also check: do any of the following exist in the conversation context or project directory?
- BRD documents
- FSD documents
- Feature Cards
- Domain Model / Entity Catalogue
- Codebase (check for route files, controller files, API spec, schema files as alternative sources)

Show state table:

| Source | Status | Detail |
|---|---|---|
| BRD documents | ✅ / ⚠️ / ❌ | [found / partial / not found] |
| FSD documents | ✅ / ⚠️ / ❌ | [found / partial / not found] |
| Feature Cards | ✅ / ⚠️ / ❌ | [X found / partial / not found] |
| Domain Model | ✅ / ⚠️ / ❌ | [found / not found] |
| Codebase | ✅ / ⚠️ / ❌ | [accessible / not accessible] |
| pureinn-workspace | ✅ / ❌ | [project exists / new project] |

Apply the standard skill interaction pattern (CLAUDE.md).

**Options:**

```
What do you want to do in this session?
  A) Full migration - extract features, build hierarchy, push to Notion, generate Phase 5 artifacts (Recommended if starting fresh)
  B) Re-extract only - re-run extraction from docs/code, overwrite local artifacts (if docs changed)
  C) Notion push only - local artifacts already exist, push to Notion
  D) Partial or something specific - describe what you need
```

---

## Step 1: Gather inputs

Ask all questions at once:

```
I need a few inputs to run the migration.

1. PRODUCT NAME AND SLUG
   What is the product name?
   Project slug (lowercase, hyphens, used for folder name): [e.g., acme-rentals]

2. EXISTING DOCUMENTS
   Paste or confirm in context:
   - BRD: [paste path or content, or "in context"]
   - FSD: [paste path or content, or "in context"]
   - Feature Cards: [paste paths or content, or "in context"]
   - Domain Model / Entity Catalogue: [paste or "in context"]

3. CODEBASE ACCESS
   Is the codebase accessible to Claude (same project directory)?
   If yes: what are the key directories for features? (e.g., src/features/, app/controllers/)
   If no: skip codebase scan.

4. CURRENT PRODUCT STATE
   Which features are currently live in production?
   (Describe or paste a list - even rough. e.g., "booking flow is live, payments not yet")

5. FEATURE SETS (if known)
   Do you already have a named Feature Set structure (FS-01, FS-02...)?
   If yes: paste it. If no: I will derive Feature Sets from the BRD/FSD domain groupings.

6. NEXT WORK
   What is the next feature or Feature Set you plan to build?
   (This determines which FS gets a BRD/FSD first in Phase 6)

7. NOTION SETUP
   Read pureinn-variables.md key "Feature Backlog". Skip if URL is present.
   If blank: do you have a Notion Product Features database?
   If yes: paste the URL.
   If no: migration runs as Markdown only. Add URL later to enable push.
```

---

## Step 2: Extract feature inventory

### 2a. Read existing documents

Read in this priority order:
1. FSD documents - flow step tables and acceptance criteria sections are the richest feature source
2. BRD documents - business rules sections reveal what the system does
3. Feature Cards - direct feature list with acceptance criteria and status
4. Domain Model / Entity Catalogue - entities and operations suggest missing features
5. Codebase - route files, controller files, API spec as fallback source

### 2b. Extract features

For each feature found:
- Rename to FDD format: `<action> <result> <object>` (e.g., "User can book a listing" → "Submit booking request")
- Assign an ID: F-001, F-002... (sequential)
- Determine status: Done / In Progress / Planned / Unclear
- Identify actor: who initiates or benefits
- Identify which BRD/FSD section covers it (if any)
- Flag if no BRD/FSD coverage exists (spec gap)

### 2c. Derive Feature Sets

If Feature Sets are provided: use them.

If not: derive from BRD/FSD domain groupings:
- Each BRD/FSD document = one Feature Set (or split if scope is too large)
- Name each Feature Set as the domain it represents (e.g., "Booking Flow", "Property Management")
- Group into MFS clusters by domain (e.g., "Listings" MFS contains "Property Management" FS and "Pricing & Availability" FS)

Apply FDD Feature Set sizing rules:
- Max ~8-10 features per FS
- If a BRD/FSD covers more: split and note the split

### 2d. Determine BRD/FSD coverage status per Feature Set

| Coverage | Meaning |
|---|---|
| Full | BRD + FSD both exist and cover all features in this FS |
| Partial | One exists, or exists but does not cover all features |
| Missing | Neither BRD nor FSD exists for this FS |

---

## Step 3: Generate Phase 5 artifacts

Generate in English.

---

### ARTIFACT 1: Features List (migration edition)

```markdown
# Features List - [Product Name]

> **Phase:** 5 - Feature Planning (Migration)
> **Date:** [date]
> **Source:** Extracted from [BRD / FSD / Feature Cards / Codebase] - [date of source docs]
> **Format:** FDD - action + result + object

---

## Feature Inventory

### [Functional Area / Feature Set name]

| ID | Feature | Actor | Status | Spec coverage | Notes |
|---|---|---|---|---|---|
| F-001 | [FDD-formatted feature name] | [Host/Guest/System] | Done / In Progress / Planned | BRD + FSD / FSD only / None | [e.g., "Covered in FSD-02 Section 2.1"] |
| F-002 | | | | | |

---

### [Functional Area 2]

[same structure]

---

## Status Summary

| Status | Count |
|---|---|
| Done (live in production) | [X] |
| In Progress | [X] |
| Planned (backlog) | [X] |
| Unclear (needs review) | [X] |
| **Total** | **[X]** |

---

## Spec Coverage Summary

| Coverage | Feature Sets | Features affected |
|---|---|---|
| Full (BRD + FSD exist) | [X FSs] | [X features] |
| Partial (one doc missing) | [X FSs] | [X features] |
| Missing (no spec) | [X FSs] | [X features] |

---

## Spec Gaps (priority write list)

Features or Feature Sets with no BRD or FSD, ordered by delivery proximity:

| Feature Set | Missing | Priority | Reason |
|---|---|---|---|
| [FS-03: Booking Flow] | BRD | High | Next stripe |
| [FS-04: Payments] | BRD + FSD | High | Next stripe |
| [FS-06: Admin Panel] | BRD + FSD | Low | Post-MVP |

---

## Features Not Mapped

Features found in codebase or docs that could not be mapped to a clear Feature Set:

| Feature | Source | Note |
|---|---|---|
| [Feature description] | [codebase: src/...] | [Possible FS assignment] |
```

---

### ARTIFACT 2: Feature Sets (migration edition)

```markdown
# Feature Sets - [Product Name]

> **Phase:** 5 - Feature Planning (Migration)
> **Date:** [date]
> **Source:** Derived from [BRD / FSD / Domain Model] - existing product state

---

## Feature Set Overview

| MFS | FS ID | Feature Set | Feature count | Status | BRD | FSD |
|---|---|---|---|---|---|---|
| [Domain A] | FS-01 | [Feature Set name] | [X] | Done / In Progress / Planned | Exists / Missing | Exists / Missing |
| [Domain A] | FS-02 | [Feature Set name] | [X] | | | |
| [Domain B] | FS-03 | [Feature Set name] | [X] | | | |

---

## Feature Set Details

### [Domain A - MFS name]

#### FS-01: [Name]

**Purpose:** [What this FS enables]
**Primary actor:** [Host / Guest / Admin / System]
**Status:** Done / In Progress / Planned
**BRD status:** Exists (path: [path]) / Missing
**FSD status:** Exists (path: [path]) / Missing

**Features in this set:**

| ID | Feature | Status |
|---|---|---|
| F-001 | [Feature name] | Done |
| F-006 | [Feature name] | Planned |

**Spec action required:**
- [ ] BRD: [write from scratch / extend with F-XXX / already complete]
- [ ] FSD: [write from scratch / extend with F-XXX / already complete]

---

[repeat per FS]
```

---

### ARTIFACT 3: Delivery Baseline (replaces Delivery Stripes for migration)

```markdown
# Delivery Baseline - [Product Name]

> **Phase:** 5 - Feature Planning (Migration)
> **Date:** [date]
> **Purpose:** Defines the current delivery state as baseline for Phase 6 forward planning.
>             Replaces the Delivery Stripes plan for products migrating into the framework.

---

## Production Baseline (Done)

Features currently live:

| FS | Feature | ID | Notes |
|---|---|---|---|
| FS-01 | [Feature] | F-001 | |
| FS-03 | [Feature] | F-010 | |

---

## In Progress

| FS | Feature | ID | Expected completion |
|---|---|---|---|
| FS-03 | [Feature] | F-012 | [date or "unknown"] |

---

## Planned Backlog (upcoming Phase 6 work)

Ordered by delivery priority (dependency + next-up logic from user input):

| Priority | FS | Feature | ID | Blocking? |
|---|---|---|---|---|
| 1 | FS-03 | [Next feature to build] | F-013 | Depends on F-012 |
| 2 | FS-04 | [Feature] | F-015 | Depends on F-013 |

---

## Next Stripe Recommendation

Based on current state and user-specified next work:

**Stripe 1 (next sprint):**
- Features: [F-013, F-015]
- Feature Sets: [FS-03, FS-04]
- Spec gate: BRD + FSD must exist for FS-03 and FS-04 before Stripe 1 starts
- Spec status: [FS-03 FSD exists, BRD missing / FS-04 both missing]
- Action before starting: [run pm-brd + pm-fsd for FS-03 and FS-04]

---

## Spec Writing Schedule

| When | Activity |
|---|---|
| Before Stripe 1 | Write BRD + FSD for [FS-03, FS-04] |
| During Stripe 1 | Write BRD + FSD for [FS-05] (if Stripe 2 includes it) |
```

---

## Step 4: Notion push

**Runs after user approves all three artifacts.**

If no Notion database is configured: skip to Step 5. Output Markdown only.

### 4a. Get data source ID

1. Read `pureinn-variables.md` key "Feature Backlog" → get URL
2. Check `state.json notion_ids.feature_backlog` → if set, use it directly
3. If not cached: call `mcp__claude_ai_Notion__notion-fetch` with the URL, extract data source ID from `<data-source url="collection://...">`, save to `state.json notion_ids.feature_backlog`
4. If URL blank in pureinn-variables.md: ask user, save URL, then proceed with step 3

### 4b. Create MFS entries

For each MFS cluster from Artifact 2: call `mcp__claude_ai_Notion__notion-create-pages` with:
- `parent.type` = `"data_source_id"`
- `parent.data_source_id` = from 4a
- Per MFS entry: `Artefact Name` = MFS name, `Artefact Type` = `"MFS"`, `Status` = `"Backlog"`

Collect returned page URLs - needed for FS parent relations.

### 4c. Create FS entries

For each Feature Set from Artifact 2: call `mcp__claude_ai_Notion__notion-create-pages` with:
- Per FS entry: `Artefact Name` = FS name, `Artefact Type` = `"FS"`, `Status` = appropriate to FS status (Done FSs → `"Done"`, others → `"Backlog"`), `Parent` = URL of corresponding MFS from 4b

Collect returned page URLs - needed for Feature parent relations.

### 4d. Create Feature entries

For each feature from Artifact 1: call `mcp__claude_ai_Notion__notion-create-pages` with:
- `parent.type` = `"data_source_id"`
- `parent.data_source_id` = from 4a

Per feature:

| Notion property | Value | Source |
|---|---|---|
| `Artefact Name` | Feature name (FDD format) | Artifact 1 |
| `Artefact Type` | `"Feature"` | Fixed |
| `Short Description` | 1-sentence description of what the feature does | Extracted from FSD/Feature Card |
| `Status` | `"Done"` / `"In Progress"` / `"Backlog"` | Artifact 1 status |
| `Parent` | URL of corresponding FS page from 4c | Artifact 2 FS assignment |
| `template_id` | Feature Template ID from database schema | From notion-fetch result |

Status mapping:
- Done (live) → `"Done"`
- In Progress → `"In Progress"`
- Planned → `"Backlog"`
- Unclear → `"Backlog"` (flag in notes)

Push features in batches of up to 100 per call.

### 4e. Confirm

After push: report counts (MFS created, FS created, Features created, errors). Remind user:
- BRD/FSD paths will be linked via `FSD URL` property on FS entries as spec is confirmed in Phase 6
- Status of Done features reflects current production state at migration time

---

## Step 5: Update framework state

Read existing `pureinn-workspace/[slug]/state.json` (created by `/pureinn` during onboarding). Update the following fields - do not overwrite the full file:

```json
{
  "migration": true,
  "migration_date": "[date]",
  "current_phase_index": 6,
  "current_phase_name": "Design by Feature",
  "phases_completed": [1, 2, 3, 4, 5],
  "phase_5_source": "reverse-extract"
}
```

If Notion was connected in Step 4, also update:
```json
{
  "notion_ids": {
    "feature_backlog": "[data_source_id from Step 4a]"
  }
}
```

All other fields written by `/pureinn` (guidance_mode, product_shape, team_structure, assessment_file, etc.) are preserved as-is.

`migration: true` signals to `/pureinn` that phases 1-5 were not run through the framework. Phase exit gates for those phases are skipped on resume.

Write pureinn-workspace/[slug]/artifacts/phase-5/ artifacts:
- `features-list.md` - from Artifact 1
- `feature-sets.md` - from Artifact 2
- `delivery-stripes.md` - from Artifact 3 (Delivery Baseline)

---

## Step 6: Migration summary and next actions

After all steps complete, output:

```
Migration complete.

[Product Name] is now registered in the Feature Implementation playbook.

PRODUCTION BASELINE
  [X] features live
  [X] features in progress
  [X] features in backlog

SPEC COVERAGE
  [X] Feature Sets - spec complete (BRD + FSD exist)
  [X] Feature Sets - spec partial
  [X] Feature Sets - spec missing

NOTION
  [X] MFS created
  [X] FS created
  [X] Features created

NEXT ACTIONS (in order)
  1. Run /pureinn to confirm project state and see Phase 6 dashboard
  2. Write missing BRD for [FS-XX] - run /pm-brd before Stripe 1 starts
  3. Write missing FSD for [FS-XX] - run /pm-fsd before Stripe 1 starts
  4. Start Stripe 1 - run /pm-stripe kickoff
```

---

## Internal completeness checklist

<!-- Claude reference only - not shown to user.
     Use in Step 0 to identify gaps. Use in Step 3 to verify output before finalizing. -->

**Feature extraction must cover:**
- [ ] All FSD sections scanned for flow steps (each step = candidate feature)
- [ ] All BRD sections scanned for rules that imply a user-facing action
- [ ] All Feature Cards read directly where they exist
- [ ] Codebase scanned if docs alone do not cover full feature set (routes, controllers, models as signal)
- [ ] Every feature in FDD format: `<action> <result> <object>` - no capability-style names
- [ ] Every feature has a status (Done / In Progress / Planned / Unclear)
- [ ] Spec coverage determined per feature (which BRD/FSD section covers it, or "none")

**Feature Set map must cover:**
- [ ] MFS → FS → Feature hierarchy complete - no features without a FS
- [ ] No FS has more than ~10 features (split if needed)
- [ ] BRD/FSD coverage status per FS determined and stated
- [ ] Spec gaps listed and ordered by delivery proximity
- [ ] Spec action required clearly stated per FS (write from scratch / extend / already complete)

**Delivery Baseline must cover:**
- [ ] Done features listed (with FS assignment)
- [ ] In Progress features listed
- [ ] Planned backlog listed and ordered
- [ ] Next Stripe recommendation includes spec gate check (what spec must be written before stripe starts)
- [ ] Spec writing schedule defined (rolling - ahead of build)

**Notion push must cover:**
- [ ] Status accurately reflects production state (Done = live, not just "built")
- [ ] Parent relations correct (Feature → FS → MFS)
- [ ] No duplicate entries (check if MFS/FS names already exist before creating)

**state.json must:**
- [ ] Set playbook to "feature-implementation"
- [ ] Set current_phase to 6
- [ ] Set migration: true, current_phase_index: 6, phases_completed: [1,2,3,4,5]
- [ ] List completed_phases [1, 2, 3, 4, 5] so /pureinn skips their exit gates

---

## Notion

Read `pureinn-variables.md` key "Feature Backlog" - used in Step 4a.

After migration: remind user to update Notion page references for BRD, FSD, and Domain Model once those pages exist in Notion. These are set in `pureinn-variables.md` under the Engineering section.

---

## Save to

```
pureinn-workspace/[project-slug]/state.json          ← UPDATE only (fields listed in Step 5)
pureinn-workspace/[project-slug]/artifacts/phase-5/features-list.md
pureinn-workspace/[project-slug]/artifacts/phase-5/feature-sets.md
pureinn-workspace/[project-slug]/artifacts/phase-5/delivery-stripes.md
```
