# Example: SaaS Subscription Billing

---

This example shows a complete FDD+SDD workflow run for a subscription billing initiative added to an existing SaaS product (ProjectFlow). It is a realistic representation of what the framework produces - not a template, not a simplified stub.

**Scenario:** The product has an existing core (project management workspace, user auth, teams). A new initiative - automated subscription billing via Stripe - is added using the Feature Implementation playbook, Track B (discovery needed, new domain).

---

## What each file shows - read in this order

### 1. `product/PRD_master.md`
The Product PRD - Phase 3b exit artifact for the core ProjectFlow product. Synthesizes all Phase 2 + 3a + 3b outputs (34 customer interviews, JTBD analysis, market sizing, Tech Feasibility, Business Model Canvas, KPIs). Covers: validated problem statement, primary persona (Martin the Engineering Team Lead), business capabilities across 5 domains (AUTH, WS, PROJ, TASK, TEAM, NOTIF), explicit out-of-scope decisions, regulatory constraints, and critical assumptions. Frozen after creation - new initiatives (like subscription billing) generate their own Initiative PRD without touching this document.

### 2. `product/product-roadmap-v3.md`
The Product Roadmap at version 3 - showing all three evolution stages in one document. v1 (Phase 3b): strategic phases and vision. v2 (Phase 4): domain constraints and WebSocket deferral incorporated. v3 (Phase 5): Delivery Stripes and Feature Sets added for the subscription billing initiative. Shows Phase 1 as complete with real outcome data, Phase 2 in progress, and Phase 3 planned with AI feature staging rationale. Demonstrates the version history and "not building" section as a strategic decision log.

### 3. `initiatives/subscription-billing/prd.md`
The Initiative PRD written after Track B discovery. Covers the business capabilities (BC-01 through BC-05), success metrics, scope boundaries, constraints (Stripe, GDPR, PCI DSS), and open questions. This is the scoped PRD for this initiative - not the product-level PRD_master.md.

### 2. `domain/domain_model.md`
The Domain Model - the Phase 4 foundation for everything else. Defines the Billing domain structure: entity catalogue (6 internal entities, 4 Stripe external entities), full entity definitions with attributes, relationships, state machines, events, enums, and ERD diagrams per entity. Read this before any Live Register - all other domain artifacts reference the entity IDs and structures defined here.

### 3. `domain/entities.md`
The Entity & State Registry (Live Register 1) shown in **append mode**. Subscription, Invoice, and PaymentMethod entities added to existing product entities. Each entity includes: state table, Mermaid stateDiagram-v2, full transitions table with guard conditions, and illegal transitions. Guard conditions marked "finalized: FEAT-SUB-001" show JIT enrichment happening during pm-feature-design just before build.

### 4. `domain/business_rules.md`
The Business Rules Library (Live Register 2) shown in **append mode**. Four new rule categories added: BR-SUB-*, BR-PAY-*, BR-INV-*, BR-REG-*. All rules have Status: Final and are cross-referenced to the features that enforce them. Each rule includes the formula/condition, enforcement point, and exceptions.

### 5. `domain/decision_models.md`
The Decision Models Matrix (Live Register 3) shown in **append mode**. Four models covering the complex conditional logic in the billing domain: TBL-SUB-01 (renewal outcome - all webhook/retry/grace period combinations), TBL-SUB-02 (plan downgrade eligibility - seats and storage constraints), TRE-PAY-01 (card expiry handling as a decision tree), SCR-SUB-01 (churn risk scoring model). Referenced by TBL-ID and TRE-ID in Feature Card Section 1 alongside BR-IDs.

### 6. `features/feature_list.md`
The Feature List (Live Register 4) shown in **append mode**. 10 features (FEAT-SUB-001..010) with KANO classification, V×C matrix placement, Delivery Stripe assignment, current status, business rule references, and feature flags. Includes the dependency map and Delivery Stripe overview showing 3 stripes.

### 7. `features/cards/FEAT-SUB-003.md`
**Status: 3_Ready_to_Build (pre-build - Sections 1-3 complete)**

Shows the state of a Feature Card just after Design Inspection, before it enters build. Section 4 is intentionally empty - it is written just before the feature enters build, not upfront. Read this before FEAT-SUB-001 to see the before state.

### 8. `features/cards/FEAT-SUB-001.md`
**Status: 6_Shipped (complete - all 4 sections)**

The complete lifecycle of a Feature Card, from spec through to promoted build. Shows:
- Section 1: Business constraints referencing BR-IDs and TBL-IDs, entity guard conditions, explicit scope exclusions
- Section 2: Full acceptance criteria with happy path, two guard failure scenarios, flag OFF behavior, and edge cases table
- Section 3: Mermaid sequence diagram (8 participants), files to create/modify table
- Section 4: Realizacny Protokol - 7 commits with hashes, 10 test results, feature flag verification, Code Inspection sign-off

---

## How this maps to the workflow

| Step | Skill used | Output file |
|---|---|---|
| Phase 2-3b synthesis → Product PRD | pm-prd [Product mode] | product/PRD_master.md |
| Roadmap v1 (Phase 3b) | pm-product-roadmap [v1] | product/product-roadmap-v3.md (v1 section) |
| Roadmap v2 (Phase 4, domain constraints) | pm-product-roadmap [v2 update] | product/product-roadmap-v3.md (v2 section) |
| Roadmap v3 (Phase 5, delivery stripes) | pm-product-roadmap [v3 update] | product/product-roadmap-v3.md (v3 section) |
| Track B discovery + Initiative PRD | pm-prd [Initiative mode] | initiatives/subscription-billing/prd.md |
| Domain model - entities, relationships, ERD | pm-domain-model [append] | domain/domain_model.md |
| Entity state machines added | pm-entity-registry [append] | domain/entities.md |
| Business rules added | pm-business-rules-library [append] | domain/business_rules.md |
| Decision tables and models added | pm-business-rules-library [append] | domain/decision_models.md |
| Feature list + KANO + V×C | pm-features-list [FI append] | features/feature_list.md |
| JIT design, guard conditions, Section 1-3 | pm-feature-design | features/cards/FEAT-SUB-001.md (Sections 1-3) |
| Build, tests, code inspection | - | features/cards/FEAT-SUB-001.md (Section 4) |

---

## What this example does NOT show

- Phase 1-3 artifacts (project charter, personas, hypotheses, Lean Canvas) - those belong to the product level and were inputs to PRD_master.md
- The Greenfield playbook path for domain model and feature work - this is Feature Implementation only
- Product Roadmap v1 and v2 as standalone files - product-roadmap-v3.md shows all three evolution stages in one document with a version history block
