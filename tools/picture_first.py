"""Replace duplicated prose only when a complete, explicit pictured rule is available."""
import re
from extend_learning import diagram

def apply(D):
 for name,cfg in D.items():
  for li,level in enumerate(cfg['levels']):
   for fi,family in enumerate(level['families']):
    for q in family['tasks']:
     for st in q.get('stages',[q]):
      if name=='logic':
       if st.get('constraints') and all(x.get('art') for x in st.get('items',[])):
        st['picturePrompt']='→ □ □'
        st['visualRules']=[diagram((st['items'][a]['art'],),'→',(st['items'][b]['art'],)) for a,b in st['constraints']]
       elif li==0:
        st['picturePrompt']=['= ?','→ ?','▧ → ▦ ?'][fi]
        if fi==1 and st.get('scene'):
         target=st['scene'][0]['art'].split('-');answer=st['options'][st['answers'][0]]['art'].split('-');other=next(x for x in ['circle','square','triangle'] if x!=target[0]);st['visualRules']=[diagram((other+'-'+target[1]+'-large',),'→',(other+'-'+answer[1]+'-large',))]
       elif li==1 and fi==1:
        pattern=re.search(r'(Plain|Striped|Filled)',st['prompt'],re.I)
        if pattern:
         pattern=pattern[1].lower();st['picturePrompt']='☑ ?';st['visualRules']=[diagram(('circle-'+pattern+'-large',),'✓',('square-'+pattern+'-large',),'✓')]
       elif li==2 and fi in [1,2]:
        st['picturePrompt']='→ ?' if fi==1 else '· · · ?'
        if fi==1:st['visualRules']=[diagram('① → ② · ③ → ?')]
       elif (li==2 and fi==0) or (li==3 and fi==0):
        shape=re.search(r'circle|square|triangle',st.get('prompt',''));pattern=re.search(r'plain|striped|filled',st.get('prompt',''))
        if shape and pattern:
         st['picturePrompt']='∧ ?';st['visualRules']=[diagram((shape[0]+'-plain-large',),'∧',('circle-'+pattern[0]+'-large',),'×' if 'NOT' in st['prompt'] else '✓')]
       elif li==5 and fi==0:
        pattern=re.search(r'plain|striped|filled',st.get('prompt',''))
        if pattern:st['picturePrompt']='⇒ × ?';st['visualRules']=[diagram(('circle-'+pattern[0]+'-large',),'✓',('square-'+pattern[0]+'-large',),'✓')]
      if name=='english':
       st['narration']=re.sub(r'^Grown-up says:\s*','',st.get('narration',''))
       if li==2 and fi==0:st['picturePrompt']=st['prompt'].replace('Copy the printed word: ','')
      elif name=='chinese':
       st['narration']=re.sub(r'^大人读：','',st.get('narration',''))
       if li==2 and fi==0:st['picturePrompt']=st['prompt'].replace('照着示例组合：','')
      # Hide no necessary narrative, scientific condition, or reading content.
