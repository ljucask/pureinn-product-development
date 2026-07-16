# Product Roadmap - PureHunger

> **Phase created:** 3 - Define & Validation
> **Current version:** v3
> **Last updated:** 2026-07-16
> **Next scheduled update:** After `/pm-mvp-scope` re-run (post-MVP feature carding) or Phase 2 kickoff

---

## Vision

**3-year vision:**
Independent restaurants in mid-size American cities keep the delivery revenue they've earned instead of surrendering a third of it to a platform that doesn't need it - and the customers in those cities discover the good local spots the big platforms bury under chains that pay for placement.

**12-month goal:**
Prove the full three-sided loop (customer, restaurant, courier) works end-to-end in one pilot market (Boise, ID) at a 12% commission, with restaurants staying on the platform past their first 90 days and couriers preferring PureHunger's daily payout over competitors' weekly cycle.

**North Star Metric:** Weekly Active Ordering Households (a household placing ≥1 order in a 7-day window)
**NSM Target (Month 12):** 2,000+ Weekly Active Ordering Households in Boise

---

## Strategic Phases

### Phase 1: Prove the Loop in Boise - Q1-Q2 2026
**Goal:** Prove that independent restaurants will accept 12% commission and that the full order-to-delivery loop works without manual intervention, in one pilot market.
**Focus:** Ordering, restaurant onboarding, courier dispatch, payment authorization/capture/refund - the MVP.
**Key hypothesis being tested:** Restaurants like Daniel Osei's will stay on a delivery platform if the commission structure doesn't erode their margin, and customers like Maya will trust and repeat-order from independent restaurants they discover through the app.

**Success criteria (phase exit gate):**
- [ ] 25 active restaurants onboarded in Boise
- [ ] Weekly Active Ordering Households ≥ 500
- [ ] Activation ≥ 60% (first order within 7 days of signup)
- [ ] Retention ≥ 35% (2nd order within 21 days)
- [ ] ≥ 40 active couriers sustaining average delivery time under 35 minutes

**What we are NOT doing in this phase:**
- PureHunger+ subscription, scheduled/future orders, group ordering, loyalty rewards (all Phase 3+)
- Any market beyond Boise
- Native iOS/Android apps (web/PWA only)

---

### Phase 2: Boise Scale + Retention Optimization - Q3-Q4 2026
**Goal:** Scale restaurant and courier supply in Boise toward profitability and introduce the first deliberate retention lever.
**Focus:** PureHunger+ subscription pilot, reorder feature, restaurant operational maturity (pause/deactivate, payout visibility).
**Key hypothesis being tested:** A $6.99/mo subscription with free delivery over $15 increases order frequency enough to offset the cannibalized delivery-fee revenue.

**Unlock condition:** Phase 1 success criteria met (WAOH ≥ 500, retention ≥ 35%, restaurant/courier supply targets hit).

**Success criteria:**
- [ ] Weekly Active Ordering Households ≥ 2,000
- [ ] ≥ 15% of active households subscribed to PureHunger+
- [ ] Day-30 retention ≥ 45%
- [ ] Restaurant count ≥ 60, courier count ≥ 90

---

### Phase 3: Multi-City Expansion - 2027
**Goal:** Replicate the Boise playbook in 2-3 additional mid-size cities (100k-500k population).
**Focus:** Scheduled orders, group ordering, loyalty rewards, geographic expansion playbook.

**Unlock condition:** Phase 2 success criteria met AND positive per-order unit economics proven in Boise (contribution margin positive after commission, delivery pay, and payment processing costs).

**Success criteria:**
- [ ] 3 total markets live
- [ ] 12% commission structure held (no erosion under competitive pressure - protected by BR-REG-001's 30-day notice requirement)
- [ ] Aggregate Weekly Active Ordering Households ≥ 6,000

---

## Functional Decomposition (top-down input to the Feature Plan)

| Strategic Phase | Domain | Feature Set (FS-NN) | Capability / business outcome |
|---|---|---|---|
| Phase 1: Prove the Loop | Ordering (ORD) | FS-01: Discovery & Cart | Customer can find an active restaurant and build a valid cart |
| Phase 1: Prove the Loop | Ordering (ORD) | FS-02: Order Fulfillment Lifecycle | Order moves reliably from Placed through Delivered with no manual steps |
| Phase 1: Prove the Loop | Restaurant (REST) | FS-03: Restaurant Onboarding & Menu | Restaurant can join, publish a menu, and keep availability accurate |
| Phase 1: Prove the Loop | Delivery (DEL) | FS-04: Courier Dispatch & Delivery Execution | Courier can onboard, go online, get dispatched, and complete a tracked delivery |
| Phase 1: Prove the Loop | Payments (PAY) | FS-05: Payment Authorization & Payout | Customer is charged fairly (BR-PAY-001/002) and couriers are paid daily |
| Phase 2: Scale + Retention | Ordering (ORD) | FS-01 (extension) | Reorder convenience feature increases order frequency |
| Phase 2: Scale + Retention | Restaurant (REST) | FS-03 (extension) | Restaurant operational maturity: pause, deactivate, payout visibility |
| Phase 2: Scale + Retention | Payments (PAY) | FS-06: Subscription Billing *(not yet carded)* | PureHunger+ recurring billing and free-delivery threshold |
| Phase 3: Multi-City | Ordering (ORD) | FS-07: Scheduled & Group Ordering *(not yet carded)* | Future-dated orders and multi-payer cart splitting |
| Phase 3: Multi-City | Ordering (ORD) | FS-08: Loyalty & Rewards *(not yet carded)* | Points/rewards program to drive retention at scale |

**Derivation rules:** Features are derived from these Feature Sets in `/pm-features-list`, top-down, leaves last. FS-01 through FS-05 are fully carded (see `features/feature_list.md`); FS-06/07/08 are named here as the Phase 2/3 functional targets but intentionally not yet decomposed into Features - premature carding of Phase 2/3 features before Phase 1 validates would violate the "not building now" discipline below.

---

## What We Are Not Building (Now)

| Item | Why deferred | Reconsider when |
|---|---|---|
| PureHunger+ subscription | Free-delivery subscription cannibalizes delivery-fee revenue until the core loop and retention baseline are proven | Phase 2, after Phase 1 retention signal (≥35% 2nd-order) holds |
| Scheduled / future orders | Adds real complexity to dispatch and kitchen-timing logic that isn't needed to prove the core loop | Phase 3 |
| Group ordering | Multi-payer cart splitting is a distinct, non-trivial feature set with its own edge cases | Phase 3 |
| Loyalty rewards program | Needs real retention data from MVP to design a program that changes behavior rather than just costing margin | Phase 3 |
| Native iOS/Android apps | Web/PWA is sufficient to validate the Boise pilot at this scale | After PMF proven on web (Phase 2) |
| Multilingual menu translations (FEAT-REST-006) | Indifferent per KANO - Boise pilot market is English-first, no validated demand | If/when expansion market data (Phase 3) shows real need |

---

## Dependencies and Risks

| Dependency / Risk | Type | Impact | Mitigation |
|---|---|---|---|
| Payment processor (Stripe) integration timeline | External | Could delay Phase 1 launch if tokenization/Connect payout setup slips | Lena started integration early in Phase 5 alongside feature carding, not after |
| Courier supply in a mid-size market | Market | Thinner gig-work labor pool than a dense urban core could cap delivery-time targets | Marcus's local recruiting push + competitive $4 base + $1.25/mile rate + daily payout as the pitch |
| Restaurant commission-change governance (BR-REG-001) | Regulatory/Contractual | 30-day written notice requirement slows any pricing experiment | Priced correctly at launch (12%) rather than planning to adjust early |
| Idaho gig-worker classification (contractor vs. employee) | Regulatory | A classification change could force a payout/benefits model rework mid-pilot | Legal review scheduled before Phase 1 exit; courier agreement drafted with a contractor-status assumption flagged as a risk, not a certainty |
| Founder team bandwidth (1.3 dev-equivalents for MVP) | Internal | FEAT-DEL-002 (dispatch + live tracking) is the single pacing feature - any slip threatens the 4-month pilot commitment | Tracked explicitly in `mvp-scope.md` Capacity Check; no new scope added to Phase 1 until this feature ships |

---

## Roadmap Assumptions

The timeline in this roadmap assumes:
- Sam, Lena, and Marcus remain the full founding team through Phase 1 (no key departure)
- First restaurants are acquired through Marcus's founder-led outreach, not paid marketing
- Stripe Connect (or equivalent) supports daily ACH payouts to couriers without prohibitive per-transaction fees at pilot volume
- No major change to Idaho's gig-worker classification law during the pilot window
- Two anchor restaurants (including Daniel Osei's) honor their launch-partner commitment within the current window

**If any of these change:** re-run `/pm-product-roadmap` v3 in delta mode and re-check the Phase 1 exit criteria and `mvp-scope.md` capacity math before committing to a new date.

---

## MVP Delivery View (v3)

> Added in Phase 5 after MVP Scope is defined (see `artifacts/phase-5-planning/mvp-scope.md` and `features/delivery-stripes.md` - this section summarizes both; those files are the source of truth).

### Feature Sets (logical groupings)

| Feature Set | Description | Feature Cards Status | Priority |
|---|---|---|---|
| FS-01: Discovery & Cart | Restaurant search, cart-build, checkout, reorder | Shipped (core), Backlog (reorder, MVP+) | P1 |
| FS-02: Order Fulfillment Lifecycle | Accept/prepare, cancel, ready-for-pickup, rate | Shipped/In Review (mostly done) | P1 |
| FS-03: Restaurant Onboarding & Menu | Restaurant profile, menu publishing, availability, pause, deactivate | Shipped (core), Backlog (ops maturity, MVP+) | P1 |
| FS-04: Courier Dispatch & Delivery Execution | Courier onboarding, approval, online toggle, dispatch, live tracking, auto-suspend | Shipped (onboarding), Ready to Build / Spec Done (dispatch + tracking) | P1 |
| FS-05: Payment Authorization & Payout | Authorize, capture, refund, daily payout, tax docs | Shipped (core), In Build (payout batch), Backlog (tax doc, MVP+) | P1-P2 |

### Delivery Stripes (domain-focused parallel channels)

| Stripe | Domain focus | Features included | Feature Set(s) | Goal |
|---|---|---|---|---|
| stripe-ordering-checkout | Order (customer-facing) + Payment | FEAT-ORD-001, 002, 011, 013, FEAT-PAY-001, 002, 003, 004 | FS-01, FS-02, FS-05 | Customer can browse, cart, pay, cancel, and rate an order end-to-end |
| stripe-restaurant-ops | Restaurant + Order fulfillment (restaurant-side) | FEAT-REST-001, 002, 003, FEAT-ORD-010, 012 | FS-02, FS-03 | Restaurant can onboard, manage menu, and progress an order to ready-for-pickup |
| stripe-delivery-dispatch | Courier + Delivery | FEAT-DEL-001, 002, 003, 004, 005 | FS-04 | Courier can onboard, go online, get dispatched, and complete a tracked delivery |

**MVP completion:** `stripe-delivery-dispatch` - when FEAT-DEL-002, FEAT-DEL-003, and FEAT-DEL-004 reach `6_Shipped`. This is the only stripe with MVP work remaining; the other two stripes have shipped or are in final review.

### Post-MVP Roadmap

| Horizon | Focus | Feature Sets planned |
|---|---|---|
| Month 1-3 post-MVP | Reorder convenience + restaurant operational maturity (pause/deactivate/payout visibility) | FS-01 (extension), FS-03 (extension) |
| Month 4-6 post-MVP | PureHunger+ subscription pilot, courier tax documentation | FS-06 (new), FS-05 (extension) |
| Month 7-12 post-MVP | Scheduled orders, group ordering, loyalty rewards, multi-city expansion prep | FS-07, FS-08 (new, TBD based on Phase 2 data) |

---

## Version History

| Version | Date | Phase | Key changes |
|---|---|---|---|
| v1 | 2025-11-03 | Phase 3b | Initial - vision, 3 strategic phases, success criteria, business-model horizon (12% commission, $2.99 flat delivery fee, daily courier payout) |
| v2 | 2026-01-19 | Phase 4 | Domain constraints added (Order/Restaurant/Courier/Delivery/Payment state machines from `entities.md`); Functional Decomposition introduced mapping phases to Domains and Feature Sets |
| v3 | 2026-04-06 (feature view added) / 2026-07-16 (delivery status refreshed) | Phase 5 | Feature view added - 23 Features across FS-01 through FS-05; MVP Delivery View with 3 Delivery Stripes; Phase 1 status updated to reflect current build progress (2 of 3 stripes MVP-complete, `stripe-delivery-dispatch` in progress) |

---
**Čo si teraz má:** Jeden živý dokument so všetkými 3 verziami roadmapy - vízia (v1), doménové obmedzenia (v2), a feature/delivery pohľad (v3) - vrátane aktuálneho stavu MVP dodávky.

**Ďalší krok:** `/pm-stripe` - pokračuj v JIT cykle pre `stripe-delivery-dispatch`, jediný stripe blokujúci Phase 1 exit.

**Môžeš preskočiť ak:** Žiadne nové strategické vstupy (validovaný problém, business model, doména, features) sa nezmenili od poslednej verzie.
