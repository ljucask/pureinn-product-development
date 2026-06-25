---
name: pm-audit
description: Health check for an existing Pureinn workspace. Scans the framework's own artifacts - the 4 Live Registers, feature_list, Feature Cards, roadmap, glossary, state.json - against the current Pureinn conventions, finds inconsistencies, drift, and errors, then fixes the mechanical ones and asks about the judgment calls. Detects framework-version drift (artifacts produced by an older Pureinn version) and offers to migrate them. Use when a workspace was built with an older version, after pm-reconcile or pm-reverse-extract, or any time you want to confirm the workspace is internally consistent before continuing. Takes an optional area argument to scope the audit (/pm-audit domain | rules | features), or audits the whole workspace by default. Distinct from pm-reconcile (code vs legacy docs) and pm-reverse-extract (code to inventory) - this checks Pureinn artifacts against Pureinn conventions.
license: MIT
metadata:
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: audit, health check, consistency check, workspace check, framework drift, version migration, fix inconsistencies, sanity check
  role: specialist
  scope: validation
  output-format: document
  related-skills: pm-reconcile, pm-reverse-extract, pm-feature-card, pm-features-list, pm-stripe
---

# PM - Audit (Workspace Health Check)

## What this skill does

Scans an existing Pureinn workspace and reports - then fixes - where its own artifacts drifted from the current framework conventions. It is the productized version of a manual consistency pass: ID and naming integrity, cross-reference resolution, structural conformance, lifecycle validity, completeness, and **framework-version drift** (artifacts from an older Pureinn version that miss newer fields or use old names).

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
- Change business decisions or rule values - only structure, naming, references, and conformance
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
| `/pm-audit [other]` | any single artifact the user names |

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

**Version-drift signals** (detect an older-framework workspace):
- Old lifecycle state names (`1_Walkthrough`, `2_Design`, `3_Design_Inspection_Passed`, `4_Build`, `5_Code_Inspection`, `6_Promoted_to_Build`)
- Old hierarchy terms (`Subject Area`, `Major Feature Set`) or bare `FS-ID` without `FS-NN: Name`
- Missing newer Feature Card fields (`feature_set`, `estimate`) or the `## Subtasks` section
- Notion cache key `notion.*` instead of `notion_ids.*`

Apply the standard skill interaction pattern (CLAUDE.md).

---

## Step 1: Scan

Read every artifact **in scope** (Step 0) and run the checks below - for an area scope, only that area's artifacts and their direct cross-references; for whole-workspace, all of them. Collect findings; do not fix yet.

| Dimension | What is checked |
|---|---|
| **Structure** | Feature Cards match the canonical template (sections 1-4 + Subtasks; frontmatter: id, title, status, stripe, feature_set, actor, owner, priority, estimate, prd_ref, feature_flag, flag_default). Registers match current format and header. |
| **ID & naming** | FEAT/BR/TBL/FS IDs well-formed (`FEAT-[DOMAIN]-NNN`, `BR-[DOMAIN]-NNN`, `TBL-[DOMAIN]-NN`, `FS-NN`) and unique. Feature names follow `<action> <result> <object>`, strong verb, object = entity. The 7 anti-patterns flagged. |
| **Cross-references** | Every `BR-ID` / `TBL-ID` / entity link in a Feature Card resolves to the register. `feature_set` matches feature_list. `stripe` is a real stripe. No dangling links. |
| **Lifecycle** | `status` is one of the canonical 6 (`1_Backlog`..`6_Shipped`). No orphaned or invalid states. |
| **Version drift** | Any of the Step 0 drift signals → migration finding. |
| **Completeness** | Every feature in feature_list has a card; every card has its required sections; registers are initialized; state.json flags match reality. |
| **Notion sync** (if configured) | Local `status` vs Notion `Status` mismatch surfaced (drift log, like pm-stripe). |

---

## Step 2: Audit report

Save to: `pureinn-workspace/[project-slug]/audit/audit_report.md`

Score and group every finding by severity:

| Severity | Meaning | Examples |
|---|---|---|
| **P0** | Broken - blocks work | Dangling BR-ID reference, invalid status value, feature_list entry with no card |
| **P1** | Drift that causes errors | Old lifecycle state names, inconsistent FS-NN, naming anti-pattern on an active feature |
| **P2** | Missing newer structure | No `feature_set`/`estimate` field, no `## Subtasks` section, incomplete card |
| **P3** | Cosmetic | Formatting, path-slash convention, optional field gaps |

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
```

Present the score and P0/P1 summary to the user before fixing.

---

## Step 3: Fix

- **Mechanical (auto-fix):** ID format normalization, old → new lifecycle state names, missing `feature_set`/`estimate`/`Subtasks` scaffolding added, `notion.*` → `notion_ids.*`, path-slash convention, dead-link repair where the target is unambiguous. Apply in place; report a diff summary.
- **Judgment (ask):** anything where the fix changes meaning - a naming anti-pattern rewrite, an ambiguous dangling reference, a feature that may need splitting, a missing card that may be intentional. Batch these via the grouped AskUserQuestion pattern (CLAUDE.md), 2-4 per round, confirm, apply.

Never silently change a rule value, an acceptance criterion, or a business decision - those are out of scope (route to `pm-feature-design` / `pm-business-rules-library`).

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

```
---
**Čo si teraz má:** Workspace zladený s aktuálnymi Pureinn konvenciami - opravené ID, naming,
cross-refs, lifecycle a doplnená novšia štruktúra. Audit report ukazuje čo bolo a čo zostáva.

**Ďalší krok:** `/pm-stripe` — pokračuj v JIT delivery na čistom workspace.
Alebo `/pureinn` pre phase gate check.

**Môžeš preskočiť ak:** Workspace práve vznikol aktuálnou verziou frameworku (greenfield) - drift
neexistuje, audit nepridáva hodnotu.
```
