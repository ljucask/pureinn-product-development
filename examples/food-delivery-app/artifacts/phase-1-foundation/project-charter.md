# Project Charter - PureHunger

> **Version:** 1.0 · **Status:** Approved (Phase 1 gate passed) · **Date:** 2025-10-06
> **Owner:** Sam Okonkwo (CEO / Product)

---

## Why this project exists

**Trigger:**
Sam Okonkwo spent two years as ops lead at a regional grocery delivery startup watching independent merchants get squeezed by 25-30% platform commissions. Direct conversations with Boise restaurant owners - including Daniel Osei, who dropped a major delivery platform after 18 months because commission ate the margin on his already-thin-margin West African menu - confirmed the same pattern holds in food delivery, and that mid-size cities are where it hurts most.

**Strategic opportunity:**
Mid-size cities (100k-500k population) are structurally underserved by delivery apps built for dense urban cores: thin restaurant selection, long delivery times, and independent restaurants buried under chain placement. A lower commission structure (12% vs. 25-30%) is a defensible wedge in these markets specifically because unit economics there don't require the volume major platforms optimize for.

---

## What we are building

**Product / Initiative:**
PureHunger - a three-sided hyper-local food delivery marketplace (customers, independent restaurants, couriers) launching first in Boise, Idaho. Restaurants pay 12% commission (not 25-30%), customers pay a flat $2.99 delivery fee, and couriers are paid daily ($4 base + $1.25/mile + 100% tips) instead of on a weekly cycle. The MVP is the ordering loop end to end: browse restaurant, build cart, checkout and pay, restaurant accepts, courier delivers, customer rates.

**In Scope:**
- Customer-facing ordering flow (browse, cart, checkout, order tracking, rating)
- Restaurant-facing order management (accept/reject, menu and availability management)
- Courier-facing delivery assignment, live tracking, and daily payout
- Boise, Idaho as the single MVP launch market

**Out of Scope:**
- PureHunger+ subscription tier (free delivery over $15) - post-MVP
- Scheduled / future orders - post-MVP
- Group ordering - post-MVP
- Loyalty rewards - post-MVP
- Any second market beyond Boise until MVP unit economics are proven

**Scope flex (first to cut if time or budget runs short):**
Post-MVP features (subscription, scheduled orders, group ordering, loyalty) are already out of scope and are the first line of defense. Within MVP scope itself, the first thing to cut is depth of restaurant-facing tooling (e.g. advanced menu analytics) - the ordering loop itself (browse → cart → pay → accept → deliver → rate) does not flex; without all six steps there is no marketplace to launch.

---

## Definition of success

**North Star (6-12 months):**
Grow Weekly Active Ordering Households (a household placing at least one order in a 7-day window) in Boise to a level that proves the 12%-commission model produces a healthy, replicable marketplace - clearing the bar to fund and plan a second-market decision.

**Key metrics:**
| Metric | Target | Horizon |
|---|---|---|
| Weekly Active Ordering Households (Boise) | 150 | 6 months |
| Weekly Active Ordering Households (Boise) | 600 | 12 months |
| Active restaurant partners | 40 | 6 months |
| Active couriers (weekly online) | 60 | 6 months |
| Activation (first order within 7 days of signup) | 55% | 6 months |
| Retention (2nd order within 21 days) | 40% | 6 months |
| Second-market Go/No-Go decision | Made, with data | 12 months |

These are not vanity metrics - Weekly Active Ordering Households and 21-day repeat-order rate are the two numbers that would fail if the core bet (restaurants tolerate 12% and customers keep coming back) is wrong. Signups or downloads are deliberately excluded as success criteria.

---

## Constraints and non-negotiables

| Type | Detail |
|---|---|
| Budget | Bootstrapped founder capital + $180K pre-seed SAFE (Grace Lindqvist, angel) - hard cap until a priced round |
| Timeline | Boise MVP launch within 4 months of kickoff (target: end of January 2026) |
| Tech stack | Builds on Lena Vogt's existing ordering/dispatch prototype - not a from-scratch stack decision |
| Regulation | Courier classification as independent contractors (gig-worker employment law); PCI scope minimization for payments (no raw card storage - BR-GOV-001); 1099-NEC issuance for couriers paid over $600/year (BR-REG-001) |
| Other | Restaurant Partner Agreement requires 30 days written notice for any commission rate change (BR-REG-001) - this is a contractual constraint on the business model itself, not just a policy preference |

---

## Decision authority

**Project Owner:** Sam Okonkwo (CEO / Product)
**Go/No-Go approver:** Sam Okonkwo, with Lena Vogt and Marcus Field consulted
**Conflict escalation:** Full founder vote (Sam, Lena, Marcus); Sam holds the tie-break as CEO

---

*This document authorizes Phase 1 initiation. All assumptions will be validated in Phase 2 (Discovery).*

---

# Assumptions & Risks Register - PureHunger

> **Version:** 1.0 · **Date:** 2025-10-06 · **Owner:** Sam Okonkwo
> Update at each phase gate.

---

## Assumptions

| ID | Assumption | Category | Consequence if false | Validation (when/how) | Status |
|---|---|---|---|---|---|
| A-01 | Independent restaurants will accept a 12% take rate as a strong enough differentiator to switch to or newly adopt delivery, even with PureHunger's smaller order volume vs. major platforms at launch **(RISKIEST)** | Business | Restaurant acquisition stalls before the marketplace reaches liquidity - no supply, no customers | Phase 2 - structured interviews with 10+ Boise independent restaurant owners, including Daniel Osei | Partially validated - Daniel Osei and 2 other owners confirmed intent to sign; broader sample pending |
| A-02 | Customers in Boise will tolerate a thinner initial restaurant selection (~40 at launch vs. hundreds on major platforms) in exchange for better discovery of independent spots and comparable delivery speed | Customer | Activation and retention targets miss; customers default back to incumbent apps for selection | Phase 2 customer interviews + Phase 8 beta cohort activation tracking | Unvalidated |
| A-03 | Couriers will accept the per-delivery payout structure ($4 base + $1.25/mile + 100% tips, paid daily) as competitive against other gig work available in Boise | Business / Market | Courier supply is undersupplied, delivery times balloon, customer experience suffers, retention collapses | Phase 2 courier interviews (incl. Priya Nair) + Phase 8 fill-rate monitoring post-launch | Unvalidated |
| A-04 | Daily courier payouts are cash-flow sustainable given restaurant payment terms and card-network/processor settlement timing (PureHunger fronts courier pay before it fully collects) | Business / Finance | Company hits a working-capital crunch as order volume scales, even if the marketplace itself is healthy | Phase 1 - cash-flow model validated against the payment processor's actual settlement schedule before launch | Validated - 3-week payout reserve modeled and funded from pre-seed |

**Categories:** Customer · Market · Tech · Business · Regulation · Team

> A-01 is marked `(RISKIEST)` - if restaurants won't accept 12% as meaningfully different from the status quo, the entire marketplace thesis fails before customers or couriers are even relevant. Phase 2 discovery and Phase 3a experiments attack A-01 first, not A-02/A-03.

---

## Risks

| ID | Risk | Probability | Impact | Severity | Mitigation | Owner |
|---|---|---|---|---|---|---|
| R-01 | Cash-flow strain from daily courier payouts outpacing restaurant/customer payment settlement | Medium | High | 🔴 | Hold a 3-week payout reserve before launch; negotiate T+1 settlement with payment processor; monitor daily cash position weekly during Phase 8-9 | Sam Okonkwo |
| R-02 | Gig-worker classification shift (state or federal) reclassifies couriers as employees, changing the payout unit economics entirely | Low-Medium | High | 🟡 | External employment counsel reviews the courier agreement before launch and quarterly thereafter; monitor Idaho and federal gig-worker legislation | Sam Okonkwo (+ external legal) |
| R-03 | Marketplace cold start in Boise - not enough restaurants to attract customers, not enough customers to attract restaurants | High | High | 🔴 | Concierge-onboard a hand-recruited restaurant base (Marcus's relationships, incl. Daniel Osei) before public customer-facing launch; do not open customer signup until 25+ restaurants are live | Marcus Field |
| R-04 | A major platform (Uber Eats / DoorDash-style) responds to PureHunger's Boise entry by temporarily cutting commission or offering incentives to squeeze it out | Medium | Medium | 🟡 | Compete on restaurant trust and payout transparency (structural, not promotional) rather than matching short-term price wars; lock in Restaurant Partner Agreements with the 30-day notice clause (BR-REG-001) so the relationship isn't a month-to-month bidding war | Sam Okonkwo |

**Severity = Probability × Impact:**
- 🔴 Critical - address immediately
- 🟡 Medium - monitor, mitigation in plan
- 🟢 Low - accept or monitor

---

*Register is updated at each phase exit gate.*
