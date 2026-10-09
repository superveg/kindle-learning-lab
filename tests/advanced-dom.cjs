const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { JSDOM } = require('jsdom');
const acorn = require('acorn');
const html=fs.readFileSync(path.join(__dirname,'..','index.html'),'utf8');
acorn.parse(html.match(/<script>([\s\S]*?)<\/script>/)[1],{ecmaVersion:5});
function setup(pointerMode) {
  let now=1000000, nextHandle=0; const pending=new Map();
  const dom=new JSDOM(html,{runScripts:'dangerously',url:'https://superveg.github.io/kindle-learning-lab/',beforeParse(w){
    w.scrollTo=function(){}; w.Date.prototype.getTime=function(){return now;};
    if(pointerMode)w.PointerEvent=function(){};else w.PointerEvent=undefined;
    Object.defineProperty(w.document,'hidden',{value:false,configurable:true});
    w.setTimeout=function(fn,delay){assert.ok(delay===3000||delay===10000);pending.set(++nextHandle,fn);return nextHandle;};
    w.clearTimeout=function(id){pending.delete(id);};
  }});
  const w=dom.window, el=id=>w.document.getElementById(id), tap=id=>el(id).click();
  const stage=el('drag-stage'),piece=el('drag-piece'),target=el('drag-target');
  stage.getBoundingClientRect=()=>({left:10,top:10});
  piece.getBoundingClientRect=()=>({left:22,top:30});
  target.getBoundingClientRect=()=>({left:220,top:150,right:320,bottom:250});
  for(const [k,v] of Object.entries({clientWidth:320,clientHeight:260,clientLeft:4,clientTop:4}))Object.defineProperty(stage,k,{value:v});
  Object.defineProperty(target,'offsetLeft',{value:210});Object.defineProperty(target,'offsetTop',{value:140});
  function event(type,x,y){const e=new w.MouseEvent(type,{clientX:x,clientY:y,button:0,bubbles:true,cancelable:true});Object.defineProperty(e,'pointerId',{value:1});return e;}
  function mouse(type,x,y){const e=event(type,x,y);if(type==='pointerdown')piece.onpointerdown(e);else if(type==='mousedown')piece.dispatchEvent(e);else w.document.dispatchEvent(e);}
  return {dom,w,el,tap,mouse,pending,setTime(v){now=v;},getTime(){return now;}};
}
for(const pointerMode of [false,true]){
 const s=setup(pointerMode),{el,tap,mouse,w}=s;
 tap('open-drag');const prefix=pointerMode?'pointer':'mouse';
 mouse(prefix+'down',32,40);mouse(prefix+'move',260,190);
 assert.equal(el('drag-piece').style.left,''); // Release-only mode makes no motion writes.
 mouse(prefix+'up',260,190);assert.match(el('drag-status').textContent,/Drop inside/);
 tap('drag-reset');tap('drag-follow');
 mouse(prefix+'down',32,40);mouse(prefix+'move',260,190);assert.notEqual(el('drag-piece').style.left,'12px');
 mouse(prefix+'up',30,100);assert.match(el('drag-status').textContent,/outside/);
 mouse(prefix+'down',32,40);tap('test-drag-back');assert.match(el('drag-status').textContent,/cancelled/);
 if(!pointerMode){
  tap('open-drag');
  el('drag-piece').ontouchstart({touches:[{identifier:7,clientX:32,clientY:40}],preventDefault(){}});
  const end=new w.Event('touchend');Object.defineProperty(end,'changedTouches',{value:[{identifier:7,clientX:260,clientY:190}]});w.document.dispatchEvent(end);
  assert.match(el('drag-status').textContent,/Drop inside/);
 }
 s.dom.window.close();
}
const s=setup(false),{el,tap,pending}=s;
function fireTimer(){assert.equal(pending.size,1);const fn=[...pending.values()][0];pending.clear();fn();}
tap('open-clock');tap('clock-start');tap('clock-start');assert.equal(pending.size,1);
s.setTime(1010000);fireTimer();assert.equal(el('clock-value').textContent,'10.0 s');assert.equal(pending.size,1);
s.setTime(1027000);fireTimer();assert.equal(el('clock-value').textContent,'27.0 s'); // Late callbacks use actual time.
s.setTime(1030000);tap('clock-read');assert.equal(el('clock-value').textContent,'30.0 s');assert.equal(pending.size,1);
const staleClock=[...pending.values()][0];
tap('test-clock-back');s.setTime(1050000);tap('open-clock');assert.equal(el('clock-value').textContent,'50.0 s');
assert.equal(pending.size,1);staleClock();assert.equal(pending.size,1);
s.setTime(1055000);tap('clock-stop');assert.equal(el('clock-value').textContent,'55.0 s');
assert.equal(pending.size,0);
s.setTime(1060000);tap('clock-stop');assert.equal(el('clock-value').textContent,'55.0 s');
tap('clock-start');s.setTime(1050000);tap('clock-read');assert.match(el('clock-status').textContent,/backward/);tap('clock-reset');
assert.equal(pending.size,0);
tap('clock-start');const resetCallback=[...pending.values()][0];tap('clock-reset');resetCallback();assert.equal(el('clock-value').textContent,'0.0 s');assert.equal(pending.size,0);
tap('clock-start');Object.defineProperty(s.w.document,'hidden',{value:true,configurable:true});s.setTime(1070000);fireTimer();assert.equal(el('clock-value').textContent,'0.0 s');
Object.defineProperty(s.w.document,'hidden',{value:false,configurable:true});fireTimer();assert.equal(el('clock-value').textContent,'20.0 s');
tap('test-clock-back');assert.equal(pending.size,0);
tap('open-delay');tap('delay-start');tap('delay-start');assert.equal(pending.size,1);
const oldCallback=[...pending.values()][0];tap('delay-cancel');assert.equal(pending.size,0);
tap('delay-start');oldCallback();assert.equal(el('delay-box').textContent,'Waiting');
s.setTime(s.getTime()+3200);const callback=[...pending.values()][0];pending.clear();callback();
assert.ok(el('delay-box').querySelector('.object'));assert.match(el('delay-status').textContent,/3.2 seconds/);
tap('delay-start');tap('test-delay-back');assert.equal(pending.size,0);assert.equal(el('delay-start').disabled,false);
s.dom.window.close();
console.log('PASS: ES5; mouse/touch/pointer gesture paths; release-only/follow/drop/cancel; timestamp timing and navigation; duplicate/cancelled/stale delayed callbacks. Kindle input, lag and sleep behavior remain pending.');
