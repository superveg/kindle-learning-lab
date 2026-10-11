/* Focused continuity check: real embedded pages, fresh JS heaps, shared storage. */
const fs=require('fs'),vm=require('vm'),assert=require('assert/strict'),{JSDOM}=require('jsdom');
const data=JSON.parse(fs.readFileSync('learning/content.json','utf8'));
const scope={};vm.createContext(scope);vm.runInContext(fs.readFileSync('learning/generator.js','utf8'),scope);
const gen=scope.LearningGenerator;
// Independent semantic oracle; do not reuse the runtime signature/content code.
function semantic(q){if(q.stages)return q.stages.map(semantic);if(q.nodes)return q.nodes;return {mode:q.mode,prompt:q.prompt||'',narration:q.narration||'',scene:q.scene||[],items:q.items||[],constraints:q.constraints||[],accepted:q.accepted||[],options:(q.options||[]).map((o,i)=>[o,(q.answers||[]).includes(i)]).sort((a,b)=>JSON.stringify(a).localeCompare(JSON.stringify(b))),observation:q.observation||''};}
function tap(d,prefix){const b=[...d.querySelectorAll('button')].find(x=>(x.getAttribute('aria-label')||x.textContent).startsWith(prefix));assert(b,prefix);b.click();}
function open(html,saved,rng,blocked=false){return new JSDOM(html,{url:'https://example.test/kindle-learning-lab/',runScripts:'dangerously',beforeParse(w){w.Math.random=rng;for(const [k,v] of Object.entries(saved))w.localStorage.setItem(k,v);if(blocked){w.Storage.prototype.getItem=function(){throw Error('blocked');};w.Storage.prototype.setItem=function(){throw Error('blocked');};}}});}
function snapshot(w){const out={};for(let i=0;i<w.localStorage.length;i++){const k=w.localStorage.key(i);out[k]=w.localStorage.getItem(k);}return out;}
let presented=0,reloads=0;
for(const kind of ['constant','seeded']){
 let seed=4719;const rng=kind==='constant'?()=>0:()=>((seed=(Math.imul(seed,1664525)+1013904223)>>>0)/4294967296);
 for(const [sub,cfg] of Object.entries(data)){
  const html=fs.readFileSync(sub+'.html','utf8');let saved={'unrelated-key':'preserve-me'};
  for(let l=1;l<=6;l++)for(let f=0;f<3;f++){
   const recent=[];
   // Three five-question visits, reconstructing the whole page between visits.
   for(let visit=0;visit<3;visit++){
    const dom=open(html,saved,rng),d=dom.window.document;tap(d,'Level '+l+':');
    for(let n=0;n<5;n++){
     tap(d,'Activity '+(f+1)+':');const p=d.getElementById('play');
     const source=cfg.levels[l-1].families[f].tasks.find(q=>q.id===p.getAttribute('data-task-id'));
     const q=gen.materialize(source,Number(p.getAttribute('data-variant')));
     // Canonical full content, not the runtime hash, is the duplicate oracle.
     const canonical=JSON.stringify(semantic(q));assert(!recent.slice(-10).includes(canonical),[kind,sub,l,f,visit,n].join('/'));
     recent.push(canonical);presented++;tap(d,'Back');
    }
    saved=snapshot(dom.window);assert.equal(saved['unrelated-key'],'preserve-me');
    const h=JSON.parse(saved['kll-'+sub+'-recent-v1']);assert(Object.values(h).every(a=>a.length<=10));
    assert.equal(h[l+'-'+f].length,Math.min(recent.length,10));dom.window.close();if(visit<2)reloads++;
   }
  }
 }
}
// Storage failure must keep the in-page window; no cross-reload promise is made.
let fallback=0;
for(const sub of Object.keys(data)){
 const html=fs.readFileSync(sub+'.html','utf8');
 for(const saved of [{}, {['kll-'+sub+'-recent-v1']:'not-json'}, {['kll-'+sub+'-recent-v1']:'{"1-0":[null,123,"valid"],"bad-key":["x"]}'}]){
  const blocked=Object.keys(saved).length===0,dom=open(html,saved,()=>0,blocked),d=dom.window.document,seen=[];
  tap(d,'Level 1:');for(let n=0;n<15;n++){tap(d,'Activity 1:');const p=d.getElementById('play'),q=data[sub].levels[0].families[0].tasks.find(q=>q.id===p.getAttribute('data-task-id'));const s=JSON.stringify(semantic(gen.materialize(q,Number(p.getAttribute('data-variant')))));assert(!seen.slice(-10).includes(s));seen.push(s);tap(d,'Back');fallback++;}dom.window.close();
 }
}
console.log('PASS:',presented,'presentations across all 90 families with constant/seeded RNG;',reloads,'fresh-page boundaries;',fallback,'storage-failure/malformed-history presentations; unrelated storage preserved. These visits leave questions unanswered; learning-repeat.cjs covers solved Next rounds.');
