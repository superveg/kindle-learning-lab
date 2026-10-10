const fs=require('node:fs'),assert=require('node:assert/strict'),{JSDOM}=require('jsdom');
const html=fs.readFileSync('math.html','utf8').replace('}());</script>','window.__audit={open:function(k,l,v){kind=k;age=l+2;round=v;renderQuestion();},state:function(){return JSON.parse(JSON.stringify(adv));}};}());</script>');
const dom=new JSDOM(html,{runScripts:'dangerously',url:'https://example.test'}),w=dom.window,d=w.document;
const open=(k,l,v)=>w.__audit.open(k,l,v),state=()=>w.__audit.state(),label=x=>[...d.querySelectorAll('button')].find(b=>b.getAttribute('aria-label')===x),tap=x=>{assert(label(x),x);label(x).click();},choose=n=>tap('Choose '+n),feedback=()=>d.getElementById('feedback').textContent;
for(let k of [0,10])for(let v=0;v<3;v++){
 open(k,6,k===10?2:v);let g=state().fullGroups;assert(g&&g.remainder>0);assert(!d.getElementById('prompt').textContent.includes('÷'),'Ask for groups without asserting exact division');
 choose(g.groups);assert(d.getElementById('scene').textContent.includes(g.groups+' full groups of '+g.size));assert(!d.getElementById('scene').textContent.includes(g.total+' ÷ '+g.size+' = '+g.groups));choose(g.remainder);
 assert.equal(d.getElementById('prompt').textContent,g.total+' = '+g.size+' × '+g.groups+' + '+g.remainder);assert.equal(g.total,g.size*g.groups+g.remainder);
}
open(1,3,1);assert.equal(d.querySelectorAll('#choices button').length,3);let [whole,part]=d.getElementById('prompt').textContent.match(/\d+/g).map(Number);assert(!d.querySelector('#part-b button'),'Reference carriage is passive');choose(whole-part);assert.equal(feedback(),'✓');
open(4,6,0);let a=state();tap('Inspect sequence position 1');assert(feedback());tap('Inspect sequence position '+(a.badIndex+1));assert.equal(feedback(),'');choose(a.sequence[a.badIndex]);assert.equal(feedback(),'');assert(d.getElementById('task-instruction').textContent.includes('last gap'));choose(a.gapValue);
open(6,4,0);tap('Select piece 1');tap('Place piece at row 3 column 3');assert(feedback().includes('edge'));assert.equal(state().occupied.length,0);tap('Place piece at row 1 column 1');assert.equal(feedback(),'');assert.equal(state().occupied.length,0);assert.equal(d.querySelectorAll('.tile-ghost').length,3);assert(d.querySelector('.tile-anchor'));tap('Place piece at row 1 column 1');assert.equal(state().occupied.length,3);assert.equal(feedback(),'');tap('Undo last piece');assert.equal(state().occupied.length,0);
open(5,6,0);assert.equal(d.querySelectorAll('.membership-board .set-region').length,4);assert.equal(d.querySelectorAll('.set-outline').length,2);let item=state().items[0],bin=(item.shape===state().shape?1:0)+(item.small===state().small?2:0),bins=['Neither A nor B','A only','B only','Both A and B'];tap('Select '+(item.small?'small ':'large ')+(item.shape?'square':'circle')+' 1');tap(bins[(bin+1)%4]);assert(feedback());tap(bins[bin]);assert.equal(feedback(),'');assert.equal(state().items[0].bin,bin);assert(d.querySelectorAll('.set-region-'+bin+' img').length);
open(8,6,0);let route=state(),invalidMove=route.start<4?'Move up':'Move down';tap(invalidMove);assert(feedback().includes('Edge'));let delta=route.path[1]-route.start;tap({'-4':'Move up','4':'Move down','-1':'Move left','1':'Move right'}[delta]);assert.equal(feedback(),'');assert.equal(state().position,route.path[1]);tap('Undo last move');assert.equal(state().position,route.start);
open(7,6,0);let equal=[...d.querySelectorAll('.equal-portion')],extra=d.querySelector('.extra-portion');assert.equal(equal.length,2);assert.equal(equal[0].textContent,equal[1].textContent);assert(extra.textContent.includes('+'));assert(!d.getElementById('scene').textContent.includes('÷ 2'),'Formula is an optional hint, not the initial model');
open(11,6,0);assert(d.getElementById('task-instruction').textContent.includes('Tap to shade'));tap('Shade equal part 1');assert(d.getElementById('task-instruction').textContent.includes('1 /'));if(state().numerator===1)assert(d.getElementById('task-instruction').textContent.includes('Complete.'));
open(11,6,1);assert(d.getElementById('task-instruction').textContent.includes('quarters'));
let modes=new Set();for(let i=0;i<30;i++){open(11,6,2);let mode=state().fractionMode; modes.add(mode);let cue=d.getElementById('task-instruction').textContent;assert(cue.includes(mode===0?'same shaded':mode===1?'larger':'equal-sized'));}assert.equal(modes.size,3);
// Current-step hints refresh whether opened before or after the first answer.
for(let level of [5,6])for(let variant=0;variant<3;variant++){
 open(1,level,variant);assert(d.getElementById('task-instruction').textContent.includes('Step 1 / 2'));
 if(variant===0)tap('Show current step hint');
 choose(state().answers[0]);assert(d.getElementById('task-instruction').textContent.includes('Step 2 / 2'));
 if(variant!==0)tap('Show current step hint');
 const hint=d.getElementById('current-step-hint').textContent;
 assert(hint.includes(level===5?'change at stop 2':'Undo stop 1'));
 choose(state().answers[1]);assert(!d.getElementById('current-step-hint'));assert(d.getElementById('task-instruction').textContent.includes('Complete.'));
}
open(7,6,0);choose(state().answers[0]);for(const segment of d.querySelectorAll('.equal-portion'))assert.equal(segment.textContent,'B '+state().answers[0]);choose(state().answers[1]);assert(d.getElementById('task-instruction').textContent.includes('Complete.'));
open(8,6,0);const path=state().path;for(let i=1;i<path.length;i++){const delta=path[i]-path[i-1];tap({'-4':'Move up','4':'Move down','-1':'Move left','1':'Move right'}[delta]);}assert(d.getElementById('task-instruction').textContent.includes('Complete.'));
open(11,6,0);tap('Shade equal part 1');open(1,3,1);[whole,part]=d.getElementById('prompt').textContent.match(/\d+/g).map(Number);choose(whole-part);assert(!d.getElementById('task-instruction').textContent.includes('shaded'),'A previous advanced task cannot leak its result into a lower level');
dom.window.close();console.log('PASS: valid intermediate remainder statements, direct train answers, feedback lifecycle, tile preview/placement/undo, spatial set destinations, segmented comparison model and all fraction cues.');
