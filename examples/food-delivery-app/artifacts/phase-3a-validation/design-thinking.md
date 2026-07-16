# Design Thinking Synthesis - PureHunger

> **Phase:** 3 - Define & Validation
> **Date:** 2025-11-03
> **Stages covered:** Define + Ideate (Empathize = Phase 2 discovery)
> **Input:** Problem Validation Summary, Personas (Maya Torres, Daniel Osei, Priya Nair), JTBD Analysis

---

## DEFINE STAGE

### Problem Statement

PureHunger addresses a two-sided failure in food delivery that is specific to mid-size cities (100k-500k population). Independent restaurant owners are stuck choosing between paying 25-30% commission to a major delivery platform - eroding margins that are often already thin (25-35% food cost) - or staying off delivery apps entirely and losing the growing share of customers who default to app-based ordering. On the other side, customers in these same markets are underserved by apps built for dense urban cores: selection is thin, delivery times run long, and discovery algorithms bury independent restaurants under chains that pay for placement. Neither side is served well by the current market structure, and the two failures reinforce each other - restaurants leave or never join, which thins out selection, which gives customers fewer reasons to open the app.

**Problem statement:** Independent restaurants in mid-size US cities cannot afford to be on delivery platforms at 25-30% commission, and the customers in those same cities who want to order from them can't reliably find them on the platforms that are supposed to connect the two.

**What makes this problem worth solving:**
- Pain intensity: High for restaurant owners (existential - commission at incumbent rates turns a marginally profitable order into a loss-making one for low-margin cuisines); Medium-High for customers (frustration and switching, not urgency - they still order, just from chains or not at all from the spots they'd prefer)
- Frequency: Every order, for restaurants (100% of transaction volume is taxed by commission); several times a week for the primary customer persona (Maya Torres orders delivery 3-4x/week)
- Current alternatives: Stay off platforms entirely (lose discoverability and convenience-driven demand) or absorb the margin loss (Daniel Osei's 18-month experience before dropping his platform); customers default to chains that pay for placement, or drive/pick up themselves
- Economic impact: For a restaurant near 28% food cost margin, a 27% commission rate can turn a $30 order into a near-zero-margin transaction once packaging and processing fees are included; for customers, the cost is time (longer search, longer delivery windows) and a worse product (missing out on the independent restaurants they'd actually prefer)

---

### Point of View (POV)

PureHunger is a three-sided marketplace, so Define stage produces a primary POV (the side the business model differentiates on) and a secondary POV (the side that makes the marketplace worth using once restaurants are on it).

**Primary POV Statement - Restaurant Owner:**

> Independent restaurant owners need to reach delivery-app customers without losing their operating margin to commission
> because commission platforms charge every restaurant the same 25-30% rate regardless of cuisine or margin structure, and a rate that a 70%-margin chain can absorb is existential for an 8-year-old, 30%-margin independent kitchen.

**Deconstructed:**

| Element | Content |
|---|---|
| User | Daniel Osei - independent restaurant owner, 8 years in business, single-location West African restaurant |
| Need | Reach app-first delivery customers while keeping enough margin per order to make the channel worth running |
| Insight | Commission is not a uniform cost - it is a cost that scales inversely with a restaurant's existing margin, and platforms have never priced for that difference |

**Secondary POV Statement - Customer:**

> Busy professional customers need to discover and order from good independent restaurants near them quickly
> because the dominant delivery apps' discovery ranking favors restaurants that pay for placement, which means the customer sees the same chains everyone else sees and never encounters the independent spot they'd actually choose if it were visible.

**Why this POV:** Restaurant economics is the wedge that gets supply onto the platform at all - without it there is no marketplace. But customer discoverability is what makes that supply valuable once it exists. A POV that only addresses one side produces a marketplace that acquires restaurants but can't retain customer demand, or vice versa. Both must hold.

---

### How Might We (HMW) Questions

**Source pains → HMW reframes:**

| Validated pain | HMW question |
|---|---|
| Restaurants lose enough margin to commission that delivery becomes a net loss on thin-margin cuisine | HMW price the platform so commission scales with what a restaurant can actually absorb, not a flat rate built for chain economics? |
| Customers can't find good independent restaurants because discovery is pay-to-play | HMW rank restaurants by relevance to the customer instead of by who paid for placement? |
| Couriers face opaque, frequently-changed payout algorithms and a weekly payout cycle | HMW make courier pay transparent and immediate enough that it becomes a reason to choose PureHunger over incumbent gig platforms? |
| Delivery apps are built and tuned for dense urban-core order density, leaving mid-size cities with slow, unreliable dispatch | HMW build a dispatch and courier-density model that works economically at mid-size-city order volume instead of importing an urban-core model? |

**Additional HMW lenses:**

| Lens | HMW question |
|---|---|
| Amplify what's working | HMW do more of what customers already value about app ordering (speed, convenience, tracking) while fixing selection and discovery? |
| Remove the pain | HMW eliminate commission as the reason an independent restaurant stays off delivery apps entirely? |
| Flip the assumption | HMW if delivery platforms didn't need to charge the same rate to every restaurant regardless of margin? |
| Change who does it | HMW shift discovery ranking logic away from advertiser payment and onto proximity, rating, and repeat-order signal? |
| Reduce anxiety | HMW make a restaurant owner's first 90 days on the platform feel low-risk enough that trying it isn't a gamble on their margin? |

**Priority HMW (to ideate on):**

1. HMW price the platform so commission scales with what a restaurant can actually absorb, not a flat rate built for chain economics?
2. HMW rank restaurants by relevance to the customer instead of by who paid for placement?
3. HMW build a dispatch and courier-density model that works economically at mid-size-city order volume instead of importing an urban-core model?

**Selection rationale:** These three HMWs map directly onto the three sides of the marketplace and, unlike the courier-payout HMW, each has a structural lever the founding team can pull immediately (pricing model, ranking algorithm, dispatch design) rather than depending on a downstream operational fix. The courier-payout HMW remains a live question but is treated as a retention lever within the dispatch/density direction rather than a separate ideation track.

---

## IDEATE STAGE

### Ideation Results

**Priority HMW being explored:** HMW price the platform so commission scales with what a restaurant can actually absorb, combined with HMW rank restaurants by relevance instead of by payment.

**Ideas generated (clustered by theme):**

#### Theme 1: Fair Take
Ideas that converge on restructuring the commission relationship itself.
- Flat 12% commission for every restaurant, published as a rate card (no negotiated or tiered rates that create distrust)
- No pay-for-placement listings or sponsored slots at launch - the commission is the only monetization lever, and it is transparent
- 30-day written notice requirement before any commission change, formalized in the Restaurant Partner Agreement
**Core hypothesis:** If commission is flat, low, and contractually protected from change, restaurants that could never make incumbent-platform economics work will sign up and stay.

#### Theme 2: Local-First Discovery
- Rank restaurants by proximity + rating + repeat-order rate, not advertiser spend
- "Independent Spotlight" curated section on the home screen highlighting non-chain restaurants
- Explicitly exclude chain/franchise restaurants from onboarding at launch to keep the catalog differentiated
**Core hypothesis:** If discovery surfaces independent restaurants on merit instead of ad spend, customers in mid-size cities will find (and return to) restaurants they couldn't reliably find on incumbent apps.

#### Theme 3: Density-Appropriate Dispatch
- Zone-based courier batching tuned for a 100k-500k city's order density instead of dense-urban-core stacking logic
- Daily (not weekly) courier payout as both a retention lever and a supply-side acquisition message
- Transparent per-delivery earnings breakdown shown to couriers before they accept a delivery
**Core hypothesis:** If dispatch is designed for mid-size-city density from day one (rather than a scaled-down urban model) and payout is faster and clearer than incumbents, PureHunger can maintain acceptable delivery times without over-subsidizing idle courier time.

---

### Promising Directions

| Direction | Core concept | Why promising | Risks / constraints |
|---|---|---|---|
| Fair Take commission model | Flat 12% commission, published rate card, 30-day change-notice guarantee | Directly resolves the restaurant-side POV; commission math is a concrete, provable number restaurant owners can evaluate immediately | Commission alone is copyable - an incumbent could price-match in a specific market to blunt PureHunger's wedge |
| Local-First Discovery | Merit-based ranking (proximity, rating, repeat orders), no sponsored placement, chain exclusion at launch | Directly resolves the customer-side POV; differentiates the catalog itself, which is harder to copy than a price | Smaller initial catalog than an incumbent (independent-only) risks looking thin in categories with few local options |
| Density-Appropriate Dispatch | Zone batching + daily payout tuned to mid-size-city order volume | Makes courier supply viable at a density incumbents don't optimize for; daily payout is a genuine courier-side differentiator | Requires proving fill-rate and delivery-time performance at lower order density than incumbent hubs operate at |

**Recommended direction to pursue:**
Fair Take + Local-First Discovery, launched together as a single positioning, with Density-Appropriate Dispatch as the operational enabler underneath both. Commission is the acquisition wedge that gets restaurants onto the platform; discovery fairness is what keeps customers engaged once a differentiated catalog exists. Neither alone produces a working marketplace - a low-commission platform with the same pay-to-play discovery as incumbents doesn't change what customers see, and a fair-discovery platform with incumbent-level commission never gets enough restaurants onto it to have anything to discover.

**What would prove this direction wrong:**
If restaurants sign up under the 12% commission (validating the pricing lever) but weekly order volume per restaurant stays too low to matter to their bottom line, the direction fails on the demand side even though the pricing thesis holds. The observable signal: restaurants that reach 90 days on the platform with fewer than ~15 orders/week are not experiencing the promised economics, regardless of commission rate. This is the falsification condition carried into `/pm-hypotheses` - at least one experiment must test customer-side order volume per restaurant, not just restaurant sign-up willingness.

---

### What We Are Not Doing

| Idea | Why ruled out |
|---|---|
| Chain/franchise restaurant onboarding at launch | Chains are already well-served by incumbent platforms and their placement budgets; onboarding them would dilute the "independent-only" catalog differentiation that Local-First Discovery depends on |
| Paid/sponsored placement as a second revenue lever | Undermines the fairness positioning that is core to the customer-side POV - the moment ranking can be bought, the discovery differentiator is gone |
| Negotiated/tiered commission rates per restaurant | Creates the same distrust dynamic restaurants already have with incumbent platforms (opaque, restaurant-specific deals); a single published rate is the trust mechanism |
| Dynamic/surge courier pricing at launch | Adds exactly the kind of payout unpredictability that Priya Nair's persona names as the top frustration with incumbent platforms; deferred until dispatch data justifies it |

---

## Elevator Pitch

PureHunger is a food delivery marketplace for independent restaurants in mid-size cities. Restaurants pay 12% commission instead of the 25-30% charged by national platforms, so an order that would be a wash - or a loss - on Uber Eats or DoorDash is actually worth fulfilling. Customers get a catalog of real independent kitchens ranked by proximity and rating instead of ad spend, and couriers get paid daily instead of waiting a week. We're starting in Boise, Idaho - a market big enough to matter and exactly the size national platforms don't optimize for.

---

## Validation Hypotheses Draft (informal - formalized in `/pm-hypotheses`)

These are directional beliefs from the Ideate stage, not yet structured hypotheses with success criteria. `/pm-hypotheses` (Plan mode) converts these into the formal Hypothesis Register.

1. Independent restaurant owners in mid-size cities will name commission as a top-2 unprompted pain and will be willing to sign a lower flat-rate agreement within weeks of being approached directly.
2. Independent restaurants are reachable and convertible via direct owner-to-owner outreach, without needing a paid acquisition channel to hit initial supply targets.
3. Customers in a mid-size city underserved by incumbent apps will engage with (sign up for, and eventually order from) a platform that visibly promotes independent restaurants over chains.
4. Couriers will prefer daily payout and transparent per-delivery pay enough to choose PureHunger shifts over incumbent platforms offering weekly payout.
5. A meaningful number of restaurants will commit (signed partner agreement, not just interest) to the platform before launch, at a volume that de-risks the initial catalog.

---

## Define → Strategy Bridge

How this Define + Ideate output connects to what comes next:

| Design Thinking output | Used by |
|---|---|
| Problem Statement | PRD Section 1, Business Case rationale |
| Primary + Secondary POV | PRD Section 3 (Value Proposition framing per segment) |
| HMW questions | Product Roadmap - what each phase must answer |
| Recommended direction (Fair Take + Local-First Discovery) | Lean Canvas - Value Proposition and Unfair Advantage blocks |
| Validation Hypotheses Draft | `/pm-hypotheses` Plan mode input |

**Open questions for Phase 3b strategy work:**
1. What courier fill-rate and delivery-time performance is achievable at Boise's order density before subsidizing idle courier time becomes necessary - needs business model / financial analysis.
2. Is 12% commission sustainable at target gross margin once payment processing and restaurant-success costs are included, or does it need to move to 13-14% as the business scales past the initial city?
