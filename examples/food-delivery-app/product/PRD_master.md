# Product Requirements Document - PureHunger

> **Phase:** 3b - Commercial Definition (Phase 3b exit artifact)
> **Date:** 2025-12-22
> **Version:** 1.0
> **Status:** Approved
> **Owner:** Sam Okonkwo (CEO/Product)
> **Audience:** Internal team (Sam Okonkwo, Lena Vogt, Marcus Field), seed investors

---

## Document Purpose

This PRD consolidates Phase 2 (Discovery), Phase 3a (Validation), and Phase 3b (Commercial Definition) outputs for PureHunger - a hyper-local food delivery marketplace connecting independent restaurants with customers in mid-size cities at a 12% commission instead of the 25-30% industry standard. It captures the validated product-market fit hypothesis and is the stable reference for Phase 4+ execution (domain modeling, feature decomposition, and build).

It is NOT a feature spec. Feature specifications are generated per Feature (JIT) in Phase 6 by `pm-feature-design` (Feature Card Sections 1-3).

---

## 1. Problem Statement

**The core problem:**
Independent restaurants in mid-size US cities (100k-500k population) cannot afford to be on major delivery platforms at 25-30% commission - a rate that turns an already-thin (25-35%) food cost margin into a break-even or loss-making transaction on many orders. As a result, they either stay off delivery apps entirely and lose the growing share of customers who default to app-based ordering, or they join and quietly absorb the margin loss until it becomes unsustainable. On the demand side, customers in these same cities are underserved: delivery apps are built and tuned for dense urban-core order density, so selection is thin, delivery times run long, and discovery algorithms bury independent restaurants under chains that pay for placement.

**Evidence basis:**
- 14 independent restaurant owner interviews conducted in Boise, Meridian, and Nampa (Phase 3a, HYP-001)
- 380-respondent customer survey plus 6,400 targeted-ad visitors and 512 signups from a Boise geo-fenced landing page test (Phase 3a, HYP-003)
- 11 courier interviews plus a 180-click courier waitlist smoke test (Phase 3a, HYP-004)
- 34 independent restaurants signed a Restaurant Partner Agreement before launch (Phase 3a, HYP-005)
- Problem urgency: High (restaurant side - existential margin impact), Medium-High (customer side - switching and frustration, not urgency)

**Why this problem is not solved well today:**
National platforms price commission uniformly across restaurant categories regardless of margin structure, and monetize discovery ranking through pay-for-placement, which structurally favors chains with marketing budgets over independent restaurants. Neither dynamic is solvable by an independent restaurant operating within the existing platform rules - the restaurant has no lever to negotiate rate or ranking individually.

---

## 2. Target Customer

PureHunger is a three-sided marketplace. All three sides are described here because the product depends on all three; there is no meaningful "primary persona" in the traditional single-sided-SaaS sense, though the restaurant segment carries the business model's core differentiation.

### Primary Segment - Customers (demand side)

**Segment:** Busy professionals in mid-size US cities who order delivery multiple times per week.
**Description:** Order-frequent, app-native, price-sensitive on delivery fees but willing to pay more for food they trust; currently served poorly by incumbent apps' thin independent-restaurant selection.
**Size (SAM):** Estimated 38,000 households in the Boise metro area matching the target ordering-frequency profile (see Market Context, Section 4).

**Primary Persona: Maya Torres (29)**
- Role: Marketing manager, orders delivery 3-4x/week on weeknights
- Core goal: Fast, reliable delivery from restaurants she trusts, with the ability to discover new local spots
- Top pain: Incumbent apps' discovery ranking surfaces the same chains everyone sees, burying independent restaurants she'd actually prefer
- What triggers her to seek a new solution: Repeated disappointment with selection quality and a desire to support local businesses when convenient to do so

### Restaurant Partner Segment (supply side - business model differentiator)

**Segment:** Independent, single-location restaurant owners in mid-size US cities.
**Persona: Daniel Osei (41)** - owns a single West African restaurant, 8 years in business, previously used a major delivery platform for 18 months before dropping it because 25-30% commission eroded an already low-margin cuisine's economics.
- Core goal: Delivery-channel revenue without losing money on every order
- Top pain: Commission rate is the same regardless of cuisine margin structure
- What triggers switching: A commission rate low enough that delivery math actually works for his cost structure, with contractual protection against future rate increases

### Courier Segment

**Segment:** Part-time couriers working delivery around a job or school schedule.
**Persona: Priya Nair (24)** - delivers part-time, cares about per-delivery payout transparency and flexible scheduling, frustrated by incumbent platforms' opaque, frequently-changed payout algorithms.
- Core goal: Predictable, transparent pay and flexible shifts
- Top pain: Weekly payout cycles create cash-flow unpredictability; payout algorithm changes feel arbitrary

### Early Adopter Profile

The first 34 restaurants (signed pre-launch via direct outreach and referral, Phase 3a HYP-005) are single-location, non-chain, 5+ years in business, and were either off delivery platforms entirely or actively dissatisfied with incumbent commission economics - a higher-pain-intensity subset of the broader restaurant segment, motivated to switch quickly rather than wait for further proof. On the customer side, the first cohort is expected to come from Boise's core neighborhoods, digitally active, and responsive to a "real independent restaurants, not chain markup" positioning (validated at 8.0% landing-page conversion, HYP-003).

### Secondary Segment

None at MVP. PureHunger launches single-city (Boise, ID) by design; a second segment (e.g., office/enterprise catering) is explicitly out of scope (Section 7).

---

## 3. Product Vision and Value Proposition

**Vision (3 years):**
PureHunger is the default delivery platform in 25+ mid-size US cities where independent restaurants keep their margins, customers trust that what they see reflects real quality rather than who paid for placement, and couriers choose PureHunger shifts because the pay is transparent and immediate.

**Value proposition:**
Keep more of every order you make. PureHunger charges independent restaurants 12% commission instead of the 25-30% national platforms charge, and passes the savings into faster courier payouts and restaurant discovery that isn't for sale.

**For Maya Torres (customer):**
- Primary outcome: Fast delivery from restaurants she actually wants, discoverable without wading through chain-dominated search results
- Pain eliminated: Pay-to-play discovery ranking that hides independent restaurants
- Differentiation: Merit-based ranking (proximity, rating, repeat-order rate), no sponsored placement

**For Daniel Osei (restaurant partner):**
- Primary outcome: Delivery-channel revenue that doesn't erase his margin
- Pain eliminated: Commission rate uniform across cuisine types regardless of actual margin structure
- Differentiation: Flat 12% published rate, 30 days' written notice before any rate change (Restaurant Partner Agreement)

**For Priya Nair (courier):**
- Primary outcome: Predictable, fast access to earnings
- Pain eliminated: Opaque, frequently-changed payout algorithms and slow payout cycles
- Differentiation: Daily payout, transparent per-delivery earnings breakdown before accepting a delivery

---

## 4. Market Context

**Market opportunity:**

| Metric | Value | Confidence |
|---|---|---|
| TAM | $95B (US food delivery market) | High (industry-standard figure) |
| SAM | $8.2B (independent-restaurant delivery GMV across US mid-size cities, 100k-500k population) | Medium (derived estimate, not primary research) |
| SOM (Year 3) | $28M GMV across ~8 mid-size cities | Low - assumption-based, contingent on Boise proving the model |
| Market CAGR | ~7% | Industry benchmark for food delivery category growth |

**Why now:**
Post-pandemic app-based ordering behavior is now the default even outside dense urban cores, closing the demand-side gap that used to make mid-size-city delivery uneconomical. At the same time, commission fatigue among independent restaurants is well documented - multiple restaurants in the Boise interview sample had already dropped a major platform specifically over commission economics, meaning the supply-side pain is not hypothetical but actively driving churn away from incumbents. Gig-worker expectations around payout speed and transparency have also risen, making daily payout a real acquisition lever rather than a marginal feature.

**Competitive position:**
Incumbent national platforms (Uber Eats/DoorDash-style) concentrate marketing and dispatch density in the top 50 US metros; mid-size cities receive a scaled-down version of the same product with the same 25-30% commission structure. PureHunger wins on restaurant economics (12% vs. 25-30%) and on discovery fairness (merit-ranked, no pay-for-placement). Regional/local delivery co-ops exist in some mid-size markets but generally lack dispatch technology sophistication and cannot match live tracking or reliable fill rates.

**Competitive whitespace:**
Mid-size cities as a category - national platforms structurally deprioritize dispatch density and marketing spend below the top-50-metro tier, leaving an opening for a platform purpose-built for this order density rather than importing an urban-core model.

---

## 5. Business Model

**Revenue model:** Marketplace commission (primary) + fixed delivery fee (supplementary, largely offsets courier base pay). Freemium-adjacent subscription upsell deferred to Post-MVP.

**Pricing:**

| Tier | Price | For whom |
|---|---|---|
| Restaurant commission | 12% per order | All onboarded restaurants (vs. 25-30% industry standard) |
| Customer delivery fee | $2.99 flat + optional tip | All customers |
| PureHunger+ (Post-MVP) | $6.99/month, free delivery over $15 | High-frequency ordering households |

Courier pay: $4 base + $1.25/mile + 100% of tips, paid out daily (vs. incumbents' weekly payout cycle - a deliberate differentiator, see Section 3).

**Unit economics targets:**

| Metric | Target |
|---|---|
| ARPU (per ordering household/month) | $9.40 (Month 6) rising to $10.80 (Month 12) |
| Monthly household churn | < 15% |
| Contribution margin per order | > $1.10 (Month 6) rising to > $1.35 (Month 12) |
| Restaurant churn (Paused/Deactivated) | < 10% per quarter |

**Acquisition model:** Direct owner-to-owner outreach for restaurants (primary, near-zero paid cost - validated at 78% meeting-rate and 22 signed LOIs from 40 contacted restaurants); geo-targeted digital ads for customers (primary demand-side channel, validated at 8.0% visitor-to-signup conversion).

---

## 6. Success Metrics

**North Star Metric:** Weekly Active Ordering Households (WAOH) - a household that places at least one Order reaching Delivered status in a rolling 7-day window.
**NSM Target (Month 12):** 4,000 WAOH

**Phase 1 exit criteria (Month 3 post-launch, Boise):**
- [ ] 900 Weekly Active Ordering Households
- [ ] 60 active restaurants onboarded
- [ ] Courier fill rate (Assigned within 8 minutes) ≥ 85%

**Phase 2 targets (Month 4-6):**
- [ ] 1,500 Weekly Active Ordering Households
- [ ] 120 active restaurants onboarded
- [ ] Day-21 household reorder rate ≥ 35%

**AARRR summary:**

| Stage | Key Metric | Target |
|---|---|---|
| Acquisition | Blended customer CAC | < $12 (Month 3) |
| Activation | Activation rate (1st order within 7 days) | 38% |
| Retention | Day-21 reorder rate | 35% |
| Revenue | Commission revenue (Month 6) | $37K/month |
| Referral | NPS (first cohort) | > 40 |

Full detail: `artifacts/phase-3b-definition/kpis.md`.

---

## 7. Product Scope

### Business Capabilities (FDD+SDD input)

What PureHunger must enable, written as business capabilities. This section is the primary input for entity extraction (Phase 4, `pm-entity-registry`) and feature decomposition (Phase 5, `pm-features-list`). Each capability names an actor and implies at least one entity from the domain model (Order, Restaurant, MenuItem, Courier, Delivery, Payment, CourierPayout).

**Domain: Ordering & Checkout (FEAT-ORD-*)**
- The system must enable customers to browse active restaurants and build a cart from available menu items.
- The system must enable customers to complete checkout, authorizing payment before the order is confirmed by the restaurant.
- The system must enable customers to cancel an order while it remains in the Placed state, before restaurant acceptance.
- The system must enable customers to track order status in real time from placement through delivery.
- The system must enable customers to rate a completed order (food quality and delivery experience) after it reaches Delivered status.
- The system must enforce that an order cannot be placed against a restaurant that is not in Active state, and that a menu item must be marked available to be added to a cart.

**Domain: Restaurant Onboarding & Menu Management (FEAT-REST-*)**
- The system must enable a restaurant owner to apply for a Restaurant Partner account and progress through review to Active status.
- The system must enable an Active restaurant to create, update, and toggle availability of menu items.
- The system must enable a restaurant to pause order intake (Paused state) without losing its account, and to be deactivated when the partnership ends.
- The system must enable restaurant staff to accept or (within the 10-minute window) implicitly decline an incoming order, triggering the appropriate payment and refund logic.
- The system must enforce the Restaurant Partner Agreement's 30-day written-notice requirement before any commission rate change takes effect.

**Domain: Delivery Dispatch & Tracking (FEAT-DEL-*)**
- The system must enable the dispatch system to assign an available, Active, Online courier to a Delivery once an order reaches ReadyForPickup.
- The system must enable a courier to view a transparent per-delivery earnings breakdown before accepting a delivery.
- The system must enable customers and restaurant staff to see live delivery status and courier location from assignment through completion.
- The system must enforce that a Delivery cannot move to PickedUp until the associated Order is in ReadyForPickup state.
- The system must automatically suspend a courier whose rolling average rating over their last 20 deliveries falls below 4.5 stars, pending manual review.

**Domain: Payments & Payouts (FEAT-PAY-*)**
- The system must enable payment authorization at order placement, capturing payment in full only when the restaurant accepts the order.
- The system must enable automatic, full refund of an order if the restaurant does not accept it within 10 minutes of placement.
- The system must enable a daily batch payout to couriers based on completed deliveries, including base pay, mileage, and 100% of tips.
- The system must enable issuance of 1099-NEC tax documents to any courier paid over $600 in the prior calendar year, by January 31.
- The system must enforce that customer card details are never stored directly - only a tokenized reference from the payment processor is retained.

> Referenced by Feature Cards via `prd_ref: "/product/PRD_master.md#business-capabilities-fdd-sdd-input"` with domain-level anchors once split into per-domain sections in Phase 4-5 if the feature volume warrants a modular PRD.

### In Scope (MVP)

The MVP is the ordering loop end to end: browse restaurant → build cart → checkout/pay → restaurant accepts → courier delivers → customer rates.

1. Ordering & Checkout - full capability set (browse, cart, checkout, live tracking, post-delivery rating)
2. Restaurant Onboarding & Menu Management - full capability set (application through Active/Paused/Deactivated lifecycle, menu CRUD)
3. Delivery Dispatch & Tracking - full capability set (assignment, live tracking, courier rating-based suspension)
4. Payments & Payouts - full capability set (authorization/capture/refund logic, daily courier payout, tax document issuance)

> Feature-level detail defined in Phase 5 (`pm-features-list`) and Phase 6 JIT design (`pm-feature-design`).

### Out of Scope (MVP)

| Item | Reason | Reconsider when |
|---|---|---|
| PureHunger+ subscription tier | Retention and reorder behavior not yet proven at MVP; a subscription commitment is premature before the underlying ordering-loop economics are validated with live data | After Phase 1 exit criteria are met (900 WAOH, Month 3) and Day-21 reorder rate trend is stable |
| Group ordering | No validated demand signal for this in the Phase 3a hypothesis set; adds meaningful checkout complexity for an unvalidated use case | If office/enterprise catering demand emerges post-launch (customer support tickets, restaurant requests) |
| Scheduled / future orders | Adds dispatch and inventory-availability complexity; MVP focuses on proving the real-time ordering loop first | After real-time dispatch reliability (courier fill rate ≥ 90%) is demonstrated |
| Loyalty / rewards program | Retention mechanics not yet understood well enough to design a rewards structure that reinforces the right behavior rather than subsidizing it | After Day-21 reorder rate plateaus and a specific retention gap is identified |
| Paid/sponsored restaurant placement | Directly undermines the Local-First Discovery positioning that is core to the customer-side value proposition (see Design Thinking synthesis) | Not planned - would require a strategic repositioning, not a phase trigger |
| Multi-city launch | Single-city (Boise) launch discipline lets the team validate dispatch density and unit economics before replicating the model | After Phase 2 targets are met and Boise-metro densification (Meridian) is live |

### Deferred (Post-MVP)

| Item | Target phase | Trigger |
|---|---|---|
| PureHunger+ subscription | Phase 2 of product | Day-21 reorder rate stable at target and restaurant density supports the "free delivery over $15" cost structure |
| Scheduled / future orders | Phase 2 of product | Real-time dispatch fill rate consistently ≥ 90% |
| Group ordering | Phase 3 of product | Validated enterprise/office demand signal |
| Loyalty rewards | Phase 2-3 of product | Identified retention gap post Day-21 reorder plateau |

---

## 8. Constraints and Risks

### Technical Constraints

| Constraint | Impact | Source |
|---|---|---|
| Real-time dispatch and live-tracking latency requirements at lower order density than incumbents optimize for | Dispatch algorithm must be purpose-built for mid-size-city density (Density-Appropriate Dispatch direction), not adapted from a dense-urban-core model | Design Thinking Synthesis, Ideate stage |
| Dependency on a third-party payment processor for tokenized card storage and courier payout batching | Processor rate limits and payout batch timing directly affect the daily-payout differentiator | Business Model, Section 5 |

**Technical feasibility verdict:** 🟢 Feasible - the ordering loop, dispatch, and payment flows are well-understood patterns; the primary technical risk is dispatch performance tuning for mid-size-city density, which is an operational tuning problem, not a feasibility blocker.

### Regulatory Constraints

| Regulation | Jurisdiction | Requirement | Timeline |
|---|---|---|---|
| PCI-DSS (via tokenized processor) | US | Customer card details must never be stored directly - only the processor's tokenized reference | Before launch |
| Courier tax documentation | US federal | 1099-NEC issued for any courier paid over $600 in the prior calendar year | By January 31 annually |
| Commission rate change notice | Contractual (Restaurant Partner Agreement) | 30 days' written notice required before any commission rate change | Ongoing governance rule |
| Local food-delivery licensing/insurance | Idaho / Boise | Standard delivery-service licensing and courier insurance requirements | Before launch |

**Regulatory showstoppers:** None identified.

**Compliance requirements to address before launch:**
- [ ] Payment processor integration confirmed to never expose raw card data to PureHunger's own systems (tokenization only)
- [ ] Courier onboarding flow captures tax documentation (W-9 equivalent) needed for future 1099-NEC issuance
- [ ] Restaurant Partner Agreement legal review includes the 30-day commission-notice clause

### Business Constraints

| Constraint | Impact |
|---|---|
| 3-person founding team (Sam Okonkwo, Lena Vogt, Marcus Field) | Sequencing discipline required - cannot build and operate everything in parallel; restaurant onboarding, dispatch tuning, and product build compete for the same limited attention |
| $650K seed raise, 18-month runway assumption | Monthly burn (~$47K at launch, see Lean Canvas) must reach Phase 1/2 exit criteria well within the runway window to support a follow-on raise |
| Single-city (Boise) launch discipline | Multi-city expansion is explicitly deferred until Boise proves unit economics and dispatch density assumptions |

---

## 9. Open Questions and Assumptions

### Open Questions (not yet resolved)

| Question | Priority | Owner | Target date |
|---|---|---|---|
| What courier fill-rate is achievable at Boise's actual order density without subsidizing idle courier time? | High | Lena Vogt | End of Month 1 post-launch (live dispatch data) |
| Will restaurants accept the 12% commission model long-term, or will a well-funded incumbent price-match in Boise specifically to blunt the wedge? | High | Sam Okonkwo | Ongoing - monitor restaurant churn rate quarterly |
| Does customer order volume per restaurant reach the ~15 orders/week threshold identified in the Design Thinking falsification condition, or does the commission wedge attract restaurants without generating enough demand to matter? | High | Sam Okonkwo | End of Month 3 post-launch |

### Critical Assumptions (that could invalidate the product)

| Assumption | Confidence | How to validate | By when |
|---|---|---|---|
| Courier supply is sufficient at Boise's launch order density without excessive idle-time subsidy | Medium | Track courier fill rate and idle-time cost against the courier waitlist conversion signal (26%, HYP-004) | Month 1 post-launch |
| Restaurants that sign the Restaurant Partner Agreement will not churn back to incumbent platforms once acquired | Medium | Track restaurant churn (Paused/Deactivated) against the < 10%/quarter Q1 OKR target | Ongoing, quarterly |
| 12% commission is sustainable at target gross margin once payment processing and restaurant-success costs are fully loaded | Medium-High | Recompute contribution margin per order against actuals once past the first 60 restaurants | Month 6 post-launch |
| Courier payout preference (daily vs. weekly) generalizes beyond the 11-interview sample validated in Phase 3a | Medium | Monitor courier shift-acceptance rate and retention post-launch (flagged caveat in Hypothesis Register) | First 60 days of live dispatch |

---

## 10. Product Roadmap (summary)

> Full roadmap maintained separately as the living Product Roadmap artifact (updated at each phase gate per the framework's roadmap versioning convention).

**Phase 1 - Boise Launch:** Months 0-3 - Prove the ordering loop end-to-end with 60 active restaurants and 900 Weekly Active Ordering Households.
**Phase 2 - Boise-Metro Densification:** Months 4-6 - Reach 120 active restaurants, launch a second Boise-metro submarket (Meridian), and begin PureHunger+ subscription design once reorder rate is stable.
**Phase 3 - Multi-City Expansion:** Months 7-12+ - Replicate the validated Boise model into 1-2 additional mid-size cities using the same dispatch-density and restaurant-acquisition playbook.

---

## 11. Artifact Input Map

This PRD synthesizes the following Phase 2, Phase 3a, and Phase 3b artifacts:

| Artifact | Phase | Status | Key contribution to PRD |
|---|---|---|---|
| personas.md | 2 | ✅ | Maya Torres, Daniel Osei, Priya Nair - target customer definitions across all 3 marketplace sides |
| market-analysis.md | 2 | ✅ | TAM/SAM/SOM, competitive position, market timing rationale |
| jtbd-analysis.md | 2 | ✅ | Switching triggers and forces behind restaurant platform abandonment and customer discovery frustration |
| design-thinking.md | 3a | ✅ | Problem Statement, dual POV (restaurant + customer), HMW questions, recommended direction (Fair Take + Local-First Discovery) |
| hypotheses-go-no-go.md | 3a | ✅ | 5 hypotheses tested, Go/No-Go verdict = GO, restaurant commitment and demand-side evidence |
| lean-canvas.md | 3b | ✅ | Revenue model, cost structure, channels, unfair-advantage honesty check |
| kpis.md | 3b | ✅ | North Star Metric (WAOH), AARRR framework, Q1/Q2 OKRs |

**Gaps noted:** None material. All required Phase 2/3a/3b inputs were available at PRD synthesis time. The unfair-advantage block (Lean Canvas) is explicitly flagged as aspirational rather than established - this is carried forward as an open risk (Section 9) rather than treated as a gap in the input set.

---

## 12. Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2025-12-22 | Sam Okonkwo | Initial - end of Phase 3b, Go/No-Go = GO |
