# North Star Metric - PureHunger

> **Phase:** 3 - Define & Validation
> **Date:** 2025-12-18

---

## North Star Metric

**NSM:** Weekly Active Ordering Households (WAOH)

**Definition:** A household - identified by a unique payment method + delivery address cluster - that places at least one Order that reaches Delivered status within a rolling 7-day window. Cart abandonment, Cancelled orders, and Refunded orders do not count toward WAOH.

**Why this metric:**
WAOH is the one metric that captures value delivered simultaneously across all three sides of the marketplace: it can only grow if restaurants have inventory customers want (supply side), if the ordering experience is good enough to repeat (product), and if couriers deliver reliably enough that "Delivered" is the common outcome (dispatch side). A metric like total orders or signups would reward volume without repeat behavior; WAOH rewards households coming back, which is the actual signal that PureHunger is solving the two-sided problem it was built for.

**What it is NOT:**
Total orders placed is the common trap metric here - it looks similar to WAOH in early charts but conflates one household ordering 10 times with 10 households ordering once. The former is a retention risk hiding inside a growth number; the latter is real market reach. WAOH forces the distinction by counting unique households, not raw order volume.

**Gaming risk (Goodhart's Law):** WAOH could be inflated by promo-driven orders that don't reflect real repeat intent (e.g., aggressive discount codes driving one-off orders from otherwise inactive households), or by counting orders that are placed but later refunded or never fulfilled. Counter-metric/guardrail: pair WAOH with **Order Completion Rate** (% of Placed orders that reach Delivered, not Cancelled/Refunded). If WAOH rises while Order Completion Rate falls, the growth is being manufactured rather than earned - restaurants may be accepting orders they can't fulfill, or promo activity is driving low-intent orders.

---

## NSM Decomposition

| Input Metric | Lever Type | Who owns it | How it moves the NSM |
|---|---|---|---|
| New Household Activation Rate (completed first order within 7 days of signup) | Activation | Product | Every activated household is a candidate for future active weeks |
| Household Reorder Rate (2nd order within 21 days of first) | Retention | Product | Directly determines whether a household becomes a repeat WAOH contributor or a one-time order |
| Restaurant Selection Density (active restaurants per zip code) | Supply | Restaurant Success (Marcus Field) | More relevant selection per neighborhood drives both activation and reorder rate |

---

## NSM Targets

| Period | Target | Basis |
|---|---|---|
| End of Month 3 post-launch | 900 WAOH | 60 active restaurants × ~12 orders/week ÷ ~0.8 orders per household per active week (Lean Canvas leading indicator targets) |
| End of Month 6 | 1,500 WAOH | 120 active restaurants at target density, Day-21 reorder rate reaching 35% |
| End of Month 12 | 4,000 WAOH | Boise-metro densification (second submarket) plus organic/referral acquisition share reaching 25% of new households |

---

# AARRR Metrics - PureHunger

> **Phase:** 3 - Define & Validation
> **Date:** 2025-12-18

---

## Funnel Overview

```
[Acquisition] → [Activation] → [Retention] → [Revenue] → [Referral]
[Signups]     → [1st order]  → [2nd order] → [Take rate + fee] → [Referred household]
```

---

## Acquisition

**Goal:** Bring the right households (in Boise, at launch) to the product.

| Metric | Definition | Target (Month 3) | Target (Month 6) | Channel |
|---|---|---|---|---|
| Monthly app downloads / signups | New customer accounts created | 3,200 | 6,000 | Geo-targeted ads + organic |
| Restaurant-side signups (active) | New Restaurant records reaching Active state | 60 | 120 | Direct outreach + referral |
| Blended customer CAC | Total acquisition spend / new signup | < $12 | < $10 | Blended (ads primary) |

**Primary acquisition channel:** Geo-targeted digital ads in Boise zip codes (validated in HYP-003: 8.0% visitor-to-signup conversion against an $850 test budget).

**Conversion: Visitor → Signup:** 8.0% (basis: HYP-003 experiment result, well above the 5% validation threshold).

---

## Activation

**Goal:** Get new households to their first completed order as fast as possible.

**Activation definition:** Household completes its first Order (reaches Delivered state) within 7 days of account signup.

| Metric | Definition | Target |
|---|---|---|
| Activation rate | % of signups who complete activation event within 7 days | 38% |
| Time to activation | Median days from signup to first Delivered order | < 3 days |
| Checkout completion rate | % of started carts that reach Placed | 72% |

**Activation bottleneck hypothesis:** The most likely drop-off point is browse-to-cart, given the smaller initial restaurant catalog (independent-only, single city) compared to incumbent apps. Mitigation: the "Independent Spotlight" curated home-screen section (from the Lean Canvas Solution block) surfaces a small, high-quality set of options rather than requiring exhaustive browsing.

---

## Retention

**Goal:** Keep households ordering again. This is the direct input to the North Star Metric.

**Retention definition:** A household is "active" in a given week if it places at least one Order reaching Delivered status in that 7-day window (identical definition to WAOH, applied at the individual-household level).

| Metric | Definition | Target | Industry Benchmark |
|---|---|---|---|
| 2nd order within 21 days | % of activated households placing a 2nd Delivered order within 21 days | 35% | Food delivery apps typically see 25-40% depending on market density |
| Day 30 retention | % of activated households still active (1+ order) in the week containing Day 30 | 28% | |
| Monthly household churn | % of previously active households with zero orders in the trailing 30 days | < 15% | |
| Order Completion Rate (NSM guardrail) | % of Placed orders reaching Delivered (not Cancelled/Refunded) | > 96% | |

**Retention curve shape:** Expect a first-order novelty effect (many households try PureHunger once because it's new) followed by a drop-off around week 2-3, then stabilization among households who find 2-3 go-to restaurants in the catalog - this is why the 21-day reorder window, not a 7-day one, is the primary retention gate.

---

## Revenue

**Goal:** Convert delivered orders into sustainable commission and fee revenue.

| Metric | Definition | Target (Month 6) | Target (Month 12) |
|---|---|---|---|
| GMV (Gross Merchandise Value) | Total value of Delivered orders | $310K/month | $890K/month |
| Commission revenue | 12% of GMV | $37K/month | $107K/month |
| ARPU (per ordering household/month) | Commission + fee revenue attributable ÷ active households | $9.40 | $10.80 |
| Contribution margin per order | (Commission + delivery fee) - courier payout - processing fee | > $1.10/order | > $1.35/order |

---

## Referral

**Goal:** Turn satisfied households into an acquisition channel that reduces blended CAC over time.

| Metric | Definition | Target |
|---|---|---|
| NPS (customer) | Net Promoter Score, post-delivery survey | > 40 (first-cohort baseline) |
| Referral share of new households | % of new signups attributing to a referral code or "friend told me" | 25% by Month 12 |
| Restaurant referral rate | % of onboarded restaurants that refer another restaurant | 35% (validated directionally: 12 of 34 pre-launch restaurants came via referral) |

**Referral mechanism:** No formal in-app referral/incentive program at MVP (deliberately deferred - see PRD Out of Scope). Early signal (restaurant-side referral in the pre-launch cohort) is organic; a structured referral incentive is a Post-MVP candidate once retention is proven.

---

## Metric Ownership

| Metric area | Owner | Review cadence |
|---|---|---|
| Acquisition | Marcus Field (Growth & Restaurant Partnerships) | Weekly |
| Activation | Lena Vogt (Product/CTO) | Weekly |
| Retention | Lena Vogt (Product/CTO) | Weekly |
| Revenue | Sam Okonkwo (CEO/Product) | Weekly |
| NPS / Referral | Marcus Field | Monthly |

---

# OKRs - PureHunger

> **Phase:** 3 - Define & Validation
> **Date:** 2025-12-18
> **Period:** Q1 post-launch - Boise, ID market

---

## OKR Design Principles

- Objectives: qualitative, inspiring, directional
- Key Results: quantitative, measurable, binary (hit or miss)
- Target: ambitious but achievable - 70% completion = success (not 100%)
- Max 3 OKRs per quarter, max 3-4 KRs per Objective

---

## Q1 OKRs (Post-Launch, Boise)

### O1: Prove the ordering-loop product-market fit in Boise

| Key Result | Target | Current | Status |
|---|---|---|---|
| KR1: Reach Weekly Active Ordering Households (WAOH) | 900 | 0 | Not started |
| KR2: Day-21 household reorder rate | ≥ 35% | - | Not started |
| KR3: NPS with first customer cohort | ≥ 40 | - | Not started |

### O2: Prove restaurant-side unit economics hold at 12% commission

| Key Result | Target | Current | Status |
|---|---|---|---|
| KR1: Active restaurants onboarded | 60 | 34 (pre-launch signed) | In progress |
| KR2: Average restaurant GMV per week | ≥ $1,800 | - | Not started |
| KR3: Restaurant churn (Paused/Deactivated) | < 10% per quarter | - | Not started |

### O3: Validate courier supply reliability at Boise's order density

| Key Result | Target | Current | Status |
|---|---|---|---|
| KR1: Courier fill rate (Assigned within 8 minutes) | ≥ 90% | - | Not started |
| KR2: Average courier delivery-acceptance rate | ≥ 80% | - | Not started |
| KR3: Daily payout cycles processed with zero missed runs | 100% | - | Not started |

---

## Q2 OKRs (Growth Phase)

### O1: Grow WAOH and prove repeatable acquisition

| Key Result | Target | Basis |
|---|---|---|
| KR1: Weekly Active Ordering Households | 1,500 | NSM Month 6 target |
| KR2: Blended CAC per ordering household | < $18 | Acquisition funnel + referral share assumptions |
| KR3: Organic/referral share of new households | ≥ 25% | Restaurant referral trend from Q1 pre-launch cohort |

### O2: Expand restaurant density and prove a second submarket

| Key Result | Target | Basis |
|---|---|---|
| KR1: Active restaurants onboarded | 120 | NSM Month 6 restaurant density target |
| KR2: Launch coverage in a second Boise-metro submarket (Meridian) | Live by end of Q2 | Product Roadmap Phase 1→2 transition |
| KR3: Restaurant NPS | ≥ 45 | Restaurant-success relationship quality signal |

---

## What We Are NOT Measuring (Yet)

- Enterprise / office catering accounts - not the segment for Q1-Q2, no group ordering capability at MVP
- PureHunger+ subscription engagement - subscription tier is explicitly Post-MVP (see PRD Out of Scope)
- Multi-city aggregate metrics - all Q1-Q2 targets are Boise-only by design; a second city is a Phase 2+ roadmap decision, not a Q1-Q2 metric
- International or cross-border metrics - not applicable at this stage
