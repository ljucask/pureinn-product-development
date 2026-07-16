# FDD Feature List
# Live Register 4 of 4 - FDD+SDD Framework

> **Product:** PureHunger
> **Version:** 1.1
> **Last updated:** 2026-07-16
> **Based on:** PRD Business Capabilities v1.0, entities.md v1.0

---

> **How to read this register:**
> - Domains and Feature Sets are grouping only - no execution logic
> - All prioritization, dependencies, MVP cut, and stripe assignment is per Feature
> - Status reflects Feature Card status (updated by pm-stripe during JIT cycle)
> - MVP membership lives in the single `phase` field - `MVP` = in the MVP cut, `MVP+` = post-MVP, `Cut` = not building. There is no separate `mvp` boolean anywhere in this register or in any Feature Card.

---

## Feature Naming Convention

**Top-down derivation:** Domain > Feature Set (FS-NN) > Feature. Every feature follows **`[Action] [Result] [Object]`** (FDD grammar). Feature Set IDs are global-sequential across the whole product (FS-01, FS-02...), not reset per domain.

---

## Domain: Ordering (ORD)

> **Column codes:** Layer = FE / BE / SYS · Phase = MVP / MVP+ / Cut · Pri = P1-P4 · KANO = M(ust-be) / P(erformance) / D(elighter) / I(ndifferent) · V×C = QW / BB / FI / TW · Sub = has subtasks (✓ / –). Full values live in each card's frontmatter; this is the index.

### FS-01: Discovery & Cart

| ID | Feature | Actor | Layer | Phase | Pri | KANO | V×C | Sub | Stripe | Status | Deps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FEAT-ORD-001 | Place order from restaurant cart | Customer | FE, BE | MVP | P1 | M | BB | ✓ | stripe-ordering-checkout | 6_Shipped | FEAT-REST-001, FEAT-REST-002, FEAT-REST-003 |
| FEAT-ORD-002 | Search restaurants by cuisine and location | Customer | FE, BE | MVP | P1 | M | QW | – | stripe-ordering-checkout | 6_Shipped | FEAT-REST-001 |
| FEAT-ORD-003 | Reorder previous order | Customer | FE, BE | MVP+ | P3 | D | FI | – | stripe-ordering-checkout | 1_Backlog | FEAT-ORD-001, FEAT-ORD-013 |

### FS-02: Order Fulfillment Lifecycle

| ID | Feature | Actor | Layer | Phase | Pri | KANO | V×C | Sub | Stripe | Status | Deps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FEAT-ORD-010 | Accept order and start preparing | Restaurant | FE, BE | MVP | P1 | M | QW | – | stripe-restaurant-ops | 6_Shipped | FEAT-ORD-001, FEAT-PAY-001 |
| FEAT-ORD-011 | Cancel order before acceptance | Customer | FE, BE | MVP | P2 | P | QW | – | stripe-ordering-checkout | 5_In_Review | FEAT-ORD-001 |
| FEAT-ORD-012 | Mark order ready for pickup | Restaurant | FE, BE | MVP | P1 | M | QW | – | stripe-restaurant-ops | 5_In_Review | FEAT-ORD-010 |
| FEAT-ORD-013 | Rate completed order | Customer | FE, BE | MVP | P2 | P | QW | – | stripe-ordering-checkout | 3_Ready_to_Build | FEAT-DEL-002 |

---

## Domain: Restaurant (REST)

### FS-03: Restaurant Onboarding & Menu

| ID | Feature | Actor | Layer | Phase | Pri | KANO | V×C | Sub | Stripe | Status | Deps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FEAT-REST-001 | Onboard new restaurant profile | Restaurant | FE, BE | MVP | P1 | M | BB | ✓ | stripe-restaurant-ops | 6_Shipped | none |
| FEAT-REST-002 | Publish menu item | Restaurant | FE, BE | MVP | P1 | M | QW | – | stripe-restaurant-ops | 6_Shipped | FEAT-REST-001 |
| FEAT-REST-003 | Toggle menu item availability | Restaurant | FE, BE | MVP | P1 | M | QW | – | stripe-restaurant-ops | 6_Shipped | FEAT-REST-002 |
| FEAT-REST-004 | Pause restaurant for online orders | Restaurant | FE, BE | MVP+ | P2 | P | QW | – | stripe-restaurant-ops | 1_Backlog | FEAT-REST-001 |
| FEAT-REST-005 | Deactivate restaurant partnership | Admin | FE, BE | MVP+ | P3 | P | FI | – | stripe-restaurant-ops | 1_Backlog | FEAT-REST-001 |
| FEAT-REST-006 | Display multilingual menu translations | Restaurant | FE, BE | Cut | P4 | I | TW | – | none | 1_Backlog | FEAT-REST-002 |

---

## Domain: Delivery (DEL)

### FS-04: Courier Dispatch & Delivery Execution

| ID | Feature | Actor | Layer | Phase | Pri | KANO | V×C | Sub | Stripe | Status | Deps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FEAT-DEL-001 | Apply as new courier | Courier | FE, BE | MVP | P1 | M | QW | – | stripe-delivery-dispatch | 6_Shipped | none |
| FEAT-DEL-002 | Track assigned delivery in real time | Courier | FE, BE | MVP | P1 | M | BB | ✓ | stripe-delivery-dispatch | 3_Ready_to_Build | FEAT-ORD-012, FEAT-DEL-001, FEAT-DEL-005, FEAT-DEL-003 |
| FEAT-DEL-003 | Toggle courier online availability | Courier | FE, BE | MVP | P1 | M | QW | – | stripe-delivery-dispatch | 3_Ready_to_Build | FEAT-DEL-001, FEAT-DEL-005 |
| FEAT-DEL-004 | Auto-suspend courier below rating threshold | System | BE, SYS | MVP | P1 | M | QW | – | stripe-delivery-dispatch | 2_Spec_Done | FEAT-DEL-002 |
| FEAT-DEL-005 | Approve courier application | Admin | FE, BE | MVP | P1 | M | QW | – | stripe-delivery-dispatch | 6_Shipped | FEAT-DEL-001 |

---

## Domain: Payments (PAY)

### FS-05: Payment Authorization & Payout

| ID | Feature | Actor | Layer | Phase | Pri | KANO | V×C | Sub | Stripe | Status | Deps |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FEAT-PAY-001 | Authorize payment for placed order | System | BE | MVP | P1 | M | BB | – | stripe-ordering-checkout | 6_Shipped | FEAT-ORD-001 |
| FEAT-PAY-002 | Capture payment on restaurant acceptance | System | BE | MVP | P1 | M | QW | – | stripe-ordering-checkout | 6_Shipped | FEAT-ORD-010, FEAT-PAY-001 |
| FEAT-PAY-003 | Auto-refund unaccepted order payment | System | BE, SYS | MVP | P1 | M | QW | – | stripe-ordering-checkout | 6_Shipped | FEAT-ORD-001, FEAT-PAY-001 |
| FEAT-PAY-004 | Calculate daily courier payout batch | System | BE, SYS | MVP | P2 | P | BB | – | stripe-ordering-checkout | 4_In_Build | FEAT-DEL-002 |
| FEAT-PAY-005 | Generate 1099-NEC tax document for courier | System | BE, SYS | MVP+ | P2 | M | FI | – | stripe-ordering-checkout | 1_Backlog | FEAT-PAY-004 |

> **Priority note - PAY-005:** classified KANO Must-be on a compliance-risk lens (absence exposes couriers and PureHunger to IRS penalties past the Jan 31 deadline, per BR-REG-002), not on the usual customer-delight lens - couriers don't notice this feature until tax season. Kept at P2 and pushed to MVP+ because the *build* isn't launch-blocking (first tax-year deadline is 8+ months post-launch), not because the rule matters less.
>
> **Priority note - REST-005:** KANO Performance but scored low Value (2) and Fill-in on V×C - deprioritized to P3 against the mapping table's general "Performance → P2" guidance because the feature protects margin on a rare event (partner churn), not day-to-day operations.

---

## Features Flagged for Splitting

None. All 23 features pass the atomicity test (one coherent client-valued result, expressible as `<verb> <result> <object>`). FEAT-ORD-001 and FEAT-DEL-002 are intentionally larger single features (Big Bet / L estimate) rather than split, because each is one client-perceived outcome (an order successfully placed; a delivery successfully tracked end-to-end) even though the underlying flow has several steps - see each card's Subtasks section for the internal nuances that were *not* promoted to separate Features.

---

## Feature Count Summary

| Domain | Feature Sets | Features |
|---|---|---|
| Ordering (ORD) | FS-01, FS-02 | 7 |
| Restaurant (REST) | FS-03 | 6 |
| Delivery (DEL) | FS-04 | 5 |
| Payments (PAY) | FS-05 | 5 |
| **Total** | **5** | **23** |

---

## Entity-Coverage Cross-Check

Every transition in `entities.md` traces to a triggering feature; every feature maps to a real entity operation or transition:

| Entity | Transition | Triggering feature |
|---|---|---|
| Order | Cart → Placed | FEAT-ORD-001 |
| Order | Placed → Accepted → Preparing | FEAT-ORD-010 |
| Order | Preparing → ReadyForPickup | FEAT-ORD-012 |
| Order | ReadyForPickup → OutForDelivery | FEAT-DEL-002 (mirrors Delivery PickedUp) |
| Order | OutForDelivery → Delivered | FEAT-DEL-002 (mirrors Delivery Completed) |
| Order | Placed → Cancelled | FEAT-ORD-011 |
| Order | Placed → Refunded | FEAT-PAY-003 |
| Restaurant | Pending → Active | FEAT-REST-001 |
| Restaurant | Active → Paused → Active | FEAT-REST-004 |
| Restaurant | Active/Paused → Deactivated | FEAT-REST-005 |
| MenuItem | availability toggle | FEAT-REST-003 |
| Courier | Applied → Active | FEAT-DEL-005 |
| Courier | Active → Suspended | FEAT-DEL-004 |
| Courier | Online/Offline substate | FEAT-DEL-003 |
| Delivery | (none) → Assigned → ... → Completed | FEAT-DEL-002 |
| Payment | (none) → Authorized | FEAT-PAY-001 |
| Payment | Authorized → Captured | FEAT-PAY-002 |
| Payment | Authorized → Refunded | FEAT-PAY-003 |
| CourierPayout | batch creation | FEAT-PAY-004 |

No dead states and no scope-creep features found - every row above has exactly one owner.

---

## Features Not in Scope (from PRD)

| Capability | Reason excluded | Reconsider when |
|---|---|---|
| Native iOS/Android apps | Web/PWA sufficient to validate the Boise pilot | After PMF proven on web (Phase 2) |
| PureHunger+ subscription | Post-MVP per product framing - free-delivery subscription cannibalizes delivery-fee revenue until order loop is proven | Phase 2, after MVP retention signal holds |
| Scheduled / future orders | Adds complexity to dispatch and kitchen-timing logic not needed to prove core loop | Phase 3 |
| Group ordering | Multi-payer cart splitting is a distinct, complex feature set | Phase 3 |
| Loyalty rewards program | Requires retention data from MVP to design a program that actually changes behavior | Phase 3 |

---

## KANO Analysis

### KANO Categories

| Category | Definition | MVP implication |
|---|---|---|
| Must-be | Expected by default. Absence = dissatisfied. Presence is neutral. | Always in MVP |
| Performance | More = better. Linear satisfaction. | Prioritize highest-impact |
| Delighter | Unexpected. Delights when present. No dissatisfaction if absent. | Post-MVP unless very fast to build |
| Indifferent | Neither satisfied nor dissatisfied. | Cut or defer indefinitely |

### Feature KANO Classification

| Feature | KANO Category | Rationale |
|---|---|---|
| FEAT-ORD-001: Place order from restaurant cart | Must-be | Without this, nobody can use PureHunger at all - it is the product |
| FEAT-ORD-002: Search restaurants by cuisine and location | Must-be | Customers assume discovery works; Boise's thin selection makes findability table-stakes, not a differentiator |
| FEAT-ORD-003: Reorder previous order | Delighter | Convenience surprise for repeat customers - the loop works fine without it |
| FEAT-ORD-010: Accept order and start preparing | Must-be | Without restaurant confirmation, no order can ever be fulfilled |
| FEAT-ORD-011: Cancel order before acceptance | Performance | More cancellation flexibility = more trust; not expected to be instant/perfect from day one |
| FEAT-ORD-012: Mark order ready for pickup | Must-be | Gates the entire delivery handoff (BR-DEL-002) - no substitute |
| FEAT-ORD-013: Rate completed order | Performance | More ratings data = better courier/restaurant quality signal over time; a thin version (1-5 stars) still works |
| FEAT-REST-001: Onboard new restaurant profile | Must-be | Zero restaurants = zero product |
| FEAT-REST-002: Publish menu item | Must-be | No menu = nothing to order |
| FEAT-REST-003: Toggle menu item availability | Must-be | Directly protects BR-ORD-002 - an unenforced version breaks trust immediately (86'd items still orderable) |
| FEAT-REST-004: Pause restaurant for online orders | Performance | More operational control = fewer bad orders during rushes/closures, not expected on day one |
| FEAT-REST-005: Deactivate restaurant partnership | Performance | Needed eventually for churn/offboarding, but low frequency and not customer-facing |
| FEAT-REST-006: Display multilingual menu translations | Indifferent | Boise pilot market is English-first; no validated customer demand signal |
| FEAT-DEL-001: Apply as new courier | Must-be | Zero couriers = zero deliveries |
| FEAT-DEL-002: Track assigned delivery in real time | Must-be | Live tracking is the baseline expectation set by every competitor Maya has used |
| FEAT-DEL-003: Toggle courier online availability | Must-be | Couriers (Priya) need control over when they're dispatchable - without it, no flexible gig work |
| FEAT-DEL-004: Auto-suspend courier below rating threshold | Must-be | Safety/quality floor (BR-DEL-001) - absence risks customer harm and platform reputation |
| FEAT-DEL-005: Approve courier application | Must-be | No vetting = no trust in who shows up with the food |
| FEAT-PAY-001: Authorize payment for placed order | Must-be | Customers expect payment to just work; failure here kills the transaction |
| FEAT-PAY-002: Capture payment on restaurant acceptance | Must-be | Directly protects BR-PAY-001 - the core trust promise ("we don't charge you for an order nobody confirmed") |
| FEAT-PAY-003: Auto-refund unaccepted order payment | Must-be | Directly protects BR-PAY-002 - the safety net if the promise above is ever violated |
| FEAT-PAY-004: Calculate daily courier payout batch | Performance | Daily (vs. industry-standard weekly) payout is an explicit differentiator Priya's persona cares about - more frequency/transparency = more satisfaction |
| FEAT-PAY-005: Generate 1099-NEC tax document for courier | Must-be | Compliance-risk lens (BR-REG-002) - absence is a legal dissatisfier once triggered, even though couriers never "notice" it positively |

### KANO Summary

| Category | Count | Notes |
|---|---|---|
| Must-be | 16 | All in MVP except none deferred - every Must-be feature ships at launch |
| Performance | 5 | FEAT-PAY-004 (daily payout) and FEAT-ORD-013 (rating) are in MVP as core differentiators/inputs; FEAT-ORD-011 in MVP for trust; FEAT-REST-004/005 deferred to MVP+ (operational maturity, not launch-blocking) |
| Delighter | 1 | FEAT-ORD-003 deferred to MVP+ |
| Indifferent | 1 | FEAT-REST-006 cut |

---

## Value vs. Complexity Matrix

### Quadrants

| Quadrant | Value | Complexity | Action |
|---|---|---|---|
| Quick Win | High | Low | Do first |
| Big Bet | High | High | Plan carefully, phase |
| Fill-in | Low | Low | Only if fits naturally |
| Time Waster | Low | High | Cut |

### Feature Scoring

| Feature | Value (1-5) | Complexity (1-5) | Quadrant | Notion Priority |
|---|---|---|---|---|
| FEAT-ORD-001: Place order from restaurant cart | 5 | 4 | Big Bet | P1 - Critical |
| FEAT-ORD-002: Search restaurants by cuisine and location | 5 | 2 | Quick Win | P1 - Critical |
| FEAT-ORD-003: Reorder previous order | 3 | 2 | Fill-in | P3 - Medium |
| FEAT-ORD-010: Accept order and start preparing | 5 | 2 | Quick Win | P1 - Critical |
| FEAT-ORD-011: Cancel order before acceptance | 4 | 1 | Quick Win | P2 - High |
| FEAT-ORD-012: Mark order ready for pickup | 5 | 1 | Quick Win | P1 - Critical |
| FEAT-ORD-013: Rate completed order | 4 | 1 | Quick Win | P2 - High |
| FEAT-REST-001: Onboard new restaurant profile | 5 | 3 | Big Bet | P1 - Critical |
| FEAT-REST-002: Publish menu item | 5 | 2 | Quick Win | P1 - Critical |
| FEAT-REST-003: Toggle menu item availability | 4 | 1 | Quick Win | P1 - Critical |
| FEAT-REST-004: Pause restaurant for online orders | 3 | 1 | Quick Win | P2 - High |
| FEAT-REST-005: Deactivate restaurant partnership | 2 | 1 | Fill-in | P3 - Medium |
| FEAT-REST-006: Display multilingual menu translations | 1 | 3 | Time Waster | P4 - Low |
| FEAT-DEL-001: Apply as new courier | 5 | 2 | Quick Win | P1 - Critical |
| FEAT-DEL-002: Track assigned delivery in real time | 5 | 4 | Big Bet | P1 - Critical |
| FEAT-DEL-003: Toggle courier online availability | 4 | 1 | Quick Win | P1 - Critical |
| FEAT-DEL-004: Auto-suspend courier below rating threshold | 5 | 2 | Quick Win | P1 - Critical |
| FEAT-DEL-005: Approve courier application | 4 | 1 | Quick Win | P1 - Critical |
| FEAT-PAY-001: Authorize payment for placed order | 5 | 3 | Big Bet | P1 - Critical |
| FEAT-PAY-002: Capture payment on restaurant acceptance | 5 | 2 | Quick Win | P1 - Critical |
| FEAT-PAY-003: Auto-refund unaccepted order payment | 5 | 2 | Quick Win | P1 - Critical |
| FEAT-PAY-004: Calculate daily courier payout batch | 4 | 3 | Big Bet | P2 - High |
| FEAT-PAY-005: Generate 1099-NEC tax document for courier | 3 | 2 | Fill-in | P2 - High |

**Quadrant totals:** Quick Win 14 · Big Bet 5 · Fill-in 3 · Time Waster 1

### Sequencing Signal

```
First in delivery: Quick Wins from Must-be category
  → FEAT-ORD-002, FEAT-ORD-010, FEAT-ORD-012, FEAT-REST-002, FEAT-REST-003,
    FEAT-DEL-001, FEAT-DEL-003, FEAT-DEL-004, FEAT-DEL-005, FEAT-PAY-002, FEAT-PAY-003

Then: Big Bets (high value, plan carefully)
  → FEAT-ORD-001, FEAT-REST-001, FEAT-DEL-002, FEAT-PAY-001, FEAT-PAY-004

Later: Fill-ins alongside other work
  → FEAT-ORD-003, FEAT-REST-005, FEAT-PAY-005

Cut: Time Wasters + Indifferent
  → FEAT-REST-006
```

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-04-06 | Initial extraction from PRD Business Capabilities (Phase 5) |
| 1.1 | 2026-07-16 | MVP cut + Delivery Stripe assignment applied via `/pm-mvp-scope`; `phase` and `stripe` columns populated across all 23 features |
