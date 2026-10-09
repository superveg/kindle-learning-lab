const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const acorn = require('acorn');
const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
acorn.parse(html.match(/<script>([\s\S]*?)<\/script>/)[1], { ecmaVersion: 5 });
const key = 'kindle-learning-lab.counting.v1';
const values = { 'unrelated': 'keep' };
const storage = { getItem(k) { return Object.hasOwn(values,k) ? values[k] : null; }, setItem(k,v) { values[k] = String(v); }, removeItem(k) { delete values[k]; } };
function load(store) { return new JSDOM(html, { runScripts:'dangerously', url:'https://superveg.github.io/kindle-learning-lab/', beforeParse(w) { w.scrollTo = function () {}; Object.defineProperty(w,'localStorage',{get() { if(store instanceof Error) { throw store; } return store; }}); }}); }
let dom = load(storage);
function el(id) { return dom.window.document.getElementById(id); }
function tap(id) { el(id).click(); }
function answer(n) { Array.from(el('count-answers').children).find(b=>b.textContent===String(n)).click(); }
tap('resume-start'); answer(2); tap('count-next'); answer(3);
let saved=JSON.parse(values[key]);
assert.equal(saved.question,1); assert.equal(saved.answered,true); assert.equal(saved.score,2);
dom.window.close(); dom=load(storage);
tap('open-resume'); assert.match(el('resume-status').textContent,/question 2/);
tap('resume-continue'); assert.equal(el('count-progress').textContent,'Question 2 of 3');
assert.equal(el('count-next').disabled,false);
assert.equal(el('count-answers').children[2].className,'chosen');
answer(3); assert.equal(JSON.parse(values[key]).score,2);
tap('count-next'); answer(1); tap('count-next');
assert.equal(JSON.parse(values[key]).completed,true);
dom.window.close(); dom=load(storage); tap('resume-continue');
assert.equal(el('count-next').style.display,'none');
assert.match(el('count-feedback').textContent,/3 of 3/);
tap('resume-clear'); assert.equal(storage.getItem(key),null); assert.equal(values.unrelated,'keep');
tap('resume-start'); answer(1);
dom.window.close(); dom=load(storage); tap('resume-continue');
assert.equal(el('count-retry').style.display,'inline');
assert.equal(el('count-next').disabled,true); answer(2); assert.equal(JSON.parse(values[key]).score,0);
for(const value of ['{broken', JSON.stringify({version:1,question:99}), 'null']) {
  storage.setItem(key,value); tap('open-resume'); tap('resume-continue');
  assert.match(el('resume-status').textContent,/invalid/);
}
tap('open-grid'); assert.equal(el('grid-cells').children.length,9);
tap('grid-cell-1'); tap('grid-cell-5'); tap('grid-cell-9'); tap('grid-cell-5');
assert.equal(el('grid-status').textContent,'Selected cells: 1, 9');
assert.equal(el('grid-cell-5').getAttribute('aria-pressed'),'false');
tap('grid-reset'); assert.equal(el('grid-status').textContent,'No cells selected.');
const reference=dom.window.document.querySelector('.reference-lines');
tap('open-refresh'); for(let i=0;i<8;i++)tap('refresh-next');
assert.equal(el('refresh-value').textContent,'6'); assert.equal(el('refresh-next').disabled,true);
assert.equal(dom.window.document.querySelector('.reference-lines'),reference);
tap('refresh-reset'); assert.equal(el('refresh-value').textContent,'0'); assert.equal(el('refresh-next').disabled,false);
tap('open-svg'); assert.equal(el('test-svg').querySelectorAll('svg').length,1);
assert.ok(el('test-svg').querySelector('img').src.startsWith('data:image/png'));
tap('svg-match'); assert.match(el('svg-status').textContent,/You reported/);
tap('svg-different'); assert.match(el('svg-status').textContent,/blank or different/);
for(const id of ['test-grid','test-svg','test-refresh','test-resume']) { tap(id+'-back'); assert.equal(el('check').style.display,'block'); }
dom.window.close();
dom=load(new Error('blocked'));tap('resume-start');answer(2);tap('count-next');
assert.equal(el('count-progress').textContent,'Question 2 of 3');
assert.match(el('resume-status').textContent,/could not be saved/);
dom.window.close();
console.log('PASS: ES5, real counting restoration (answered/retry/completed), score integrity, malformed/blocked storage fallback, scoped deletion, nine-cell toggles, finite local updates, SVG comparison structure and report controls. Device rendering remains pending.');
