# Problem Validation Summary - PureHunger

> **Phase:** 2 - Discovery (Convergence)
> **Date:** 2026-07-14
> **Input artifacts:** Market Analysis (`market-analysis.md` - TAM/SAM/SOM, Competitor Analysis, SWOT, Market Timing Rationale), Personas (`personas.md` - Customer Segments, Personas, Early Adopters Profile), JTBD Analysis (`jtbd-analysis.md`). Tech Feasibility and Domain Analysis were not run as formal artifacts for this discovery cycle - summarized below at founder-assessment level only (Track A/B marked Partial in the Track Completeness Check).

---

## Validation Verdict

**Overall verdict:** ⚠️ Partially validated

Both jobs (Maya's ordering-friction job and Daniel's delivery-revenue-trust job) are well-articulated and internally consistent across personas, JTBD, and market analysis - but the evidence base underneath them is asymmetric and thin. The restaurant-side pain has real, first-hand grounding (3 informal conversations with actual Boise restaurant owners, including a detailed first-hand account from Daniel Osei). The customer-side pain rests entirely on synthetic interviews calibrated against founder assumptions, with zero real conversations with a Maya-type customer to date. Proceeding to Phase 3a is justified to keep momentum on the restaurant-side thesis, which has the stronger evidence, but the customer-side thesis should not be treated as more than a well-reasoned hypothesis until real interviews close the gap.

---

## The Problem (Validated)

**Problem statement:**
Independent restaurants in mid-size US cities are stuck between two options that both cost them: pay 25-30% commission to a major delivery platform and erode already-thin margins, or opt out and lose the growing share of customers who default to app-based ordering. Customers in these same cities are simultaneously underserved by delivery apps optimized for dense urban cores - independent restaurants get buried under chain placement, delivery times outside downtown cores are unreliable, and checkout fees stack in ways that feel non-transparent.

**Evidence basis:**
- 3 informal, real conversations with independent Boise restaurant owners (including Daniel Osei) `[REAL VOC - n=3]`
- 14 synthetic customer interviews calibrated against published secondary-metro delivery-usage patterns `[SYNTHETIC INTERVIEW]`
- 1 bottom-up market sizing model built for this discovery cycle (`market-analysis.md`)
- 0 formal JTBD-specific interviews beyond what's captured above - the JTBD analysis is synthesized from the same persona inputs, not independently sourced

**Problem urgency:** High for restaurants, Medium for customers.
**Basis for urgency:** Restaurant-side urgency is grounded in a real, dated event - Daniel dropped a major platform 18 months ago after discovering negative per-order economics on dishes with already-thin margins, and 2 other Boise owners corroborated similar commission math independently. Customer-side urgency is more moderate: Maya's frustrations (buried discovery, fee stacking, unreliable delivery outside downtown) are real annoyances with a working incumbent alternative already in hand - she is not in acute pain, she has a recurring low-grade friction. This asymmetry matters for Phase 3a: the restaurant-side pitch can be validated faster and more confidently than the customer-side pitch.

---

## Validated Customer Pains

| Pain | Segment | Frequency | Intensity | Evidence |
|---|---|---|---|---|
| Commission math doesn't work on already-low-margin dishes | Restaurants | High - true of every order under the previous platform | High | `[REAL VOC - n=1, Daniel Osei, detailed dish-level account]`, corroborated `[REAL VOC - n=2]` |
| Independent restaurants buried under chain placement in incumbent discovery feeds | Customers | High - cited spontaneously, unprompted | High | Cited in 9 of 14 synthetic interviews `[SYNTHETIC INTERVIEW]` |
| Weekly payout cycle strains restaurant cash flow | Restaurants | Recurring (weekly) | Medium | `[REAL VOC - n=1]` |
| Checkout fee stacking feels non-transparent | Customers | High - every order | Medium-High | Cited in 8 of 14 synthetic interviews |
| Delivery time unreliability outside Boise's downtown core | Customers | Medium | Medium | Cited in 6 of 14 synthetic interviews |

**Top validated pain (focus for Phase 3a Design Thinking):** Commission math failing on already-thin restaurant margins. It has the strongest evidence (first-hand, dated, dish-level detail from a real conversation, independently corroborated by 2 other owners) and it is the pain that, if unaddressed, makes the entire supply side of the marketplace impossible - per `personas.md`'s segment prioritization, restaurant supply is the constrained resource this MVP must solve for first.

---

## Primary Customer (Validated)

**Segment:** Margin-Squeezed Independent Restaurants (supply side, primary for MVP sequencing) and Time-Starved Urban Professionals (demand side, secondary sequencing but equally required for the marketplace to function)
**Persona:** Daniel Osei (restaurant side); Maya Torres (customer side)
**Early adopter archetype:** On the restaurant side, an independent owner who has either already dropped a major platform over commission math or is actively losing app-first customers and can be won with a restaurant-specific, verifiable margin calculation plus a peer reference. On the customer side, an existing DoorDash/Uber Eats user who discovers a specific independent restaurant she already wanted to try newly available (and easy to find) on PureHunger.

---

## JTBD Core (Summary)

**The Job (Maya):**
When I'm leaving work exhausted with no dinner plan, I want to get a meal I like on the table with minimal decision effort, so I can protect the rest of my evening without feeling like I compromised on food or got fee-stacked.

**The Job (Daniel):**
When I see app-first customers I can't reach and I'm re-evaluating delivery after being burned once, I want a commission and payout structure that provably works on my actual menu math, so I can grow revenue instead of repeating a costly decision.

**Dominant force (what drives switching):**
- Maya - Push: independent restaurants buried under chain placement in incumbent apps. Pull: independent-first discovery feed + genuinely flat, visible fee.
- Daniel - Push: lost reach to app-first customers since dropping his previous platform. Pull: 12% commission that makes his own spreadsheet math work, plus daily payout matching his cash-flow rhythm.

Both jobs share a structural pattern worth flagging explicitly: neither persona is won by more features - Maya's habit and anxiety forces (app fatigue, small-catalog risk) and Daniel's habit and anxiety forces (owner-time cost, "burned once already") both dominate unless the product and go-to-market specifically reduce friction and rebuild trust, not just add pull-side benefits. This matches the JTBD skill's explicit warning against piling on features when the anxiety/habit side is strong - see `jtbd-analysis.md` Forces Diagrams for both personas.

---

## Market Opportunity (Summary)

| Metric | Value | Confidence |
|---|---|---|
| SAM | ~$636M GMV/year (15-city Mountain West/secondary-metro cohort) | Low-Med (bottom-up model, not independently verified) |
| SOM (Year 3) | ~$30.6M GMV/year (~$4.3M PureHunger revenue), Boise + 2 expansion markets | Low (channel-capacity-derived, still assumption-heavy) |
| Market timing | Strong | Grubhub's active secondary-metro pullback + visibly growing independent-restaurant commission frustration are both current, not anticipated, conditions - see `market-analysis.md` Market Timing Rationale |

**Competitive whitespace:** Independent-restaurant-first discovery and a commission structure that survives real restaurant margin math - neither DoorDash, Uber Eats, nor Grubhub is structurally positioned to match without restructuring their own economics; TableHop (illustrative smaller competitor) proves the commercial thesis attracts restaurants but has not proven the operational reliability (courier density, live tracking) needed to actually retain customers - this is the specific gap PureHunger's MVP scope (including FEAT-DEL-002, courier assignment + live tracking) is built to close.

---

## Technical Feasibility (Summary)

**Verdict:** 🟡 Feasible with risks

**Key risks:**
- Courier density and live-tracking reliability are unproven at Boise launch scale - this is the same operational gap that undermined TableHop's otherwise-similar commercial thesis (per `market-analysis.md` Competitive Risks)
- Split/staged payment capture (authorize at order placement, capture in full only on restaurant acceptance, per BR-PAY-001) requires a payment processor supporting this flow correctly under load - a solved problem industry-wide (e.g., Stripe Connect-style tokenized authorization/capture), but not yet implemented or load-tested for this product

**Critical blockers:** None identified at this stage, but this assessment is founder-level (Lena Vogt's architecture judgment), not a formal Tech Feasibility Report - `[ASSUMED - Track A not formally run for this discovery cycle]`. A formal `/pm-tech-feasibility` pass is recommended before Phase 3b locks technical scope commitments.

---

## Regulatory Summary

**Showstoppers:** None identified.
**Key compliance requirements to address:**
- Courier classification (1099 independent contractor) - state-level regulatory risk noted in `market-analysis.md` Enabling Conditions as a factor that could raise courier-side costs and compress the margin funding the 12% commission rate
- Courier tax documentation (1099-NEC, per BR-REG-002) for any courier paid over $600/year
- Payment data handling - card details must never be stored directly, only the payment processor's tokenized reference (per BR-GOV-001)

This is a founder-level regulatory scan, not a formal Domain Analysis - `[ASSUMED - Track B not formally run for this discovery cycle]`. A formal `/pm-domain-analysis` pass is recommended, particularly on courier classification, before Phase 4 domain modeling locks in courier employment assumptions.

---

## Assumptions Confirmed / Invalidated

| Assumption (from Phase 1) | Status | Finding |
|---|---|---|
| Independent restaurants will switch from a major platform for a lower commission alone | ⚠️ Partially confirmed | Daniel's real account confirms commission math is the primary driver, but his own Forces Diagram (`jtbd-analysis.md`) shows trust (being "burned once already") is an equally strong blocker - commission alone is necessary but not sufficient; a peer reference and verifiable dish-level math are required to convert |
| Customers in mid-size cities are meaningfully underserved by incumbent delivery apps | ⚠️ Partially confirmed | Synthetic interviews consistently surface buried discovery, fee stacking, and delivery unreliability, but this is not yet cross-checked against any real Maya-type customer conversation |
| Boise is a representative anchor launch market for the mid-size-city thesis | ✅ Confirmed (directionally) | Boise's independent-restaurant density, "buy local" culture, and Grubhub's local pullback all support the thesis per `market-analysis.md`, though city-specific restaurant counts remain estimated, not measured |

---

## Open Questions Going into Phase 3a

| Question | Priority | Who resolves |
|---|---|---|
| Does a real Maya-type customer confirm the buried-discovery and fee-stacking pains at the intensity the synthetic interviews suggest? | High | Human research - at least 8-10 real customer interviews before Phase 3a design decisions lock in the discovery-feed and fee-transparency bets |
| How many additional independent Boise restaurants (beyond the 3 informally consulted) confirm the same commission-math failure, and at what dish-level specificity? | High | Marcus Field's ongoing restaurant scouting conversations, tracked explicitly as real VOC going forward |
| Can courier density in Boise actually be built to the reliability level the value proposition depends on? | High | Phase 3a experiment design (`pm-hypotheses`) - this is the single highest-consequence unresolved risk per the SWOT Weaknesses/Threats analysis |
| What is the real (not estimated) count of independent, non-chain restaurants in the Boise MSA? | Medium | Direct count via Marcus Field's scouting list, cross-checked against Idaho Dept. of Labor data |
| Does courier classification regulatory risk materially threaten the 12% commission's underlying economics within the 18-24 month window identified in Market Timing Rationale? | Medium | Formal `/pm-domain-analysis` pass, given this was only founder-assessed here |

---

## Track Completeness Check

| Track | Status | Confidence | Notes |
|---|---|---|---|
| A: Tech Feasibility | ⚠️ Partial | Med | Founder-level assessment only (Lena Vogt's architecture judgment); no formal `/pm-tech-feasibility` artifact produced this cycle |
| B: Domain + Legal | ⚠️ Partial | Low-Med | Founder-level regulatory scan only; courier classification risk flagged but not formally researched via `/pm-domain-analysis` |
| C: Market Analysis | ✅ Complete | Med | Full Market Size, Competitor Analysis, SWOT, and Market Timing Rationale produced (`market-analysis.md`); figures are bottom-up modeled but not independently verified against primary sources |
| D: VOC + JTBD | ✅ Complete | Med (restaurant side) / Low (customer side) | Personas, Segments, Early Adopters Profile, and JTBD Analysis produced for both sides of the marketplace; restaurant-side evidence is real but low-N (n=3), customer-side evidence is entirely synthetic |

---

## Phase 2 → Phase 3a Recommendation

**Recommendation:** ⚠️ Proceed with gaps noted

**Reason:** The restaurant-side thesis (commission math + trust rebuilding) is grounded in real, if low-N, evidence and is strong enough to justify moving into Phase 3a hypothesis design specifically around restaurant acquisition and onboarding. The customer-side thesis is well-reasoned but entirely synthetic - it should be treated as the highest-priority validation target in Phase 3a's experiment design, not assumed true. Given that every Track D synthetic interview and every market-sizing figure traces back to the same founding team's domain knowledge (Sam Okonkwo, Lena Vogt, Marcus Field), the apparent convergence across personas, JTBD, and market analysis is not independent confirmation - it is one team's internally consistent hypothesis, articulated well across four documents. That consistency is useful for design work; it is not evidence.

**What Phase 3a must answer:**
1. Do real customer interviews (not synthetic) confirm the buried-discovery and fee-stacking pains at the intensity assumed, and does the independent-first feed concept actually change ordering behavior in a test?
2. Can courier density and delivery reliability be proven at a pilot scale in Boise before committing further restaurant or customer acquisition spend?
3. Does the 12%-commission, daily-payout pitch convert additional real restaurant owners beyond the 3 already informally consulted, at the rate the SOM model in `market-analysis.md` assumes (15-20 qualified restaurants/month via ground-game acquisition)?

---
**Čo si teraz má:** Phase 2 je formálne uzavretá - máš čestný, nie príliš optimistický verdikt (⚠️ Partially validated), s presne pomenovaným rozdielom medzi silne podloženou reštauračnou stranou a zatiaľ nepotvrdenou zákazníckou stranou trhu.

**Ďalší krok:** `/design-thinking` (Phase 3a) - postav Define/Ideate okolo top validovanej bolesti (commission math) a nastav Phase 3a experimenty presne na tri Open Questions vyššie (real customer interviews, courier density pilot, restaurant conversion rate).

**Môžeš preskočiť ak:** Nič - vzhľadom na ⚠️ verdikt a chýbajúce Track A/B artefakty by preskočenie `/design-thinking` a `/pm-hypotheses` znamenalo ísť do Phase 3b s nepotvrdenou zákazníckou stranou trhu, čo je presne to riziko, ktoré tento dokument identifikuje.
