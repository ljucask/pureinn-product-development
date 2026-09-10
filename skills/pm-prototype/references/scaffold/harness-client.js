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

  /* Comment mode. The shell cannot see clicks inside this document, so when a
     reviewer is placing a comment the artifact forwards the one click and the
     selector of what was hit. It is off unless the shell turns it on, and it
     adds nothing to the page but a cursor. */
  var picking = false;

  function selectorFor(el) {
    if (!el || el === document.body || el === document.documentElement) return null;
    if (el.id) return '#' + CSS.escape(el.id);
    for (var i = 0; i < el.attributes.length; i++) {
      var a = el.attributes[i];
      // a data- attribute is the most stable anchor an artifact can offer
      if (a.name.indexOf('data-') === 0 && document.querySelectorAll('[' + a.name + ']').length === 1) {
        return '[' + a.name + ']';
      }
    }
    var path = [];
    var node = el;
    while (node && node !== document.body && path.length < 5) {
      var part = node.tagName.toLowerCase();
      var parent = node.parentElement;
      if (parent) {
        var same = Array.prototype.filter.call(parent.children, function (c) { return c.tagName === node.tagName; });
        if (same.length > 1) part += ':nth-of-type(' + (same.indexOf(node) + 1) + ')';
      }
      path.unshift(part);
      node = parent;
    }
    return path.length ? path.join(' > ') : null;
  }

  function onPickClick(e) {
    if (!picking) return;
    e.preventDefault();
    e.stopPropagation();
    var sel = selectorFor(e.target);
    global.parent.postMessage({
      __harness: true, type: 'pick',
      selector: sel,
      label: (e.target.textContent || '').trim().slice(0, 60)
    }, '*');
  }

  function setPicking(on) {
    picking = !!on;
    document.documentElement.style.cursor = picking ? 'crosshair' : '';
  }

  /* Presentation mode drives the artifact from outside: it scrolls the page to
     a fraction of its own height and, where a tour declares one, performs a
     single click. Both are the shell asking the artifact to do something it
     could already do - no synthetic input is invented, and nothing runs unless
     the shell is presenting. */
  function scrollTo(fraction) {
    var doc = document.documentElement;
    var max = Math.max(0, doc.scrollHeight - global.innerHeight);
    global.scrollTo({ top: max * Math.min(1, Math.max(0, fraction)), behavior: 'smooth' });
  }

  function clickOn(selector) {
    var el = null;
    try { el = document.querySelector(selector); } catch (e) { /* bad selector */ }
    if (!el) return;
    el.scrollIntoView({ block: 'center', behavior: 'smooth' });
    el.classList.add('harness-touch');
    setTimeout(function () {
      el.click();
      setTimeout(function () { el.classList.remove('harness-touch'); }, 600);
    }, 260);
  }

  global.addEventListener('message', function (e) {
    var d = e.data;
    if (!d || !d.__harness) return;
    if (d.type === 'state' || d.type === 'time' || d.type === 'variant') apply(d.type, d.value);
    if (d.type === 'picking') setPicking(d.value);
    if (d.type === 'scroll') scrollTo(d.value);
    if (d.type === 'click') clickOn(d.value);
  });

  /* the ring that shows where a presented click landed. Injected once, and only
     ever visible on an element the shell is about to click. */
  (function () {
    var s = document.createElement('style');
    s.textContent = '.harness-touch{position:relative;outline:2px solid rgba(237,109,87,.9);' +
                    'outline-offset:3px;border-radius:4px;transition:outline-color .3s}';
    document.head.appendChild(s);
  })();

  document.addEventListener('click', onPickClick, true);

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
