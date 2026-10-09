/* Logic and syntax checks only; this does not verify browser rendering. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const acorn = require('acorn');
const { JSDOM } = require('jsdom');
const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
acorn.parse(script, { ecmaVersion: 5 });
assert.equal(/<(?:script|img|link)\b[^>]*(?:src|href)=/i.test(html), false);
const dom = new JSDOM(html, {
  runScripts: 'dangerously',
  url: 'https://example.test/kindle-learning-lab/',
  beforeParse(window) { window.scrollTo = function () {}; }
});
const doc = dom.window.document;
function el(id) { return doc.getElementById(id); }
function tap(id) { el(id).click(); }
function answer(value) {
  Array.from(el('count-answers').children).find(button => button.textContent === String(value)).click();
}
function visible(id) { assert.equal(el(id).style.display, 'block'); }
visible('home');
assert.equal(el('script-status').textContent, 'JavaScript is working.');
tap('open-count'); visible('count');
assert.equal(el('count-next').disabled, true);
tap('count-next'); assert.equal(el('count-progress').textContent, 'Question 1 of 3');
answer(1); assert.equal(el('count-next').disabled, true);
answer(2); answer(2); tap('count-next');
answer(3); answer(3); tap('count-next');
answer(1); answer(1); tap('count-next');
assert.match(el('count-feedback').textContent, /First-try answers: 2 of 3/);
assert.equal(el('count-next').style.display, 'none');
tap('count-home'); tap('open-count');
assert.equal(el('count-progress').textContent, 'Question 1 of 3');
answer(2); tap('count-next'); answer(3); tap('count-next'); answer(1); tap('count-next');
assert.match(el('count-feedback').textContent, /First-try answers: 3 of 3/);
tap('count-home'); tap('open-shapes'); tap('shape-square');
assert.match(el('shapes-feedback').textContent, /Look for/);
tap('shape-circle'); assert.equal(el('shape-square').disabled, true);
tap('shapes-home'); tap('open-shapes'); assert.equal(el('shape-square').disabled, false);
tap('shapes-home'); tap('open-letters'); tap('letter-c'); tap('letter-a');
assert.match(el('letters-feedback').textContent, /All done/);
assert.equal(el('letter-b').disabled, true);
tap('letters-home');
for (const choice of ['garden', 'pond']) {
  tap('open-story'); tap('story-' + choice);
  assert.match(el('story-feedback').textContent, /The end/);
  assert.equal(el('story-garden').disabled, true);
  assert.equal(el('story-pond').disabled, true);
  tap('story-home');
}
tap('open-check'); tap('text-size'); assert.equal(doc.body.className, 'large');
tap('text-size'); assert.equal(doc.body.className, '');
tap('tap-one'); tap('tap-one'); assert.match(el('tap-status').textContent, /1 of 3/);
tap('tap-two'); tap('tap-three'); assert.match(el('tap-status').textContent, /Touch check complete/);
tap('check-home'); visible('home');
dom.window.close();
const fallback = new JSDOM(html);
assert.equal(fallback.window.document.getElementById('shape-circle').disabled, true);
assert.ok(fallback.window.document.querySelector('noscript'));
fallback.window.close();
console.log('PASS: ES5 syntax, self-contained assets, navigation, scoring, retries, completion, reset, story branches, text size, touch state, static fallback. Rendering and actual Kindle remain pending.');
