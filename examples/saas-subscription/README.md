# Example: SaaS Subscription Billing

**Workflow diagram:** [View on Excalidraw](https://excalidraw.com/#json=9qmQbUdyAoxvAZSoUoG2l,KZrO_YJXIdcl7KWKE9tnPw)

---

This example shows a complete FDD+SDD workflow run for a subscription billing initiative added to an existing SaaS product (ProjectFlow). It is a realistic representation of what the framework produces - not a template, not a simplified stub.

**Scenario:** The product has an existing core (project management workspace, user auth, teams). A new initiative - automated subscription billing via Stripe - is added using the Feature Implementation playbook, Track B (discovery needed, new domain).

---

## What each file shows

### `initiatives/subscription-billing/prd.md`
The Initiative PRD written after Track B discovery. Covers the business capabilities (BC-01 through BC-05), success metrics, scope boundaries, constraints (Stripe, GDPR, PCI DSS), and open questions. This is the scoped PRD for this initiative - not the product-level PRD_master.md.

### `domain/entities.md`
The Entity & State Registry (Live Register 1) shown in **append mode**. The Subscription, Invoice, and PaymentMethod entities were added to existing product entities. Each entity includes: state table, Mermaid stateDiagram-v2, full transitions table with guard conditions, and illegal transitions. Guard conditions marked "finalized: FEAT-SUB-001" show JIT enrichment happening during pm-feature-design just before build.

### `domain/business_rules.md`
The Business Rules Library (Live Register 2) shown in **append mode**. Four new rule categories added: BR-SUB-*, BR-PAY-*, BR-INV-*, BR-REG-*. All rules have Status: Final and are cross-referenced to the features that enforce them. Each rule includes the formula/condition, enforcement point, and exceptions.

### `features/feature_list.md`
The Feature List (Live Register 4) shown in **append mode**. 10 features (FEAT-SUB-001..010) with KANO classification, V×C matrix placement, Delivery Stripe assignment, current status, business rule references, and feature flags. Includes the dependency map and Delivery Stripe overview showing 3 stripes.

### `features/cards/FEAT-SUB-001.md`
**Status: 6_Promoted_to_Build (complete - all 4 sections)**

The complete lifecycle of a Feature Card, from spec through to promoted build. Shows:
- Section 1: Business constraints table, entity guard conditions, explicit scope exclusions
- Section 2: Full acceptance criteria with happy path, two guard failure scenarios, flag OFF behavior, and edge cases table
- Section 3: Mermaid sequence diagram (8 participants), files to create/modify table
- Section 4: Realizacny Protokol - 7 commits with hashes, 10 test results, feature flag verification, Code Inspection sign-off

### `features/cards/FEAT-SUB-003.md`
**Status: 3_Design_Inspection_Passed (pre-build - Sections 1-3 complete)**

Shows the state of a Feature Card just after Design Inspection, before it enters build. Section 4 is intentionally empty - it is written just before the feature enters build, not upfront. The contrast with FEAT-SUB-001 illustrates the lifecycle progression.

---

## How this maps to the workflow

| Step | Skill used | Output file |
|---|---|---|
| Track B discovery + Initiative PRD | pm-prd [Initiative mode] | initiatives/subscription-billing/prd.md |
| Domain entities added | pm-entity-registry [append] | domain/entities.md |
| Business rules added | pm-business-rules-library [append] | domain/business_rules.md |
| Feature list + KANO + V×C | pm-features-list [FI append] | features/feature_list.md |
| JIT design, guard conditions, Section 1-3 | pm-feature-design | features/cards/FEAT-SUB-001.md (Sections 1-3) |
| Build, tests, code inspection | - | features/cards/FEAT-SUB-001.md (Section 4) |

---

## What this example does NOT show

- Phase 1-3 artifacts (project charter, personas, hypotheses, Lean Canvas) - those belong to the product level, not this initiative
- The Greenfield playbook path - this is Feature Implementation only
- PRD_master.md - that already existed for the core product; this initiative appended to the domain registers without touching it
- Decision models (domain/decision_models.md) - not needed for this domain; subscription state transitions are captured in entities.md
