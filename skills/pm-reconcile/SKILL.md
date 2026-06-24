---
name: pm-reconcile
description: Rebuild playbook for an existing product onboarded to Pureinn. Reconciles the actual codebase against a folder of legacy documents (BRD, FSD, domain/entity models, business rules) that may contain logical, semantic and structural inconsistencies. Runs in two phases - first PLAN (inspect docs + code, define which areas to reconcile, in what order, into which Pureinn artifacts), then per-area EXECUTION (/pm-reconcile domain | rules | features ...) one layer at a time. Produces a living Reconciliation Report and rebuilds the 4 Live Registers + feature inventory clean. Use when a product was built outside the framework, has stale or conflicting docs, and the (often new) team needs one consistent source of truth that matches the code. Multi-session - track progress with pm-reconcile-status.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: reconcile, rebuild, migration, existing product, old docs, BRD reconciliation, team handover, codebase vs docs, onboard existing product, rebuild from code
  role: specialist
  scope: reconciliation
  output-format: document
  related-skills: pm-reconcile-status, pm-entity-registry, pm-domain-model, pm-business-rules-library, pm-reverse-extract, pm-glossary, pm-stripe
---

# PM - Reconcile (Rebuild from Existing Product)

## What this skill does

Takes an existing product - working code plus a pile of legacy, possibly inconsistent documentation - and rebuilds a clean Pureinn structure that matches reality. It runs in **two phases**:

1. **PLAN** - inspect the old-docs folder and the codebase surface, detect which areas exist, map each to its target Pureinn artifact, and define the order. Output: `reconciliation_plan.md`.
2. **EXECUTE per area** - `/pm-reconcile [area]` reconciles one layer at a time in the planned order, asking about real business-logic conflicts, appending to a living Reconciliation Report, and rebuilding that layer's register.

Reconciliation can span multiple sessions. Progress is held in `state.json` and shown by **`/pm-reconcile-status`**.

This is the **Rebuild playbook** referenced in the `/pureinn` orchestrator. Run it when a product was built outside Pureinn, legacy docs disagree with the code and each other, and the (often new) team needs one trustworthy source of truth.

---

## Invocation modes

| Command | Mode | Does |
|---|---|---|
| `/pm-reconcile` | **Plan / route** | No plan yet → build the Reconciliation Plan. Plan exists → short status + point to the next area (full dashboard via `/pm-reconcile-status`). |
| `/pm-reconcile plan` | **Plan (force)** | Re-inspect and rebuild the plan. |
| `/pm-reconcile domain` | **Execute** | Reconcile entities + attributes + enums + state machine **structure** → `entities.md` (Register 1) + glossary aliases. Offers the cross-domain ERD → `domain-model.md`. |
| `/pm-reconcile rules` | **Execute** | Reconcile business rules + decision models + transition **guard conditions** → `business_rules.md` + `decision_models.md` (Registers 2-3). |
| `/pm-reconcile features` | **Execute** | Reconcile feature inventory → `feature_list.md` + stub Feature Cards Section 1 (Register 4). |
| `/pm-reconcile [other]` | **Execute** | Any extra area the plan defined (e.g. `events`, `integrations`). |

**Default area order is dependency-driven:** `domain` → `rules` → `features`. Entities are the vocabulary everything references, so they become canonical first. Rules operate on entities and guard transitions, so they come next. Features reference rules and entities, so they come last. This mirrors the register numbering 1 → 2 → 3 → 4. The plan can adapt the order (e.g. domain-by-domain on a large product).

---

## Source of truth model (read before running any area)

Reconciliation is **asymmetric**. Two layers, two kinds of mismatch. Apply on every comparison:

| Layer | Source of truth | On mismatch |
|---|---|---|
| **Business intent** - rule values, decisions, what a feature should do, *why* | **Legacy docs (BRD / business rules / decision models)** | If code implements a *different business rule* (e.g. refund window 14 vs 30 days) → **business-logic divergence**. Do NOT silently pick a side. Surface via AskUserQuestion; the team rules "code is the bug" or "doc is stale". Record it. |
| **Technical structure** - entity / attribute / enum / state names, state-machine shape, what is implemented | **Codebase** (observed reality) | **Rewrite the docs to match the code. Mechanical, no question.** Old doc name kept as an **alias** in the glossary. |

Two rules that follow:
1. **Never change the codebase.** This skill rebuilds documents only. Code that diverges from intended logic is *flagged*, not edited away.
2. **Docs that run ahead of the code** (described but not implemented) are recorded as `specified, not implemented` → backlog. They are not fabricated into the live registers. The registers describe the system that actually runs.

End state: legacy docs become a dead reference. The rebuilt registers are the new single source of truth - structurally aligned to code, carrying business logic from the docs, every divergence visible.

---

## Business logic now, feature design JIT

Migrate all business logic now so the team never mirrors the old docs again - but do not design every feature upfront:

| Layer | When | Lives in |
|---|---|---|
| Entities, states, rules, decision models | **Fully now** | The Live Registers. Old BRD then retired. |
| Feature → rule mapping (Feature Card Section 1) | **Now** | Stub cards link to register BR-IDs |
| Feature technical design (Sections 2-3: ACs, sequence diagram, files) | **JIT** via pm-feature-design | Written when the feature is next worked, with a fresh code scan |

Business logic lives in the registers, not the cards - so deferring Sections 2-3 loses nothing.

---

## What this skill does NOT do

- Change, refactor, or "fix" the codebase - documents only
- Resolve genuine business-logic conflicts on its own - those go to the user via AskUserQuestion
- Write Feature Card Sections 2-3 - that stays JIT in `pm-feature-design`
- Re-run product discovery or validation - this is a rebuild, not a new-product workflow

---

## Dependencies

**Required:**
- `/pureinn` already run - workspace, `state.json`, `pureinn-variables.md` exist
- Codebase accessible (routes / controllers / models / schema / enums / tests)
- A folder containing the legacy docs (any format)

**Recommended:** `/common-ground` (stack, APIs, domain model) - speeds the code scan.

**Produces artifacts used by:** `pm-feature-design` (JIT) and `pm-stripe` (rebuilt registers); the team (Reconciliation Report); `pm-reconcile-status` (progress).

---

# ===== PLAN MODE =====

Runs on `/pm-reconcile` (when no plan exists) or `/pm-reconcile plan`.

## Step P0: Current state check

Show a state table: codebase accessible? old-docs folder found (and which doc types)? do any registers already exist? does `reconciliation_plan.md` exist? If a plan exists, ask whether to keep it (route to status) or rebuild it.

Apply the standard skill interaction pattern (CLAUDE.md).

## Step P1: Inspect (do not deep-reconcile yet)

- Skim the old-docs folder: catalogue every document and what it covers (domain model, internal/external entities, state machines, business rules, decision tables, FSDs, feature lists).
- Skim the codebase surface: top-level structure, models/schema, route map, enums - enough to know what areas exist. Do NOT diff yet.

## Step P2: Define the plan

For each detected area:
- Map it to its target Pureinn artifact (entities.md / business_rules.md / decision_models.md / feature_list.md + cards / extra)
- Set its order (default `domain → rules → features`, adapt if the product is large or multi-domain)
- Note its primary source docs and the relevant code locations

Then use AskUserQuestion to confirm:
- Question 1: "Source-of-truth policy?" - A: "Code wins structure, docs win business logic, ask on conflicts (Recommended)" / B: "Code wins everything" / C: "Docs win everything, flag code"
- Question 2: "Reconcile the whole product, or domain-by-domain?" - A: "Domain-by-domain (Recommended for large products)" / B: "Whole product per layer"

Surface this inline if the product is large:
```
Assumption: a whole-product layer pass on a large codebase produces a large Reconciliation Report
and a long AskUserQuestion queue. Domain-by-domain keeps each pass reviewable.
If this is wrong, tell me - it affects how I batch the areas.
```

## Step P3: Write the plan + initialize status

Write `reconcile/reconciliation_plan.md` (template below) and initialize `state.json` `reconcile.areas[]` (schema below) with every area at `status: pending`.

Close with the ordered list of commands to run, e.g.:
```
PLAN READY - [N] areas.
Run in order:
  1. /pm-reconcile domain
  2. /pm-reconcile rules
  3. /pm-reconcile features
Check progress any time with /pm-reconcile-status.
```

---

# ===== PER-AREA EXECUTION =====

Runs on `/pm-reconcile [area]`.

## Step A0: Load plan & confirm

Read `reconciliation_plan.md` + `state.json reconcile`. Confirm the requested area exists in the plan. If an earlier area in the order is still `pending`, warn (dependencies may be unsettled) but allow override if the user insists. Mark this area `in_progress`.

## Step A1: Scoped code scan

Scan only the slice relevant to this area:
- **domain:** models / schema / migrations / enums / status fields + transition logic → real entities, attributes, enums, and state-machine **structure** (which states & transitions exist)
- **rules:** validation / guard / computed-condition logic + the conditions gating each state transition → rules the code actually enforces
- **features:** routes / controllers / services / tests → what the system actually does

## Step A2: Scoped doc parse

Read the source docs the plan tied to this area; extract the intended business picture for this layer only (with provenance: doc + section).

## Step A3: Reconcile

Diff code (A1) vs intent (A2), applying the source-of-truth model. Classify every mismatch:

| Type | Resolution |
|---|---|
| Naming drift (same thing, different name) | Auto: canonical = code name; alias → glossary |
| Structural drift (attribute/enum/state shape differs) | Auto: register reflects code; doc term as alias or `not implemented` |
| **Business-logic divergence** (the rule itself differs) | **AskUserQuestion** - team rules code-bug vs stale-doc; record |
| Doc-only / aspirational (described, not built) | Mark `specified, not implemented` → backlog; not added as real |
| Code-only / undocumented (built, not in docs) | Capture as real; flag "confirm intent" |
| Internal doc contradiction (docs disagree) | **AskUserQuestion** - which is authoritative |

Use the **grouped question pattern** (CLAUDE.md): batch related conflicts (2-4 per group), present code behavior + doc statement(s) + a recommended resolution, confirm, continue. Never silently resolve a business-logic conflict. Assign `DIV-NN` IDs to divergences.

**High-volume batching (checkpointed) - required when an area is large:** When a single area pass has many items to reconcile (roughly **>15** rules / decision tables / features - common in legacy systems with dozens of each), do NOT process them all in one sitting. Batch and checkpoint:

1. Split the area's items into batches by a natural grouping - rules and decision tables by **feature set or rule category**, features by **feature set**, entities by **cluster**. Aim for ~10-15 items per batch. Business rules and decision tables can be batched as separate runs if both are large.
2. Process one batch fully: auto-reconcile the matches, raise AskUserQuestion only on **that batch's** divergences. Then **checkpoint** - append the batch's findings to the report, record progress in `state.json` (`reconcile.areas[].batches_done` / `batches_total`), and report: `batch N/M done - X divergences resolved, Y open`.
3. The user can stop after any batch. `/pm-reconcile-status` shows batch progress; re-running `/pm-reconcile [area]` **resumes at the next un-done batch** and does not re-reconcile completed batches.

This bounds the AskUserQuestion load per batch (not by the whole area's volume) and keeps each sitting reviewable. The area's `status` becomes `done` only when its last batch is checkpointed.

## Step A4: Append to the Reconciliation Report

Append this area's section to the living `reconcile/reconciliation_report.md` (do not overwrite other areas' sections).

## Step A5: Rebuild this area's register (reconciled mode)

Drive the existing skill - do not duplicate its template:
- **domain** → `/pm-entity-registry` (reconciled mode) → `entities.md` (entities, attributes, state-machine structure) + `/pm-glossary` for aliases.
  **Also offer the higher-level map:** ask via AskUserQuestion (default **Yes** for a rebuild - a new team benefits) whether to generate `domain-model.md` too via `/pm-domain-model` (reconciled mode) - the cross-domain ERD and domain boundaries, derived from the same reconciled entities. The two are complementary: the Reconciliation Report is the audit ("what conflicted, how we ruled"); the domain model is the structural map ("how it all fits together"). Skip only if the user declines.
- **rules** → `/pm-business-rules-library` (reconciled mode) → `business_rules.md` + `decision_models.md`; also writes the reconciled guard conditions onto the transitions in `entities.md`. Rules with an open `DIV-NN` stay `Draft` linked to the report; divergence-free rules go `Final`.
- **features** → `/pm-reverse-extract` (reconciled mode) → `feature_list.md` + stub cards. Features normalized to FDD grammar, grouped into `FS-NN`, Section 1 linked to register BR-IDs; code-only features included; doc-only items NOT carded (backlog).

  **Right-sizing legacy features (apply the semantic atomicity test):** legacy systems are often mis-granular. Reconcile each to one coherent client-valued function:
  - **Too granular** (several legacy "features" are really nuances of one capability, e.g. *login*, *register*, *reset password* under *authenticate user*) → consolidate them under one rightful Feature and capture the granular bits as **Subtasks** (helper notes) on that card. They are not lost, not kept as pseudo-features.
  - **Too big** (a legacy feature carries two independent results) → split into separate Features.
  - Record every merge/split in the Reconciliation Report (Section: feature regrouping) so the team can trace where each legacy item went.

## Step A6: Update status + Notion

Set this area `status: done` in `state.json reconcile.areas[]` (record `divergences_open` count) and tick it in `reconciliation_plan.md`. Push this slice to Notion via the downstream skill's existing logic if a target is configured (`notion_ids.<key>` convention; never invent columns).

Close with: what this area produced, open divergences, and the next area command (or "all areas done - run /pm-reconcile-status").

---

## Reconciliation Plan template

Save to: `pureinn-workspace/[project-slug]/reconcile/reconciliation_plan.md`

```markdown
# Reconciliation Plan - [Product Name]

> **Scope:** [whole product / domain-by-domain]
> **Source-of-truth policy:** [chosen]
> **Generated:** [date]  **By:** pm-reconcile v[version]

## Areas (in execution order)

| # | Area | Command | Source docs | Code locations | Target artifact | Status |
|---|---|---|---|---|---|---|
| 1 | domain | `/pm-reconcile domain` | [domain_model.md, entities.md] | [app/models, db/schema] | domain/entities.md (R1) + domain-model.md (ERD, offered) | pending |
| 2 | rules | `/pm-reconcile rules` | [BRD.md §rules, decision_tables.md] | [services, validators] | business_rules.md + decision_models.md (R2-3) | pending |
| 3 | features | `/pm-reconcile features` | [FSD/*, feature_list.xlsx] | [routes, controllers] | features/feature_list.md + cards (R4) | pending |

## Notes
- [anything that affects ordering or batching]
```

## Reconciliation Report structure (living, appended per area)

Save to: `pureinn-workspace/[project-slug]/reconcile/reconciliation_report.md`

Header (written by Plan mode): purpose, scope, policy, date. Then one section appended per area pass:

```markdown
## [Area] reconciliation - [date]

### Naming & structure drift (auto, code = truth)
| Concept | Old doc name | Canonical (code) | Alias |
### Business-logic divergences
| ID | Topic | Doc says | Code does | Ruling | Action for team |
| DIV-01 | ... | ... | ... | [code bug / doc stale] | [fix code / update rule] |
### Decisions made (AskUserQuestion log)
### Specified but not implemented (→ backlog)
### Undocumented in code (→ confirm intent)
### Feature regrouping (features area only - merges/splits, where each legacy item went)
### Open questions for the team
```

## state.json schema

```json
"reconcile": {
  "plan_created": true,
  "policy": "code-structure/docs-business/ask-conflicts",
  "scope": "domain-by-domain | whole-product",
  "areas": [
    {"area": "domain",   "order": 1, "target": "domain/entities.md",        "status": "done",        "divergences_open": 0, "batches_done": 1, "batches_total": 1},
    {"area": "rules",    "order": 2, "target": "domain/business_rules.md",   "status": "in_progress", "divergences_open": 2, "batches_done": 2, "batches_total": 5},
    {"area": "features", "order": 3, "target": "features/feature_list.md",   "status": "pending",     "divergences_open": 0, "batches_done": 0, "batches_total": 0}
  ]
}
```
`status` ∈ `pending | in_progress | done`. On full completion also set `registers.reconciled: true`, `registers.feature_list_initialized: true`, `current_phase_index: 6`.

---

## Handoff

```
---
**Čo si teraz má:** [Po PLANE] plán rekonciliácie - ktoré oblasti, v akom poradí, do akej Pureinn
štruktúry. [Po oblasti] tá vrstva je zladená s kódom, jej sekcia je v Reconciliation Reporte,
register prestavaný.

**Ďalší krok:** `/pm-reconcile [ďalšia oblasť podľa plánu]` — pokračuj v poradí.
Stav kedykoľvek cez `/pm-reconcile-status`.

**Po dokončení všetkých oblastí:** `/pm-audit` → overí konzistenciu prestaveného workspace, potom `/pm-stripe` → delivery channels a JIT po featurach.
Reconciliation Report prejdi s tímom kvôli otvoreným divergenciám.

**Môžeš preskočiť ak:** žiadne staré docs neexistujú (len kód) — vtedy stačí naivná migračná cesta
(`/pm-entity-registry` + `/pm-business-rules-library` + `/pm-reverse-extract`) bez rekonciliácie.
```
