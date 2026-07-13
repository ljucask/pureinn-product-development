---
name: pm-audit
description: Health check for an existing Pureinn workspace. Scans the framework's own artifacts - the 4 Live Registers, feature_list, Feature Cards, roadmap, glossary, state.json - against the current Pureinn conventions, finds inconsistencies, drift, and errors, then fixes the mechanical ones and asks about the judgment calls. Detects framework-version drift (artifacts produced by an older Pureinn version) and offers to migrate them. Use when a workspace was built with an older version, after pm-reconcile or pm-reverse-extract, or any time you want to confirm the workspace is internally consistent before continuing. Takes an optional area argument to scope the audit (/pm-audit domain | rules | features), or audits the whole workspace by default. Distinct from pm-reconcile (code vs legacy docs) and pm-reverse-extract (code to inventory) - this checks Pureinn artifacts against Pureinn conventions (Tier 1: form) and cross-checks the strategic layer (PRD, roadmap, personas, market, business model) for semantic consistency, surfacing contradictions read-only and routing each fix to its authoring skill (Tier 2: substance).
license: MIT
metadata:
  agent-mode: synthesis
  author: https://github.com/ljucask
  version: "1.3.0"
  domain: product-management
  triggers: audit, health check, consistency check, workspace check, framework drift, version migration, fix inconsistencies, sanity check, naming check, anti-pattern, strategic consistency, cross-artifact check, re-check
  role: specialist
  scope: validation
  output-format: document
  related-skills: pm-reconcile, pm-reverse-extract, pm-feature-card, pm-features-list, pm-stripe
---

# PM - Audit (Workspace Health Check)


## Agent mode (`--agent`)

Supports `--agent`: runs autonomously in a subagent, drafts the artifact from existing inputs, and returns a short summary + coverage note.

- **No flag** → interactive (default); if inputs are heavy, offer agent mode.
- **`--agent`** → obey. First check inputs are complete. Anything missing: do NOT invent it - mark `[ASSUMED - what/why]` in the output and summary. Never hallucinate to fill a gap.

---

## What this skill does

Scans an existing Pureinn workspace and reports - then fixes - where its own artifacts drifted from the current framework conventions. It is the productized version of a manual consistency pass: ID and naming integrity, cross-reference resolution, structural conformance, lifecycle validity, completeness, and **framework-version drift** (artifacts from an older Pureinn version that miss newer fields or use old names).

**Two tiers, two different jobs:**

- **Tier 1 - Form.** Naming, IDs, cross-refs, lifecycle, schema, metadata parity. Mechanical - auto-fixed in place. This is the classic audit.
- **Tier 2 - Strategic consistency (substance).** Does the strategic layer still agree with itself and with the research it was built on - PRD Target Customer vs. personas, value prop vs. research pains, roadmap phases vs. feature phases, pricing vs. WTP? This tier is **read-only**: it never auto-edits strategic content (that is a business decision). It surfaces each contradiction as `[CONFLICT]` and routes the fix to the authoring skill (`pm-prd`, `pm-product-roadmap`, `pm-business-model`, ...), which re-runs in delta mode. Run Tier 2 after a research injection or strategic pivot, and before a build commitment or pitch.

Run it when:
- A workspace was built with an older Pureinn version and you want it brought current
- Right after `pm-reconcile` or `pm-reverse-extract`, as a verification pass
- Any time before continuing work, to confirm the workspace is internally consistent

**Produces:**
1. `audit/audit_report.md` - findings by severity (P0-P3), scored
2. Mechanical fixes applied in place (with a diff summary)
3. A short AskUserQuestion round for every judgment call

**It checks Pureinn artifacts against Pureinn conventions** - it does not read the codebase or legacy docs (that is `pm-reconcile` / `pm-reverse-extract`).

---

## Position vs. related skills

| Skill | Input → output |
|---|---|
| `pm-reconcile` | codebase vs **legacy docs** → reconciled rebuild |
| `pm-reverse-extract` | **codebase** → feature inventory |
| **pm-audit** | **Pureinn artifacts** vs **Pureinn conventions** → drift/error fix |

`pm-reconcile` and `pm-reverse-extract` hand off to `pm-audit` as their verification step.

---

## What this skill does NOT do

- Read the codebase or legacy documents (that is reconcile / reverse-extract)
- Change business decisions or rule values - only structure, naming, references, and conformance. **Tier 2 may report a strategic contradiction, but it never resolves it** - resolving means choosing between two business claims, which belongs to the authoring skill in delta mode.
- Generate new artifacts that do not exist - it audits what is there (a missing artifact is a finding, not something it invents)

---

## Dependencies

- A Pureinn workspace exists: `pureinn-workspace/[project-slug]/` with at least `state.json` and some artifacts.

If no workspace is found, do not guess. Tell the user to run `/pureinn` first (greenfield) or `/pm-reverse-extract` / `/pm-reconcile` (existing product).

---

## Scope (whole workspace or one area)

`pm-audit` takes an optional area argument, mirroring `pm-reconcile`'s per-area model:

| Command | Audits |
|---|---|
| `/pm-audit` | **Whole workspace** (default) - all artifacts |
| `/pm-audit domain` | `domain/entities.md` + `domain/domain-model.md` (structure, entity/state naming, ERD ↔ entities consistency) |
| `/pm-audit rules` | `domain/business_rules.md` + `domain/decision_models.md` (BR/TBL IDs, rule↔entity refs, decision-table completeness) |
| `/pm-audit features` | `features/feature_list.md` + `features/cards/` (card structure, FS-NN, Section-1 BR-ID refs resolve, lifecycle status) |
| `/pm-audit strategy` | **Tier 2 only** - cross-artifact strategic consistency (PRD ↔ personas ↔ roadmap ↔ market ↔ business model ↔ feature phases). Read-only, routes fixes to authoring skills. |
| `/pm-audit [other]` | any single artifact the user names |

**Tier scoping:** area scopes (`domain`, `rules`, `features`) run Tier 1 only. `strategy` runs Tier 2 only. The default whole-workspace run does **both** tiers.

When an area is given, scan and report only that area's artifacts (plus their direct cross-references - e.g. `features` checks that BR-IDs in cards resolve into `business_rules.md`, without auditing the rules themselves). When no area is given, audit everything. If the user states a scope in plain language, honour it (per the Adaptive-execution standard).

---

## Step 0: Locate workspace + detect version

Determine the **scope** first (from the argument or the user's request - default whole workspace). Then find the workspace and inventory the artifacts in scope:

| Artifact | Present? |
|---|---|
| state.json | |
| domain/entities.md, business_rules.md, decision_models.md | |
| features/feature_list.md + features/cards/ | |
| product/PRD_master.md | |
| roadmap, glossary | |

**Version-drift signals** (detect an older-framework workspace). This is the concrete migration checklist - an artifact produced by an older Pureinn version will carry one or more of these; scan for each literally, not just "convention drift" in the abstract:
- Old lifecycle state names (`1_Walkthrough`, `2_Design`, `3_Design_Inspection_Passed`, `4_Build`, `5_Code_Inspection`, `6_Promoted_to_Build`)
- Old hierarchy terms (`Subject Area`, `Major Feature Set`) or bare `FS-ID` without `FS-NN: Name`
- Missing newer Feature Card fields (`feature_set`, `estimate`) or the `## Subtasks` section
- Notion cache key `notion.*` instead of `notion_ids.*`
- **Feature Card `prd_ref` pointing at the old PRD path** - `prd_ref: /product/PRD.md#...` (or the missing-slash variants `product/PRD.md#...` / bare `PRD.md#...`). Older versions saved the PRD as `PRD.md`; the canonical save path is now `product/PRD_master.md`, so every old card carries a **dead reference to a file that no longer exists**. Migrate to `prd_ref: /product/PRD_master.md#...` (preserve the `#section` anchor). Initiative-PRD refs (`/initiatives/[slug]/prd.md#bc-...`) are a separate valid form - leave them.
- A separate MVP-membership field (`mvp: true/false`, `roadmap_phase:`, or an "MVP" column) instead of the single canonical `phase` axis
- `layer: fullstack` instead of the explicit layer set (`frontend`, `backend`, `system`)
- Reconcile-reality words (`Built` / `In Progress` / `Backlog`) sitting in a `status`/`Status` field instead of a canonical lifecycle value

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Scan

Read every artifact **in scope** (Step 0) and run the checks below - for an area scope, only that area's artifacts and their direct cross-references; for whole-workspace, all of them. Collect findings; do not fix yet.

| Dimension | What is checked |
|---|---|
| **Structure** | Feature Cards match the canonical template (sections 1-4 + Subtasks; frontmatter: id, title, status, stripe, feature_set, actor, owner, priority, estimate, prd_ref, feature_flag, flag_default). Registers match current format and header. |
| **ID & naming** | FEAT/BR/TBL/FS IDs well-formed (`FEAT-[DOMAIN]-NNN`, `BR-[DOMAIN]-NNN`, `TBL-[DOMAIN]-NN`, `FS-NN`) and unique. **The naming check is mandatory and must actually run over every feature name - report its result explicitly (even "0 anti-patterns found") so a silent skip is visible.** Each name must be `<action verb> <result> <object>` with a **strong verb** and an **object = a domain entity**. Flag every violation: (a) **vague/banned verbs** `Process` / `Manage` / `Handle` (and similar non-specific verbs); (b) **technical objects** - the object is an implementation construct not a domain entity (e.g. "...state machine", "...FSM", "...queue", "...flag", "...handler"); (c) the other FDD anti-patterns (bundled multi-op, missing object, CRUD-as-feature, etc.). A naming anti-pattern on an active feature is a P1 finding. Report each as `[FEAT-ID] "name" → [which anti-pattern] → suggested rename`. |
| **Cross-references** | Every `BR-ID` / `TBL-ID` / entity link in a Feature Card resolves to the register. `feature_set` matches feature_list. `stripe` is a real stripe. **`prd_ref` resolves** - it must point at `product/PRD_master.md` (or an `/initiatives/[slug]/prd.md` for an Initiative PRD); a `prd_ref` still pointing at `/product/PRD.md` (or `product/PRD.md` / bare `PRD.md`) is a dead reference to the old PRD path and is drift (P1 - JIT design reads this file). No dangling links. |
| **Lifecycle** | `status` is one of the canonical states (`1_Backlog`, `2_Spec_Done`, `2b_In_Design`, `3_Ready_to_Build`, `4_In_Build`, `5_In_Review`, `6_Shipped`) **everywhere - frontmatter, feature_list, and Notion use the same single vocabulary**. No orphaned or invalid states. `2b_In_Design` is valid **only for a feature whose `layer` includes `frontend`** - a pure backend/system feature in `2b_In_Design` is drift (P2: it has no UI to design). **Reconcile-reality words (`Built` / `In Progress` / `Backlog`) are NOT status values** - if a feature_list or Notion `Status` still carries them, that is drift: map to canonical (`Built`→`6_Shipped`, `In Progress`→`4_In_Build`, `Backlog`→`1_Backlog`) and keep the reality word only as a human label in the card's `Current state (extracted)` section. Mixed vocabularies on the status axis = P1. |
| **Version drift** | Any of the Step 0 drift signals → migration finding. |
| **Completeness** | Every feature in feature_list has a card; every card has its required sections; registers are initialized; state.json flags match reality. |
| **Description present** | Every feature has a non-blank Description - both its `feature_list.md` entry and its card's `## Description` section, for **every status** (including `6_Shipped` lean stubs and `1_Backlog`). A feature with no description is a P2 finding (orientation gap). |
| **Feature metadata complete** | Every feature carries the full property set in frontmatter + feature_list + Notion: `layer` (frontend/backend/system), `phase` (MVP/MVP+/Phase 1... or the project's P0/P1…), `kano`, `vxc`, `stripe` (Dev Stripe), `has_subtasks`. Also check **value consistency**: `has_subtasks` matches whether the card's Subtasks section actually has items; values are from the allowed sets. **`layer` is one or more of `{frontend, backend, system}`** (a cross-layer feature lists several, e.g. `frontend, backend`) - flag any value outside the set, especially **`fullstack`** (not a layer → replace with the actual layers), P2. Missing or inconsistent = P2. **Canonical-field check:** `phase` is the **single axis for MVP membership** - flag and consolidate any duplicate/non-canonical field that encodes the same thing (`mvp: true/false`, `roadmap_phase`, an "MVP" column) into `phase` (IN-MVP = the first/`MVP`/`P0` phase). Two fields on one axis drift apart - a stray `mvp`/`roadmap_phase` is a P2 finding, migrate it to `phase`. |
| **Notion sync** (if configured) | Local `status` vs Notion `Status` mismatch surfaced (drift log, like pm-stripe). |

The table above is **Tier 1 (form)**. For a whole-workspace run or `/pm-audit strategy`, also run Tier 2 below.

### Tier 2: Strategic consistency (read-only, cross-artifact)

Does NOT check form - checks whether the strategic layer's *content* still agrees with itself and with the research it was built on. It **never auto-fixes** (changing a value prop or a segment is a business decision). It surfaces each conflict and routes the fix to the authoring skill, which re-runs in delta mode.

Read the strategic artifacts that exist - `product/PRD_master.md`, roadmap, `personas.md`, `customer-segments.md`, `market-analysis.md`, `business-model-canvas.md`, `feature_list.md` - and check these cross-artifact pairs:

| Check | Conflict looks like | Route fix to |
|---|---|---|
| **Primary segment coherence** | PRD Target Customer, personas, customer-segments, roadmap Segments, business-model Customer Segments do not all name the same primary segment | `/pm-prd` or `/pm-personas` (whichever is stale) |
| **Value prop ↔ pains** | A PRD Value Proposition claim addresses a pain no persona actually has, or a top persona pain has no value-prop answer | `/pm-prd` |
| **Problem coherence** | PRD Problem Statement, roadmap Problem&Market, market-analysis problem framing describe different problems | `/pm-prd` / `/pm-product-roadmap` |
| **Phase ↔ feature phase** | A `phase` value in feature_list has no matching phase in the roadmap, or a roadmap MVP phase has no features carrying it | `/pm-product-roadmap` / `/pm-features-list` |
| **Market numbers** | PRD Market Context TAM/SAM/SOM figures differ from market-analysis.md | `/pm-market-analysis` |
| **Pricing ↔ WTP** | business-model take-rate / pricing contradicts WTP evidence in personas/research or the PRD Business Model section | `/pm-business-model` |
| **KANO ↔ persona pain** | A feature classified Must-be addresses no pain of the primary persona (soft flag) | `/pm-features-list` |

For each conflict, record: `[CONFLICT] Artifact A says X (location) / Artifact B says Y (location) → route: /pm-[skill]`. Do not resolve it - the authoring skill resolves it against real evidence in delta mode. If a referenced strategic artifact is absent, note it as "not present - check skipped", do not invent it.

---

## Step 2: Audit report

Save to: `pureinn-workspace/[project-slug]/audit/audit_report.md`

Score and group every finding by severity:

| Severity | Meaning | Examples |
|---|---|---|
| **P0** | Broken - blocks work | Dangling BR-ID reference, invalid status value, feature_list entry with no card |
| **P1** | Drift that causes errors | Old lifecycle state names, inconsistent FS-NN, naming anti-pattern on an active feature |
| **P2** | Missing newer structure | No `feature_set`/`estimate` field, no `## Subtasks` section, incomplete card |
| **P3** | Cosmetic | Formatting, path-slash convention, optional field gaps, a prose block (e.g. a handoff/routing note) wrapped in a stray ` ``` ` code fence that suppresses its own markdown rendering |

```markdown
# Workspace Audit - [Product Name]
> Generated: [date]  By: pm-audit v[version]
> Workspace: pureinn-workspace/[slug]   Framework target: v[current]

## Score: [N] findings - P0:[x] P1:[x] P2:[x] P3:[x]

## P0 - Broken
| ID | Finding | Location | Fix |
## P1 - Drift
## P2 - Missing structure
## P3 - Cosmetic

## Version migration (if drift detected)
[what older-version patterns were found and the migration applied/proposed]

## Strategic consistency (Tier 2 - read-only, not auto-fixed)
[If clean: "No strategic conflicts - the strategic layer is coherent."]
| Conflict | Artifact A (says) | Artifact B (says) | Route fix to |
|---|---|---|---|
| [check name] | [claim + location] | [claim + location] | `/pm-[skill]` |
```

Tier 2 conflicts are listed separately and are **not** scored P0-P3 - they are not mechanical findings and are never auto-fixed. They are routed, not resolved.

Present the score, P0/P1 summary, **and any Tier 2 conflicts** to the user before fixing.

---

## Step 3: Fix

- **Mechanical (auto-fix):** ID format normalization, old → new lifecycle state names, missing `feature_set`/`estimate`/`Subtasks` scaffolding added, `notion.*` → `notion_ids.*`, **`prd_ref: /product/PRD.md#anchor` (and the `product/PRD.md` / bare `PRD.md` variants) → `/product/PRD_master.md#anchor`, anchor preserved** (an Initiative-PRD `/initiatives/[slug]/prd.md#bc-...` ref is left untouched), path-slash convention, `layer: fullstack` → the explicit layer set derived from evidence, dead-link repair where the target is unambiguous, **collapsing a stray `mvp`/`roadmap_phase` field or "MVP" column into the canonical `phase`** (one axis). Apply in place; report a diff summary.
- **Judgment (ask):** anything where the fix changes meaning - a naming anti-pattern rewrite (always propose a concrete client-valued rename, e.g. "Drive order state machine" → "Submit order for matching"; never leave a flagged name unaddressed), an ambiguous dangling reference, a feature that may need splitting, a missing card that may be intentional. Batch these via the grouped AskUserQuestion pattern (CLAUDE.md), 2-4 per round, confirm, apply.
**The `feature_list.md` is the whole-list orientation surface - backfill writes there FIRST, for every feature, then mirrors to the card and Notion.** Do not fill individual cards while leaving the list incomplete - the list is what the team reads to understand the backlog at a glance. Every feature in the list must end up with a Description and the full property set; iterate across the whole list, not card-by-card in isolation.

- **Missing / weak descriptions (backfill from evidence):** for every feature whose Description is missing OR too terse (a few words / a single clause), draft a proper one from the card's Evidence / code references / linked rules: **2-3 clear, genuinely orientational sentences - what it does, who uses it, the value/role.** Not a one-liner restating the title. Batch via AskUserQuestion, then write to **the `feature_list.md` entry AND the card's `## Description`**. The list entry can be a tight 1-2 sentences; the card carries the fuller version - but neither is blank or trivial.
- **Missing / inconsistent feature metadata (backfill) - for the WHOLE list:** for `layer`, `phase`, `kano`, `vxc`, `has_subtasks` on every feature:
  - `has_subtasks` → **mechanical**: true only if the Subtasks section has a **real item** - ignore italic/placeholder lines (`*TBD ...*`, the `- [ ] [nuance...]` template line). Empty/placeholder → false.
  - `layer` → **derive from evidence** (FE routes/components → frontend, controllers/services → backend, jobs/cron/integrations → system), confirm in batch.
  - `phase`, `kano`, `vxc` → **propose with reasoning** and confirm via AskUserQuestion (a `6_Shipped` feature is usually KANO Must-be; phase from the roadmap / MVP flag if present - for a coherent phase split across the whole list, align to `pm-product-roadmap`). Never silently guess KANO/V×C - they are planning judgments.
  Write confirmed values to **the `feature_list.md` entry, the card frontmatter, and Notion** - keep all three in sync (the v4.11.0 parity rule). The list is not done until every feature carries the full set.

Never silently change a rule value, an acceptance criterion, or a business decision - those are out of scope (route to `pm-feature-design` / `pm-business-rules-library`).

**Tier 2 (strategic consistency) is report-only.** Never auto-edit PRD / roadmap / personas / market / business-model content to resolve a strategic conflict - choosing between two strategic claims is a business decision. List each `[CONFLICT]` with its route and stop. The user runs the routed authoring skill (which re-runs in delta mode) to resolve it against real evidence. Auditing must not silently pick a winner.

For version migration: show the old→new mapping, confirm once, then apply across all affected artifacts in one pass.

---

## Step 4: Re-verify + summary

Re-run the Step 1 scan on the fixed workspace. Confirm P0/P1 are cleared (or list what remains and why).

```
AUDIT COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Before:  P0:[x] P1:[x] P2:[x] P3:[x]
Fixed:   [N] mechanical, [N] confirmed via questions
Remaining: [N] (listed in audit_report.md with reason)
Version:  [migrated from vX / already current]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Save to

```
pureinn-workspace/[project-slug]/audit/audit_report.md   (this skill)
```
Plus in-place fixes to the affected artifacts (registers, feature_list, Feature Cards, state.json).

---

## Handoff

---
**Čo si teraz má:** Workspace zladený s konvenciami (Tier 1) a obraz strategickej koherencie (Tier 2) - opravené ID/naming/refs/lifecycle + zoznam strategických konfliktov s routovaním.

**Ďalší krok:**
- Ak Tier 2 našiel `[CONFLICT]`: spusti routovaný authoring skill (`/pm-prd`, `/pm-product-roadmap`, `/pm-business-model`...) - opraví to v delta mode voči reálnym dátam. Audit ich nerieši.
- Ak je čisto: `/pm-stripe` — pokračuj v JIT delivery. Alebo `/pureinn` pre phase gate check.

**Môžeš preskočiť ak:** Workspace práve vznikol aktuálnou verziou frameworku a strategická vrstva sa od poslednej validácie nezmenila - drift ani strategický konflikt neexistuje.
