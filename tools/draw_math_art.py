"""Draw embedded E Ink illustrations; Pillow is development-only."""
from PIL import Image,ImageDraw
from pathlib import Path
import json,base64,io
root=Path(__file__).resolve().parent.parent
assets={};imgs=[]
for name in ['rabbit0','rabbit1','rabbit2','carrot0','carrot1','carrot2','bear0','bear1','bear2','engine','ruler','dots']:
 im=Image.new('RGB',(200,200),'white');d=ImageDraw.Draw(im);v=int(name[-1]) if name[-1].isdigit() else 0
 def oval(box,fill='white',w=5):d.ellipse(box,fill=fill,outline='black',width=w)
 def line(pts,w=4):d.line(pts,fill='black',width=w)
 if name.startswith('rabbit'):
  oval((55,87,151,175));oval((57+v*3,9,84+v*3,88));oval((116-v*3,8,145-v*3,88));line((70+v*3,25,72+v*3,67),2);line((129-v*3,23,130-v*3,66),2);oval((42,63,160,143));oval((74,91,80,100),'black',2);oval((122,91,128,100),'black',2);d.polygon([(94,108),(108,108),(101,116)],fill='black');d.arc((88,109,101,129),0,180,fill='black',width=2);d.arc((101,109,114,129),0,180,fill='black',width=2)
  for y in [110,121]:line((49,y,74,y+2),2);line((128,y+2,153,y),2)
  oval((44,157,93,185),w=4);oval((111,157,160,185),w=4)
 elif name.startswith('carrot'):
  d.polygon([(59,61),(140,71),(85,184)],fill='white',outline='black',width=5)
  for y in [88,115,140]:line((73,y,94,y+3),3)
  line((100,66,89-v*5,13),7);line((100,65,132+v*3,18),7);line((100,64,65,29),7)
 elif name.startswith('bear'):
  oval((32,44,80,90));oval((127,44,173,90));oval((41,54,164,162));oval((77,94,83,103),'black',2);oval((123,94,129,103),'black',2);oval((79,113,130,147),w=3);oval((95,118,111,128),'black',2);d.arc((89,124,118,141),0,180,fill='black',width=3);d.rectangle((59,163,145,184),outline='black',width=4)
  if v==1:d.polygon([(49,63),(103,17),(155,63)],fill='white',outline='black',width=4)
  if v==2:d.rectangle((67,27,135,57),fill='white',outline='black',width=4);line((57,59,148,59),5)
 elif name=='engine':
  d.rectangle((23,94,174,160),outline='black',width=6);d.rectangle((116,38,174,118),fill='white',outline='black',width=6);d.rectangle((130,52,161,89),outline='black',width=4);d.rectangle((42,61,63,94),fill='black');line((30,61,75,61),5)
  for x in [45,95,145]:oval((x-15,149,x+15,181),w=5)
  d.arc((28,12,64,46),180,340,fill='black',width=3);d.arc((70,4,104,37),180,340,fill='black',width=3)
 elif name=='ruler':
  d.rectangle((12,65,186,139),outline='black',width=6)
  for x in range(27,179,19):line((x,70,x,104),3)
 else:
  for x,y in [(36,54),(127,32),(81,105),(164,130),(37,166)]:oval((x-11,y-11,x+11,y+11),'black',2)
 im=im.resize((120,120),Image.Resampling.LANCZOS);b=io.BytesIO();im.save(b,format='PNG');assets[name]='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode();imgs.append(im)
(root/'art-data.json').write_text(json.dumps(assets))
sheet=Image.new('RGB',(480,435),'white');d=ImageDraw.Draw(sheet)
for i,(name,im) in enumerate(zip(assets,imgs)):x=i%4*120;y=i//4*145;sheet.paste(im,(x,y));d.text((x+7,y+123),name,fill='black')
sheet.save(root.parent/'math-art-contact.png')
