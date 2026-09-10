# Prototype harness - the kit

The reference implementation of the contract in [`../in-repo-loop.md`](../in-repo-loop.md), for a **standalone HTML/CSS/JS prototype**. Inside an existing repo or a published artifact, build to the same contract in that stack instead - the contract is the source of truth, this is one conforming implementation.

## Files

| File | Copy byte-for-byte | Edit per prototype |
|---|---|---|
| `harness.html` | yes - never re-author it | no |
| `harness-client.js` | yes | no |
| `harness.config.js` | as a starting point | **yes - this is the only one** |

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

`h` hides and restores all chrome. In hidden mode the artifact fills the window exactly as a user would see it - no bars, no notes, no frame. One action, both directions.

## What this kit does not decide for you

The contract requires them; the kit cannot supply them:

- **Fixtures** - realistic content in its own file, plausible for this audience, covering the unbounded cases. Never lorem ipsum on a task path.
- **The four states themselves** - the harness switches them, the artifact renders them. An `unauth` state that renders identically to `full` is a missing state, not a satisfied one.
- **The disclosure screen** - it belongs in `screens` as a normal entry, because it is part of the prototype, not part of the chrome.
- **Which elements earn an annotation** - the test is *"could someone act on this, with no way to verify it?"*, not *"is it fake?"*

## Verified

The kit was driven end to end in a browser before shipping - state switching reaching the artifact, variant, time scrub, device presets firing the artifact's own media queries, artifact events arriving in the shell log, chrome hiding and restoring, annotation anchoring and dismissal, and the rail releasing when no note is visible. Two layout bugs found that way and fixed: notes overflowed the viewport and forced sideways scrolling, and turning notes off left the rail reserved.
