/*
  Prototype harness - artifact side.

  Include this in every prototype page. It is the whole contract between the
  artifact and the shell around it, and it is deliberately small: the artifact
  must never depend on the harness to function. Open a page without the shell
  and it still runs - it just has no state switching, no time scrub and no
  event capture.

  Copy byte-for-byte. Do not re-author per prototype.
*/
(function (global) {
  'use strict';

  var handlers = { state: [], time: [], variant: [] };
  var current = { state: 'full', time: 0, variant: 'default' };
  var embedded = global.parent !== global;

  function on(kind, fn) {
    if (!handlers[kind]) throw new Error('unknown harness channel: ' + kind);
    handlers[kind].push(fn);
    // fire immediately so a late subscriber is never out of sync
    fn(current[kind]);
    return function off() {
      handlers[kind] = handlers[kind].filter(function (h) { return h !== fn; });
    };
  }

  function apply(kind, value) {
    if (current[kind] === value) return;
    current[kind] = value;
    handlers[kind].forEach(function (fn) {
      try { fn(value); } catch (e) { console.error('[harness] handler failed', e); }
    });
  }

  /* Event log. Local only - never a network call, never production analytics. */
  function log(name, detail) {
    var entry = {
      t: Date.now(),
      name: name,
      detail: detail === undefined ? null : detail,
      state: current.state,
      variant: current.variant
    };
    if (embedded) global.parent.postMessage({ __harness: true, type: 'event', entry: entry }, '*');
    else (global.__harnessEvents = global.__harnessEvents || []).push(entry);
  }

  /* Time-relative fixtures. Never hardcode a date: a prototype that has
     visibly rotted between the build and the showing discredits itself. */
  function nextWeekday(day, hour) {
    var t = new Date();
    t.setHours(hour || 0, 0, 0, 0);
    var diff = (day - t.getDay() + 7) % 7;
    if (diff === 0 && new Date() > t) diff = 7;
    t.setDate(t.getDate() + diff);
    return t;
  }

  function ago(minutes) {
    return new Date(Date.now() - minutes * 60000);
  }

  global.addEventListener('message', function (e) {
    var d = e.data;
    if (!d || !d.__harness) return;
    if (d.type === 'state' || d.type === 'time' || d.type === 'variant') apply(d.type, d.value);
  });

  /* Announce readiness so the shell can push the current selection. */
  if (embedded) global.parent.postMessage({ __harness: true, type: 'ready' }, '*');

  global.Harness = {
    on: on,
    log: log,
    embedded: embedded,
    get: function (kind) { return current[kind]; },
    nextWeekday: nextWeekday,
    ago: ago
  };
})(window);
