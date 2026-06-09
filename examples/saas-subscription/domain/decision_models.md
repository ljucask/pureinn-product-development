# Decision Models Matrix
# Live Register 3 of 4 - FDD+SDD Framework

> **Product:** ProjectFlow SaaS
> **Version:** 1.2
> **Last updated:** 2026-06-01
> **Maintained by:** pm-business-rules-library (init) + pm-feature-design (JIT enrichment)

---

> **How to read this register:**
> - Decision tables define outputs for all combinations of input conditions
> - Used by Claude Code to generate unit tests covering all edge cases
> - Referenced in Feature Cards Section 1 (Biznis Mantinely) by TBL-ID
> - Status: Draft = structure defined, values TBD | Final = complete, used in build

---

> **Note:** This example shows three decision model types used in the subscription-billing initiative:
> TBL (decision table) for multi-condition logic, TRE (decision tree) for sequential branching,
> and SCR (scoring model) for multi-factor evaluation. Each maps back to the BR-IDs in business_rules.md.

---

## TBL-SUB-01: Subscription renewal outcome
**Domain:** Subscription
**Type:** Decision Table (TBL)
**Used by rules:** BR-SUB-002, BR-PAY-001
**Affected entity:** Subscription (entities.md#subscription), Invoice (entities.md#invoice)
**Status:** Final
**Used in features:** FEAT-SUB-005 (Process subscription renewal)

**What is being decided:** What happens to the subscription and invoice when a renewal attempt is processed.

| Webhook event | Retry count | Grace period expired? | Subscription outcome | Invoice outcome | Notes |
|---|---|---|---|---|---|
| `payment_intent.succeeded` | Any | N/A | Remains Active (or PastDue -> Active) | Set to Paid | Reset retry counter |
| `payment_intent.payment_failed` | 0 | No | Active -> PastDue | Remains Open | Begin grace period clock |
| `payment_intent.payment_failed` | 1 | No | Remains PastDue | Remains Open | Retry scheduled +3 days |
| `payment_intent.payment_failed` | 2 | No | Remains PastDue | Remains Open | Retry scheduled +5 days |
| `payment_intent.payment_failed` | 3 | No | Remains PastDue | Set to Uncollectible | No more automatic retries |
| `payment_intent.payment_failed` | Any | Yes | PastDue -> Cancelled | Set to Void | Workspace access restricted |

**Edge cases:**
- Webhook received twice (duplicate): idempotency key on `invoice.stripe_payment_intent_id` - second event is ignored
- Webhook received after grace period expired but before Cancelled transition: cancel transition takes priority - treat as expired
- Subscription manually cancelled while PastDue: transitions to Cancelled immediately regardless of retry schedule

---

## TBL-SUB-02: Plan downgrade eligibility
**Domain:** Subscription
**Type:** Decision Table (TBL)
**Used by rules:** BR-SUB-003
**Affected entity:** Subscription (entities.md#subscription)
**Status:** Draft
**Used in features:** FEAT-SUB-010 (Change plan) - TBD

**What is being decided:** Whether a workspace can downgrade to a lower plan tier, and when the change takes effect.

| Current plan | Target plan | Seats used | Storage used | Downgrade allowed? | Effective date | Action required |
|---|---|---|---|---|---|---|
| Pro | Starter | <= 5 | <= 5 GB | Yes | period_end | None |
| Pro | Starter | <= 5 | > 5 GB | No | N/A | User must reduce storage first |
| Pro | Starter | > 5 | Any | No | N/A | User must remove seats first |
| Business | Pro | <= 20 | <= 50 GB | Yes | period_end | None |
| Business | Pro | > 20 | Any | No | N/A | User must remove seats first |
| Business | Pro | <= 20 | > 50 GB | No | N/A | User must reduce storage first |
| Business | Starter | Any | Any | No | N/A | Direct downgrade not permitted - must go Business -> Pro -> Starter |

**Edge cases:**
- Downgrade requested on same day as renewal: downgrade schedules for next period_end (renewal applies to current plan)
- Seats removed and re-added within same period: recalculate eligibility at time of downgrade request
- Storage recalculation: storage check is real-time at request, not cached

---

## TRE-PAY-01: Payment method expiry handling
**Domain:** Payment
**Type:** Decision Tree (TRE)
**Used by rules:** BR-PAY-002
**Affected entity:** PaymentMethod (entities.md#paymentmethod)
**Status:** Final
**Used in features:** FEAT-SUB-004 (Update payment method), FEAT-SUB-005 (Process subscription renewal)

**What is being decided:** What action to take when a payment method is detected as expired or about to expire.

```
Is the PaymentMethod expiry date in the past?
├── YES: Status -> Expired
│   └── Is this the default PaymentMethod for an Active subscription?
│       ├── YES: Send "card expired" email + block renewal attempt until updated
│       │   └── Renewal due within 7 days?
│       │       ├── YES: Send urgent warning email daily until updated
│       │       └── NO: Send single warning email, re-evaluate on next weekly check
│       └── NO: Set status = Expired, no email sent (non-default card)
│
└── NO: Is expiry within the next 30 days?
    ├── YES: Send "card expiring soon" email (once per month maximum)
    │   └── Is this the only Active PaymentMethod?
    │       ├── YES: Include prominent "add backup card" CTA in email
    │       └── NO: Include standard "update card" CTA
    └── NO: No action - re-evaluate on next weekly check
```

**Edge cases:**
- Card updated between weekly checks: re-run tree immediately after update confirmation webhook from Stripe
- Multiple expired cards on same workspace: send single consolidated email, list all expired cards
- User has no email set: log event, surface warning in app UI on next login only

---

## SCR-SUB-01: Churn risk score
**Domain:** Subscription
**Type:** Scoring Model (SCR)
**Used by rules:** (no direct BR - informational model for retention logic)
**Affected entity:** Subscription (entities.md#subscription)
**Status:** Draft
**Used in features:** FEAT-SUB-006 (Retention offer on cancellation intent) - TBD

**What is being decided:** Risk level of a workspace cancelling, to determine whether to show a retention offer.

| Signal | Condition | Points |
|---|---|---|
| Subscription age | < 30 days | +30 |
| Subscription age | 30-90 days | +15 |
| Subscription age | > 90 days | 0 |
| Payment failures (last 90 days) | >= 1 failure | +25 |
| Payment failures (last 90 days) | 0 failures | 0 |
| Last login (any seat) | > 14 days ago | +20 |
| Last login (any seat) | 7-14 days ago | +10 |
| Last login (any seat) | < 7 days ago | 0 |
| Active seats used | < 50% of purchased seats | +15 |
| Active seats used | >= 50% of purchased seats | 0 |
| Support tickets (last 30 days) | >= 2 open tickets | +10 |
| Support tickets (last 30 days) | 0-1 open tickets | 0 |

**Score thresholds:**

| Score range | Risk level | Action |
|---|---|---|
| 0-20 | Low | No retention offer - proceed to cancel normally |
| 21-50 | Medium | Show standard retention offer (1-month discount) |
| 51-80 | High | Show aggressive retention offer (2-month discount or plan downgrade suggestion) |
| 81+ | Critical | Trigger CS notification in addition to aggressive offer |

**Notes:**
- Score is calculated at the moment cancellation flow is initiated (not cached)
- Model is Draft - weights not yet validated against real churn data. `[ASSUMED - replace when real data available]`
- Discount offers are hardcoded in v1 - no dynamic offer engine

---

## Changelog

| Version | Date | Change | Triggered by |
|---|---|---|---|
| 1.0 | 2026-06-01 | Initial tables: TBL-SUB-01, TBL-SUB-02, TRE-PAY-01, SCR-SUB-01 | subscription-billing initiative init |
| 1.1 | 2026-06-01 | TBL-SUB-01 finalized | pm-feature-design FEAT-SUB-005 |
| 1.1 | 2026-06-01 | TRE-PAY-01 finalized | pm-feature-design FEAT-SUB-004 |
