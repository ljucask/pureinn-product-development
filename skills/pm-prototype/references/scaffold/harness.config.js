/*
  Prototype harness - the only file edited per prototype.

  This file belongs to the shell, not to the artifact. The prototype never
  reads it and never knows it exists; the only thing that crosses into the
  artifact is a value over postMessage. So nothing declared here can shift a
  layout or add an element to a screen.

  Everything here is declaration, not logic. If you find yourself writing
  behaviour in this file, it belongs in the artifact instead.
*/
window.HARNESS_CONFIG = {

  /* Used in the exported event log's filename and in screenshot filenames. */
  name: 'prototype',

  /* Shown in the chrome and in the browser tab. Falls back to `name`.
     This is the prototype's name, not the product's - "AMA lifecycle v1"
     rather than "Acme". */
  title: '',

  /* One clause on the disclosure screen, under its title. The chrome carries
     the PROTOTYPE badge and nothing else: the same sentence in the top bar was
     a third statement of something the badge already implies and the
     disclosure screen already says properly. */
  boundary: 'Not a live service. Data and some interactions are simulated.',

  /* ─────────────────────────────────────────────────────────────────────
     Screens. First one loads on open.

     `time` is declared per screen, never globally: time means something
     different on each one - minutes since an order on one screen, days into
     a subscription on the next - and a single scale across both measures
     nothing. A screen without a `time` block simply has no scrubber.

       icon    which glyph marks it in the screen panel, so the list is scannable:
               list · detail · form · board · chart · user · lock · cog · map · info
       desc    one sentence in the screen panel: which part of the flow this is.
               A reviewer who has to guess what "02 Detail" means navigates by
               trial, and loses the order the showing was meant to follow
       label   what the reviewer reads under the scrubber ("Minutes since order")
       hint    what moving it actually demonstrates HERE, in ONE SHORT LINE -
               it sits beside the scrubber in the shell bar and clamps to two
               small lines. Never rendered over the artifact
       format  turns the raw value into what the reviewer reads

     `activities` - OPTIONAL, per screen, and the answer to a specific failure:
     a prototype hides its own behaviour. The question journey only runs if the
     reviewer thinks to press submit; the empty state only appears if someone
     knows it is there. The usual fix is a demo panel drawn INSIDE the artifact
     - scaffolding shipped in the product's own UI, which is the thing this
     harness exists to take out.

     So the screen declares what can be done on it, and the shell lists it under
     `Try it`. Four kinds, each one something the artifact could already do:

       state   switch to a declared state       { state: 'empty' }
       time    move this screen's clock         { time: 30 }
       scroll  travel to a fraction of the page { scroll: 1 }
       click   click a declared selector        { click: '#assign' }
       says    a toast instead of an action, for the step only a person can do

     `click` is the only one that reaches into the document, it is named here
     rather than guessed at runtime, and where the artifact carries
     harness-client.js it travels as a message - otherwise the shell performs
     the same click itself, same-origin. Never declare an activity that fakes
     input the prototype does not really take: when the point is that something
     runs on real typing, say so with `says` and let the reviewer type.

       activities: [
         { label: 'Assign the 08:30 job', does: 'the one action under test', click: '#assign' },
         { label: 'An empty morning',     does: 'nothing waiting yet',       state: 'empty' },
         { label: 'Write your own',       does: 'this one runs on real input only', scroll: 0,
           says: 'Type into the box and send it - nothing pre-plays this.' }
       ]
     ───────────────────────────────────────────────────────────────────── */
  screens: [
    {
      label: '01 Entry',
      src: 'index.html',
      icon: 'list',
      desc: 'The dispatcher opens the day and sees jobs waiting to be assigned.',
      time: {
        min: 0, max: 45, step: 1,
        label: 'Minutes since order',
        hint: 'Watch the delivery estimate degrade as the courier stalls.',
        format: function (v) { return v + ' min'; }
      },
      activities: [
        { label: 'A quiet morning',   does: 'nothing in the queue yet',        state: 'empty' },
        { label: 'The queue fills',   does: 'the ordinary case',               state: 'full'  },
        { label: 'Twenty minutes in', does: 'the estimate has started to slip', time: 20 }
      ]
    },
    {
      label: '02 Detail',
      src: 'detail.html',
      icon: 'detail',
      desc: 'One job opened - where the assignment is actually confirmed.'
    },

    /* Three generated screens. Each exists only if its block above is filled in,
       each is a view of something already written down, and each can be left
       out of a shared link at the moment you send it. Give them no `src`. */
    {
      label: 'Overview',
      overview: true,
      icon: 'chart',
      desc: 'What this is, who it is for, and what it should move. For whoever decides.'
    },
    {
      label: 'How to test it',
      instructions: true,
      icon: 'user',
      desc: 'The steps to try, what to ignore, and how to leave a note.'
    },
    {
      label: 'What is real',
      disclosure: true,
      icon: 'info',
      desc: 'Generated from the notes: every simulated element, and what it would be in production.'
    }
  ],

  /* ─────────────────────────────────────────────────────────────────────
     The Overview screen - OPTIONAL, and for a different audience.

     Not for a tester. For whoever decides: an investor, a sponsor, a team, a
     steering committee. They are not here to click around; they are here to
     see what this is, who it is for, and what it should move - and the
     prototype on its own does not say any of that.

     A coding agent assembles it from the prototype folder's meta.md,
     hypotheses.md and context/ - it is a VIEW of those, not a second copy.
     Leave it out and the screen simply does not exist.

     THE NUMBERS HERE ARE THE MOST DANGEROUS IN THE WHOLE PROTOTYPE. A
     projection in front of a committee is the textbook case of "could someone
     act on this with no way to verify it?", so every metric carries its class:
       observed    measured, with a named source and period
       calculated  derived from observed inputs
       projected   estimated from stated assumptions
       target      desired, and therefore not evidence
       sample      fictional, to show the shape
     The class is printed beside the number, and the metric is listed on the
     disclosure screen with everything else that is simulated.

     It is shown at desktop width whatever the device switcher says: it is read
     by someone at a desk, and it is not part of the product surface.
     ───────────────────────────────────────────────────────────────────── */
  overview: null,
  /* overview: {
       is:  'Whether a dispatcher can assign a job first time, without being told how.',
       who: 'Dispatchers running 8-15 jobs a day, mostly on a laptop, often mid-call.',
       job: 'Clear the morning queue in ten minutes instead of forty.',
       metrics: [
         { label: 'Time to assign one job', value: '40s → 12s', kind: 'projected',
           note: 'From the walkthrough, not measured with users' },
         { label: 'Wrong assignments a week', value: 'under 2', kind: 'target' },
         { label: 'Jobs per dispatcher per day', value: '11', kind: 'observed',
           note: 'Ops export, Jan-Mar' }
       ],
       notIn: 'Pricing, billing, the courier app, and anything after the job is assigned.'
     }, */

  /* ─────────────────────────────────────────────────────────────────────
     The Instructions screen - OPTIONAL, and for the other audience.

     What a tester should try, in order. `review.task` is the one-line version
     shown in the opening card; this is the longer form for a session that has
     several steps. Leave it out for "just use it and tell me where it breaks".
     ───────────────────────────────────────────────────────────────────── */
  instructions: null,
  /* instructions: {
       steps: [
         'Start on the morning queue and find the 08:30 job.',
         'Assign it to a courier.',
         'Come back to the queue and check it is gone.'
       ],
       ignore: 'Styling, wording and anything outside the assignment flow.',
       ask: 'Say out loud whatever you are looking for. Where you hesitate is the finding.'
     }, */

  /* Four states are the contract. Drop one only when it genuinely cannot exist
     for this artifact - and say so on the disclosure screen, because a missing
     unauthorised state is usually an omission rather than an impossibility.

     Five more are offered, none required. Each answers a lie a prototype tells
     by default, and the first three are the ones worth the trouble:

       'loading'    the biggest one. A prototype answers instantly, so nobody
                    notices the flow assumed an instant result. Pair it with the
                    latency control and Harness.wait()
       'partial'    real data is ragged - a null field, a missing image. A
                    prototype's data is complete, so the layout is never tested
       'long'       the 200-item list, the 60-character name. content-and-copy
                    already asks fixtures to cover these; as a state it can be
                    checked rather than hoped for
       'offline'    for anything that will be used away from a desk
       'forbidden'  signed in but not allowed. 'unauth' is NOT signed in; they
                    are different screens and the second is routinely missed

     Adding one means the artifact must render it. A state the artifact ignores
     is worse than a state it does not offer. */
  states: ['empty', 'full', 'error', 'unauth'],
  // states: ['empty', 'loading', 'full', 'partial', 'long', 'error', 'unauth', 'forbidden', 'offline'],

  /* Named directions, shown side by side.
     MANDATORY when the prototype exists to choose between directions: a single
     committed option produces inflated ratings and near-zero rejection.
     Leave empty when the prototype is an answer rather than a choice. */
  variants: [],

  /* ─────────────────────────────────────────────────────────────────────
     Notes, keyed by screen src. Two kinds, and they are not interchangeable.

     DISCLOSURE - the element is invented and someone could act on it with no
     way to verify it. The test is not "is it fake?" but:

         Could someone ACT on this, with NO WAY to verify it?

     Four categories pass that test, and `kind` must be one of them:
       'number'      a figure someone would plan against
       'generated'   an AI or generated output
       'system'      a result attributed to a system - score, match, ranking
       'connection'  a claim that something is connected or synced

     Invented names, avatars, titles and a scripted navigation path do NOT
     pass it and must not be annotated. Over-labelling changes behaviour and
     buys nothing.

     Every disclosure note carries `real:` - what the element would be in
     production. That pair is what the generated disclosure screen is built
     from, and it is required by the harness contract.

     CONVENTION - `kind: 'convention'`. Explains the prototype, not the
     product ("this is the state after 14 sessions"). No `real:`; it describes
     nothing that would ship.

     `selector` runs inside the artifact document. Omit it for a note with no
     anchor. A selector that matches nothing renders as an orphan card rather
     than disappearing, so a renamed class is visible instead of silent.

     A third kind, 'comment', is written by reviewers at runtime and is never
     declared here.

     SCOPE is separate from kind, and it is read from the note itself:
       with a selector    → about that ELEMENT. It gets a pin, a curve, a number
       without a selector → about the SCREEN it is declared under
       under the '*' key  → about the PROTOTYPE, and shown on every screen

     A number always means "look at the pin with the same number". Anything
     without one is grouped in the rail under a header saying what it is about,
     so a card with no line cannot be mistaken for one whose line failed.
     ───────────────────────────────────────────────────────────────────── */
  annotations: {
    // 'index.html': [
    //   { kind: 'number',     selector: '[data-eta]',
    //     text: 'Projected - author estimate, not measured.',
    //     real: 'Computed from the courier feed and live traffic.' },
    //   { kind: 'system',     selector: '.match',
    //     text: 'The match score is fixed, not calculated.',
    //     real: 'Scored by the matching service against availability and rating.' },
    //   { kind: 'convention', text: 'This screen shows the state after 14 sessions.' }
    // ],
    //
    // // shown on every screen - about the prototype rather than any one screen
    // '*': [
    //   { kind: 'convention', text: 'Nothing here is saved. A refresh starts over.' }
    // ]
  },

  /* The generated disclosure screen's opening pair. Both halves are stated -
     what the prototype proves is worthless without what it does not. */
  disclosure: {
    proves: 'That the assignment flow is understandable end to end, and where it stalls.',
    doesNotProve: 'Anything about performance, permissions, or whether the matching logic is correct.',
    classification: 'Reference'   // Disposable | Reference | Evolutionary
  },

  /* ─────────────────────────────────────────────────────────────────────
     Presentation. Press the play button and the harness runs the prototype on
     its own: full screen, chrome reduced to prev / pause / next, each slot
     sweeping that screen's time across its range and scrolling the page
     through its own height.

     With no `tour` it simply walks the screens in order, `present.hold` ms
     each. Declare a `tour` when the demo has a story - then each step says
     exactly what is shown:

       screen   which screen (its src)
       state    empty | full | error | unauth
       variant  when the prototype carries variants
       time     a fixed value instead of the automatic sweep
       scroll   0-1: how far down the page to travel during the slot
       click    a selector to click, ONCE, part-way through the slot
       say      a caption under the artifact - what the audience should notice
       hold     ms for this step, overriding present.hold

     `click` is the only thing that touches the artifact, it is declared rather
     than guessed, and the element is ringed before it fires. A presentation
     that invented input would show an audience behaviour the prototype was
     never claimed to have.
     ───────────────────────────────────────────────────────────────────── */
  present: { hold: 4000 },

  tour: null,
  /* tour: [
       { screen: 'index.html', state: 'empty', say: 'A dispatcher opening an empty morning.', hold: 3500 },
       { screen: 'index.html', state: 'full',  scroll: 1, say: 'Jobs arrive; the estimate is the thing they act on.' },
       { screen: 'index.html', click: '#assign', say: 'Assigning is one action - this is what we wanted to test.' },
       { screen: 'detail.html', state: 'error', say: 'And what happens when the courier feed drops.' }
     ], */

  /* ─────────────────────────────────────────────────────────────────────
     Review mode. Open the harness with ?review=1 and the reviewer gets the
     task up front and a permanently visible Send control.

     Without a backend, comments live in that reviewer's own browser and reach
     you only when they press Send - which is exactly why the prompt to do it
     has to be unmissable rather than a button they might find.

     `submitTo` is optional and empty by default. Filled in (a form endpoint -
     Formspree, a Google Form, your own handler) comments post themselves and
     nothing depends on the reviewer remembering. Left empty, Send copies to
     the clipboard, offers a prefilled mail, and can save a file.

     One consequence worth keeping: reviewers cannot see each other's comments.
     For an async test with real users that is required, not a limitation - a
     shared thread contaminates the sample the moment the second person reads
     the first.
     ───────────────────────────────────────────────────────────────────── */
  /* The mark at the top of the screen panel. Unset shows Pureinn's, which is
     the honest default: the reviewer is looking at a Pureinn harness.

     Set it when the reviewer is looking at THEIR OWN product and the tool
     should recede - a client review, a stakeholder showing. `logo` is a path
     next to this file or a data: URI; `name` alone is enough when there is no
     mark to hand.

       brand: { logo: 'logo.svg', name: 'Acme Dispatch' }
       brand: { name: 'Acme Dispatch' }
       brand: false                      // no mark at all, for a white-label handover

     One mark, never two: the harness replaces its own rather than sitting
     beside yours, because two logos in one row read as a partnership. */
  /* What kind of application this is, which decides the hardware drawn around
     it. 'web' keeps a URL bar on every device; 'native' drops it and draws a
     status bar instead. Drawing browser chrome around a native app is a small
     lie a client notices before anything else. Switchable at run time from the
     caret beside the mockup button - this is only the starting value.

     NATIVE PROTOTYPES: the status bar OVERLAYS the artifact rather than taking
     a strip of its own, so a 390px phone still renders 390 x 844 and a height
     media query still fires truthfully. That means the top ~47px of a native
     screen sits under it - leave that much safe area at the top, as a real app
     does, or the first line of the screen reads through the clock. */
  // appType: 'web',            // 'web' | 'native'

  /* A faint reflection across the display in mockup mode. On by default; the
     first thing to turn off for a usability test, and switchable there too. */
  // glare: true,

  /* The app being opened, once, when the harness first shows it with the
     hardware drawn: a web app arrives at its address, a native one grows out
     of its icon on a home screen. Costs a second and is the difference between
     "here is a screen" and "here is the app".

     Any click skips it, it never plays with the mockup off, and it is skipped
     entirely under prefers-reduced-motion. Set false if even that is too much. */
  // opening: true,

  // brand: { logo: '', name: '' },

  review: {
    task: 'Try to assign the 08:30 job to a courier, then come back to the list.',
    name: '',        // pre-fills the reviewer's name; they can change it
    to: '',          // your address, for the prefilled mail
    submitTo: ''     // optional endpoint. Empty = manual return

    /* What you want ONE particular person to look at is not written here - it
       is typed into the Review link composer at the time you send it, travels
       in the URL, and is shown to them before they start. A per-person ask does
       not belong in a file shared by every run. */
  }
};
