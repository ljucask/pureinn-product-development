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
  Harness.on('time',    renderAtMinute);          // only if the config declares time
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

`h` hides and restores all chrome. In hidden mode the artifact is shown exactly as a user would see it - no islands, no notes, no device frame, no notch.

**The viewport does not change.** Only a desktop view goes full-bleed - there the window *is* the viewport, so white to the edges is honest. A phone or tablet keeps its own size, because otherwise "hide chrome" would silently swap the viewport under review for a different one.

It also stays **visibly bounded**: the canvas remains behind it, the artifact keeps an outline and a shadow, and its pixel size is captioned underneath. A white artifact on a white page reads as something that failed to load, not as a phone.

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
- **The disclosure screen** - it belongs in `screens` as a normal entry, because it is part of the prototype, not part of the chrome.
- **Which elements earn an annotation** - the test is *"could someone act on this, with no way to verify it?"*, not *"is it fake?"*

## Design intent

The chrome floats over a dotted canvas as translucent glass islands - the language every current prototyping tool speaks - with Pureinn's live coral-to-gold gradient as the accent. Three islands, so the disclosure is never mixed into a toolbar: it is not a control and must not look like one.

Two things were deliberately avoided. **Warm cream with terracotta**, because this framework's own design research names that exact combination as a generic 2026 AI-default cluster, and a file shipped as a reference should not look generated. And **anything left native** - a stock `<select>` is the loudest "unfinished" signal in a tool like this, so the screen picker is a real menu with keyboard navigation.

Annotations: a numbered pin on the element, a card on the rail, a curve joining them, and hovering either end lights all three. The numbering is what makes a rail of several notes legible - without it the reader has to guess which card belongs to which pin.

`prefers-reduced-motion` turns every animation off.

## Verified

Driven end to end in a real browser before shipping, per the contract's own "test outside the generating agent" rule: all four states reaching the artifact, variants, time scrub, device presets firing the artifact's own media queries, artifact events arriving in the shell log, chrome hiding and restoring, annotation anchoring and dismissal, the rail releasing when no note is visible, the screen menu with keyboard navigation, the mockup frame, a real PNG written to disk, and a shared link restoring screen + state + variant + time + device + mockup in one go.

Bugs found that way, none of which a reading of the code would have caught:

- notes overflowed the viewport and forced sideways scrolling
- turning notes off left the annotation rail reserved
- the chrome printed "Prototype" twice, once from the markup and once from the config default
- a connector-curve "improvement" scaled the bezier control points by the vertical gap, putting a control point past its own endpoint and tying the line in a knot
- the disclosure tag was a `<span>`, so a lower-specificity rule lost to the generic one and it rendered brown-on-coral at 1.9:1
