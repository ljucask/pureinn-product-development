# JTBD Analysis - PureHunger

> **Phase:** 2 - Discovery (Track D: VOC - Customer Discovery)
> **Date:** 2026-07-14
> **Primary personas:** Maya Torres (customer side) and Daniel Osei (restaurant side) - analyzed as two separate jobs, not averaged, because they hire PureHunger for structurally different reasons.
> **Data basis:** Synthesized from `personas.md` (3 informal real-VOC restaurant conversations `[REAL VOC - n=3]`, 14 synthetic customer interviews `[SYNTHETIC INTERVIEW]`, founder assumptions `[ASSUMED]`) - no new interviews conducted for this document.

---

## Job 1: Maya Torres - The Ordering Job

### The Core Job

**When** I'm leaving work exhausted on a weeknight with no dinner plan and no energy to cook or decide,
**I want to** get a meal I actually like on the table with almost no decision effort,
**So I can** reclaim the rest of my evening without feeling like I compromised on food quality or overpaid for the convenience.

**The job in plain language:**
Maya isn't hiring a delivery app to solve hunger - she's hiring it to protect her limited weeknight energy from one more decision. The real progress she's after is ending the workday and immediately removing "what's for dinner" from her mental load, while still feeling good about what she ate and what she supported. When the app fails at this (buried discovery, fee surprises, late delivery), it doesn't just annoy her - it puts the decision-fatigue burden right back on her.

**Frequency and context:** Near-daily consideration, 3-4x/week actual conversion into an order - almost always weeknights (Sun-Thu), almost always evenings (6-8 PM), almost always under real time/energy pressure rather than leisurely browsing. This is a recurring operational job, not an occasional one - which means reliability and speed compound in importance every single week, and one bad experience is weighted heavily because it happens so often.

---

## Job 2: Daniel Osei - The Delivery-Revenue Job

### The Core Job

**When** I see delivery-app ordering growing among the customers I want to keep, while my own margins are already thin,
**I want to** add delivery as a real revenue channel without repeating the mistake that cost me money last time,
**So I can** grow the business instead of quietly losing ground to competitors who are on delivery apps.

**The job in plain language:**
Daniel already tried the obvious answer (join a major platform) and it failed - not because delivery itself was a bad idea, but because the commission math made every order a net loss on his lower-margin dishes. His job now isn't "get on a delivery app" in the abstract - it's "find a delivery channel where the after-commission number actually holds up," because he's already been burned by one that didn't. This is fundamentally a trust-and-math job, not a discovery job.

**Frequency and context:** This is not a recurring operational job the way Maya's is - it's a periodic, high-stakes evaluation event. It gets triggered when the cost of staying off delivery apps becomes visible enough (a customer asking "are you on DoorDash?", a slow month, a competitor visibly gaining reach) that Daniel re-opens a decision he thought he'd already closed 18 months ago.

---

## Three Dimensions of the Job

| Persona | Dimension | The job | Why it matters |
|---|---|---|---|
| Maya | Functional | Get a specific meal delivered, on time, at a price she can predict before checkout | Practical outcome: dinner solved, budget not violated |
| Maya | Emotional | Feel like ordering delivery isn't a small daily defeat (guilt, annoyance at fees) | She wants convenience without the low-grade friction that currently taxes the experience |
| Maya | Social | Feel like she's supporting good local restaurants, not just feeding a chain-optimized algorithm | Identity signal - she screenshots and shares finds; being "the friend who knows the good spots" matters to her |
| Daniel | Functional | Generate incremental delivery revenue that survives commission and packaging cost | Practical outcome: the P&L has to work, dish by dish |
| Daniel | Emotional | Regain confidence that a delivery platform can be a partner, not an extractor | He was burned once; trust has to be rebuilt before he'll re-engage emotionally with delivery as a channel |
| Daniel | Social | Maintain standing among peer restaurant owners as someone who makes sound, disciplined business decisions | His informal owner network is a bigger influence on this decision than any vendor's marketing |

---

## Forces Diagram - Maya Torres

```
                    TOWARD NEW SOLUTION (PureHunger)
                           ↑
              PULL (attraction to new)
         ┌─────────────────────────────────────────┐
         │ Favorite/aspirational independent        │
         │ restaurants surfaced first, not buried   │
         │ Flat, visible $2.99 fee - no checkout     │
         │ surprises                                 │
         │ "Supporting local" identity payoff        │
         └─────────────────────────────────────────┘
                           ↑
PUSH ──────────────── DECISION ──────────────── ANXIETY
(away from incumbent)    POINT       (hesitation about switching)
         │                                     │
┌────────┴──────────────────┐         ┌────────┴──────────────────┐
│ Chain restaurants crowd    │         │ "What if my regular spots │
│ out independents in feed   │         │  aren't even on it yet?"  │
│ Fee stacking feels         │         │ "Is this just another app │
│ deceptive at checkout      │         │  I have to manage?"       │
│ Delivery time unreliable   │         │ Small-selection risk on a │
│ outside downtown core      │         │ new, unproven platform    │
└────────────────────────────┘         └────────────────────────────┘
                           ↓
              HABIT (inertia - staying with incumbent apps)
         ┌─────────────────────────────────────────┐
         │ DoorDash/Uber Eats already installed,    │
         │ payment method saved, zero setup friction│
         │ "Rotation" of 4-5 go-to restaurants       │
         │ already muscle-memory on existing apps    │
         │ Good-enough-most-of-the-time reliability  │
         └─────────────────────────────────────────┘
                    TOWARD STATUS QUO
```

### Forces Detail - Maya

**Push Forces**

| Force | Description | Intensity | Evidence |
|---|---|---|---|
| Buried discovery | Independent restaurants ranked below chains that pay for placement | High | Cited spontaneously in 9 of 14 synthetic interviews `[SYNTHETIC INTERVIEW]` |
| Fee stacking | Service fee + delivery fee + suggested tip compound at checkout, feels non-transparent | Med-High | Cited in 8 of 14 synthetic interviews |
| Delivery unreliability | Estimated delivery windows frequently miss outside downtown core | Med | Cited in 6 of 14 synthetic interviews |

**Dominant push force:** Buried discovery - the frustration that shows up most consistently and is most tied to the emotional "I know a better place exists and can't easily get to it" feeling.

**Pull Forces**

| Force | Description | What they imagine it will do |
|---|---|---|
| Independent-first feed | Restaurant discovery leads with local independents, not paid chain placement | Removes the "I have to already know the name to find it" tax |
| Flat, visible fee | $2.99 delivery fee shown up front, no stacking surprises | Restores a sense of pricing honesty and predictability |
| "Support local" framing | Marketing and product positioning around independent restaurants | Lets her feel good about a habit (frequent delivery ordering) she's privately a little guilty about |

**Dominant pull force:** Independent-first discovery - it directly answers her single most-cited frustration and reinforces the identity payoff she already values.

**Anxiety Forces**

| Force | Description | Mitigation in our product |
|---|---|---|
| "What if my regulars aren't on it yet?" | Fear of switching to a smaller catalog and losing access to her existing rotation | Restaurant-side onboarding sequenced ahead of customer marketing (see personas.md MVP sequencing); launch messaging names specific signed restaurants |
| "One more app to manage" | General app fatigue - another download, another account, another payment method | Fast, low-friction signup; social/Apple/Google sign-in; saved payment on first order |
| Small-selection risk | New, unproven platform might simply have fewer choices than DoorDash/Uber Eats | Be explicit in onboarding that catalog is smaller but curated - "fewer, better" as a stated positioning, not a hidden gap |

**Habit Forces**

| Force | Description | How to overcome |
|---|---|---|
| Incumbent apps already installed | DoorDash/Uber Eats have zero marginal setup cost for her next order | Cross-promotion at the point of dine-in (table tents, receipts) creates a lower-friction entry point than a cold app-store download |
| Rotation restaurants already bookmarked | 4-5 go-to spots are muscle memory on the existing apps | Prioritize onboarding restaurants she's likely already loyal to, not just any independent |
| "Good enough" reliability | Incumbent delivery times are inconsistent but rarely bad enough to trigger active complaint | Reliability has to be visibly *better*, not just "also fine," to justify switching cost |

---

## Switching Trigger - Maya

**The moment everything changed:**
Not a single dramatic event - a slow accumulation of "buried discovery" moments (scrolling past chains to find nothing new) combined with one specific trigger: seeing a restaurant she already wanted to try (via Instagram or a friend) listed on PureHunger and easy to find, when it was hard or impossible to surface on the incumbent apps.

**Examples of triggers in this market:**
- A friend shares a new local restaurant find and mentions it's on PureHunger
- A bad-enough incumbent-app experience (favorite restaurant delisted, late delivery) creates active dissatisfaction right when a PureHunger touchpoint (restaurant table tent, local ad) is visible

**Design implication:** Acquisition messaging and restaurant-side rollout should be sequenced together - don't market to Maya's segment generically ("lower fees!"); market a specific, recognizable restaurant she'd already want, and meet her at the exact moment she's looking for it.

---

## Job Stories (Maya)

### Primary Job Story

When I'm leaving work exhausted with no dinner plan,
I want to find a good independent restaurant and get food delivered reliably without checkout surprises,
So I can protect the rest of my evening without feeling like I compromised on food or got fee-stacked.

**Secondary job stories:**

| Situation | Motivation | Expected outcome |
|---|---|---|
| When a friend recommends a new local restaurant | I want to find it on the app immediately without hunting | I feel like I didn't miss out on a good discovery |
| When I'm deciding whether to order again | I want to see the same flat fee I saw last time | I trust the platform isn't nickel-and-diming me order to order |

---

## Forces Diagram - Daniel Osei

```
                    TOWARD NEW SOLUTION (PureHunger)
                           ↑
              PULL (attraction to new)
         ┌─────────────────────────────────────────┐
         │ 12% commission vs. 25-30% - the math      │
         │ actually works on his real dishes          │
         │ Daily payout matches his cash-flow rhythm  │
         │ Regains reach to app-first customers       │
         └─────────────────────────────────────────┘
                           ↑
PUSH ──────────────── DECISION ──────────────── ANXIETY
(away from status quo)   POINT       (hesitation about new platform)
         │                                     │
┌────────┴──────────────────┐         ┌────────┴──────────────────┐
│ Losing app-first customers │         │ "I've been burned before -│
│ who won't call to order    │         │  what if this is the same │
│ Slow revenue growth vs.    │         │  math trap again?"        │
│ competitors on delivery    │         │ Owner-time cost of setup  │
│ Direct customer asks "are  │         │ and managing a 3rd channel│
│ you on any app?"           │         │ Unproven, small platform  │
└────────────────────────────┘         │ risk - will it even last? │
                           ↓            └────────────────────────────┘
              HABIT (inertia - staying delivery-app-free)
         ┌─────────────────────────────────────────┐
         │ Dine-in + phone + word of mouth already   │
         │ "work" well enough to keep the doors open │
         │ No new vendor relationship to manage       │
         │ Avoids repeating a decision that already   │
         │ cost him once                              │
         └─────────────────────────────────────────┘
                    TOWARD STATUS QUO
```

### Forces Detail - Daniel

**Push Forces**

| Force | Description | Intensity | Evidence |
|---|---|---|---|
| Lost app-first customer reach | Customers who default to app ordering can't find him at all since he dropped the platform | High | `[REAL VOC - n=1, Daniel Osei]` |
| Growth gap vs. delivery-enabled competitors | Suspects competitors on delivery apps are pulling ahead in reach, though he lacks hard data to size it | Med | `[REAL VOC - n=1]`, corroborated informally `[REAL VOC - n=2, other Boise owners]` |
| Direct customer requests | Customers periodically ask if he's on a delivery app | Med | `[REAL VOC - n=1]` |

**Dominant push force:** Lost app-first customer reach - it's the most concrete, most frequently-felt cost, and the one most directly reversible by a working delivery channel.

**Pull Forces**

| Force | Description | What they imagine it will do |
|---|---|---|
| 12% commission | Commission rate low enough that his own spreadsheet math turns positive on the dishes that broke even before | Turns delivery from a margin risk back into real incremental revenue |
| Daily payout | Payout cycle matches his cash-flow rhythm rather than straining it | Removes the working-capital tax he carried under the previous platform's weekly cycle |
| Regained app-first reach | Becomes visible again to the growing app-ordering customer segment | Closes the reach gap he's been feeling but couldn't fix without a working delivery channel |

**Dominant pull force:** 12% commission - it is the single number that converts his own margin math from a rejection to a "worth trying," and it's the number he checks first, before anything else about the platform.

**Anxiety Forces**

| Force | Description | Mitigation in our product |
|---|---|---|
| "Burned once already" | Direct prior negative experience with a major platform's commission math | Show the after-commission number on his actual menu items before he signs, not a generic pitch deck |
| Owner-time cost | Fear that managing a third channel (on top of dine-in and phone) consumes time he doesn't have | Manual, founder-led onboarding (Marcus Field in person) rather than a self-serve flow that assumes spare owner-time |
| Unproven, small platform risk | PureHunger is new and unproven - "will this even still exist in a year?" | Peer reference from another signed Boise restaurant owner; transparent, direct communication from the founding team rather than a faceless platform |

**Habit Forces**

| Force | Description | How to overcome |
|---|---|---|
| "Works well enough" status quo | Dine-in + phone + word of mouth keeps the restaurant running, even if suboptimal | Make the lost-reach cost concrete and visible (e.g., estimate of nearby app-ordering household volume) rather than abstract |
| No new vendor relationship to manage | Avoiding a third channel avoids the operational overhead of managing it | Low-touch onboarding, single point of contact (Marcus Field), no new POS integration required at MVP |
| Avoiding repeat of a costly decision | Having been burned once, the safest choice psychologically is simply not deciding again | Peer proof point is more persuasive than any vendor claim - this is the single highest-leverage lever to overcome habit |

---

## Switching Trigger - Daniel

**The moment everything changed:**
Not a single event but a recurring one: a customer directly asking "are you on any delivery app?" often enough, combined with a slow sales month, that the cost of staying off delivery platforms becomes undeniable and Daniel re-opens a decision he considered closed.

**Examples of triggers in this market:**
- A specific customer request for delivery that Daniel has to turn away
- A visible slow period that prompts him to re-examine every possible revenue lever, including one he'd previously ruled out
- Direct outreach from Marcus Field with restaurant-specific margin math, rather than a generic sales pitch

**Design implication:** The sales motion (not just the product) has to lead with restaurant-specific commission math and a peer reference, because the switching trigger is fundamentally a trust-rebuilding event, not a feature-discovery event.

---

## Job Stories (Daniel)

### Primary Job Story

When I see app-first customers I can't reach and I'm re-evaluating delivery after being burned once,
I want a commission and payout structure that provably works on my actual menu math,
So I can grow revenue instead of repeating a decision that cost me money last time.

**Secondary job stories:**

| Situation | Motivation | Expected outcome |
|---|---|---|
| When a customer asks if I'm on a delivery app | I want to say yes without worrying the math will hurt me | I don't lose the sale or the trust of a customer who expected app ordering |
| When I check my monthly numbers | I want to see delivery revenue as a clean net-positive line, not a hidden loss | I can confidently keep the channel running instead of dropping it again |

---

## Key Insight for Product Design

**What the customer is really hiring our product for:**
Maya hires PureHunger to remove a recurring, high-frequency decision-fatigue moment while feeling good about what she chose. Daniel hires PureHunger to reverse a specific, previously-failed decision by proving - with his own numbers, not a pitch - that the math finally works. These are structurally different jobs (frequent/emotional vs. periodic/trust-and-math), and the product and go-to-market must serve both without collapsing them into one generic "delivery app" pitch.

**What this means for our MVP:**
The MVP ordering loop (browse → cart → checkout/pay → accept → deliver → rate) directly serves Maya's job only if restaurant discovery genuinely leads with independents and the fee is genuinely flat - a marketplace that looks like the incumbents with a lower number attached does not convert her. On the restaurant side, the MVP's value is 100% commission and payout terms - a merchant dashboard beyond a basic order list and payout ledger is not what converts Daniel; his own spreadsheet is what converts him, so the product must make the after-commission number easy for him to verify.

**What this means for our messaging:**
To Maya: lead with independent-restaurant discovery and fee transparency, not "cheaper than DoorDash" - she isn't price-shopping, she's frustration-avoiding. To Daniel and his segment: lead with the after-commission math on real dishes and a peer reference, never with "more visibility" - that claim is specifically discredited by his prior experience and will trigger, not resolve, his anxiety forces.

---
**Čo si teraz má:** Formálne JTBD s Forces Diagram pre obe strany trhu - vysvetľuje prečo (a za akých podmienok) Maya aj Daniel prejdú na PureHunger, a čo presne ich brzdí.

**Ďalší krok:** `/pm-market-analysis` - trhová veľkosť, konkurencia a timing pre Boise, doplní Track C pred konvergenciou v `/pm-problem-validation`.

**Môžeš preskočiť ak:** Trhová analýza už existuje a Track C je hotový - choď rovno na `/pm-problem-validation`.
