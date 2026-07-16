# Lean Canvas

**Product:** PureHunger
**Date:** 2025-12-15
**Status:** Phase 3b - Commercial Definition (Go/No-Go: GO)

---

## Canvas Overview

| Block | Content |
|---|---|
| **Problem** | 1. Independent restaurants lose thin margins to 25-30% commission / 2. Customers in mid-size cities get thin selection and long delivery times / 3. Couriers face opaque, weekly-cycle payout on incumbent platforms |
| **Existing alternatives** | Major national platforms (Uber Eats/DoorDash-style) for restaurants; ordering from platform-favored chains or self-pickup for customers; multi-app gig work for couriers |
| **Customer segments** | Independent, single-location restaurant owners in mid-size US cities (primary economic segment); busy professional customers in the same cities (demand segment) |
| **Early adopters** | Independent restaurants in Boise, ID not currently on any major platform or actively unhappy with platform economics; digitally-active professionals in Boise's core neighborhoods |
| **Unique value proposition** | Keep more of every order you make - 12% commission instead of 25-30%, passed into faster courier payouts and fair, non-pay-to-play restaurant discovery |
| **High-level concept** | The commission-fair delivery marketplace for independent restaurants |
| **Solution** | 1. Flat 12% commission, published rate card / 2. Merit-ranked discovery (proximity, rating, repeat orders), no sponsored placement / 3. Daily courier payout with transparent per-delivery earnings |
| **Channels** | Direct owner-to-owner restaurant outreach (primary, supply side) + geo-targeted digital ads and local community reach (secondary, demand side) |
| **Revenue streams** | 12% commission per order + $2.99 flat delivery fee; post-MVP PureHunger+ subscription at $6.99/mo |
| **Cost structure** | Courier payouts (base + mileage), payment processing fees, engineering/hosting, restaurant success & onboarding, customer acquisition / burn: ~$47K/month at launch |
| **Key metrics** | North Star: Weekly Active Ordering Households / Leading: restaurants onboarded per week, orders per restaurant per week, courier fill rate |
| **Unfair advantage** | Not yet established - commission rate alone is copyable. Emerging edge: direct owner-level restaurant relationships in Boise + first-mover density in a market incumbents don't optimize for |

---

## Expanded View

### Problem

| # | Problem | Severity (1-5) | Existing alternative |
|---|---|---|---|
| 1 | Independent restaurants pay 25-30% commission to major platforms, eroding thin (25-35%) food cost margins to the point of unprofitability on many orders | 5 | Stay off delivery platforms entirely, or absorb the margin loss (Daniel Osei's 18-month experience before dropping his platform) |
| 2 | Customers in mid-size cities (100k-500k) get thin selection and long delivery times because platforms are tuned for dense urban-core density and bury independent restaurants under paid-placement chains | 4 | Order from chains that pay for placement, or drive/pick up themselves |
| 3 | Couriers face opaque, frequently-changed payout algorithms and a weekly payout cycle, creating cash-flow unpredictability | 3 | Multi-app gig work across several delivery platforms; accept the terms as the cost of the work |

**Source:** Phase 2 personas + JTBD (Daniel Osei, Maya Torres, Priya Nair) and Phase 3a Hypothesis Register (HYP-001 through HYP-005) - 14 restaurant owner interviews, 11 courier interviews, 380-respondent customer survey.

---

### Customer Segments

**Primary segment:** Independent, single-location restaurant owners in mid-size US cities (100k-500k population) - this is the segment the business model differentiates on, and the one whose adoption determines whether a marketplace exists at all.

**Demand-side segment:** Busy professional customers in the same cities who order delivery multiple times per week and are underserved by incumbent apps' selection and discovery.

**Early adopters:**
- Who: Independent restaurants in Boise, ID - single-location, non-chain, 5+ years in business, currently off delivery platforms entirely or dissatisfied with incumbent economics (the Daniel Osei archetype)
- Why early adopter: Already feeling acute margin pain (higher than average pain intensity), motivated to switch quickly rather than wait for more proof
- Where to find them: Boise Independent Restaurant Association member list, Marcus Field's existing restaurant-industry network, referrals from the first onboarded cohort

---

### Unique Value Proposition

**UVP:** Keep more of every order you make. PureHunger charges independent restaurants 12% commission instead of the 25-30% national platforms charge, and passes the savings into faster courier payouts and restaurant discovery that isn't for sale.

**High-level concept:** The commission-fair delivery marketplace for independent restaurants.

**Promise:** A restaurant owner gets delivery-app reach without the margin damage; a customer gets real, findable independent restaurants instead of a chain-dominated feed; a courier gets paid the next day, not the next week.

---

### Solution

| Problem | Solution | MDP scope |
|---|---|---|
| Restaurants lose margin to commission | Flat 12% commission, published rate card, 30-day written notice on any rate change (Restaurant Partner Agreement) | Fixed 12% rate at launch; no negotiated or tiered rates; commission-change governance rule enforced contractually |
| Customers can't find good independent restaurants | Discovery ranked by proximity + rating + repeat-order rate; no sponsored placement; chains excluded from onboarding at launch | Browse/search + rating-weighted ranking algorithm; "Independent Spotlight" curated section on the home screen |
| Couriers face opaque, delayed payout | $4 base + $1.25/mile + 100% of tips, paid out daily with a transparent per-delivery earnings breakdown | Daily payout batch job; earnings breakdown shown before a courier accepts a delivery |

---

### Channels

| Channel | Stage | CAC estimate | Priority |
|---|---|---|---|
| Direct owner-to-owner outreach (restaurant side) | Acquisition + Activation | ~$180/restaurant (Marcus Field's time, no ad spend) | Primary |
| Geo-targeted digital ads (customer side, Boise zip codes) | Awareness + Acquisition | ~$1.66/signup ($850 spend / 512 signups, HYP-003) | Primary (demand side) |
| Restaurant-to-restaurant referral | Acquisition | Near-zero (12 of 34 pre-launch restaurants came via referral) | Secondary, expected to grow post-launch |
| Local community / Boise-specific press and social | Awareness | Unknown - not yet tested | Secondary |

---

### Revenue Streams

**Model:** Commission (marketplace take rate) + fixed delivery fee. Post-MVP: freemium-adjacent subscription upsell (PureHunger+).

| Tier | Price | Target customer | Revenue per year |
|---|---|---|---|
| Restaurant commission | 12% per order | All onboarded restaurants | Variable - scales with restaurant GMV; primary revenue line |
| Customer delivery fee | $2.99 flat per order | All customers | Supplementary - largely offsets courier base pay cost, not a margin driver |
| PureHunger+ (post-MVP) | $6.99/month, free delivery over $15 | High-frequency ordering households | Deferred - see PRD Out of Scope |

**Path to first revenue:** First commission revenue is generated on Day 1 of live ordering in Boise - the 34 pre-launch signed restaurants are the initial catalog.

---

### Cost Structure

| Cost driver | Type | Monthly estimate |
|---|---|---|
| Courier payouts (base + mileage) | Variable, scales with order volume | ~$22,000 at initial Boise volume |
| Payment processing fees (~2.9% + $0.30/transaction) | Variable | ~$3,200 at initial Boise volume |
| Engineering / hosting | Fixed | ~$9,500 |
| Restaurant success & onboarding (Marcus Field's team) | Fixed, step-function as headcount grows | ~$8,500 |
| Customer acquisition (ads) | Variable, controllable | ~$3,800 |

**Monthly burn at launch:** ~$47,000
**Runway needed to PMF signal:** 6 months to reach Q1/Q2 OKR targets (see `/pm-kpis`), against a $650K seed raise with an 18-month runway assumption

---

### Key Metrics

**North Star metric:** Weekly Active Ordering Households (WAOH) - a household that places at least one completed order in a rolling 7-day window. Measures repeated real value delivery across all three sides of the marketplace simultaneously.

| Leading indicator | Frequency | Target (Month 3) | Target (Month 6) |
|---|---|---|---|
| Restaurants onboarded (active) | Weekly | 60 | 120 |
| Orders per restaurant per week | Weekly | 12 | 18 |
| Courier fill rate (assigned within 8 min) | Daily | 85% | 90% |

---

### Unfair Advantage

Not yet established at launch - this is an honest gap, not an oversight. The 12% commission rate is a pricing decision, and pricing alone can be matched by a well-funded incumbent in a specific market if PureHunger proves the model works. What is beginning to accrue as a real advantage:

- Direct, owner-level relationships in Boise's independent restaurant community built through Marcus Field's outreach (22 LOIs converted with zero paid acquisition cost) - this is slower for an incumbent to replicate than a rate cut
- First-mover density in a market incumbents structurally don't optimize for (courier fill-rate and dispatch economics tuned for mid-size-city order volume) - matching this would require an incumbent to subsidize a market they currently deprioritize

Both of these need 6-12 months of operating data before they can be called a durable advantage rather than a head start.

---

## Canvas health check

| Block | Status | Risk |
|---|---|---|
| Problem | Validated | 14 restaurant interviews + 380-respondent customer survey; strong evidence base |
| Customer segments | Validated | Both restaurant and customer sides tested via HYP-002/HYP-003 with real engagement |
| UVP | Strong | Directly tied to the highest-severity validated pain (commission) |
| Solution | Validated (restaurant + customer sides); Partially validated (courier side) | Courier payout preference (HYP-004) rests on a borderline sample size |
| Channels | Tested | Direct outreach and targeted ads both cleared their thresholds |
| Revenue | Tested (commitment level) | 34 signed Restaurant Partner Agreements is a real signal, but zero live order volume yet |
| Unfair advantage | Aspirational | Explicitly flagged as not yet real - pricing is copyable |

**Overall:** The canvas is strong on problem-solution fit and channel viability; the biggest open bet is whether the emerging relationship/density advantage becomes durable before a well-capitalized incumbent responds to a proven 12%-commission model in a specific market.

---

## Open items

| Item | Block | Action needed |
|---|---|---|
| Unfair advantage is not yet real | Unfair Advantage | Track restaurant retention and courier fill-rate as the advantage-forming metrics through Month 6; revisit this block in the next Lean Canvas re-run |
| Courier payout preference sample size | Solution | Re-validate with live shift-acceptance and retention data in the first 60 days of dispatch operation |
| Commission sustainability at scale | Cost Structure | Confirm 12% holds gross margin targets once restaurant-success cost per restaurant is fully loaded past the first 60 restaurants |
