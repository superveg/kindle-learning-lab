/* Independent representation checks and real DOM interaction for depth/breadth tasks. */
const fs=require('fs'),vm=require('vm'),assert=require('assert/strict'),{JSDOM}=require('jsdom'),acorn=require('acorn');
process.env.KLL_ORACLE_ONLY='1';const {expected}=require('./extended-quality.cjs');delete process.env.KLL_ORACLE_ONLY;
const context={Math:Object.create(Math)};let seed=5189;context.Math.random=()=>((seed=(Math.imul(seed,1664525)+1013904223)>>>0)/4294967296);vm.createContext(context);
for(const file of ['learning/pictures.js','learning/higher-math.js']){const code=fs.readFileSync(file,'utf8');acorn.parse(code,{ecmaVersion:5});vm.runInContext(code,context);}
let diagrams=0;const modelDom=new JSDOM('');
for(let k=0;k<16;k++)for(let l=k>=12?6:7;l<=12;l++)for(let v=0;v<3;v++)for(let sample=0;sample<8;sample++){
 const q=JSON.parse(JSON.stringify(context.HigherMath.task(k,l,v))),o=q.oracle;assert.deepEqual(q.answers,expected(q));assert(q.scene.length||(q.mode==='multi'&&q.options.every(c=>c.diagram)),'There must be a mathematical representation');
 if(o.type==='transform'&&!o.inverse){let cells=o.source.slice();const grids=q.scene.filter(c=>c.grid);assert.deepEqual(grids[0].grid.cells,cells);for(let i=0;i<o.code.length-1;i++){cells=cells.map(cell=>{let x=cell%o.size,y=Math.floor(cell/o.size);const op=o.code[i];if(op==='R')[x,y]=[o.size-1-y,x];else if(op==='H')x=o.size-1-x;else y=o.size-1-y;return y*o.size+x;}).sort((a,b)=>a-b);assert.deepEqual(grids[i+1].grid.cells,cells,'Every shown intermediate transformation must be exact');}}
 for(const c of q.scene){if(!c.model)continue;const m=c.model,d=m.data,html=context.HigherMath.modelHTML(c),doc=modelDom.window.document;doc.body.innerHTML=html;
  if(m.type==='array'){assert.equal(doc.querySelectorAll('.array-row').length,d.rows);assert.equal(doc.querySelectorAll('.array-cell').length,d.rows*d.columns);assert.equal(doc.querySelectorAll('.model-dot').length,d.rows*d.columns+(d.extra||0));if(d.split)assert.equal(doc.querySelectorAll('.array-split').length,d.rows);}
  if(m.type==='groups'){assert.equal(doc.querySelectorAll('.model-group').length,d.rows.length);assert.equal(doc.querySelectorAll('.model-dot').length,d.rows.filter(x=>x!=='?').reduce((a,b)=>a+b,0)+d.extra);}
  if(m.type==='place'){assert.equal(doc.querySelectorAll('.model-ten').length,d.tens);assert.equal(doc.querySelectorAll('.model-dot').length,d.ones);if(o.type==='place-depth')assert.equal(10*d.tens+d.ones,o.operation==='missing'?o.a+o.b:o.a);}
  if(m.type==='ruler'){const ticks=[...doc.querySelectorAll('.ruler-tick')].map(x=>Number(x.textContent));for(let i=0;i<ticks.length-1;i++)assert.equal(ticks[i+1]-ticks[i],d.step);assert.equal(ticks[d.start+d.length]-ticks[d.start],Number(q.options[q.answers[0]].text));}
  if(m.type==='rectangle'&&d.mode==='tiles'){assert.equal(parseInt(doc.querySelector('.measure-square').style.width),d.cellSize||36);if(o.operation==='same-area')assert.equal(d.cellSize,24);assert.equal(doc.querySelectorAll('.measure-square').length,d.w*d.h);assert.equal(doc.querySelectorAll('.cut').length,(d.cutW||0)*(d.cutH||0));if(o.operation==='composite')assert.equal(doc.querySelectorAll('.measure-square:not(.cut)').length,Number(q.options[0].text));}
  if(m.type==='chart'){const rows=[...doc.querySelectorAll('.chart-row')];assert.equal(rows.length,3);for(let i=0;i<3;i++)assert.equal(rows[i].querySelectorAll('.model-dot').length,d.counts[i]==='?'?0:d.counts[i]);assert(doc.querySelector('.chart-key').textContent.includes(String(d.scale)));}
  if(m.type==='bars'){const pieces=[...doc.querySelectorAll('.model-bar-piece')];assert.equal(pieces.length,d.rows.reduce((a,b)=>a+b.parts.length,0));const unknown=pieces.filter(x=>x.textContent==='B ?');if(unknown.length>1)for(const x of unknown)assert.equal(x.style.width,unknown[0].style.width);}
  diagrams++;
 }
 if(o.type==='place-depth'&&o.operation==='carry')assert(o.a%10+o.b>=10);
 if(o.type==='place-depth'&&o.operation==='borrow')assert(o.a%10<o.b);
 if(o.type==='time-lab'&&l===6)assert.equal(Math.floor(o.start/60),Math.floor(o.end/60));
 if(o.type==='time-lab'&&l===7)assert(Math.floor(o.end/60)>Math.floor(o.start/60));
}
modelDom.window.close();
const raw=fs.readFileSync('math.html','utf8');acorn.parse(raw.match(/<script>([\s\S]*?)<\/script>/)[1],{ecmaVersion:5});
const html=raw.replace('}());</script>','window.__depth={open:function(k,l,v){kind=k;age=l+2;round=v;renderQuestion();},task:function(){return JSON.parse(JSON.stringify(adv.task));}};}());</script>');
for(const blocked of [false,true]){
 const dom=new JSDOM(html,{runScripts:'dangerously',url:'https://example.test/math.html',beforeParse(w){if(blocked)Object.defineProperty(w,'localStorage',{get(){throw Error('blocked');}});}}),w=dom.window,d=w.document;
 for(let k=0;k<16;k++)for(let l=k>=12?6:7;l<=12;l++){
  w.__depth.open(k,l,1);const q=w.__depth.task(),answers=expected(q),before=d.querySelector('#scene').innerHTML;
  const hint=d.querySelector('[aria-label="Show a thinking step"]');assert(hint);hint.click();assert(d.querySelector('#wide-thinking-step').textContent);const hintText=d.querySelector('#wide-thinking-step').textContent;hint.click();assert(d.querySelector('#wide-thinking-step').textContent);
  const afterHint=d.querySelector('#scene').innerHTML;const wrong=q.options.findIndex((_,i)=>!answers.includes(i));d.querySelector('[aria-label^="Extended option '+(wrong+1)+':"]').click();assert.equal(d.querySelector('#scene').innerHTML,afterHint);assert.deepEqual(w.__depth.task(),q);
  for(const i of answers)d.querySelector('[aria-label^="Extended option '+(i+1)+':"]').click();assert.equal(d.querySelector('#feedback').textContent,'✓');assert(!d.querySelector('#wide-guidance'));assert(!d.querySelector('#scene button'));assert(!d.querySelector('#choices button'));assert(d.querySelector('.math-result'));
  d.querySelector('#next').click();assert.equal(d.querySelector('#stage').getAttribute('aria-label'),'Level '+l);assert(!d.querySelector('.math-result'));assert(!d.querySelector('#wide-thinking-step'));
 }
 dom.window.close();
}
console.log('PASS:',diagrams,'exact model representations; all 100 advanced/new entries with hints, stable retry, passive completion and manual continuation under normal/blocked storage; ES5.');
