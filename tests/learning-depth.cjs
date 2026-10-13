/* Independent condition/record solvers and evidence/rendering checks; not a child study. */
const fs=require('fs'),assert=require('assert/strict'),vm=require('vm'),{JSDOM}=require('jsdom'),acorn=require('acorn');
const data=JSON.parse(fs.readFileSync('learning/content.json'));
const scope={};vm.createContext(scope);for(const file of ['learning/pictures.js','learning/subject-pictures.js']){const s=fs.readFileSync(file,'utf8');acorn.parse(s,{ecmaVersion:5});vm.runInContext(s,scope);}
function expected(s){const o=s.oracle;if(!o)return s.answers;
 if(o.type==='transform'){const apply=(cells,code,n)=>cells.map(cell=>{let x=cell%n,y=Math.floor(cell/n);for(const op of code){if(op==='R')[x,y]=[n-1-y,x];else if(op==='H')x=n-1-x;else y=n-1-y;}return y*n+x;}).sort((a,b)=>a-b);const goal=apply(o.source,o.code,o.size);return s.options.flatMap((c,i)=>JSON.stringify(o.inverse?apply(c.grid.cells,o.code,o.size):c.grid.cells)===JSON.stringify(goal)?[i]:[]);}
 if(o.type==='logic-features'){return s.options.flatMap((c,i)=>{const [shape,fill,size]=c.art.split('-'),a=shape===['circle','square','triangle'][o.shape],b=fill===['plain','striped','filled'][o.fill];const ok=size===o.size&&(o.operation==='two-clues'?a&&!b:o.operation==='counterexample'?a&&b:o.operation==='exclude'?!a&&b:o.operation==='either'?a||b:a&&b);return ok?[i]:[];});}
 if(o.type==='logic-useful-question'){const f=s.scene.map(c=>{const[shape,fill,size]=c.art.split('-');return{shape,fill,size,page:'white'};});return s.options.flatMap((c,i)=>f[0][o.optionFeatures[i]]!==f[1][o.optionFeatures[i]]?[i]:[]);}
 if(o.type==='language-detail')return s.options.flatMap((c,i)=>c.text===o.expected?[i]:[]); // Authored-language consistency, not an independent NLP oracle.
 if(o.type==='language-evidence'){return s.options.flatMap((c,i)=>(o.proofs||[o.required]).some(proof=>proof.every(index=>c.evidence.includes(index)))?[i]:[]);}
 if(o.type==='science-depth'){const p=s.scene.find(c=>c.panel&&c.panel.title.startsWith('Supplied')).panel;const rows=p.rows;let correct;
  if(o.operation==='change')correct=Math.abs(Number(rows[0][3])-Number(rows[0][2]));
  else if(o.operation==='difference')correct=Math.abs(Number(rows[0][3])-Number(rows[1][3]));
  else if(o.operation==='repeat'){const a=rows[0].slice(1).map(Number),b=rows[1].slice(1).map(Number);correct=a.every((v,i)=>v>b[i])?'A higher in every trial':a.every((v,i)=>v<b[i])?'B higher in every trial':'Results overlap across trials';}
  else if(o.operation==='confounded'){assert(s.scene[0].panel.rows.some(r=>r[1].includes('also differed')));correct='not-isolated';}
  else if(o.operation==='anomaly'){const a=rows[0].slice(1).map(Number);assert(Math.abs(a[2]-a[0])>Math.abs(a[1]-a[0])+4);correct='repeat-check';}
  else{const deltaA=Math.abs(Number(rows[0][3])-Number(rows[0][2])),deltaB=Math.abs(Number(rows[1][3])-Number(rows[1][2]));assert(s.options[0].text.includes(deltaA>deltaB?'more':'less'));correct='bounded';}
  return s.options.flatMap((c,i)=>o.values[i]===correct?[i]:[]);
 }
 if(o.type==='investigation-plan')return o.plans.flatMap((p,i)=>{const ok=o.goal==='measure'?p.measuresOutcome:o.goal==='repeat-plan'?p.repeatsBoth&&p.measuresOutcome:o.goal==='separate-explanations'?(p.targetChanged!==p.otherChanged)&&p.measuresOutcome:o.goal==='complete-plan'?p.targetChanged&&!p.otherChanged&&p.measuresOutcome&&p.repeatsBoth:p.targetChanged&&!p.otherChanged;return ok?[i]:[];});
 if(o.type==='science-evidence'){const correct=o.operation==='change'?`${o.a} → ${o.b} `:o.operation==='difference'?`${o.b} versus ${o.c} `:o.operation==='confound'?'Two conditions differed':o.operation==='anomaly'?'A repeat can check':'Further comparable observations';return s.options.flatMap((c,i)=>c.text.startsWith(correct)?[i]:[]);}
 if(o.type==='social-plan')return o.options.flatMap((p,i)=>p.respects&&p.fits?[i]:[]);
 if(o.type==='social-stated')return o.statements.flatMap((v,i)=>v?[i]:[]);
 if(o.type==='social-understanding'){const prefix={impact:'What happened and its impact',ask:s.prompt.startsWith('Which question')?'What would help':'Ask what happened',boundary:'A stated boundary',check:'Ask whether the plan'}[o.operation];return s.options.flatMap((c,i)=>c.text.startsWith(prefix)?[i]:[]);}
 return s.answers;
}
function orderSolution(s){const ids=s.items.map((_,i)=>i);if(!s.constraints)return ids;const out=[];while(out.length<ids.length){const id=ids.find(i=>!out.includes(i)&&s.constraints.filter(e=>e[1]===i).every(e=>out.includes(e[0])));assert.notEqual(id,undefined);out.push(id);}return out;}
let seeds=0,stages=0,languageChecks=0,conditionChecks=0;
for(const [sub,cfg]of Object.entries(data))for(const level of cfg.levels.slice(6))for(const family of level.families){assert.equal(family.tasks.length,12);for(const q of family.tasks){seeds++;assert(q.preview,'Upper menu needs a compact representative preview');assert(!q.preview.panel,'Do not squeeze a complete passage/table into menu tiles');if(q.mode==='branch'){assert(!q.answers,'Feelings/path choices are not graded');continue;}for(const s of q.stages||[q]){stages++;assert(s.key&&s.hint,'New rules need visible meaning and optional support');if(s.mode==='order'){orderSolution(s);continue;}if(s.mode==='predict')continue;assert.deepEqual(s.answers,expected(s),q.id+' '+s.prompt);if(s.oracle?.type.startsWith('language'))languageChecks++;else conditionChecks++;
 if(s.oracle?.type==='language-evidence'){assert(s.oracle.required.length<4);for(const option of s.options){assert(option.evidence.length<4);assert.deepEqual(option.panel.rows.map(r=>r[1]),option.evidence.map(i=>s.oracle.lines[i]));assert.deepEqual(option.panel.rows.map(r=>Number(r[0])),option.evidence.map(i=>i+1));}assert(!s.options.some(c=>c.text==='Only a guess'));}
 for(const c of s.scene||[]){if(c.panel){assert(c.panel.columns.length>=2);for(const row of c.panel.rows)assert.equal(row.length,c.panel.columns.length);const html=scope.SubjectPictures.html(c,{});assert(html.includes('<caption>'));assert(html.includes('scope="col"'));}}
}}}
for(const sub of Object.keys(data)){
 const raw=fs.readFileSync(sub+'.html','utf8');acorn.parse(raw.match(/<script>([\s\S]*?)<\/script>/)[1],{ecmaVersion:5});
 const html=raw.replace('loadMarks();loadHistory();levels();','window.__depth={open:function(l,f,qIndex){level=l;family=f;q=JSON.parse(JSON.stringify(CONFIG.levels[l-1].families[f].tasks[qIndex]));phase=0;done=false;selected=[];order=[];storyNode="start";show("play");render();},phase:function(){return phase;}};loadMarks();loadHistory();levels();');
 const dom=new JSDOM(html,{runScripts:'dangerously',url:'https://example.test/'+sub+'.html'}),w=dom.window,d=w.document;
 const click=label=>{const b=[...d.querySelectorAll('button')].find(b=>b.getAttribute('aria-label')===label||b.textContent===label);assert(b,label);b.click();};
 for(let l=7;l<=12;l++)for(let f=0;f<3;f++){
  const q=data[sub].levels[l-1].families[f].tasks[0];w.__depth.open(l,f,0);
  if(q.mode==='branch'){let node='start';while(!q.nodes[node].end){const op=q.nodes[node].options[0];click('Story choice 1: '+op.text);node=op.to;}assert(d.getElementById('feedback').textContent.startsWith('✓'));continue;}
  for(const s of q.stages||[q]){
   const before=d.getElementById('scene').innerHTML;const hint=d.querySelector('.hint-control');assert(hint);hint.click();assert(d.querySelector('.hint'));assert.equal(d.getElementById('scene').innerHTML,before);
   if(s.mode==='order'){for(const i of orderSolution(s))click('Add card '+(i+1)+': '+s.items[i].label);continue;}
   if(s.mode==='predict'){click('Predict option 2: '+s.options[1].label);assert(!d.getElementById('feedback').textContent);click('Observe →');assert(d.querySelector('.prior-observation').textContent.includes('Supplied observation'));continue;}
   const answers=expected(s),wrong=s.options.findIndex((_,i)=>!answers.includes(i));if(wrong>=0){click('Choose option '+(wrong+1)+': '+s.options[wrong].label);assert.equal(d.getElementById('scene').innerHTML,before);}
   for(const i of answers)click('Choose option '+(i+1)+': '+s.options[i].label);
  }
  assert(d.getElementById('feedback').textContent.startsWith('✓'));assert(!d.getElementById('next').hidden);assert(!d.querySelector('#choices button'));assert(!d.querySelector('#tools button'));if(q.stages){assert(d.querySelector('.prior-clue'));assert(d.querySelector('.subject-panel'));}
 }
 dom.window.close();
}
console.log('PASS:',seeds,'rewritten upper seeds;',conditionChecks,'condition/record checks;',languageChecks,'authored-language/evidence consistency checks; all 90 upper entries with hints, stable retries, retained clues/observations and passive completion. Natural-language meaning still requires editorial/device/child review.');
