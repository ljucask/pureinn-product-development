# Rebuild Playbook - Reference

Onboard an existing product into Pureinn. Two sub-paths depending on the state of your legacy documentation.

**Playbook:** Rebuild · **Use when:** a product was built outside Pureinn and you are onboarding it

---

## How to read this page

This is the detailed runbook behind [Playbook 2: Rebuild](../playbook-rebuild.md), which only makes the A1/A2 routing decision. Once you know your sub-path, the steps below are what you actually run.

---

## Which sub-path?

```
Legacy docs exist AND conflict with code or each other?
            │
      ┌─────┴─────┐
      │ Yes       │ No (clean or absent)
      ▼           ▼
  A1 RECONCILE   A2 BOOTSTRAP
```

| Situation | Sub-path |
|---|---|
| Legacy docs (BRD, FSD, domain models) exist but conflict with the actual code | **A1 Reconcile** |
| Docs are clean, consistent with code, or don't exist at all | **A2 Bootstrap** |

Both sub-paths funnel into the **[JIT delivery engine](../phase-6-build/index.md)** once onboarding is complete.

---

## A1 - Reconcile (conflicting docs)

The full rebuild: reconcile the codebase against the legacy docs, produce a Reconciliation Report, and rebuild the registers and feature inventory clean.

**Use when:** docs are stale, contradictory, or the team is changing and needs one trustworthy source of truth.

### Source-of-truth model (read this before running anything)

Reconciliation is asymmetric - know which side wins before you hit a conflict:

| Layer | Source of truth | On mismatch |
|---|---|---|
| Technical structure - entity/attribute/enum/state names, state-machine shape, what is implemented | **Code** | Rewrite docs to match code. Old name → glossary alias. |
| Business intent - rule values, decisions, *why* | **Legacy docs (BRD)** | If code implements a different rule → flag `DIV-NN` + ask the team: code bug or stale doc? |

**Code is never changed** - only documents. Docs that run ahead of code → marked `specified, not implemented` (goes to backlog). Business logic migrated fully now; feature technical design stays JIT (Phase 6).

### Step 0 - Prep

- **When to run / skip:** always, first.
- **Gather first:** every legacy doc (BRD, FSD, domain models) - read completely, not just index/summary files.
- **Command:** `/pureinn` + `/common-ground`, then put all legacy docs in `legacy-docs/`.
- **What you get:** workspace + tech context, source docs collected in one place.
- **Done when:** every legacy doc you have is in `legacy-docs/`, not scattered.

### Step 1 - Reconciliation Plan

- **When to run / skip:** always, after prep.
- **Gather first:** `legacy-docs/` + the codebase.
- **Command:** `/pm-reconcile`
- **What you get:** `reconciliation_plan.md` - which areas to reconcile, in what order.
- **What it does NOT give you:** the reconciliation itself - this is planning only, execution is the next steps.
- **Done when:** the plan names areas and a dependency-driven order (entities → rules → features).

### Step 2 - Domain

- **When to run / skip:** always, per the plan's order.
- **Command:** `/pm-reconcile domain`
- **What you get:** `entities.md` (R1) + glossary aliases (old name → canonical name).
- **Done when:** every entity, attribute, enum, and state-machine shape matches the code.

### Step 3 - Rules

- **When to run / skip:** always, after domain (rules reference entity states).
- **Command:** `/pm-reconcile rules`
- **What you get:** `business_rules.md` + `decision_models.md` (R2-3), transition guard conditions, `DIV-NN` flags on any code/doc mismatch.
- **Done when:** every legacy rule is either reconciled or flagged as a divergence for the team to resolve.

### Step 4 - Features

- **When to run / skip:** always, after rules.
- **Command:** `/pm-reconcile features`
- **What you get:** `feature_list.md` (R4) in FDD grammar, `FS-NN` grouping, Section 1 BR-IDs, stub cards.
- **Done when:** every shipped capability in the code has a corresponding feature entry.

### Monitor - anytime

- **Command:** `/pm-reconcile-status`
- **What you get:** dashboard of done/pending areas, open divergences, disposal-readiness. Run this whenever you need a status check - it's not a sequential step.

### Step 5 - Verify (source-disposal gate)

- **When to run / skip:** always, after Steps 2-4 are complete. This is a **hard checkpoint** before you archive the legacy source.
- **Command:** `/pm-reconcile verify`
- **What you get:** `coverage_report.md` - re-reads the source one more time, proves every unit was transposed, incorporates any gaps found (not just reports them), and rules whether the legacy source is safe to archive.
- **What it does NOT give you:** permission to archive on a partial pass - if verify finds gaps, it closes them before ruling the source safe.
- **Done when:** verify rules the source safe to archive.

### Step 6 - Exit

```bash
/pm-product-roadmap    # delivery-driven roadmap
/pm-audit               # form check
archive source
/pm-stripe              # enter JIT delivery
```

**Order is dependency-driven:** entities → rules → features (R1 → R2 → R3 → R4). On a large product, run domain-by-domain rather than the whole codebase at once.

### A1 strategy note

Rebuild captures structure, not strategy. A1 skips Phase 1-3, so the strategic layer (vision, North Star Metric, business model, per-phase success criteria) is not captured. `/pm-product-roadmap` will produce a delivery-driven roadmap and ask for strategic inputs or mark them TBD.

If you want strategy-driven phasing: backfill the strategic layer before the roadmap (`/pm-business-model` + a North Star Metric + a 12-month goal).

---

## A2 - Bootstrap (clean or no docs)

Docs are already clean or absent - just sync current state from the code. No reconciliation needed.

- **When to run / skip:** run when there's no doc/code conflict to resolve (that's A1's job).
- **Gather first:** nothing beyond the existing codebase.

| Step | Command | What you get |
|---|---|---|
| 1 | `/pureinn` | Workspace setup, `state.json`, `pureinn-variables.md` |
| 2 | `/common-ground` (fullstack-dev-skills) | Technical context: stack, APIs, domain model, debt → `COMMON-GROUND.md` |
| 3 | `/pm-glossary` | Domain glossary |
| 4 | `/pm-entity-registry` | `entities.md` (R1) extracted from existing codebase |
| 5 | `/pm-business-rules-library` | `business_rules.md` + `decision_models.md` (R2-3) extracted |
| 6 | `/pm-reverse-extract` | `feature_list.md` (R4) + Feature hierarchy → Notion |

`pm-reverse-extract` extracts what it can from the codebase and shows the result before proceeding - you confirm or correct. Use it **instead of** `pm-features-list` + `pm-mvp-scope`.

**Done when:** you've confirmed the extracted feature inventory and registers reflect the actual codebase.

---

## Rebuild skills reference

| Skill | Description |
|---|---|
| [pm-reconcile](pm-reconcile.md) | Multi-mode reconciliation engine (plan / domain / rules / features / verify) |
| [pm-reconcile-status](pm-reconcile-status.md) | Reconciliation progress dashboard |
| [pm-reverse-extract](pm-reverse-extract.md) | Extract feature inventory from existing codebase |
| [pm-onboarding](../cross-phase/index.md#pm-onboarding) | Generate role-specific onboarding briefs (cross-phase) |

---

## After Rebuild

Both A1 and A2 exit into Feature Implementation. Once the registers exist and the feature inventory is complete, run:

```bash
/pureinn [project-slug]          # resume context
/pm-feature-design [FEAT-ID]     # JIT spec for the next feature
```

Then enter the [JIT delivery engine](../phase-6-build/index.md).
