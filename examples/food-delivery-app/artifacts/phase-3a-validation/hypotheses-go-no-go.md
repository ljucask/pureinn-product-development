# Hypothesis Register - PureHunger

> **Phase:** 3 - Define & Validation
> **Last updated:** 2025-12-08
> **Status:** 5 hypotheses / 4 confirmed / 0 rejected / 1 confirmed-with-caveat

---

## ICP Definition

Because PureHunger is a three-sided marketplace, the ICP that carries the highest business-model risk is the supply side: the platform does not exist without restaurants willing to accept the 12% commission model. Customer and courier hypotheses are tested as dependent - can we build a working marketplace around this restaurant - rather than independent ICPs.

**ICP:** Independent, single-location restaurant owners in mid-size US cities (100k-500k population) who have either (a) tried a major delivery platform for 6+ months and dropped it due to commission eating an already-thin food-cost margin, or (b) never joined a platform for the same reason, and who are still losing app-first customers as a result.

**Example:** Daniel Osei - owns a single West African restaurant in Boise, ID, 8 years in business, ran on a major platform for 18 months before dropping it because 27% commission turned a marginally profitable order into a loss on his cuisine's cost structure.

---

## Assumption Map

| Assumption | Type | Riskiest? | Why |
|---|---|---|---|
| Independent restaurants will name commission as a top unprompted pain and sign a lower-rate agreement quickly | Problem | Yes | The entire business model differentiator (12% vs. 25-30%) only matters if restaurant owners actually feel this pain acutely enough to switch, not just agree it's theoretically better |
| Restaurants are reachable and convertible via direct outreach without a paid acquisition channel | Customer | No | Affects CAC and go-to-market cost, but a slower/costlier channel is a solvable problem, not a fatal one |
| A meaningful number of restaurants will sign (not just express interest) before launch | Market | Yes | Signed commitment is the strongest signal that "I'd use a cheaper platform" is a real decision, not a polite answer to a founder they know |
| Customers in an underserved mid-size city will engage with a platform that promotes independent restaurants over chains | Customer | No | Demand-side engagement is necessary but recoverable through marketing iteration if initial signal is weak |
| Couriers will prefer daily payout and transparent per-delivery pay over incumbent weekly payout | Solution | No | Affects courier supply and retention but is a secondary lever - couriers can be recruited even without this preference being dominant, just at higher cost |

**Most dangerous assumption:** That restaurants will sign, not just agree in principle. A restaurant owner nodding along to "yes, 12% is better than 27%" in an interview is not the same as a restaurant owner willing to sign a Restaurant Partner Agreement and put their menu on a new, unproven platform. This was tested first, via HYP-001 (unprompted pain) and HYP-005 (signed commitment), before any customer- or courier-side spend.

---

## Hypothesis Register

| ID | Type | Hypothesis | Riskiest | Experiment | Success Criteria | Status | Result | Decision |
|---|---|---|---|---|---|---|---|---|
| HYP-001 | Problem | We believe independent restaurant owners in mid-size cities lose enough margin to commission that it ranks as a top-2 unprompted pain with their current or former delivery platform | Yes | Customer Interview (14 restaurant owners, Boise + Meridian + Nampa) | ≥7/14 name commission as top-2 pain unprompted | Complete | 12/14 named commission as #1 or #2 unprompted; average historical/current commission paid: 27% | Confirmed |
| HYP-002 | Customer | We believe independent restaurant owners are reachable via direct outreach (no paid channel) and will engage within 2 weeks | No | Direct outreach (in-person + phone, 40 restaurants over 3 weeks) | ≥50% of contacted restaurants take a meeting; ≥15 sign a non-binding LOI within the outreach window | Complete | 31/40 took a meeting (78%); 22/31 signed a non-binding LOI within 2 weeks | Confirmed |
| HYP-003 | Customer | We believe customers in an underserved mid-size city will engage with a platform promoted on "real independent restaurants, no chain markup" | No | Landing Page + geo-fenced targeted ads ($850 spend, Boise zip codes) | ≥5% conversion from targeted visitors to email signup (≥100 visitor floor) | Complete | 6,400 targeted visitors, 512 signups (8.0% conversion); 380-respondent survey: 71% named thin selection/long wait times as top complaint with existing apps | Confirmed |
| HYP-004 | Solution | We believe couriers will prefer daily payout and transparent per-delivery pay enough to choose PureHunger over incumbent weekly-payout platforms | No | Customer Interview (11 part-time couriers currently working incumbent platforms) + courier waitlist smoke test (180 targeted ad clicks) | ≥7/10 interviewees confirm daily payout as "very appealing"; ≥15% waitlist conversion (≥10 interview floor) | Complete | 9/11 said daily payout was "very appealing" or "a dealbreaker in our favor" vs. weekly; waitlist conversion 47/180 (26%) | Confirmed - caveat: interview count (11) barely clears the 10-interview floor; treat as directionally strong, not conclusive |
| HYP-005 | Market | We believe at least 25 independent restaurants in the Boise metro area will sign a Restaurant Partner Agreement (12% commission, no upfront fee) within a 60-day pre-launch window | Yes | Pre-commitment campaign - signed Restaurant Partner Agreement (converting HYP-002 LOIs + referral outreach) | ≥25 signed Restaurant Partner Agreements within 60 days | Complete | 34 restaurants signed within 47 days (22 from converted LOIs + 12 from owner-to-owner referrals) | Confirmed |

---

## Experiment Plans

### [HYP-001] - Restaurant commission pain

**Experiment type:** Customer Interview
**What we're testing:** Whether commission is genuinely a top-tier pain for independent restaurant owners, not just a cost they've made peace with.
**Method:** In-person and phone interviews, no pitch until the last 5 minutes. Structured around past behavior ("walk me through your experience with [platform]"), not hypothetical reaction to PureHunger.
**ICP targeting:** Independent, single-location restaurant owners in Boise, Meridian, and Nampa, sourced via the Boise Independent Restaurant Association member list and Marcus Field's existing restaurant-industry contacts.
**Duration:** 3 weeks, 14 completed interviews.
**Budget:** Time only.

**Success criteria (defined before running):**
- Quantitative: ≥7/14 (50%) name commission as a top-2 unprompted pain
- Qualitative: Interviewees describe specific dollar or margin impact, not just general dissatisfaction

**Signals to watch for:**
- Positive: Unprompted mention of specific commission percentages, stories of dropping a platform, mental math about margin per order
- Negative: Vague dissatisfaction without specifics, or commission framed as "just the cost of doing business" with no appetite to switch

**Interview approach:**
- "Walk me through your experience with [the platform you used or considered]."
- "What was the most frustrating part of that relationship?"
- "Have you done anything to work around the commission cost - menu pricing, portion size, dropping the platform?"
- "What do you do now for delivery, if anything?"

**Result:** 12/14 named commission as #1 or #2 pain without prompting. 9/14 are currently off delivery platforms entirely, citing margin loss as the reason. Average commission rate paid (current or historical): 27%. Two interviewees described specific menu-price increases made solely to offset commission. **Confirmed.**

---

### [HYP-002] - Restaurant reachability

**Experiment type:** Direct Outreach + LOI
**What we're testing:** Whether independent restaurants can be acquired via low-cost direct outreach rather than requiring a paid acquisition channel.
**Method:** Marcus Field conducted in-person and phone outreach to 40 independent restaurants, presenting the 12% commission model and Restaurant Partner Agreement terms, asking for a non-binding letter of intent.
**ICP targeting:** Same list as HYP-001, expanded via referral.
**Duration:** 3 weeks.
**Budget:** Time only (no paid channel).

**Success criteria (defined before running):**
- Quantitative: ≥50% of contacted restaurants take a meeting; ≥15 sign a non-binding LOI within the 2-week outreach window

**Signals to watch for:**
- Positive: Restaurant owner asks detailed follow-up questions about payout timing, contract terms, menu upload process
- Negative: Polite interest with no follow-through, requests to "circle back next quarter"

**Result:** 31/40 restaurants took a meeting (78%). 22/31 signed a non-binding LOI within 2 weeks. **Confirmed** - direct outreach is a viable, low-cost acquisition channel for the supply side at this stage.

---

### [HYP-003] - Customer demand signal

**Experiment type:** Landing Page + Targeted Ads
**What we're testing:** Whether Boise customers underserved by incumbent apps will engage with a "real independent restaurants" positioning.
**Method:** Geo-fenced ads targeting Boise zip codes ($850 spend) driving to a landing page with a "Notify me at launch" fake-door CTA and a short post-signup survey.
**ICP targeting:** Boise residents, ages 25-45, targeted by zip code density rather than demographic profile.
**Duration:** 2 weeks.
**Budget:** $850.

**Success criteria (defined before running):**
- Quantitative: ≥5% conversion from targeted visitors to email signup, with a minimum floor of 100 targeted visitors

**Signals to watch for:**
- Positive: Survey respondents naming specific independent restaurants they wished were on delivery apps
- Negative: High click-through but low signup (curiosity without intent)

**Result:** 6,400 targeted visitors, 512 email signups (8.0% conversion, above the 5% threshold and well above the 100-visitor floor). Of 380 survey respondents, 71% named thin selection or long delivery times on existing apps as their top complaint. **Confirmed.**

---

### [HYP-004] - Courier payout preference

**Experiment type:** Customer Interview + Smoke Test
**What we're testing:** Whether daily payout and transparent per-delivery pay are a meaningful preference for couriers, not just a nice-to-have.
**Method:** Interviews with 11 part-time couriers currently working incumbent platforms in Boise, plus a courier recruitment landing page disclosing the $4 base + $1.25/mile + 100% tips, daily-payout terms.
**ICP targeting:** Active gig couriers in Boise, recruited via local gig-worker Facebook groups and referral from interviewees.
**Duration:** 2 weeks.
**Budget:** ~$150 in ad spend for the waitlist page.

**Success criteria (defined before running):**
- Quantitative: ≥7/10 interviewees confirm daily payout as "very appealing"; ≥15% waitlist conversion from targeted ad clicks (minimum 10-interview floor for the qualitative pass)

**Signals to watch for:**
- Positive: Spontaneous comparison to a specific bad experience with a payout-algorithm change on an incumbent platform
- Negative: Indifference to payout timing, interest driven only by per-mile rate

**Result:** 9/11 said daily payout was "very appealing" or explicitly "a dealbreaker in our favor" compared to weekly payout. Waitlist conversion: 47/180 targeted ad clicks (26%). **Confirmed, with a caveat:** 11 interviews barely clears the ≥10 floor required for a qualitative pass - treat this as a strong directional signal to monitor post-launch (courier retention, shift acceptance rate), not as conclusively settled.

---

### [HYP-005] - Pre-launch restaurant commitment

**Experiment type:** Pre-commitment (signed agreement)
**What we're testing:** Whether restaurant interest converts into actual signed commitment at a volume sufficient to de-risk the initial catalog.
**Method:** Converted HYP-002's 22 LOIs into signed Restaurant Partner Agreements, plus additional owner-to-owner referral outreach from the initial cohort.
**ICP targeting:** Same restaurant ICP, expanded via referral network from the first 22.
**Duration:** 60 days.
**Budget:** Time only.

**Success criteria (defined before running):**
- Financial/commitment: ≥25 signed Restaurant Partner Agreements within 60 days

**Signals to watch for:**
- Positive: Referral-driven signups (restaurants telling other restaurants) without additional outreach effort
- Negative: LOIs stalling at the signature stage, requests to renegotiate the 12% rate

**Result:** 34 restaurants signed within 47 days - 22 from converted LOIs, 12 from referrals with no direct outreach required. No requests to renegotiate the published 12% rate. **Confirmed**, exceeding target by 36%.

---

# Validation Go/No-Go - PureHunger

> **Date:** 2025-12-08
> **Phase:** 3 - Define & Validation exit
> **Hypotheses tested:** 5 total / 4 confirmed / 0 rejected / 1 confirmed-with-caveat

---

## Evidence Summary

| Hypothesis | Type | Result | Pre-defined criteria met? |
|---|---|---|---|
| HYP-001 - Restaurant commission pain | Problem | 12/14 named commission as top-2 pain unprompted; average 27% commission paid historically | Yes |
| HYP-002 - Restaurant reachability | Customer | 31/40 meetings, 22/31 signed LOI within 2 weeks | Yes |
| HYP-003 - Customer demand signal | Customer | 512 signups from 6,400 visitors (8.0%), 71% cite thin selection as top complaint | Yes |
| HYP-004 - Courier payout preference | Solution | 9/11 confirm daily payout preference; 26% waitlist conversion | Partial - directionally confirmed, sample size borderline |
| HYP-005 - Pre-launch restaurant commitment | Market | 34 signed Restaurant Partner Agreements within 47 days (target: 25) | Yes |

**Strongest signal:** 34 signed Restaurant Partner Agreements in 47 days, exceeding the 25-agreement target by 36% - this is a commitment-level signal (level 2 on the commitment strength scale: signed pilot agreement), not just expressed interest, and it validates the riskiest assumption in the register.

**Weakest signal:** Courier payout preference (HYP-004) rests on only 11 interviews, which clears the minimum floor but not by much. The direction is strong and consistent (9/11, plus 26% waitlist conversion well above typical cold-audience rates), but this should be treated as a working hypothesis to keep validating post-launch via courier retention and shift-acceptance data, not as closed.

---

## Decision

**Verdict: GO**

---

### GO - confirmed signals across problem, customer, and market

- **Problem hypothesis confirmed:** 12/14 restaurant owners named commission as a top-2 pain unprompted, with specific dollar/margin impact described, not vague dissatisfaction (HYP-001).
- **Customer hypothesis confirmed:** Both sides of the marketplace are reachable and responsive - restaurants via direct outreach (78% meeting rate, HYP-002) and customers via targeted ads (8.0% conversion, above the 5% floor, HYP-003).
- **Market hypothesis confirmed:** 34 signed Restaurant Partner Agreements within 47 days is a meaningful commitment signal (signed agreement, level 2 commitment strength) well above the pre-defined 25-agreement target (HYP-005).

Solution hypothesis (courier payout preference, HYP-004) remains partially open - directionally strong but based on a borderline sample size. This is acceptable to carry forward: it gets tested further with real operating data once dispatch is live in Phase 6, via courier retention and shift-acceptance-rate tracking.

→ **Proceed to Phase 3b (Commercial Definition).** Next: `/pm-kotler`, then `/pm-lean-canvas`, `/pm-kpis`, and `/pm-prd`.

---

## Notes for Phase 3b carry-forward

- The falsification condition surfaced in the Design Thinking synthesis (restaurants that reach 90 days with fewer than ~15 orders/week are not experiencing the promised economics regardless of commission rate) was **not** directly tested in this validation round - none of the 34 signed restaurants have live order volume yet, since this is a pre-launch commitment signal. This becomes the first thing to monitor operationally after launch, not a gap in this Go/No-Go.
- Courier payout preference (HYP-004) should be re-validated with real shift-acceptance and retention data within the first 60 days of live dispatch operation in Boise.
