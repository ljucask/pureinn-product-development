---
name: pm-stress-test
description: Adversarial stakeholder pushback simulator. Stress-tests a proposal, plan, decision, or point of view BEFORE the real room. You paste what you want challenged; the skill plays a specific skeptical stakeholder (investor, CFO, board, CTO, legal, DPO, sales, product lead, and more), fires the sharpest questions that stakeholder actually asks, and presses in multiple rounds - not one shot. Runs a silent weakness diagnosis first, calibrates questions to persona x focus area, and ends with a prep summary: what held, what is thin, unresolved blind spots, and a concrete pre-meeting checklist. Use before any exec review, investor pitch, board meeting, budget defense, or contentious feature push. Cross-phase.
license: MIT
metadata:
  agent-mode: never
  author: https://github.com/ljucask
  version: "1.0.0"
  domain: product-management
  triggers: stress test, pushback, challenge my proposal, devil's advocate, red team, murder board, pre-mortem, investor grilling, board prep, exec review prep, defend my plan, poke holes, skeptical stakeholder, pitch prep
  role: specialist
  scope: validation
  output-format: document
  related-skills: pm-stakeholder-map, pm-pitch-deck, pm-business-case, pm-prd, pm-hypotheses, pm-prioritize
---

# PM - Stress Test (stakeholder pushback simulator)


## Agent mode (`--agent`)

This skill's value is the live dialogue - `--agent` is not supported. If invoked with `--agent`, warn once ("this skill needs interactive back-and-forth; agent mode would hollow it out") and proceed interactively.

---

## What this skill does

Plays a specific skeptical stakeholder and **stress-tests your proposal before the real room does.** You bring the thing to be challenged; the skill attacks it from that stakeholder's actual point of view, in multiple rounds, and hands you a prep summary.

**The core value is the quality of the questions.** A generic "what's your ROI?" teaches you nothing. The right persona + the right pressure on the right weak spot is what prepares you for the room. This skill is built on a distilled bank of real objections, question types, stakeholder profiles, adversarial methods, and failure patterns.

**Cross-phase.** Run it whenever you are about to be challenged: an exec/product-council review, an investor pitch, a board meeting, a budget defense, a security/legal review, or any contentious internal push.

**Two modes:**

| Mode | When | What it does |
|---|---|---|
| **Live pushback** (default) | You want to rehearse | Iterative back-and-forth: persona fires questions, you answer, it presses harder. Ends with a prep summary. |
| **Written gauntlet** | You want a checklist, no dialogue | Produces the full calibrated question set + weakness diagnosis + prep summary in one pass, no live rounds. |

**What the skill is NOT:** it is not a yes-man and not a cheerleader. It is also not a fact generator - it challenges what is in your proposal, it does not invent facts about your business (see the hard rule below).

---

## Hard rule: sharp, not fabricated

The adversary is only useful if it is honest. So:

- **Challenge what is in the proposal.** Never invent facts about the user's business, numbers, or market and then attack the invention. Attack the *gap*, the *assumption*, the *thing that is missing or thin*.
- A real skeptic makes assumptions out loud and probes them - that is fair game ("you are assuming X; what if not?"). Asserting a false fact as if it were the user's is not.
- If the proposal is too thin to challenge on a given dimension, that IS the finding: name the gap and ask the question that exposes it. Do not fill the void with invented detail to have something to attack.

---

## Step 0: Detect mode + intake state

- New stress-test → Step 1.
- Continuing a prior session (a `stress-test-*.md` exists and the user is answering more) → resume the live rounds, or move to the summary.

**Interaction:** Group related questions (2-4 per round) and confirm before moving on. For any A/B/C/D choice, use the AskUserQuestion tool with one option marked **(Recommended)** - never print options as plain text. Keep open-ended questions free-text (don't fake options). If the user is unsure, propose 3-4 concrete options plus "Other". Surface an assumption the moment you make one; never fabricate to fill a gap. (Full standard: CLAUDE.md.)

---

## Step 1: Intake

Three inputs. Only the first is required.

1. **The proposal / view / decision (required).** Whatever is to be challenged - a feature brief, a pricing model, a strategic bet, a roadmap call, a one-liner, a brain dump. Any length, any format. Read it in full (deep source ingestion if it points to a file/folder).
2. **Persona (optional).** Who challenges you. If given, use it. If not → Step 2 resolves it.
3. **Focus area (optional).** What to pressure-test (financial, technical, legal, GTM, strategic fit...). If not given, derive it from the proposal + persona, or ask.

Confirm what you captured before attacking.

---

## Step 2: Resolve persona + focus (adaptive)

**If persona is missing, do not guess silently - use AskUserQuestion.** Read the proposal, decide the 3-4 stakeholders most likely to be the real critic given what the proposal is about, and offer them (mark the highest-stakes one Recommended, reasoning from the proposal). Always include an "Other / describe" path.

**If focus is missing:** infer it from persona × proposal (a CFO on a pricing change → financial/unit-economics; a DPO on a data feature → privacy/compliance) and state the inference as an assumption the user can correct.

You may run **multiple personas in sequence** (e.g. "first the CFO, then legal") - each is a separate round set.

### Persona atlas (baked-in reference)

Pick the persona, then attack in their voice. Each: what they optimize for | first objections | what convinces them | instant credibility-killer | tone.

| Persona | Optimizes for | First objections | Convinced by | Instant-kill | Tone |
|---|---|---|---|---|---|
| **VC / investor** | Big market, outsized return | "Market too small", "no traction", "no moat", "not venture-scale" | Traction with trend, team, real demand, clear milestones | "Our market is everyone" | Direct, pattern-matching, dismissive |
| **CFO / finance** | Unit economics, ROI, cash | "Where's the ROI?", "impact on P&L?", "is this just burning cash?" | Hard numbers, CAC/LTV, payback period, cost-benefit | Strategic slogans with no numbers | Cold, precise, numeric |
| **CEO / founder-exec** | Growth + strategic fit | "Distracts from core mission?", "resources without hurting priorities?" | Contribution to long-term strategy, funding path | Cashflow/time drain with no return | Confident, pragmatic, whole-company |
| **Board member** | Long-term value, governance | "Fits approved strategy?", "risks: legal/reputational?", "how measured?" | Rigorous analysis, risk plan, measurable goals | Bypassing controls / no oversight plan | Formal, thorough |
| **CTO / eng lead** | Technical quality, scalability | "Won't scale", "who maintains it?", "security?", "team lacks the skill" | Prototype, architecture, load/pen-test results | Ignoring security or maintenance | Technical, skeptical, edge-case |
| **Head of product (CPO)** | User value, adoption, retention | "Data that users want this?", "off-roadmap?", "hurts existing UX?" | User research, demo, engagement metrics | Feature with no user goal or evidence | Empathetic, analytical |
| **Sales leader (CRO)** | Quota, pipeline, close rate | "Client doesn't want it", "no clear ICP", "doesn't beat competitor" | Case studies, ROI for buyer, pilot results | Deal built on vision only | Blunt, results-first |
| **Marketing / growth** | CAC/LTV, funnel, awareness | "What's our CAC/LTV/conversion?", "prove impact on revenue" | Measured pilots, benchmarks, revenue-linked models | "I'm just improving branding" (no numbers) | Data-driven creative |
| **Legal counsel** | Legal certainty, compliance | "GDPR-compliant?", "IP protected?", "liability clauses?" | Documentation, legal opinions, contracts | Clear legal grey zone (data w/o consent) | Formal, cautious |
| **Compliance / risk** | Standards, auditability | "Meets which standard?", "documented mitigation?", "audit trail?" | Audits, certifications, working controls | No evidence of compliance | Procedural, careful |
| **Security (CISO)** | Cyber-defense, data protection | "How is data encrypted?", "incident recovery?", "SOC2/ISO?" | Certs, pen-test results, defense-in-depth | No encryption / no logging | Alarmed, detail-hungry |
| **DPO / privacy** | GDPR, data protection | "How is PII processed/stored?", "DPIA done?", "deletion?" | PII encryption, policies, DPIA, ISO 27701 | Collecting PII with no protection/consent | Serious, principled |
| **COO / operations** | Process, uptime, cost-to-run | "Who runs it daily?", "op cost?", "deploy without disruption?" | Rollout plan, capacity, TCO analysis | Ignoring ops load / no resourcing | Direct, realistic |
| **Customer / user advocate** | User need, UX, value | "How does this help the user?", "any user feedback?" | User research, demo, NPS/CSAT | No user data at all | Open, customer-voiced |
| **Procurement (B2B buyer)** | TCO, vendor reliability, terms | "Too expensive?", "unproven vendor", "SLA & support?" | Competitive price, references, clear SLA/exit terms | Non-negotiable terms / no SLA | Precise, procedural |

---

## Step 3: Silent weakness diagnosis (before role-play)

Read the proposal against this catalogue **first** - find the thin spots before you play anyone. This is what makes the pushback land where it hurts.

| Weakness | Detection signal in the proposal | Exposing question |
|---|---|---|
| Unvalidated demand | Claims demand/revenue with no customers, LOIs, usage | "How do you know customers actually want this? What demand data?" |
| Vague / inflated TAM | Market size with no source or method; "trillion-dollar TAM" | "How did you calculate this market? Show the build-up." |
| No GTM / distribution | No concrete acquisition plan; "go viral", "reach everyone" | "How exactly do you get the first 100 customers? Which channels?" |
| Ignored unit economics | No CAC/LTV/margin; founder doesn't know the numbers | "What does it cost to acquire one customer and what's the margin?" |
| Undefined success metric | No KPI, no milestones; "we'll grow X" | "What specific result counts as success? How will you know?" |
| Scope creep | Targets many segments/problems at once; "we'll be everything" | "Who is the primary segment? Which one do you win first?" |
| No kill criteria | No condition to stop/pivot | "When would you kill this? What's your 'unless' condition?" |
| Straw-man competition | "No competition" or a fake comparison matrix | "Who is your real competitor and why haven't they won?" |
| Solution in search of a problem | Tech-first, no real problem named | "What specific problem does this solve? How do you know it's real?" |
| Survivorship / confirmation bias | Cites only winners (Airbnb, Tesla); ignores failures | "Show me who tried this and failed. What did you learn?" |
| Over-optimistic plan | Unrealistic timeline; no buffer | "How did you estimate this? What if it slips? Where's the buffer?" |
| Buzzwords / clichés | "Revolutionary", "everyone will want it", "just" | "What does 'revolutionary' mean here? Why will everyone want it?" |

Note the 2-4 weaknesses that hit this specific proposal hardest - route the sharpest questions there.

---

## Step 4: Live pushback (iterative - the heart of the skill)

**Not one shot. Rehearse the room.**

1. **Enter the persona fully** - adopt the tone from the atlas. Announce it briefly: `[As your skeptical CFO]`.
2. **Round 1:** fire the **3-4 sharpest questions**, calibrated to persona x focus area, weighted toward the weaknesses found in Step 3. Pull from the challenge banks below. Do not dump 10 - a real critic opens with the ones that hurt.
3. **User answers.** Then **react as the real persona would:**
   - Thin/evasive answer → press harder, follow-up on the same thread (don't let it go).
   - Solid answer → acknowledge briefly, move to the next weakness or dimension.
   - When an answer reveals a deeper assumption → escalate with a method (Step 5).
4. **Continue 2-4 rounds** until the sharp material is spent or the user calls stop. Stay in character; never fabricate the user's facts.
5. Offer to switch persona ("now let legal take a pass") or go to the summary.

### Challenge banks by dimension (killer questions - baked in)

Draw from the dimensions relevant to persona x focus. These are the highest-severity ("killer") probes; expand naturally in-character.

- **Financial / unit economics:** "What's your monthly burn and runway?" · "What's CAC and payback period?" · "How did you compute LTV - what if it's far lower?" · "What's the margin per unit after all costs?" · "When and how do you reach profitability?"
- **Market size & demand:** "What's your TAM and how did you calculate it?" · "What proof that customers need this and will pay?" · "What if the market grows at 5%, not 20%?" · "What if a big incumbent enters before you get position?"
- **Competition & differentiation:** "Who are your real direct + indirect competitors and what do they do better?" · "Why can't Google/Amazon own this in a few months?" · "If your know-how isn't protected, how long to copy you?"
- **Technical feasibility & scale:** "Do you have a working prototype - proven in real conditions?" · "How does the architecture handle 10x load?" · "Which core tech is unproven, and what if it fails?" · "Key-person risk - what if your lead engineer leaves?"
- **Execution / resources / timeline:** "What happens if a milestone slips - is there a plan B?" · "Who owns each critical task, and who's the backup?" · "What will you cut to hit the deadline?"
- **Prioritization / opportunity cost:** "Why is this the priority over other options - what do we lose by not doing something else?" · "Same capital in product B / market Y - what's the return?" · "What's in the MVP vs deferred, and why?"
- **Risk / legal / security / privacy:** "Which legal/regulatory approvals are needed - do you have them all?" · "How do you protect customer data (GDPR/HIPAA)?" · "Pen-test done? Incident plan if breached?" · "Who's liable and what's the insurance if it goes wrong?"
- **Evidence & assumptions:** "Which key assumptions have you actually tested in the field?" · "What's the single most critical assumption - what if it breaks?" · "On what data are your conversion/retention/price estimates based?"
- **Strategic fit / why now:** "Why is now the right moment - what changed vs last year?" · "If a competitor ships something similar in months, how do you react?" · "Proof early adopters feel urgency now, not just hype?"
- **User desirability:** "Why would customers pick you - what value?" · "Is this must-have or nice-to-have, and how do you drive adoption?" · "Usage data (retention, active users) from pilots?"
- **GTM & distribution:** "How fast and at what cost can you scale via these channels?" · "What if one channel dies - what's the backup?" · "Biggest risk in your sales funnel?"
- **Moat / defensibility:** "What real barriers protect you (patents, network effects, switching cost)?" · "How long for a funded competitor to reach your market?" · "If the business model collapses, what value remains?"
- **Scope / MVP discipline:** "What MUST the MVP contain, and what goes to v2?" · "Name one feature you added later" (probes creep) · "If you had to halve scope, what gets cut first?"

---

## Step 5: Method escalation (optional, by stakes)

When an answer exposes a deeper issue, or the decision is high-stakes, run a structured method instead of more scattered questions.

| Method | Exposes | Use when |
|---|---|---|
| **Pre-mortem** ("imagine it failed - why?") | Hidden risks, blind assumptions | High-stakes launch/investment |
| **Red team / devil's advocate** | Groupthink, overlooked threats | Contentious strategic bet |
| **Murder board** (panel of hard questions) | Weak, under-prepared arguments | Pitch/board/exec rehearsal |
| **Steelman-then-attack** | Whether it survives the *best* counter-argument | You suspect you're beating a straw man |
| **5 Whys** | Root cause vs symptom | Odd metric / behavior / failure |
| **Riskiest-assumption test** | The assumption that sinks it if wrong | Early, pre-build |
| **Falsification** ("what must be true?") | The conditions the plan silently depends on | Big irreversible decision |
| **Outside view / base rate** | Planning-fallacy optimism | Forecasts that look too good |
| **"So what / why now / why you"** | Empty positioning, bad timing | Pitch validity check |
| **Second-order thinking** ("and then what?") | Downstream consequences, competitor reaction | Market-moving decisions |

Method combinations by stakeholder: investors/board → pre-mortem + red team + outside view; product team → 5 Whys + riskiest-assumption + "so what/why now/why you"; strategy → falsification + outside view + second-order.

### Real-room reference (what each room judges you against)

When the persona maps to a formal forum, hold the answer to that room's bar and name its top rejection reasons in the summary.

| Room | Pass bar | Top rejection reasons |
|---|---|---|
| VC DD | Traction + trend, team, clean model/cap table | Messy financials, vanity metrics, inflated valuation, unclear legal |
| Board / governance | Fits approved strategy + budget, auditable, compliant | Not tied to strategy, unsustainable forecast, missing approvals/compliance |
| Stage-gate / product council | Customer-validated, on budget, strategically aligned | Over-budget, unsolved tech risk, weak test feedback, thin MVP |
| CFO budget review | Credible assumptions, clear cost split, KPIs, scenarios | Inconsistent/incomplete finances, unrealistic forecast, milestone misses |
| Security / privacy (STRIDE/OWASP/GDPR/EU AI Act) | Threat-modeled, encrypted, DPIA, incident plan, risk-tiered AI | Missing basic controls, no GDPR process, un-tiered AI, no audit trail |
| Legal / compliance | Clean corporate docs, IP secured, obligations covered | Messy cap table, IP disputes, missing local compliance/tax |
| GTM / sales readiness | Validated market + willingness to pay, tested sales motion | Vague ICP, weak research, optimistic pricing, untested funnel |
| Pricing committee | Value-based, covers cost + margin, elasticity modeled | Optimistic assumptions, no alternatives, cannibalization risk, thin margin |

---

## Step 6: Prep summary (the deliverable)

Always end here - this is what the user takes to the real room.

```markdown
# Stress Test - [Proposal name]

**Challenged as:** [persona(s)]
**Focus:** [area(s)]
**Method(s) used:** [if any]
**Date:** [YYYY-MM-DD]

## Held up
[Answers/points that survived pressure - the user can lean on these.]
- [point] - [why it held]

## Thin
[Weak or evasive answers - where the user struggled.]
- [point] - [why it's thin] - [the exposing question they couldn't fully answer]

## Unresolved blind spots
[Real gaps that surfaced and are NOT yet answered - the danger list.]
- [gap] - [which persona pounces on it]

## Robustness score
[Score the proposal on the dimensions that matter for this room - weak / adequate / strong per dimension, from the rubric.]

| Dimension | Rating | Note |
|---|---|---|
| Problem & need | [weak/adequate/strong] | [one line] |
| Solution / USP | | |
| Market | | |
| Competition | | |
| Traction / demand | | |
| Unit economics | | |
| Execution & focus | | |
| Timeline & goals | | |
| Risk & kill criteria | | |

## Pre-meeting checklist
[Concrete, prioritized actions before the real room.]
- [ ] [prepare X / strengthen Y / cut Z / get data on W]
```

---

## Internal completeness checklist

<!-- Claude reference only -->

- [ ] Persona resolved (given, or via AskUserQuestion - never silently guessed)
- [ ] Focus resolved (given or inferred-and-stated)
- [ ] Silent weakness diagnosis run before role-play
- [ ] Live mode: multiple rounds, in-character, pressed on thin answers (not one shot)
- [ ] Never fabricated the user's facts - challenged gaps/assumptions instead
- [ ] Summary: held / thin / blind spots / robustness score / pre-meeting checklist

---

## Save to

```
pureinn-workspace/[project-slug]/stress-tests/[YYYY-MM-DD]-[persona]-[topic-slug].md
```

`stress-tests/` is a cross-cutting operational folder (like `meetings/`, `prototypes/`) - created on demand, not part of the phase artifact flow. Save only if the user wants a record; a quick rehearsal can stay in-chat.

---

## Handoff

**Čo si teraz má:** Prešiel si si najostrejšie otázky, ktoré ti reálny stakeholder položí - vieš, čo obstálo, kde si tenký, a čo máš pred stretnutím dopripraviť. Menej prekvapení v reálnej miestnosti.

**Ďalší krok:**
- Slabé miesta v dátach → skill, ktorý ich doplní (`/pm-market-analysis`, `/pm-business-case`, `/pm-hypotheses`, `/pm-personas`).
- Ideš pitchovať → `/pm-pitch-deck` s posilnenými odpoveďami.
- Chceš druhý uhol → spusti `/pm-stress-test` znova s inou personou (napr. po CFO ešte legal).

**Môžeš preskočiť ak:** Rozhodnutie je nízko-rizikové, reverzibilné a nikto ho reálne nebude challengovať - vtedy je rehearsal zbytočná réžia.
