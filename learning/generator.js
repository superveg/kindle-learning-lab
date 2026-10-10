/* Pure, bounded runtime variation. Authored science records remain hypothetical. */
var LearningGenerator=(function(){'use strict';
function materialize(source,variant){var q=JSON.parse(JSON.stringify(source)),g=q.generator;if(!g){return q;}var n=variant%61,a=2+n+Math.max(0,-g.delta),b=a+g.delta;
if(g.type==='change-record'){
 var p='Supplied '+g.kind+' record: A first '+a+', later '+b+'. B first '+(a+1)+', later '+(a+1)+'. ';
 q.prompt=p+g.question;
}else if(g.type==='trial-record'){
 var low=2+n,high=low+g.gap;
 q.prompt='Supplied '+g.kind+' in three trials: A '+low+', '+(low+1)+', '+low+'; B '+high+', '+(high+1)+', '+high+'. Which conclusion fits?';
}
return q;}
/* Canonical content ignores task IDs, feedback, display order and metadata. */
function content(task){
 if(task.stages){return {stages:task.stages.map(content)};}
 if(task.mode==='branch'){return {mode:'branch',nodes:task.nodes};}
 var out={mode:task.mode,prompt:task.prompt||'',narration:task.narration||'',scene:task.scene||[]};
 if(task.items){out.items=task.items;out.constraints=task.constraints||[];out.accepted=task.accepted||[];}
 if(task.options){out.options=task.options.map(function(o,i){return {card:o,accepted:(task.answers||[]).indexOf(i)>=0};}).sort(function(a,b){var x=JSON.stringify(a),y=JSON.stringify(b);return x<y?-1:x>y?1:0;});}
 if(task.observation){out.observation=task.observation;}return out;
}
function signature(task){var s=JSON.stringify(content(task)),a=2166136261,b=5381;for(var i=0;i<s.length;i++){a^=s.charCodeAt(i);a+=(a<<1)+(a<<4)+(a<<7)+(a<<8)+(a<<24);b=((b<<5)+b)^s.charCodeAt(i);}return (a>>>0).toString(16)+'-'+(b>>>0).toString(16)+'-'+s.length;}
return {materialize:materialize,signature:signature,content:content};
}());
