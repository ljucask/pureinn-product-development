# Customer Segments & Personas - PureHunger

> **Phase:** 2 - Discovery (Track D: VOC - Customer Discovery)
> **Date:** 2026-07-14
> **Data basis:** 3 informal in-person conversations with independent Boise restaurant owners (conducted by Marcus Field, Head of Growth & Restaurant Partnerships, during pre-launch restaurant scouting in June-July 2026) + 1 first-hand operator account from Sam Okonkwo (CEO, 6 years running merchant commission conversations at a regional grocery-delivery startup) + 14 synthetic customer interviews (structured founder-knowledge elicitation, calibrated against published secondary-metro food-delivery usage research) + founder assumptions filling remaining gaps.
>
> **Provenance key used throughout this document:**
> - `[REAL VOC - n=X]` - actual conversations with real people matching the profile, informal and low-N (not a formal research study)
> - `[SYNTHETIC INTERVIEW]` - AI-assisted synthetic interview calibrated against founder domain knowledge and published market data, not a real transcript
> - `[ASSUMED - reason]` - founder inference with no interview or observational basis yet
>
> This is a greenfield, founder-led product (no commissioning client) - there is no `[CLIENT-ASSERTED]` data class in this document. Every claim not tagged `[REAL VOC]` should be read as a hypothesis, not validated fact.

---

## Segmentation Overview

PureHunger is a two-sided marketplace (a third side - couriers - is analyzed separately in operator/courier discovery, not repeated here). The primary segmentation dimension is **which side of the marketplace the person sits on and what job they hire PureHunger for** - customers hire it to get food without the trip; independent restaurants hire it to get incremental delivery revenue without the margin damage a major platform inflicts. These are not two flavors of the same need; they get different products, different pricing logic, and different success metrics, which is why they are treated as separate segments rather than one "user" segment with two personas of convenience.

---

## Segment Map

| Segment | Size (est.) | Primary Need | Key Differentiator from Other Segments |
|---|---|---|---|
| Time-Starved Urban Professionals (customer side) | ~38,000 households in the Boise MSA identified as frequent (weekly+) app-delivery users `[ASSUMED - derived from Boise MSA population 830K x estimated 32% delivery-app penetration x professional-household filter, see market-analysis.md]` | Fast, reliable delivery from restaurants they trust, without wading through chain listings | Will pay a premium for curation and speed; price-sensitive on the delivery *fee*, not on the food itself |
| Margin-Squeezed Independent Restaurants (supply side) | ~410 independent, non-chain full-service restaurants in the Boise MSA `[ASSUMED - Idaho Dept. of Labor food-service establishment counts, chain-filtered estimate]` | A delivery revenue channel that doesn't erode an already-thin margin | Needs low commission + fast payout, not just app visibility - visibility without margin is what drove them off the incumbent platform |

**Out of scope for this document:** Couriers (Priya Nair's segment) are the marketplace's third side. They are analyzed in a separate courier/operator persona track since their relationship to PureHunger is closer to gig-labor supply than to either demand-side segment above - conflating them here would blur genuinely different needs (a courier's "primary need" is payout transparency and schedule flexibility, not food or restaurant revenue).

---

## Segment Profiles

### Segment 1: Time-Starved Urban Professionals

**Who they are:** Working professionals age 26-40 in Boise's core neighborhoods (North End, East End, Downtown, Bench) and inner suburbs, household income $55K-$110K, no kids or young kids, 1-2 person households, high weekday time pressure from work.

**Primary goal:** Get a good meal on the table on a weeknight with near-zero planning or prep time, while still feeling like they're supporting places they actually like.

**Current solution:** DoorDash and Uber Eats (both already operate in Boise), supplemented by direct pickup calls to 2-3 favorite independent spots when the delivery apps' selection or wait times disappoint.

**Key frustrations with current solution:**
- Chain restaurants (with placement budgets) crowd out the independent spots they'd actually rather order from
- Delivery times in Boise are inconsistent - the incumbent apps' courier density was built for denser metros and thins out fast outside downtown core
- Fee stacking (service fee + delivery fee + "small order" fee + suggested tip on top of an already-marked-up menu price) feels deceptive, even when the total isn't wildly different from PureHunger's flat model

**What they'd pay for:** A flat, predictable delivery fee and a feed that actually surfaces good independent restaurants first, not last.

**Revenue potential:** ~38,000 households x est. 32% active delivery-app usage x ~$600/year average delivery GMV per active user ≈ $7.3M/year in addressable GMV within Boise proper alone `[ASSUMED - see market-analysis.md TAM/SAM/SOM methodology]`.

**Strategic priority:** High - this is the segment that generates order volume, which is the only thing that makes the restaurant-side value proposition (delivery revenue) real. Without volume here, Daniel's segment gets nothing worth having.

---

### Segment 2: Margin-Squeezed Independent Restaurants

**Who they are:** Owner-operated, single-location, full-service or fast-casual independent restaurants in the Boise MSA, typically 5-15 years in business, thin (8-15%) net margins even before any delivery commission, owner is also the primary decision-maker (no corporate franchise layer).

**Primary goal:** Add a delivery revenue channel that is net-positive after commission, not a channel that technically "adds revenue" while quietly destroying margin order by order.

**Current solution:** Either (a) enrolled with a major platform and eating the 25-30% commission as a cost of visibility, or (b) opted out entirely and relying on dine-in, phone-order pickup, and word of mouth - actively losing the growing share of customers who default to app-based ordering.

**Key frustrations with current solution:**
- Commission math simply doesn't work on already-low-margin cuisines - a $28 entree at 28% commission returns less than the food cost plus labor on some dishes `[REAL VOC - n=1, Daniel Osei's account]`
- No influence over placement - independents get buried under chains that pay for featured slots, even though the independent's food is what customers search reviews for `[REAL VOC - n=2]`
- Weekly (not daily) payout cycles from the major platform created cash-flow strain during slow weeks `[REAL VOC - n=1]`

**What they'd pay for:** A lower, transparent commission rate and a payout cycle that matches how a small, cash-flow-sensitive business actually operates (daily, not weekly).

**Revenue potential:** ~410 independent restaurants x est. 15-20% realistic PureHunger adoption in Year 1-2 x average incremental delivery GMV per restaurant of ~$1,800/month ≈ $1.3M-$1.8M/year in restaurant-side GMV within Boise proper `[ASSUMED]`.

**Strategic priority:** High - this segment is the supply-side bottleneck of the marketplace. Selection density (how many good independents are on PureHunger) is the entire differentiator versus the incumbents; under-investing here means Segment 1's core reason to switch never materializes.

---

## Segment Prioritization

| Segment | Market Size | Pain Intensity | Willingness to Pay | Accessibility | Priority |
|---|---|---|---|---|---|
| Margin-Squeezed Independent Restaurants | M | High | High (commission delta is the whole pitch) | Medium (requires door-to-door founder-led sales, not self-serve) | **1** |
| Time-Starved Urban Professionals | M | Medium | Medium (fee-sensitive, food-price-tolerant) | High (standard app acquisition channels apply) | **2** |

**Primary segment for MVP:** Margin-Squeezed Independent Restaurants. In a two-sided marketplace, the constrained resource at launch is supply, not demand - Boise already has two national platforms serving customer-side demand adequately on paper. PureHunger's entire wedge (a materially lower commission) only becomes visible to a customer as "better restaurant selection," which requires signing 30-50 independent restaurants *before* meaningful customer-side marketing spend is justified. Sequence: restaurant acquisition first (Marcus Field's ground game), customer acquisition second, timed to restaurant density crossing a usable threshold (~40 active restaurants in the Boise core).

---

## Persona 1: Maya Torres (Time-Starved Urban Professionals)

**Role:** Marketing Manager at a mid-size Boise employer (SaaS or professional services)
**Age range:** 27-32
**Context:** Lives alone or with a partner in Boise's North End or East End, no children, works a standard 9-to-6 that regularly runs long, drives or bikes to work, orders delivery 3-4x/week on weeknights.

### Goals

| Goal | Priority |
|---|---|
| Get dinner sorted with minimal decision fatigue after a long workday | High |
| Discover and support good independent restaurants, not just default to whatever app surfaces first | Med |
| Keep delivery costs predictable so it doesn't feel like a "tax" on eating well | Med |

### Pains

| Pain | Intensity | Current Workaround |
|---|---|---|
| Good independent restaurants are buried under paid-placement chains in the incumbent apps | High | Manually searches by name for 2-3 favorite spots instead of browsing |
| Delivery times outside the Boise downtown core are unreliable | Med | Orders earlier than she wants to eat, or picks up herself when she's in a rush |
| Fee stacking makes the final price feel non-transparent | Med | Mentally "budgets" an extra $6-8 above the menu price before ordering |

### Behaviors & Habits

- Orders almost exclusively on weeknights (Sun-Thu), rarely weekends (goes out instead)
- Has 4-5 "rotation" restaurants she reorders from rather than exploring broadly - discovery has to be low-effort to break this pattern
- Checks star rating and delivery-time estimate before opening a restaurant's menu; abandons if estimate exceeds ~40 minutes
- Tips based on a flat percentage regardless of order size, and considers tip a signal of respect for the courier, not an optional extra

### Tools They Use Today

DoorDash, Uber Eats, Google Maps (to check a restaurant's real reviews before trusting the delivery app's curated ones), Instagram (to find new local spots before they show up in delivery apps)

### Quotes (from research)

> "I know there's a good Ethiopian place near me because I saw it on Instagram, but by the time I open DoorDash it's on page 3 behind four different pizza chains." `[SYNTHETIC INTERVIEW]`

> "I don't mind paying a flat fee if I know that's actually the number. What annoys me is opening the checkout screen and watching the total climb three times before I hit pay." `[SYNTHETIC INTERVIEW]`

### Empathy Map

| Quadrant | Findings |
|---|---|
| **Says** | "I just want dinner sorted without thinking about it." / "I wish these apps showed me the good local places first." |
| **Thinks** | Worries that ordering delivery constantly is a little wasteful or unhealthy, but rationalizes it as a fair trade for the time she gets back on a busy week. |
| **Does** | Re-orders from the same 4-5 restaurants; checks delivery-time estimate before browsing the menu; screenshots new restaurant recommendations from Instagram to try "someday." |
| **Feels** | Mild guilt about not cooking more; low-grade annoyance at fee stacking; genuine pride when she finds and shares a good independent spot with friends. |
| **Sees** | Friends' Instagram stories tagging small Boise restaurants that don't show up prominently in her delivery app; coworkers comparing DashPass vs. Uber One subscriptions at lunch. |
| **Hears** | Coworker recommendations for "hidden gem" restaurants; local Boise Reddit/Facebook groups debating which delivery app has better coverage outside downtown. |

### Current Journey (as-is)

1. **6:15 PM, still at desk or just leaving work** - Realizes she hasn't planned dinner; feels a flicker of decision fatigue on top of an already tiring day.
2. **Opens DoorDash or Uber Eats** - Scrolls past 2-3 screens of chain restaurants with paid placement before reaching anything independent; mild frustration.
3. **Defaults to a "rotation" restaurant** rather than the new spot she saw on Instagram last week, because trying something new means more browsing effort she doesn't have energy for.
4. **Checkout screen** - Watches the total climb through service fee, delivery fee, and suggested tip; feels the "fee stacking is deceptive" annoyance but completes the order anyway - sunk cost of time already spent.
5. **Waits, sometimes past the estimated window** - If she's outside downtown core, delivery frequently runs 10-15 minutes past the quoted time; she doesn't complain (low stakes, not worth the effort) but the reliability erosion registers subconsciously.
6. **Eats, rates absentmindedly** - Rarely leaves a review; the transaction is functional, not delightful.

### What Success Looks Like for Them

Opening one app, seeing the independent restaurants she already half-remembers from Instagram surfaced first, and knowing the fee she sees at browse time is the fee she pays at checkout - with food arriving when promised.

### Why They'd Adopt Our Product

The trigger is friction fatigue with fee stacking and buried discovery, not price shock - Maya isn't looking to save money, she's looking to stop feeling low-grade annoyed at a routine she does 3-4x/week. A flat, visible $2.99 fee and a restaurant feed that leads with independents converts her the first time it delivers on time.

### Why They Might Not

She has switching inertia - her 4-5 "rotation" restaurants may not be on PureHunger at launch (restaurant density risk), and re-downloading yet another delivery app for marginal fee transparency isn't obviously worth the effort unless her favorite spots are actually there.

---

## Persona 2: Daniel Osei (Margin-Squeezed Independent Restaurants)

**Role:** Owner-operator of a single Ghanaian/West African restaurant in Boise
**Age range:** 38-45
**Context:** 8 years in business, full-service dine-in with a growing takeout share, ~9 staff including himself, makes every commercial decision personally - no corporate layer, no dedicated ops or finance staff.

### Goals

| Goal | Priority |
|---|---|
| Add a delivery revenue channel that is net-positive after commission and packaging cost | High |
| Regain the customer reach he lost when he dropped the major platform, without repeating the margin mistake | High |
| Spend as little owner-time as possible managing a third delivery channel on top of running the restaurant | Med |

### Pains

| Pain | Intensity | Current Workaround |
|---|---|---|
| Delivery-platform commission (25-30%) eats margin on dishes that are already low-margin due to ingredient cost | High | Dropped the major platform entirely 18 months ago after tracking that several dishes were losing money net of commission |
| Loss of app-based discovery reach since dropping the platform | Med | Relies on dine-in loyalty, phone orders, and word of mouth; acknowledges he's invisible to the growing share of customers who only order through an app |
| Weekly payout cycles strained cash flow during slower weeks, before he even left the platform | Med | Kept a larger cash buffer than he'd otherwise need, tying up working capital |

### Behaviors & Habits

- Tracks food cost and margin per dish manually in a spreadsheet - he knows his numbers cold, which is exactly why the commission math was untenable
- Personally negotiates or vets any new vendor relationship; distrustful of anything pitched as "more visibility" without a clear, provable margin case
- Talks to other independent restaurant owners in Boise regularly (informal owner network) - reputation among peers matters more to his decisions than marketing claims

### Tools They Use Today

Square POS (in-restaurant), a manual spreadsheet for food cost/margin tracking, phone-based takeout ordering, Instagram for restaurant marketing

### Quotes (from research)

> "I did the math on my jollof rice plate after DoorDash's cut - I was making less than minimum wage per order once you count the packaging and my time. I'm not doing that again unless the number actually works." `[REAL VOC - n=1, Daniel Osei's account, June 2026]`

> "Nobody in this business trusts 'more visibility' as a pitch anymore. Show me the number after your cut and I'll decide." `[REAL VOC - n=2, other independent Boise restaurant owners]`

### Empathy Map

| Quadrant | Findings |
|---|---|
| **Says** | "Show me the number after your cut." / "I'm not doing delivery again unless the math actually works this time." |
| **Thinks** | Suspects most delivery platforms optimize for their own take rate, not restaurant health; privately worries that staying off delivery apps is slowly costing him younger customers who default to ordering through an app. |
| **Does** | Tracks food cost/margin per dish in a spreadsheet before agreeing to anything; asks other restaurant owners about their experience before signing up for a new channel. |
| **Feels** | Burned by the previous platform experience; cautiously curious but guarded about trying delivery again; protective of the margin that keeps his restaurant viable. |
| **Sees** | Other independent restaurants in his owner network either struggling with the same commission math or quietly also opting out of delivery apps entirely. |
| **Hears** | Peer restaurant owners' word-of-mouth accounts (trusted more than any sales pitch); occasional customer requests asking "are you on any delivery app?" |

### Current Journey (as-is)

1. **A customer asks "are you on DoorDash?"** - Daniel says no; feels the quiet cost of lost reach each time this happens, but doesn't act on it because the previous experience burned him.
2. **Reviews his monthly numbers** - Notices takeout/phone orders plateauing while he suspects app-based ordering keeps growing citywide; feels the gap without hard data to size it.
3. **A new delivery platform rep pitches him** (this is where PureHunger enters) - His default posture is skepticism; he asks for the commission rate and payout terms before anything else, because he was burned once already.
4. **Runs his own margin math** on 2-3 of his actual menu items against the pitched commission rate, using his existing spreadsheet - this is the moment that decides whether he signs up, not the sales pitch itself.
5. **Talks to at least one peer restaurant owner** before committing, to sanity-check the pitch against someone he trusts more than a rep.

### What Success Looks Like for Them

Delivery orders arrive as pure incremental revenue with commission and payout terms that hold up under his own spreadsheet math, no owner-time lost to platform management beyond initial setup, and daily (not weekly) payouts that match his cash-flow rhythm.

### Why They'd Adopt Our Product

The 12% commission (vs. 25-30%) is the number that changes his spreadsheet math from negative to positive on the dishes that mattered most in his previous platform experience - and daily payout directly answers his cash-flow pain, a concrete improvement over his prior weekly cycle, not just a marketing claim.

### Why They Might Not

Trust is the core objection, not price - he was burned once on a "better" platform pitch before, and 8 years of hands-on margin discipline makes him allergic to unproven promises. He needs to see the after-commission number on his actual dishes, ideally validated by a peer he trusts, before he'll sign anything.

---

## Persona Usage Guide

| Persona | Use for | Don't use for |
|---|---|---|
| Maya Torres | MVP ordering-flow UX, discovery/feed ranking decisions, customer-side acquisition messaging, delivery-fee transparency design | Restaurant onboarding flow, courier-facing product decisions, B2B sales messaging |
| Daniel Osei | Restaurant onboarding flow and sales pitch structure, commission/payout messaging, restaurant-facing dashboard priorities | Consumer app UX decisions, courier scheduling/payout product decisions |

---
**Čo si teraz má:** Segmenty a dve plne rozpracované persony (Maya - zákazník, Daniel - nezávislá reštaurácia) s Empathy Map a as-is journey, plus jasná MVP sekvencia (reštaurácie pred zákazníkmi kvôli supply-side bottlenecku).

**Ďalší krok:** `/jtbd-building` - analyzuje Jobs-to-be-Done a Forces diagram pre Mayu aj Daniela, vysvetlí prečo by prešli na PureHunger a čo ich brzdí.
Alebo spusti `/pureinn` pre Phase 2 gate check ak sú hotové aj ostatné Track A-C.

**Môžeš preskočiť `/jtbd-building` ak:** Máš jasné JTBD insights z rozhovorov a nepotrebuješ formálny Forces diagram pre fázu 3a - v tomto prípade to však neplatí, formálny Forces diagram pre obe strany trhu je potrebný kvôli chýbajúcemu formálnemu výskumu (zatiaľ len n=3 real VOC).

---

## Early Adopters Profile

> **Phase:** 2 - Discovery (Track D: VOC - Customer Discovery)
> **Date:** 2026-07-14

### Definition

Early adopters are the first 30-50 restaurants and first ~500 ordering households in Boise. They are not average users - they are willing to use an imperfect, unproven platform because the pain (or the opportunity) is intense enough that waiting for a polished, battle-tested product costs them more than the risk of trying something new.

Because PureHunger is two-sided, there are two distinct early-adopter profiles that must land together - restaurant density with no customers is a ghost-town marketplace, and customer demand with no restaurant selection is an empty app. Both are described below.

---

### Early Adopter Profile A: Restaurant Side (Supply)

**Segment:** Margin-Squeezed Independent Restaurants
**Persona:** Daniel Osei

#### Characteristics

| Characteristic | Description |
|---|---|
| Pain intensity | High - actively losing app-ordering customers today with no delivery channel at all, or actively bleeding margin on an existing platform |
| Current situation | Either fully off delivery apps (losing reach) or still enrolled with a major platform while quietly resenting the commission math |
| Technical comfort | Medium - comfortable with Square POS and basic digital tools; will not tolerate a clunky merchant dashboard, but doesn't need a sophisticated one either |
| Decision speed | Medium - Daniel-type owners decide fast once shown their own margin math, but want a peer reference first, which adds 1-2 weeks to the cycle |
| Feedback willingness | High - restaurant owners who feel burned by a previous platform are vocal, opinionated, and want a direct line to actually be heard |
| Referral potential | High within the informal Boise independent-restaurant owner network - one convinced owner credibly refers 2-3 peers |

#### What Triggers Them to Try a New Solution

- A concrete, restaurant-specific margin calculation showing the commission delta on their actual menu (not a generic pitch)
- Hearing from a trusted peer restaurant owner that the payout and commission terms held up in practice, not just on paper
- A customer directly asking "are you on any delivery app?" often enough that the lost-reach cost becomes undeniable

#### What They Need from Us (Day 1)

**Must have:**
- A commission rate materially and verifiably lower than 25-30%, shown against their real dishes before they sign
- Daily payout, working from day one - this is the second half of the pitch and cannot slip in early operations

**Nice to have (but OK to lack at launch):**
- A polished merchant analytics dashboard (a basic order list and payout ledger is enough at launch)

**What they'll tolerate:**
- A manual or semi-manual onboarding process (Marcus Field walking them through setup in person) rather than a slick self-serve flow, as long as the commission and payout terms are real

### Where to Find Them

| Channel | Method | Est. Volume |
|---|---|---|
| Door-to-door restaurant scouting | Marcus Field visiting independent restaurants in Boise's core commercial corridors in person | 30-40 qualified conversations in first 60 days |
| Informal Boise restaurant owner network | Referrals from the first 3-5 signed restaurants to their peers | 10-15 warm referrals once initial cohort is live |
| Idaho Restaurant Association / local business associations | Direct outreach and info sessions | 10-20 contacts |

### Success Metric for Early Adopter Phase

**Target:** 40 active restaurants live in the Boise core within 90 days of launch
**Signal of success:** At least 60% of signed restaurants process 10+ orders in their first 30 days (proof the commission pitch converts to real usage, not just a signed agreement)

---

### Early Adopter Profile B: Customer Side (Demand)

**Segment:** Time-Starved Urban Professionals
**Persona:** Maya Torres

#### Characteristics

| Characteristic | Description |
|---|---|
| Pain intensity | Medium - frustration with fee stacking and buried discovery is real but not acute; customers have working alternatives (incumbent apps) today |
| Current situation | Already an active DoorDash/Uber Eats user 3-4x/week; switching cost is low (just downloading another app) but so is the incentive unless her favorite restaurants are present |
| Technical comfort | High - comfortable adopting new apps quickly, no onboarding friction expected |
| Decision speed | Fast - will try a new delivery app on a single friend recommendation or Instagram mention |
| Feedback willingness | Medium - will leave a review or complain in a local Facebook/Reddit group if something goes wrong, but won't proactively volunteer feedback |
| Referral potential | High if the restaurant selection includes spots she already wanted to try - she actively shares food discoveries on Instagram |

#### What Triggers Them to Try a New Solution

- Seeing a specific independent restaurant they already wanted to try listed on PureHunger and not (or poorly) on the incumbent apps
- A local social post or a friend's recommendation specifically calling out PureHunger's lower fees or "supports local restaurants" framing
- A bad-enough experience on an incumbent app (late delivery, favorite restaurant delisted) creating a moment of active dissatisfaction

#### What They Need from Us (Day 1)

**Must have:**
- At least a handful of restaurants she actually recognizes and wants, visible without digging
- A delivery fee that is genuinely flat and visible before checkout, with no late-stage fee surprises

**Nice to have (but OK to lack at launch):**
- Loyalty/rewards program (explicitly post-MVP per product scope)
- Scheduled/future ordering (explicitly post-MVP)

**What they'll tolerate:**
- A smaller overall restaurant catalog than DoorDash/Uber Eats, as long as the specific independents she cares about are there and delivery is reliable

### Where to Find Them

| Channel | Method | Est. Volume |
|---|---|---|
| Restaurant-side cross-promotion | Table tents / receipt inserts at the first 40 signed restaurants directing dine-in customers to order via PureHunger next time | 300-500 initial installs `[ASSUMED]` |
| Local Instagram / Boise neighborhood social channels | Targeted local ads emphasizing "support local restaurants, lower fees" framing | 150-250 installs `[ASSUMED]` |
| Word of mouth from early restaurant partners' existing customer base | Restaurant owners directly telling regulars about the switch | 50-100 installs `[ASSUMED]` |

### Success Metric for Early Adopter Phase

**Target:** 500 households complete a first order within 90 days of launch
**Signal of success:** Weekly Active Ordering Households (North Star Metric) reaches 150+ by day 90, with 2nd-order retention within 21 days ≥ 35% of first-time orderers (per Activation/Retention targets in the product's AARRR framing)

---
**Čo si teraz má:** Kompletný obraz oboch strán trhu - kto sú early adopters na strane reštaurácií aj zákazníkov, čo ich presvedčí v deň 1, a kde presne ich hľadať v Boise.

**Ďalší krok:** `/jtbd-building` - formalizuje prečo (a za akých podmienok) Maya aj Daniel prejdú na PureHunger.

**Môžeš preskočiť ak:** Uprednostňuješ ísť rovno na `/pm-market-analysis`, keďže tento dokument už poskytol dostatočný segment/persona kontext pre trhovú analýzu paralelne.
