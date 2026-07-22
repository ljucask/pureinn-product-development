# Business Rules Library
# Live Register 2 of 5 - FDD+SDD Framework

> **Product:** PureHunger
> **Version:** 1.3
> **Last updated:** 2026-03-04
> **Maintained by:** pm-business-rules-library (init) + pm-business-rule-core / pm-business-rule-critical / pm-business-rule-governance (JIT single-rule additions) + pm-feature-design (JIT finalization)

---

> **How to read this register:**
> - Rules are referenced by ID (BR-XXX-NNN) in Feature Cards and `entities.md`
> - Status: Draft = intent captured, formula TBD | Final = complete, used in build
> - **This register is explicitly three-way split by priority class - each tier is produced and maintained by its own JIT helper skill:**

| Tier | Section below | Produced by | Meaning | Exceptions allowed? |
|---|---|---|---|---|
| **Core** | [Core Rules](#core-rules) | `pm-business-rule-core` | Everyday operational logic (matching, pricing, fulfillment). Can have exceptions/variations. Violating it degrades quality/fairness, not irreversible. | Yes |
| **Critical** | [Critical Rules](#critical-rules) | `pm-business-rule-critical` | Hard invariants. Violation = financial loss, legal exposure, or irreversible damage. No exceptions, no admin overrides. | No |
| **Governance** | [Governance Rules](#governance-rules) | `pm-business-rule-governance` | Compliance, regulatory, and policy rules (GDPR-style, tax law, admin constraints). May have regional/partner variations. | Regional only |

Within each tier, rules are grouped by domain (Ordering, Restaurant, Payment, Delivery, Regulatory, User/Authorization). A rule's tier is fixed by what it protects, not by which domain it happens to touch - e.g. both Payment and Delivery rules appear in the Critical tier, because both domains have invariants where violation means real money lost or a safety failure.

---

## Core Rules

*High/Medium priority operational rules. Everyday business logic that governs normal system behavior and CAN have exceptions or context-dependent variations. Added by `pm-business-rule-core`.*

### Ordering Rules (BR-ORD-xxx)

### BR-ORD-001: Restaurant Must Be Active to Accept Orders
**Category:** Fulfillment
**Affected entity:** Order (entities.md#order), Restaurant (entities.md#restaurant)
**Priority:** High
**Status:** Final

**Rule:**
An Order cannot be placed if the Restaurant is not in Active state.

**Formula/Condition:**
`order.transition(Cart -> Placed) = allowed ONLY IF restaurant.status == "active"`

**Exceptions:** None known at MVP - the framing is Core rather than Critical because a future "scheduled order for a Paused restaurant reopening tomorrow" variation is plausible post-MVP and would need to slot in here without becoming a hard invariant rewrite.

**Applies to features:** FEAT-ORD-001
**Source:** Business decision - PRD Ordering & Checkout capability

---

### BR-ORD-002: MenuItem Must Be Available to Add to Cart
**Category:** Fulfillment
**Affected entity:** Order (entities.md#order), MenuItem (entities.md#menuitem)
**Priority:** High
**Status:** Final

**Rule:**
A MenuItem must be marked available (`is_available = true`) to be added to a cart.

**Formula/Condition:**
`cart.add_item(menu_item) = allowed ONLY IF menu_item.is_available == true`

**Exceptions:** None at MVP. Post-MVP "notify me when back in stock" would not violate this rule - it queues a request, it does not add an unavailable item to a live cart.

**Applies to features:** FEAT-ORD-001
**Source:** Business decision - prevents ordering items the kitchen cannot fulfill

---

### BR-ORD-003: Customer Cancellation Window
**Category:** Cancellation
**Affected entity:** Order (entities.md#order)
**Priority:** High
**Status:** Final

**Rule:**
An Order can be cancelled by the customer only while in Placed state (before the Restaurant has accepted it).

**Formula/Condition:**
`order.transition(Placed -> Cancelled, actor=customer) = allowed ONLY IF order.status == "placed"`

**Exceptions:** Once Accepted, only Ops can unwind an order, and that path goes through a refund (BR-PAY-004) rather than a customer-initiated cancellation - this is the documented exception boundary, not a variation of this rule itself.

**Applies to features:** FEAT-ORD-001
**Source:** Business decision - balances customer flexibility against restaurant kitchen waste once prep has started

---

### BR-ORD-004: Minimum Order Subtotal
**Category:** Pricing
**Affected entity:** Order (entities.md#order), Restaurant (entities.md#restaurant)
**Priority:** Medium
**Status:** Final

**Rule:**
An Order's subtotal must meet a minimum threshold before checkout is allowed. Default minimum is $10; individual restaurants may raise or lower it within a bounded range.

**Formula/Condition:**
`order.transition(Cart -> Placed) = allowed ONLY IF order.subtotal >= restaurant.minimum_order_subtotal`

**Exceptions:** Restaurants may set their own minimum between $8 and $25 (configured at onboarding, changeable via Restaurant Management settings); the platform default of $10 applies if unset.

**Applies to features:** FEAT-ORD-001
**Source:** Business decision - protects restaurant margin on very small orders where the flat $2.99 delivery fee doesn't cover courier dispatch cost

---

### Restaurant Rules (BR-REST-xxx)

### BR-REST-001: Restaurant Needs an Available MenuItem to Go Active
**Category:** Fulfillment
**Affected entity:** Restaurant (entities.md#restaurant), MenuItem (entities.md#menuitem)
**Priority:** High
**Status:** Final

**Rule:**
A Restaurant cannot move from Pending to Active (or from Paused back to Active) without at least one MenuItem marked available.

**Formula/Condition:**
`restaurant.transition(-> Active) = allowed ONLY IF EXISTS menu_item WHERE menu_item.restaurant_id == restaurant.id AND menu_item.is_available == true`

**Exceptions:** None currently, though a future "grand opening countdown" mode (visible but not yet orderable) is a plausible Core-tier variation, not a Critical rewrite.

**Applies to features:** FEAT-REST-001 (Restaurant onboarding)
**Source:** Business decision - an Active restaurant with an empty menu is a broken customer experience, not a policy violation, hence Core not Critical

---

### BR-REST-002: Prep Time Redeclaration Trigger
**Category:** SLA
**Affected entity:** Restaurant (entities.md#restaurant), Order (entities.md#order)
**Priority:** Medium
**Status:** Final

**Rule:**
If a Restaurant's rolling average *actual* prep time (measured Preparing → ReadyForPickup) deviates by more than 15 minutes from its declared `avg_prep_time_minutes` across 20 consecutive orders, the Restaurant is prompted to redeclare its estimate.

**Formula/Condition:**
`prompt_redeclare = true IF abs(rolling_avg_actual_prep_time(n=20) - restaurant.avg_prep_time_minutes) > 15min`

**Exceptions:** Suppressed during the first 14 days after `restaurant.activated` (onboarding grace period) - new restaurants' prep times are naturally volatile while staff calibrate to delivery-platform order volume.

**Applies to features:** FEAT-REST-002 (Restaurant operational dashboard)
**Source:** Business decision - accurate prep-time estimates directly affect customer ETA trust and courier dispatch timing

---

## Critical Rules

*Hard invariants. Violation causes financial loss, legal exposure, or irreversible system damage. Must hold in ALL circumstances - no exceptions, no admin overrides. Added by `pm-business-rule-critical`.*

### Payment Rules (BR-PAY-xxx)

### BR-PAY-001: Payment Capture Timing
**Category:** Payment
**Affected entity:** Payment (entities.md#payment), Order (entities.md#order)
**Priority:** Critical
**Status:** Final

**Rule:**
Payment must be authorized at Order placement but captured in full only when the Restaurant accepts the order. This protects customers from being charged for orders that are never confirmed.

**Formula/Condition:**
`payment.transition(Authorized -> Captured) = allowed ONLY IF order.status == "accepted"`

**Enforcement point:** Checked at the Payment entity's `Authorized -> Captured` transition (entities.md#payment), triggered by the `order.accepted` event - never callable directly from checkout code.
**Detection:** Nightly reconciliation job cross-checks every `Captured` Payment against its Order's `accepted_at` timestamp; any Payment captured before the corresponding `order.accepted` event fires a P1 alert (this should be structurally impossible, so an occurrence indicates a guard bypass bug, not a policy exception).
**Exceptions:** None - this is a hard invariant.
**Applies to features:** FEAT-ORD-001
**Source:** Financial integrity - core founder commitment ("no charging for orders that are never confirmed")

---

### BR-PAY-002: Auto-Refund on Restaurant Non-Response
**Category:** Payment
**Affected entity:** Payment (entities.md#payment), Order (entities.md#order)
**Priority:** Critical
**Status:** Final

**Rule:**
A refund must be issued automatically and in full if a Restaurant does not accept an Order within 10 minutes of placement.

**Formula/Condition:**
`IF (now - order.placed_at) > 10min AND order.status == "placed" THEN order.transition(-> Refunded) AND payment.transition(-> Refunded)`

**Enforcement point:** A scheduled timeout job evaluated against every `Placed` Order's `placed_at` timestamp - not dependent on any user or restaurant action.
**Detection:** Dashboard metric "Orders refunded on timeout, % of daily volume" - a sustained spike flags either a specific restaurant with response-time problems or a dispatch/notification delivery failure preventing restaurants from seeing new orders in time.
**Exceptions:** None - the 10-minute window is fixed platform-wide, not restaurant-configurable (unlike BR-ORD-004's minimum order, which is intentionally Core-tier and adjustable).
**Applies to features:** FEAT-ORD-001
**Source:** Financial integrity - prevents indefinite payment holds on unconfirmed orders

---

### BR-PAY-003: Courier Payout Fund Segregation
**Category:** Payment
**Affected entity:** CourierPayout (entities.md#courierpayout)
**Priority:** Critical
**Status:** Final

**Rule:**
Funds owed to couriers must be held in a ledger account segregated from PureHunger's operating funds from the moment a Delivery is Completed until the corresponding CourierPayout batch transitions to Paid.

**Formula/Condition:**
`courier_owed_funds.account == "segregated_ledger" FOR ALL delivery WHERE delivery.status == "completed" AND courier_payout(delivery).status != "paid"`

**Enforcement point:** Checked at the `CourierPayout.Pending -> Processing` transition (entities.md#courierpayout) - the batch submission job verifies segregated-ledger balance covers the batch total before submitting to the payment processor.
**Detection:** Daily automated reconciliation compares segregated ledger balance against the sum of unpaid completed-Delivery earnings; any shortfall triggers an immediate P1 finance alert before the next payout cutoff.
**Exceptions:** None - commingling operating funds with courier-owed funds, even briefly, is the exact failure mode this rule exists to prevent.
**Applies to features:** FEAT-PAY-001 (Courier payout batch job)
**Source:** Financial integrity - protects daily-payout differentiator from becoming a solvency risk if operating funds are ever short

---

### BR-PAY-004: Refund Cap
**Category:** Payment
**Affected entity:** Payment (entities.md#payment)
**Priority:** Critical
**Status:** Final

**Rule:**
A refund (full or partial) must never exceed the amount originally captured for that Order's Payment.

**Formula/Condition:**
`payment.refunded_amount <= payment.captured_amount ALWAYS`

**Enforcement point:** Checked at both `Captured -> Refunded` and `Captured -> PartiallyRefunded` transitions (entities.md#payment) - the refund service rejects any refund request exceeding remaining refundable balance before calling the Stripe API.
**Detection:** Stripe itself would reject an over-refund at the API layer, but the enforcement point exists to prevent an aggregate of *multiple* partial refunds exceeding the total - a case Stripe's single-call validation would not catch. Weekly finance audit sums refunds per Payment as a second-layer check.
**Exceptions:** None - this is a hard mathematical ceiling.
**Applies to features:** FEAT-PAY-002 (Ops refund tooling, post-MVP)
**Source:** Financial integrity - basic accounting correctness

---

### Delivery Rules (BR-DEL-xxx)

### BR-DEL-001: Courier Auto-Suspend on Low Rating
**Category:** Trust & Safety
**Affected entity:** Courier (entities.md#courier)
**Priority:** Critical
**Status:** Final

**Rule:**
A Courier whose rolling average rating over the last 20 deliveries falls below 4.5 stars is automatically suspended pending manual review.

**Formula/Condition:**
`courier.transition(Active -> Suspended) = automatic IF rolling_avg(courier.deliveries[-20:].customer_rating) < 4.5`

**Enforcement point:** Recomputed on every `delivery.completed` event (entities.md#delivery) that carries a `customer_rating` - the guard is checked synchronously as part of processing that event, not on a delayed batch job.
**Detection:** Because this is automatic (not a policy an admin could forget to apply), detection risk is inverted - the concern is a *missed* auto-suspend, not an unauthorized override. A daily audit query flags any Courier with `rolling_rating_avg < 4.5` but `status == "active"` as a P1 - it should never occur if the guard fires correctly.
**Exceptions:** None - no admin override skips the check itself; Ops can only reinstate *after* suspension via manual review (Suspended → Active), which is a separate, logged action, not an exception to the trigger condition.
**Applies to features:** FEAT-DEL-002
**Source:** Trust & safety - protects customers and restaurants from a degrading service floor; protects couriers from opaque platform-side deactivation by making the threshold explicit and consistent

---

### BR-DEL-002: Pickup Requires Order Ready
**Category:** Fulfillment
**Affected entity:** Delivery (entities.md#delivery), Order (entities.md#order)
**Priority:** Critical
**Status:** Final

**Rule:**
A Delivery cannot move to PickedUp until the Order is in ReadyForPickup state. This prevents couriers from marking pickup before the food is actually ready.

**Formula/Condition:**
`delivery.transition(EnRoute-to-Restaurant -> PickedUp) = allowed ONLY IF order.status == "ready_for_pickup"`

**Enforcement point:** Checked at the Delivery entity's `PickedUp` transition (entities.md#delivery) - the courier app's "Confirm Pickup" action calls this guard before allowing the state change.
**Detection:** Any Delivery reaching `PickedUp` while its linked Order's status log shows no `order.ready_for_pickup` event preceding it is structurally impossible if the guard holds; a weekly data-integrity job scans for this pattern as a defense-in-depth check against a guard bug.
**Exceptions:** None - this sequencing protects both food safety perception (no picking up food that isn't actually ready) and accurate ETA data for customers.
**Applies to features:** FEAT-DEL-002
**Source:** Operational integrity - prevents inaccurate delivery timestamps and premature pickups

---

### BR-DEL-003: Delivery Completion Requires Proximity Confirmation
**Category:** Trust & Safety
**Affected entity:** Delivery (entities.md#delivery), Order (entities.md#order)
**Priority:** Critical
**Status:** Final

**Rule:**
A Delivery cannot be marked Completed unless GPS confirms the courier's location is within 150 meters of the customer's delivery address, or an Ops staff member manually overrides with a logged reason.

**Formula/Condition:**
`delivery.transition(EnRoute-to-Customer -> Completed) = allowed IF gps_distance(courier.location, order.delivery_address) < 150m OR (ops_override == true AND ops_override_reason IS NOT NULL)`

**Enforcement point:** Checked at the Delivery entity's `Completed` transition (entities.md#delivery) - the courier app blocks the "Mark Delivered" action client-side and server-side re-validates GPS distance before accepting the state change.
**Detection:** Every Ops override is logged with actor ID and reason (itself required by BR-GOV-002); a weekly report surfaces override rate per courier - an unusually high override rate for one courier is a fraud/GPS-spoofing signal investigated by Trust & Safety.
**Exceptions:** The Ops manual override is not an exception to the rule itself - it is a built-in secondary verification path (for legitimate GPS failure in dense urban cores or building interiors), always logged, never silent.
**Applies to features:** FEAT-DEL-002
**Source:** Trust & safety / financial integrity - prevents fraudulent "delivered" claims that would otherwise trigger courier payout (BR-PAY-003 chain) without an actual delivery

---

## Governance Rules

*Compliance, regulatory, and policy rules - GDPR-style data handling, tax law, admin/ops constraints. May have regional or partner-specific variations. Added by `pm-business-rule-governance`.*

### Regulatory / Compliance Rules (BR-REG-xxx)

### BR-REG-001: Commission Rate Change Notice
**Category:** Compliance
**Regulation:** Restaurant Partner Agreement (contractual, not statutory)
**Affected entity:** Restaurant (entities.md#restaurant)
**Priority:** Critical
**Status:** Final

**Rule:**
Restaurant commission rate changes require 30 days written notice per the Restaurant Partner Agreement.

**Data retention / action required:**
Notice must be sent (email + in-app) at least 30 days before any `commission_rate` change takes effect; the notice record (recipient, date sent, old rate, new rate, effective date) must be retained for the life of the partner relationship plus 3 years for dispute resolution.

**Enforcement point:** The Restaurant Management admin tool blocks a `commission_rate` update from taking effect in fewer than 30 days from the change request date - the new rate is staged with an `effective_date`, not applied immediately.
**Exceptions:** None on the notice period itself. Restaurants may voluntarily agree to an earlier effective date only with a signed written waiver on file (rare, tracked as a manual exception record, not a system-level bypass).
**Applies to features:** FEAT-REST-003 (Restaurant commission management, post-MVP admin tooling)
**Source:** Restaurant Partner Agreement, Section on Fee Changes

---

### BR-REG-002: Courier Tax Document Issuance
**Category:** Compliance
**Regulation:** IRS 1099-NEC reporting requirement (US federal tax law)
**Affected entity:** Courier (entities.md#courier), CourierPayout (entities.md#courierpayout)
**Priority:** Critical
**Status:** Final

**Rule:**
Courier tax documents (1099-NEC) must be issued by January 31 for any courier paid over $600 in the prior calendar year.

**Data retention / action required:**
`tax_paid_ytd` (derived from summed `Paid` CourierPayout `total_amount` per courier per calendar year, entities.md#courierpayout) must be evaluated against the $600 threshold no later than January 15; 1099-NEC forms generated and filed with the IRS, and delivered to qualifying couriers, by January 31. Records of issued forms retained 7 years per IRS recordkeeping requirements.

**Enforcement point:** Annual scheduled job (runs January 10-15) - not tied to any single Delivery or Payout transition, since it evaluates a full calendar year's aggregate.
**Exceptions:** None on the threshold or deadline - this is a federal filing requirement, not a company policy choice.
**Applies to features:** FEAT-PAY-003 (Annual tax document generation, post-MVP - required before first full calendar year of operation)
**Source:** IRS 1099-NEC filing requirement (26 U.S.C. reporting obligations for independent contractor payments)

---

### BR-REG-003: Restaurant Food-Service Permit Verification
**Category:** Compliance
**Regulation:** Local food-service licensing (Boise / Ada County health department, and per-market equivalent as PureHunger expands)
**Affected entity:** Restaurant (entities.md#restaurant)
**Priority:** Critical
**Status:** Final

**Rule:**
Restaurants must have a current, valid food-service permit on file before their account can move from Pending to Active, and permit status must be re-verified annually thereafter.

**Data retention / action required:**
Permit document (or verified reference number) and its expiration date stored against the Restaurant record; annual re-verification job checks expiration date and prompts renewal 30 days before lapse. A restaurant whose permit lapses without renewal is auto-transitioned to Paused (not Deactivated - preserves the relationship pending renewal).

**Enforcement point:** Checked at the Restaurant `Pending -> Active` transition (entities.md#restaurant) - part of the same guard as BR-REST-001, but this clause is Governance-tier (legal requirement) rather than Core-tier (product-quality requirement), which is why the two live in different registers despite gating the same transition.
**Exceptions:** Permit requirements vary by city/county as PureHunger expands beyond Boise - the specific permit type and verification source is market-configurable, but the requirement itself (a valid permit must exist) has no exception.
**Applies to features:** FEAT-REST-001 (Restaurant onboarding)
**Source:** Local health department food-service licensing regulation

---

### User / Authorization Rules (BR-GOV-xxx, BR-USR-xxx)

### BR-GOV-001: No Raw Card Data Storage
**Category:** Compliance
**Regulation:** PCI-DSS (industry security standard, not statutory but contractually required by payment processors)
**Affected entity:** Payment (entities.md#payment), Customer (entities.md#customer)
**Priority:** Critical
**Status:** Final

**Rule:**
Customer payment data (card details) must never be stored directly - PureHunger stores only the payment processor's tokenized reference.

**Data retention / action required:**
Only `stripe_payment_intent_id` (or equivalent tokenized reference) is persisted on the Payment and Customer records (entities.md#payment, entities.md#customer); raw PAN, CVV, or full card number must never appear in application logs, database tables, or backups. Log-scrubbing middleware redacts any field matching card-number patterns as a defense-in-depth measure.

**Enforcement point:** Enforced at the API/data-model layer - the Payment and Customer schemas structurally have no field capable of holding a raw card number; this is a design-time guarantee, not a runtime check that could be bypassed.
**Exceptions:** None - this is both a PCI-DSS compliance requirement and a condition of PureHunger's payment processor agreement.
**Applies to features:** FEAT-ORD-001
**Source:** PCI-DSS compliance requirement; Stripe processor agreement

---

### BR-GOV-002: Admin Action Audit Logging
**Category:** Compliance
**Regulation:** Internal policy (supports dispute resolution and BR-DEL-003 override auditing)
**Affected entity:** Customer, Restaurant, Courier, Order (cross-entity - any entity subject to an Ops override)
**Priority:** High
**Status:** Final

**Rule:**
Any Ops/Admin action that overrides normal system behavior on a customer, restaurant, or courier account (refund override, manual delivery-completion override, account suspension/reinstatement) must be logged with the acting admin's ID, a reason code, and a timestamp.

**Data retention / action required:**
Audit log entry created synchronously with the override action (not best-effort/async) - `actor_id`, `action_type`, `target_entity_id`, `reason_code`, `free_text_reason` (optional), `timestamp`. Retained for 3 years to support dispute resolution and support-quality review.

**Enforcement point:** Every Ops-facing override action (BR-DEL-003 GPS override, refund issuance under BR-PAY-004, Courier reinstatement) is implemented as a wrapper that requires a reason code parameter - there is no code path to perform the override without one.
**Exceptions:** None on the logging requirement itself; the reason code taxonomy may vary as new override types are added.
**Applies to features:** FEAT-DEL-002, FEAT-PAY-002 (Ops refund tooling)
**Source:** Internal policy - operational accountability, supports the detection requirement named in BR-DEL-003 and BR-PAY-004

---

### BR-USR-001: Right-to-Erasure Handling
**Category:** Compliance
**Regulation:** Consumer data-privacy best practice (modeled on GDPR Art. 17 / CCPA deletion-right patterns, applied as company policy in the US market)
**Affected entity:** Customer (entities.md#customer)
**Priority:** High
**Status:** Final

**Rule:**
A customer's request to delete their account and personal data must result in full deletion or anonymization within 30 days of the request being confirmed, except for transaction records required for tax/financial reporting.

**Data retention / action required:**
Primary customer profile (name, email, phone, saved addresses, `payment_method_token`) deleted within 30 days of confirmed request. Order and Payment records are anonymized (customer reference replaced with a non-identifying placeholder) rather than deleted, and retained 7 years to satisfy financial reporting obligations (aligned with BR-REG-002's retention pattern).

**Enforcement point:** A scheduled deletion job processes confirmed erasure requests; anonymization of Order/Payment records runs as part of the same job, not a separate manual step that could be forgotten.
**Exceptions:** Financial/transaction records are the sole exception, and even those are anonymized (not exempted from the request entirely) - only the retention period and form (anonymized vs. deleted) differ.
**Applies to features:** FEAT-USR-001 (Account deletion, post-MVP - not in the initial MVP ordering-loop scope)
**Source:** Company policy, modeled on GDPR/CCPA deletion-right conventions as a trust commitment even though not yet legally mandated in Idaho at MVP launch

---

## Rule Coverage Map

| Rule ID | Tier | Rule Name | Status | Used in Features |
|---|---|---|---|---|
| BR-ORD-001 | Core | Restaurant Must Be Active to Accept Orders | Final | FEAT-ORD-001 |
| BR-ORD-002 | Core | MenuItem Must Be Available to Add to Cart | Final | FEAT-ORD-001 |
| BR-ORD-003 | Core | Customer Cancellation Window | Final | FEAT-ORD-001 |
| BR-ORD-004 | Core | Minimum Order Subtotal | Final | FEAT-ORD-001 |
| BR-REST-001 | Core | Restaurant Needs an Available MenuItem to Go Active | Final | FEAT-REST-001 |
| BR-REST-002 | Core | Prep Time Redeclaration Trigger | Final | FEAT-REST-002 |
| BR-PAY-001 | Critical | Payment Capture Timing | Final | FEAT-ORD-001 |
| BR-PAY-002 | Critical | Auto-Refund on Restaurant Non-Response | Final | FEAT-ORD-001 |
| BR-PAY-003 | Critical | Courier Payout Fund Segregation | Final | FEAT-PAY-001 |
| BR-PAY-004 | Critical | Refund Cap | Final | FEAT-PAY-002 |
| BR-DEL-001 | Critical | Courier Auto-Suspend on Low Rating | Final | FEAT-DEL-002 |
| BR-DEL-002 | Critical | Pickup Requires Order Ready | Final | FEAT-DEL-002 |
| BR-DEL-003 | Critical | Delivery Completion Requires Proximity Confirmation | Final | FEAT-DEL-002 |
| BR-REG-001 | Governance | Commission Rate Change Notice | Final | FEAT-REST-003 |
| BR-REG-002 | Governance | Courier Tax Document Issuance | Final | FEAT-PAY-003 |
| BR-REG-003 | Governance | Restaurant Food-Service Permit Verification | Final | FEAT-REST-001 |
| BR-GOV-001 | Governance | No Raw Card Data Storage | Final | FEAT-ORD-001 |
| BR-GOV-002 | Governance | Admin Action Audit Logging | Final | FEAT-DEL-002, FEAT-PAY-002 |
| BR-USR-001 | Governance | Right-to-Erasure Handling | Final | FEAT-USR-001 |

**Tier totals:** 6 Core / 7 Critical / 6 Governance = 19 rules.

---

## Changelog

| Version | Date | Change | Triggered by |
|---|---|---|---|
| 1.0 | 2026-02-14 | Initial draft: BR-ORD-001/002/003, BR-PAY-001/002, BR-DEL-001/002, BR-REG-001/002, BR-GOV-001 captured from PRD + founder constraints | Phase 5 init (pm-business-rules-library) |
| 1.1 | 2026-02-20 | BR-ORD-004, BR-REST-001, BR-REST-002 added (Core tier) | pm-business-rule-core, during FEAT-REST-001 design |
| 1.2 | 2026-02-27 | BR-PAY-003, BR-PAY-004, BR-DEL-003 added (Critical tier) | pm-business-rule-critical, during FEAT-DEL-002 and FEAT-PAY-001 design |
| 1.3 | 2026-03-04 | BR-REG-003, BR-GOV-002, BR-USR-001 added (Governance tier); all rules moved from Draft to Final with enforcement points and detection notes | pm-business-rule-governance + pm-feature-design JIT finalization for FEAT-ORD-001 and FEAT-DEL-002 |
