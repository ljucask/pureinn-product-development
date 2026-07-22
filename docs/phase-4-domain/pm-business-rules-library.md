# pm-business-rules-library

> Live Registers 2 and 3 of 5 - Business Rules Library (business_rules.md) and Decision Models Matrix (decision_models.md)

**Phase:** 4-5 (initial draft); enriched JIT in Phase 6  
**Agent mode:** `decision` - drafts, then requires your review  
**Version:** 2.1.0  
**Triggers:** business rules, decision models, business rules library, BR-ID, rule catalog, Phase 4, Phase 5

---

## When to use

Phase 4-5 transition. Run this skill once to create the library structure and capture known constraints, compliance rules, and high-level policies. In Phase 6, individual rules are added JIT via the focused single-rule helpers, not by re-running this skill.

---

## What it produces

**Live Register 2** (`domain/business_rules.md`) - Business Rules Library:
- Centralized catalog with unique IDs: `BR-[DOMAIN]-NNN`
- Rules organized by domain and priority class
- Each rule: ID, name, description, domain, priority class (Core/Critical/Governance), status (Draft/Final), rule text (exact or draft), applicable entities/states

**Live Register 3** (`domain/decision_models.md`) - Decision Models Matrix:
- Decision tables with IDs: `TBL-[DOMAIN]-NN`
- Multi-condition logic → single output (pricing, eligibility, risk matrices)
- Each table: ID, name, conditions, outcomes, entity/trigger references

**JIT enrichment:** Rules are captured in two stages:
1. **Draft (Phase 4-5)** - known constraints, compliance rules, high-level policies as raw text
2. **JIT finalization (Phase 6)** - exact formulas, guard conditions, and decision matrices completed just before the feature using them is built

---

## How to invoke

```bash
/pm-business-rules-library           # interactive - full library creation or update
/pm-business-rules-library --agent   # autonomous draft, requires review before finalizing
```

---

## Adding individual rules after the library exists

Do not re-run this skill to add a single rule. Use the focused helpers:

| Helper | What it adds | ID format |
|---|---|---|
| `/pm-business-rule-core` | High priority operational rule (matching, pricing, SLAs, fulfillment) | `BR-[DOMAIN]-NNN` |
| `/pm-business-rule-critical` | Critical hard invariant (financial loss, legal exposure, irreversible damage) | `BR-[DOMAIN]-NNN` |
| `/pm-business-rule-governance` | Compliance / policy rule (GDPR, regulatory, admin, data handling) | `BR-[DOMAIN]-NNN` |
| `/pm-decision-model` | Single decision table (multi-condition logic) | `TBL-[DOMAIN]-NN` |

These helpers are typically triggered from `pm-feature-design` when a feature surfaces a rule not yet in the register.

**What belongs in this library:**
- Corporate policies that apply across features
- Compliance and regulatory requirements
- Security and authorization rules
- Business logic that applies to multiple features or Feature Sets

**What does NOT belong here:**
- Feature-specific implementation details (go in Feature Cards)
- API contracts or payloads (go in ADRs)
- UI/UX rules (go in design docs)
- Technical architecture decisions (go in ADRs)

---

## Reconciled mode (Rebuild playbook)

When `reconcile/reconciliation_report.md` exists, it is the authoritative input. Business rule values come from the reconciled docs, expressed against real code entities. Rules tied to an unresolved divergence (`DIV-{DOMAIN}-NN` in the report and in `domain/open_questions.md`) stay `Draft` with a link to the report row; only divergence-free rules go `Final`.

---

## Dependencies

**Required before running:**
- `pm-entity-registry` - entities define the scope of rules; rules reference entity states

**Recommended:**
- `pm-domain-model` - domain boundaries scope rule application
- `pm-domain-analysis` - legal and regulatory requirements from Phase 2 inform Governance rules
- `pm-prd` - Business Capabilities section names the domains and processes

**Produces for:**
- `pm-feature-design` - Feature Cards reference rules by BR-ID; guard conditions added JIT
- `pm-features-list` - rule catalog informs which features have cross-cutting compliance dependencies
- `pm-stripe` - Design Inspection checklist references critical rules

**Related skills:** `pm-entity-registry`, `pm-business-rule-core`, `pm-business-rule-critical`, `pm-business-rule-governance`, `pm-decision-model`, `pm-open-questions`

---

## Open questions

A rule's exact formula, enforcement point, or a decision table's condition combinations that are genuinely unresolved (not just a draft-mode TBD awaiting normal JIT finalization) are logged directly in `domain/open_questions.md` (Live Register 5, `pm-open-questions`) - Type: Question, `OQ-{DOMAIN}-NN`.
