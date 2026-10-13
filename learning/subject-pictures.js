/* Meaningful subject diagrams; math keeps its separate renderer. */
var SubjectPictures=(function(){'use strict';
function E(s){return PictureCards.escape(s);}
function cell(value,art){if(value&&typeof value==='object'){var h='';if(value.art&&art[value.art]){h='<img class="panel-icon" src="'+art[value.art]+'" alt="">';}return h+E(value.text||'');}return E(value);}
function html(c,art){if(c.panel){var p=c.panel,h='<table class="subject-panel'+(p.columns[0]==='#'?' facts-panel':'')+'"><caption>'+E(p.title)+'</caption><thead><tr>';for(var i=0;i<p.columns.length;i++){h+='<th scope="col">'+E(p.columns[i])+'</th>';}h+='</tr></thead><tbody>';for(i=0;i<p.rows.length;i++){h+='<tr>';for(var j=0;j<p.rows[i].length;j++){h+='<'+(j===0?'th scope="row"':'td')+'>'+cell(p.rows[i][j],art)+'</'+(j===0?'th':'td')+'>';}h+='</tr>';}return h+'</tbody></table>';}
if(c.grid){var g=c.grid,n=g.size,h='<span class="subject-grid" role="img" aria-label="'+E(c.label||'Grid picture')+'" style="width:'+(n*32)+'px">';for(var i=0;i<n*n;i++){h+='<i class="subject-cell'+(g.cells.indexOf(i)>=0?' ink':'')+'">'+E(g.marks&&g.marks[i]||'')+'</i>';}return h+'</span>';}
return PictureCards.html(c,art);}
return {html:html};
}());
