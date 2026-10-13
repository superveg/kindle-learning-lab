"""Reusable upper logic constructors; subject_depth owns current curriculum content."""
import itertools

SHAPES=['circle','square','triangle']
OBJECTS=['book','cup','key','ball','engine','umbrella']
def dependencies(count,seed,branch=False):
 graphs=[]
 for order in itertools.permutations(range(count)):
  shapes=[[[order[i],order[i+1]] for i in range(count-1)],[[order[0],order[i]] for i in range(1,count)],[[order[i],order[-1]] for i in range(count-1)]]
  for edges in shapes:
   edges=sorted(edges)
   if edges not in graphs:graphs.append(edges)
 return graphs[(seed*(2 if branch else 1))%len(graphs)]
def grid(cells,n=3):return {'grid':{'size':n,'cells':sorted(set(cells))},'label':'Grid '+','.join(map(str,sorted(set(cells))))}
def diagram(*parts):return {'diagram':[{'text':p} if isinstance(p,str) else {'art':p[0],'label':p[0]} for p in parts],'label':'Pictured relationship'}
def transform(cells,code,n=3):
 out=[]
 for v in cells:
  r,c=divmod(v,n)
  for op in code:
   if op=='R':r,c=c,n-1-r
   elif op=='H':c=n-1-c
   elif op=='V':r=n-1-r
  out.append(r*n+c)
 return sorted(out)
def symbols(code):return ' '.join({'R':'↻','H':'↔','V':'↕'}[x] for x in code)
def choices(correct,others):
 out=[correct]
 for o in others:
  if o not in out:out.append(o)
  if len(out)==4:break
 return out

def Q(prompt,options,answers=None,scene=None,**kw):
 q={'mode':'choice','prompt':prompt,'cue':'Use the pictured rule.','visualCue':'☞ ?','scene':scene or [],'options':[{'text':o,'label':o} if isinstance(o,str) else o for o in options],'answers':[0] if answers is None else answers,'explain':'Check all of the visible conditions.'}
 q.update(kw);return q

def logic(l,f,s):
 cells=list(itertools.combinations(range(9),3))[s*5+f]
 if f==0:
  codes=['RH','HV','RRR','RHR','HRR','RHV']
  code=codes[l-7];out=transform(cells,code)
  opts=choices(out,[transform(cells,c) for c in ['', 'R','H','V','RR','RRR','RH','HR','RV','VR']]+[[0,4,8],[1,3,7]])
  q=Q(symbols(code)+' → ?',list(map(grid,opts)),scene=[grid(cells)],oracle={'type':'transform','source':cells,'code':code,'size':3})
  if l==9:
   # Reverse instead of another forward rotation.
   q['prompt']='? '+symbols(code)+' →';q['scene']=[grid(out)];q['options']=list(map(grid,choices(list(cells),[transform(cells,c) for c in ['R','H','V','RR','RH','HV']]+[[1,4,7]])));q['oracle']['inverse']=True
  return q
 if f==1:
  a=set(cells);b=set(list(itertools.combinations(range(9),3))[s*5+f+9]);op=['union','intersection','xor','difference','subset','counterexample'][l-7]
  if op in ['union','intersection','xor','difference']:
   out={'union':a|b,'intersection':a&b,'xor':a^b,'difference':a-b}[op]
   opts=choices(sorted(out),[sorted(a),sorted(b),sorted(a|b),sorted(a&b),sorted(a^b),[0,8]])
   return Q({'union':'A ∪ B','intersection':'A ∩ B','xor':'A △ B','difference':'A − B'}[op]+' → ?',list(map(grid,opts)),scene=[grid(a),diagram('A', '·','B'),grid(b)],oracle={'type':'set','a':sorted(a),'b':sorted(b),'op':op})
  # Select all subsets or a counterexample to a pictured containment claim.
  opts=[grid(sorted(a)[:2]),grid(a),grid(sorted(a|{next(i for i in range(9) if i not in a)}))]
  return Q('⊆ ?' if op=='subset' else '⊆ × ?',opts,answers=[0,1] if op=='subset' else [2],scene=[grid(a)],mode='multi' if op=='subset' else 'choice',visualCue='☑ ☑' if op=='subset' else '× ?',oracle={'type':'subset','base':sorted(a),'counter':op=='counterexample'})
 count=3 if l<=8 else 4 if l<=10 else 5
 items=[{'art':OBJECTS[i],'label':OBJECTS[i]} for i in range(count)]
 # A dependency DAG, with multiple legal solutions at levels 8/10/12.
 edges=dependencies(count,s)
 scene=[diagram((items[a]['art'],),'→',(items[b]['art'],)) for a,b in edges]
 return Q('→ □ □',[],scene=scene,mode='order',items=items,constraints=edges,visualCue='□ → □',oracle={'type':'order','edges':edges})
