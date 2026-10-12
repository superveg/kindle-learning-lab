"""Original levels 7–12: explicit picture rules, relational reading and evidence tasks."""
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

def extend(D):
 for subject,cfg in D.items():
  cfg['levels']=cfg['levels'][:6]
  for lev in range(7,13):
   names={
    'logic':['Two transformations','Combine sets','Reverse a change','Complete a matrix','Test a rule','Plan with several rules'],
    'chinese':['联系两条信息','比较不同说法','倒序追踪','排除与条件','修正推断','综合证据'],
    'english':['Connect two clues','Compare statements','Trace backwards','Use exclusions','Revise an inference','Combine evidence'],
    'science':['Compare changes','Control a variable','Check repeated records','Separate causes','Test an alternative','Limit a conclusion'],
    'stories':['Agree on an order','Meet separate needs','Check a plan','Revise with permission','Consider alternatives','Coordinate several needs']}
   fams=[]
   for f in range(3):
    tasks=[]
    for seed in range(12):
     if subject=='logic':q=logic(lev,f,seed)
     elif subject in ['chinese','english']:q=language(subject,lev,f,seed)
     elif subject=='science':q=science(lev,f,seed)
     else:q=stories(lev,f,seed)
     q['id']='extended-'+subject+'-'+str(lev)+'-'+str(f)+'-'+str(seed)
     tasks.append(q)
    fn={'logic':['Transform a picture','Compare picture rules','Arrange dependencies'],'chinese':['关系与条件','追踪信息','信息与证据'],'english':['Relationships and conditions','Track information','Claim and evidence'],'science':['Read the supplied record','Choose a fair comparison','Evidence and limits'],'stories':['Pictured agreements','Check pictured needs','Ask and revise']}[subject][f]
    fams.append({'name':fn,'description':names[subject][lev-7]+'. Keep every pictured condition visible; adults may narrate language and social context.','tasks':tasks})
   cfg['levels'].append({'name':names[subject][lev-7],'goal':names[subject][lev-7], 'preview':'Visible rules → ?', 'families':fams})

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

# Twelve different relational structures, with visible short passages rather than extra UI prose.
READ_CASES=[
 ('Cat','Dog','book','inside','outside'),('Rabbit','Bear','cup','above','below'),('Dog','Bird','key','left','right'),('Bear','Cat','ball','before','after'),
 ('Bird','Rabbit','train','first','last'),('Cat','Rabbit','umbrella','dry','wet'),('Bear','Dog','book','open','closed'),('Dog','Cat','cup','full','empty'),
 ('Rabbit','Bird','key','near','far'),('Bird','Bear','ball','small','large'),('Cat','Bear','train','early','late'),('Dog','Rabbit','umbrella','new','old')]
ZH={'Cat':'小猫','Dog':'小狗','Rabbit':'小兔','Bear':'小熊','Bird':'小鸟','book':'书','cup':'杯子','key':'钥匙','ball':'球','train':'火车','umbrella':'伞','inside':'里面','outside':'外面','above':'上面','below':'下面','left':'左边','right':'右边','before':'之前','after':'之后','first':'第一','last':'最后','dry':'干','wet':'湿','open':'打开','closed':'关着','full':'满','empty':'空','near':'近','far':'远','small':'小','large':'大','early':'早','late':'晚','new':'新','old':'旧'}
def language(sub,l,f,s):
 a,b,obj,p,n=READ_CASES[s];zh=sub=='chinese'
 third=next(x for x in ['Cat','Dog','Rabbit','Bear','Bird'] if x not in [a,b])
 C=ZH[third] if zh else third
 A=ZH[a] if zh else a;B=ZH[b] if zh else b;O=ZH[obj] if zh else obj;P=ZH[p] if zh else p;N=ZH[n] if zh else n
 art='engine' if obj=='train' else obj
 if f==0:
  patterns=[
   (f'{O}属于{A}。{A}借给{B}，{B}让{C}拿着。现在谁拿着？',[C,A,B]),
   (f'{A}说{P}，{B}说{N}。观察到{O}是{P}的。谁的说法符合观察？',[A,B,'两人都符合']),
   (f'{A}把{O}给{B}，{B}又还给{A}。现在谁有？',[A,B,'没人']),
   (f'{O}属于{A}或{B}。它不属于{B}。属于谁？',[A,B,'无法判断']),
   (f'先猜{A}有{O}。后来{B}拿出自己的{O}。谁有明确证据？',[B,A,'没人']),
   (f'{A}有自己的{O}。{B}的{O}给了{A}。{A}又还给{B}。谁仍有自己的{O}？',[f'{A}和{B}',A,B])]
  english=[
   (f'{A} owns the {O}. {A} lends it to {B}; {C} carries it for {B}. Who holds it now?',[C,A,B]),
   (f'{A} says {P}; {B} says {N}. We observe the {O} is {P}. Which report fits the observation?',[A,B,'Both']),
   (f'{A} gives the {O} to {B}. {B} returns it. Who has it now?',[A,B,'Neither']),
   (f'The {O} belongs to {A} or {B}. It is not {B}’s. Whose is it?',[A,B,'Unknown']),
   (f'We guessed {A} had the {O}. {B} shows their own {O}. Who has direct evidence?',[B,A,'Neither']),
   (f'{A} has their own {O}. {B} lends theirs to {A}. {A} returns the borrowed one. Who has their own {O}?',[f'{A} and {B}',A,B])]
  prompt,opts=(patterns if zh else english)[l-7]
  return Q(prompt,opts,scene=[{'art':a.lower() if a not in ['Rabbit','Bear'] else a.lower()+'0','label':A},{'art':art,'label':O},{'art':b.lower() if b not in ['Rabbit','Bear'] else b.lower()+'0','label':B}],cue='读短句，联系信息。' if zh else 'Connect the short statements.',visualCue='① + ② → ?')
 if f==1:
  # Semantic operations increase: follow a transfer; reverse it; track two transfers;
  # ignore an irrelevant event; distinguish ownership from possession; undo a loan.
  op=l-7
  en=[f'{A} owns the {O}. {A} gives it to {B}. Who holds it now?',f'{B} now holds the {O}. {A} just gave it to {B}. Who held it before?',f'{A} gives the {O} to {B}. {B} passes it to {third}; {third} returns it to {B}. Who holds it now?',f'{A} gives the {O} to {B}. {A} opens a door. Who still holds the {O}?',f'{A} lends their {O} to {B}. Who owns it?',f'{A} lends the {O} to {B}. {B} returns it, then leaves. Who has it now?']
  cn=[f'{A}把自己的{O}给{B}。现在谁拿着？',f'{B}现在拿着{O}。刚才{A}把它给{B}。之前谁拿着？',f'{A}把{O}给{B}，{B}又给{C}，{C}再还给{B}。现在谁拿着？',f'{A}把{O}给{B}，然后去开门。谁仍拿着{O}？',f'{A}把自己的{O}借给{B}。{O}属于谁？',f'{A}把{O}借给{B}。{B}还回来再离开。现在谁有？']
  answer=[B,A,B,B,A,A][op]
  distractors=[x for x in [A,B,'小鸟' if zh else 'Bird','不知道' if zh else 'Unknown'] if x!=answer]
  return Q((cn if zh else en)[op],[answer]+list(dict.fromkeys(distractors))[:2],visualCue='→ ?' if op!=1 else '← ?')
 first=language(sub,l,0,s)
 true=first['options'][0]['text'];incorrect=first['options'][1]['text']
 st=Q('哪条信息支持答案？' if zh else 'Which detail supports the answer?', [first['prompt'].split('。' if zh else '. ')[0], '只凭猜测' if zh else 'Only a guess', '无关的颜色' if zh else 'An unrelated colour'],visualCue='? → ✓')
 # Evidence is the whole short passage, avoiding unsupported chopped clauses at upper levels.
 st['options'][0]={'text':first['prompt'].rsplit('。',1)[0] if zh else first['prompt'].rsplit('. ',1)[0],'label':'Passage evidence'}
 return {'stages':[first,st],'guide':'Read the short passage aloud when needed. Keep it visible during the evidence stage. Printed language is the learning content.'}

def science(l,f,s):
 a=2+s;b=a+1+s%3;c=a+(s%2);gap=b-a
 rec=diagram('A',str(a),'→',str(b),'·','B',str(a),'→',str(c))
 if f==0:
  operation=['change','difference','repeat','reverse','exception','bounds'][l-7]
  if operation=='change':opts=[str(gap),str(b),str(a)];prompt='A: Δ ?'
  elif operation=='difference':opts=[str(b-c),str(b),str(b+c)];prompt='A − B: ?'
  elif operation=='repeat':
   rec=diagram('A',str(b),str(b+1),str(b),'·','B',str(c),str(c+1),str(c));opts=['A','B','A = B'];prompt='3 × · ↑ ?';opts= ['A = B','A','B'] if b==c else opts
  elif operation=='reverse':opts=[str(a),str(b),str(gap)];prompt='A: ? → +'+str(gap)+' → '+str(b)
  elif operation=='exception':
   rec=diagram(str(a),str(a+gap),str(a+2*gap),str(a+3*gap+1));opts=[str(a+3*gap+1),str(a),str(a+gap)];prompt='Δ = '+str(gap)+' · × ?'
  else:
   vals=[a,b,c,b+1];rec=diagram(*map(str,vals));opts=[str(min(vals))+'–'+str(max(vals)),str(b)+'–'+str(b), '0–100'];prompt='↔ ?'
  return Q(prompt,list(dict.fromkeys(opts)),scene=[rec],oracle={'type':'record','operation':operation,'a':a,'b':b,'c':c},guide='These are supplied hypothetical records, not measurements collected by this app. Interpret only the shown values.')
 if f==1:
  # Full pictured condition vectors: one changed variable, then evidence limits.
  count=2 if l<=8 else 3 if l<=10 else 4
  icons=['sun','water','seed','cup'][:count]
  source=[1+(s//(4**i))%4 for i in range(count)]
  changed=s%count
  right=source[:];right[changed]+=1
  wrong=right[:];wrong[(changed+1)%count]+=1
  wrong2=source[:]
  def condition(vals):return diagram(*[p for i,v in enumerate(vals) for p in [(icons[i],),str(v)]])
  return Q(diagram((icons[changed],),'Δ').get('label','') if False else 'Δ '+str(changed+1)+' · = ?', [condition(right),condition(wrong),condition(wrong2)],scene=[condition(source),diagram((icons[changed],),' +1')],oracle={'type':'fair','source':source,'changed':changed},guide='Choose a comparison changing just the indicated pictured condition; every other condition must stay equal. Icons are condition labels, not claims about plant growth.')
 st=science(l,0,s)
 second=Q('✓ → ?', ['Shown record only','Every object everywhere','All future trials'],guide='The supplied record supports a statement about this record; it cannot establish a universal law.',visualCue='◉ → ?')
 return {'stages':[st,second],'guide':'Compare the record, then choose the scope justified by the supplied data. An adult may narrate scope choices.'}

def stories(l,f,s):
 count=[3,4,4,5,5,6][l-7]
 objects=OBJECTS[:count]
 if f==0:
  items=[{'art':a,'label':a} for a in objects]
  edges=dependencies(count,s)
  return Q('☑ →',[],scene=[diagram((objects[a],),'→',(objects[b],)) for a,b in edges],mode='order',items=items,constraints=edges,visualCue='□ → □',guide='The pictures show an already agreed activity order. Arrange that agreement; this is not a requirement to wait when unsafe or to accept unwanted touch.')
 needs=[1+(s//(4**i))%4 for i in range(2 if l<10 else 3)]
 def plan(vals):return diagram(*[p for i,v in enumerate(vals) for p in [(('rabbit0','bear0','cat')[i],),str(v),(objects[0],)]])
 good=needs[:];bad=needs[:];bad[s%len(bad)]-=1;bad2=needs[:];bad2[(s+1)%len(bad2)]+=1
 first=Q('☑ = ?', [plan(good),plan(bad),plan(bad2)],scene=[plan(needs)],oracle={'type':'needs','needs':needs},guide='These quantities are the explicitly pictured agreements, not a claim that all children need equal amounts. Match all stated agreements. Feelings and personal boundaries are not scored.')
 if f==1:
  if l==11:
   # Two plans satisfy minimum requested amounts within the shown available supply.
   extra=needs[:];extra[0]+=1
   first['options']=[plan(needs),plan(extra),plan(bad),plan([v+3 for v in needs])]
   first['answers']=[0,1];first['mode']='multi';first['prompt']='☑ ≥ · ≤ '+str(sum(needs)+1);first['visualCue']='☑ ☑'
   first['scene']=[plan(needs),diagram('≤',str(sum(needs)+1))]
   first['oracle']={'type':'needs-range','needs':needs,'supply':sum(needs)+1}
   first['guide']='In this hypothetical agreement, participants request at least the pictured amounts and allow more. Select every plan meeting all minimums within the pictured supply. This permission is specific to this task.'
  return first
 new=needs[:];new[s%len(new)]+=1
 nextq=Q('Δ → ?', [plan(new),plan(needs),plan([v+1 for v in needs])],scene=[diagram((('rabbit0','bear0','cat')[s%len(new)],),' +1 ✓'),plan(new)],oracle={'type':'needs','needs':new},guide='A pictured participant has requested and agreed to a revised amount. Choose the plan matching the new agreement; other agreements still apply.')
 # At the highest levels the changed agreement is a delta, not an answer preview.
 if l>=9:nextq['scene']=[diagram((('rabbit0','bear0','cat')[s%len(new)],),' +1 ✓')]
 return {'stages':[first,nextq],'guide':'First match the stated agreements; then revise after explicit permission. Keep the preceding needs visible. Do not infer a real person’s feelings from these quantities.'}
