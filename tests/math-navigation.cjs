const fs=require('node:fs'),assert=require('node:assert/strict'),{JSDOM}=require('jsdom');
const html=fs.readFileSync('math.html','utf8');let randomCalls=0;
const dom=new JSDOM(html,{runScripts:'dangerously',url:'https://example.test/math.html',beforeParse(w){w.Math.random=()=>{randomCalls++;return .37;};}}),d=dom.window.document;
const id=x=>d.getElementById(x),topics=()=>[...d.querySelectorAll('#activities button')],visible=()=>topics().filter(b=>b.style.display!=='none');
assert.equal(visible().length,6);assert(id('topic-prev').disabled);assert(!id('topic-next').disabled);
id('topic-next').click();assert.equal(id('topic-page').textContent,'2 / 2');assert.equal(visible()[0].getAttribute('aria-label'),'Find the matching shape');assert(id('topic-next').disabled);
assert(!d.querySelector('.topic-progress'));assert.equal(randomCalls,0,'Menu navigation must not consume practice randomness');
let examples=0;
for(let k=0;k<12;k++){
 topics()[k].click();const levels=[...d.querySelectorAll('#levels button')];assert.equal(levels.length,k<9?6:12-k);
 for(const b of levels){const picture=b.querySelector('.level-preview');assert(picture);assert(picture.getAttribute('aria-label').startsWith('Example: '));assert(picture.textContent.trim()||picture.querySelector('img,.preview-board'));assert(!picture.querySelector('button,a,input'));examples++;}
 assert(id('level-note').closest('details'),'Adult explanations are collapsed');id('back').click();assert.equal(id('topic-page').textContent,'2 / 2');
}
assert.equal(examples,60);assert.equal(randomCalls,0);
id('topic-prev').click();topics()[0].click();d.querySelector('#levels button').click();assert.equal(id('session-meta').style.display,'table-cell');assert(id('stage').closest('#toolbar'));assert(id('progress').closest('#toolbar'));
assert.equal(d.querySelectorAll('#stage').length,1);assert.equal(d.querySelectorAll('#progress').length,1);
while(d.querySelector('#scene button'))d.querySelector('#scene button').click();
assert.equal(id('feedback').textContent,'✓');assert.equal(id('next').textContent,'→');assert(!id('next').querySelector('.steps'));assert(id('advance').querySelector('.steps'));assert(!id('advance').textContent.includes('→'));
id('next').click();assert.equal(id('stage').getAttribute('aria-label'),'Level 1');assert.match(id('progress').getAttribute('aria-label'),/^Question 2;/);
while(d.querySelector('#scene button'))d.querySelector('#scene button').click();id('advance').click();assert.equal(id('stage').getAttribute('aria-label'),'Level 2');assert.match(id('progress').getAttribute('aria-label'),/^Question 1;/);
id('back').click();assert.equal(id('session-meta').style.display,'none');assert(d.querySelector('#levels .played-mark'));
dom.window.close();console.log('PASS: six-topic paging, 60 passive level examples without RNG consumption, played marks, compact toolbar, distinct continuation and level advance.');
