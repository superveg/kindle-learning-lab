const assert = require('node:assert/strict');
const fs = require('node:fs');
const { JSDOM } = require('jsdom');
const acorn = require('acorn');
const guard = fs.readFileSync('tools/touch-guard.js', 'utf8');
acorn.parse(guard, { ecmaVersion: 5 });
for (const file of fs.readdirSync('.').filter(f => f.endsWith('.html'))) {
  const html = fs.readFileSync(file, 'utf8');
  const dom = new JSDOM(html);
  const d = dom.window.document;
  assert.match(d.querySelector('meta[name=viewport]').content, /maximum-scale=1,user-scalable=no/);
  assert.equal(d.querySelectorAll('#touch-guard').length, 1);
  assert.equal(d.querySelector('#touch-guard').textContent, guard);
  assert.match(d.querySelector('#touch-guard-style').textContent, /touch-action:manipulation/);
  dom.window.close();
}
for (const legacy of [false, true]) {
  const dom = new JSDOM('<button id="button"><span id="child">Tap</span></button><button id="disabled" disabled>Disabled</button><div id="blank"></div>', { runScripts: 'outside-only' });
  const w = dom.window, d = w.document;
  let clock = 1000, clicks = 0;
  w.Date = function () { this.getTime = () => clock; };
  if (legacy) {
    const add = d.addEventListener.bind(d);
    d.addEventListener = function (type, cb, options) {
      if (options && typeof options === 'object') throw Error('Boolean options only');
      return add(type, cb, options);
    };
  }
  w.eval(guard);
  d.getElementById('button').onclick = () => clicks++;
  function event(type, target = 'child', x = 50, y = 50, extra = {}) {
    const e = new w.Event(type, { bubbles: true, cancelable: true });
    const point = { clientX: x, clientY: y, identifier: 1 };
    Object.assign(e, { touches: type === 'touchend' ? [] : [point], changedTouches: [point] }, extra);
    d.getElementById(target).dispatchEvent(e);
    return e;
  }
  function tap(target = 'child', x = 50, y = 50) {
    event('touchstart', target, x, y); clock += 20;
    const e = event('touchend', target, x, y);
    if (!e.defaultPrevented) d.getElementById(target).click();
    return e;
  }
  assert.equal(tap().defaultPrevented, false);
  clock += 100;
  assert.equal(tap().defaultPrevented, true);
  assert.equal(clicks, 2, 'Second tap still performs one control action');
  clock += 100;
  assert.equal(tap().defaultPrevented, true);
  assert.equal(clicks, 3, 'Rapid triple tap stays blocked without dropping actions');
  clock += 500;
  assert.equal(tap().defaultPrevented, false, 'Slow tap remains native');
  clock += 100;
  assert.equal(tap('child', 120).defaultPrevented, false, 'Distant tap remains native');
  event('touchstart'); event('touchmove', 'child', 50, 100);
  assert.equal(event('touchend', 'child', 50, 100).defaultPrevented, false, 'Scroll remains native');
  assert.equal(tap().defaultPrevented, false, 'Scroll clears previous tap');
  event('touchstart'); clock += 400;
  assert.equal(event('touchend').defaultPrevented, false, 'Long press remains native');
  event('touchstart', 'child', 50, 50, { touches: [{}, {}] });
  assert.equal(event('touchend').defaultPrevented, false, 'Multi-touch never produces a control click');
  tap(); event('touchcancel'); assert.equal(tap().defaultPrevented, false);
  clock += 100; assert.equal(tap('disabled').defaultPrevented, true);
  clock += 100; assert.equal(tap('blank').defaultPrevented, true);
  assert.equal(event('dblclick').defaultPrevented, true);
  dom.window.close();
}
console.log('PASS: all pages embed fixed-scale ES5 guard; rapid taps retain one action each; native single/distant taps, scrolls, long presses, cancellation, disabled controls and legacy listener fallback.');
