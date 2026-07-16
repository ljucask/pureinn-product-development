# Market Analysis - PureHunger

> **Phase:** 2 - Discovery (Track C: Market Discovery)
> **Date:** 2026-07-14
> **Geography:** United States, mid-size cities (100K-500K population), anchor launch market Boise, Idaho
> **Data basis:** Founder domain knowledge (Sam Okonkwo's regional grocery-delivery ops background) + publicly known industry structure (major platform commission ranges, mid-size-city underinvestment pattern) + bottom-up modeling built for this document. Figures are illustrative estimates built to a stated methodology, not sourced from a live market-research vendor - `[ASSUMED]` unless otherwise noted. Verify against primary sources (Census, IBISWorld, platform 10-Ks) before using in investor materials.

---

## Market Size Analysis

### Market Definition

**Product category:** Hyper-local restaurant food delivery marketplace, positioned against national platforms on commission structure and independent-restaurant discovery rather than on breadth of catalog.

**Primary customer:** Two-sided - independent (non-chain) restaurants in mid-size US cities on the supply side; time-starved urban professionals who order delivery 2-4x/week on the demand side. This document sizes the demand-side GMV opportunity (the number restaurants and customers jointly transact through), since that is the figure investors and the team track as the addressable market; commission economics are modeled separately in `pm-business-model`.

---

### TAM / SAM / SOM

| Level | Definition | Size | Source / Method |
|---|---|---|---|
| **TAM** (Total Addressable Market) | All US mid-size cities (100K-500K population, ~300 cities nationally) - total food-delivery GMV addressable in this city-size band | ~$13.0B GMV/year | Bottom-up: see Calculation Methodology below `[ASSUMED - bottom-up estimate]` |
| **SAM** (Serviceable Addressable Market) | Subset of ~15 mid-size, non-coastal, secondary-metro cities matching Boise's profile (independent-restaurant density, non-saturated delivery infrastructure, operationally reachable for a small team) | ~$636M GMV/year | Bottom-up from target-city cohort population `[ASSUMED]` |
| **SOM** (Serviceable Obtainable Market) | Boise MSA + 2 similarly-sized expansion markets, realistic 3-year capture given restaurant-first ground-game acquisition capacity | ~$30.6M GMV/year by Year 3 (~$4.3M/year PureHunger revenue at blended ~14% effective take) | Derived from acquisition-channel throughput, not "X% of SAM" - see below |

### Key Assumptions

| Assumption | Value | Confidence |
|---|---|---|
| Number of US cities, 100K-500K population | ~300 cities | Med (Census-derivable, not independently verified here) |
| Average population per mid-size city | ~220K-230K | Med |
| Delivery-app penetration in mid-size cities | ~32% of population (below the ~40% dense-urban-core national average - the underinvestment gap this product targets) | Low-Med - directional, not measured |
| Average annual delivery GMV per active user | ~$600/year (~$30/order x ~20 orders/year) | Low-Med |
| Boise MSA population (Ada + Canyon counties) | ~830,000 | Med (public estimate, not re-verified for this document) |
| Boise-proper population (falls within the 100K-500K "mid-size city" band) | ~235,000 | Med |
| Independent (non-chain) restaurant count, Boise MSA | ~410 | Low - `[ASSUMED - Idaho food-service establishment counts, chain-filtered estimate]` |

### Calculation Methodology

**Bottom-up, not top-down.** TAM = (aggregate population across ~300 US mid-size cities, ~68M) x (delivery-app penetration, ~32%) x (average annual delivery GMV per active user, ~$600) ≈ $13.0B GMV/year. SAM narrows this to the ~15-city cohort operationally similar to Boise (secondary Mountain West/interior metros with weak incumbent density and strong independent-restaurant culture) using the same per-capita method. SOM does **not** apply a flat percentage to SAM - it is derived from realistic acquisition-channel throughput: Marcus Field's restaurant-first ground game can onboard an estimated 15-20 qualified restaurants/month in a new city (in-person visits, margin-math conversations, peer referral cycles - see `personas.md` and `jtbd-analysis.md`), which caps how much of the market can plausibly be captured regardless of marketing spend on the customer side. This produces a SOM close to 5% of SAM, but the number is a channel-capacity output, not an assumed percentage - if restaurant onboarding capacity doubled, SOM would rise; it is not simply "5% because that felt reasonable."

---

### Market Growth

**CAGR (national online food delivery, industry-wide):** ~8%/year `[ASSUMED - directionally consistent with widely reported industry growth rates, not independently verified for this document]`
**Growth drivers:**
- Continued generational shift toward app-based ordering as a default behavior, not an occasional convenience
- Post-2020 normalization of delivery as routine (not emergency) behavior, still diffusing into mid-size and secondary metros slower than it saturated dense urban cores
- Independent restaurants increasingly recognizing that opting out of delivery apps entirely means losing an entire customer segment, not just a channel

**Key market trends:**
- National platforms have historically under-invested courier density and account-management attention in mid-size and secondary metros relative to top-20 dense urban markets - this is the structural gap PureHunger is built to exploit, not a hypothetical one
- Independent restaurant owners are increasingly vocal (in industry press and owner networks) about commission economics not working on lower-margin cuisines - a real and growing willingness to consider a lower-commission alternative

---

### Revenue Potential

| Scenario | Year 1 | Year 3 | Assumptions |
|---|---|---|---|
| Conservative | $180K | $2.1M | Boise only, 25 active restaurants by Year 1 / 55 by Year 3, slower customer-side adoption |
| Base | $340K | $4.3M | Boise + 1 expansion city by Year 3, 40 restaurants by Year 1 / 90+ combined by Year 3, matches SOM figure above |
| Optimistic | $520K | $7.0M | Boise + 2 expansion cities by Year 3 ahead of plan, stronger-than-modeled restaurant referral cycle |

All figures are PureHunger net revenue (12% restaurant commission + $2.99 customer delivery fee, net of courier payout pass-through), not GMV. `[ASSUMED - model built for this document, not independently verified]`

---

## Competitor Analysis

### Competitive Landscape Map

**Category:** Restaurant food delivery marketplace

| Competitor | Type | Geography | Core Value Prop | Target Segment | Est. Size / Stage |
|---|---|---|---|---|---|
| DoorDash | Direct | National, including Boise | Largest catalog and courier density; DashPass subscription bundling | Mainstream urban/suburban consumers, all restaurant types | Public, market leader, dominant national GMV share |
| Uber Eats | Direct | National, including Boise | Cross-sell with Uber rides app; broad catalog, aggressive promo-driven acquisition | Mainstream consumers already in the Uber ecosystem | Public, #2 national player |
| Grubhub | Direct (weaker in this geography) | National, but visibly reduced investment in secondary metros including Boise | Long-tail restaurant catalog, legacy brand recognition | Price- and habit-driven consumers in markets where it retains presence | Public (owned by Wonder as of recent restructuring), pulling back in many mid-size markets |
| TableHop *(fictional, illustrative)* | Direct, small local-first competitor | 2-3 Mountain West secondary cities (not yet Boise) | Lower commission (~15%) pitch to independents, community-first branding | Independent restaurants specifically, similar thesis to PureHunger | Bootstrapped/seed-stage, thin courier supply, unreliable live tracking |
| Self-delivery / phone-order status quo | Substitute (do-nothing alternative) | Everywhere, including Boise | No commission at all; direct customer relationship | Restaurants (like Daniel, pre-PureHunger) who opted out of platforms entirely | Not a company - the actual current state for a meaningful share of independent restaurants |

**Why the status quo row matters:** A meaningful share of Boise's independent restaurants (including Daniel Osei's, before PureHunger) have already tried a major platform and quit. "No delivery app at all" is not a null option - it is the alternative currently winning against every commercial platform for this segment, and it is the one PureHunger has to beat, not just DoorDash and Uber Eats.

---

### Head-to-Head Comparison

| Feature / Dimension | PureHunger | DoorDash | Uber Eats | Grubhub | TableHop | Status Quo (self-delivery) |
|---|---|---|---|---|---|---|
| Restaurant commission | 12% | 25-30% (typical) | 25-30% (typical) | 25-30% (typical) | ~15% | 0% (but no digital reach) |
| Customer delivery fee | Flat $2.99 | Variable, stacked (service + delivery + small-order fees) | Variable, stacked | Variable, stacked | Flat, low | N/A |
| Restaurant payout cycle | Daily | Weekly | Weekly | Weekly | Weekly | Immediate (cash/card at point of sale) |
| Independent-restaurant discovery priority | ✅ Explicit feed priority | ❌ Chain-placement-driven | ❌ Chain-placement-driven | 🔧 Partial (long-tail catalog, weak curation) | ✅ Community-first | N/A |
| Courier density / delivery reliability | 🔧 Unproven at launch, targeted local hiring | ✅ Strong in dense markets, weaker in mid-size | ✅ Strong in dense markets, weaker in mid-size | 🔧 Declining in secondary metros | ❌ Thin, unreliable | N/A (restaurant's own staff/driver) |
| Subscription tier | ❌ None at MVP (planned post-MVP: PureHunger+) | ✅ DashPass | ✅ Uber One | 🔧 Grubhub+ (reduced marketing push) | ❌ None | N/A |
| Target segment fit for independents | ✅ Purpose-built | ❌ Secondary priority to chains | ❌ Secondary priority to chains | 🔧 Legacy catalog, not purpose-built | ✅ Similar thesis, weaker execution | ✅ (by definition, no compromise) but zero reach |

Legend: ✅ = strong / 🔧 = partial / ❌ = absent

---

### Competitor Profiles

#### DoorDash

| Dimension | Finding | Source |
|---|---|---|
| **Pricing model** | 25-30% commission tiers depending on plan (marketing/basic/premier-style tiers); customer-side service + delivery fees stack, partially offset by DashPass subscription | `[ASSUMED - publicly known industry commission structure]` |
| **Go-to-market** | Sales-led restaurant acquisition at scale + heavy consumer-side promotional spend (first-order discounts, DashPass bundling) | `[ASSUMED]` |
| **Customer feedback** | Independent restaurant owners' most consistent complaint across public forums and industry press: commission erodes margin on lower-price-point or lower-margin cuisines; consumers frequently cite fee stacking as a checkout-experience frustration | `[ASSUMED - consistent with widely reported industry sentiment]` |
| **Origin & trajectory** | Market leader by GMV share; continued national growth, but structurally incentivized to prioritize catalog breadth (chains) over independent curation | `[ASSUMED]` |
| **Key weaknesses → our opportunity** | Commission math doesn't work for margin-sensitive independents (Daniel's exact experience) → PureHunger's 12% is the direct answer; chain-favoring discovery buries independents (Maya's exact frustration) → PureHunger's independent-first feed is the direct answer | Cross-referenced against `personas.md` and `jtbd-analysis.md` |

#### Uber Eats

| Dimension | Finding | Source |
|---|---|---|
| **Pricing model** | Commission structure comparable to DoorDash (25-30% typical range); Uber One bundles delivery with rideshare benefits | `[ASSUMED]` |
| **Go-to-market** | Cross-sell into existing Uber rider base; aggressive promo-driven acquisition | `[ASSUMED]` |
| **Customer feedback** | Similar restaurant-side commission complaints as DoorDash; some consumer preference for it specifically due to existing Uber account/payment setup, not delivery-specific loyalty | `[ASSUMED]` |
| **Origin & trajectory** | #2 national player, continued investment, but delivery is a secondary business line behind rides for the parent company - less category-specific focus on independent-restaurant curation than a delivery-only competitor would have | `[ASSUMED]` |
| **Key weaknesses → our opportunity** | Same commission-math and chain-discovery weaknesses as DoorDash; being a secondary business line for its parent company means less incentive to solve mid-size-city courier density specifically | |

#### Grubhub

| Dimension | Finding | Source |
|---|---|---|
| **Pricing model** | Commission structure historically similar to DoorDash/Uber Eats; recent corporate restructuring has reduced marketing and account-management investment in many secondary markets | `[ASSUMED - consistent with widely reported pullback in mid-size-market investment]` |
| **Go-to-market** | Historically sales-led; investment now uneven across markets post-restructuring | `[ASSUMED]` |
| **Customer feedback** | Restaurant owners in secondary metros report reduced account support responsiveness; consumers report inconsistent catalog freshness in non-priority markets | `[ASSUMED]` |
| **Origin & trajectory** | Reduced strategic priority in markets like Boise creates a specific whitespace window - restaurants who might otherwise stay on Grubhub out of inertia are more open to switching when service visibly degrades | `[ASSUMED]` |
| **Key weaknesses → our opportunity** | Active market pullback = restaurants and customers both more receptive to a credible alternative right now, not hypothetically - this is a timing lever, covered in Market Timing Rationale below | |

#### TableHop *(fictional, illustrative smaller competitor)*

| Dimension | Finding | Source |
|---|---|---|
| **Pricing model** | ~15% commission, positioned similarly to PureHunger but not yet in Boise | Invented for this document as an illustrative "proof the low-commission thesis has been tried at small scale" reference point |
| **Go-to-market** | Community-first, restaurant-owner-network-driven, similar ground-game approach to Marcus Field's | Illustrative |
| **Customer feedback** | Praised for commission fairness; criticized for thin courier supply and unreliable live tracking - the operational side lags the commercial pitch | Illustrative |
| **Origin & trajectory** | Small, bootstrapped, has not scaled operational reliability alongside its commercial thesis | Illustrative |
| **Key weaknesses → our opportunity** | Validates that independents respond to a lower-commission pitch, while showing that commission alone isn't sufficient - operational reliability (courier density, live tracking, on-time delivery) has to match the commercial pitch, which is why PureHunger's MVP scope explicitly includes live delivery tracking (FEAT-DEL-002) as a Phase 1 feature, not an afterthought | |

---

### Our Competitive Position

**Primary differentiation:** A commission structure (12% vs. 25-30%) that makes the after-commission math work for margin-sensitive independent restaurants, paired with a discovery experience that leads with those same independents instead of burying them under chain placement.

**Defensible advantage:** Restaurant relationships built through a founder-led, in-person ground game (Marcus Field) that competitors' self-serve or sales-led-at-scale models don't replicate easily in a specific city, plus the informal owner-referral network effect once a critical mass of trusted independent restaurants is signed - this is closer to a local trust network than a pure price advantage, which is harder for a well-funded national competitor to simply out-discount.

**Weaknesses vs. competition:** Far smaller catalog and courier density than DoorDash/Uber Eats at launch; no subscription bundling to compete with DashPass/Uber One; unproven operational reliability (the exact gap that hurt TableHop) until live tracking and courier density are proven in practice.

---

### Competitive Risks

| Risk | Probability | Mitigation |
|---|---|---|
| DoorDash or Uber Eats runs a targeted commission-reduction promotion for independents in Boise specifically, in response to PureHunger's entry | Med | Lean into the trust/relationship advantage (peer referrals, founder-led onboarding) that a temporary promotional price cut doesn't replicate; daily payout is a structural, not promotional, differentiator |
| A well-funded national or regional player replicates the low-commission, independent-first positioning at scale | Med | Speed of restaurant-network lock-in in Boise specifically; the informal owner-referral effect compounds faster than a new entrant can replicate without the same ground-game investment |
| Courier supply proves harder to build than modeled, undermining the reliability promise that differentiates PureHunger from TableHop's failure mode | Med-High | Explicit MVP priority on courier assignment + live tracking (FEAT-DEL-002); courier payout terms ($4 base + $1.25/mile + 100% tips, daily payout) designed to out-compete incumbents on courier-side economics, not just customer/restaurant economics |

---

## SWOT Analysis

### SWOT Matrix

| | Positive | Negative |
|---|---|---|
| **Internal** | **Strengths** | **Weaknesses** |
| | S1: Founding team combines relevant direct experience - Sam Okonkwo's regional grocery-delivery ops background, Lena Vogt's ordering/dispatch architecture prototype already built | W1: No existing customer base or restaurant network at launch - starting from zero in a market where incumbents already operate |
| | S2: 12% commission is a structural, not promotional, differentiator directly answering the exact pain that drove Daniel (and peers) off a major platform | W2: Small team and limited marketing budget relative to DoorDash/Uber Eats' national advertising scale |
| | S3: Daily courier payout is a genuine operational differentiator vs. all major competitors' weekly cycles | W3: Unproven operational reliability (courier density, live tracking) - the exact failure mode that undermined TableHop |
| **External** | **Opportunities** | **Threats** |
| | O1: Grubhub's active pullback from secondary-metro investment creates a real, current whitespace window in markets like Boise | T1: A well-funded competitor could match the commission cut as a promotion without matching the structural trust/relationship model |
| | O2: Independent restaurant owners' commission frustration is visibly growing (industry press, owner networks) - the market is more receptive to this pitch now than 3 years ago | T2: Courier supply is a genuine constrained resource nationally; if PureHunger can't build reliable courier density in Boise, the reliability promise collapses and undermines the entire pitch |
| | O3: Boise-specific independent restaurant density and civic "buy local" culture provide a receptive early-adopter environment | T3: Regulatory risk around courier classification (1099 independent contractor status) could increase courier-side costs industry-wide, compressing the commission-rate advantage that funds this entire model |

---

### Strategic Implications

**SO Strategies (Strengths + Opportunities):**
- Use the founding team's direct ops and architecture experience to move fast on restaurant onboarding in Boise while Grubhub's local pullback keeps the window open

**WO Strategies (Weaknesses + Opportunities):**
- Offset the small marketing budget by leaning on the informal Boise restaurant-owner referral network (a near-zero-CAC channel) rather than competing head-on with DoorDash/Uber Eats' paid acquisition spend

**ST Strategies (Strengths + Threats):**
- Use the daily-payout and 12%-commission structural advantages (hard to match without restructuring a competitor's own economics) to defend against a temporary promotional price match

**WT Strategies (Weaknesses + Threats):**
- Prioritize proving courier density and live-tracking reliability in Boise specifically before any multi-city expansion, since operational failure here is both the biggest internal weakness and the clearest path to repeating TableHop's failure mode

---

### Priority Actions (from SWOT)

1. Lock in 30-40 signed, active independent restaurants in the Boise core within 90 days, while Grubhub's local pullback keeps the whitespace open (O1 + S2)
2. Prove courier density and on-time delivery reliability in Boise before any expansion-city commitment - this is the single highest-consequence unresolved risk (W3 + T2)
3. Build the informal owner-referral channel deliberately (not just opportunistically) as the primary low-CAC acquisition engine, given the marketing-budget constraint (W2 + O3)

---

## Market Timing Rationale

### "Why Now?" Statement

Independent restaurant owners' commission frustration has reached a visible, vocalized breaking point (Daniel Osei's experience is representative, not unique), at the same moment a major incumbent (Grubhub) is visibly reducing investment in secondary metros like Boise - creating a specific, current window where both the supply-side pain and the competitive whitespace are real, not hypothetical.

---

### Enabling Conditions

| Condition | Change | Since When | Impact on Our Opportunity |
|---|---|---|---|
| Competition | Grubhub's reduced investment and account-management presence in secondary metros including Boise | Ongoing, accelerating recently | High - direct whitespace, restaurants already experiencing reduced service are more open to switching |
| Behavior | Independent restaurant owners increasingly vocal (owner networks, industry press) about commission economics not working on lower-margin cuisines | Ongoing, growing | High - the core pitch (12% vs. 25-30%) lands on an audience already primed to want this, not one that has to be educated into the problem |
| Market | Mid-size and secondary-metro delivery-app penetration still below dense-urban-core levels (structural underinvestment by incumbents) | Structural, longstanding | High - the demand-side headroom (customers who would order more if reliability and discovery were better) is real and largely untapped by incumbents |
| Technology | Payment processing (tokenized/split payments, e.g., Stripe Connect-style infrastructure) and mapping/dispatch tooling are now mature, low-cost, and available off-the-shelf | Ongoing (past several years) | Med - lowers the technical barrier for Lena Vogt's team to build a reliable ordering/dispatch stack without incumbent-scale engineering investment |
| Regulation | Courier employment classification (1099 independent contractor) remains contested state-by-state, including active discussion in some states | Ongoing | Med, watch closely - could raise courier-side costs industry-wide if reclassification spreads, compressing the margin that funds the 12% commission advantage |

---

### Window of Opportunity

**Opens:** Now - Grubhub's pullback and the vocalized independent-restaurant commission frustration are both current conditions, not anticipated future ones.
**Closes:** When either (a) a well-funded competitor replicates the low-commission, independent-first positioning in Boise specifically, or (b) courier classification regulation materially raises costs industry-wide, compressing the margin that funds the 12% rate.
**Estimated window:** 18-24 months before a credible, well-funded copycat is likely to target the same whitespace, based on how quickly similar positioning plays (e.g., TableHop) have surfaced in adjacent Mountain West markets.

**Urgency:** High - the whitespace is real but not exclusive; the restaurant-side ground game and owner-referral network effect need real momentum in Boise before a better-funded competitor notices and responds.

---

### Risk of Being Early / Late

| Scenario | Probability | Consequence |
|---|---|---|
| Too early (market not ready) | Low | Independent restaurant commission frustration and mid-size-city delivery underpenetration are both already-present conditions (per personas.md and jtbd-analysis.md), not conditions PureHunger has to wait for or create |
| Right timing | Med-High | Whitespace captured before a well-funded competitor responds; restaurant-side trust network builds a defensible moat during the open window |
| Too late (window closes) | Med | A well-funded competitor (or Grubhub reversing its pullback) matches the commission cut before PureHunger reaches critical restaurant density in Boise, eliminating the first-mover trust advantage this model depends on |

---
**Čo si teraz má:** TAM/SAM/SOM postavené bottom-up (nie top-down %), konkurenčná mapa vrátane "no delivery app" status quo, SWOT so strategickými akciami, a jasne argumentovaný "Why Now" s konkrétnym oknom príležitosti (18-24 mesiacov).

**Ďalší krok:** `/pm-problem-validation` - skonvertuje toto s personami a JTBD do jedného Phase 2 exit dokumentu a vydá Go/No-Go odporúčanie pre Phase 3a.

**Môžeš preskočiť ak:** Ideš rovno na `/pm-problem-validation` bez ďalšieho track-u - trh a konkurencia sú tu už dostatočne zmapované pre konvergenciu.
