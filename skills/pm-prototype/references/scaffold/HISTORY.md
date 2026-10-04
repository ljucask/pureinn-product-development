# Prototype harness - verification history

> Moved out of `README.md`. A record of what was driven in a browser and which defects that found. **Not needed to use the harness** - read it before changing `harness.html`, because every item under "Bugs found" is a mistake this file has already made once.

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

The twenty-second added the view layer: a phase filter hiding a marked feature and one named only from the config, the role switch hiding a `data-role` element and a role-bound feature, a version group showing one option, a hand switch overriding the phase and carrying its `added` tag, the client's `Harness.has()` following every change, a link restoring role + phase + hand switches + version, Reset returning to the config's default, and the feature map listing four features under three phases.

The twenty-third ran the view layer over a real prototype - seven screens, fifteen registered features, four phases, three roles - instead of a test page: the default view opening on the first phase with 8 of 15 features, two screens dimmed with their reason and returning as the phase advanced, a role dimming two more, elements hidden both by `data-feature` in the artifact and by `on` selectors from the config, and a `'*'` selector hiding links on every screen. It changed the design once: most features there are a whole screen, which the first version could not express at all.

The twenty-fourth replaced hand verification with a suite - `tests/harness/`, seventeen tests driving the shipped files in a real browser against a fixture prototype. The same round moved the view onto its own dark island, made the feature list fold by phase, put the feature card beside the screen as a rendered document, gave every floating surface one closing rule, added motion that answers a press, and **removed the app-opening sequence entirely**: it was a second of theatre in front of the thing being reviewed.

The twenty-fifth followed an independent design review (22/40 on Nielsen's heuristics, "reads as every other AI tool"). The chrome was rebuilt as docked opaque bars with pushing sidebars, the feature list and card moved into one right-hand column, the accent went flat and darker, secondary text and every small label were brought to AA, closed sidebars became inert, and the controls were renamed to say what they do - *Share*, *Scenarios*, *Time and speed*, *Send notes*, *State: With data*. The suite grew to twenty-six tests, including measured contrast, the top bar's two halves never overlapping, and the prototype never sitting under the feature column.

The twenty-sixth closed what that round left open, after the owner looked at it: the bottom bar was a tall box holding a dark rounded card, nothing like the bar above it. It is now that bar's twin - one row, the same height, the view as the dark left end rather than a box inside. Every surface closes on a press outside it and only one is ever open; a docked column that "covered nothing and so stayed" had been the second exception to that rule in one day, and the second time the owner could not close it. Also: small targets raised to 24px, Undo on a deleted note, focus into a menu or sheet as it opens, the feature map as a table rather than a grid of identical cards. Thirty tests.

The twenty-seventh came from the owner using it. The bars became floating rounded toolbars, because the docked pass had made the chrome correct and dated. Three defects went with it, each with a test that now fails without the fix:

- **a second menu never closed the first.** A menu button stops its click reaching the document and `closeSurfaces('menu')` leaves menus alone, so opening State and then Share left State on screen for good - no longer tracked, under everything opened after it, with no control that could remove it. The pair test opens every control after every other and counts what is left
- **a box did not stay on what it was drawn around.** Marks were fractions of the frame - a place on the glass, not on the page - so scrolling moved the page out from under them, and a note added to one read those window fractions as page fractions and pinned somewhere else again. A mark is now anchored to the element under its centre
- **a quick second press could be ignored.** The guard that stops an opening click from also closing what it opened was a flag cleared by `setTimeout(0)`, and a browser runs input ahead of timers. It is the click event itself now

Bugs found that way, none of which a reading of the code would have caught:

- three panels could be open over the prototype with no way to clear them, because each had been given its own reason to ignore a press outside it. One rule now: a press outside closes it, and the prototype is outside
- opening the card of a feature that is a whole screen outlined a LINK to that screen on the current page instead of going there - any element matching the feature counted as "it is here". Found by the suite on its first run, not by eye
- **one duplicated opening tag took out a third of the shell.** A markup edit left `<div class="brief" hidden>` twice; the outer one never closed, so the note rail, every toast, the Show menu button and the review brief all sat inside a hidden element. A note saved and nothing appeared; Hide menu could not be undone with the pointer; a `?review=1` link showed a blurred screen with no card. Seventeen passing tests did not see it, because they all tested the view. An independent design review did. The suite now checks that no top-level surface is trapped inside a hidden ancestor, and exercises each of the four
- a list rebuilt on every paint can never transition: a new element has no previous state to move from. The switch that was just pressed is drawn in its old state and flipped a frame later

- one unparseable selector in a feature's `on` list showed every version of every group at once. It was already one rule per selector; that is not enough, because an unclosed bracket makes the parser keep reading for its partner and swallow every rule after it. Each selector is tried against the document first now
- every press in the view panel repaints its list, so the pressed button had left the document by the time the dismiss handler asked whether the click was inside the panel - the panel closed on its own first click and every later one landed on a stale copy. The third time this file has met that, and the same guard answers it

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
