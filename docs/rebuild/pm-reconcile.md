# pm-reconcile

> Rebuild playbook - reconciles codebase against legacy docs to produce a clean Pureinn structure that matches reality

**Phase:** Rebuild playbook  
**Agent mode:** `never` - value is the live dialogue (business-logic conflicts require human decisions)  
**Version:** 1.2.0  
**Triggers:** reconcile, rebuild, migration, existing product, old docs, BRD reconciliation, team handover, codebase vs docs, onboard existing product, rebuild from code, source coverage, verify transposition, disposal readiness, archive source

---

## When to use

When a product was built outside Pureinn, legacy docs disagree with the code and each other, and the team needs one trustworthy source of truth. Typically run at Rebuild playbook entry or when onboarding an existing product into the framework.

**Agent mode is not supported.** Business-logic conflicts require human decisions (which value is correct - the code or the doc?). Invoking with `--agent` will warn once and proceed interactively.

---

## What it produces

1. **Reconciliation Plan** (`reconcile/reconciliation_plan.md`) - which areas to reconcile, in what order, into which Pureinn artifacts
2. **Reconciliation Report** (`reconcile/reconciliation_report.md`) - living audit log per area: what matched, what diverged (`DIV-NN` entries), human decisions recorded
3. **Rebuilt Live Registers** - `entities.md`, `business_rules.md`, `decision_models.md`, `feature_list.md` - structurally aligned to code, carrying business logic from docs, every divergence visible
4. **Stub Feature Cards** - for specified-not-yet-implemented capabilities discovered in the source

---

## How to invoke - seven modes

```bash
/pm-reconcile                       # Plan / route: no plan → build plan; plan exists → status + next area
/pm-reconcile plan                  # Force rebuild the reconciliation plan
/pm-reconcile domain                # Execute: entities + state machines → entities.md (Register 1)
/pm-reconcile rules                 # Execute: business rules + decision models → business_rules.md + decision_models.md (Registers 2-3)
/pm-reconcile features              # Execute: feature inventory → feature_list.md + stub cards (Register 4)
/pm-reconcile [other-area]          # Execute: any extra area the plan defined (events, integrations, etc.)
/pm-reconcile verify [area]         # Verify + incorporate: re-read source, prove coverage, fill gaps, rule on disposal readiness
```

Default area execution order: `domain` → `rules` → `features` (dependency-driven: entities are the vocabulary, rules reference entities, features reference rules and entities).

---

## Source of truth model (asymmetric reconciliation)

| Layer | Source of truth | On mismatch |
|---|---|---|
| **Business intent** (rule values, what a feature should do, why) | **Legacy docs** | Surface as business-logic divergence (`DIV-NN`). Do NOT silently pick a side. Team rules "code is the bug" or "doc is stale". |
| **Technical structure** (entity names, attribute names, enum values, state names) | **Codebase** | Rewrite docs to match code. Mechanical, no question needed. Old doc name kept as alias in glossary. |

**Two hard rules:**
1. Never change the codebase. This skill rebuilds documents only.
2. Docs-ahead-of-code (specified but not yet implemented) → stub Feature Card at `1_Backlog` status. Do NOT include in Live Registers 1-3. Backlog items must be carded to survive source archival.

---

## The source is whatever you point to

The skill never assumes the source is a "BRD" or any specific filename. At PLAN time, it asks where the source of business intent lives and deep-ingests whatever the user points to: FSD, Confluence/Notion space, wiki, spreadsheet, spec folder, any format.

---

## Multi-session support

Reconciliation spans multiple sessions. Progress is held in `state.json`. Use `/pm-reconcile-status` to see a dashboard of completed/pending areas and open divergences before sitting down to a new session.

---

## Rebuild vs. strategic layer

Reconcile captures **structure** (entities, rules, features), not the **strategic layer** (vision, North Star, business model, per-phase success criteria). If you want strategy-driven roadmap phases, backfill the strategic layer after reconcile completes before running `/pm-product-roadmap`. If a delivery-driven roadmap is acceptable, run roadmap directly and let it mark strategic fields TBD.

This is a fork the team should decide consciously. The skill surfaces it at handoff.

---

## Dependencies

**Required:**
- A codebase accessible to Claude Code
- A source of business intent (legacy docs, any format) pointed to by the user
- Pureinn workspace initialized (`/pureinn` or `/pureinn rebuild`)

**Produces for:**
- `pm-entity-registry` - entities.md (Rebuild mode, Register 1)
- `pm-business-rules-library` - business_rules.md + decision_models.md (Rebuild mode, Registers 2-3)
- `pm-reverse-extract` - uses reconciliation_report.md as authoritative input
- `pm-audit` - runs after reconcile as the verification pass
- `pm-domain-model` - builds cross-domain ERD on top of reconciled entities

**Related skills:** `pm-reconcile-status`, `pm-reverse-extract`, `pm-entity-registry`, `pm-business-rules-library`, `pm-domain-model`, `pm-audit`
