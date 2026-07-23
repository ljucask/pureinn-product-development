# Phase 4 - Domain Modeling + Register Setup

Initialize the four Live Registers that become the source of truth for the entire build phase. Map entities, define business rules, document process flows, and address privacy requirements.

**Duration:** 3-5 days · **Gate type:** Soft gate · **Playbooks:** Greenfield, Feature Implementation (new domain)

---

## How to read this page

Everything here is initialized in **Draft**, not finalized - the "Draft until JIT" principle. Guard conditions and exact rule values are finalized just-in-time when `pm-feature-design` designs the feature that enforces them (Phase 6). Do not try to fully specify rules here - that produces upfront work that diverges from build reality.

---

## When to enter this phase

Enter after the PRD is frozen (Phase 3b exit). For Feature Implementation adding a new domain, run the domain-specific skills for that domain before entering the JIT build cycle - you don't redo the whole phase, just the registers for the new area.

**What you need before entering:** frozen PRD (`PRD_master.md`), Product Roadmap v1, domain knowledge (regulatory requirements, business logic, entity relationships).

---

## Step 1 - Domain Model (optional but recommended)

- **When to run / skip:** run once, early in this phase, for any domain with real structural complexity. Skip only for a trivial domain (few entities, no meaningful relationships) - `pm-entity-registry` alone covers that.
- **Gather first:** frozen PRD's Business Capabilities.
- **Command:** `/pm-domain-model`
- **What you get:** `domain-model.md` - the high-level ERD and relationship overview, the strategic map.
- **What it does NOT give you:** entity states or guard conditions - that's Step 2, the operational detail underneath this map.
- **Done when:** every domain boundary and major entity relationship is drawn.

---

## Step 2 - Entity Registry (R1)

- **When to run / skip:** always run - required, not optional.
- **Gather first:** Domain Model (Step 1) if it exists.
- **Command:** `/pm-entity-registry`
- **What you get:** `entities.md` (Register 1) - detailed entity list with states and Mermaid state machines per entity. Guard conditions start as `TBD` here - finalized JIT in Phase 6.
- **What it does NOT give you:** finalized guard conditions. `TBD` here is expected and correct, not a gap to fill now.
- **Done when:** every entity has its full state machine drawn, even with guards still `TBD`.

---

## Step 3 - Business Rules Library (R2-R3)

- **When to run / skip:** always run.
- **Gather first:** Entity Registry (Step 2) - rules reference entity states.
- **Command:** `/pm-business-rules-library`
- **What you get:** `business_rules.md` (Register 2) with rules in Draft (`BR-[DOMAIN]-[NUMBER]` IDs), and `decision_models.md` (Register 3) with decision tables in Draft.
- **What it does NOT give you:** finalized rule values - Draft captures intent, exact values finalize JIT per feature in Phase 6.
- **Done when:** every known business rule has a Draft entry with an ID, even if the exact value is still open.

---

## Step 4 - Privacy Requirements

- **When to run / skip:** run when the product handles PII or is subject to any data-protection regime. Skip only for a domain with genuinely no personal data (rare).
- **Gather first:** Entity Registry - PII lives on specific entities.
- **Command:** `/pm-privacy-requirements`
- **What you get:** PII Inventory, Privacy Requirements, GDPR/regulatory action plan.
- **What it does NOT give you:** implementation - this is the requirement, not the code that enforces it.
- **Done when:** every entity holding PII is in the inventory with its handling requirement.

---

## Step 5 - Process Flows

- **When to run / skip:** run for any product with more than one user type or a non-trivial end-to-end flow. Skip only for a single-user-type, single-flow product.
- **Gather first:** Entity Registry (references entity states by name, no duplication).
- **Command:** `/pm-process-flows`
- **What you get:** system user types (not just end users), an E2E process map per domain, and per-user flows connected to screens (loading/empty/error states) - feeds `pm-feature-design`'s UX sections later.
- **What it does NOT give you:** screen-level wireframes - that's the designer's job (impeccable/Figma), using this as the brief.
- **Done when:** every user type has at least one flow connected to real screen states.

---

## Step 6 - Product Roadmap (v2)

- **When to run / skip:** always run, closing this phase.
- **Gather first:** all of Steps 1-5.
- **Command:** `/pm-product-roadmap`
- **What you get:** Product Roadmap v2 - the v1 strategic roadmap enriched with domain constraints discovered in this phase.
- **What it does NOT give you:** feature-level delivery detail - that's v3, after Phase 5.
- **Done when:** roadmap phases account for any domain constraint that changes sequencing (e.g. a regulatory dependency).

---

## pm-domain-model vs. pm-entity-registry - which to reach for

| | pm-domain-model | pm-entity-registry |
|---|---|---|
| Level | High-level (strategic) | Detailed (operational) |
| Output | ERD + relationship overview | Entity list + state machines per entity |
| Required? | Optional (recommended) | Required |

`pm-domain-model` is the map; `pm-entity-registry` is the living source of truth that Phase 6 reads from every time.

---

## The four Live Registers - state after this phase

| Register | File | State after Phase 4 | Finalized when |
|---|---|---|---|
| R1 | `entities.md` | Entity list + states + state machine shapes; guard conditions `TBD` | JIT via `pm-feature-design` per feature |
| R2 | `business_rules.md` | Rules in Draft with `BR-[DOMAIN]-[NUMBER]` IDs | JIT via `pm-feature-design` when the enforcing feature is designed |
| R3 | `decision_models.md` | Decision tables in Draft | JIT via `pm-feature-design` |
| R4 | `feature_list.md` | Not yet initialized | Phase 5 (`pm-features-list` + `pm-mvp-scope`) |

---

## What you exit with

- **Domain Model + ERD** - structural map of the product's domain
- **entities.md** (R1) - entity list + state machines in Draft
- **business_rules.md** (R2) - business rules in Draft
- **decision_models.md** (R3) - decision tables in Draft
- **PII Inventory + Privacy Requirements** - GDPR/regulatory compliance baseline
- **Process Flows + User Flows** - business and UX flow documentation
- **Product Roadmap v2** - roadmap updated with domain constraints

---

## Phase exit gate

Run `/pureinn` to check the Phase 4 exit gate and advance to Phase 5.

**Gate type: Soft.** All four registers must exist (even in Draft/stub form). Process flows and privacy requirements are checked. Gaps are named and you can proceed acknowledging them.
