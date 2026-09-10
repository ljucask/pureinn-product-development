# pm-prototype - The way in

> Reference for `skills/pm-prototype/SKILL.md`. Read it at **Step 1** when what arrived is a raw idea rather than a scoped chunk of a product.

The rest of this skill assumes you already have something: a feature, an initiative, a brief. Reality often starts a step earlier - one thought, one sentence, a hunch. Getting from there to something buildable is a craft in its own right, and skipping it is why prototypes get built for problems nobody has stated.

**When to run this.** The scope answer at Step 1 is a sentence rather than a name; the user is describing a situation rather than pointing at an artifact; or a `/pureinn` run in `explore` mode routed here. When the scope is already a FEAT-ID or a named initiative, skip this file entirely.

**No canvas reliably turns an unformed thought into a buildable concept**, and the strongest evidence attaches to none of the popular ones. A field experiment with 151 entrepreneurs found that adding an explicit **theory of value** to evidence gathering produced better revenue and profit than evidence gathering alone. So the sequence below is short and load-bearing, not a set of templates to fill.

---

## The sequence

> **Incident → three rival frames → tiebreaker → theory of value → value-event sketches → killer assumption → test contract → code only if code is the right test.**

### 1. Raw capture, without completing it

The person speaks or writes freely. Return: their verbatim fragments · the tensions and contradictions in them · your interpretations **labelled as interpretations** · what is missing, left missing.

**Refuse to skip:** preserving the original wording, separated from your inference. Unusual language is where the idea actually lives, and it is the first thing normalisation destroys.

### 2. The nearest concrete episode

"What is the last real situation that made you think about this?" Then follow it through actor, trigger, current behaviour, workaround, cost and frequency.

If there is no real episode, ask for the closest analogous one and **label it an analogy, not evidence**.

**Refuse to skip:** the current alternative. "Do nothing" is an alternative and must be described operationally - without it, value is measured against nothing.

### 3. Three rival frames, before any category

Generate three that differ by **actor, causal mechanism or desired progress** - not by feature set. At least one in which software is not the main intervention.

Design fixation is measured, not folklore: exposure to one example demonstrably narrows what gets generated afterwards. Three rivals is the countermeasure.

**Refuse to skip:** genuine divergence before selection. The first coherent frame is not automatically the right one.

### 4. Forced choice, and the tiebreaker

Compare the frames pairwise. Construct a pair where both options are attractive but optimise different criteria - speed vs assurance, automation vs control, a broad audience vs a sharp first use case.

Ask: *"If you could only protect one for the first test, which one?"* Then: **"What made that the tiebreaker?"**

The criterion matters more than the choice.

**Refuse to skip:** human ownership of the criterion. You can expose the trade-off; you cannot decide what matters.

### 5. Theory of value

The causal conjecture, with links that can fail independently:

> In situation **S**, actor **A** experiences **mechanism M**. If intervention **X** changes **M**, the actor will change behaviour **B**, producing outcome **O**, because **reason R**.

Add only the business fields needed to expose value creation, delivery and capture: beneficiary · buyer or approver · current alternative · delivery dependency · economic logic · the one critical constraint.

**Refuse to skip:** the *because*. A benefit without a mechanism is a wish.

### 6. The value event, and three sketches

Define the smallest moment where the actor **experiences** the promised change - not "which feature is the MVP" but "what observable event would make them feel it".

Then three rough end-to-end sequences that reach it by **different mechanisms**. One should be manual or concierge where that is feasible at all.

A useful sketch is not a homepage. It is three to seven frames: the triggering situation → the actor's first meaningful action → the system's response → the value event → the next consequence.

**Refuse to skip:** the complete path to value. A disconnected screen is not a concept.

### 7. The killer assumption

List the load-bearing beliefs across desirability, usability, feasibility, viability and any safety or compliance dimension. Score evidence **only by linked observations or sources**. Pick the highest-importance, lowest-evidence one.

**Refuse to skip:** provenance. Conviction, model agreement and a completed template are not evidence.

### 8. The test contract, then the medium

State: what must be learned · what will be observed · what result means proceed, revise or stop · which test gives the most information for the least commitment · **why code is or is not necessary**.

---

## The threshold before building

All seven, or the concept is not ready:

1. **Situation** - one specific actor and triggering context
2. **Progress and current alternative** - the blocked outcome, and what happens today
3. **Causal theory** - intervention, mechanism, behaviour change, outcome, linked
4. **Value event** - the smallest end-to-end moment, drawable or enactable
5. **Business and operating boundary** - beneficiary, payer or approver, delivery owner, one load-bearing constraint
6. **Killer assumption** - named, with an evidence state
7. **Test contract** - the next observation, the decision threshold, the resulting action

**Unknowns are acceptable. Unmarked unknowns are not.**

### And then the decision rule

> Code only if **a working interaction is the cheapest credible test of the killer assumption**, at the fidelity that test requires.

If the riskiest belief is that the problem exists at all, an incident interview, an observation, a fake door or a commitment test is usually cheaper and more discriminating than code. If money, PII, safety, regulation or an irreversible state transition is involved, the risk boundary must be explicit before the prototype touches real data or users.

Say this out loud when it applies. *"The cheapest test of your riskiest belief is not a prototype"* is a valid and useful outcome of this skill.

---

## Eleven things this sequence must refuse to skip

Protections against predictable reasoning errors, not documents:

1. A concrete actor and situation - otherwise the frame stays rhetorical
2. The current alternative - otherwise value is measured against nothing
3. At least three rival framings - otherwise the first articulation becomes the solution
4. A causal theory of value - otherwise experiments become disconnected activity
5. An explicit **human** tiebreaker - otherwise the model or the workshop mechanics choose the product
6. Evidence labels on every load-bearing claim - otherwise a complete artifact creates false confidence
7. One killer assumption - otherwise you produce a backlog of doubts and learn nothing decisive
8. A falsifier and a decision rule - otherwise every result can be narrated as validation
9. A complete, smallest value event - otherwise the prototype tests screen preference rather than product value
10. A code-versus-no-code decision - otherwise the presence of a coding agent makes implementation the default way of thinking
11. Risk boundaries for money, PII, safety, law or irreversible actions - otherwise a "prototype" can do real harm while still being treated as disposable

---

## Working as the partner, not the author

**Where an AI partner genuinely helps:** articulation, relentless contrast generation, memory and traceability of what was said and rejected, cheap functionalisation, gap detection.

**Where it flattens the idea.** The risk is not hallucination, it is **plausible normalisation** - replacing strange, incomplete or contradictory material with a recognisable SaaS pattern. Four independent studies converge: AI support raised average creativity while **reducing the diversity** of the idea pool; LLM product ideas scored higher on purchase intent but covered a narrower semantic space and were less novel; AI image support **increased fixation** on the first example.

So: generate many candidates **inside a human-defined problem space**. Do not be the author of that space, or the judge of what is meaningfully different.

**Do:**
- preserve the person's raw wording before rewriting anything
- mark every addition you inferred
- ask for episodes and contrasts before offering solutions
- produce three genuinely different frames and name the axis of difference
- separate divergent generation from convergent selection
- ask the person for the tiebreaker criterion
- keep rejected frames and the reason they were rejected
- generate low-fidelity alternatives before a polished interface
- ask what result would change their mind, before building

**Do not:**
- lead with a canvas or a PRFAQ template
- autocomplete unknown boxes
- show a polished prototype before the learning question is explicit
- pick the "best" problem on generic market plausibility
- evaluate your own ideas with the framing you used to generate them
- **relabel an assumption as customer evidence**
- **treat simulated users, AI personas or model agreement as demand evidence**

---

## Where the output goes

The concept produced here becomes the **scope** for Step 1 and the raw material for Step 2's intent gate. Carry forward, in the user's words wherever possible:

- the chosen frame, the tiebreaker criterion, and what would revive a rejected frame
- the theory of value
- the value event
- the killer assumption with its evidence state
- the test contract - which becomes the success criterion, so do not invent a second one

Then continue with Step 2. If the test contract concluded that code is not the right test, stop there and say so - the skill has done its job.
