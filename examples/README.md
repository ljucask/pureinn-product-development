# Pureinn - Framework Examples

Real-world showcase artifacts demonstrating the FDD+SDD framework in action.

These are not templates with placeholders. They are complete, realistic outputs showing what each register and Feature Card looks like for an actual use case.

---

## Available examples

### [SaaS Subscription Billing](saas-subscription/)

**Context:** Existing SaaS product adds a subscription billing domain as a new major initiative. Demonstrates the Feature Implementation path with Initiative PRD + append mode on all 4 living registers.

**What this example shows:**
- Initiative PRD scoped to the billing domain
- `domain/entities.md` - Subscription, Invoice, and PaymentMethod entities with full state machines
- `domain/business_rules.md` - Critical and operational rules with BR-SUB-*, BR-PAY-*, BR-REG-* IDs
- `features/feature_list.md` - 10 features with FEAT-SUB-NNN IDs, KANO, Stripe assignment
- `features/cards/FEAT-SUB-001.md` - "Subscribe to a plan" - **complete Feature Card, all 4 sections, status: 6_Promoted_to_Build**
- `features/cards/FEAT-SUB-003.md` - "Cancel subscription" - **Sections 1-3 complete, status: 3_Design_Inspection_Passed** (pre-build state)

**Phases illustrated:** Feature Implementation Track B → Initiative PRD → Phase 4 append → Phase 5 append → Phase 6+7 JIT cycle

---

## How to read these examples

Each file is structured exactly as the live registers and Feature Cards in real projects. The artifact formats match what skills generate.

**feature_list.md** = Live Register 4 - the full feature backlog with IDs, status, and stripe assignment.

**entities.md** = Live Register 1 - entity states and Mermaid state machines. Claude Code reads this before implementing any feature.

**business_rules.md** = Live Register 2 - rules referenced by ID in Feature Cards. BR-IDs appear in Feature Card Section 1 (Biznis Mantinely).

**Feature Card - 6_Promoted_to_Build** = what a feature looks like after the full JIT cycle: design → inspection → build → code inspection → promote. Section 4 (Realizacny Protokol) is filled.

**Feature Card - 3_Design_Inspection_Passed** = what a feature looks like just before entering build. Sections 1-3 complete, Section 4 empty.
