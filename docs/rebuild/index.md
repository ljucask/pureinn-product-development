# Rebuild Playbook

Onboard an existing product into Pureinn. Two sub-paths depending on the state of your legacy documentation.

**Playbook:** Rebuild  
**Use when:** a product was built outside Pureinn and you are onboarding it

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

### Source-of-truth model

Reconciliation is asymmetric:

| Layer | Source of truth | On mismatch |
|---|---|---|
| Technical structure - entity/attribute/enum/state names, state-machine shape, what is implemented | **Code** | Rewrite docs to match code. Old name → glossary alias. |
| Business intent - rule values, decisions, *why* | **Legacy docs (BRD)** | If code implements a different rule → flag `DIV-NN` + ask the team: code bug or stale doc? |

**Code is never changed** - only documents. Docs that run ahead of code → marked `specified, not implemented` (goes to backlog). Business logic migrated fully now; feature technical design stays JIT.

### Skills

| Skill | What it does | Output |
|---|---|---|
| [pm-reconcile](pm-reconcile.md) | Inspects docs + code surface, defines reconciliation areas and order | `reconciliation_plan.md` |
| [pm-reconcile](pm-reconcile.md) (domain) | Entities, attributes, enums, state-machine structure | `entities.md` (R1) + glossary aliases |
| [pm-reconcile](pm-reconcile.md) (rules) | Business rules, decision models, transition guard conditions | `business_rules.md` + `decision_models.md` (R2-3) |
| [pm-reconcile](pm-reconcile.md) (features) | Feature inventory in FDD grammar, FS-NN grouping, Section 1 BR-IDs | `feature_list.md` (R4) + stub cards |
| [pm-reconcile-status](pm-reconcile-status.md) | Dashboard: done / pending areas, open divergences, disposal-readiness | Status report |
| [pm-reconcile](pm-reconcile.md) (verify) | Re-reads source, proves coverage, incorporates gaps, rules source safe to archive | `coverage_report.md` |

### Flow

| Phase | Command | What happens |
|---|---|---|
| Prep | `/pureinn` + `/common-ground` + put docs in `legacy-docs/` | Workspace, tech context, source docs in one folder |
| Plan | `/pm-reconcile` | Reconciliation plan with areas + order |
| Execute 1 | `/pm-reconcile domain` | Entities, states → R1 |
| Execute 2 | `/pm-reconcile rules` | Business rules, decision models → R2-3 |
| Execute 3 | `/pm-reconcile features` | Feature inventory → R4 + stub cards |
| Monitor | `/pm-reconcile-status` | Progress dashboard at any time |
| Verify | `/pm-reconcile verify` | Coverage proof + gap incorporation |
| Exit | `/pm-product-roadmap` → `/pm-audit` → archive source → `/pm-stripe` | Plan then form then JIT |

**Order is dependency-driven:** entities → rules → features (R1 → R2 → R3 → R4). On a large product, run domain-by-domain.

### A1 strategy note

Rebuild captures structure, not strategy. A1 skips Phase 1-3, so the strategic layer (vision, NSM, business model, per-phase success criteria) is not captured. `/pm-product-roadmap` will produce a delivery-driven roadmap and ask for strategic inputs or mark them TBD.

If you want strategy-driven phasing: backfill the strategic layer before the roadmap (`/pm-business-model` + a North Star Metric + a 12-month goal).

---

## A2 - Bootstrap (clean or no docs)

Docs are already clean or absent - just sync current state from the code. No reconciliation needed.

### Skills

| Step | Skill | Output |
|---|---|---|
| 1 | `/pureinn` | Workspace setup, `state.json`, `pureinn-variables.md` |
| 2 | `/common-ground` (fullstack-dev-skills) | Technical context: stack, APIs, domain model, debt → `COMMON-GROUND.md` |
| 3 | `/pm-glossary` | Domain glossary |
| 4 | `/pm-entity-registry` | `entities.md` (R1) extracted from existing codebase |
| 5 | `/pm-business-rules-library` | `business_rules.md` + `decision_models.md` (R2-3) extracted |
| 6 | `/pm-reverse-extract` | `feature_list.md` (R4) + Feature hierarchy → Notion |

`pm-reverse-extract` extracts what it can from the codebase and shows the result before proceeding - you confirm or correct. Use it **instead of** `pm-features-list` + `pm-mvp-scope`.

---

## Rebuild skills

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
