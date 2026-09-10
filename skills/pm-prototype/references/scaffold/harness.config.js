/*
  Prototype harness - the only file edited per prototype.

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

  /* Every screen the reviewer can reach. First one loads on open.
     A disclosure screen ("what is real and what is simulated") belongs here as
     a normal entry - it is part of the prototype, not part of the chrome. */
  screens: [
    { label: '01 Entry',      src: 'index.html' },
    { label: '02 Detail',     src: 'detail.html' },
    { label: 'What is real',  src: 'simulated.html' }
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

  /* A scrubber, not a timer. Omit this block entirely if the artifact has no
     time dimension. `format` turns the raw value into what the reviewer reads. */
  time: null,
  /* time: {
       min: 0,
       max: 45,
       step: 1,
       format: function (v) { return (v < 10 ? '0' : '') + v + ':00'; }
     }, */

  /* Notes anchored to elements inside the artifact, keyed by screen src.
     `selector` runs inside the artifact document; omit it for a note with no
     anchor. An annotation earns its place when someone could ACT on the element
     and has no way to verify it - a number, a generated output, a result
     attributed to a system, a connection claim. Invented names, avatars and
     scripted navigation do not need one. */
  annotations: {
    // 'index.html': [
    //   { selector: '[data-metric]', text: 'Projected - author estimate, not measured.' },
    //   { selector: '.feed',         text: 'Sample data. Ordering is fixed, not ranked.' },
    //   { text: 'This screen shows the state after 14 sessions.' }
    // ]
  }
};
