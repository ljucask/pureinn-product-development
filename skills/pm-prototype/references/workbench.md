# pm-prototype - The workbench: build wide, cut down, hand over

> Reference for `skills/pm-prototype/SKILL.md`. Read it when Step 2 finds the purpose is **shaping and scoping** a product rather than testing one hypothesis. In-repo path only - it depends on the harness's view layer.

A test prototype answers one question and is then killed or promoted. A workbench prototype is something else: the place where a product is **thought out loud**, deliberately wider than what will ship first, and then cut down until what is left is the MVP. Meetings are run over it instead of over slides, because people decide better about a thing they can click.

The two are not the same instrument, and the rules that protect one damage the other:

| | Test | Workbench |
|---|---|---|
| Scope | one vertical slice | wide on purpose - nice-to-haves and rival versions included |
| Ends when | the hypothesis has a verdict | the phases are decided and the first one is handed over |
| Produces | a finding | a phased feature plan, and a clickable reference for whoever builds it |
| Evidence it yields | whatever the precommitted observation supports | **stakeholder alignment only** - see the last section |
| After promotion | the folder freezes | the folder stays live as the reference until its phases ship |

Say which one this is before building, and write it into `meta.md` as `**Purpose:** test | workbench`. A prototype that drifts from the first into the second without anyone saying so is the scope creep `in-repo-loop.md` warns about; one that was declared a workbench is doing its job.

---

## The three stages

### 1. Diverge

Build wide. Rival versions of a screen or an element, features nobody has costed, visual ideas with no regard for implementation. That is the point of the stage, not a lapse in it.

Two rules still hold, because they cost nothing now and are expensive to recover later:

- **Every feature is registered the moment it is built** - a row in `feature-plan-prt.md` with a `PRT-` ID, and its elements marked in the artifact (`data-feature="PRT-..."`). A feature that exists only as pixels cannot be hidden, phased, cut or handed over; it can only be forgotten.
- **Specification accumulates on the feature, in whatever form it arrives.** A sentence said in a meeting goes into that feature's `spec` as it was said. It is tidied at promotion, not before - asking for a clean spec during divergence stops people saying things.

Rival versions are declared as version groups, not as copies of a screen: the harness shows one option at a time and a reviewer switches between them in place.

### 2. Converge

The moment there are enough ideas and the question changes from *what could this be* to *what ships first*.

1. **Take the phases from the roadmap, do not invent a second set.** If the workspace has a roadmap, its phase names and order are the ones used. If it has none, ask for them - and say that `/pm-product-roadmap` is where they will have to live once this is promoted.
2. **Put every `built` feature in a phase, or cut it.** `cut` needs its reason. A feature left with no phase is undecided, and the harness lists it under *No phase yet* so the gap is visible.
3. **The feasibility pass is not optional.** Divergence ignored implementation cost by design, so before a feature is placed in the first phase, its card states what the production version is and what it costs (`prototype-folder.md` § a prototype feature card has to be buildable). Without this the MVP is chosen by what looks good in a meeting, which is the one failure this stage exists to prevent.
4. **Read the result in the harness.** *Phase: MVP* shows the product as it would first ship. Later phases are added one at a time, and a single feature can be switched in by hand to argue about it.

Phase is a decision the user makes. Offer the placement with a recommendation and the reasoning; never assign phases silently.

### 3. Hand over

What a developer gets: the feature map by phase, a card per feature, and the prototype itself - where each feature can be found, seen as each user type, and clicked through.

Promotion follows `promotion.md`, phase by phase rather than all at once: the first phase's `PRT-` cards become Feature Cards with real `FEAT-` IDs, each carrying `phase` and `promoted_from:`. Later phases stay `PRT-` until their turn.

**The source of truth for phase changes hands at promotion, once:**

| Feature is | Its phase lives in |
|---|---|
| still `PRT-` | `feature-plan-prt.md` |
| promoted to `FEAT-` | the Feature Card and `feature_list.md` |

The harness config is **generated from those, never edited as the origin**. A phase changed only in `harness.config.js` is a second truth, and the next generation overwrites it.

**Cards have to be reachable from where the harness is served.** The harness fetches a card relative to `harness.html`, and a server cannot hand out a file above its own root. Serve the prototype folder (so `build/harness.html` reaches `feature-cards/`), or generate the cards into `build/cards/`. A card that cannot be fetched shows only what the config carries, and says so.

After promotion the feature's entry in the config keeps its place and gains `card:` pointing at the Feature Card, so the prototype still opens the specification a developer should build from.

---

## Asked at the start, per project

Nothing in the view is universal. A workbench run opens by asking, and writes the answers into `meta.md`:

- **Who uses this product?** The user types become the roles. Offer candidates from what exists - personas, the user types in `pm-process-flows`, the actors on existing cards - and let the user correct them. No source at all: ask in plain text, then confirm the list. Never ship a default set of roles; "Admin / User" invented by the skill is a fabricated input.
- **What are the phases called, and in what order?** From the roadmap if there is one. Otherwise ask - two is enough to start (*first release*, *later*), and more can be added when the prototype converges.

A project with one user type declares no roles and the *User type* control does not appear. A prototype still diverging declares no phases yet. Both are normal.

## The view layer - what the config declares

Detail and examples in `scaffold/README.md` § The view. In short:

| Config | What it gives |
|---|---|
| `roles` | a *User type* switch. **Visual only** - it hides what that user type would not see and enforces nothing |
| `phases` | *Phase*, cumulative, in roadmap order |
| `features` | the register: `id`, `name`, `phase`, `status`, `desc`, `spec`, `roles`, `card`, and `on` for artifacts that cannot be edited |
| `feature:` on a screen | the feature is that whole screen - the screen panel dims it when it is out of the view |
| `versions` | named options of a screen or an element, one shown at a time |
| `view` | what a link opens on by default - usually `{ phase: '<first phase>' }` once converged |
| a `featureMap: true` screen | the register read as a plan, generated |

---

## What a workbench is not evidence for

A room agreeing over a prototype is **stakeholder alignment**. It is real and it is worth having, and it is not user evidence: nobody in the room chose the product over an alternative or paid anything to continue.

So a workbench records its decisions as decisions - who was in the room, what was placed in which phase and why - and never as a verdict in the four-state sense. If a feature's place in the MVP rests on a belief about users, that belief is a hypothesis: write it down and test it with a **test** prototype, or another method, before the phase is built.

---

## Taking over a prototype built elsewhere

When the prototype already exists - made in a design tool, by another team, before this skill was in use - Wrap mode puts the harness around it, and the workbench then needs the one thing that prototype never had: the register. Walk the screens, name the features, mark or select their elements, and write the rows. From there it is at stage 1 or 2 like any other.

How much of this can be automated depends on the form the prototype arrives in, and is not settled yet. Ask what was exported before promising anything.
