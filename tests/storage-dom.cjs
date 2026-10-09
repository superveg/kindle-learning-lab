/* Optional development-only checks: Node.js, jsdom, and Acorn. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const acorn = require('acorn');
const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
acorn.parse(html.match(/<script>([\s\S]*?)<\/script>/)[1], { ecmaVersion: 5 });
const key = 'kindle-learning-lab.storage-test.v1';
function load(storage) {
  return new JSDOM(html, { runScripts: 'dangerously', url: 'https://superveg.github.io/kindle-learning-lab/', beforeParse(window) {
    window.scrollTo = function () {};
    Object.defineProperty(window, 'localStorage', { get() { if (storage instanceof Error) { throw storage; } return storage; } });
  }});
}
const values = { 'unrelated-setting': 'keep' };
const storage = { getItem(k) { return Object.hasOwn(values, k) ? values[k] : null; }, setItem(k,v) { values[k] = String(v); }, removeItem(k) { delete values[k]; } };
let dom = load(storage);
function click(id) { dom.window.document.getElementById(id).click(); }
function status() { return dom.window.document.getElementById('storage-status').textContent; }
assert.match(status(), /No saved/);
click('storage-save');
const marker = values[key];
assert.match(marker, /^KLL-\d+-\d+$/);
assert.match(status(), /Written and read back/);
dom.window.close();
dom = load(storage); // New document with the retained storage adapter.
assert.ok(status().includes(marker));
click('open-check'); click('storage-read'); assert.ok(status().includes(marker));
click('storage-clear'); assert.match(status(), /cleared/);
assert.equal(values['unrelated-setting'], 'keep');
dom.window.close(); dom = load(storage); assert.match(status(), /No saved/);
dom.window.close();
for (const failingStorage of [new Error('SecurityError'), undefined, { getItem() { return null; }, setItem() { throw new Error('QuotaExceededError'); }, removeItem() { throw new Error('SecurityError'); } }]) {
  dom = load(failingStorage);
  click('storage-save'); assert.match(status(), /Save failed/);
  click('storage-clear'); assert.match(status(), /Could not clear/);
  click('open-letters'); click('letter-a');
  assert.match(dom.window.document.getElementById('letters-feedback').textContent, /All done/);
  dom.window.close();
}
dom = load({ getItem() { return null; }, setItem() {}, removeItem() {} });
click('storage-save'); assert.match(status(), /could not be verified/);
dom.window.close();
console.log('PASS: ES5, marker write/read, reload simulation, scoped clear, blocked/missing/full storage, silent write failure, activity fallback. Actual Kindle persistence remains pending.');
