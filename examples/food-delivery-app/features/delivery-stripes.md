# Delivery Stripes - PureHunger

> **Phase:** 5 - Feature Planning
> **Date:** 2026-07-16
> **Definition:** A Delivery Stripe is an isolated development channel for a coherent domain slice.
>                MVP cut and stripe assignment are per Feature - not per Feature Set.
>                Feature Sets are grouping only. JIT design and build operate at Feature level.
>
> **MVP membership is recorded in the `phase` field on each feature (`MVP` / `MVP+` / `Cut`) - never a separate `mvp` true/false column.** The table below shows `Phase`, not a boolean.

---

## Stripe Overview

| Stripe ID | Name | Domain focus | MVP Features | Goal |
|---|---|---|---|---|
| stripe-ordering-checkout | Ordering & Checkout Stripe | Order (customer-facing) + Payment | FEAT-ORD-001, FEAT-ORD-002, FEAT-ORD-011, FEAT-ORD-013, FEAT-PAY-001, FEAT-PAY-002, FEAT-PAY-003, FEAT-PAY-004 | Customer can browse, cart, pay, cancel, and rate an order end-to-end |
| stripe-restaurant-ops | Restaurant Ops Stripe | Restaurant + Order fulfillment (restaurant-side) | FEAT-REST-001, FEAT-REST-002, FEAT-REST-003, FEAT-ORD-010, FEAT-ORD-012 | Restaurant can onboard, publish/manage a menu, and progress an order from acceptance through ready-for-pickup |
| stripe-delivery-dispatch | Delivery & Dispatch Stripe | Courier + Delivery | FEAT-DEL-001, FEAT-DEL-002, FEAT-DEL-003, FEAT-DEL-004, FEAT-DEL-005 | Courier can onboard, go online, receive a dispatch, and complete a live-tracked delivery |

**MVP features total:** 18 across 3 stripes
**Post-MVP backlog:** 4 features (FEAT-ORD-003, FEAT-REST-004, FEAT-REST-005, FEAT-PAY-005 - remain assigned to their domain-affinity stripe for when their phase comes up, execution deferred)
**Cut (no stripe):** 1 feature (FEAT-REST-006 - not building, not stripe-assigned)

---

## Stripe Design Rules

- Each stripe covers a coherent domain slice (minimizes register conflicts between parallel agents)
- No feature is assigned to a stripe if its dependencies are in a different stripe that hasn't started
- Feature Sets span multiple stripes - that is expected and correct (FS-02 "Order Fulfillment Lifecycle" splits across `stripe-ordering-checkout` and `stripe-restaurant-ops` because the customer-side and restaurant-side halves of the order lifecycle have different owners and different pace)
- JIT design (`pm-feature-design`) runs per feature, per stripe, just before build
- Stripes can run in parallel (different Claude agents / Class Owners per stripe) - cross-stripe dependencies below are the coordination points that must be respected even when running in parallel

---

## Feature-to-Stripe Assignment

| FEAT-ID | Feature | Phase | Stripe | Dependency on |
|---|---|---|---|---|
| FEAT-ORD-001 | Place order from restaurant cart | MVP | stripe-ordering-checkout | FEAT-REST-001, FEAT-REST-002, FEAT-REST-003 |
| FEAT-ORD-002 | Search restaurants by cuisine and location | MVP | stripe-ordering-checkout | FEAT-REST-001 |
| FEAT-ORD-003 | Reorder previous order | MVP+ | stripe-ordering-checkout | FEAT-ORD-001, FEAT-ORD-013 |
| FEAT-ORD-010 | Accept order and start preparing | MVP | stripe-restaurant-ops | FEAT-ORD-001, FEAT-PAY-001 |
| FEAT-ORD-011 | Cancel order before acceptance | MVP | stripe-ordering-checkout | FEAT-ORD-001 |
| FEAT-ORD-012 | Mark order ready for pickup | MVP | stripe-restaurant-ops | FEAT-ORD-010 |
| FEAT-ORD-013 | Rate completed order | MVP | stripe-ordering-checkout | FEAT-DEL-002 |
| FEAT-REST-001 | Onboard new restaurant profile | MVP | stripe-restaurant-ops | none |
| FEAT-REST-002 | Publish menu item | MVP | stripe-restaurant-ops | FEAT-REST-001 |
| FEAT-REST-003 | Toggle menu item availability | MVP | stripe-restaurant-ops | FEAT-REST-002 |
| FEAT-REST-004 | Pause restaurant for online orders | MVP+ | stripe-restaurant-ops | FEAT-REST-001 |
| FEAT-REST-005 | Deactivate restaurant partnership | MVP+ | stripe-restaurant-ops | FEAT-REST-001 |
| FEAT-REST-006 | Display multilingual menu translations | Cut | none | FEAT-REST-002 |
| FEAT-DEL-001 | Apply as new courier | MVP | stripe-delivery-dispatch | none |
| FEAT-DEL-002 | Track assigned delivery in real time | MVP | stripe-delivery-dispatch | FEAT-ORD-012, FEAT-DEL-001, FEAT-DEL-005, FEAT-DEL-003 |
| FEAT-DEL-003 | Toggle courier online availability | MVP | stripe-delivery-dispatch | FEAT-DEL-001, FEAT-DEL-005 |
| FEAT-DEL-004 | Auto-suspend courier below rating threshold | MVP | stripe-delivery-dispatch | FEAT-DEL-002 |
| FEAT-DEL-005 | Approve courier application | MVP | stripe-delivery-dispatch | FEAT-DEL-001 |
| FEAT-PAY-001 | Authorize payment for placed order | MVP | stripe-ordering-checkout | FEAT-ORD-001 |
| FEAT-PAY-002 | Capture payment on restaurant acceptance | MVP | stripe-ordering-checkout | FEAT-ORD-010, FEAT-PAY-001 |
| FEAT-PAY-003 | Auto-refund unaccepted order payment | MVP | stripe-ordering-checkout | FEAT-ORD-001, FEAT-PAY-001 |
| FEAT-PAY-004 | Calculate daily courier payout batch | MVP | stripe-ordering-checkout | FEAT-DEL-002 |
| FEAT-PAY-005 | Generate 1099-NEC tax document for courier | MVP+ | stripe-ordering-checkout | FEAT-PAY-004 |

---

## Cross-Stripe Dependencies (coordination points)

Running stripes in parallel does not remove real dependencies - it just means the *owning* team must signal readiness across stripe boundaries. These are the load-bearing crossings in this plan:

| Dependent feature (stripe) | Depends on (different stripe) | What must be true before the dependent starts |
|---|---|---|
| FEAT-ORD-001 (Ordering & Checkout) | FEAT-REST-001/002/003 (Restaurant Ops) | At least one Active restaurant with available menu items exists to browse/cart |
| FEAT-ORD-010 (Restaurant Ops) | FEAT-PAY-001 (Ordering & Checkout) | Payment authorization exists before a restaurant can accept (BR-PAY-001 ordering) |
| FEAT-DEL-002 (Delivery & Dispatch) | FEAT-ORD-012 (Restaurant Ops) | An Order must be able to reach `ReadyForPickup` before pickup can ever be marked (BR-DEL-002) |
| FEAT-ORD-013, FEAT-PAY-004 (Ordering & Checkout) | FEAT-DEL-002 (Delivery & Dispatch) | A completed, tracked delivery must exist before there is anything to rate or pay out |

This is why the Delivery & Dispatch Stripe is the current pacing stripe: `stripe-restaurant-ops` and `stripe-ordering-checkout` have already shipped everything needed to prove the loop up through `ReadyForPickup`; the remaining MVP gap is entirely inside Delivery & Dispatch.

---

## Dependency Sequencing per Stripe

**stripe-ordering-checkout:**
1. FEAT-ORD-002 (cross-stripe: needs FEAT-REST-001) - *Shipped*
2. FEAT-ORD-001 (cross-stripe: needs FEAT-REST-001/002/003) - *Shipped*
3. FEAT-PAY-001 (needs FEAT-ORD-001) - *Shipped*
4. FEAT-PAY-003 (needs FEAT-ORD-001, FEAT-PAY-001) - *Shipped*
5. FEAT-ORD-011 (needs FEAT-ORD-001) - *In Review*
6. FEAT-PAY-002 (cross-stripe: needs FEAT-ORD-010; needs FEAT-PAY-001) - *Shipped*
7. FEAT-ORD-013 (cross-stripe: needs FEAT-DEL-002 - **blocked, in progress**) - *Ready to Build*
8. FEAT-PAY-004 (cross-stripe: needs FEAT-DEL-002 - **blocked, in progress**) - *In Build*
9. *(MVP+)* FEAT-ORD-003 (needs FEAT-ORD-001, FEAT-ORD-013)
10. *(MVP+)* FEAT-PAY-005 (needs FEAT-PAY-004)

**stripe-restaurant-ops:**
1. FEAT-REST-001 (no deps) - *Shipped*
2. FEAT-REST-002 (needs FEAT-REST-001) - *Shipped*
3. FEAT-REST-003 (needs FEAT-REST-002) - *Shipped*
4. FEAT-ORD-010 (cross-stripe: needs FEAT-ORD-001, FEAT-PAY-001) - *Shipped*
5. FEAT-ORD-012 (needs FEAT-ORD-010) - *In Review*
6. *(MVP+)* FEAT-REST-004 (needs FEAT-REST-001)
7. *(MVP+)* FEAT-REST-005 (needs FEAT-REST-001)
8. *(Cut - not scheduled)* FEAT-REST-006

**stripe-delivery-dispatch:**
1. FEAT-DEL-001 (no deps) - *Shipped*
2. FEAT-DEL-005 (needs FEAT-DEL-001) - *Shipped*
3. FEAT-DEL-003 (needs FEAT-DEL-001, FEAT-DEL-005) - *Ready to Build*
4. FEAT-DEL-002 (cross-stripe: needs FEAT-ORD-012; needs FEAT-DEL-001, FEAT-DEL-005, FEAT-DEL-003) - *Ready to Build* ← current pacing feature for MVP completion
5. FEAT-DEL-004 (needs FEAT-DEL-002) - *Spec Done*

---
**Čo si teraz má:** Delivery Stripe assignment pre všetkých 23 features - 3 paralelné delivery kanály (Ordering & Checkout, Restaurant Ops, Delivery & Dispatch) s explicitnými cross-stripe závislosťami a poradím.

**Ďalší krok:** `/pm-stripe` - orchestruje JIT cyklus pre `stripe-delivery-dispatch`, kde FEAT-DEL-002 je aktuálna pacing feature blokujúca MVP completion.

**Môžeš preskočiť ak:** Stripe assignment sa nezmenil od posledného behu `/pm-mvp-scope` - nový prechod nepridáva hodnotu.
