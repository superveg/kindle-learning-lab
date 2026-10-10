"""Build self-contained ES5 subject pages from reviewed authored banks and PNG art."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,re,io,base64
ROOT=Path(__file__).resolve().parent.parent
raw=(ROOT/'math.html').read_text();art=json.loads(re.search(r'var art=(\{.*?\});',raw,re.S).group(1))
assets={k:art[k] for k in ['rabbit0','bear0','engine','carrot0','circle','square','triangle']}
for name in ['cup','book','key','door','shoe','sock','umbrella','rain','sun','seed','sprout','plant','ball','bed','wash','dry','eat','run','sleep','cat','dog','bird','fish','boat','bus','table','under','on','in','out','happy','sad','angry','ask','wait','help','stop','blocks','quiet','music','house','tree','leaf','ramp','roll','exit','water','mountain']:
 im=Image.new('RGB',(160,160),'white');d=ImageDraw.Draw(im)
 def line(p,w=5):d.line(p,fill='black',width=w)
 def box(p):d.rectangle(p,outline='black',width=5)
 def oval(p,fill='white'):d.ellipse(p,fill=fill,outline='black',width=5)
 if name=='mountain':d.polygon([(10,140),(60,25),(100,95),(120,55),(155,140)],outline='black',width=5)
 elif name=='cup':box((35,45,108,135));d.arc((90,55,140,115),270,90,fill='black',width=6)
 elif name=='book':d.polygon([(15,30),(78,45),(145,30),(145,130),(78,145),(15,130)],outline='black',width=5);line((78,45,78,145));line((30,60,60,68));line((95,68,125,60))
 elif name=='key':oval((20,40,70,90));line((60,75,140,130),9);line((112,110,125,95),7);line((130,122,144,108),7)
 elif name in ['door','exit']:box((40,15,120,145));oval((95,80,101,86),'black');line((65,145,65,110));
 elif name in ['shoe','sock']:
  d.polygon([(45,20),(90,20),(90,93),(135,115),(135,140),(25,140),(25,112),(45,95)],outline='black',width=5)
  if name=='shoe':line((25,112,70,112));line((70,95,95,95));line((70,106,110,106))
 elif name=='umbrella':d.pieslice((15,10,145,140),180,360,outline='black',width=5);line((80,75,80,130));d.arc((53,114,81,143),0,180,fill='black',width=5)
 elif name in ['rain','water']:
  for x,y in [(35,30),(100,45),(65,95)]:d.polygon([(x,y),(x-15,y+25),(x,y+40),(x+15,y+25)],outline='black',width=4)
 elif name=='sun':
  oval((45,45,115,115));
  for p in [(80,5,80,30),(80,130,80,155),(5,80,30,80),(130,80,155,80),(20,20,37,37),(123,123,140,140)]:line(p)
 elif name in ['seed','sprout','plant','tree','leaf']:
  if name=='seed':oval((52,95,105,125));line((10,138,150,138))
  elif name=='leaf':d.polygon([(25,110),(25,55),(75,20),(135,25),(125,90),(75,130)],outline='black',width=5);line((25,110,125,35))
  else:
   line((80,55,80,145));oval((35,55,78,88));oval((82,35,130,72));line((10,145,150,145))
   if name in ['plant','tree']:oval((35,15,95,55));oval((80,5,135,42))
 elif name in ['ball','roll']:oval((25,25,135,135));d.arc((30,25,130,130),45,225,fill='black',width=5);line((35,115,120,45))
 elif name in ['bed','sleep']:box((15,75,145,120));line((15,120,15,145));line((145,120,145,145));oval((25,58,65,85));
 elif name=='wash':box((20,90,145,130));line((105,35,105,70,75,70));line((110,30,145,30));line((75,77,75,87),3)
 elif name=='dry':box((30,30,130,140));line((30,65,130,65));line((30,100,130,100));line((55,30,55,140),3)
 elif name=='eat':oval((50,12,105,65));line((80,65,80,95));line((80,75,120,60,95,40));oval((25,100,135,135));line((40,105,65,125));
 elif name in ['cat','dog','bird','fish']:
  if name=='fish':oval((25,55,115,110));d.polygon([(110,82),(145,50),(145,120)],outline='black',width=5);oval((45,72,53,80),'black')
  else:
   oval((35,45,125,135));oval((58,75,65,83),'black');oval((95,75,102,83),'black')
   if name=='cat':d.polygon([(35,65),(30,15),(70,50)],outline='black',width=5);d.polygon([(95,50),(130,15),(125,70)],outline='black',width=5)
   elif name=='dog':oval((15,45,45,105));oval((115,45,145,105))
   else:d.polygon([(80,87),(95,98),(80,107)],fill='black');line((60,135,50,150));line((100,135,110,150))
 elif name in ['bus','boat']:
  if name=='bus':box((15,45,145,120));oval((25,110,55,145));oval((105,110,135,145));box((30,60,65,85));box((80,60,115,85))
  else:d.polygon([(15,95),(145,95),(115,135),(45,135)],outline='black',width=5);line((80,15,80,95));d.polygon([(85,20),(140,80),(85,80)],outline='black',width=5)
 elif name in ['table','under','on','in','out']:
  box((15,70,145,85));line((30,85,30,145));line((130,85,130,145));oval((65,105,95,135) if name=='under' else (65,35,95,65))
  if name in ['in','out']:im=Image.new('RGB',(160,160),'white');d=ImageDraw.Draw(im);d.rectangle((25,40,115,135),outline='black',width=5);d.ellipse((55,75,85,105) if name=='in' else (125,80,153,108),fill='black')
 elif name in ['happy','sad','angry']:
  oval((20,20,140,140));oval((48,60,56,68),'black');oval((102,60,110,68),'black');d.arc((45,65,115,115) if name=='happy' else (45,90,115,135),0 if name=='happy' else 180,180 if name=='happy' else 360,fill='black',width=5)
  if name=='angry':line((42,43,67,57));line((95,57,120,43))
 elif name in ['ask','help','wait','stop','quiet','music']:
  if name=='music':line((65,30,65,110));line((65,30,120,15,120,95));oval((35,100,65,125),'black');oval((90,90,120,115),'black')
  elif name=='quiet':oval((35,20,125,125));line((80,70,80,150),12)
  elif name=='stop':d.regular_polygon((80,80,65),8,rotation=22.5,outline='black',width=5);line((45,80,115,80),8)
  elif name=='wait':oval((25,25,135,135));line((80,45,80,80,110,95))
  else:oval((20,15,140,115));d.polygon([(50,108),(40,140),(80,115)],fill='white',outline='black',width=5);line((75,50,85,50,85,65,78,73));oval((76,88,80,92),'black')
 elif name=='blocks':box((20,80,70,130));box((80,80,130,130));box((45,25,95,75))
 elif name=='house':box((35,70,125,140));d.polygon([(20,70),(80,15),(140,70)],outline='black',width=5);box((65,95,95,140))
 elif name=='ramp':d.polygon([(20,130),(140,130),(140,35)],outline='black',width=5);oval((110,5,140,35))
 else:
  oval((55,10,95,50));line((75,50,75,100));line((75,60,30,80));line((75,60,120,75));line((75,100,40,145));line((75,100,120,130))
 b=io.BytesIO();im.save(b,format='PNG');assets[name]='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
# Feature cards are deterministic PNGs, avoiding SVG/CSS-only answer distinctions.
for shape in ['circle','square','triangle']:
 for fill in ['plain','striped','filled']:
  for size in ['small','large']:
   im=Image.new('RGB',(160,160),'white');d=ImageDraw.Draw(im);a,b=(50,110) if size=='small' else (20,140)
   mask=Image.new('1',(160,160));m=ImageDraw.Draw(mask)
   if shape=='circle':m.ellipse((a,a,b,b),fill=1)
   elif shape=='square':m.rectangle((a,a,b,b),fill=1)
   else:m.polygon([(80,a),(b,b),(a,b)],fill=1)
   pat=Image.new('RGB',(160,160),'white');pd=ImageDraw.Draw(pat)
   if fill=='filled':pd.rectangle((0,0,160,160),fill='black')
   elif fill=='striped':
    for x in range(-160,160,15):pd.line((x,0,x+160,160),fill='black',width=5)
   im.paste(pat,(0,0),mask);d=ImageDraw.Draw(im)
   if shape=='circle':d.ellipse((a,a,b,b),outline='black',width=5)
   elif shape=='square':d.rectangle((a,a,b,b),outline='black',width=5)
   else:d.polygon([(80,a),(b,b),(a,b)],outline='black',width=5)
   bts=io.BytesIO();im.save(bts,format='PNG');assets[shape+'-'+fill+'-'+size]='data:image/png;base64,'+base64.b64encode(bts.getvalue()).decode()
engine=(ROOT/'learning/engine.js').read_text();style=(ROOT/'learning/style.css').read_text();data=json.loads((ROOT/'learning/content.json').read_text())
for subject,config in data.items():
 used=assets # Small complete pack keeps authorship and offline session simple.
 page='<!doctype html><html lang="'+('zh-Hans' if subject=='chinese' else 'en')+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+config['title']+' — Kindle Learning Lab</title><style>'+style+'</style></head><body><main><nav><a href="subjects.html" aria-label="All subjects">⌂ <span>Subjects</span></a><button id="back" aria-label="Back">← <span>Back</span></button></nav><h1>'+config['title']+'</h1><div id="levels"></div><div id="families" hidden></div><section id="play" hidden><div id="progress"></div><h2 id="family-title"></h2><p id="cue"></p><div id="scene"></div><div id="choices"></div><div id="work"></div><div id="feedback" role="status" aria-live="polite"></div><div id="tools"></div><button id="next" hidden>→ Another question</button><details><summary>Grown-up guide</summary><p id="guide"></p></details></section><noscript>JavaScript is needed for these activities.</noscript></main><script>var CONFIG='+json.dumps(config,ensure_ascii=False)+';var ART='+json.dumps(used)+';'+engine+'</script></body></html>'
 (ROOT/(subject+'.html')).write_text(page)
print('Built:',', '.join(data))
