# Phase 4 - Domain Modeling + Register Setup

Initialize the four Live Registers that become the source of truth for the entire build phase. Map entities, define business rules, document process flows, and address privacy requirements.

**Duration:** 3-5 days  
**Gate type:** Soft gate  
**Playbooks:** Greenfield, Feature Implementation (new domain)

---

## When to enter this phase

Enter Phase 4 after the PRD is frozen (Phase 3b exit). For Feature Implementation adding a new domain, run the domain-specific skills for that domain before entering the JIT build cycle.

The Live Registers initialized here are enriched continuously during Phase 6-7 - they are never "done" upfront.

---

## What you need before entering

- Frozen PRD (`PRD_master.md`)
- Product Roadmap v1
- Domain knowledge (regulatory requirements, business logic, entity relationships)

---

## Skills in this phase

| Skill | What it does | Output |
|---|---|---|
| [pm-domain-model](pm-domain-model.md) | High-level domain model and ERD - the structural map of entities and their relationships | `domain-model.md` + optional Excalidraw diagram |
| [pm-entity-registry](pm-entity-registry.md) | Detailed entity list with states and Mermaid state machines per entity; guard conditions added JIT | `entities.md` (Register 1) |
| [pm-business-rules-library](pm-business-rules-library.md) | Business rules and decision tables in Draft mode; finalized JIT per feature | `business_rules.md` (Register 2) + `decision_models.md` (Register 3) |
| [pm-privacy-requirements](pm-privacy-requirements.md) | PII inventory, privacy requirements, GDPR/regulatory action plan | PII Inventory, Privacy Requirements |
| [pm-process-flows](pm-process-flows.md) | System user types + E2E process map per domain + per-user flows connected to screens | Process Flows + User Flows |
| [pm-product-roadmap](pm-product-roadmap.md) | Phase 4 update: roadmap enriched with domain constraints | Product Roadmap v2 |

**Recommended order:**
```
pm-domain-model → pm-entity-registry → pm-business-rules-library
→ pm-privacy-requirements → pm-process-flows → pm-product-roadmap (v2)
```

---

## The four Live Registers

Phase 4 initializes all four:

| Register | File | Initialized state | Finalized when |
|---|---|---|---|
| R1 | `entities.md` | Entity list + states + state machine shapes; guard conditions TBD | JIT via `pm-feature-design` per feature |
| R2 | `business_rules.md` | Rules in Draft with `BR-[DOMAIN]-[NUMBER]` IDs | JIT via `pm-feature-design` when the enforcing feature is designed |
| R3 | `decision_models.md` | Decision tables in Draft | JIT via `pm-feature-design` |
| R4 | `feature_list.md` | Initialized in Phase 5 | Complete after `pm-features-list` + `pm-mvp-scope` |

**"Draft until JIT" principle:** business rules are documented in Draft during Phase 4 to capture intent. Guard conditions and exact rule values are finalized just-in-time when the feature that enforces the rule is designed. This prevents upfront over-specification that diverges from build reality.

---

## pm-domain-model vs. pm-entity-registry

| | pm-domain-model | pm-entity-registry |
|---|---|---|
| Level | High-level (strategic) | Detailed (operational) |
| Output | ERD + relationship overview | Entity list + state machines per entity |
| When to run | Once, early in Phase 4 | Phase 4, after domain model; updated JIT |
| Optional? | Optional (recommended) | Required |

`pm-domain-model` is the map; `pm-entity-registry` is the living source of truth.

---

## pm-process-flows: what it produces

A lean artifact that lives between the business view and the designer brief:

- **System user types** - who interacts with the system (not just end users)
- **E2E process map per domain** - business-level view of how things flow
- **Per-user flows connected to screens** - what each user type does, linked to UI screens/states (loading, empty, error states)

References entity states by name - no duplication with the entity registry. Feeds `pm-feature-design` UX sections.

---

## What you exit with

- **Domain Model + ERD** - structural map of the product's domain
- **entities.md** (Register 1) - entity list + state machines in Draft
- **business_rules.md** (Register 2) - business rules in Draft
- **decision_models.md** (Register 3) - decision tables in Draft
- **PII Inventory + Privacy Requirements** - GDPR/regulatory compliance baseline
- **Process Flows + User Flows** - business and UX flow documentation
- **Product Roadmap v2** - roadmap updated with domain constraints

---

## Phase exit gate

Run `/pureinn` to check the Phase 4 exit gate and advance to Phase 5.

**Gate type: Soft.** All four registers must exist (even in Draft/stub form). Process flows and privacy requirements are checked. Gaps are named and you can proceed acknowledging them.
