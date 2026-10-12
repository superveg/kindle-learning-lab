/* Prevent accidental browser zoom without polling or changing activity state. */
(function () {
  'use strict';
  var last = null, start = null, moved = false, options = false;
  function reset() { last = null; start = null; moved = false; }
  function distance(a, b) {
    return Math.abs(a.clientX - b.clientX) > 32 || Math.abs(a.clientY - b.clientY) > 32;
  }
  function control(node) {
    while (node && node !== document) {
      if (node.nodeType === 1 && /^(BUTTON|A|INPUT|SELECT|TEXTAREA|SUMMARY)$/.test(node.tagName)) { return node; }
      node = node.parentNode;
    }
    return null;
  }
  /* Older Kindle browsers accept only the boolean listener argument. */
  try {
    var probe = Object.defineProperty({}, 'passive', { get: function () { options = { passive: false }; return false; } });
    var noop = function () {};
    document.addEventListener('kll-zoom-options', noop, probe);
    document.removeEventListener('kll-zoom-options', noop, probe);
  } catch (error) { options = false; }
  document.addEventListener('touchstart', function (event) {
    if (!event.touches || event.touches.length !== 1 || event.defaultPrevented) { reset(); return; }
    var point = event.touches[0];
    start = { clientX: point.clientX, clientY: point.clientY, time: new Date().getTime() };
    moved = false;
  }, options);
  document.addEventListener('touchmove', function (event) {
    if (!start || !event.touches || event.touches.length !== 1) { reset(); return; }
    var point = event.touches[0];
    /* A scroll/drag is never treated as a second tap. */
    if (Math.abs(point.clientX - start.clientX) > 10 || Math.abs(point.clientY - start.clientY) > 10) { moved = true; last = null; }
  }, options);
  document.addEventListener('touchend', function (event) {
    if (!start || moved || event.defaultPrevented || !event.changedTouches || event.changedTouches.length !== 1 || (event.touches && event.touches.length)) { reset(); return; }
    var point = event.changedTouches[0], now = new Date().getTime();
    if (now - start.time > 350 || Math.abs(point.clientX - start.clientX) > 10 || Math.abs(point.clientY - start.clientY) > 10) { reset(); return; }
    if (last && now - last.time <= 350 && !distance(last, point) && event.cancelable) {
      /* Cancelling touchend also cancels its click: deliver that control's click once. */
      event.preventDefault();
      if (event.defaultPrevented) {
        var target = control(event.target);
        if (target && !target.disabled && typeof target.click === 'function') { target.click(); }
      }
    }
    last = { clientX: point.clientX, clientY: point.clientY, time: now };
    start = null;
  }, options);
  document.addEventListener('touchcancel', reset, false);
  document.addEventListener('dblclick', function (event) { event.preventDefault(); }, false);
}());
