const fs=require('fs'),assert=require('assert/strict'),{JSDOM}=require('jsdom');
const data=JSON.parse(fs.readFileSync('learning/content.json','utf8'));
let branches=0;
for(const [id,cfg] of Object.entries(data)){
 let ids=new Set();
 for(const lev of cfg.levels)for(const fam of lev.families)for(const q of fam.tasks){
  assert(!ids.has(q.id));ids.add(q.id);
  if(q.mode==='branch'){
   const seen=new Set();function walk(key,path){assert(!path.includes(key),'No cycle');let node=q.nodes[key];assert(node);seen.add(key);if(node.end){branches++;return;}assert(node.options.length>=2);for(const opt of node.options)walk(opt.to,[...path,key]);}walk('start',[]);assert.equal(seen.size,Object.keys(q.nodes).length,'No unreachable authored story nodes');
  }
  for(const s of q.stages||[q]){assert(s.mode);if(s.mode==='choice'||s.mode==='multi'){
   const pictures=s.options.filter(x=>x.art);if(s.answers.length===1&&pictures.length===s.options.length){const correct=s.options[s.answers[0]];assert(!s.options.some((o,i)=>i!==s.answers[0]&&o.art===correct.art&&o.scale===correct.scale),'A picture answer cannot also be an identical wrong picture');}
  }}
 }
}
// Independent visible-image equality oracle for exact-match activities.
for(const q of data.logic.levels[0].families[0].tasks){const expected=q.options.map((o,i)=>o.art===q.scene[0].art?i:-1).filter(i=>i>=0);assert.deepEqual(q.answers,expected);}
// Independent logical-feature predicates for representative two-clue deduction.
for(const q of data.logic.levels[3].families[0].tasks){const expected=q.options.map((o,i)=>{let [shape,pattern]=o.art.split('-');return (q.prompt.includes('Round')?shape==='circle'&&pattern!=='filled':pattern==='striped'&&shape!=='circle')?i:-1;}).filter(i=>i>=0);assert.deepEqual(q.answers,expected);}
const dom=new JSDOM(fs.readFileSync('english.html','utf8'),{runScripts:'dangerously',url:'https://example.test'}),w=dom.window,d=w.document;
function tap(prefix){let b=[...d.querySelectorAll('button')].find(b=>(b.getAttribute('aria-label')||b.textContent).startsWith(prefix));assert(b,prefix);b.click();}
tap('Level 3:');tap('Activity 1:');
// Both cat and book are valid print-construction samples; deliberately choose a reversed order.
const id=d.getElementById('play').getAttribute('data-task-id'),q=data.english.levels[2].families[0].tasks.find(q=>q.id===id);
for(let i=q.items.length-1;i>=0;i--)tap('Add card '+(i+1)+':');assert(d.getElementById('feedback').textContent.startsWith('↺'));assert(d.getElementById('next').hidden);tap('↶ Undo');assert.equal(d.getElementById('feedback').textContent,'');assert.equal(d.querySelectorAll('#work .card').length,q.items.length-1);
// Undo the whole attempt; put duplicate o tiles in interchangeable positions.
while(d.querySelectorAll('#work .card').length)tap('↶ Undo');let sequence=q.items.map((_,i)=>i);if(q.items.length===4)sequence=[0,2,1,3];for(const i of sequence)tap('Add card '+(i+1)+':');assert(d.getElementById('feedback').textContent.startsWith('✓'));dom.window.close();
// Every asset reference exists and icons meant to differ actually have different bytes.
for(const id of Object.keys(data)){
 const html=fs.readFileSync(id+'.html','utf8');const art=JSON.parse(html.match(/var ART=(\{.*?\});/s)[1]);
 function check(x){if(x&&typeof x==='object'){if(x.art)assert(art[x.art],x.art);for(const v of Object.values(x))check(v);}}
 check(data[id]);assert.notEqual(art.wash,art.dry);assert.notEqual(art.eat,art.run);assert.notEqual(art.mountain,art.ramp);
 assert(!/<script[^>]+src=/.test(html),'No task-time JS requests');
}
console.log('PASS: independent picture/feature oracles, authored answer ambiguity, all',branches,'story ending paths, rejected ordering/Undo/repeated letters, and distinct complete asset references.');
