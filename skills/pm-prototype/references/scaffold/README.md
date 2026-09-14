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

**Serve it with caching off, and threaded.** `python3 -m http.server` sends no `Cache-Control`, so browsers cache your config heuristically - you edit `harness.config.js`, reload, and see nothing changed. It is also single-threaded, and the harness holds the page plus an iframe plus the three side-by-side copies open at once, so one stalled connection wedges the whole server and every later request hangs with no error. Use this instead:

```python
# serve.py
import http.server, socketserver
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()
class S(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True
S(("", 8000), H).serve_forever()
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
| `await Harness.wait()` | a simulated delay, scaled by the latency setting - zero when it is off |

**Never hardcode a date in a fixture.** A prototype that has visibly rotted between the build and the showing discredits itself for free.

## Keys

`h` hides and restores the menus. Arrow keys, Enter and Escape drive the screen panel while it is open. In hidden mode the artifact is shown exactly as a user would see it - no islands, no notes, no device frame, no notch.

**The viewport does not change.** Only a desktop view goes full-bleed - there the window *is* the viewport, so white to the edges is honest. A phone or tablet keeps its own size, because otherwise "hide chrome" would silently swap the viewport under review for a different one.

It also stays **visibly bounded**: the canvas remains behind it, the artifact keeps an outline and a shadow, and its pixel size is captioned underneath. A white artifact on a white page reads as something that failed to load, not as a phone.

## Two front screens, both optional

A prototype meets two kinds of people, and they need opposite things first. A **tester** needs the task and nothing else - framing contaminates them. **Whoever decides** needs the framing; that is the whole reason they are in the room.

| Screen | For | From |
|---|---|---|
| **Overview** | investor, sponsor, team, steering committee | `overview:` - six blocks: what this is, who for, the job it does, what it should move, what you will see, what is not in it |
| **What is real** | both | `disclosure:` plus every non-convention note. Carries the pair, the classification, the element table with its **effort** column, and `beforeLaunch` - what still has to happen before any of it could ship |
| **How to test it** | the tester | `instructions:` - the steps, what to ignore, how to leave a note |

Both exist only if their block is filled in, and **`Invite to review` lets you tick which of them travels with the link** - the overview to the sponsor, the instructions to the tester, neither to someone who has already seen it.

**Every figure on the Overview carries its class** - `observed` · `calculated` · `projected` · `target` · `sample` - printed beside the number. A projection in front of a committee is the most actionable unverifiable number a prototype can contain, and a footnote does not travel with a screenshot.

**A prototype that already has its own document keeps it.** Where the artifact carries an honesty page the author wrote by hand, `about: true` on that screen files it in the same section - unnumbered, read at desktop width, loaded from its own file. The alternative, regenerating it from the config, produces a near-copy of a page that already exists and is not the page anyone was shown. The reverse also works: give the generated page that prototype's own `title` and its content row for row, and it is the same document in the harness's own design.

**Both, and `What is real`, are documents about the prototype rather than screens of it.** The panel puts them in their own **collapsible section**, outlined instead of filled and without a number, and the numbering in the flow counts only the real screens. Mixed into the same list in the same styling they read as two more things to click through, and a tester will dutifully test them.

They are shown at desktop width whatever the device switcher says. It is read by someone at a desk and is not part of the product surface.

## The screen panel

Screens live in a slide-out panel on the left, dark against the light canvas, opened by the `Screens` button at the far left of the top bar - which stays lit while it is open, with the current screen named beside it. Opening it **moves** the prototype rather than covering it. Each row carries its number on the right, and the open screen is a filled accent block rather than a marker beside a dark one. Each entry carries its **name and one sentence** saying which part of the flow it is - `desc` in the config.

That sentence is the reason it is a panel and not a dropdown. A reviewer who has to work out what *"02 Detail"* means is navigating by trial, and the first thing lost is the order the showing was meant to follow. The generated disclosure screen is tagged in the list, so nobody has to hunt for it.

Two sections - **Screens** and **About this prototype** - each headed and counted; the second collapses and stays collapsed. Arrow keys move through the list, Enter opens, Escape closes.

## Activities: what can be done on this screen

A prototype hides its own behaviour. The journey that only starts when someone presses submit; the empty state that only appears if you know it exists. A reviewer who does not think to do it never sees the thing the prototype was built to show, and reports back on the half they found.

The usual fix is a demo panel drawn **inside** the artifact. That is scaffolding shipped in the product's own UI, and it is exactly what this harness exists to take out - it survives into screenshots, into the handover, and sometimes into production.

So a screen declares what can be done on it, in `activities`, and the shell lists them under **`Try it`** in the dock. The group hides itself on a screen that declares none, and the button carries the count.

| Kind | Written as | What it does |
|---|---|---|
| state | `{ state: 'empty' }` | switches to a declared state |
| time | `{ time: 30 }` | moves this screen's clock |
| scroll | `{ scroll: 1 }` | travels to a fraction of the page |
| click | `{ click: '#assign' }` | clicks a declared selector |
| says | `{ says: '...' }` | a line of guidance instead of an action |

Each carries a `label` and a one-line `does` saying what it demonstrates - the same reasoning as `desc` on a screen: a list of unexplained buttons is a puzzle.

**`click` is the only kind that reaches into the document.** It is named in the config rather than guessed at runtime, and where the artifact carries `harness-client.js` it travels as a message; without the client the shell performs the same click itself, same-origin. Either way it is a real click on a real element - nothing synthetic is invented, for the same reason presentation mode never fabricates input.

**Never declare an activity that fakes input the prototype does not really take.** Where the point is that something runs on real typing - a journey that would carry no weight if it were pre-baked - use `says` and let the reviewer type. An activity that simulates the very thing under test destroys what it was meant to demonstrate.

## One surface at a time

The dropdowns, the situation panel, the notes panel and the screen panel are all ways of asking the harness something, and two of them open at once is two answers competing for the same corner of the screen. Opening any one closes the rest.

They also close by clicking away from them, which matters because a dropdown has no close button of its own. **A click inside the artifact counts as clicking away** - it happens in a separate document and never reaches the shell, which is why a menu used to stay open while the reviewer was already clicking around inside the prototype.

One exception: the situation panel stays open when the artifact is clicked. It is the panel that drives the artifact, so shutting it the moment someone clicks the thing they just changed would fight them.

## Following the artifact

A prototype worth reviewing has real links in it, and a reviewer uses them. The iframe then changes document on its own, without going through the screen panel - so the shell has to ask the document where it actually is rather than assume it is still showing what it loaded. It does that after every load, and adopts the answer only when the config already declares that screen; an outbound link leaves the selection alone instead of blanking it.

Without this the screen name, the activity list, the time axis and the notes all stay with the page the reviewer left, which reads as "the harness only works on the first screen".

**Pins are re-measured, not remembered.** Scroll the artifact and each pin recomputes from its element's current position, so the line follows the thing it points at instead of wandering across the screen. A pin whose element has scrolled out of view hides rather than clamping to the edge - a pin parked at the rim claims the note is about something on screen when it is not.

## Hiding the chrome

`h` hides everything the harness draws. That has to mean **everything**: the device frame, the notch, the status bar, the address pill, the glare, the side buttons, the safe-area padding the phone chrome needed, and the rounded corners. What is left is the artifact as a browser would show it.

The parts injected at runtime are the ones that keep surviving this, because they are added after the rules that hide them were written. Anything `hardware()` builds has to be in that list.

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

**Comments take emphasis and one picture** - bold, italic, underline, and an attached reference image, because *"make it look like this"* with a screenshot is worth ten sentences. Pasted markup is stripped to `b/i/u/br/img` and an image is scaled to 1100px before it is kept, or the second note fills the browser's quota.

Both bottom bars live in **one dock** that wraps when the window runs out, so they lay out against each other instead of overlapping on a width nobody tested. The simulation panel, the return sheet and the note rail all read the dock's measured height rather than assuming it.

The bottom folded from fourteen controls to six, grouped by intent rather than listed:

| | |
|---|---|
| **State** | the segmented switch, used constantly, one click |
| **Simulate** | the chip and its panel |
| **Share ▾** | *Copy this view* · *Invite to review* · *Screenshot* · *Event log* - one family: taking something out of here |
| **Add note ▾** | *Something I click* · *This screen* · *The whole prototype* - one action with three targets, and no three button labels can say that. In a menu each gets a line |
| **Mark ▾** | *Box* · *Marker pen* |
| **Return notes (n)** | stays visible and keeps its count. Without a backend nothing reaches you until it is pressed, so folding it away would break the one mechanism it serves |

Spotlight moved up beside `Present`: it is a way of showing someone something, not a way of recording anything.

**Notes have their own island**, bottom right, on a warm ground rather than the cool glass - it is a different job from driving the prototype and it looks like one: *Mark something* (pin, box, marker, spotlight), *Write one* (an unanchored note, the overall note, the editor) and *When you finish*. They had outgrown being a group inside the bar that drives the prototype.

**Not every note points at something.** `Note` writes one about the screen with no anchor - "this screen has no way back" does not belong pinned to an arbitrary button. And after a box or a marker stroke, a bubble offers *Add a note here* for a few seconds and then gets out of the way.

**`View all notes`** at the foot of the rail opens the note editor on the right: every note in one place, filtered by kind, severity and text, editable and deletable. Clicking a row goes to where that note lives - its screen, its state, its device - and flashes its pin. **Edit happens in the panel**, not back in the bubble; and a note being written in the bubble can carry on there via the small expand icon beside its close control. The rail is a notepad; this is the register. While it is open the rail steps aside.

**Closing a card rolls it up; it does not delete it.** Clicking the strip or its pin brings it back. Only the `Notes` toggle removes the layer, and that state is not carried in a shared link - so no link can hand on a screen where an invented number has lost its label.

A selector that matches nothing renders as an orphan card with a warning instead of vanishing, so a renamed class is visible rather than silent.

## Marks and the spotlight

A note explains; a **mark points**. Some things cannot be said with a pin - *this region*, *these three words*, *the gap here* - so there are two marking tools beside `Add note`:

| | |
|---|---|
| **Box** | drag a rectangle around something |
| **Marker** | drag across it, like a highlighter |

Both are kept as **fractions of the frame**, so they survive a resize or a device change, and both belong to a screen + state + device exactly as a comment does - a box around a narrow layout means nothing on a wide one. Hover a mark to remove it.

**Spotlight** is the live version of the same instinct - *look here*, while someone is watching. Everything but the pointer steps back. It is deliberately **not saved**: a gesture, not a record.

## Placing a comment

Arm the note button, click the thing, type, save. Two details decide whether that works at all:

**The cursor goes to the text, not to the name.** Focusing the name field first put the first thing typed into "Your name", left the note empty, and made it look as though a comment could not be submitted. The name is optional and can be filled at any point.

**Placing a note closes the all-notes panel**, because that panel hides the rail and the rail is where a new note is written. A pin appearing with no editor is indistinguishable from nothing happening.

Where the artifact carries `harness-client.js` the click is forwarded as a message. Where it does not - a prototype built before the client existed, or one that must not be edited at all - the shell captures the same click itself on the same-origin document. Both produce the same note.

## Sending it to someone

**Host it first, then share from the hosted address.** Every link the harness makes - `Copy this view`, `Invite to review` - is built from wherever it is running, because the harness cannot know where it will end up. Made on a development server, a link points at a machine nobody else can reach; the toast says so rather than letting a reviewer discover it days later.

The files are static, so anywhere that serves a folder will do. It has to be **served, not opened**: the artifact runs in an iframe and the shell reads that document to place labels, comments and screenshots, and under `file://` every file is a separate origin, so that reading is refused. The screens still appear; the layer over them does not.

`Invite to review` is the link worth sending. It carries the task written for that one person, and a tick for whether the Overview and the instructions travel with it - the overview to a sponsor, the instructions to a tester, neither to someone who has already seen it.

## Getting feedback back

**`Add note ▾` → `The whole prototype`** writes one covering note about it - no pin, no severity. It leads the rail, leads the sheet, and leads the report. Six remarks about six elements are not the same as what someone thinks of the thing.

**`Share ▾` → `Copy this view` and `Invite to review`** open genuinely different things:

| | |
|---|---|
| **Copy this view** | this exact screen, state, time and device. No task, no prompt to send anything back |
| **Invite to review** | the same instruments **plus** the task, their name on every note, and a Send control that will not let them leave without offering |

**A review link differs by what it asks, not by what it removes.** Every instrument that helps someone look - the widths, the mockup, the grid, side by side, the presentation, a screenshot to argue with elsewhere - is as useful to a reviewer as to you, and taking it away only makes them worse at the job you asked for. Two things stay behind: the **event log**, which is your instrumentation rather than theirs, and **`Invite to review`** - minting a review link with a task on it is not a reviewer's to hand out. `Copy this view` stays: pointing at the exact screen they mean is useful, and they already have the link.

`Invite to review` opens a small composer: add a line saying what you want *this* person to look at, then copy the link. That line travels in the URL, is shown to them before they start, and is carried into what comes back - so the reader can tell which remarks answer the question.

The reviewer's name is asked in the review brief, and - because most notes get written in an ordinary session where that card never appears - once more on the first note, inline. Severity is a labelled row of three dots: blue, orange, red.

`Add note ▾` → `Something I click` puts the artifact into comment mode: the next click inside it places a pin and opens an empty card. The shell cannot see that click on its own, so the client forwards it together with a selector - nothing is injected into the page but a cursor.

Comments live in that reviewer's own `localStorage`. **Without a backend they reach you only when the reviewer presses Send**, which is why that control is permanent, counts what is waiting, and nudges once after the first comment. `Send` copies a formatted summary to the clipboard, opens a prefilled mail when `review.to` is set, and saves a text file. Set `review.submitTo` to an endpoint and it posts instead - the only reason to do that is a run with several reviewers where you cannot depend on each of them remembering.

Open the harness with **`?review=1`** and the reviewer gets the task first, then three steps, then Start. Send it that way; the share button preserves the flag.

Reviewers never see each other's comments. For an async test with real users that is required, not a shortcoming - a shared thread contaminates the sample the moment the second person reads the first.

## Inspecting, comparing, presenting

| | |
|---|---|
| **Grid** | cycles off → 8px → 64px. 8 asks whether an element sits on the rhythm, 64 whether the layout does. Drawn in the shell over the frame - measured from the iframe itself, so inside a device mockup it stops at the screen and takes its corner radius rather than bleeding over the bezel |
| **All three** (in the device switcher) | THIS screen on desktop, tablet and phone at once, each at its own natural size and all at one scale, bottom-aligned - a product shot, not three columns. It is a choice of *device*, so it lives beside the three it replaces rather than as a control of its own |
| **Screens** | ALL screens at the width the device switcher is set to |
| **Simulate** | opens the simulation panel - the time axis with **play** and reset, and latency. Time is something being *run*, not a value being picked, and the panel is where the next dimensions go (audience, data volume, locale) without the bar growing a row. The chip shows the current value; the panel remembers whether it was open |
| **Latency** | `none` / `realistic` / `slow`, published to the artifact. `await Harness.wait()` resolves immediately when it is off and costs nothing to call, so a prototype can be honest about waiting without being slow to build. A prototype that answers everything instantly teaches the wrong expectation |
| **Present** | full screen, chrome down to prev / pause / next, each slot sweeping that screen's time across its range and scrolling the page through its own height |

A **pointer is on screen for the whole run**, resting inside the artifact and travelling to each declared target before it taps, so a run reads as someone using the prototype rather than as screens changing on their own.

`Present` and `Hide menu` sit together at the far right: they are **modes** - they take the whole surface over - rather than tools that change one thing on it. Present has its own glyph, not a second play triangle beside the simulation's.

**Mockup is orthogonal to both.** The same button that frames the single view frames these, and they use the *same* markup and CSS as the single view, scaled - so there is one iPhone in this tool, not three that drift apart. Each frame still renders at its real width before scaling, so the artifact's own media queries fire.

**Grid and Add note are off in both multi views.** A pin belongs to one frame, and a grid measures one viewport at full size - at 43% an 8px rule on screen is not 8px in the artifact, so it would quietly lie. Opening a document screen leaves the multi view too: three scaled copies of one page is nonsense.

**A note cannot be placed in either multi view.** A pin belongs to one frame; with three or six on screen and no rail, `Add note` is disabled and says why.

**A presentation may drive the artifact; it must not invent input.** With no `tour` it walks the screens in order at `present.hold` ms each. Declare a `tour` when the demo has a story, and each step says exactly what is shown - `screen`, `state`, `variant`, `time`, `scroll`, `click`, `say`, `hold`. `click` is the only thing that touches the artifact, it is declared rather than guessed, and the element is ringed before it fires. Arrow keys step, space pauses, Escape exits.

## Presenting it

Press play and the harness runs the prototype on its own. With no `tour` it walks the screens in order; declare one and each step says exactly what is shown - screen, state, variant, a fixed time, how far to scroll, and one selector to click.

**A tour that only scrolls narrates the prototype. A tour that clicks uses it.** Where a declared click lands on a link, the screen changes because it was pressed, not because the tour jumped there, and the shell follows the artifact the same way it does when a reviewer clicks. Name the screen on the following step anyway: it costs nothing when the click already took you there, and it recovers the walk if a click ever misses.

**The pointer travels at a speed that depends on how far it has to go** - a hand does not take the same time to cross a screen as to nudge to the next button, and a fixed duration for both is the single thing that makes a walkthrough read as an animation. The pause before the click follows the travel, because arriving and clicking in the same instant looks like a script.

**The opening sequence never plays during a presentation.** It is the app being started, which happens once and at the beginning; arriving in the middle of a walkthrough it reads as the prototype crashing and reloading.

**Pace it for someone watching.** The default slot is six seconds, and each step can set its own `hold`. The person in the room has to see the screen change, read the caption, follow a number moving, and form an opinion - four seconds covers only the first of those.

## Side by side, scrolling together

Both multi views - the same screen at three device widths, and every screen at one width - **scroll in step**. Move one copy and the rest follow.

Position travels as a **fraction of each document's own scrollable height**, not as pixels. The same screen at three widths is three different heights, and in the all-screens view they are different documents entirely, so pixel 800 is a different place in each while "a third of the way down" is the same place in all of them.

Without this the copies sat frozen at the top, which made side by side good for comparing a header and useless for anything below it - and most of what a reviewer argues about is below it.

**The copies take the wheel but not a link.** Scrolling has to reach the document or the view cannot be read at all; following a link does not, because it would take one copy somewhere the others are not and the row would stop comparing the same thing. A held link says so rather than doing nothing. Everything else the screen does still works in each copy.

## The report

The sheet offers **one primary action and one beside it**, with the rest as quiet links - and which is primary follows whose hands it is in: a reviewer wants to send (Copy, then Email), a maker wants the report. Four buttons of equal weight is a menu, not a choice.

The sheet behind `Return notes` does not list the notes again - the rail already shows them. It carries the covering note (or a field to write one, if it is still missing) and a single control to look the rest over before they go.

The sheet separates **Send it back** (Copy · Email · the endpoint) from **Or keep a copy** (PDF report · Text · CSV · JSON). Getting the notes to a person and keeping a copy of them are not the same act. CSV is one row per note - severity, screen, state, device, anchor, author, time - and opens in a spreadsheet with a BOM so Excel reads it as UTF-8. JSON carries everything, marks included.

`Return notes` → **PDF report** assembles everything into one page and hands it to the browser's print dialogue, which is where a PDF comes from without a library:

It is styled in the tool's own language - the coral-to-gold accent, the mono labels, the same cards - so what lands in someone's inbox is recognisably the thing they were looking at.

- the header - who, when, how many, and a tally **grouped by device**, severity inside: three high on a phone and three high on a desktop are not the same finding
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
| **Export PNG** | Saves the current screen, with the mockup if it is on - **the same frame, cut-outs included**, because a mockup that loses its notch on export is a different mockup - and with any **marks** drawn on it, but **never** the notes. The split is what each one is for: a note explains and travels as text, so the report and the CSV carry all of it; a mark only says "this bit", and a mark left out of the picture says nothing at all |

**The honest limit on export.** No browser API rasterises another document, so the artifact's DOM is cloned into an SVG foreignObject with its stylesheets inlined. That works, and it is fragile: cross-origin images, webfonts and canvas content will not come through. Every failure drops into capture mode - chrome and notes hidden, a message telling you to take a system screenshot - rather than saving something silently wrong.

## What this kit does not decide for you

The contract requires them; the kit cannot supply them:

- **Fixtures** - realistic content in its own file, plausible for this audience, covering the unbounded cases. Never lorem ipsum on a task path.
- **The four states themselves** - the harness switches them, the artifact renders them. An `unauth` state that renders identically to `full` is a missing state, not a satisfied one. Five more are offered and none required - `loading`, `partial`, `long`, `offline`, `forbidden` - each answering a lie a prototype tells by default. Adding one obliges the artifact to render it; a state it ignores is worse than one never offered, because it reads as tested.
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

Driven end to end in a real browser before shipping, per the contract's own "test outside the generating agent" rule: all four states reaching the artifact, variants, device presets firing the artifact's own media queries, artifact events arriving in the shell log, chrome hiding and restoring, annotation anchoring, the rail releasing when no note is visible, the screen menu with keyboard navigation, the mockup frame, a real PNG written to disk with no notes in it, and a shared link restoring screen + state + variant + time + device + mockup in one go.

The second round added: per-screen time appearing, disappearing and keeping each screen's own value across a switch; a comment placed by clicking inside the artifact, with a real selector computed for it; collapse to a pin and reopen; an orphan anchor; the generated disclosure screen; and the review brief.

The third: the screen panel with its descriptions and keyboard navigation, and the viewport transition - sampled mid-flight at 427px between a 1106px desktop and a 390px phone, with the annotations re-anchoring correctly once it settled.

The twenty-first was a full code and security review of the three files rather than a feature round, run through the framework's own JIT review flow and then re-verified in the browser: the sanitiser rejecting every nested payload that used to pass, a note carrying a remote image scrubbed out of storage on load, a screenshot-only note counted and exported instead of silently deleted, the side-by-side columns measured at exactly the 1280 / 834 / 390 they advertise, Hide menu going white on desktop, the mockup staying off a document screen, a malformed `?m=` leaving a working harness, and an editor surviving a stage scroll with its caret and focus intact.

Three things the review raised were decisions rather than defects, and were settled rather than patched: Send now says, beside the button, that it also carries a record of the session, because the sheet promised notes and the POST sent the browsing log too; the share URL still carries the author's message (without a backend there is nowhere else for it) but the event log records only that a link was made, so the message is not amplified into the POST; and marks now appear in the PNG and the report, verified by reading the exported file's pixels back - a coral box and an amber stroke, the stroke still multiplying over the text under it.

The twentieth: the three note scopes reached from one menu and a screen note written through it, the Share menu carrying all four exports, and the mark menu relabelling its button to "Drag a box" while armed.

The nineteenth: both bottom bars side by side at 1700 with a 12px gap, wrapping to two rows at 1200 and with both panels open, and everything above them following the measured height.

The eighteenth: the spotlight no longer blanking the page, a note written with no anchor, a box offering a note and getting one, editing inside the panel, and a CSV with one row per note.

The seventeenth: a comment written with bold and saved as HTML, the note panel filtering 5 notes down to 1 by text and by kind, a box and a marker stroke drawn, stored and disappearing on another state, and the spotlight following the pointer.

The sixteenth: Present moved beside Hide menu with its own icon, and the note rail anchored to the window - no horizontal scrollbar behind it and the curves still landing after a device change.

The fifteenth: the simulation panel opening from its chip, play running the axis from 0 to 25 min and pausing, reset returning it, and the latency setting arriving in the artifact.

The fourteenth: the multi-device row staying inside the stage at 1440 and at 900 with the mockup on, the time axis changing from minutes to days between two screens, and the mockup no longer drawn around a document screen.

The thirteenth: All three selected from the device switcher and showing a laptop, a tablet and a phone at true relative size on one baseline, Grid and Add note disabled there, a document screen dropping out of it, and the documents section collapsing and staying collapsed.

The twelfth: both multi views composing the single view's own frames at 44%, the mockup toggle reframing either, states reaching all three copies, `Add note` disabled in both, and the panel listing three documents below a divider while the count says two screens.

The eleventh: the Overview rendering its six blocks with three provenance classes and the device switcher locked to desktop, the instructions screen, both screens dropping out of a link when unticked, and the promo view framing every screen at a proportional bezel.

The tenth: a reviewer's link keeping every looking instrument while the event log and the sharing controls stay behind, the sheet reduced to Copy plus Email with two links under it, and the report's tally split into a desktop and a mobile group.

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
- the side-by-side container and the body-state class were both called `compare`, so `.compare { display: none }` matched `<body>` and blanked the entire document - and the promo view repeated the mistake a week later
- the promo frames put their iframes at `top: 0`, which measures from the padding box, so each artifact covered the bezel it was supposed to sit inside
- `.marks svg` was meant for the drawing surface and caught the icon inside the delete button too, absolutely positioning it into the button's top-left corner. Scope a rule to `> svg` when it means *that* svg
- the note rail positioned itself from the frame's measured width, caught a mid-transition number, and drifted off the right edge - with a horizontal scrollbar behind it, because an absolutely positioned child in the reserved padding counts as overflow. It is anchored to the window now
- `body.compare .wrap { display: none }` hid the scaled copies too, because they are `.wrap` as well - the third time in this file that a rule meant for one element caught everything sharing its name
- and the fifth: `body.spot` shared its name with `.spot`, so `.spot { display: none }` matched `<body>` and **the whole page went white**. Every body state now carries an `is-` prefix - `is-spot`, `is-compare`, `is-promo`, `is-mock`, `is-bare`, `is-notes` - and no element class may begin with one. Before that, the fourth: the mockup state was `mock`, the same as the frame element's, so `document.querySelector('.mock')` returned `<body>`. **No state class on `<body>` may share a name with an element class** - they are `is-mock`, `compare`, `promo` now, and the containers are `.mock`, `.cmpset`, `.proset`
- the multi-device row sized itself from the viewports alone and then drew a bezel around each, pushing the row past the stage - and a centred flex row that overflows loses its left end where no scrollbar can reach it (`justify-content: safe center`)
- the rail positioned its cards absolutely, so once a few notes existed the newest ran off the bottom of the window - and the one being written was the first to go
- the annotation layer skipped its redraw while the chrome was hidden, silently dropping every change made in the meantime: toggles flipped there did nothing, and notes could come back missing after Hide
- a cross-origin artifact reserved the annotation rail and then drew nothing into it, because the document was read only after the rail was measured
- the `is-` prefix sweep missed two selectors, and both failed silently: `body.bare:has(...)` never matched, so Hide menu on a desktop viewport left the dotted canvas behind a full-bleed artifact, and `:not(.fixed-width)` guarded all seventeen mockup rules against a class nothing sets any more - so a text document was drawn inside an iPhone bezel with the toggle greyed out. A rename is not finished until you grep for the old name in the CSS as well as the JS
- `clean()` snapshotted `childNodes` before unwrapping, so anything one level inside a `<span>` or `<p>` - the exact shape a paste produces - sailed past the tag allowlist with its attributes intact. It also parsed into a `document.createElement('div')`, which still has this document as its owner, so the input executed while it was being sanitised. It parses into `document.implementation.createHTMLDocument()` now and walks live nodes. **A sanitiser that trusts a snapshot is not one**
- four code paths disagreed about what makes a note real. A screenshot with no words rendered in the rail, never reached the count or any export, and was deleted by the load filter on the next refresh - silently losing the single highest-value note the layer carries. `plain()` is the only test now, and everything that reads `.text` goes through `noteText()`
- `writeStore` swallowed every exception, quota included, so past roughly twenty image notes the toast still said "Note added" and the reload found nothing. It reports once, while there is still time to export
- the storage key was the config `name` alone, and two prototypes on one host are one origin: on the shipped default they shared every key, so Send in one posted the other's notes to the wrong endpoint. The path is part of the key now
- `fetch` rejects only on a network failure, so a 413 or a 500 from the author's endpoint thanked the reviewer for notes that never arrived
- `drawAnnots` empties the rail and rebuilds every card, and it was wired straight to the stage's scroll event - so scrolling to look at the thing you were describing tore the editor down mid-sentence. It waits while anyone is writing
- the side-by-side copies set the wrap to the viewport width and then drew the bezel inside it, so the phone column rendered at 368px under a label reading 390. A media query at `min-width: 390px` fired in the single view and not in the comparison the view exists to make
- only the `ready` branch of the message listener checked `e.source`, so the three scaled copies tripled every event in the log and answered a presented aim three extra times - up to sixteen clicks for one declared step
- `annotEl.querySelector('.note--comment')` looked for cards in the layer they do not live in, so the saved-note confirmation flash never played once
- and one introduced by the review itself, caught only because it was re-run in a browser: `clean()` is called at load on stored notes, so a module-level `var KEEP` was still `undefined` when it ran and the exception took the whole boot with it. `node --check` passed. **Hoisting is not an ordering guarantee, and a syntax check is not a load**
- `.seg` and `.grp` set their own `display`, which beats the browser's rule for `[hidden]` - hiding the variant group did nothing at all
