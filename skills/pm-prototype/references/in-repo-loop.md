# pm-prototype - In-repo loop reference

> Reference for `skills/pm-prototype/SKILL.md`. The path where the prototype is built here, by a coding agent, rather than handed to an external tool. Read it when Step 3b routes to the in-repo path.

This path has no moment of handoff. There is no brief to compile and send - there is a running thing you iterate against. That difference is why it needs its own reference rather than a variation on the external one.

**Where it lives.** The prototype folder was created at Step 3b, before this path started - `references/prototype-folder.md`. The harness and the artifact go in its `build/`, except for Evolutionary code, which goes on a branch in the real repo (see the last section). Nothing here creates a folder; if there isn't one, Step 3b was skipped and the decisions it records were never made.

---

## The harness shell

**The artifact is a pure product surface. Everything else lives around it and switches off.**

Anything added inside the product UI changes the experience being tested - and an explanation of a prototype convention ("the state shown is after 14 sessions") is not a property of the product at all. So the scaffolding is a shell the artifact sits inside:

```
┌─ harness shell - never part of the product ────────────────┐
│  Prototype - not a live service     [desktop│tablet│mobile] │
│                                                             │
│   ┌──────────────────────┐                                  │
│   │                      │╌╌╌╌╌ "state shown is after 14    │
│   │      the artifact    │       sessions"            [×]   │
│   │   (pure product UI,  │                                  │
│   │    nothing added)    │╌╌╌╌╌ "voting is local, no        │
│   │                      │       backend"             [×]   │
│   └──────────────────────┘                                  │
│                                                             │
│  states: empty│full│error│unauth    variants    time ⟷      │
└─────────────────────────────────────────────────────────────┘
```

The shell is what gets shared, so the boundary travels with the artifact without touching the UI. The one loss is a screenshot cropped to the inner frame - a nameable limit, not a reason to pollute the product surface.

**Everything in the shell toggles off in one action** - the annotation layer as a whole, individual annotations, comments, connector lines, and the shell chrome itself. A reviewer must be able to see the artifact exactly as a user would, immediately.

---

## The contract

Any harness must provide these, whatever the stack. A kit satisfies the contract for standalone HTML/CSS/JS; inside an existing repo or a published artifact the agent builds to the same contract in that stack.

**The reference implementation is in `scaffold/`** - copy `harness.html` and `harness-client.js` byte-for-byte, edit only `harness.config.js`. See `scaffold/README.md`. It must be served, not opened as `file://`.

It also carries a handful of things the contract does not require but a reviewer expects: a **device mockup** (off by default - it is presentation, and a usability test does not want it), a **share link** that restores screen, state, variant, time, device and mockup in one go, a **PNG export** of the current screen that never includes the annotation layer, an **alignment grid**, a **side-by-side** view of the same screen at three widths, and a **presentation mode**. Treat them as conveniences, not contract items: a harness built in another stack is complete without them.

Two of those are worth a sentence, because they are easy to build wrongly:

- **Side by side** must render each frame at its **real width** and scale it down. Shrinking one iframe to a narrow box shows the same layout smaller; it does not fire the artifact's own media queries, which is the entire question being asked.
- **Presentation** may drive the artifact, but it must not **invent input**. Advancing screens, sweeping time and scrolling are the shell asking for things the artifact already does. A click belongs in a declared tour, ringed before it fires - a demo that improvises interaction shows an audience behaviour the prototype was never claimed to have. Show a **pointer travelling to the target** before it fires: a click with no visible approach reads as a glitch rather than as someone using the thing.

### 1. State switcher

Four states, each reachable in **one action**:

| State | Why it is mandatory |
|---|---|
| **Empty** | Pre-filled demo data conceals the null state - a documented, repeated failure. The first-run experience is usually the least designed and the most decisive |
| **Populated** | The normal case |
| **Error** | What the product does when something fails, which is where trust is won or lost |
| **Unauthorised** | What a viewer without permission sees. Routinely skipped, and routinely the thing that breaks in production |

Deliberate empty states are content, not blanks: a first-ever session with its seed row reads differently from an empty grid.

### 2. Fixtures

- **In their own editable file**, reusable across prototypes and across variants.
- **Plausible for this audience** - domain terminology, realistic lengths, real state relationships. Never lorem ipsum on a task path: when meaning is under test, meaningless copy invalidates the test.
- **Time-relative, never dated.** Compute from now (`the next Wednesday at 20:00`), never a hardcoded date. A prototype that has visibly rotted between the build and the showing discredits itself for free.
- **Cover the unbounded cases** - the long name, the 200-item list, the message thread that never ends, the input that overflows. Decide per element whether it truncates or wraps; long Slovak and German strings break chips and fixed columns first.

### 3. Time

A **scrubber, not a timer.** Reason, and it is the deciding one: a reviewer goes through the prototype alone and without narration. An autonomous transition on a timer is missed, and seen a second time only after a reload. A scrubber makes a forty-minute session arc replayable in ten seconds, in either direction, at the reviewer's pace.

It is also visibly a demo control, which is honest.

**Declared per screen, never globally.** Time means a different thing on each one - minutes since an order here, days into a subscription there - so one scale across both measures nothing. A screen declares its own range, the label the reviewer reads, and **what moving it actually demonstrates here**; a screen with no time dimension simply has no scrubber. That explanation belongs in the shell beside the control. Putting it on the screen would add an element to the product surface and shift the layout being tested.

### 4. Variant switcher

Named variants, switchable side by side. **Not optional when the prototype exists to choose a direction:** a single committed option produces inflated ratings and near-zero rejection - in the controlled study, none of 36 participants rejected the single design, while 3 of 12 rejected an alternative when shown three. If the prototype answers "which direction", it must carry more than one.

When the prototype is an answer rather than a choice - a commissioned assignment, a decided direction - one variant is correct and the switcher stays empty.

### 5. Device switcher

Viewport presets, at minimum mobile / tablet / desktop. **The change should be a movement, not a cut** - watching the frame travel between widths reads as one artifact at another size, where a jump cut reads as a different screen and the reviewer loses what they were looking at. Not cosmetic: it is the instrument that catches what the research says breaks first - long labels in chips and fixed columns, dense layouts in narrow viewports, and anything that assumes two dimensions at 400% zoom.

### 6. Annotation layer

One geometry - an **anchor to an element**, a **visible connector**, a body of text - carrying **three intents that must not look alike**:

| Intent | Written by | What it is for |
|---|---|---|
| **Disclosure** | the author | the element is invented and someone could act on it with no way to verify it. This one carries the honesty contract |
| **Convention** | the author | explains the *prototype*, not the product - "this is the state after 14 sessions" |
| **Comment** | a reviewer | a remark left where it happened, at runtime |

Building three mechanisms would be duplicated work and three inconsistent surfaces. Letting them share a look is worse: a reviewer cannot tell an admission from a caption.

**A note anchors where the reviewer pointed, not at the element's edge.** They aim at a word; a pin parked at the bounding box points at the right thing in the wrong place. Store the position as a fraction of the element, so it survives re-layout.

**A disclosure note carries what the element would be in production**, not only what it is here. That pair is the contract - and it is what the disclosure screen is assembled from, so the same list is never written twice.

**Closing a note collapses it to its pin. It never deletes it.** If an admission could be dismissed for good, and that state travelled in a shared link, someone could hand on a screen where an invented number carries no label - the one failure this layer exists to prevent. The whole layer still switches off in one action, because a reviewer must be able to see the artifact exactly as a user would; that is a visible toggle, and it is not carried in a shared link.

**What earns an annotation** - the test is not "is it fake?" but **"could someone act on this, with no way to verify it?"**

| Annotate | Leave alone |
|---|---|
| An unverifiable claim someone would act on: a number, a generated or AI output, a result attributed to a system (score, match, recommendation), a connection claim | Fakeness that is obvious or inconsequential: invented names, avatars, titles, a scripted navigation path |

**Comments have to get back, and without a backend nothing is automatic.** They live in that reviewer's own browser and reach the author only when the reviewer sends them, which makes the prompt to do so part of the instrument rather than a button they might find: the task stated before they start, a send control that is always visible and counts what is waiting, and one nudge after the first comment. Where a run cannot depend on that - several reviewers, one pass - an endpoint removes the dependency, and that is the only reason to introduce one.

That comments are per viewer is not a limitation to work around. An async test with real users **requires** commenters who cannot see each other; the sample is contaminated the moment the second person reads the first.

**One exception, where it goes inside the artifact:** when the artifact will travel **without the shell** - a screenshot cropped into a deck - and the element carries a decision. Then provenance is baked into the element's own label: *"Projected - illustrative"* in the chart title, because that is what survives a crop.

### 6b. The screen list

Whatever picks between screens must carry **a sentence per screen**, not only a name. A reviewer who has to work out what "02 Detail" means navigates by trial, and the first casualty is the order the showing was meant to follow - which `showing.md` treats as the thing that decides how the session goes.

### 7. Event log

Local, exportable, no telemetry. Records what was clicked, in what order, where the session stalled, what was never reached.

**Prototype events never go into production analytics** - a separate store or a local file. An event-name prefix alone does not prevent contamination.

Behaviour is the higher-weight evidence, but it does not stand alone: pair the log with observation notes and the participant's own explanation. An acceptance event with no note makes a failed review look successful.

### 8. Persistence - a feature to be tested, not a requirement to be met

The question is never "how do I store this" but **"does my hypothesis need this to survive?"**

| Level | Mechanism | Survives | Enough when |
|---|---|---|---|
| **In-session** | plain JS in memory | nothing | testing whether the interaction belongs there at all, and how it feels. **Covers most cases** |
| **Per-viewer** | localStorage | refresh, same browser | the flow spans a return within one person's session |
| **Shared** | artifact DB or a real backend | across people | the hypothesis is *about* several people, or about coming back |

Do not generalise this decision. A framework rule that pushes every prototype toward the heaviest option is how a three-hour prototype becomes a three-day one.

### 9. Disclosure

The shell carries the boundary line. Depth belongs in a **dedicated screen** - not scattered labels:

- **what the prototype proves / what it does not** - as a pair, both stated
- **element by element**: what it is in the prototype, what it would be in production
- **the classification** (below), and what it binds

**Assembled from the disclosure notes, not written separately.** Every one of them already states what the element is here and what it would be in production, which is exactly this screen's table. Maintaining the two by hand guarantees they diverge, and the version the reviewer reads is the one that will be out of date.

The effort answer to *"and how hard is it really"* belongs in the accompanying document, not on a product surface: it is the author's estimate, not a property of the product. Carry its basis (*"author's estimate, based on X"*) or a coarse band. When the basis cannot be written, "cannot estimate" is more honest than a grade someone will plan against.

---

## Rules for the loop itself

**Dead UI.** What looks interactive must respond. What cannot be made to move must not look interactive. This includes affordance, not just response: a horizontal rail that cannot be dragged on desktop reads as a static list.

**One vertical slice, not a miniature roadmap.** The reliable unit is one decision-carrying path across the necessary UI and logic. A broad request produces added random features while the requested ones stay broken.

**Annotate as you build, not afterwards.** The moment the agent creates an element that passes the "could someone act on this, with no way to verify it" test, it writes that element's disclosure note - what it is here, what it would be in production - in the same step. Left until the end, annotating becomes homework nobody does properly, and the disclosure screen is assembled from those notes anyway.

**Bound every agent request.** State the audience and the question; name exactly what to build; require bundled synthetic data visibly labelled as sample; **forbid the adjacent temptations explicitly** ("do not add login, live AI grouping, external services, real merging"); require labelled controls, keyboard access and visible focus; keep instrumentation local; ask for runnable files, startup instructions, checks performed, known limitations and assumptions; and end with **"stop after this interaction."**

Keep that scope visible during revisions. An agent's suggestion to add a dashboard is another product decision, not a free improvement.

**Test outside the generating agent.** Do not accept "implemented", "fixed" or "tests pass" as evidence. Run it, traverse the states in a browser, check the non-happy paths.

**Include one surface that tests the operating model**, not only the audience experience. The screen that answers *"does this still run when 200 arrive instead of 20"* is usually the one that decides whether the thing is a business, and a prototype made only of audience surfaces cannot expose it.

**Scope creep is generated, not merely requested.** Natural-language iteration has almost no transaction cost, so scope expands at generation speed while comprehension stays human-speed. New ideas go to a parking list, not into the current prompt.

**Separate prototype and production capabilities with actual permissions, not prose.** A conversational "do not change anything" is not a boundary. Disposable data, sandbox credentials, no production write access.

---

## When to stop, and when to restart

**Finished** when one of four things is true: the decision threshold is met and the team can act · the concept is falsified · the prototype cannot expose the uncertainty without production-grade work, so it is replaced by a spike, a concierge test or a real build · the budget is exhausted without a decision, **which is itself evidence that the chosen prototype was wrong**.

Visual polish, stakeholder enthusiasm and deployability are **not** finish criteria - unless the question under test is specifically visual preference, stakeholder communication or deployment feasibility.

**Restart** - no credible universal iteration count exists, so use the signals:

| Signal | What it means |
|---|---|
| The core data model no longer represents the decision | clean branch or rewrite |
| The same regression returns after two repair attempts | clean branch or rewrite |
| A new request changes the primary user, workflow or architectural boundary | clean branch or rewrite |
| The diff cannot be reviewed within the remaining budget | **stop prototyping, decide about productionisation** |
| Nobody can explain which paths are real and which are simulated | **stop prototyping, decide about productionisation** |
| It has real users or sensitive data without environment separation, access control, rollback and observability | **stop prototyping, decide about productionisation** |

---

## Classification decides where the code lives

> Full detail, plus kill and promotion, in `promotion.md`. Repeated here because it governs how the loop is run, not only what happens afterwards.

Made **before the first line of code**, because it sets the quality bar:

| Classification | Meaning | Where the code lives |
|---|---|---|
| **Disposable** | proof only, never merged | `build/` in the prototype folder |
| **Reference** | binding for flow, states and measurement, not architecture - engineering reimplements, but must not have to guess what should happen | `build/` in the prototype folder |
| **Evolutionary** | deliberately may reach production | **the real repo, on a branch** - repo rules, security, tests and review from the first line. The prototype folder holds the spec and a pointer |

The dangerous middle is *throwaway quality with evolutionary expectations*. Evolutionary code inside a prototype folder sits outside repo rules, which defeats the classification.

---

When the loop reaches one of its finish conditions, return to `SKILL.md` and run **Step 7 (Write the prototype reference back)**, then **Step 8 (Result mode)** once there is a result to record.
