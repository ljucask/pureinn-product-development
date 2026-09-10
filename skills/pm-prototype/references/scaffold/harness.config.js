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

  /* The qualifier after the word "Prototype" in the chrome, which is always
     there. Say what is simulated in one clause - depth belongs on the
     disclosure screen, not in this line. */
  boundary: 'not a live service. Data and some interactions are simulated.',

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
      }
    },
    {
      label: '02 Detail',
      src: 'detail.html',
      icon: 'detail',
      desc: 'One job opened - where the assignment is actually confirmed.'
    },

    /* The disclosure screen is generated from the annotations below, so the
       same list is never maintained twice. Give it no `src`. */
    {
      label: 'What is real',
      disclosure: true,
      icon: 'info',
      desc: 'Generated from the notes: every simulated element, and what it would be in production.'
    }
  ],

  /* Four states are the contract. Drop one only when it genuinely cannot exist
     for this artifact - and say so on the disclosure screen, because a missing
     unauthorised state is usually an omission rather than an impossibility. */
  states: ['empty', 'full', 'error', 'unauth'],

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
  review: {
    task: 'Try to assign the 08:30 job to a courier, then come back to the list.',
    name: '',        // pre-fills the reviewer's name; they can change it
    to: '',          // your address, for the prefilled mail
    submitTo: ''     // optional endpoint. Empty = manual return
  }
};
