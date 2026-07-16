# MVP Scope - PureHunger

> **Phase:** 5 - Feature Planning
> **Date:** 2026-07-16
> **MVP definition:** The minimum set of features that delivers the core value proposition
>                    to the primary persona and enables the first paying customers.

---

## MVP Definition

**What MVP must prove:** We will consider MVP successful if we prove that independent restaurants in a mid-size city (Boise, ID) will accept a 12% commission - instead of leaving delivery platforms entirely or eating 25-30% elsewhere - and that customers will complete the full browse → cart → checkout → accept → deliver → rate loop without human intervention, repeatedly.

**Success signal:** 25 active restaurants onboarded in Boise; Weekly Active Ordering Households ≥ 500 (North Star Metric); Activation ≥ 60% (first order within 7 days of signup); Retention ≥ 35% (2nd order within 21 days); courier supply of ≥ 40 active couriers sustaining an average delivery time under 35 minutes.

**Primary persona served:** Maya Torres - "The Busy Professional Customer" (29, orders 3-4x/week on weeknights, price-sensitive on delivery fees but trusts good food). Daniel Osei ("The Independent Restaurant Owner") and Priya Nair ("The Courier") are equally load-bearing for MVP - this is a three-sided marketplace and the loop fails if any one side is unproven.

**MVP hypothesis non-negotiables:**
- The full order loop must work **without any manual/phone-based fallback** - that is the entire point of proving the platform, not just the commission rate.
- BR-PAY-001 and BR-PAY-002 (payment authorization/capture/refund sequencing) are non-negotiable from day one - a customer being charged for a never-confirmed order would destroy trust in the first week of a fragile three-sided pilot.
- Daily courier payout (FEAT-PAY-004) is non-negotiable for MVP even though it is a "Performance" KANO feature, not "Must-be" - it is an explicit, named differentiator in the courier value proposition (Priya's persona is explicitly frustrated by opaque, weekly-cycle competitors). Cutting it for MVP would remove the reason a courier picks PureHunger over the incumbent.

**Explicit exclusions (confirmed with founding team):** PureHunger+ subscription, scheduled/future orders, group ordering, and loyalty rewards are excluded regardless of KANO/V×C scoring - these require retention data from a working MVP to design correctly, and adding any of them now would dilute focus on proving the core loop.

---

## In MVP

| Feature | ID | KANO | V×C | Delivery Stripe |
|---|---|---|---|---|
| Place order from restaurant cart | FEAT-ORD-001 | Must-be | Big Bet | stripe-ordering-checkout |
| Search restaurants by cuisine and location | FEAT-ORD-002 | Must-be | Quick Win | stripe-ordering-checkout |
| Cancel order before acceptance | FEAT-ORD-011 | Performance | Quick Win | stripe-ordering-checkout |
| Rate completed order | FEAT-ORD-013 | Performance | Quick Win | stripe-ordering-checkout |
| Accept order and start preparing | FEAT-ORD-010 | Must-be | Quick Win | stripe-restaurant-ops |
| Mark order ready for pickup | FEAT-ORD-012 | Must-be | Quick Win | stripe-restaurant-ops |
| Onboard new restaurant profile | FEAT-REST-001 | Must-be | Big Bet | stripe-restaurant-ops |
| Publish menu item | FEAT-REST-002 | Must-be | Quick Win | stripe-restaurant-ops |
| Toggle menu item availability | FEAT-REST-003 | Must-be | Quick Win | stripe-restaurant-ops |
| Apply as new courier | FEAT-DEL-001 | Must-be | Quick Win | stripe-delivery-dispatch |
| Approve courier application | FEAT-DEL-005 | Must-be | Quick Win | stripe-delivery-dispatch |
| Toggle courier online availability | FEAT-DEL-003 | Must-be | Quick Win | stripe-delivery-dispatch |
| Track assigned delivery in real time | FEAT-DEL-002 | Must-be | Big Bet | stripe-delivery-dispatch |
| Auto-suspend courier below rating threshold | FEAT-DEL-004 | Must-be | Quick Win | stripe-delivery-dispatch |
| Authorize payment for placed order | FEAT-PAY-001 | Must-be | Big Bet | stripe-ordering-checkout |
| Capture payment on restaurant acceptance | FEAT-PAY-002 | Must-be | Quick Win | stripe-ordering-checkout |
| Auto-refund unaccepted order payment | FEAT-PAY-003 | Must-be | Quick Win | stripe-ordering-checkout |
| Calculate daily courier payout batch | FEAT-PAY-004 | Performance | Big Bet | stripe-ordering-checkout |

**MVP total:** 18 features across 3 stripes (~11-13 weeks at current team size, see Capacity Check below)

---

## Post-MVP

| Feature | ID | KANO | Reason deferred | Target phase |
|---|---|---|---|---|
| Reorder previous order | FEAT-ORD-003 | Delighter | Convenience layer - the loop works without it | MVP+ |
| Pause restaurant for online orders | FEAT-REST-004 | Performance | Operational control, not needed to prove first orders | MVP+ |
| Deactivate restaurant partnership | FEAT-REST-005 | Performance | Low-frequency offboarding action; manual admin workaround acceptable at pilot scale | MVP+ |
| Generate 1099-NEC tax document for courier | FEAT-PAY-005 | Must-be (compliance) | Legally required, but the Jan 31 deadline (BR-REG-002) is 8+ months past pilot launch - not launch-blocking | MVP+ (before end of first calendar year) |

---

## Cut (Not building)

| Feature | ID | Reason |
|---|---|---|
| Display multilingual menu translations | FEAT-REST-006 | Indifferent per KANO - Boise pilot market is English-first with no validated customer demand signal; revisit only if expansion market data shows otherwise |

**Also cut at the roadmap level (not even carded as features - see `product/product-roadmap-v3.md` "What We Are Not Building"):** PureHunger+ subscription, scheduled/future orders, group ordering, loyalty rewards program, native iOS/Android apps.

---

## Capacity Check (against team size and timeline)

**Team:** 3 people - Sam Okonkwo (CEO/Product), Lena Vogt (CTO, owns build), Marcus Field (Growth & Restaurant Partnerships, non-technical). Effectively **1 full-time engineer (Lena)** for MVP build, with Sam contributing part-time on frontend/product work. Treat as **~1.3 developer-equivalents**.

**Timeline constraint:** Runway-constrained - the founding team has committed to a Boise pilot launch within 4 months of Phase 5 sign-off (milestone: 25 restaurants + working end-to-end loop), driven by a soft handshake with two anchor restaurants (including Daniel Osei's) who agreed to be launch partners for a limited window.

**Reconciliation:**
- 18 MVP features break down as: 14 Quick Win-equivalent (≈3-5 days each at this team's velocity) + 4 Big Bet-equivalent (FEAT-ORD-001, FEAT-REST-001, FEAT-DEL-002, FEAT-PAY-001, FEAT-PAY-004 - wait, 5 Big Bets; see V×C matrix) at ≈2-3 weeks each.
- Rough load: 14 Quick Wins × 4 days ≈ 8 weeks (sequential) + 5 Big Bets × 2.5 weeks ≈ 12.5 weeks if built serially. At ~1.3 developer-equivalents with the 3-stripe parallelization this plan uses, effective throughput is closer to 14-16 weeks of serial-equivalent work compressed into **~11-13 calendar weeks** - this is snug but workable against a 16-week (4-month) constraint, **provided the current status holds**: as of this scope, `stripe-ordering-checkout` and `stripe-restaurant-ops` are effectively done (all MVP features Shipped/In Review), and the only remaining MVP gap is `stripe-delivery-dispatch` (FEAT-DEL-002, FEAT-DEL-003, FEAT-DEL-004 not yet shipped).
- **Verdict:** on track, not slack. If FEAT-DEL-002 (Big Bet, dispatch + live tracking) slips more than ~2 weeks past its Ready-to-Build estimate, the 4-month pilot commitment is at risk - this is the single feature to watch.

---
**Čo si teraz má:** Definitívny IN/POST-MVP/CUT rozhodovací rez pre všetkých 23 features, zapísaný výhradne cez `phase` field (žiadny samostatný `mvp` boolean) - a realistický capacity check proti tímu a termínu.

**Ďalší krok:** `/pm-stripe` - spusti JIT delivery cyklus pre `stripe-delivery-dispatch`, kde FEAT-DEL-002 je aktuálne pacing feature.

**Môžeš preskočiť ak:** MVP cut sa nezmenil od posledného schválenia - žiadne nové PRD/roadmap vstupy, ktoré by ho menili.
