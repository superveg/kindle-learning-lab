const assert=require('node:assert/strict');
const fs=require('node:fs');const {JSDOM}=require('jsdom');const acorn=require('acorn');
const html=fs.readFileSync('math.html','utf8');acorn.parse(html.match(/<script>([\s\S]*?)<\/script>/)[1],{ecmaVersion:5});
function launch(blocked=false){return new JSDOM(html,{url:'https://example.test/kindle-learning-lab/math.html',runScripts:'dangerously',beforeParse(w){if(blocked)Object.defineProperty(w,'localStorage',{get(){throw Error('blocked')}})}});}
function tap(d,id){d.getElementById(id).click();}function children(d,id){return Array.from(d.getElementById(id).querySelectorAll('button'));}
for(const age of [3,4,5])for(let kind=0;kind<9;kind++){
 const dom=launch();const d=dom.window.document;children(d,'age-buttons')[age-3].click();assert.equal(children(d,'activities').length,9);children(d,'activities')[kind].click();
 for(let r=0;r<3;r++){
  assert.equal(d.getElementById('next').disabled,true);tap(d,'check');assert.equal(d.getElementById('next').disabled,true);
  const n=age===3?[2,3,4][r]:age===4?[4,5,6][r]:[6,8,10][r];const small=age===3?[1,2,3][r]:[3,4,5][r];
  if(kind===0){children(d,'workspace').forEach(b=>b.click());children(d,'choices').find(b=>b.textContent===String(n)).click();}
  if(kind===1)for(let i=0;i<n;i++)tap(d,'plus');
  if(kind===2){if(age===5)children(d,'choices').find(b=>b.textContent===String([1,0,2][r])).click();else children(d,'choices')[[2,1,0][r]].click();}
  if(kind===3){const bs=children(d,'choices');if(age===5&&r===2){for(let i=0;i<3;i++)bs[1].click();}else{for(let i=0;i<(r===2?2:1);i++)bs[r===1?0:1].click();}}
  if(kind===4)children(d,'choices').find(b=>b.getAttribute('aria-label')==='Choose '+r).click();
  if(kind===5)children(d,'choices').find(b=>b.getAttribute('aria-label')==='Choose '+r).click();
  if(kind===6){for(let i=0;i<(age===3?3:age===4?4:5);i++){tap(d,'item-'+i);children(d,'baskets')[i%2].click();}}
  if(kind===7){if(age===3)children(d,'choices')[1].click();else for(let i=0;i<small;i++)children(d,'choices')[1].click();}
  if(kind===8)children(d,'choices')[r].click();
  tap(d,'check');assert.equal(d.getElementById('next').disabled,false,`${age}/${kind}/${r}`);tap(d,'check');assert.equal(d.getElementById('next').disabled,false);tap(d,'next');
 }
 assert.equal(d.getElementById('next').style.display,'none');assert.equal(JSON.parse(dom.window.localStorage.getItem('kindle-math-v1'))[age+'-'+kind],true);tap(d,'back');assert.match(children(d,'activities')[kind].textContent,/✓/);children(d,'activities')[kind].click();assert.equal(d.getElementById('next').disabled,true);dom.window.close();
}
const blocked=launch(true);const d=blocked.window.document;children(d,'age-buttons')[0].click();assert.match(d.getElementById('storage-note').textContent,/unavailable/);children(d,'activities')[0].click();assert.equal(d.getElementById('play').style.display,'block');blocked.window.close();
console.log('PASS: ES5; 27 activities / 81 rounds; retries, answer checks, completion, restart and blocked-storage fallback.');
