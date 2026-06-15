# Pureinn - Framework Examples

Real-world showcase artifacts demonstrating the FDD+SDD framework in action.

These are not templates with placeholders. They are complete, realistic outputs showing what each register and Feature Card looks like for an actual use case.

---

## Available examples

### [SaaS Subscription Billing](saas-subscription/)

**Context:** Existing SaaS product (ProjectFlow - B2B project management) adds a subscription billing domain as a new major initiative. Demonstrates the full workflow: product-level Phase 3b artifacts + Feature Implementation path with Initiative PRD + append mode on all 4 living registers.

**What this example shows:**
- `product/PRD_master.md` - Product PRD for the core product (Phase 3b exit artifact). Shows: validated problem statement, 5-domain Business Capabilities (AUTH, WS, PROJ, TASK, TEAM), explicit out-of-scope list, critical assumptions, and artifact input map. Frozen after creation.
- `product/product-roadmap-v3.md` - Product Roadmap at v3 (all 3 versions in one document). Shows: 3 strategic phases with exit criteria, Phase 1 completed with real outcome data, MVP Delivery View with Delivery Stripes for subscription billing, "not building" list as strategic decision log.
- `initiatives/subscription-billing/prd.md` - Initiative PRD scoped to the billing domain
- `domain/domain_model.md` - Billing domain entities (Subscription, Invoice, PaymentMethod) with attributes, relationships, state machines, events, and ERD diagrams
- `domain/entities.md` - Live Register 1: entity state machines with JIT guard conditions
- `domain/business_rules.md` - Live Register 2: critical and operational rules with BR-SUB-*, BR-PAY-*, BR-REG-* IDs
- `domain/decision_models.md` - Live Register 3: decision tables (TBL), decision tree (TRE), and scoring model (SCR) covering renewal outcomes, plan downgrade eligibility, card expiry handling, and churn risk
- `features/feature_list.md` - 10 features with FEAT-SUB-NNN IDs, KANO, Stripe assignment
- `features/cards/FEAT-SUB-001.md` - "Subscribe to a plan" - **complete Feature Card, all 4 sections, status: 6_Shipped**
- `features/cards/FEAT-SUB-003.md` - "Cancel subscription" - **Sections 1-3 complete, status: 3_Ready_to_Build** (pre-build state)

**Phases illustrated:** Phase 3b (PRD + Roadmap) → Feature Implementation Track B → Initiative PRD → Phase 4 append → Phase 5 append → Phase 6+7 JIT cycle

---

## How to read these examples

Each file is structured exactly as the live registers and Feature Cards in real projects. The artifact formats match what skills generate.

**feature_list.md** = Live Register 4 - the full feature backlog with IDs, status, and stripe assignment.

**domain_model.md** = Phase 4 foundational artifact - entity catalogue, attributes, relationships, state machines, events, ERD diagrams. Input for all other Phase 4-6 registers.

**entities.md** = Live Register 1 - entity states and Mermaid state machines. Claude Code reads this before implementing any feature.

**business_rules.md** = Live Register 2 - rules referenced by ID in Feature Cards. BR-IDs appear in Feature Card Section 1 (Biznis Mantinely).

**decision_models.md** = Live Register 3 - decision tables (TBL), decision trees (TRE), and scoring models (SCR). TBL-IDs and TRE-IDs appear in Feature Card Section 1 alongside BR-IDs. Claude Code uses these to generate unit test coverage for edge cases.

**Feature Card - 6_Shipped** = what a feature looks like after the full JIT cycle: design → inspection → build → code inspection → promote. Section 4 (Realizacny Protokol) is filled.

**Feature Card - 3_Ready_to_Build** = what a feature looks like just before entering build. Sections 1-3 complete, Section 4 empty.
