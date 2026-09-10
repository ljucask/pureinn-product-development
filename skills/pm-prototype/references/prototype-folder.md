# pm-prototype - The prototype folder

> Reference for `skills/pm-prototype/SKILL.md`. On the in-repo path, read it at **Step 3b** - the folder is created before the build, not after it - then again at **Step 7** (update) and **Step 8** (record the decision). The external path writes a spec file instead and does not use this.

A prototype gets its own folder, separate from the production registers. Not because separation is tidy, but because of what actually happens to prototypes: **most of them die, and that is their purpose.**

| Outcome | If it lived in the production artifacts | With its own folder |
|---|---|---|
| It dies (**the common case**) | clean-up: dead FEAT-IDs in the feature list, entities and rules that existed only for it, rows in the delivery plan | delete a folder |
| It survives (rarer) | free - just deepen it | transposition work |

Keeping it in the production registers optimises for the rarer outcome, and fills live registers - the source of truth for the build - with speculative entries. That is the exact drift `pm-audit` exists to catch.

---

## Shape

```
pureinn-workspace/[project-slug]/prototypes/[prototype-name]/
  meta.md                 what it is, the uncertainty, audience, classification,
                          targets:, decision state
  hypotheses.md           what we are here to prove
  findings.md             what held, what broke, what stayed open
  context/                thin Discovery/Define artifacts - ONLY when the global ones do not serve
                          personas.md · jtbd.md · voc.md · segments.md
  feature-plan-prt.md     PRT-[NAME]-001..N, one sentence of intent each
  feature-cards/          thin cards, same field names as production cards
  domain.md               ONLY when the prototype deliberately diverges
  rules.md                ONLY when it deliberately diverges
  design/                 ONLY when it has its own visual direction
  build/                  the prototype itself, or a pointer to the branch
```

Always at the **workspace root**, never nested under an initiative. A prototype often has no initiative yet - that is frequently why it exists - and moving it later when it acquires one is churn. The relationship is carried by `targets:`, not by the path.

`hypotheses.md` and `findings.md` are a pair. The first states what is to be proven, the second what came of it. **Without the second, a prototype is a demo.**

---

## The rule that keeps two truths out

**Reference by default. Local only on deliberate divergence.**

A local copy of a global rule with no divergence is not a "thin version" - it is a duplicate that will drift from the original within a month. So `domain.md`, `rules.md` and everything in `context/` exist **only when the prototype deliberately goes a different way**, and must then say *in what way*, not merely be an abridged copy.

A prototype that simply uses existing entities references them in `meta.md` and creates no local file.

The same test applies to `context/`: if the global personas serve, point at them. If the prototype explores a segment the global work never covered, a thin local file is right - and it carries its provenance, because context assembled from research is not the same evidence as context from customer interviews.

### Filling `context/` when the global artifacts do not serve

Three sources, and they combine rather than compete:

| Source | When |
|---|---|
| **Global artifacts** | they already answer it. Reference, never duplicate |
| **Targeted research in this session** | a narrow, specific gap. Run it scoped to one question at a time, in parallel where the questions are independent, each writing one file into `context/` |
| **External deep research** | the question deserves depth and time that an in-session pass cannot give |

The middle row is what stops the prototype track stalling or inventing: it can fill its own context gaps. Depth follows the audience row in `audience-depth.md`, not production depth - this is a prototype's context, not the product's.

**Every context file states where it came from and how strong that is**, using the four evidence classes from `hypotheses.md` § 3:

```markdown
**Provenance:** EVIDENCE-BASED INFERENCE - desk research, [sources], [date].
Not customer contact. Replace before any claim about this segment leaves the prototype.
```

A researched persona is `EVIDENCE-BASED INFERENCE`. An agent-generated one is `SYNTHETIC HYPOTHESIS` - **never** `SOURCE FACT`, even when it was grounded in a real description. A prototype built on the first and presented as the second is exactly the failure the evidence discipline exists to prevent, and `findings.md` inherits the weakness of whatever the conclusion rested on.

---

## meta.md

```markdown
# [Prototype name]

**Created:** [YYYY-MM-DD]
**Uncertainty:** [the one thing this exists to resolve]
**Audience:** [primary from Step 3b] · secondary: [others, whose needs yield]
**Path:** [in-repo | external tool]
**Classification:** [Disposable | Reference | Evolutionary]
**Decision:** open
**Stop condition:** [declared before starting - see below]

## targets

[What this prototype is about, so the relationship is explicit rather than implied]

- `FEAT-ORD-014` - prototyping a redesign of a feature already in the plan
- `domain/orders` - something in a domain area
- `OQ-12` / `BLK-3` - resolving an entry in the Open Questions Register
- `HYP-4` - testing a specific hypothesis
- persona / segment - exploring for a specific audience
- *(none)* - a net-new idea. It gets a production FEAT-ID only on promotion

## What it uses from the global artifacts

[Referenced, not copied. Name them. Anything NOT listed here and present as a
local file must state why it diverges.]

## What is deliberately simulated

[Pointer to the disclosure screen. This section is a summary, not a duplicate -
the screen is the artifact the reviewer actually sees.]
```

**The stop condition is declared before the work starts, not discovered.** Three usable forms, all more honest than a clock:

- **Evidence-based** (preferred): "this exists to answer these hypotheses. When they are answered - or it is clear they cannot be answered this way - we stop."
- **Iteration-based**: "three iterations without new information means stop."
- **Budget-based**: "one evening, one session." An intent, never a measurement.

---

## Decision state

`open` → one of `kill` · `persevere` · `partial`.

**Open is not a resting state.** A prototype that has been open for a long time with no decision is the failure mode this whole structure exists to prevent - a folder where nothing is dead and nothing is alive. When a run finds one, say so and ask for the decision.

Recording the outcome uses the four verdict states in `references/hypotheses.md` § 4. The verdict is what the evidence says; the decision is what you do about it. They are not the same field: *Refuted within scope* usually means kill, but *Prototype or study failure* means fix the instrument and re-run, and it must not be recorded as a kill.

---

## findings.md

Four records, kept apart, because each supports a different claim - implementation, usability, potential usefulness, commercial. Plus:

- **What we observed** - behaviour, not opinion
- **What we did not test** - the excluded dimensions from the hypothesis
- **Known distortions** - demand effects if the maker moderated, staged behaviour, the bound a small n actually supports
- **Contradictory evidence, preserved.** An acceptance event with no observation note makes a failed review look successful.

---

## Naming

`prototypes/[prototype-name]/` in kebab-case, named for what it explores rather than for a date or a version: `ama-lifecycle`, `pricing-tiers`, `dispatcher-assignment`. Feature IDs inside a prototype are `PRT-[NAME]-001` - deliberately not `FEAT-`, so a prototype ID can never be mistaken for a committed feature, and killing one leaves no hole in the production register.
