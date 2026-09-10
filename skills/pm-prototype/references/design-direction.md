# pm-prototype - Design direction

> Reference for `skills/pm-prototype/SKILL.md`. Read it at **Step 3b**, after the audience is known and before anything visual is generated. Applies to both paths - an external tool needs the direction in its brief just as much as a coding agent does.

Skipping this does not produce "no direction". It produces the **default** one, and the default is recognisable.

---

## 1. First question: inherit, own, or evolve

Three relations to the product's existing design, and they lead to completely different work:

| Choice | Meaning | Where the design comes from |
|---|---|---|
| **Inherit** | it should look like the product already does | the design-context sources in `pureinn-variables.md` - codebase tokens, `figma_project_url`, `live_product_url` |
| **Own** | deliberately its own look - a new product, a separate brand, or a direction the current one cannot carry | decided here, then `design/` in the prototype folder |
| **Evolve** | the existing design as the base, testing a shift away from it | inherit as the base, and record the delta as **the thing being tested** |

Ask with **AskUserQuestion**. Recommend `inherit` whenever a product already exists and the prototype is not about how it looks - it is the cheapest and it keeps the test on the question that was actually asked.

**Evolve is not a compromise between the other two.** When the visual direction *is* the hypothesis, it belongs in `hypotheses.md` with a threshold, not only in `design/`. A shift in direction that nobody wrote down as a claim cannot be supported or refuted; it can only be argued about.

**Inherit needs a source.** If `repo.present` is `none` and no Figma exists and there is no live product to look at, "inherit" has nothing to inherit from - say so and treat it as `own`.

---

## 2. When it is "own" with nothing to go on

Four directions cover the space. Not a style taxonomy - they are separated by **what the interface treats as its primary material**, which is what actually changes how it is built and what it can carry.

| Direction | Primary material | Optimises for | Recognisable as | Cost | Forgiveness |
|---|---|---|---|---|---|
| **Fast and precise** | records, states, commands, metrics | repeated expert operation | Linear, Raycast, Stripe Dashboard, Grafana | 4/5 | medium-low |
| **Calm and clear** | prose, blocks, forms, simple lists | reading, composing, completing | Notion, Craft, Basecamp, GOV.UK | 2/5 | high |
| **Friendly and guided** | steps, prompts, feedback, progress | confidence and continued participation | Duolingo, Monzo, Headspace, TurboTax | 5/5 | low |
| **Visual and immersive** | images, covers, maps, collections | browsing, taste, discovery | Spotify, Airbnb, Pinterest, AllTrails | 5/5 | very low |

**Classify the surface being designed, not the company.** Notion has dense database views; Spotify has utilitarian settings.

**Not separate directions - modifiers that any of the four can wear:** glassmorphism, Liquid Glass, neumorphism, claymorphism, bento, brutalism, minimalism, dark mode, "AI interface".

### Each one's characteristic failure

| Direction | How it fails |
|---|---|
| Fast and precise | **false precision** - the interface implies a mature data model and reliable operational states that do not exist |
| Calm and clear | **absence mistaken for restraint** - removing decoration does not create hierarchy |
| Friendly and guided | **surface friendliness without interaction care** - cheerful colour cannot repair confusing questions or missing undo |
| Visual and immersive | **content quality mistaken for interface quality** - the demo succeeds because the sample images are unusually good |

### Default

**Calm and clear**, for an early prototype where visual emotion is not what is being tested. It is the most forgiving at low effort and the least likely to imply capabilities the product does not have. Deviate deliberately, not by momentum.

---

## 3. How to put the choice to someone

Never four unrelated homepages. The **same representative task, content and state**, in four small equally-finished frames, ordered least to most expressive. Each with:

- two screens, not one hero image
- one normal state and one edge state
- a one-line signal: clarity, control, encouragement or discovery
- a one-line cost warning
- one "not this" exemplar, to fix the boundary

Then ask **recognition and rejection**, never style vocabulary:

> Ktorej z nich má byť produkt najbližšie po desiatich sekundách - a ktorej sa **rozhodne** podobať nemá?

Follow-ups worth asking:

1. Čo má produkt signalizovať ako prvé - **prehľadnosť, kontrolu, povzbudenie, alebo objavovanie**?
2. Ktorá možnosť obstojí aj v najmenej pôvabnom reálnom stave - prázdne dáta, chyba, dlhý slovenský popisok, malý telefón?
3. Aký dôkaz od prototypu chceme - záujem investora, dokončenie úlohy, technický súhlas, alebo emocionálnu reakciu?

**Do not ask "which do you like".** Preference without a product job produces a mood-board vote, and a mood-board vote cannot be tested.

Record three things: the **closest**, the **rejected**, and the intended signal. That is enough to write a usable brief and enough to tell later whether the built thing honoured it.

---

## 4. Escaping the default look

There is a real convergent default, and "purple gradient plus Inter" is only its old form. The 2026 clusters are warm cream with serif and terracotta, near-black with an acid accent, identical rounded cards, all-caps eyebrow labels, monospace metadata, repeated fade-and-slide motion. The mechanism has a name - **distributional convergence**: high-probability patterns dominate whenever the prompt gives no direction.

The deeper tell is **context-independent composition**: the same hero, the same card pile, whether the product is a clinic tool or a music service.

**No robust study shows ordinary users can identify AI-generated design**, so "users can always tell" is not a defensible claim. But a prototypical design can score fine on first impression while failing distinctiveness and product fit - which is exactly what a prototype is supposed to expose.

**The minimum escape is not a new palette:**

1. **One direction and one rejection**, named. *"Like Linear and Stripe Dashboard; explicitly not Notion-like, not playful."*
2. **Name the primary material** - the records, documents, steps or media that dominate the screen - and supply representative content including one empty or failure state.
3. **Fix eight decisions before generation:** background, text, accent and semantic colours · type family and scale · spacing density · radius · border and shadow policy · motion policy · imagery policy · information hierarchy.
4. **Ban context-free component grammar.** Not every idea becomes an identical rounded card. Say which information is a row, a group, a panel, an inline note or a full surface, and why.
5. **Spend distinctiveness once.** One memorable element tied to the domain; the rest disciplined.

Steps 1-3 are the true minimum for a prototype. Steps 4-5 are what stop it regressing during generation.

---

## 5. What breaks first

Worth knowing before choosing, because these are the states a reviewer will find:

| Constraint | Breaks first in | Most resilient |
|---|---|---|
| Dark mode | Friendly and guided; any glass-heavy variant | Fast and precise, if contrast is tested rather than greyed down |
| WCAG contrast | glass and neumorphic treatments; text over images | Calm and clear, with solid surfaces |
| German and Finnish compounds | Fast and precise; Visual and immersive - fixed columns, chips, overlays | Calm and clear, with wrapping containers |
| Slovak diacritics and longer labels | Friendly and guided; Fast and precise - custom display fonts, fixed-height controls | Calm and clear, with tested line height |
| 400% zoom, narrow viewport | dense workstations, media overlays | linear, document-like or form-based flows |

The device switcher in the harness exists to catch exactly these - see `in-repo-loop.md` § 5.

---

## Where it goes

- **Inherit** → the design-context sources, named in `meta.md`. No `design/` folder.
- **Own or evolve** → `design/` in the prototype folder: the direction, the rejection, the eight decisions, and for evolve, the delta being tested.
- **External path** → the direction, the rejection and the eight decisions go into the brief's design guidance section. A tool given no direction returns the default, and one prompt of vagueness costs more to correct than it saved.
