# Prototype harness - the kit

The reference implementation of the contract in [`../in-repo-loop.md`](../in-repo-loop.md), for a **standalone HTML/CSS/JS prototype**. Inside an existing repo or a published artifact, build to the same contract in that stack instead - the contract is the source of truth, this is one conforming implementation.

## Files

| File | Copy byte-for-byte | Edit per prototype |
|---|---|---|
| `harness.html` | yes - never re-author it | no |
| `harness-client.js` | yes | no |
| `harness.config.js` | as a starting point | **yes - this is the only one** |

Set `title` in the config: it names the prototype in the chrome and in the browser tab. It is the prototype's name, not the product's - *"AMA lifecycle v1"* rather than *"Acme"*.

Why byte-for-byte: the value is that the same keystroke hides the chrome and the same event format comes out of every prototype, so findings stay comparable. A harness re-invented per prototype has neither.

## Use

```bash
cp harness.html harness-client.js harness.config.js  <prototype>/build/
cd <prototype>/build && python3 -m http.server 8000
# open http://localhost:8000/harness.html
```

**It must be served, not opened as `file://`.** The artifact runs in an iframe so the device switcher triggers its real media queries - inside a plain container they respond to the window, not the container, and "mobile" would change nothing while appearing to work. Browsers block cross-document access for `file://` frames, so a local server is the price of that honesty.

Then in every prototype page:

```html
<script src="harness-client.js"></script>
<script>
  Harness.on('state',   render);                  // empty | full | error | unauth
  Harness.on('variant', applyVariant);            // only if the config declares variants
  Harness.on('time',    renderAtMinute);          // only if THIS screen declares time
  button.addEventListener('click', function () { Harness.log('act:click'); });
</script>
```

The artifact never depends on the harness. Open a page directly and it still runs - it simply has no state switching, no scrub and no event capture.

## What the client gives the artifact

| | |
|---|---|
| `Harness.on(kind, fn)` | subscribe to `state` / `variant` / `time`; fires immediately, so a late subscriber is never out of sync |
| `Harness.get(kind)` | current value |
| `Harness.log(name, detail)` | one event into the local log. Never a network call |
| `Harness.nextWeekday(day, hour)` | time-relative fixture helper - `nextWeekday(3, 20)` is the next Wednesday at 20:00 |
| `Harness.ago(minutes)` | a timestamp in the past, relative to now |

**Never hardcode a date in a fixture.** A prototype that has visibly rotted between the build and the showing discredits itself for free.

## Keys

`h` hides and restores all chrome. Arrow keys, Enter and Escape drive the screen panel while it is open. In hidden mode the artifact is shown exactly as a user would see it - no islands, no notes, no device frame, no notch.

**The viewport does not change.** Only a desktop view goes full-bleed - there the window *is* the viewport, so white to the edges is honest. A phone or tablet keeps its own size, because otherwise "hide chrome" would silently swap the viewport under review for a different one.

It also stays **visibly bounded**: the canvas remains behind it, the artifact keeps an outline and a shadow, and its pixel size is captioned underneath. A white artifact on a white page reads as something that failed to load, not as a phone.

## The screen panel

Screens live in a slide-out panel on the left, dark against the light canvas, opened by the `Screens` button at the far left of the top bar - which stays lit while it is open, with the current screen named beside it. Opening it **moves** the prototype rather than covering it. Each row carries its number on the right, and the open screen is a filled accent block rather than a marker beside a dark one. Each entry carries its **name and one sentence** saying which part of the flow it is - `desc` in the config.

That sentence is the reason it is a panel and not a dropdown. A reviewer who has to work out what *"02 Detail"* means is navigating by trial, and the first thing lost is the order the showing was meant to follow. The generated disclosure screen is tagged in the list, so nobody has to hunt for it.

Arrow keys move through the list, Enter opens, Escape closes.

## Notes: three kinds, and they are not interchangeable

All three share one geometry - a numbered pin on the element, a card on the rail, a curve joining them - and are told apart by colour and by a label on the card.

**A comment is bound to the device it was written on.** It carries a small device glyph, shows only at that width, and the rail says how many are waiting on another one with a click to go there. A remark about a narrow layout is wrong on a wide one, and a pin anchored at one width lands somewhere meaningless at another.

| `kind` | Who writes it | When |
|---|---|---|
| `number` · `generated` · `system` · `connection` | the author, in the config | **disclosure**: the element is invented and someone could act on it with no way to verify it |
| `convention` | the author, in the config | explains the prototype, not the product |
| `comment` | a reviewer, at runtime | a remark left where it happened |

The four disclosure kinds are the four categories that pass the test *"could someone act on this, with no way to verify it?"*. Invented names, avatars, titles and a scripted navigation path do **not** pass it and must not be annotated - over-labelling changes behaviour and buys nothing.

Every disclosure note carries `real:`, what the element would be in production. **The "What is real" screen is generated from those notes** - and it is responsive, because it is read on whatever device the prototype is being shown on: the table becomes one labelled block per element on a narrow screen, so the list is never maintained twice and cannot drift from the screens. Declare it as a screen entry with `disclosure: true` and no `src`.

**A note lands where you clicked**, not at the element's edge - the position is kept as a fraction of the element so it survives re-layout. A click that hits nothing selectable still gets a pin, anchored to a fraction of the document: *"there is nothing here"* is a finding, and a layer that only accepts notes on existing elements cannot receive it.

**An author's label can only be minimised; only your own comments can be deleted.** A disclosure the reader can make disappear is not a disclosure.

**Minimising rolls a card up to its title, in place.** It keeps its number, its pin and its line, and one click opens it again - it never leaves the rail, because a note pushed out of the way must not vanish with nothing on screen saying it was ever there. Notes without an anchor are grouped at the **top** of the rail under `About this screen` and `About this prototype`, each collapsible: put them last and every comment added shoves them further down, so they never sit still long enough to read as headers.

**Closing a card rolls it up; it does not delete it.** Clicking the strip or its pin brings it back. Only the `Notes` toggle removes the layer, and that state is not carried in a shared link - so no link can hand on a screen where an invented number has lost its label.

A selector that matches nothing renders as an orphan card with a warning instead of vanishing, so a renamed class is visible rather than silent.

## Getting feedback back

**Overall** (beside Add note) writes one covering note about the whole prototype - no pin, no severity. It leads the rail, leads the sheet, and leads the report. Six remarks about six elements are not the same as what someone thinks of the thing.

**`This view` and `For review`** sit together under *Send it on*, both labelled, because they are two different jobs: the first opens exactly what you are looking at - screen, state, time, device - for someone who should see that; the second opens in review mode with the task and the prompt to send notes back.

`For review` opens a small composer: add a line saying what you want *this* person to look at, then copy the link. That line travels in the URL, is shown to them before they start, and is carried into what comes back - so the reader can tell which remarks answer the question.

The reviewer's name is asked in the review brief, and - because most notes get written in an ordinary session where that card never appears - once more on the first note, inline. Severity is a labelled row of three dots: blue, orange, red.

`Add note` puts the artifact into comment mode: the next click inside it places a pin and opens an empty card. The shell cannot see that click on its own, so the client forwards it together with a selector - nothing is injected into the page but a cursor.

Comments live in that reviewer's own `localStorage`. **Without a backend they reach you only when the reviewer presses Send**, which is why that control is permanent, counts what is waiting, and nudges once after the first comment. `Send` copies a formatted summary to the clipboard, opens a prefilled mail when `review.to` is set, and saves a text file. Set `review.submitTo` to an endpoint and it posts instead - the only reason to do that is a run with several reviewers where you cannot depend on each of them remembering.

Open the harness with **`?review=1`** and the reviewer gets the task first, then three steps, then Start. Send it that way; the share button preserves the flag.

Reviewers never see each other's comments. For an async test with real users that is required, not a shortcoming - a shared thread contaminates the sample the moment the second person reads the first.

## Inspecting, comparing, presenting

| | |
|---|---|
| **Grid** | cycles off → 8px → 64px. 8 asks whether an element sits on the rhythm, 64 whether the layout does. Drawn in the shell over the frame - measured from the iframe itself, so inside a device mockup it stops at the screen and takes its corner radius rather than bleeding over the bezel |
| **Side by side** | the same screen at 1280 / 834 / 390 at once, each rendered at its **real width** and then scaled to fit, so the artifact's own media queries fire. Annotations are anchored to the single frame, so they step aside here and say why |
| **Present** | full screen, chrome down to prev / pause / next, each slot sweeping that screen's time across its range and scrolling the page through its own height |

A **pointer is on screen for the whole run**, resting inside the artifact and travelling to each declared target before it taps, so a run reads as someone using the prototype rather than as screens changing on their own.

**A presentation may drive the artifact; it must not invent input.** With no `tour` it walks the screens in order at `present.hold` ms each. Declare a `tour` when the demo has a story, and each step says exactly what is shown - `screen`, `state`, `variant`, `time`, `scroll`, `click`, `say`, `hold`. `click` is the only thing that touches the artifact, it is declared rather than guessed, and the element is ringed before it fires. Arrow keys step, space pauses, Escape exits.

## The report

The sheet behind `Return notes` does not list the notes again - the rail already shows them. It carries the covering note (or a field to write one, if it is still missing) and a single control to look the rest over before they go.

`Return notes` → **PDF report** assembles everything into one page and hands it to the browser's print dialogue, which is where a PDF comes from without a library:

It is styled in the tool's own language - the coral-to-gold accent, the mono labels, the same cards - so what lands in someone's inbox is recognisably the thing they were looking at.

- the header - who, when, how many, and a tally by severity
- **what was asked** and the reviewer's **overall note**
- one section per screen, **state and device**, showing that screen as it was when it was commented on, with the pins drawn back on and the notes numbered against them. A phone capture is never shown above 1:1
- **what was simulated**, from the disclosure notes, so the remarks are read against a prototype rather than against a finished product

Two things to know. It **visits** each screen and state to photograph it, so the view moves while it works; the original state is restored at the end. And the capture has the same limits as the PNG export - a screen it cannot reproduce gets a stated gap in the report rather than a silently wrong picture.

## Beyond the contract

Three conveniences the contract does not require, but that a reviewer expects from a tool like this:

| | |
|---|---|
| **Mockup** | A device frame around the artifact, modelled on the real hardware rather than a generic rounded rectangle: iPhone with its Dynamic Island and side buttons, iPad with an even bezel and camera, MacBook with a camera notch, browser chrome and the base under the lid. Off by default: it is presentation, and a usability test does not want it |
| **Share** | Copies a link carrying the whole state - screen, state, variant, time, device, mockup. The recipient opens *exactly* what you were looking at, and can keep clicking. For a prototype that beats sending a static image |
| **Export PNG** | Saves the current screen, with the mockup if it is on - **the same frame, cut-outs included**, because a mockup that loses its notch on export is a different mockup - and **never** with the annotation layer, since annotations are chrome, not product |

**The honest limit on export.** No browser API rasterises another document, so the artifact's DOM is cloned into an SVG foreignObject with its stylesheets inlined. That works, and it is fragile: cross-origin images, webfonts and canvas content will not come through. Every failure drops into capture mode - chrome and notes hidden, a message telling you to take a system screenshot - rather than saving something silently wrong.

## What this kit does not decide for you

The contract requires them; the kit cannot supply them:

- **Fixtures** - realistic content in its own file, plausible for this audience, covering the unbounded cases. Never lorem ipsum on a task path.
- **The four states themselves** - the harness switches them, the artifact renders them. An `unauth` state that renders identically to `full` is a missing state, not a satisfied one.
- **What the time scrubber means on each screen** - its scale, its label, and the one line saying what moving it demonstrates *there*. Declared per screen; a screen without a `time` block has no scrubber, which is the right answer wherever time is not part of the question.
- **Which elements earn an annotation** - the test is *"could someone act on this, with no way to verify it?"*, not *"is it fake?"*

## Design intent

The top bar carries the `PROTOTYPE` badge and the name, and no boundary sentence: the badge already implies it and the disclosure screen says it properly, so a third statement in the chrome was noise.

The chrome floats over a dotted canvas as translucent glass islands - the language every current prototyping tool speaks - with Pureinn's live coral-to-gold gradient as the accent. Three islands, so the disclosure is never mixed into a toolbar: it is not a control and must not look like one.

Two things were deliberately avoided. **Warm cream with terracotta**, because this framework's own design research names that exact combination as a generic 2026 AI-default cluster, and a file shipped as a reference should not look generated. And **anything left native** - a stock `<select>` is the loudest "unfinished" signal in a tool like this, so the screen picker is a real menu with keyboard navigation.

Annotations: a numbered pin on the element, a card on the rail, a curve joining them, and hovering either end lights all three. The numbering is what makes a rail of several notes legible - without it the reader has to guess which card belongs to which pin. Disclosure keeps the accent and the loudest pin because it carries the honesty contract; a convention recedes to grey; a comment is blue, visibly the reviewer's rather than the author's.

Changing device animates the frame between viewports rather than cutting to it. Seeing it travel reads as one artifact at another width; a jump cut reads as a different screen, and the reviewer loses the thread of what they were looking at. Annotations re-anchor when the movement finishes, not during it.

The bottom bar is a labelled tool bar rather than a strip of icons: every group says what it is, the scrubber carries the current screen's own label and a line explaining what it demonstrates, and the feedback group ends in the one call to action the reviewer has to reach. Nothing animates on its own - motion only ever answers an action, because the prototype is what is being looked at.

`prefers-reduced-motion` turns every animation off.

## Verified

Driven end to end in a real browser before shipping, per the contract's own "test outside the generating agent" rule: all four states reaching the artifact, variants, device presets firing the artifact's own media queries, artifact events arriving in the shell log, chrome hiding and restoring, annotation anchoring, the rail releasing when no note is visible, the screen menu with keyboard navigation, the mockup frame, a real PNG written to disk with no annotation layer in it, and a shared link restoring screen + state + variant + time + device + mockup in one go.

The second round added: per-screen time appearing, disappearing and keeping each screen's own value across a switch; a comment placed by clicking inside the artifact, with a real selector computed for it; collapse to a pin and reopen; an orphan anchor; the generated disclosure screen; and the review brief.

The third: the screen panel with its descriptions and keyboard navigation, and the viewport transition - sampled mid-flight at 427px between a 1106px desktop and a 390px phone, with the annotations re-anchoring correctly once it settled.

The ninth: a note written on mobile hidden on desktop with the rail offering to switch, the report grouped by screen/state/device with a phone shot held at 390px, and the sheet's roll-out opening below its control rather than beside it.

The eighth: the covering note leading the rail and the sheet, the author's line travelling in the link and reaching the brief, and a report built from two screen/state groups - five numbered pins matching five numbered rows, the shot cropped from a 1059px frame to the 392px the artifact actually draws, and the harness restored to where it started.

The seventh: a card rolled up keeping its number, pin and line while staying in the rail, and opening again on a click.

The sixth: a note placed on the background with nothing selectable under it, the grid measured against the frame in all three devices with and without a mockup, the disclosure screen at 390px with no horizontal overflow, and the presented pointer staying on screen for a whole four-step run.

The fifth: a note landing on the exact spot clicked rather than the element's edge, the name asked inline on the first note, the rail scrolling with its curves redrawn, and the presented pointer travelling to a target and tapping it.

The fourth: note scopes and their rail headers, a comment written and committed with a name and a severity, the return sheet, the grid's three steps, side by side at 53% with all three widths measured, and a four-step tour played to the end - states switching, captions changing, time sweeping and the progress bar filling.

Bugs found that way, none of which a reading of the code would have caught:

- notes overflowed the viewport and forced sideways scrolling
- turning notes off left the annotation rail reserved
- the chrome printed "Prototype" twice, once from the markup and once from the config default
- a connector-curve "improvement" scaled the bezier control points by the vertical gap, putting a control point past its own endpoint and tying the line in a knot
- the disclosure tag was a `<span>`, so a lower-specificity rule lost to the generic one and it rendered brown-on-coral at 1.9:1
- the dropdown's tick was an inline `<svg>` with no width, so it rendered at its intrinsic size and spilled across the menu
- a draft comment survived a reload and held the whole annotation layer in writing mode for ever
- the side-by-side container and the body-state class were both called `compare`, so `.compare { display: none }` matched `<body>` and blanked the entire document
- the rail positioned its cards absolutely, so once a few notes existed the newest ran off the bottom of the window - and the one being written was the first to go
- the annotation layer skipped its redraw while the chrome was hidden, silently dropping every change made in the meantime: toggles flipped there did nothing, and notes could come back missing after Hide
- a cross-origin artifact reserved the annotation rail and then drew nothing into it, because the document was read only after the rail was measured
- `.seg` and `.grp` set their own `display`, which beats the browser's rule for `[hidden]` - hiding the variant group did nothing at all
