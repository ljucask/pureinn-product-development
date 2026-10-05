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

## Files, continued

| File | Copy byte-for-byte | What it is for |
|---|---|---|
| `serve.py` | yes | serves the prototype; saves what a reviewer sends into the project; reloads the prototype when a file changes |
| `sync.py` | yes | writes the config's `features` from `../feature-cards/` |

## Use

```bash
cp harness.html harness-client.js harness.config.js serve.py sync.py  <prototype>/build/
python3 <prototype>/build/serve.py          # prints the URL to open
```

`serve.py` is the standard library and nothing else. It binds to `127.0.0.1`, sends `no-store` so an edited config is picked up on reload, and is threaded - a prototype with a looping video holds a connection open, and a single-threaded server then hangs every other request with no error.

In a prototype folder (one with `meta.md` beside `build/`) it serves the **folder**, so the harness can reach `feature-cards/`, and opens at `/build/harness.html`. Anywhere else it serves its own folder.

Any static host will also do for showing it - the bridge below is simply absent there.

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

## Around something that already exists (Wrap mode)

The harness does not need the prototype to know about it.

1. Copy `harness.html`, `harness-client.js`, `harness.config.js`, `serve.py` and `sync.py` into the folder the app's pages are served from - or into the folder **above** it, with `src: 'app/index.html'`, which leaves the app's own folder untouched.
2. In the config, list the pages under `screens` (`src` relative to `harness.html`) and remove what does not apply. For pages that render no states, set `states: []` and the State control goes away. Write `features` by hand, with `on` selectors - there are no cards for `sync.py` to read.
3. `python3 serve.py`.

**The pages must be on the same origin as the harness.** The shell reads the artifact's document to place notes, marks, labels and the view's rules; across origins it can show the page and nothing else, and it says so when such a screen is opened. A deployed app at another address has to be served through the same host, or copied beside the harness.

What works on pages that are left exactly as they are, and what needs one line added to them:

| Works untouched | Needs `<script src="harness-client.js">` in the page |
|---|---|
| screens, device widths, mockup, side by side | **states** - the page has to render them |
| notes, marks, screenshots, the report | **variants**, **time**, **response speed** |
| author's labels and the *What is real* screen | scenarios that scroll, and scrolling in a presentation |
| the feature list, phases, user types and versions through `on` selectors | the event log of what was clicked inside the page |
| scenarios and tour steps that click a declared element | |

So an untouched app gets the review layer and the feature view, not the simulation. Adding the client is one line; making the page answer `Harness.on('state', ...)` is the real work, and it is the same work as on any prototype.

A page served from somewhere else than its harness names the harness before loading the client: `<script>window.HARNESS_ORIGINS = ['https://review.example.com'];</script>`.

## The bridge: between the harness and the code

With `serve.py` behind it, three things work that a static host cannot give:

| | |
|---|---|
| **Save to project** | the primary action in *Send notes*. Writes `review/notes/<time>-<who>.json` and appends a readable entry to `review/notes.md`. Whoever works on the prototype in the repo reads them there - nothing to copy or paste |
| **Edit description** | on a feature's card. Saves the new description and notes to `review/proposals.json` as a **proposal**; the card shows it marked *Proposed - not applied yet*. Nothing else changes until `sync.py --apply` |
| **Live reload** | a change under the artifact reloads the frame and keeps the screen, state and view; a change to the config reloads the page onto the same place. Never while a note is being written |

**It writes only into `review/`, and never from a path in a request** - file names are built on the server. Every write needs the `X-Harness: 1` header and a `Host` of this machine: a page on another site cannot send that header without a preflight the server does not answer, and a rebound DNS name does not carry this Host. Dot-files are not served, and there are no directory listings.

The server listens on port 8931 unless given another, takes at most 8 MB in one save, follows no symlink out of the folder, and refuses a request that another site made.

`review/` holds reviewers' names, notes and screenshots. `serve.py` does not serve it as files, and **it must not be published with the prototype**: when the folder goes to a host, leave `review/` behind.

Nothing a reviewer sends can shape `review/notes.md` beyond its own line - every field beside the note text is flattened to one line, because that file is read by an agent as well as a person.

The bridge is looked for only on `localhost` / `127.0.0.1`. A hosted harness has no `serve.py` behind it, and probing for one would put an error in every reviewer's console.

### What the bridge answers

For a script, or an agent checking its own work, the routes are plain HTTP on the same address:

| | | |
|---|---|---|
| `GET /__harness/ping` | is the bridge here | `{ bridge: 1, prototype, prefix, writes }` |
| `GET /__harness/changes` | newest change among the shell files and among everything else | `{ shell, art }` |
| `GET /__harness/proposals` | every proposal, with its `status`: `open`, `superseded`, `applied` | a list |
| `POST /__harness/notes` | save a review | `{ from, asked, overall, notes: [...], marks: [...] }` → `{ ok, file }` |
| `POST /__harness/proposal` | propose a description | `{ feature, field: "desc" \| "spec", value, was, by }` → `{ ok, proposal }` |

Both `POST`s need `Content-Type: application/json` and `X-Harness: 1`.

## The feature list is generated

```bash
python3 build/sync.py           # rewrite `features` in harness.config.js from ../feature-cards/
python3 build/sync.py --check   # exit 1 if they no longer agree
python3 build/sync.py --apply   # accept the open proposals into the cards, then rewrite
```

It rewrites only what sits between its two markers. `phases`, `roles`, `versions` and `view` stay hand-written: they are asked once per project. A `cut` card is in no view and is listed on the feature map with its `reason:`; a card with no phase is reported, and its feature is shown in every view under *No phase* until someone decides. With no `feature-cards/` folder there is nothing to generate and the config is left alone.

## What the client gives the artifact

| | |
|---|---|
| `Harness.on(kind, fn)` | subscribe to `state` / `variant` / `time`; fires immediately, so a late subscriber is never out of sync |
| `Harness.get(kind)` | current value |
| `Harness.log(name, detail)` | one event into the local log. Never a network call |
| `Harness.nextWeekday(day, hour)` | time-relative fixture helper - `nextWeekday(3, 20)` is the next Wednesday at 20:00 |
| `Harness.ago(minutes)` | a timestamp in the past, relative to now |
| `await Harness.wait(base)` | a simulated delay, scaled by the response-speed setting - zero when it is instant. `base` is your own duration in ms; left out, a short realistic one is used |
| `Harness.has(id)` | is this feature in the current view? Always true outside the harness |
| `Harness.version(group)` | which option of a version group is showing |
| `Harness.embedded` | true when the page is running inside the shell |

`kind` is one of `state` · `variant` · `time` · `latency` · `role` · `phase` · `features` · `versions`. `Harness.on` returns a function that unsubscribes.

## Addresses

Everything the harness is showing can be opened by link - that is what `Copy this view` builds, and it is the quickest way to point someone, or an agent's user, at a change.

| Parameter | |
|---|---|
| `screen` | a screen's `src` from the config |
| `state` · `variant` · `device` | one of the declared states / variants; `desktop`, `tablet` or `mobile` |
| `t` | the time value on that screen |
| `mockup=1` | with the device frame |
| `role` · `phase` | a user type id, a phase id, or `all` |
| `fx` | features switched by hand: `PRT-A-001:1,PRT-A-002:0` |
| `ver` | version groups: `hero:B` |
| `review=1` | open as a reviewer, with the brief |
| `m` | the author's line for that reviewer - it is in the address, so nothing private |
| `x` | generated screens left out of a review link: `overview,instructions` |

A value the config does not declare is ignored.

**Never hardcode a date in a fixture.** A prototype that has visibly rotted between the build and the showing discredits itself for free.

## Keys

`h` hides and restores the menus. Arrow keys, Enter and Escape drive the screen panel while it is open. In hidden mode the artifact is shown exactly as a user would see it - no bars, no side panels, no notes, no device frame, no notch.

**The viewport does not change.** Only a desktop view goes full-bleed - there the window *is* the viewport, so white to the edges is honest. A phone or tablet keeps its own size, because otherwise "hide chrome" would silently swap the viewport under review for a different one.

It also stays **visibly bounded**: the canvas remains behind it, the artifact keeps an outline and a shadow, and its pixel size is captioned underneath. A white artifact on a white page reads as something that failed to load, not as a phone.

## Two front screens, both optional, and the disclosure screen both audiences share

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

So a screen declares what can be done on it, in `activities`, and the shell lists them under **Scenarios** in the bottom bar. The group hides itself on a screen that declares none, and the button carries the count.

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

## The view: role, phase, features, versions

Optional. Declare `roles`, `phases`, `features` or `versions` in the config and the **left end of the bottom bar** becomes the view; declare none and it is not there.

That end of the bar is dark, edge to edge and full height - the only dark thing in the chrome. It decides what the prototype is being read *as*, which is a different order of thing from the tools beside it. It is not a card sitting in the bar: an earlier version was, a rounded dark box with its own labels inside a taller white one, and it read as a bar inside a bar.

| In the bar | |
|---|---|
| **User type** | one user type, or all of them. A menu, with each type's one-line description. Visual only. The button carries the name, so it has no label |
| **Phase** | every phase in a row, one press each. The chosen one is lit and those before it are tinted, so "up to and including" is read off the control |
| **Features** | *Features 8 / 15* - how many are shown out of the total. Opens the list |

| In the list | |
|---|---|
| **The meter** | one block per feature, coloured by phase, solid where it is shown - the whole plan in one line |
| **Search and filter** | by name, id or description; *All*, *Shown*, *Hidden* |
| **Phases fold** | each phase header folds its features and keeps saying how many are shown. A phase can hold thirty; a search opens every group, because a match inside a folded one is a miss |
| **A row** | the name, its id, the screen it is on, and a switch. Pressing the name opens the feature's card |
| **Versions** | the groups that apply to this screen, above the list |

**The feature card opens beside the screen**, in that column, and points at the feature in the prototype as it opens - going to the feature's screen first if it is elsewhere. Reading what something should do and seeing where it is are one act; a description in another tab gets read instead of the prototype.

The card's top comes from the config: phase, user types, name, the one-line description, the notes so far. Under it is the feature's own card file (`card:`), rendered as a document - headings, paragraphs, lists, tables, bold and code, with the frontmatter left out. Everything is escaped before it is marked up, so a card file cannot put HTML on the page. No `card:` and the config half is the whole card; a file that fails to load says so.

**The list and the card share one column on the right**, and that column pushes the prototype rather than covering it. The card replaces the list and *All features* goes back. Floating, the two of them left about 390px of prototype in view.

**Every label says what the control does.** *User type*, *Phase*, *Shown*, *Hidden manually*, *Show in prototype*. A reviewer who has to work out what a control is called has stopped looking at the prototype.

Switches are real switches (`role="switch"`), everything is reachable by keyboard with a visible focus ring, and Escape closes the card or the list.

**How an element is hidden.** The artifact marks it - `data-feature`, `data-role`, `data-version-of` with `data-version` - and the shell writes one stylesheet into the artifact's document. An artifact that cannot be edited is handled from the config with `on`. The scaled copies in both multi views get the same stylesheet, so a comparison never shows a feature the single view hides.

**A feature is often a whole screen.** The screen entry names it - `feature: 'PRT-DSP-005'`, or several - and when every feature it names is out of the view the screen panel dims the row and prints the reason under it (*Hidden · In v1.1*). It stays in the list and can still be opened: a list that quietly lost a row would hide exactly what was cut. A presentation without a `tour` skips it. Hide the links that lead there with `on: { '*': ['a[href="moderation.html"]'] }`.

**Hiding from outside leaves debris.** `on` selectors hide elements, not the reason they were laid out that way. Cut most of a screen and what remains is a heading, a button and a gap - which is a finding about the plan, not a defect in the view: a feature that survives alone on a screen that was cut usually belongs on another screen. Mark elements in the artifact where it can be edited, and treat a ragged remainder as a question for the feature plan.

**A switch by hand is marked *Shown manually***, and a feature the user type hides cannot be switched at all - its switch is disabled and says why. Two presses never stack: the first undoes a hand switch, and only if the feature is then still the wrong way round does it set a new one.

**What travels.** `Copy this view` and `Invite to review` carry role, phase, hand switches and versions. A comment and every logged event record the role and phase they were made in. `Reset view` returns to the config's `view`.

**In script** - for what a stylesheet cannot do:

```js
Harness.on('features', render);          // fires on every change of view
if (Harness.has('PRT-DSP-002')) total += bulk;
Harness.version('hero');                 // 'A' | 'B' | ...
Harness.get('role');                     // 'all' or a role id
```

Outside the harness `Harness.has()` is true for everything, so the artifact still runs on its own.

**The feature map** is a generated screen - `{ featureMap: true }` - a table per phase: the feature, what it is, who it is for. It shows the whole plan whatever the view is set to.

A tour step may set `role` and `phase`, so a presentation can walk the MVP and then open the next phase.

## One surface at a time

The menus, the time-and-speed panel, the feature column, the note register, the send sheets and the screen panel are all ways of asking the harness something, and two of them open at once is two answers competing for the same corner of the screen. Opening any one closes the rest.

**Two rules, and they hold for every surface. The single exception is named in the first.**

1. **Only one is open at a time.** Opening the screen panel, the feature column, time and speed, the note register, a menu or a send sheet closes whatever was open before it. Two things open at once is two things to close, and the second was nearly always opened to replace the first. The one case kept: the *User type* menu, which is a control for the feature list and leaves it open.
2. **A press outside closes it, and the prototype counts as outside.** The artifact is a separate document, so the shell listens inside it as well as around it.

Escape closes the last thing opened: the feature card goes back to the list, then the list closes. A menu takes focus when it opens, the arrow keys move through it, and Escape returns focus to the button that opened it.

Two earlier versions each made an exception - panels that "drive the artifact" stayed open over it, then a docked column stayed open because it covered nothing. Both times the result was the same: a reader who could not work out how to clear the screen. A rule with exceptions has to be learned; this one does not.

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

**An author's label can only be minimised; only your own notes can be deleted.** A disclosure the reader can make disappear is not a disclosure. A deleted note can be taken back for six seconds - *Undo* in the message that confirms it.

**Minimising rolls a card up to its title, in place.** It keeps its number, its pin and its line, and one click opens it again - it never leaves the rail, because a note pushed out of the way must not vanish with nothing on screen saying it was ever there. Notes without an anchor are grouped at the **top** of the rail under `About this screen` and `About this prototype`, each collapsible: put them last and every comment added shoves them further down, so they never sit still long enough to read as headers.

**Comments take emphasis and one picture** - bold, italic, underline, and an attached reference image, because *"make it look like this"* with a screenshot is worth ten sentences. Pasted markup is stripped to `b/i/u/br/img` and an image is scaled to 1100px before it is kept, or the second note fills the browser's quota.

**The bottom bar is the top bar's twin**: the same height, the same white, one row. Left to right - the view, then *State*, *Scenarios*, *Time and speed*, *Share*, then *Add note*, *Mark* and *Send notes* at the right.

No control has a label above it; each carries its own word. The one exception is *Phase*, because a row of phase names does not say what it is. When the bar narrows - a smaller window, or a sidebar open - *Scenarios*, *Time and speed*, *Share* and *Mark* fall back to their icons. *State*, *Add note* and *Send notes* keep their words through that step: a reader has to be able to find those by name. Only at the last one - a small laptop with a side panel open, the bar under 940px - does every control become its icon with its name as the tooltip, because there the choice is between words and reaching the controls at all. The feature column narrows on a small window for the same reason.

*Send notes* stays visible and keeps its count. Without a backend nothing reaches you until it is pressed.



**Notes sit at the right end of the bottom bar**: `Add note ▾` (*Something I click*, *This screen*, *The whole prototype*), `Mark ▾` (*Box*, *Marker pen*) and `Send notes`, with *View all notes* under the caret beside it.

**Not every note points at something.** `Add note ▾` → `This screen` writes one about the screen with no anchor - "this screen has no way back" does not belong pinned to an arbitrary button. And after a box or a marker stroke, a bubble offers *Add a note here* for a few seconds and then gets out of the way.

**`View all notes`** at the foot of the rail opens the note editor on the right: every note in one place, filtered by kind, severity and text, editable and deletable. Clicking a row goes to where that note lives - its screen, its state, its device - and flashes its pin. **Edit happens in the panel**, not back in the bubble; and a note being written in the bubble can carry on there via the small expand icon beside its close control. The rail is a notepad; this is the register. While it is open the rail steps aside.

**Closing a card rolls it up; it does not delete it.** Clicking the strip or its pin brings it back. Only the `Labels` toggle in the top bar removes the author's labels - `Notes` beside it does the same for the reviewer's notes and marks - and that state is not carried in a shared link - so no link can hand on a screen where an invented number has lost its label.

A selector that matches nothing renders as an orphan card with a warning instead of vanishing, so a renamed class is visible rather than silent.

## Marks

A note explains; a **mark points**. Some things cannot be said with a pin - *this region*, *these three words*, *the gap here* - so there are two marking tools beside `Add note`:

**A mark belongs to the thing it was drawn on, not to the window.** It remembers the element under its centre and where it sits relative to that element, so it stays put when the page scrolls, when a side panel changes the prototype's width, when the layout reflows. A note added to a mark is pinned to the same element, so the two cannot drift apart. Where no element can be named, the mark falls back to a fraction of the page.

| | |
|---|---|
| **Box** | drag a rectangle around something |
| **Marker pen** | drag across it, like a highlighter |

Both belong to a screen + state + device exactly as a comment does - a box around a narrow layout means nothing on a wide one. Hover a mark to remove it.

Switching `Notes` off hides marks along with the notes, and choosing a mark tool switches them back on - drawing something invisible is not a feature.

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

Open the harness with **`?review=1`** and the reviewer gets the task first, then three steps, then Start. Send it that way; `Copy this view` preserves the flag.

**What leaves the browser, and when.** Nothing, until a reviewer acts. *Copy notes*, *Email* and the file exports carry the notes only. *Send to the author* - present only when `review.submitTo` is set - also carries the session's event log, and says so beside the button. *Save to project* writes to this machine through `serve.py`. The line an author adds in *Invite to review* travels in the link itself, so it is in the browser history and the host's access log of whoever opens it: do not put anything private in it.

**The shell and the artifact only talk to each other.** The shell takes messages only from this origin and the origins of the screens its config declares; the artifact's client takes them only from its parent window, and only when the parent is its own origin or one the page names in `window.HARNESS_ORIGINS` before loading the client. A reviewer who follows a link out of the prototype has put a stranger's page in the frame, and it gets no channel.

Reviewers never see each other's comments. For an async test with real users that is required, not a shortcoming - a shared thread contaminates the sample the moment the second person reads the first.

## Inspecting, comparing, presenting

| | |
|---|---|
| **Grid** | cycles off → 8px → 64px. 8 asks whether an element sits on the rhythm, 64 whether the layout does. Drawn in the shell over the frame - measured from the iframe itself, so inside a device mockup it stops at the screen and takes its corner radius rather than bleeding over the bezel |
| **All three** (in the device switcher) | THIS screen on desktop, tablet and phone at once, each at its own natural size and all at one scale, bottom-aligned - a product shot, not three columns. It is a choice of *device*, so it lives beside the three it replaces rather than as a control of its own |
| **Screens** | ALL screens at the width the device switcher is set to |
| **Time and speed** | opens the simulation panel - this screen's time axis with **play** and reset, and the response speed. Time is something being *run*, not a value being picked. The button shows the current time value where the screen declares an axis |
| **Response speed** | *Instant* / *Normal* / *Slow* in the panel; the artifact receives `none` / `realistic` / `slow`. `await Harness.wait()` resolves immediately when it is instant and costs nothing to call, so a prototype can be honest about waiting without being slow to build. A prototype that answers everything instantly teaches the wrong expectation |
| **Present** | full screen, chrome down to prev / pause / next, each slot sweeping that screen's time across its range and scrolling the page through its own height |

A **pointer is on screen for the whole run**, resting inside the artifact and travelling to each declared target before it taps, so a run reads as someone using the prototype rather than as screens changing on their own.

`Present` and `Hide menu` sit together at the far right: they are **modes** - they take the whole surface over - rather than tools that change one thing on it. Present has its own glyph, not a second play triangle beside the simulation's.

**Mockup is orthogonal to both.** The same button that frames the single view frames these, and they use the *same* markup and CSS as the single view, scaled - so there is one iPhone in this tool, not three that drift apart. Each frame still renders at its real width before scaling, so the artifact's own media queries fire.

**Grid and Add note are off in both multi views.** A pin belongs to one frame, and a grid measures one viewport at full size - at 43% an 8px rule on screen is not 8px in the artifact, so it would quietly lie. Opening a document screen leaves the multi view too: three scaled copies of one page is nonsense.

**A note cannot be placed in either multi view.** A pin belongs to one frame; with three or six on screen and no rail, `Add note` is disabled and says why.

**Each step declares what it shows, and says nothing about what it does not.** A step's `role` and `phase` hold for that step only; one that names neither is shown in the view the author had before pressing `Present`, and that view comes back when the tour ends. A step with a `click` lasts at least about three seconds whatever its `hold`, because the pointer has to aim, travel, pause and press.

**A presentation may drive the artifact; it must not invent input.** With no `tour` it walks the screens in order at `present.hold` ms each. Declare a `tour` when the demo has a story, and each step says exactly what is shown - `screen`, `state`, `variant`, `time`, `scroll`, `click`, `say`, `hold`. `click` is the only thing that touches the artifact, it is declared rather than guessed, and the element is ringed before it fires. Arrow keys step, space pauses, Escape exits.

## Presenting it

Press `Present` and the harness runs the prototype on its own. With no `tour` it walks the screens in order; declare one and each step says exactly what is shown - screen, state, variant, a fixed time, how far to scroll, and one selector to click.

**A tour that only scrolls narrates the prototype. A tour that clicks uses it.** Where a declared click lands on a link, the screen changes because it was pressed, not because the tour jumped there, and the shell follows the artifact the same way it does when a reviewer clicks. Name the screen on the following step anyway: it costs nothing when the click already took you there, and it recovers the walk if a click ever misses.

**The pointer travels at a speed that depends on how far it has to go** - a hand does not take the same time to cross a screen as to nudge to the next button, and a fixed duration for both is the single thing that makes a walkthrough read as an animation. The pause before the click follows the travel, because arriving and clicking in the same instant looks like a script.

**Pace it for someone watching.** The default slot is six seconds, and each step can set its own `hold`. The person in the room has to see the screen change, read the caption, follow a number moving, and form an opinion - four seconds covers only the first of those.

## Side by side, scrolling together

Both multi views - the same screen at three device widths, and every screen at one width - **scroll in step**. Move one copy and the rest follow.

Position travels as a **fraction of each document's own scrollable height**, not as pixels. The same screen at three widths is three different heights, and in the all-screens view they are different documents entirely, so pixel 800 is a different place in each while "a third of the way down" is the same place in all of them.

Without this the copies sat frozen at the top, which made side by side good for comparing a header and useless for anything below it - and most of what a reviewer argues about is below it.

**The copies take the wheel but not a link.** Scrolling has to reach the document or the view cannot be read at all; following a link does not, because it would take one copy somewhere the others are not and the row would stop comparing the same thing. A held link says so rather than doing nothing. Everything else the screen does still works in each copy.

## The report

The sheet offers **one primary action and one beside it**, with the rest as quiet links - and which is primary follows whose hands it is in: a reviewer wants to send (Copy, then Email), a maker wants the report. Four buttons of equal weight is a menu, not a choice.

The sheet behind `Send notes` does not list the notes again - the rail already shows them. It carries the covering note (or a field to write one, if it is still missing) and a single control to look the rest over before they go.

The sheet separates **Send your notes** (Save to project · Send to the author · Copy notes · Email - each present only when it can work) from **Or keep a copy** (PDF report · Text · CSV · JSON). Getting the notes to a person and keeping a copy of them are not the same act. CSV is one row per note - severity, screen, state, device, anchor, author, time - and opens in a spreadsheet with a BOM so Excel reads it as UTF-8. JSON carries everything, marks included.

`Send notes` → **PDF report** assembles everything into one page and hands it to the browser's print dialogue, which is where a PDF comes from without a library:

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
| **Share ▾ → Copy this view** | Copies a link carrying the whole state - screen, state, variant, time, device, mockup. The recipient opens *exactly* what you were looking at, and can keep clicking. For a prototype that beats sending a static image |
| **Share ▾ → Screenshot** | Saves the current screen as a PNG, with the mockup if it is on - **the same frame, cut-outs included**, because a mockup that loses its notch on export is a different mockup - and with any **marks** drawn on it, but **never** the notes. The split is what each one is for: a note explains and travels as text, so the report and the CSV carry all of it; a mark only says "this bit", and a mark left out of the picture says nothing at all |

**The honest limit on export.** No browser API rasterises another document, so the artifact's DOM is cloned into an SVG foreignObject with its stylesheets inlined. That works, and it is fragile: cross-origin images, webfonts and canvas content will not come through. Every failure drops into capture mode - chrome and notes hidden, a message telling you to take a system screenshot - rather than saving something silently wrong.

## What this kit does not decide for you

The contract requires them; the kit cannot supply them:

- **Fixtures** - realistic content in its own file, plausible for this audience, covering the unbounded cases. Never lorem ipsum on a task path.
- **The four states themselves** - the harness switches them, the artifact renders them. An `unauth` state that renders identically to `full` is a missing state, not a satisfied one. Five more are offered and none required - `loading`, `partial`, `long`, `offline`, `forbidden` - each answering a lie a prototype tells by default. Adding one obliges the artifact to render it; a state it ignores is worse than one never offered, because it reads as tested.
- **What the time scrubber means on each screen** - its scale, its label, and the one line saying what moving it demonstrates *there*. Declared per screen; a screen without a `time` block has no scrubber, which is the right answer wherever time is not part of the question.
- **Which elements earn an annotation** - the test is *"could someone act on this, with no way to verify it?"*, not *"is it fake?"*

## Design intent

**Floating, opaque, quiet.** The chrome is five objects resting on the canvas - a bar across the top, its twin across the bottom, and three side panels - each rounded, lifted by one soft shadow and inset from the window edge, with the canvas visible all the way round. The panels push the prototype aside instead of covering it: screens on the left, the feature list with its card on the right, the note register on the right. The prototype is the content; the tool is arranged around it, the way a canvas tool is.

The first version was translucent glass islands floating over a dotted canvas, with a coral gradient on everything pressed. A design review named it accurately as the look of every current AI tool, and it had costs beyond taste: the two top islands slid over each other on any window under 1500px, panels covered the prototype they were about, and white on the gradient measured between 2.1:1 and 3.0:1.

The first correction overshot. Full-bleed white bars with a hairline fixed everything that was broken and read as a web admin from ten years ago: flat is not the same as current. What makes a tool read as current is not translucency but that its chrome is a few distinct objects rather than walls. So the bars and panels float; they are still opaque, and still push.

What the chrome holds to now:

- **Coral is flat and reserved** - the PROTOTYPE marker, a note pin, a switch that is on, the one primary action. Selected is ink, not coral. It is `#c2452d`, which clears 4.5:1 both under white text and as text on white.
- **One dark block**, the view, because it changes what the prototype is being read as. It is the only signature left, on purpose.
- **Nothing under 11px**, and secondary text at 5.9:1.
- **A label only where a control does not say what it is.** The view block keeps *User type*, *Phase*, *Features*. The tools beside it do not carry a label over a button that already has the word on it.
- **The top bar answers to its own width**, not the window's, because a sidebar narrows it as surely as a small screen does. The tools on the right give up their words before the left gives up the name of the open screen.
- **Motion only answers a press**, and stays small. Nothing animates on its own; the pulsing dot on the PROTOTYPE marker is gone for that reason.
- **Nothing left native** - a stock `<select>` is the loudest "unfinished" signal in a tool like this.

Annotations: a numbered pin on the element, a card on the rail, a curve joining them, and hovering either end lights all three. The numbering is what makes a rail of several notes legible. Disclosure keeps the accent because it carries the honesty contract; a convention recedes to grey; a reviewer's note is blue, visibly theirs rather than the author's.

Changing device animates the frame between viewports rather than cutting to it. Seeing it travel reads as one artifact at another width; a jump cut reads as a different screen.

`prefers-reduced-motion` turns every animation off.

## Verified

Driven end to end in a real browser before shipping, per the contract's own "test outside the generating agent" rule, and re-verified on every change. The rounds, and the defects each one caught, are in [`HISTORY.md`](HISTORY.md) - read it before editing `harness.html`.

After any change, two checks, both required:

```bash
python3 check.py                       # structure: load order, name clashes, undefined calls
cd <repo>/tests/harness && npm test    # behaviour: the shipped files driven in a real browser
```

The second exists because the first cannot see behaviour, and behaviour is where this file breaks: a panel that closed on its own first click and a selector that silently un-hid every feature both passed `check.py`.
