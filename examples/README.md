# Pureinn - Framework Examples

Real-world showcase artifacts demonstrating the FDD+SDD framework in action.

These are not templates with placeholders. They are complete, realistic outputs showing what each register, artifact, and Feature Card looks like for an actual use case - matched to the current version of every skill's schema and conventions.

---

## Available examples

### [PureHunger - food delivery marketplace](food-delivery-app/)

**Context:** Greenfield product - a hyper-local food delivery marketplace (PureHunger) launching in Boise, Idaho, built by a 3-person founding team (CEO/Product, CTO, Head of Growth). Runs the full Greenfield playbook end to end: Foundation through Build, plus the cross-phase skills that don't wait for a phase gate.

**What this example shows:**

**Phase 1 - Foundation**
- `artifacts/phase-1-foundation/project-charter.md` - Project Charter + Assumptions & Risks Register, with the riskiest assumption (restaurants accepting 12% commission) named explicitly
- `artifacts/phase-1-foundation/team-roster.md` - Team Roster + Decision Rights Matrix + Skill Gap Assessment, flagging a real engineering capacity gap that blocks Phase 6
- `artifacts/phase-1-foundation/comms-charter.md` - Communication Charter right-sized for a 3-person team
- `artifacts/phase-1-foundation/stakeholder-map.md` - Stakeholder Map + RACI + Escalation Tree, including external stakeholders (an angel investor, two restaurant partners)

**Phase 2 - Discovery**
- `artifacts/phase-2-discovery/personas.md` - Customer Segments, two full Personas with Empathy Maps, provenance-tracked (real VOC vs. synthetic vs. founder-assumed)
- `artifacts/phase-2-discovery/jtbd-analysis.md` - Job stories + Forces Diagrams for both personas
- `artifacts/phase-2-discovery/market-analysis.md` - TAM/SAM/SOM, Competitor Analysis, SWOT, Market Timing Rationale
- `artifacts/phase-2-discovery/problem-validation.md` - Phase 2 exit synthesis with an honest "Partially validated" verdict, not an inflated pass

**Phase 3a - Validation**
- `artifacts/phase-3a-validation/design-thinking.md` - Problem Statement, POV, HMW questions, Elevator Pitch
- `artifacts/phase-3a-validation/hypotheses-go-no-go.md` - Hypothesis Register with real experiment results and a **GO** verdict

**Phase 3b - Commercial Definition**
- `artifacts/phase-3b-definition/lean-canvas.md` - full Lean Canvas
- `artifacts/phase-3b-definition/kpis.md` - North Star Metric, AARRR, first-two-quarter OKRs
- `product/PRD_master.md` - Product PRD (Phase 3b exit artifact, frozen after creation), with four named Business Capabilities that the Domain Model and Feature List are derived from directly

**Phase 4 - Domain Modeling**
- `domain/domain_model.md` - full Domain Model (entity catalogue, attributes, relationships, states, events, ERD)
- `domain/entities.md` - Live Register 1: entity state machines with JIT guard conditions
- `domain/business_rules.md` - Live Register 2, demonstrating the **Core / Critical / Governance three-way split** (19 rules: 6 Core, 7 Critical, 6 Governance), each tier tagged with the skill that produces it
- `domain/decision_models.md` - Live Register 3: three decision tables (TBL-REST-01 restaurant onboarding approval, TBL-PAY-01 cancellation refund amount, TBL-DEL-01 courier reinstatement outcome), each cross-referencing the BR-IDs and entity transitions they support
- `artifacts/phase-4-domain/process-flows.md` - system user types, E2E process maps, per-user user flows

**Phase 5 - Feature Planning**
- `features/feature_list.md` - Live Register 4: 23 features across 4 domains, table-indexed, with KANO Analysis and Value vs. Complexity Matrix. MVP membership lives entirely in the `phase` field - there is no separate `mvp` boolean anywhere in this register
- `features/delivery-stripes.md` - 3 Delivery Stripes with feature assignment
- `artifacts/phase-5-planning/mvp-scope.md` - IN/POST-MVP/CUT decision per feature
- `product/product-roadmap-v3.md` - Product Roadmap at v3 (all 3 versions in one living document)

**Phase 6-7 - JIT Delivery**
- `features/cards/FEAT-ORD-001.md` - "Place order from restaurant cart" - **complete Feature Card, all 4 sections, status: 6_Shipped**
- `features/cards/FEAT-DEL-002.md` - "Courier delivery assignment and live tracking" - **Sections 1-3 complete, status: 3_Ready_to_Build** (pre-build state), referencing a Critical rule (BR-DEL-003) added mid-cycle by the Domain register and picked up correctly by the Feature Card

**Cross-phase**
- `artifacts/cross-phase/meeting-2026-02-10-product-review.md` - a captured Product Review meeting where the founders decide to ship guest checkout in response to a real checkout drop-off number, with action items tagged to their destination (Feature Card / framework skill)
- `artifacts/cross-phase/onboarding-brief-developer.md` - a Developer-role onboarding brief for a new backend hire, landing them directly on the next feature to build

---

## How to read this example

Every file is structured exactly as the live registers, phase artifacts, and Feature Cards produced by a real Pureinn run - the formats match the current schema each skill generates, including frontmatter fields, table structures, and cross-references between files (Feature Cards reference Business Rule IDs and entity states that actually exist in the domain registers; the feature list references entities that actually exist; the PRD's Business Capabilities are the ones the Domain Model and Feature List were derived from).

**`business_rules.md`** is the artifact most worth reading closely - it is the concrete demonstration of the framework's three-way rule split (Core / Critical / Governance), each produced by its own skill (`pm-business-rule-core`, `pm-business-rule-critical`, `pm-business-rule-governance`) but living in one register.

**Feature Card - 6_Shipped** (`FEAT-ORD-001.md`) = what a feature looks like after the full JIT cycle: design → inspection → build → code inspection → promote. Section 4 (Realizacny Protokol) is filled.

**Feature Card - 3_Ready_to_Build** (`FEAT-DEL-002.md`) = what a feature looks like just before entering build. Sections 1-3 complete, Section 4 empty.

**`feature_list.md`** = Live Register 4 - the full feature backlog, table-indexed with IDs, KANO/V×C classification, phase, and stripe assignment.

**`entities.md`** = Live Register 1 - entity states and Mermaid state machines. Claude Code reads this before implementing any feature.

**`decision_models.md`** = Live Register 3 - decision tables (TBL-IDs) for multi-condition logic that a flat rule statement can't express cleanly (onboarding approval, refund amount, reinstatement outcome). Each table links back to the BR-ID(s) it supports and the entity transition it gates.
