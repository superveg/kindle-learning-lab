const fs=require('fs'),assert=require('assert/strict'),{JSDOM}=require('jsdom'),acorn=require('acorn');
const content=JSON.parse(fs.readFileSync('learning/content.json','utf8'));
function permutations(a){if(!a.length)return [[]];return a.flatMap((x,i)=>permutations(a.filter((_,j)=>j!==i)).map(r=>[x,...r]));}
function independentOrder(s){const permutationsOfIds=permutations(s.items.map((_,i)=>i));return permutationsOfIds.filter(ids=>s.constraints?s.constraints.every(([a,b])=>ids.indexOf(a)<ids.indexOf(b)):(s.accepted||[s.items.map(c=>c.value||c.text||c.label)]).some(v=>JSON.stringify(v)===JSON.stringify(ids.map(i=>s.items[i].value||s.items[i].text||s.items[i].label))));}
let samples=0,questions=0;
for(const [subject,cfg] of Object.entries(content)){
 assert.equal(cfg.levels.length,6);const html=fs.readFileSync(subject+'.html','utf8');acorn.parse(html.match(/<script>([\s\S]*?)<\/script>/)[1],{ecmaVersion:5});
 for(const l of cfg.levels){assert.equal(l.families.length,3);for(const f of l.families){assert(f.tasks.length>=2);for(const q of f.tasks){samples++;for(const s of q.stages||[q]){if(s.mode==='branch'){for(const [k,n] of Object.entries(s.nodes)){if(!n.end){assert(n.options.length);for(const o of n.options)assert(s.nodes[o.to]);}}continue;}if(s.mode==='order'){assert(independentOrder(s).length>0);assert(s.items.length>=2);continue;}assert(s.options.length>=2);assert(s.answers.length);assert(new Set(s.answers).size===s.answers.length);for(const i of s.answers)assert(s.options[i]);if(s.mode==='multi')assert(s.answers.length<s.options.length);}}}}
 const dom=new JSDOM(html,{runScripts:'dangerously',url:'https://example.test/'+subject+'.html'}),w=dom.window,d=w.document;
 function btn(label){return [...d.querySelectorAll('button')].find(b=>b.getAttribute('aria-label')===label||b.textContent===label);}
 function tap(label){assert(btn(label),label);btn(label).click();}
 function solve(q){for(const s of q.stages||[q]){
  if(s.mode==='branch'){let node='start',seen=new Set();while(!q.nodes[node].end){assert(!seen.has(node),'No branch loops');seen.add(node);let o=q.nodes[node].options[0];tap('Story choice 1: '+o.text);node=o.to;}continue;}
  if(s.mode==='predict'){tap('Predict option 1: '+s.options[0].label);tap('Observe →');continue;}
  if(s.mode==='order'){const ids=independentOrder(s).at(-1);for(const id of ids)tap('Add card '+(id+1)+': '+s.items[id].label);continue;}
  const wrong=s.options.findIndex((_,i)=>!s.answers.includes(i));if(wrong>=0){const before=d.getElementById('scene').innerHTML;tap('Choose option '+(wrong+1)+': '+s.options[wrong].label);assert(d.getElementById('feedback').textContent.includes('↺'));assert.equal(d.getElementById('scene').innerHTML,before,'Retry keeps the task');}
  for(const id of s.answers)tap('Choose option '+(id+1)+': '+s.options[id].label);
 }}
 for(let l=1;l<=6;l++){
  tap('Level '+l+': '+cfg.levels[l-1].name);
  for(let f=0;f<3;f++){
   tap('Activity '+(f+1)+': '+cfg.levels[l-1].families[f].name);
   // Observe bank without relying on closure state: choices/prompts identify the displayed authored sample.
   let last=null,seen=new Set(),recentContent=[];
   for(let n=0;n<100;n++){
    let q=cfg.levels[l-1].families[f].tasks.find(q=>q.id===d.getElementById('play').getAttribute('data-task-id'));assert(q,'Rendered task matches its authored bank');
    assert.notEqual(q.id,last,'Avoid adjacent repeats where bank has alternatives');last=q.id;seen.add(q.id);
    const materialized=w.LearningGenerator.materialize(q,Number(d.getElementById('play').getAttribute('data-variant'))),sig=w.LearningGenerator.signature(materialized);assert(!recentContent.slice(-10).includes(sig),'No content repeats in previous ten');recentContent.push(sig);const progress=d.getElementById('progress').textContent;
    d.getElementById('next').click();assert.equal(d.getElementById('progress').textContent,progress,'No unanswered skip');
    const hint=btn('? Hint');if(hint){hint.click();assert(d.querySelector('.hint'));}
    solve(q);assert(d.getElementById('feedback').textContent.startsWith('✓'));assert(!d.getElementById('next').hidden);assert.equal(d.querySelectorAll('#choices button').length,0,'Completed choices become passive');assert.equal(d.getElementById('tools').children.length,0,'Completed tasks clear Undo and hints');assert(d.getElementById('cue').textContent.includes(subject==='chinese'?'完成':'Complete'));assert(d.getElementById('progress').textContent.includes('Level '+l));
    d.getElementById('next').click();questions++;
   }
   assert(seen.size>=2);tap('Back');assert(!d.getElementById('families').hidden);
  }tap('Back');assert(!d.getElementById('levels').hidden);
 }
 dom.window.close();
 // Storage denied must never prevent entry.
 const blocked=new JSDOM(html,{runScripts:'dangerously',url:'https://example.test',beforeParse(win){Object.defineProperty(win,'localStorage',{get(){throw Error('denied');}});}});assert.equal(blocked.window.document.querySelectorAll('.level').length,6);blocked.window.close();
 console.log('PASS:',subject,'six levels, three families each, 1800 continued questions, passive completion, retries and storage fallback.');
}
// Relation constraints must accept several legal orders, rather than a single witness.
const openPlan=content.logic.levels[4].families[1].tasks[0];assert.equal(independentOrder(openPlan).length,2);
console.log('PASS:',samples,'authored examples;',questions,'generated selections.');
