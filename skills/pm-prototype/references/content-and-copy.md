# pm-prototype - Content, copy and language

> Reference for `skills/pm-prototype/SKILL.md`. Read it at **Step 3b**, alongside the design direction, and again whenever content is being written into the prototype.

**Content is part of the test stimulus, not decoration.** When words, values, dates, states or examples are needed to complete the task, placeholder text does not just look unfinished - it changes what the test measures.

A documented case: placeholder dates and requirements in a redesign recreated the exact comprehension problem the redesign existed to solve, and blocked task completion. The team expected to explain the placeholders during sessions; the placeholders had already done the damage.

---

## 1. Realistic does not mean final, and it does not mean real

The line is not *placeholder vs production-approved copy*. It is **non-semantic filler vs representative content**.

| Fine | Not fine |
|---|---|
| Fictional names, synthetic records, draft wording | Lorem ipsum or dummy strings **on a task path** |
| Content whose length, terminology, state relationships and consequences resemble the real service | Content that removes the semantic cues the live experience depends on |
| Deliberately fictional data, labelled as sample | Real customer data - usually unnecessary, and a privacy risk |

**Placeholder is acceptable** for private layout exploration, or for areas explicitly outside the session's scope. If it stays on screen, record that the corresponding content, comprehension and trust findings are invalid - do not let them into `findings.md` unqualified.

### Fixtures that carry their weight

- **Plausible for this audience** - domain terminology, realistic lengths, real state relationships.
- **Time-relative, never dated.** A prototype that has visibly rotted between the build and the showing discredits itself for free. The harness client provides `Harness.nextWeekday()` and `Harness.ago()` for this.
- **Cover the unbounded cases** - the long name, the 200-item list, the thread that never ends, the input that overflows. Decide per element whether it truncates or wraps.
- **Deliberate empty states are content, not blanks.** A first-ever session with its seed row reads completely differently from an empty grid, and the first-run experience is usually the least designed and the most decisive.

---

## 2. Language - ask, do not assume

**Ask which language the prototype is written in.** This is **not** `artifact_language`, which governs Pureinn's own artifacts. A workspace can write its artifacts in English while the prototype must speak Slovak, and the two settings answer different questions.

> V akom jazyku má byť prototyp napísaný? Nie artefakty Pureinnu - samotný prototyp, ktorý niekto uvidí.

What the evidence says:

- **Proficient non-native speakers found similar interaction problems** in English-language tests. So English *can* be acceptable when the decision is interaction-only and the users genuinely operate in English - with proficiency screening and an explicit scope limit on the conclusion.
- **Perceived usability was higher when a product was originally conceived in the participant's language** than when translated, even at high translation quality. Translation is not a neutral wrapper.
- **English-only testing is also a recruitment filter.** It selects for education and international exposure - that is, away from exactly the people whose language difficulties you were trying to find.

### When full localisation is not feasible

Translate **one complete critical journey** rather than scattering translated labels across an otherwise English prototype. In order: navigation, labels, controls, instructions, errors, confirmations, prices, dates, units, consent, and any trust-sensitive claim.

Keep the participant in one coherent language state. If the product is bilingual, make the switch functional and preserve what they entered.

Use a local-language moderator, or a briefed interpreter who is told not to solve the task or help.

**Code every observation by likely cause:** interaction · content · translation · moderator or interpreter effect · unknown. Never merge language-caused hesitation into general usability findings - it is the difference between "the flow is confusing" and "this word is wrong".

**Scope the conclusion honestly.** An English test validates the tested flow for the tested English-proficient segment. It cannot validate local-language comprehension, terminology, cultural meaning, or trust in the target market.

---

## 3. Writing the copy

Use whatever content or copywriting skills are available rather than improvising filler - copy carries a large share of a prototype's credibility, and improvised copy is where an otherwise careful prototype starts sounding generated.

**Numbers carry their provenance, in the title rather than a legend.** Every decision-relevant number is one of:

| | |
|---|---|
| **Observed** | measured, with a named source and period |
| **Calculated** | derived from observed inputs, method visible |
| **Projected** | estimated from explicit assumptions, with a horizon |
| **Target** | desired, and therefore not evidence |
| **Sample** | fictional, used to demonstrate layout or logic |

*"Projected monthly saving - illustrative"*, not *"Monthly saving"* with a footnote. **Precision implies provenance:** do not show a precise value just because it makes the prototype look operational. If the assumptions cannot be written down, use a range, an obviously fictional sample, or omit it.

---

## 4. What must not be inside the artifact

The prototype is a product surface. Editorial notes, admin explanations and statements of the obvious do not belong on it - they change the experience being tested, and they turn a product into a notebook.

*"This is the state after 14 sessions"* explains the **prototype**, not the product. It goes in the annotation layer beside the screen, or on the disclosure screen. Not in the UI.

**The one exception**, and the test for it is not "is it fake?" but:

> Could someone **act** on this, with **no way to verify** it?

| Label it | Leave it alone |
|---|---|
| An unverifiable claim someone would act on: a number, a generated or AI output, a result attributed to a system (score, match, recommendation), a connection claim | Fakeness that is obvious or inconsequential: invented names, avatars, titles, a scripted navigation path |

And when the artifact will travel **without its harness** - a screenshot cropped into a deck - provenance for a decision-bearing element gets baked into that element's own label, because that is what survives a crop.

Over-labelling ordinary controls is its own failure: it changes behaviour and buys nothing. Match the disclosure to the risk.
