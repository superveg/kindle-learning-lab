const fs=require('node:fs'),assert=require('node:assert/strict'),{JSDOM}=require('jsdom');
const raw=fs.readFileSync('math.html','utf8');
const html=raw.replace('}());</script>','window.__quality={next:start,signature:taskSignature,history:function(){return JSON.parse(JSON.stringify(recentTasks));},state:function(){return JSON.parse(JSON.stringify(adv));}};}());</script>');
function launch(seed=7103,fixed=false){return new JSDOM(html,{url:'https://example.test',runScripts:'dangerously',beforeParse(w){w.Math.random=()=>{if(fixed)return 0.2;seed=seed*16807%2147483647;return(seed-1)/2147483646;};}});}
const buttons=(d,id)=>[...d.getElementById(id).querySelectorAll('button')];
function open(d,k,l){buttons(d,'activities')[k].click();buttons(d,'levels').find(x=>x.getAttribute('aria-label').startsWith('Level '+l+':')).click();}
// Broad sample: balance remains exact, history stays bounded and never needs storage.
let count=0;
for(let k=0;k<12;k++)for(let l=k===9?4:k===10?5:k===11?6:1;l<=6;l++){
 let dom=launch(),w=dom.window,d=w.document;open(d,k,l);let variants=[],history=[];
 for(let q=0;q<18;q++){let signature=w.__quality.signature();variants.push(Number(d.getElementById('play').getAttribute('data-variant')));
  if([0,1,3,7,9].includes(k)&&l>=4&&!(k===7&&l===4))assert(!history.includes(signature),'Recent arithmetic task repeated: '+k+'/'+l);
  history.push(signature);history=history.slice(-8);assert(w.__quality.history()[(l+2)+'-'+k].length<=8);w.__quality.next();count++;
 }
 for(let i=0;i<18;i+=3)assert.equal(new Set(variants.slice(i,i+3)).size,3);
 for(let i=1;i<18;i++)assert.notEqual(variants[i],variants[i-1]);
 d.getElementById('back').click();let openLevel=buttons(d,'levels').find(x=>x.getAttribute('aria-label').startsWith('Level '+l+':'));openLevel.click();assert.equal(w.__quality.history()[(l+2)+'-'+k].length,8,'Menu return retains recent history');dom.window.close();
}
// A pathological RNG or tiny bank must not hang or suppress a valid question.
let dom=launch(1,true),w=dom.window,d=w.document;open(d,9,5);for(let i=0;i<24;i++)w.__quality.next();assert(buttons(d,'choices').length===3);assert.equal(w.__quality.history()['7-9'].length,8);dom.window.close();
// Adjacent levels change reasoning/constraints, not just quantities.
for(let [k,levels] of [[1,[5,6]],[4,[5,6]],[5,[4,5,6]],[8,[4,5,6]],[2,[4,5,6]],[3,[4,5,6]]]){
 let types=[];for(let l of levels){let dom=launch(),d=dom.window.document;open(d,k,l);let a=dom.window.__quality.state();types.push(d.getElementById('play').getAttribute('data-task'));
 if(k===5){assert.equal(a.negate,l===5);assert.equal(d.getElementById('play').getAttribute('data-task'),l===6?'venn-sort':'predicate-sort');}
 if(k===2){assert.equal(a.unlimited,l===4);assert.equal(a.required>0,l===6);}
 if(k===8){assert.equal(a.waypoints.length,l-4);assert.equal(a.walls.length,l===4?0:l===5?2:4);}
 if(k===2&&l===6)assert(a.required>0,'Level 6 adds a piece-count constraint');dom.window.close();}
 if(k!==2&&k!==8&&k!==5)assert.equal(new Set(types).size,types.length,'Distinct reasoning per level for topic '+k);
}
console.log('PASS: '+count+' generated tasks across all 60 combinations; bounded recent history, arithmetic variety, menu continuity, variant balance, constant-RNG fallback and structural level checks.');
