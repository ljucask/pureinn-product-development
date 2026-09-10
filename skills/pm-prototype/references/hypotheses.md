# pm-prototype - Hypotheses, thresholds and verdicts

> Reference for `skills/pm-prototype/SKILL.md`. Read it at **Step 2** when writing the success criterion, and again at **Step 8** when recording what happened.

A prototype is not evidence about "the idea". It is an instrument that makes selected aspects of a possible product observable. A result is defensible only for the aspect the prototype represented, the behaviour the session actually elicited, and the people and context sampled.

Everything here exists to stop one failure: **a conclusion that outruns the behaviour the prototype made observable.**

---

## 1. What makes a hypothesis testable

"Users will like this" cannot fail in a disciplined way - "like" is undefined, the population is unspecified, there is no situation or alternative, and no observation would change the decision.

Seven elements, all required:

| Element | The question it answers | Weak | Testable |
|---|---|---|---|
| Evidence basis | why is this plausible *now*? | "we think…" | "because 9 of 12 recent support calls show…" |
| Population | for whom? | "users" | "first-time payroll admins in firms of 20-100" |
| Context and trigger | in what real situation? | "when using the app" | "when correcting a rejected submission before the daily cut-off" |
| Intervention | what changes? | "a better dashboard" | "a single exception queue ordered by deadline" |
| Observable outcome | what **behaviour** should change, not what opinion? | "they like it" | "they identify the next case and start it without help" |
| Comparator and time | compared with what, by when? | none | "versus the current list view, within two minutes" |
| Decision boundary | what result changes the decision? | "positive feedback" | "proceed only if ≥15 of 20 succeed unprompted with no critical error" |

### The formulation to write

It joins the four things separate templates leave apart - the causal claim, the instrument's validity, precommitted evidence, and an action:

> **Because** [dated evidence], **we believe** [intervention] for [population] in [context] will cause [observable outcome] relative to [baseline] within [time].
> **This prototype represents** [role / look and feel / implementation] and **does not represent** [excluded dimensions].
> **We will measure** [primary measure plus guardrails].
> **Kill / iterate / persevere criteria are** [precommitted thresholds, including the ambiguous zone].
> **A rival explanation would be** [alternative], which we will check by [control or second method].

On the branded formats - Hypothesis Kit, Lean UX statement, Test Card, riskiest-assumption test, assumption mapping - all carry **limited comparative evidence** that they produce better decisions. They are useful coordination devices; their effective parts are falsifiability, evidence provenance, risk prioritisation, construct-method fit, precommitted criteria and traceability to an action. Two findings matter more than any template: **probing drove learning, not the number of hypotheses written** (in a 152-team study, teams that wrote more hypotheses probed fewer of them), and real practice is not linear - a study of two startups found hypotheses no MVP ever tested, and MVPs unrelated to any hypothesis.

---

## 2. Thresholds, and why the famous one does not apply

**There is no universal prototype threshold.** "Five users" was a model for *finding interface problems* at an assumed problem-detectability rate - not a validity bar, not a way to estimate prevalence, compare designs, prove desirability or decide a market. Re-sampling from a 60-person study, five-person groups found between 55% and 99% of the known problems: the average reassures while any particular five-person study does not.

What perfect small-n results actually support:

| Result | An all-success run supports | An all-failure run supports |
|---|---|---|
| 5/5 | true success only above **55%** | only below 45% |
| 8/8 | above 69% | below 31% |
| 10/10 | above 74% | below 26% |
| 20/20 | above 86% | below 14% |

So five clean sessions do not establish 80% or 90% usability. Say the bound, not the percentage.

### Precommit an inconclusive zone

Without one, ordinary sampling noise gets forced into a political pass/fail. Write all three bands before the first session: what counts as clearing the bar, what counts as crossing the negative threshold, and the range in between that means *run it again* rather than *decide*.

### Defensible rules by purpose

| Purpose | Evidence and threshold logic | What it can decide |
|---|---|---|
| Find obvious interaction failures | 4-6 participants in one reasonably homogeneous segment, realistic tasks, no coaching; another batch after revision | iterate on observed high-severity failures. **Not** kill the idea, **not** estimate rates |
| Clear a usability bar | required completion rate, confidence, task, assistance rule and critical-error ceiling defined first; size the sample from that bar | persevere only if the interval clears the bar and guardrails pass |
| Concept desirability | target users, realistic trigger, a meaningful alternative; prefer an observable choice over approval | kill only when the core value assumption fails across credible representations - not because people were lukewarm |
| Willingness to pay | predefined price points and a consequential action: paid pilot, deposit, purchase, procurement step | a direction. Stated WTP alone decides nothing |
| High-risk or irreversible | multiple methods, independent analysis, representative coverage, replication, negative controls | requires convergent evidence. One prototype round is insufficient |

---

## 3. How prototype validation goes wrong

Each of these has documented evidence behind it, and each has a control.

| Failure | What the evidence shows | Control |
|---|---|---|
| **Demand effects** | participants were ~2.5x more likely to prefer the artifact they believed the interviewer built; labelling a keyboard "research-based" changed *objective typing speed* | separate maker from moderator where possible, neutral provenance, hide the intended direction, include an equivalent or negative control, ask afterwards what they thought was being tested |
| **Leading tasks and rescue** | moderators say and do materially different things; findings are actively produced, not simply found | state the user's goal and context, never the UI steps; predefine what counts as assistance; record first action and wrong turns separately from completion |
| **Testing usability when the risk is desirability** | a prototype answers about role, look-and-feel or implementation - not all three | write the risk type beside the hypothesis. For desirability, observe a choice against a real alternative |
| **Confirmation bias in analysis** | it measurably skews evidence evaluation; a decision matrix reduces it | precommit the primary outcome and the zones; log disconfirming evidence first; keep per-participant evidence |
| **Fidelity bias** | genuinely contested - studies manipulate different bundles of visual polish, functional depth, content realism and latency | match fidelity to the construct under test; document every mismatch with the intended product |
| **Costless, staged behaviour** | hypothetical WTP averaged **21% above real** across 77 studies | add realistic alternatives, opportunity cost and consequences before drawing a demand conclusion |

**In a solo build the maker is the moderator.** That makes demand effects the single most likely distortion here, not a theoretical one. Name it in the findings rather than pretending it was controlled.

**Engagement requires a choice not to engage.** If every participant was told to open the prototype and do three tasks, clicks and time are properties of the session, not evidence of adoption. Engagement becomes interpretable only when someone can refuse, choose an alternative, stop, return later, or spend something scarce.

**Synthetic users cannot validate a prototype.** Generic LLM personas are unsupported as primary evidence for usability, comprehension, trust, desirability, demand, prevalence or willingness to pay, and are especially weak for small-language and minority populations. They sharpen research - reviewing an interview guide, expanding objections, rehearsing moderation, generating test scenarios - they do not replace it. Store every such output as `SYNTHETIC HYPOTHESIS`, never as user evidence.

Four evidence classes, used throughout: `SOURCE FACT` · `EVIDENCE-BASED INFERENCE` · `SYNTHETIC HYPOTHESIS` · `UNKNOWN`.

---

## 4. The verdict - four states, never "validated"

| State | Meaning |
|---|---|
| **Supported within scope** | the precommitted observation cleared the bar, with stated uncertainty, for this population, context and represented dimension |
| **Refuted within scope** | the observation crossed the negative threshold and rival explanations were controlled |
| **Prototype or study failure** | the instrument did not expose the hypothesis credibly - **this must not update belief in the product** |
| **Inconclusive** | the evidence fell in the ambiguous zone, or was too weak for the decision |

The third is the one teams skip, and skipping it is how a broken test becomes a verdict on an idea.

### Which one it is - the failure tree

A negative result has five possible locations. Work down in order; stop at the first *no*.

| Question | If no | What failed | Next |
|---|---|---|---|
| Did they understand and inhabit the scenario? | scenario wrong or irrelevant | **study instrument** | rewrite or recruit correctly. **Do not update belief in the idea** |
| Could the prototype express the promised outcome without impossible gaps? | missing content, state, data, latency | **representation** | raise only the fidelity the hypothesis needs, repeat |
| Could someone who wanted the outcome operate it unassisted? | motivation present, operation fails | **interaction design** | iterate IA, flow, feedback, copy |
| Did they choose it over a credible current alternative, or incur a cost to continue? | understood and usable, no meaningful choice | **value proposition** | test another proposition; if it replicates under consequential conditions, kill or pivot |
| Can the product and business deliver it repeatedly at acceptable cost? | user value present, system cannot | **feasibility / viability** | change implementation or model, or stop |

Three comparisons isolate a prototype failure from an idea failure:

- **Representation check** - ask them to paraphrase the proposition afterwards. If they cannot, negative desirability evidence is uninterpretable.
- **Alternative embodiment** - test the same value through a materially different representation, such as a storyboard or a concierge enactment.
- **Current-alternative control** - let them use their existing workflow under the same scenario. Losing to a real alternative is far stronger evidence than a low rating in isolation.

### When a kill is defensible

All five must hold:

1. The failed assumption is **necessary** to the proposition, not one execution choice
2. The prototype faithfully represented the dimension under test
3. Participants, scenario, incentives and alternatives matched the intended context
4. The failure crossed a **precommitted** threshold and survived a rival-explanation check or a replication
5. The downside of a false kill is lower than the cost of more evidence

Before that point, **"iterate the representation" is usually the more accurate conclusion** than "the idea is wrong". And a well-run test that rejects a weak idea is a *successful experiment* - the experiment and the idea succeed or fail separately.

---

## 5. Four records, kept apart

Conflating these is how a demo becomes "validated". Each supports a different claim:

| Record | Example evidence | What it supports |
|---|---|---|
| **Implementation** | remove excludes the selected item; reset restores the fixture | the intended interaction works |
| **Usability** | a participant found the source detail and corrected the group unaided | it is understandable in this session |
| **Potential usefulness** | they connected it to a recent task and named where it fits | a reason to investigate workflow fit |
| **Commercial** | a relevant buyer committed to a scoped paid test | a limited WTP signal under those terms |

An agent clicking every button belongs in the implementation record. A tester following your instructions does not establish voluntary use.

**Preserve contradictory evidence.** If someone accepts a group without noticing the deliberately wrong item, the acceptance event alone makes a failed review look successful. Pair event logs with observation notes and the participant's own explanation.

**Numbers carry their provenance.** Every decision-relevant number is one of: **observed** (measured, named source and period) · **calculated** (visible method) · **projected** (explicit assumptions and horizon) · **target** (desired, not evidence) · **sample** (fictional). Put it in the title, not a legend - "Projected monthly saving - illustrative". Precision implies provenance; if the assumptions cannot be stated, use a range or omit the number.
