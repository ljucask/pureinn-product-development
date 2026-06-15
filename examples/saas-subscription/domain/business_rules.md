# Business Rules Library
# Live Register 2 of 4 - FDD+SDD Framework

> **Product:** ProjectFlow SaaS
> **Version:** 1.2
> **Last updated:** 2026-06-01
> **Maintained by:** pm-business-rules-library (init) + pm-feature-design (JIT enrichment)

---

> **How to read this register:**
> - Rules are referenced by ID (BR-XXX-001) in Feature Cards and entities.md
> - Status: Draft = intent captured, formula TBD | Final = complete, used in build
> - Priority: Critical = blocking feature build | High = must address before launch | Medium = address before scale

---

> **Note:** This example shows business_rules.md in **append mode**. The SUB, PAY, INV, and REG sections
> were added for the subscription-billing initiative. Existing rules (BR-USR-*, BR-WS-*) from the
> original product are above this point - not shown here for brevity.

---

## Subscription Rules

### BR-SUB-001: Subscription must not activate without confirmed payment
**Category:** Subscription
**Affected entity:** Subscription (entities.md#subscription)
**Priority:** Critical
**Status:** Final

**Rule:**
A Subscription must remain in Draft state until a payment confirmation webhook is received from Stripe. The system must never activate a Subscription based on a direct API response - only on the `payment_intent.succeeded` webhook event. This prevents race conditions where the API call succeeds but the actual charge fails.

**Formula/Condition:**
`subscription.status = Active ONLY IF stripe_webhook.event == payment_intent.succeeded AND invoice.status == Paid`

**Enforcement point:** Stripe webhook handler - `payment_intent.succeeded` event triggers activation.
**Exceptions:** None - this is a hard invariant.
**Applies to features:** FEAT-SUB-001 (Subscribe to a plan), FEAT-SUB-009 (Reactivate cancelled subscription)
**Source:** Financial integrity requirement + Stripe best practice

---

### BR-SUB-002: Grace period before access restriction on renewal failure
**Category:** Subscription
**Affected entity:** Subscription (entities.md#subscription)
**Priority:** Critical
**Status:** Final

**Rule:**
When a subscription renewal payment fails, the subscription must transition to PastDue state and remain accessible for 7 calendar days (grace period). Access must not be restricted immediately on payment failure. The grace period gives the user time to update their payment method or for automated retries to succeed.

**Formula/Condition:**
`grace_period_end = period_end + 7 days`
`workspace.access = restricted ONLY IF subscription.status == Cancelled`
`subscription.status = Cancelled IF now >= grace_period_end AND invoice.status != Paid`

**Exceptions:** None - grace period is always 7 days regardless of plan or payment history.
**Applies to features:** FEAT-SUB-005 (Process subscription renewal), FEAT-SUB-002 (View subscription details)
**Source:** Business decision - balances revenue protection with customer experience

---

### BR-SUB-003: Cancellation takes effect at end of billing period
**Category:** Subscription
**Affected entity:** Subscription (entities.md#subscription)
**Priority:** High
**Status:** Final

**Rule:**
When a user cancels a subscription, access continues until the end of the current billing period. The subscription transitions to Cancellation_Scheduled immediately, but transitions to Cancelled only when period_end is reached. No refunds are issued for the remaining days in the current period. Immediate cancellation (with refund) is not supported in v1.

**Formula/Condition:**
`ON user.cancel_requested: subscription.status = Cancellation_Scheduled; subscription.cancels_at = period_end`
`ON period_end.reached IF subscription.status == Cancellation_Scheduled: subscription.status = Cancelled`

**Exceptions:** Enterprise customers may request immediate cancellation via support - processed manually outside the system.
**Applies to features:** FEAT-SUB-003 (Cancel subscription)
**Source:** Business decision - standard SaaS practice; simplifies billing reconciliation

---

### BR-SUB-004: User can reactivate while in Cancellation_Scheduled state
**Category:** Subscription
**Affected entity:** Subscription (entities.md#subscription)
**Priority:** High
**Status:** Final

**Rule:**
A user who has scheduled a cancellation can reverse it at any time before period_end. Reverting restores the subscription to Active state. No new payment is taken - the user has already paid for the current period.

**Formula/Condition:**
`ON user.reactivation_requested IF subscription.status == Cancellation_Scheduled AND now < period_end: subscription.status = Active; subscription.cancels_at = NULL`

**Exceptions:** Cannot reactivate after period_end has been reached (subscription is already Cancelled).
**Applies to features:** FEAT-SUB-003 (Cancel subscription - reversal path)
**Source:** Business decision - reduces involuntary churn

---

## Payment Rules

### BR-PAY-001: Payment status driven by webhook, not API response
**Category:** Payment
**Affected entity:** Invoice (entities.md#invoice), Subscription (entities.md#subscription)
**Priority:** Critical
**Status:** Final

**Rule:**
Invoice status must never be set to Paid based on the direct Stripe API response. Invoice status is set to Paid exclusively when the `payment_intent.succeeded` Stripe webhook is received and validated. This prevents data inconsistency in network error or timeout scenarios.

**Formula/Condition:**
`invoice.status = Paid ONLY IF webhook.event == payment_intent.succeeded AND webhook.payment_intent_id == invoice.stripe_payment_intent_id AND webhook.signature_valid == true`

**Enforcement point:** Webhook controller - all other payment status update paths are blocked.
**Exceptions:** None.
**Applies to features:** FEAT-SUB-001 (Subscribe to a plan), FEAT-SUB-005 (Process subscription renewal)
**Source:** Financial integrity + Stripe webhook-first architecture requirement

---

### BR-PAY-002: Default payment method must always be set for active subscriptions
**Category:** Payment
**Affected entity:** PaymentMethod (entities.md#paymentmethod), Subscription (entities.md#subscription)
**Priority:** High
**Status:** Final

**Rule:**
An active Subscription must always have exactly one Active PaymentMethod designated as default. If a user removes the current default payment method, they must designate a replacement before the removal completes. Removal of the only payment method while subscription is Active is not permitted.

**Formula/Condition:**
`workspace.paymentMethods.filter(status == Active).length >= 1 WHEN subscription.status IN [Active, PastDue, Cancellation_Scheduled]`
`SET new_default BEFORE removing current_default`

**Exceptions:** Subscriptions in Cancelled or Draft state are not subject to this rule.
**Applies to features:** FEAT-SUB-004 (Update payment method)
**Source:** Business integrity - subscription cannot renew without a valid payment method

---

## Invoice Rules

### BR-INV-001: Invoices are immutable after reaching Paid status
**Category:** Invoice
**Affected entity:** Invoice (entities.md#invoice)
**Priority:** Critical
**Status:** Final

**Rule:**
Once an Invoice reaches Paid status, its financial fields (amount, tax, line items, invoice number) must not be modified under any circumstances. A correction to a paid invoice requires a new Credit Note (not supported in v1 - manual Stripe dashboard action). This is a financial and legal compliance requirement.

**Formula/Condition:**
`IF invoice.status == Paid: BLOCK all write operations on invoice.amount, invoice.tax_amount, invoice.total, invoice.line_items`

**Exceptions:** None - applies to all paid invoices regardless of amount or context.
**Applies to features:** FEAT-SUB-001, FEAT-SUB-007 (View invoice history)
**Source:** Tax compliance + accounting integrity requirement

---

## Regulatory / Compliance Rules

### BR-REG-001: Invoices must be retained for 7 years
**Category:** Compliance
**Regulation:** EU VAT Directive + local tax law (variable by market)
**Affected entity:** Invoice (entities.md#invoice)
**Priority:** Critical
**Status:** Final

**Rule:**
All invoices (Paid and Void) must be retained in storage for a minimum of 7 years from the invoice date. Invoices must not be deleted or hard-purged even if the associated workspace or user account is deleted. When a workspace is deleted, invoices are anonymized (workspace_id reference removed, billing details retained) but not deleted.

**Data retention / action required:**
- Primary DB: retain for 7 years from invoice.issued_at. Add `retain_until` field = issued_at + 7 years.
- On workspace deletion: anonymize invoice records (set workspace_id = NULL, retain financial data)
- Deletion of invoice records only permitted after retain_until date has passed (automated cleanup job)

**Applies to features:** FEAT-SUB-001, FEAT-SUB-007, FEAT-SUB-008 (Download invoice PDF)
**Source:** EU VAT Directive Article 246; local tax law in SK/CZ/AT requires minimum 7-year retention

---

### BR-REG-002: Card data must not be stored locally
**Category:** Compliance
**Regulation:** PCI DSS
**Affected entity:** PaymentMethod (entities.md#paymentmethod)
**Priority:** Critical
**Status:** Final

**Rule:**
Full card numbers, CVV codes, and magnetic stripe data must never be stored in the application database. The system stores only: Stripe PaymentMethod ID, card brand (Visa/Mastercard/etc.), last 4 digits, expiry month/year (for display and expiry warning only). All card data is vaulted exclusively by Stripe.

**Data retention / action required:**
- Store: stripe_payment_method_id, brand, last4, exp_month, exp_year
- Never store: full PAN, CVV, full expiry in any log or database field
- On removal: delete the local PaymentMethod record and call Stripe API to detach from customer

**Applies to features:** FEAT-SUB-001, FEAT-SUB-004 (Update payment method)
**Source:** PCI DSS Level 1 compliance requirement

---

## Rule Coverage Map

| Rule ID | Rule Name | Status | Used in Features |
|---|---|---|---|
| BR-SUB-001 | Subscription activates only on webhook confirmation | Final | FEAT-SUB-001, FEAT-SUB-009 |
| BR-SUB-002 | 7-day grace period on renewal failure | Final | FEAT-SUB-005 |
| BR-SUB-003 | Cancellation at period_end only | Final | FEAT-SUB-003 |
| BR-SUB-004 | Reactivation while Cancellation_Scheduled | Final | FEAT-SUB-003 |
| BR-PAY-001 | Payment status from webhook only | Final | FEAT-SUB-001, FEAT-SUB-005 |
| BR-PAY-002 | Active subscription must have default payment method | Final | FEAT-SUB-004 |
| BR-INV-001 | Paid invoices are immutable | Final | FEAT-SUB-001, FEAT-SUB-007 |
| BR-REG-001 | 7-year invoice retention | Final | FEAT-SUB-001, FEAT-SUB-007, FEAT-SUB-008 |
| BR-REG-002 | No local card data storage | Final | FEAT-SUB-001, FEAT-SUB-004 |

---

## Changelog

| Version | Date | Change | Triggered by |
|---|---|---|---|
| 1.0 | 2026-05-01 | Initial rules - BR-USR-*, BR-WS-* | Phase 4 init |
| 1.1 | 2026-05-20 | BR-USR-001 finalized | pm-feature-design FEAT-USR-001 |
| 1.2 | 2026-06-01 | BR-SUB-*, BR-PAY-*, BR-INV-*, BR-REG-* added | subscription-billing initiative append |
