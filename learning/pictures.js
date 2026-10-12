/* Exact, static diagrams. No image requests or animation. */
var PictureCards=(function(){'use strict';
function escape(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function html(c,art){var h='',i;if(c.fraction){h='<span class="picture-fraction" role="img" aria-label="'+c.fraction.filled+' / '+c.fraction.parts+'">';for(i=0;i<c.fraction.parts;i++){h+='<i class="fraction-part'+(i<c.fraction.filled?' ink':'')+'" style="width:'+(140/c.fraction.parts)+'px"></i>';}return h+'</span>';}if(c.grid){var g=c.grid,n=g.size;h='<span class="picture-grid" role="img" aria-label="'+escape(c.label||'Grid picture')+'" style="width:'+(n*24+4)+'px">';for(i=0;i<n*n;i++){h+='<i class="picture-cell'+(g.cells.indexOf(i)>=0?' ink':'')+'">'+escape(g.marks&&g.marks[i]||'')+'</i>';}return h+'</span>';}
if(c.diagram){h='<span class="picture-diagram">';for(i=0;i<c.diagram.length;i++){var p=c.diagram[i];if(p.art&&art[p.art]){h+='<img src="'+art[p.art]+'" alt="'+escape(p.label||p.art)+'">';}if(p.text!==undefined){h+='<span>'+escape(p.text)+'</span>';}}return h+'</span>';}
if(c.art&&art[c.art]){h='<img src="'+art[c.art]+'" alt=""'+(c.scale==='small'?' style="width:50px;height:50px;margin:25px"':'')+'>';}
if(c.crop){h='<div style="height:'+(typeof c.crop==='number'?c.crop:48)+'px;overflow:hidden">'+h+'</div>'; }return h;}
return {html:html,escape:escape};
}());
