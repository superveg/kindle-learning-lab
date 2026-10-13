/* Independent oracles for every new generated math combination and authored diagram. */
const fs=require('fs'),vm=require('vm'),assert=require('assert/strict'),{JSDOM}=require('jsdom'),acorn=require('acorn');
const scope={Math:Object.create(Math)};let seed=90210;scope.Math.random=()=>((seed=(Math.imul(seed,1664525)+1013904223)>>>0)/4294967296);vm.createContext(scope);
for(const path of ['learning/higher-math.js','learning/pictures.js']){const code=fs.readFileSync(path,'utf8');acorn.parse(code,{ecmaVersion:5});vm.runInContext(code,scope);}
function transformed(cells,code,n){return cells.map(cell=>{let x=cell%n,y=Math.floor(cell/n);for(const op of code){if(op==='H')x=n-1-x;else if(op==='V')y=n-1-y;else if(op==='R')[x,y]=[n-1-y,x];}return y*n+x;}).sort((a,b)=>a-b);}
function routeDistance(o){let todo=[[o.start,false,0,0]],seen=new Set();while(todo.length){let [p,key,w,d]=todo.shift();key=key||p===o.key;if(w<o.waypoints.length&&p===o.waypoints[w])w++;let tag=[p,key,w].join();if(seen.has(tag))continue;seen.add(tag);if(p===o.goal&&w===o.waypoints.length&&(o.key<0||key))return d;for(const delta of [-o.size,1,o.size,-1]){let next=p+delta;if(next<0||next>=o.size**2||(delta===1&&p%o.size===o.size-1)||(delta===-1&&p%o.size===0)||o.walls.includes(next)||(next===o.door&&!key))continue;todo.push([next,key,w,d+1]);}}throw Error('No legal route');}
function expected(q){let o=q.oracle,n,indices;
 if(o.type==='transform'){let answer=transformed(o.source,o.code,o.size);if(o.mask)answer=[...new Set([...answer,...o.mask])].filter(x=>answer.includes(x)!==o.mask.includes(x)).sort((a,b)=>a-b);return q.options.flatMap((c,i)=>JSON.stringify(o.inverse?transformed(c.grid.cells,o.code,o.size):c.grid.cells)===JSON.stringify(o.inverse?transformed(o.source,o.code,o.size):answer)?[i]:[]);}
 if(o.type==='relative-route'){let heading=o.facing,p=o.start;for(const m of o.moves){heading=(heading+m.turn+4)%4;for(let j=0;j<m.steps;j++){let next=p+[-o.size,1,o.size,-1][heading];assert(next>=0&&next<o.size**2);assert(heading!==1||p%o.size<o.size-1);assert(heading!==3||p%o.size>0);p=next;}}assert.equal(p,o.end);let wanted=o.inverse?o.start:p;return q.options.flatMap((c,i)=>Object.keys(c.grid.marks).includes(String(wanted))?[i]:[]);}
 if(o.type==='moves'){n=o.start;for(const m of o.moves)n+=({'↑':-o.size,'↓':o.size,'←':-1,'→':1}[m]);return q.options.flatMap((c,i)=>Object.keys(c.grid.marks).includes(String(n))?[i]:[]);}
 if(o.type==='features'){const f=i=>{const a=!!(i&1),b=!!(i&2),c=!!(i&4);return o.level===7?a!==b:o.level===8?i===o.target:o.level===9?!a&&(b||c):o.level===10?(!a&&!b)||(a&&c):o.level===11?a&&!b:i!==o.target&&a===!!(o.target&1)&&c===!!(o.target&4);};return q.options.flatMap((c,i)=>f(c.value)?[i]:[]);}

 if(o.type==='train-depth'){n=o.operation==='forward'?o.a+o.b-o.c:o.operation==='reverse'||o.operation==='reverse-three'?o.a:o.operation==='three'?o.a+o.b-o.c+o.d:o.operation==='transfer'?o.b+o.c:((o.b+2*o.c)-o.b)/2;}
 else if(o.type==='compare-depth'){n=o.operation==='equal-transfer'?((o.b+2*o.d)-o.b)/2:o.operation==='ratio-change'?o.b*o.factor-o.d:o.b;}
 else if(o.type==='place-depth'){n=o.operation==='carry'?o.a+o.b:o.operation==='borrow'?o.a-o.b:o.operation==='compensate'?10-o.b:o.operation==='missing'?o.a:o.operation==='exchange'?o.a-(o.tens-1)*10-10:o.a+o.b-10;}
 else if(o.type==='share-depth'){const total=o.groups*o.each+o.extra;n=o.operation==='share'||o.operation==='inverse'?Math.floor(total/o.groups):o.operation==='remainder'?total%o.groups:o.operation==='group-count'?(total-o.extra)/o.each:o.operation==='grouped'?total-total%o.groups:o.groups-total%o.groups;}
 else if(o.type==='track-depth'){const total=o.shortCount*o.short+(o.count-o.shortCount)*o.long;n=o.operation==='total'?total:o.operation==='short-count'?(o.count*o.long-total)/(o.long-o.short):o.operation==='long-count'?(total-o.count*o.short)/(o.long-o.short):o.operation==='count'?o.count:o.operation==='difference'?o.count*o.long-total:(total-o.shortCount*o.short)/(o.count-o.shortCount);}
 else if(o.type==='bar-lab'){n=o.operation==='part'||o.operation==='sum-difference'||o.operation==='sum-ratio'||o.operation==='difference-ratio'||o.operation==='extra-ratio'?o.unit:o.operation==='transfer'?((o.unit+2*o.extra)-o.unit)/2:o.n*o.unit-o.known;}
 else if(o.type==='measure-lab'){n=o.operation==='ruler'?((o.start+o.w)*o.step-o.start*o.step):o.operation==='units'?o.w*100+o.h*10:o.operation==='missing-side'?(2*(o.w+o.h)-2*o.h)/2:o.operation==='area'?o.w*o.h:o.operation==='composite'?o.w*o.h-o.cutW*o.cutH:2*(2*o.w+1)-2*(o.w+2);}
 else if(o.type==='data-lab'){const quantities=o.counts.map(x=>x*o.scale);n=o.operation==='read'?quantities[o.index]:o.operation==='difference'?Math.abs(quantities[0]-quantities[1]):o.operation==='combine'?quantities[0]+quantities[1]:o.operation==='scale'?quantities[0]/o.counts[0]:o.operation==='missing'?(quantities.reduce((a,b)=>a+b,0)-quantities[0]-quantities[1])/o.scale:Math.max(...quantities)-Math.min(...quantities);}
 else if(o.type==='time-lab'){const clock=t=>`${Math.floor(t/60)}:${String(t%60).padStart(2,'0')}`;let result=o.operation==='elapsed'?o.end-o.start:o.operation==='convert'?60+o.duration:o.operation==='end'?clock(o.start+o.duration):o.operation==='start'?clock(o.end-o.duration):o.operation==='exclude-break'?o.duration+o.other:clock(o.end-o.duration-o.wait-o.other);return q.options.flatMap((c,i)=>String(c.text)===String(result)?[i]:[]);}
 else if(o.type==='route')n=routeDistance(o);
 else if(o.type==='multiply-add')n=o.a*o.b+o.c;
 else if(o.type==='distributive')n=o.a*(o.b+o.c);
 else if(o.type==='missing-factor')n=(o.total-o.c)/o.a;
 else if(o.type==='balance')n=o.a+o.b-o.c;
 else if(o.type==='ratio')n=o.a*o.b;
 else if(o.type==='inverse-sub')n=(o.total+o.c)/o.b;
 else if(o.type==='inverse-affine')n=(o.total-o.offset)/o.factor;
 else if(o.type==='growing-step')n=o.start+o.step*6;
 else if(o.type==='sequence'){if(o.level===7){n=o.values[4]+o.b;}else if(o.level===8){n=o.values[4]+(o.values[2]-o.values[0]);}else if(o.level===10){n=o.values[4]+5;}else throw Error('Sequence');}
 else if(o.type==='fraction-add')n=o.a+o.b;
 else if(o.type==='fraction-sub')n=o.a-o.b;
 else if(o.type==='equivalence')n=o.numerator*o.to/o.from;
 else if(o.type==='fraction-groups')n=o.total;
 else if(o.type==='fraction-complement')n=o.d-o.a;
 else if(o.type==='fraction-missing')n=o.total-o.b;
 else throw Error(o.type);
 assert(Number.isInteger(n)&&n>=0);return q.options.flatMap((c,i)=>Number(c.text)===n?[i]:[]);
}
if(process.env.KLL_ORACLE_ONLY){module.exports={expected};return;}
let count=0;
for(let k=0;k<16;k++)for(let l=(k>=12?6:7);l<=12;l++)for(let v=0;v<3;v++)for(let s=0;s<20;s++){
 const q=JSON.parse(JSON.stringify(scope.HigherMath.task(k,l,v)));for(const c of q.scene){if(c.fraction){assert(c.fraction.filled>=0&&c.fraction.filled<=c.fraction.parts);}}assert(q.options.length>=2);assert(q.legend&&q.hints.length,'Every advanced task needs visible meaning and optional thinking support');assert.deepEqual(q.answers,expected(q),[k,l,v,s,q.prompt].join('/'));assert(q.answers.length<q.options.length);count++;
}
const data=JSON.parse(fs.readFileSync('learning/content.json'));let authored=0;
for(const [sub,cfg]of Object.entries(data))for(let l=6;l<12;l++)for(const f of cfg.levels[l].families)for(const q of f.tasks){authored++;for(const s of q.stages||[q]){
 const o=s.oracle;if(!o)continue;
 if(o.type==='transform'){const right=transformed(o.source,o.code,o.size),answers=s.options.flatMap((c,i)=>JSON.stringify(o.inverse?transformed(c.grid.cells,o.code,o.size):c.grid.cells)===JSON.stringify(o.inverse?right:right)?[i]:[]);assert.deepEqual(s.answers,answers);}
 if(o.type==='set'){const a=o.a,b=o.b;const right=o.op==='union'?[...new Set([...a,...b])]:o.op==='intersection'?a.filter(x=>b.includes(x)):o.op==='xor'?[...a.filter(x=>!b.includes(x)),...b.filter(x=>!a.includes(x))]:a.filter(x=>!b.includes(x));right.sort((a,b)=>a-b);assert.deepEqual(s.answers,s.options.flatMap((c,i)=>JSON.stringify(c.grid.cells)===JSON.stringify(right)?[i]:[]));}
 if(o.type==='subset')assert.deepEqual(s.answers,s.options.flatMap((c,i)=>c.grid.cells.every(x=>o.base.includes(x))!==o.counter?[i]:[]));
 if(o.type==='record'){const nums=s.scene[0].diagram.filter(x=>x.text!==undefined&&/^\d+$/.test(x.text)).map(x=>Number(x.text));let n;if(o.operation==='change')n=nums[1]-nums[0];else if(o.operation==='difference')n=nums[1]-nums[3];else if(o.operation==='repeat')n=nums[0]===nums[3]?'A = B':nums[0]>nums[3]?'A':'B';else if(o.operation==='reverse')n=nums[0];else if(o.operation==='exception')n=nums[3];else n=Math.min(...nums)+'–'+Math.max(...nums);assert.deepEqual(s.answers,s.options.flatMap((c,i)=>String(c.text)===String(n)?[i]:[]));}
 if(o.type==='fair'){const got=s.options[0].diagram.filter(x=>x.text!==undefined).map(x=>Number(x.text));const right=o.source.map((v,i)=>v+(i===o.changed?1:0));assert.deepEqual(got,right);for(const bad of s.options.slice(1))assert.notDeepEqual(bad.diagram.filter(x=>x.text!==undefined).map(x=>Number(x.text)),right);}
 if(o.type==='needs'||o.type==='needs-range'){const nums=c=>c.diagram.filter(x=>x.text!==undefined).map(x=>Number(x.text));assert.deepEqual(s.answers,s.options.flatMap((c,i)=>{const a=nums(c),valid=o.type==='needs'?JSON.stringify(a)===JSON.stringify(o.needs):a.every((v,j)=>v>=o.needs[j])&&a.reduce((x,y)=>x+y,0)<=o.supply;return valid?[i]:[];}));}
}}
// Full rendered higher-math lifecycle, plus no advance beyond 12 and no unanswered skipping.
const html=fs.readFileSync('math.html','utf8').replace('}());</script>','window.__extended={open:function(k,l){kind=k;age=l+2;round=0;renderQuestion();},task:function(){return JSON.parse(JSON.stringify(adv.task));}};}());</script>');
const dom=new JSDOM(html,{runScripts:'dangerously',url:'https://example.test'}),w=dom.window,d=w.document;
for(let k=0;k<16;k++)for(let l=(k>=12?6:7);l<=12;l++){
 w.__extended.open(k,l);const q=w.__extended.task(),answers=expected(q),before=d.getElementById('scene').innerHTML;d.getElementById('next').click();assert.equal(d.getElementById('scene').innerHTML,before);
 const wrong=q.options.findIndex((_,i)=>!answers.includes(i));d.querySelector('[aria-label^="Extended option '+(wrong+1)+':"]').click();assert.equal(d.getElementById('feedback').textContent,'↺');assert.equal(d.getElementById('scene').innerHTML,before);
 for(const i of answers)d.querySelector('[aria-label^="Extended option '+(i+1)+':"]').click();assert.equal(d.getElementById('feedback').textContent,'✓');assert.equal(d.querySelector('#task-instruction [aria-hidden=true]').textContent,'✓ →');assert.equal(d.querySelectorAll('#choices button').length,0);assert.equal(d.getElementById('advance').style.display,l===12?'none':'block');d.getElementById('next').click();assert.equal(d.getElementById('stage').getAttribute('aria-label'),'Level '+l);
}
w.__extended.open(11,6);const numerator=Number(d.getElementById('prompt').textContent.match(/\d+/)[0]);for(let i=0;i<numerator;i++)d.querySelector('#fraction-select button').click();d.getElementById('advance').click();assert.equal(d.getElementById('stage').getAttribute('aria-label'),'Level 7');d.getElementById('back').click();assert.equal(d.getElementById('math-level-page').textContent,'2 / 2');
dom.window.close();console.log('PASS:',count,'independently solved high-level math tasks;',authored,'new authored tasks with checked diagram oracles; all 100 higher/new math entries, retries, passive completion, continuation and level-12 boundary.');
