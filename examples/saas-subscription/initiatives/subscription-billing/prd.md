# Initiative PRD - Subscription Billing
> **Parent PRD:** product/PRD_master.md
> **Discovery source:** initiatives/subscription-billing/discovery/
> **Version:** 1.0
> **Last updated:** 2026-06-01
> **Status:** Approved - drives Phase 4 append + Phase 5 append

---

## 1. Initiative Context

**What triggered this initiative:** The product (a B2B project management SaaS) currently runs on manual invoicing with 30-day net terms. Sales cycle data shows 40% of churned trials cite "no self-serve billing" as the reason they did not convert. The decision was made to add automated subscription billing.

**Relationship to PRD_master:** PRD_master covers the core product - project management workspace, user auth, team collaboration. This initiative adds the billing domain as a distinct functional layer. All existing entities (User, Workspace, Team) remain unchanged.

**Initiative slug:** subscription-billing
**Domain code:** SUB (features: FEAT-SUB-*), PAY rules: BR-PAY-*, REG rules: BR-REG-*

---

## 2. Business Capabilities

*This section is the primary input for pm-entity-registry (append) and pm-business-rules-library (append).*

The billing domain must enable the product to:

**BC-01: Subscription lifecycle management**
The system must allow a user to subscribe to a plan (Starter / Pro / Enterprise), move through the subscription lifecycle (active, past due, cancelled), and enforce that access to product features is gated by subscription status. A workspace with no active subscription must have restricted access - read-only for existing data, no new content creation.

**BC-02: Automated payment collection**
The system must collect payments automatically on a recurring schedule (monthly or annual). Initial payment is collected at subscription creation. Renewal payments are attempted 3 days before the end of the billing period. Failed renewal payments must trigger a grace period (7 days) before restricting access. The system must never mark a payment as successful before the payment provider confirms it.

**BC-03: Invoice generation and compliance**
Every payment attempt (successful or failed) must generate an invoice. Invoices must include all legally required fields for VAT/tax compliance (buyer details, seller details, line items, tax rate, amount, invoice number). Invoices must be retained and downloadable for 7 years. Invoices must be immutable after issuance.

**BC-04: Plan management**
Users must be able to upgrade or downgrade plans. Upgrades take effect immediately with prorated billing. Downgrades take effect at the end of the current billing period. Users must be able to cancel their subscription with continued access until the end of the current billing period.

**BC-05: Payment method management**
Users must be able to add, update, and remove payment methods (credit/debit cards). The system must detect expired payment methods and notify users before renewal failure. The default payment method must always be explicitly set.

---

## 3. Success Metrics

| Metric | Target | Measurement method |
|---|---|---|
| Self-serve conversion rate | ≥ 25% of trials convert without sales touch | Billing dashboard: trial → paid conversions |
| Payment failure rate | < 5% of renewal attempts fail | Stripe dashboard: failed_payment_intent events |
| Involuntary churn (billing failure) | < 2% monthly | Subscriptions moved to Cancelled due to payment failure |
| Invoice compliance | 100% of invoices include required VAT fields | Automated invoice validation test |
| Time to first payment | ≤ 3 minutes from plan selection to active subscription | Frontend event tracking |

---

## 4. Scope

**In scope (this initiative):**
- Subscription creation (Starter, Pro plans; Enterprise = manual quote, not self-serve)
- Monthly and annual billing cycles
- Stripe as the sole payment provider (v1)
- Invoice generation, storage, and download
- Plan upgrades (immediate) and downgrades (end of period)
- Cancellation (end of period; no immediate cancellation in v1)
- Subscription renewal (automated)
- Payment method management (card only; bank transfer = post-MVP)
- Grace period handling on renewal failure
- Admin tools: view and manually adjust subscriptions

**Out of scope:**
- Enterprise plan self-serve (manual quote process remains)
- Multiple payment providers
- Refunds (manual process via Stripe dashboard in v1)
- Usage-based billing
- Multi-currency (EUR only in v1)
- Dunning email sequences (basic failure notification only in v1)

---

## 5. Constraints

- **Stripe dependency:** All payment processing via Stripe. Webhook reliability is critical - all subscription state changes must be driven by Stripe webhooks, not direct API responses, to prevent race conditions.
- **GDPR:** Payment data is never stored locally. Stripe vaults card details. We store only Stripe Customer ID and last 4 digits + card brand for display.
- **Tax compliance:** VAT handling via Stripe Tax. We must pass validated billing address to Stripe to compute tax correctly.
- **Existing auth:** Subscription status check must integrate with the existing workspace middleware. No new auth system.

---

## 6. Open Questions

| Question | Owner | Resolution needed by |
|---|---|---|
| Annual billing discount: 20% or 2 months free framing? | Product | Before FEAT-SUB-001 enters build |
| Enterprise plan: include in billing UI but show "Contact sales"? | Sales | Before FEAT-SUB-001 design |
| Refund policy: will we commit to a 14-day money-back guarantee? | Legal | Before FEAT-SUB-001 design |

---

## 7. Revision History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-06-01 | Initial draft from Track B discovery (5 customer interviews + competitor analysis) |
