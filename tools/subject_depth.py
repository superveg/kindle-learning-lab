"""Subject-specific upper-level content; facts and observations remain visible."""
from itertools import combinations
from extend_learning import Q, grid, diagram, transform, symbols, logic as original_logic


def panel(title, columns, rows):
    return {'panel': {'title': title, 'columns': columns, 'rows': rows}, 'label': title}


def facts(lines, title='Read the clues'):
    return panel(title, ['#', 'Information'], [[str(i+1), line] for i, line in enumerate(lines)])


def attach(q, key, hint):
    q['key'] = key
    q['hint'] = hint
    return q


# Distinct situations, causes and outcomes; not one ownership template with renamed nouns.
READINGS = [
 {'art':'umbrella','en':['Rain started before Rabbit left home.','Rabbit took an umbrella to keep dry.','Rabbit opened it outside.','Bear stayed at home.'], 'zh':['小兔出门前下雨了。','小兔带了伞，想让自己不淋湿。','小兔在门外撑开了伞。','小熊留在家里。'], 'detail':('What did Rabbit open outside?','小兔在门外打开了什么？','The umbrella','伞','The book','书','The window','窗'), 'cause':('To keep dry in the rain','想在雨中不淋湿','To shade a sunny window','想挡住窗边阳光','To carry library books','想搬图书馆的书'), 'summary':('Rabbit used an umbrella because it was raining.','下雨了，小兔用伞挡雨。'), 'inference':('Rabbit expected to be outside in the rain.','小兔想到自己会在雨中出门。'), 'update':('The rain stopped, and Rabbit folded the umbrella.','雨停了，小兔把伞收起来。','Rabbit is no longer using the open umbrella.','小兔现在不用撑开的伞了。')},
 {'art':'book','en':['The library notice said the story room was closed today.','Bear chose a book from the open reading room.','Bear read at a table there.','The notice was beside the door.'], 'zh':['图书馆通知说，故事室今天关闭。','小熊从开放的阅览室选了一本书。','小熊在那里坐下读书。','通知贴在门边。'], 'detail':('Where did Bear read?','小熊在哪里读书？','In the open reading room','开放的阅览室','In the closed story room','关闭的故事室','On the bus','公共汽车上'), 'cause':('The story room was closed','因为故事室关闭了','The reading room was closed','因为阅览室关闭了','The library had no books','因为图书馆没有书'), 'summary':('Bear read in an open room while the story room was closed.','故事室关闭，小熊在开放的阅览室读书。'), 'inference':('The notice helped Bear choose a different room.','通知帮助小熊换了一个房间。'), 'update':('A librarian announced that the story room had reopened.','管理员说故事室重新开放了。','Bear can now choose the story room too.','小熊现在也可以选择故事室。')},
 {'art':'bridge','en':['A sign said the small bridge was being repaired.','Rabbit followed the marked path around it.','Rabbit reached the park by that path.','A bird sat near the sign.'], 'zh':['牌子说小桥正在维修。','小兔沿着标出的路绕过去。','小兔顺着那条路到了公园。','一只鸟停在牌子附近。'], 'detail':('How did Rabbit reach the park?','小兔怎样到公园？','By the marked path','沿着标出的路','By crossing the repaired bridge','直接走维修中的桥','By swimming across','游泳过去'), 'cause':('The bridge was being repaired','因为小桥正在维修','The park was closed','因为公园关闭了','The sign forbade every path','因为牌子不许走任何路'), 'summary':('Rabbit used another path because the bridge was under repair.','小桥在维修，小兔绕路到公园。'), 'inference':('The marked path was an available alternative.','标出的路是可以选择的另一条路。'), 'update':('A new sign said the bridge was open again.','新牌子说小桥重新开放了。','The bridge is now an available route.','现在可以选择走小桥。')},
 {'art':'seed','en':['Bear planted a seed and marked the pot.','A sprout appeared in that marked pot a week later.','Bear drew the sprout in a notebook.','Rabbit drew the empty watering can.'], 'zh':['小熊种下一颗种子，在花盆上做了记号。','一周后，有记号的花盆长出小芽。','小熊把小芽画进本子。','小兔画的是空水壶。'], 'detail':('What did Bear draw?','小熊画了什么？','The sprout in the marked pot','有记号花盆里的小芽','A flower that was not described','没有提到的花','The empty watering can','空水壶'), 'cause':('A sprout had appeared in the marked pot','因为有记号的花盆长出了小芽','The pot had grown flowers','因为花盆开出了花','Rabbit planted the watering can','因为小兔种下了水壶'), 'summary':('Bear recorded a sprout appearing after planting a seed.','小熊记录了种下种子后出现的小芽。'), 'inference':('The mark helped connect the later sprout with the earlier pot.','记号帮助把后来的小芽和先前的花盆联系起来。'), 'update':('Bear noticed a second sprout and added it to the drawing.','小熊又看到一棵小芽，把它补画进去。','The updated drawing includes two sprouts.','更新后的画有两棵小芽。')},
 {'art':'engine','en':['The toy track had a gap.','Rabbit found the missing curved piece.','Rabbit fitted it into the gap before trying the train.','Bear put the box on a shelf.'], 'zh':['玩具轨道缺了一段。','小兔找到了缺少的弯轨。','小兔先补上缺口，再试着开火车。','小熊把盒子放到架上。'], 'detail':('What did Rabbit do before trying the train?','小兔试开火车前做了什么？','Filled the track gap','补上轨道缺口','Put the box on a shelf','把盒子放到架上','Removed every track piece','拆掉所有轨道'), 'cause':('The track had a missing piece','因为轨道缺了一段','The train had no wheels','因为火车没有轮子','The shelf needed a new box','因为架子需要新盒子'), 'summary':('Rabbit repaired the gap before testing the toy train.','小兔先补好轨道，再试开火车。'), 'inference':('The curved piece belonged in the missing part of the track.','找到的弯轨适合轨道缺少的部分。'), 'update':('The train stopped at a different loose joint.','火车又停在另一处松开的接头。','A different joint now needs checking.','现在要检查另一处接头。')},
 {'art':'bird','en':['A bird carried grass to a nest near the window.','Bear watched from inside without touching the nest.','Later the bird returned with another piece of grass.','The window had a white curtain.'], 'zh':['一只鸟把草叼到窗边的巢里。','小熊在屋里看，没有碰鸟巢。','后来，鸟又叼来一根草。','窗上挂着白色窗帘。'], 'detail':('What did the bird bring back?','鸟后来又带来了什么？','Another piece of grass','另一根草','A piece of the curtain','一块窗帘','A toy train','玩具火车'), 'cause':('Bear was watching the bird without disturbing the nest','小熊想观察鸟，不去碰鸟巢','Bear was moving the nest','小熊正在搬走鸟巢','The bird asked for a new curtain','鸟要求换窗帘'), 'summary':('Bear watched a bird carry grass to its nest.','小熊观察鸟把草叼到巢里。'), 'inference':('The bird visited the same nest more than once.','鸟不止一次回到同一个巢。'), 'update':('Bear later saw the bird bring a small leaf to that nest.','小熊后来看到鸟把一片小叶子叼进巢里。','The nest received grass and a leaf.','巢里收到了草和叶子。')},
 {'art':'cup','en':['The picture recipe said to add fruit before stirring.','Rabbit put fruit into the bowl.','Rabbit then stirred with a spoon.','Bear washed a cup beside the bowl.'], 'zh':['图画食谱说，先放水果，再搅拌。','小兔把水果放进碗里。','然后，小兔用勺子搅拌。','小熊在旁边洗杯子。'], 'detail':('What came before stirring in the recipe?','食谱要求搅拌前先做什么？','Add fruit','放水果','Wash Bear’s cup','洗小熊的杯子','Remove the spoon','拿走勺子'), 'cause':('The recipe put fruit before stirring','因为食谱要求先放水果再搅拌','The recipe said not to use fruit','因为食谱不许放水果','Bear wanted the bowl left empty','因为小熊要空碗'), 'summary':('Rabbit followed the fruit-then-stir order.','小兔按照先放水果、再搅拌的顺序做。'), 'inference':('Rabbit followed the pictured order for those two steps.','小兔按照图示完成了这两个步骤。'), 'update':('A second recipe picture said to cover the bowl after stirring.','第二张食谱图说，搅拌后盖好碗。','Covering the bowl is the next instructed step.','接下来按食谱盖好碗。')},
 {'art':'sock','en':['A sock on the bench had Rabbit’s name label.','Bear showed the label to Rabbit.','Rabbit recognized the name and took the sock.','A blue bag was under the bench.'], 'zh':['长椅上的袜子贴着小兔的姓名标签。','小熊把标签给小兔看。','小兔认出自己的名字，拿走袜子。','长椅下有一个蓝袋子。'], 'detail':('Which clue connected the sock to Rabbit?','哪条线索把袜子和小兔联系起来？','The name label','姓名标签','The bag’s colour','袋子的颜色','The bench’s height','长椅的高度'), 'cause':('Rabbit recognized the name label','因为小兔认出了姓名标签','Bear guessed from the bag’s colour','因为小熊猜了袋子的颜色','Every sock belonged to Bear','因为所有袜子都属于小熊'), 'summary':('The name label helped Rabbit recover a sock.','姓名标签帮助小兔找回袜子。'), 'inference':('The name label provided a direct clue connecting Rabbit and the sock.','姓名标签提供了把小兔和袜子联系起来的直接线索。'), 'update':('Bear found another sock with Bear’s own name label.','小熊又找到一只写着自己名字的袜子。','The second sock has a different named owner.','第二只袜子的姓名标签指向另一个人。')},
 {'art':'blocks','en':['The game card said each player places one block per turn.','Rabbit had thought a turn allowed two blocks.','Rabbit reread the card and used one block next turn.','Bear kept the card beside the game.'], 'zh':['游戏卡说，每人每轮放一块积木。','小兔原来以为每轮可以放两块。','小兔重新读卡片，下一轮只放一块。','小熊把卡片放在游戏旁。'], 'detail':('What did Rabbit use on the next turn?','小兔下一轮放了几块积木？','One block','一块','Two blocks','两块','No block','零块'), 'cause':('Rabbit reread the stated one-block rule','因为小兔重新读了每轮一块的规则','Bear changed the rule to two blocks','因为小熊把规则改成两块','The card described no turns','因为卡片没有轮流规则'), 'summary':('Rabbit corrected a misunderstanding by rereading the game rule.','小兔重读规则后修正了误解。'), 'inference':('Rabbit’s earlier idea differed from the printed rule.','小兔原先的想法和印出的规则不同。'), 'update':('A new agreed game card allowed two blocks per turn.','大家同意的新游戏卡允许每轮放两块。','The new agreed rule differs from the earlier rule.','大家同意的新规则和旧规则不同。')},
 {'art':'bus','en':['The bus notice said the bus would arrive later than planned.','Bear told Rabbit about the notice.','They waited together at the stop.','Rabbit held a book while waiting.'], 'zh':['公共汽车通知说，车会比原定时间晚到。','小熊把通知告诉小兔。','他们一起在站牌旁等。','小兔等车时拿着一本书。'], 'detail':('What did the notice report?','通知说了什么？','A later bus arrival','汽车会晚到','The bus stop had moved','车站搬走了','No bus would ever arrive','以后永远没有车'), 'cause':('The notice reported a delayed arrival','因为通知说汽车晚到','Rabbit’s book cancelled the bus','因为小兔的书取消了汽车','Bear changed every bus route','因为小熊改了所有路线'), 'summary':('Bear and Rabbit used the delay notice while waiting for the bus.','小熊和小兔根据晚到通知一起等车。'), 'inference':('The notice gave information about a later arrival.','通知提供了汽车会晚到的信息。'), 'update':('The driver announced that this bus would not come and named another stop.','司机通知说这班车不来了，并告知另一个站点。','The later message changes their waiting plan.','后来的通知改变了他们等车的计划。')},
 {'art':'sun','en':['Yesterday’s forecast predicted rain for the picnic.','At picnic time Rabbit observed a clear sky.','Rabbit recorded the clear sky, not the old prediction.','Bear brought a basket.'], 'zh':['昨天的预报说，野餐时可能下雨。','野餐时，小兔观察到天空晴朗。','小兔记录的是当时晴天，不是旧预报。','小熊带了篮子。'], 'detail':('What did Rabbit observe at picnic time?','野餐时小兔观察到什么？','A clear sky','晴朗的天空','The predicted rain','预报中的雨','An unseen storm','没有看到的暴风雨'), 'cause':('The record describes the sky seen at that time','因为记录要写当时看到的天空','Old forecasts are observations of the future','因为旧预报就是未来的观察','The basket proved it had rained','因为篮子证明下过雨'), 'summary':('Rabbit distinguished a forecast from a later observation.','小兔区分了预报和后来实际看到的天气。'), 'inference':('A prediction can differ from a later observation.','预报可能和后来的实际观察不同。'), 'update':('Clouds later arrived and rain began during the picnic.','后来云来了，野餐时开始下雨。','The later weather record should include the new rain.','后来的天气记录要写进新出现的雨。')},
 {'art':'boat','en':['Rabbit predicted that a paper boat would stay dry.','Bear watched its paper become wet in the basin.','Rabbit changed the prediction after seeing the wet paper.','A dry spare sheet lay on the table.'], 'zh':['小兔原来猜纸船会一直干着。','小熊看到水盆里纸船的纸变湿了。','小兔看到湿纸后修正了猜想。','桌上放着一张干的备用纸。'], 'detail':('What evidence changed Rabbit’s prediction?','什么证据让小兔修正猜想？','The wet paper on the tested boat','试过的纸船变湿了','The dry spare sheet','备用纸还是干的','The table’s colour','桌子的颜色'), 'cause':('The tested boat’s paper became wet','因为试过的纸船变湿了','The spare sheet stayed on the table','因为备用纸在桌上','The basin was never used','因为水盆没有使用'), 'summary':('Rabbit revised a prediction using the tested boat’s wet paper.','小兔根据纸船变湿的证据修正了猜想。'), 'inference':('The spare sheet does not report what happened to the tested boat.','备用纸不能说明试过的纸船发生了什么。'), 'update':('A coated second boat stayed dry during a separate short test.','另一只涂层纸船在另一次短测试里保持干燥。','The two supplied tests had different outcomes.','提供的两次测试结果不同。')}
]
# Use existing artwork; the bridge scene is a narrated route, not a new art promise.
READINGS[2]['art'] = 'ramp'

MEANINGS = [
 ('The bag is light enough to carry.','这个袋子很轻，提着不费力。','light','轻','Not heavy','重量不大','Giving light','发出亮光','Dark in colour','颜色深'),
 ('The lamp gives a bright light.','灯亮了，发出亮光。','light','亮','Illumination from the lamp','灯发出的光','A low weight','重量很轻','A loud sound','声音很大'),
 ('Bear held the bark from a tree.','小熊摸了树皮，表面很粗。','bark','皮','The outer layer of a tree','树干外面的一层','A dog’s sound','小狗发出的叫声','A whole leaf','一整片叶子'),
 ('The seal on the jar kept its lid closed.','盖子密封好了，瓶里的水不漏。','seal','封','A closure keeping the jar shut','把开口关严','An ocean animal','一种海里的动物','An open doorway','敞开的门'),
 ('Rabbit saw a bat flying at dusk.','小兔看到蝙蝠在傍晚飞过。','bat','蝠','A flying animal','会飞的动物','Sports equipment','打球的器具','A toy boat','玩具船'),
 ('Bear used a bat to hit the ball.','小熊用球棒击球。','bat','棒','Sports equipment','打球的器具','A flying animal','会飞的动物','A ball’s name','球的名字'),
 ('The duck swam across the pond.','鸭子游过池塘。','duck','鸭','The swimming bird','游泳的鸟','A movement to lower the head','低下头的动作','A type of bridge','一种桥'),
 ('Rabbit had to duck under the low branch.','小兔低下头，躲过低树枝。','duck','低','Lower the head or body','把头或身体放低','A swimming bird','游泳的鸟','Move straight upward','往正上方移动'),
 ('Bear sat on the river bank.','小熊坐在河岸边。','bank','岸','The land beside the river','河边的土地','A place for money','存钱的地方','A boat’s sail','船上的帆'),
 ('The bank stored the money safely.','银行保管钱款。','bank','行','A place that handles money','办理钱款的机构','Land beside a river','河边的土地','A playground slide','游乐场滑梯'),
 ('Rabbit watched the leaves fall.','小兔看到树叶落下来。','fall','落','Move downward','向下掉','The season autumn','秋天这个季节','Become taller','长得更高'),
 ('In the fall, some trees lost leaves.','秋天，一些树开始落叶。','fall','秋','The season autumn','秋天这个季节','A downward movement','向下掉的动作','A type of summer rain','一种夏天的雨')]


CHINESE_MEANINGS=[
 ('这个盒子很轻，提着不费力。','轻','重量不大','动作声音小','颜色很深'),
 ('小兔轻轻关上门，没有发出大声音。','轻轻','动作不重、声音小','盒子的重量小','关得非常快'),
 ('河水很深，水面到河底的距离大。','深','从表面到底部的距离大','颜色很浓','时间很早'),
 ('这块布的蓝色很深。','深','颜色很浓','河底很远','布的重量大'),
 ('春天，这朵花开了，花瓣展开。','开','花瓣展开','盒盖被拿开','开始开车'),
 ('小熊打开盒子，拿出里面的书。','打开','让盒子不再合着','花瓣展开','把书画出来'),
 ('衣服晾干了，摸起来没有水。','干','没有水、不是湿的','做事情','放进水里'),
 ('小兔帮忙干活，把玩具收好。','干活','做事情','变得不湿','衣服的颜色'),
 ('小熊看了一幅挂在墙上的画。','画','用线条或颜色表现的作品','拿笔画的动作','墙上的门'),
 ('小兔用笔画了一棵树。','画','用笔表现形状的动作','现成的一幅作品','种下一棵树'),
 ('这本故事书很好看，小熊想再读。','好看','看起来或读起来令人喜欢','修理完成了','书很重'),
 ('坏掉的轨道修好了，又能使用。','好了','恢复到可以使用的状态','书的故事有趣','变得更重')]

def language(sub,l,f,s):
    zh=sub=='chinese';c=READINGS[s];lines=c['zh' if zh else 'en'];key='编号对应原文信息。' if zh else 'Numbers identify details in the passage.'
    def read_facts(text,title=None):
        return panel(title or ('原文' if zh else 'Passage'),['#','原文信息' if zh else 'Information'],[[str(i+1),line] for i,line in enumerate(text)])
    hint='先读原文，再检查选项是否增加了原文没有的信息。' if zh else 'Read the passage, then check whether a choice adds something the passage does not say.'
    if f==0:
        if l==7:
            # A pronoun refers to an explicitly named actor within a real event.
            actors=[('小兔','Rabbit'),('小熊','Bear'),('小兔','Rabbit'),('小熊','Bear'),('小兔','Rabbit'),('小熊','Bear'),('小兔','Rabbit'),('小熊','Bear'),('小兔','Rabbit'),('小熊','Bear'),('小兔','Rabbit'),('小兔','Rabbit')]
            a=actors[s][0 if zh else 1];reference_line=[2,2,2,2,2,1,2,1,2,1,2,2][s];sentence=lines[reference_line]+('这件事是它做的。' if zh else ' This is what they did.')
            q=Q('“它”指谁？' if zh else 'Who does “they” refer to here?', [a, '小鸟' if zh else 'Bird', '杯子' if zh else 'The cup'],scene=[read_facts([sentence], '读句子' if zh else 'Read the sentence')],oracle={'type':'language-detail','expected':a})
        elif l==8:
            m=MEANINGS[s];prompt=('句中的“'+m[3]+'”是什么意思？') if zh else 'What does “'+m[2]+'” mean in this sentence?'
            opts=[m[5 if zh else 4],m[7 if zh else 6],m[9 if zh else 8]]
            if zh:
                sentence,word,*opts=CHINESE_MEANINGS[s];prompt='句中的“'+word+'”是什么意思？';scene=read_facts([sentence],'语境')
            else:scene=read_facts([m[0]],'Context')
            q=Q(prompt,opts,scene=[scene],oracle={'type':'language-detail','expected':opts[0]})
        elif l==9:
            conjunction=['because','after','but'][s%3];cn={'because':'因为','after':'然后','but':'但是'}[conjunction]
            prompt='选择表示'+{'because':'原因','after':'接下来','but':'转折'}[conjunction]+'的连接词。' if zh else 'Choose the connector for '+{'because':'a reason','after':'a later event','but':'a contrast'}[conjunction]+'.'
            opts=[cn,'但是' if cn!='但是' else '因为','然后' if cn!='然后' else '因为'] if zh else [conjunction,'but' if conjunction!='but' else 'because','after' if conjunction!='after' else 'because']
            opts=list(dict.fromkeys(opts));q=Q(prompt,opts,scene=[read_facts(lines[:2])],oracle={'type':'language-detail','expected':opts[0]})
        elif l==10:
            opts=[c['summary'][1 if zh else 0],lines[3],c['detail'][5 if zh else 4]]
            q=Q('哪一句保持了原文的主要意思？' if zh else 'Which sentence keeps the passage’s main meaning?',opts,scene=[read_facts(lines)],oracle={'type':'language-detail','expected':opts[0]})
        elif l==11:
            observed=lines[2];guess=('明天可能还会发生同样的事。' if zh else 'The same thing may happen tomorrow.');opinion=('这是最好的一种做法。' if zh else 'This is the best possible way.');opts=[observed,guess,opinion]
            q=Q('哪一句报告原文已经发生的事？' if zh else 'Which sentence reports an event stated in the passage?',opts,scene=[read_facts(lines)],oracle={'type':'language-detail','expected':observed})
        else:
            opts=[lines[2], '它把它放在那里。' if zh else 'They put it over there.', c['detail'][7 if zh else 6]]
            q=Q('哪一句既符合原文，又把信息说清楚？' if zh else 'Which sentence is clear and agrees with the passage?',opts,scene=[read_facts(lines)],oracle={'type':'language-detail','expected':opts[0]})
        return attach(q,key,hint)
    if f==1:
        if l==9:
            # The supplied chronology is explicit; background events precede the response.
            items=[{'text':x,'label':x} for x in lines[:3]]
            q=Q('按原文发生顺序排列。' if zh else 'Put the stated events in passage order.',[],scene=[read_facts(lines)],mode='order',items=items,accepted=[lines[:3]],oracle={'type':'language-order','events':lines[:3]})
        elif l==7:
            d=c['detail'];opts=[d[3 if zh else 2],d[5 if zh else 4],d[7 if zh else 6]]
            q=Q(d[1 if zh else 0],opts,scene=[read_facts(lines)],oracle={'type':'language-detail','expected':opts[0]})
        elif l==8:
            d=c['cause'];opts=[d[1 if zh else 0],d[3 if zh else 2],d[5 if zh else 4]]
            question=('哪一句描述小熊观察的方式？' if zh else 'Which description fits Bear’s way of observing?') if s==5 else ('什么原因或目的符合原文？' if zh else 'Which reason or purpose fits the passage?');q=Q(question,opts,scene=[read_facts(lines)],oracle={'type':'language-detail','expected':opts[0]})
        elif l==10:
            opts=[c['inference'][1 if zh else 0],c['cause'][3 if zh else 2],c['cause'][5 if zh else 4]]
            q=Q('哪一个推断有原文支持？' if zh else 'Which inference has support in the passage?',opts,scene=[read_facts(lines)],oracle={'type':'language-detail','expected':opts[0]})
        elif l==11:
            opts=[c['summary'][1 if zh else 0],c['detail'][5 if zh else 4],c['detail'][7 if zh else 6]]
            q=Q('哪一句总结了主要事件？' if zh else 'Which sentence summarizes the main events?',opts,scene=[read_facts(lines)],oracle={'type':'language-detail','expected':opts[0]})
        else:
            first=language(sub,10,1,s);u=c['update'];opts=[u[3 if zh else 2],c['summary'][1 if zh else 0],c['detail'][5 if zh else 4]]
            second=attach(Q('后来有了新信息。现在什么说法合适？' if zh else 'New information arrived. Which statement fits now?',opts,scene=[read_facts([u[1 if zh else 0]],'新信息' if zh else 'New information')],oracle={'type':'language-detail','expected':opts[0]}),key,hint)
            return {'stages':[first,second],'guide':'Preserve the earlier passage and the new information. The revised claim uses the later record.'}
        return attach(q,key,hint)
    # Evidence must select meaningful details, not the entire passage against absurd alternatives.
    first=language(sub,8 if l<10 else 10,1,s)
    if l==9:first=language(sub,7,1,s)
    causes=[[1],[0],[0],[1],[0],[1],[0],[2],[0,2],[0],[1,2],[1]]
    details=[[1,2],[1,2],[1,2],[1,2],[1,2],[2],[0],[0],[2],[0],[1],[1]]
    inferences=[[0,1],[0,1],[0,1,2],[0,1],[1],[0,2],[0,1,2],[0],[0,1],[0],[0,1],[1,3]]
    evidence=(details if l==9 else inferences if l>=10 else causes)[s];proofs=[evidence]
    alternatives=({0:[[1],[0,2]],4:[[0],[1,2]],11:[[1],[2]]} if l<9 else {4:[[1,2],[0,2]],7:[[0],[1,2]],11:[[1],[2]]} if l==9 else {2:[[0,1],[1,2]],4:[[1],[0,2]],7:[[0],[1,2]],8:[[0,1],[1,2]],10:[[0,1],[0,2]]})
    proofs=alternatives.get(s,proofs);evidence=proofs[0]
    possible=[list(ids) for n in range(1,4) for ids in combinations(range(4),n)]
    supports=lambda ids:any(all(i in ids for i in proof) for proof in proofs)
    good=[ids for ids in possible if supports(ids)];bad=[ids for ids in possible if not supports(ids)]
    chosen=list(proofs[:2]);chosen += [ids for ids in good if ids not in chosen][:max(0,2-len(chosen))];groups=chosen+bad[-2:];answers=list(range(len(chosen)))
    options=[dict(panel('原文证据' if zh else 'Passage evidence',['#','原文信息' if zh else 'Information'],[[str(i+1),lines[i]] for i in ids]), evidence=ids) for ids in groups]
    second=attach(Q('选择所有能支持刚才答案的证据组。' if zh else 'Select every evidence set that supports that answer.',options,answers=answers,mode='multi' if len(answers)>1 else 'choice',oracle={'type':'language-evidence','lines':lines,'required':evidence,'proofs':proofs},visualCue='☑ ☑' if len(answers)>1 else '? → ✓'),key,'可以回看原文。不同的证据组也可能充分支持同一个答案。' if zh else 'Reread the passage. More than one evidence set may be sufficient; a true but unrelated detail is not enough.')
    return {'stages':[first,second],'guide':'Printed language is the learning content. An adult may narrate; evidence stays visible. Several relevant details may be needed.'}


SCIENCE=[
 ('ramp','ramp height','travel distance','cm','same ball, surface and release point','low','high'),
 ('ball','surface texture','travel distance','cm','same ball, ramp height and release point','smooth','rough'),
 ('water','paper type','absorption time','seconds','equal drops, sample size and timing method','paper A','paper B'),
 ('cup','cup cover','water remaining','mL','same starting water, cup and elapsed time','open','covered'),
 ('plant','light condition','leaf count','leaves','same plant kind, water, soil and observation time','shade','light'),
 ('seed','water condition','sprout height','cm','same seed kind, light, soil and elapsed time','less water','more water'),
 ('sun','position of a screen','shadow length','cm','same lamp, object and measuring method','near','far'),
 ('blocks','wrapping material','ice remaining','g','equal starting ice, container and elapsed time','wrap A','wrap B'),
 ('boat','boat material','floating time','seconds','same shape, size, water and release method','paper A','paper B'),
 ('leaf','leaf surface','drops retained','drops','equal drops, leaf area and counting method','surface A','surface B'),
 ('dry','drying location','cloth mass','g','same starting wet cloth, airflow and elapsed time','location A','location B'),
 ('roll','ramp surface','stopping distance','cm','same ball, release height and measuring method','surface A','surface B')]


def science(l,f,s):
    art,factor,outcome,unit,held,A,B=SCIENCE[s];competing=held.split(',')[0].replace('same ','').replace('equal ','');a=8+s;b=a+2+s%3;c=a+1
    if s in [0,4,5]:b,c=a+1,a+2+s%3
    if s in [3,7,10]:b,c=a-(2+s%3),a-1
    rows=[['A',A,str(a),str(b)],['B',B,str(a),str(c)]]
    records=panel('Supplied '+outcome+' records', ['Setup',factor,'First ('+unit+')','Later ('+unit+')'],rows)
    conditions=facts(['Changed: '+factor+'.','Held alike: '+held+'.','These are supplied examples, not measurements made by this app.'],'Investigation')
    if f==0:
        op=['change','difference','repeat','confounded','anomaly','scope'][l-7]
        if op=='change':
            opts=[str(abs(b-a))+' '+unit,str(b)+' '+unit,str(a)+' '+unit];prompt='How much did A '+('decrease' if b<a else 'increase')+'?';value=abs(b-a)
        elif op=='difference':
            opts=[str(abs(b-c))+' '+unit,str(b)+' '+unit,str(b+c)+' '+unit];prompt='What is the later difference between A and B?';value=abs(b-c)
        elif op=='repeat':
            va=[a+2,a+3,a+2];vb=[a,a+1,a];
            if s%3==1:va=[a,a+3,a+1];vb=[a+2,a+1,a+2]
            records=panel('Supplied repeated '+outcome+' ('+unit+')', ['Setup','Trial 1 ('+unit+')','Trial 2','Trial 3'],[['A']+list(map(str,va)),['B']+list(map(str,vb))]);
            trend='A higher in every trial' if all(x>y for x,y in zip(va,vb)) else 'Results overlap across trials'
            opts=[trend,'B higher in every trial','A and B equal in every trial'];prompt='Which description fits all three paired trials?';value=trend
        elif op=='confounded':
            conditions=facts(['A and B differed in '+factor+'.','Their '+competing+' also differed.','Later records are supplied below.'],'Two differences')
            opts=['Two conditions changed; the cause is not isolated','The named factor alone is proved to be the cause','The records show that no condition changed'];prompt='What limits the causal explanation?';value='not-isolated'
        elif op=='anomaly':
            va=[a,a+1,a+8];vb=[a,a+1,a+2];records=panel('Supplied repeated '+outcome+' ('+unit+')',['Setup','Trial 1 ('+unit+')','Trial 2','Trial 3'],[['A']+list(map(str,va)),['B']+list(map(str,vb))]);opts=['Repeat the unusual result under the recorded conditions','Remove the unusual result without checking it','Declare the unusual result a rule for every future trial'];prompt='What is a useful next step for the unusual record?';value='repeat-check'
        else:
            direction='more' if abs(b-a)>abs(c-a) else 'less';opts=['A changed '+direction+' than B in these supplied records','A will always change '+direction+' than B in every setting','The factor explains every possible difference'];prompt='Which conclusion keeps the scope of the record?';value='bounded'
        q=Q(prompt,opts,scene=[conditions,records],oracle={'type':'science-depth','operation':op,'a':a,'b':b,'c':c,'trialsA':locals().get('va'),'trialsB':locals().get('vb'),'values':[value, 'other-1','other-2']},guide='Use only the supplied conditions and observations. A measured association is not automatically a sole cause or a universal law.')
        if op in ['change','difference']:
            q['oracle']['values']=[value,b,a if op=='change' else b+c]
        if op=='repeat':q['oracle']['values']=opts
        return attach(q,'Read the condition labels and measurement units.','Compare the relevant records. Check what was held alike before explaining a cause.')
    if f==1:
        goal=['fair-pair','measure','repeat-plan','repair-confound','separate-explanations','complete-plan'][l-7]
        if goal=='fair-pair':
            prompt='Which comparison can test '+factor+'?';opts=['Change '+factor+'; keep '+held+' alike','Change '+factor+' and '+competing+' together','Keep '+factor+' fixed while changing '+competing]
        elif goal=='measure':
            prompt='Which observation directly measures the question’s outcome?';opts=['Measure '+outcome+' in '+unit,'Measure a different property without recording '+outcome,'Record only the setup labels, without a measurement']
        elif goal=='repeat-plan':
            prompt='Which plan checks whether the result repeats?';opts=['Repeat both setups with the same method and record every trial','Repeat only the setup with the preferred result','Change all conditions between trials and keep one number']
        elif goal=='repair-confound':
            prompt='Two conditions changed. Which plan better isolates '+factor+'?';opts=['Vary '+factor+' while making '+held+' alike','Vary '+factor+' and the competing condition again','Compare only the original unmatched setups']
        elif goal=='separate-explanations':
            prompt='Both '+factor+' and '+competing+' could explain a difference. Which next comparison helps?';opts=['Keep '+competing+' alike and vary '+factor,'Keep '+factor+' alike and vary '+competing,'Change both factors again in the same direction','Keep both factors alike without a comparison']
        else:
            prompt='Which plan includes a fair comparison, repeated observations and the stated measurement?';opts=['Vary '+factor+', hold '+held+' alike, repeat and measure '+outcome,'Vary '+factor+' and hold others alike, but record only one trial','Repeat both setups but do not measure '+outcome]
        plans=[{'targetChanged':True,'otherChanged':False,'measuresOutcome':True,'repeatsBoth':True},{'targetChanged':True,'otherChanged':True,'measuresOutcome':False,'repeatsBoth':False},{'targetChanged':False,'otherChanged':False,'measuresOutcome':False,'repeatsBoth':False}]
        if goal=='separate-explanations':plans=[{'targetChanged':True,'otherChanged':False,'measuresOutcome':True,'repeatsBoth':True},{'targetChanged':False,'otherChanged':True,'measuresOutcome':True,'repeatsBoth':True},{'targetChanged':True,'otherChanged':True,'measuresOutcome':True,'repeatsBoth':True},{'targetChanged':False,'otherChanged':False,'measuresOutcome':True,'repeatsBoth':False}]
        return attach(Q(prompt,opts,answers=[0,1] if goal=='separate-explanations' else [0],mode='multi' if goal=='separate-explanations' else 'choice',scene=[facts(['Question: does '+factor+' relate to '+outcome+'?','Record '+outcome+' in '+unit+'.','Conditions to compare: '+held+'.'],'Investigation question')],oracle={'type':'investigation-plan','goal':goal,'plans':plans}), 'Question → comparison → observation', 'A useful plan changes the relevant condition and measures the stated outcome; repeated records can reveal variation.')
    if l==9:
        predict=attach(Q('Predict which setup might have the larger later '+outcome+'.',['A may be larger','B may be larger','They may be equal'],mode='predict',scene=[conditions],observation='Supplied observation: A later '+str(b)+' '+unit+'; B later '+str(c)+' '+unit+'.'), 'Prediction is not scored as a fact.','A prediction can be revised after observing the record.')
        after=science(8,0,s);return {'stages':[predict,after],'guide':'Prediction is neutral. Observe reveals a supplied record, not an experiment performed by this app.'}
    first=science(l,0,s)
    rows2=[{'text':'The stated conditions and the relevant records','label':'Conditions and relevant records','value':'conditions-data'}, {'text':'Only the unrelated picture identity','label':'Unrelated picture identity','value':'picture'}, {'text':'A preference for one outcome, without records','label':'Preference without records','value':'preference'}]
    # Select exact record details with meaningful near-miss alternatives.
    if l in [7,8]:
        opts=([str(a)+' → '+str(b)+' '+unit,str(a)+' → '+str(c)+' '+unit,str(b)+' '+unit+' alone'] if l==7 else [str(b)+' versus '+str(c)+' '+unit,str(a)+' → '+str(b)+' '+unit,str(c)+' '+unit+' alone'])
        evidence=Q('Which evidence is enough to find A’s change?' if l==7 else 'Which evidence gives the later difference?',opts,scene=[records],oracle={'type':'science-evidence','operation':'change' if l==7 else 'difference','a':a,'b':b,'c':c})
    elif l==10:
        evidence=Q('Which setup detail explains the limit?', ['Two conditions differed between A and B','Only the intended condition differed','No setup conditions were recorded'],scene=[first['scene'][0]],oracle={'type':'science-evidence','operation':'confound'})
    elif l==11:
        evidence=Q('Why repeat the unusual result?', ['A repeat can check whether that result recurs','A repeat guarantees the preferred answer','One unusual value proves every future result'],oracle={'type':'science-evidence','operation':'anomaly'})
    else:
        evidence=Q('What helps check whether the finding holds in other conditions?', ['Further comparable observations in other conditions','More repeats only in the same original setting','Removing all records that disagree'],oracle={'type':'science-evidence','operation':'scope'})
    attach(evidence,'Choose evidence for this question, not merely a true detail.','Check whether the detail addresses the claim and its limits.')
    return {'stages':[first,evidence],'guide':'Keep the supplied investigation and data visible while discussing evidence and limitations.'}


SOCIAL=[
 ('music','Rabbit wants music now. Bear wants quiet now.','A spare room is available.','Bear says a quieter room would help.','Move music to the spare room','Keep this room quiet and agree another music space','Turn up the music beside Bear','quiet'),
 ('engine','Rabbit is finishing a track. Bear asks for a later train turn.','Both agree that Rabbit can finish this short track first.','Bear says waiting for the agreed turn works.','Finish the agreed short track, then check the turn','Ask a grown-up to help remember the agreed turn','Take the train before the agreed turn','turn'),
 ('bear0','Bear says no to a hug. Rabbit wants to greet Bear.','A wave is an optional greeting; Bear may decline it too.','Bear says a wave is welcome and still does not want a hug.','Wave without a hug','Say hello from a comfortable distance','Hug Bear despite the stated no','consent'),
 ('cup','Rabbit spilled water near Bear’s picture by accident.','Bear asks for help protecting the picture before talking.','Bear says a towel and adult help would be useful.','Ask an adult for a towel and protect the picture','Offer help and ask before moving the picture','Move the picture without asking and blame Bear','repair'),
 ('blocks','Bear says the game rules are confusing. Rabbit wants to continue.','They can pause the game to read the card together.','Bear says understanding the card matters before restarting.','Pause and read the rule card together','Ask a grown-up to explain before restarting','Restart immediately without explaining the rule','understand'),
 ('rabbit0','Rabbit stands beside a game. Bear does not know whether Rabbit wants to join.','Watching first is allowed.','Rabbit says watching first feels better today.','Let Rabbit watch and stay available for questions','Explain the game if Rabbit asks, without requiring a turn','Pull Rabbit into the game without asking','observe'),
 ('ask','Bear did not answer Rabbit’s greeting. Rabbit does not know why.','Not hearing or wanting space are possibilities, not facts.','Bear says the room was loud and the greeting was not heard.','Try the greeting gently in a quieter place','Check whether Bear wants to talk now','Declare Bear unfriendly because of the earlier silence','unknown'),
 ('stop','Rabbit says pushing has made the game unsafe. Bear notices Rabbit moving away.','A trusted teacher is nearby.','Rabbit asks for help from that teacher.','Go with Rabbit to ask the teacher for help','Stay safely nearby while the teacher helps','Require Rabbit to return to the unsafe pushing','safety'),
 ('book','Rabbit wants table space for a puzzle. Bear wants space for drawing.','The table has enough separate space for both.','Both agree to use separate areas for now.','Use the agreed separate table areas','Ask whether the separate areas are still comfortable','Cover Bear’s drawing area with the puzzle','space'),
 ('quiet','A sudden sound startled Rabbit. Bear wants to offer support.','Rabbit may choose company or space.','Rabbit says quiet space, without touch, would help.','Offer a quiet space and respect no touch','Stay available at a distance Rabbit chooses','Touch Rabbit without permission to stop the feeling','touch'),
 ('sad','Bear is disappointed after a game. Rabbit wants another game.','Bear can choose a pause rather than another game now.','Bear says a short pause is wanted before deciding.','Respect the pause and check later','Offer company during the pause if Bear wants it','Require another game immediately','pause'),
 ('wait','Rabbit and Bear had agreed to play outside. Bear now says rest is needed.','An agreement can be discussed when needs change.','Rabbit agrees to discuss a later outdoor plan after Bear rests.','Respect rest and discuss the later plan','Ask what later plan works after checking both needs','Force the old plan despite the stated need to rest','revise')]


def stories(l,f,s):
    art,event,context,reveal,good1,good2,bad,need=SOCIAL[s]
    sentences=event.split('. ');people=['Bear' if sentence.startswith('Bear') else 'Rabbit and Bear' if sentence.startswith('Rabbit and Bear') else 'Rabbit' for sentence in sentences];rows=[[{'text':who,'art':'bear0' if who=='Bear' else 'rabbit0'},sentence] for who,sentence in zip(people,sentences)];rows.append(['Context',context]);reference=panel('Stated needs and context',['Person','What is stated'],rows)
    if f==0:
        if l==7:
            opts=[event,context,'One person secretly wants the opposite of what was stated.'];prompt='Select the statements actually supplied in this situation.';op='stated';return attach(Q(prompt,opts,answers=[0,1],mode='multi',scene=[reference],oracle={'type':'social-stated','statements':[True,True,False]}),'Separate statements from guesses.','An event and its context can both be known; a hidden wish is not established.')
        elif l==8:
            opts=['What happened and its impact can be discussed separately.', 'An accidental action can have no impact.', 'An unwanted impact proves a harmful intention.'];prompt='Which statement separates an action from its possible impact?';op='impact'
        elif l==9:
            opts=['Ask what happened or what help is wanted.', 'Decide the person’s hidden intention without asking.', 'Assume everyone responds for the same reason.'];prompt='What gathers information instead of guessing an intention?';op='ask'
        elif l==10:
            opts=['A stated boundary can be respected while considering another plan.', 'A greeting requires accepting any touch.', 'An earlier plan removes the right to ask for a change.'];prompt='Which statement preserves choice and the stated boundary?';op='boundary'
        elif l==11:
            opts=[good1,good2,bad];prompt='Select the plans fitting the stated agreement below.';op='plans'
            return attach(Q(prompt,opts,answers=[0,1],mode='multi',scene=[reference,facts([reveal],'After asking')],oracle={'type':'social-plan','need':need,'options':[{'respects':True,'fits':True},{'respects':True,'fits':True},{'respects':False,'fits':False}]}),'Use stated wishes; do not guess feelings.','More than one plan may fit. Check what the person actually requested.')
        else:
            opts=['Ask whether the plan is working for both people.', 'Assume agreement guarantees the same feelings forever.', 'Keep a plan unchanged even after someone asks to revise it.'];prompt='How can the participants check the plan after trying it?';op='check'
        return attach(Q(prompt,opts,scene=[reference],oracle={'type':'social-understanding','operation':op}), 'An event does not reveal every intention or feeling.', 'Separate what was said from what is still unknown. Feelings are not marked right or wrong.')
    if f==1:
        # Both authored paths are available; a story ending is completion, not moral grading.
        intro=event+' '+context
        a1='Ask what would help now.' if l<=9 else 'Check the current agreement and ask what has changed.'
        a2='Offer a choice of help or space.' if l<=9 else 'Pause and ask whether another plan is wanted.'
        nodes={'start':{'text':intro,'art':art,'options':[{'text':a1,'to':'ask'},{'text':a2,'to':'choice'}]},
               'ask':{'text':reveal,'options':[{'text':good1,'to':'end-a'},{'text':good2,'to':'end-b'}]},
               'choice':{'text':reveal+' The person can still choose whether to accept support.','options':[{'text':good2,'to':'end-c'},{'text':good1,'to':'end-d'}]},
               'end-a':{'text':'They try the chosen plan and check whether it works for both. Another request can change the plan.','end':True},
               'end-b':{'text':'They consider the alternative and stay open to feedback. A choice does not guarantee a particular feeling.','end':True},
               'end-c':{'text':'Support is offered with choice. They can pause or ask a trusted grown-up for help.','end':True},
               'end-d':{'text':'They use the stated information and check again. A person may ask for space or a revision.','end':True}}
        if l>=8:
            node_text={8:'They separate the effect of an action from a guess about intention. '+reveal,9:'The reply supplies information that was not known before. '+reveal,10:'The stated boundary remains valid after an offer of help. '+reveal,11:'They compare available alternatives with both people’s current requests. '+reveal,12:'After trying a plan, they ask again rather than assuming it worked. '+reveal}[l]
            nodes['check']={'text':node_text,'options':[{'text':'Check that the chosen response still fits the request.','to':'end-c'},{'text':'Ask whether another option or trusted-adult help is wanted.','to':'end-d'}]}
            for key in ['ask','choice']:
                for opt in nodes[key]['options']:opt['to']='check'
        if l==12:
            nodes['revise']={'text':'The participants may change their request after checking. The earlier agreement is not a reason to ignore new information.','options':[{'text':'Discuss a revised agreement using both current requests.','to':'end-c'},{'text':'Pause and seek help with an unresolved disagreement.','to':'end-d'}]}
            for opt in nodes['check']['options']:opt['to']='revise'
        # Keep every reachable ending only; no dead nodes masquerade as extra story content.
        seen=set()
        def visit(key):
            if key in seen:return
            seen.add(key)
            for opt in nodes[key].get('options',[]):visit(opt['to'])
        visit('start');nodes={k:v for k,v in nodes.items() if k in seen}
        return {'mode':'branch','prompt':intro,'references':[reference],'nodes':nodes,'guide':'Explore either reasonable path. Endings are possible outcomes, not promises or scores for feelings. Respect safety, consent and trusted-adult help.'}
    first=attach(Q('Which question would help before choosing a response?', ['What would help, and is help or space wanted?','Why must you feel exactly the way I do?','Can I decide what you need without asking?'],scene=[reference],oracle={'type':'social-understanding','operation':'ask'}), 'Ask before interpreting an unknown need.', 'A useful question allows a person to describe their own need.')
    second=attach(Q('After this reply, select every plan fitting the stated request.',[good1,good2,bad],answers=[0,1],mode='multi',scene=[facts([reveal],'New information')],oracle={'type':'social-plan','need':need,'options':[{'respects':True,'fits':True},{'respects':True,'fits':True},{'respects':False,'fits':False}]}),'New information can change a response.','Use the actual reply. More than one response may respect the same request.')
    return {'stages':[first,second],'guide':'Ask, hear the reply, then revise using the stated information. Preserve boundaries and adult-help options; feelings are not graded.'}


def logic(l,f,s):
    if f==0:
        q=original_logic(l,f,s);o=q['oracle'];code=o['code'];current=o['source'];q['key']='↻ = 90° clockwise; ↔ = vertical mirror; ↕ = horizontal mirror. Read left to right.'
        if not o.get('inverse'):
            scene=[grid(current)]
            for op in code[:-1]:
                current=transform(current,op,o['size']);scene.extend([{'text':symbols(op),'label':symbols(op)},grid(current)])
            scene.append({'text':symbols(code[-1])+' → ?','label':'Apply the last operation'})
            q['scene']=scene
        else:q['key']+=' The question asks for the original picture.'
        q['hint']='Apply one operation at a time; for an original picture, undo the operations in reverse order.';return q
    if f==2:
        q=original_logic(l,f,s)
        q['key']='A → B means A comes before B. Other pairs can be in either order unless a clue says otherwise.'
        q['hint']='Start with an item that has no unmet earlier requirement. More than one order may satisfy every clue.'
        # Avoid duplicate pictured edges inserted again by the later picture-first pass.
        q['scene']=[];return q
    # New deduction strand replaces another six grid/set-operation templates.
    features=['plain','striped','filled'];shapes=['circle','square','triangle'];target=s%3;other=(s//3)%3;size='small' if s>=9 else 'large'
    cards=[{'art':shape+'-'+fill+'-'+sz,'label':sz+' '+fill+' '+shape,'shape':i,'fill':j,'size':sz} for i,shape in enumerate(shapes) for j,fill in enumerate(features) for sz in ['small','large']]
    predicate=lambda c:c['shape']==target and c['fill']!=other and c['size']==size
    if l==7:
        answers=[i for i,c in enumerate(cards) if predicate(c)];prompt='Select every card meeting both clues.';clues=['Shape: '+shapes[target]+'.','Not '+features[other]+'.'];op='two-clues'
    elif l==8:
        answers=[i for i,c in enumerate(cards) if c['shape']==target and c['fill']==other and c['size']==size];prompt='Select the cards that break the stated rule.';clues=['Only check '+size+' cards.','If '+shapes[target]+', then NOT '+features[other]+'.','A rule is broken only when the first condition is present and the second fails.'];op='counterexample'
    elif l==9:
        varying='fill' if s<9 else 'shape'
        if varying=='fill':
            opts=['Is the fill '+features[other]+'?', 'Is it still the known '+shapes[target]+'?', 'Is the page white?']
            candidates=[shapes[target]+'-'+features[other]+'-'+size,shapes[target]+'-'+features[(other+1)%3]+'-'+size];option_features=['fill','shape','page']
        else:
            opts=['Is the shape '+shapes[target]+'?', 'Is it still the known '+features[other]+' fill?', 'Is the page white?']
            candidates=[shapes[target]+'-'+features[other]+'-'+size,shapes[(target+1)%3]+'-'+features[other]+'-'+size];option_features=['shape','fill','page']
        q=Q('Which question can distinguish the pictured candidates?',opts,scene=[{'art':art,'label':'Candidate '+str(i+1)+': '+art.replace('-',' ')} for i,art in enumerate(candidates)],oracle={'type':'logic-useful-question','varying':varying,'optionFeatures':option_features})
        return attach(q,'A useful clue must separate the remaining possibilities.','Ask about a feature that differs between the candidates.')
    elif l==10:
        answers=[i for i,c in enumerate(cards) if c['shape']!=target and c['fill']==other and c['size']==size];prompt='Select every card consistent with all clues.';clues=['Fill: '+features[other]+'.','Shape is NOT '+shapes[target]+'.'];op='exclude'
    elif l==11:
        answers=[i for i,c in enumerate(cards) if (c['shape']==target or c['fill']==other) and c['size']==size];prompt='Select every card allowed by the rule.';clues=['Shape is '+shapes[target]+' OR fill is '+features[other]+'.','OR permits either condition or both.'];op='either'
    else:
        first=logic(7,1,s);answer=[i for i,c in enumerate(cards) if c['shape']==target and c['fill']==(other+1)%3 and c['size']==size]
        second=attach(Q('A new clue arrived. Which card remains possible?',cards,answers=answer,scene=[facts(['Fill: '+features[(other+1)%3]+'.'],'New clue')],oracle={'type':'logic-features','operation':'new-clue','shape':target,'fill':(other+1)%3,'size':size}), 'Keep the earlier clues and add the new one.','A new clue narrows the possibilities; it does not erase an earlier clue.')
        return {'stages':[first,second],'guide':'Preserve earlier clues during revision. Check every condition independently.'}
    return attach(Q(prompt,cards,answers=answers,mode='multi' if len(answers)>1 else 'choice',scene=[facts(clues+['Size: '+size+'.'])],oracle={'type':'logic-features','operation':op,'shape':target,'fill':other,'size':size}), 'Clues restrict features; check each card.', 'A card must satisfy every stated condition. An implication is not the same as its reverse.')


def improve(D):
    family_names={
      'logic':['Transform and explain','Deduce from clues','Plan with dependencies'],
      'chinese':['语境与表达','联系原文信息','结论与原文证据'],
      'english':['Language in context','Connect a passage','Claim and passage evidence'],
      'science':['Interpret an investigation','Plan a useful test','Observe, explain and check'],
      'stories':['Understand stated needs','Explore possible responses','Ask and revise a response']}
    levels={
      'logic':['Connect transformations and clues','Test a pictured rule','Ask a useful question','Combine exclusions','Find every possibility','Revise with another clue'],
      'chinese':['指代与信息','语境中的词义','连接词与顺序','主要意思与推断','事实与总结','清楚表达与修正'],
      'english':['References and details','Context meanings and causes','Connections and order','Paraphrase and inference','Stated facts and summaries','Precision and revision'],
      'science':['Changes with units','Measure the comparison','Check repeated observations','Recognize competing conditions','Check an unusual record','Design and limit a conclusion'],
      'stories':['Recognize stated needs','Intent and impact','Ask before inferring','Respect boundaries and choice','Compare reasonable plans','Check and revise agreements']}
    for subject,cfg in D.items():
      cfg['levels']=cfg['levels'][:6]
      for l in range(7,13):
        level={'name':levels[subject][l-7],'goal':levels[subject][l-7],'families':[{} for _ in range(3)]};cfg['levels'].append(level)
        for f,family in enumerate(level['families']):
          family['name']=family_names[subject][f]
          family['description']='Use subject-specific relations and keep necessary clues visible. Adults may narrate written content.'
          family['tasks']=[]
          for seed in range(12):
            maker=logic if subject=='logic' else science if subject=='science' else stories if subject=='stories' else None
            q=maker(l,f,seed) if maker else language(subject,l,f,seed)
            if subject=='logic':
                stage=q.get('stages',[q])[0];candidates=(stage.get('scene') or [])+(stage.get('options') or [])+(stage.get('items') or []);q['preview']=next((c for c in candidates if c.get('grid') or c.get('art')), {'text':'A → B'})
                if f==2:
                    a,b=stage['constraints'][0];q['preview']=diagram((stage['items'][a]['art'],),'→',(stage['items'][b]['art'],))
            elif subject in ['chinese','english']:
                symbol=({'chinese':['它 ?','轻 / 轻轻','因为 / 但是','① + ②','事实 / 猜测','① → 新②'],'english':['they ?','light ?','because / but','① + ②','fact / guess','① → new ②']}[subject][l-7]) if f==0 else '① → ②' if f==1 else '① + ② → ✓'
                q['preview']=diagram((READINGS[seed]['art'],),symbol)
            elif subject=='science':q['preview']=diagram((SCIENCE[seed][0],),'A → B' if f==0 else 'A ≠ B' if f==1 else '? → ◉')
            else:q['preview']=diagram(('rabbit0',),'↔' if f==0 else '↗ ↘' if f==1 else '? →',('bear0',))
            q['id']='depth-'+subject+'-'+str(l)+'-'+str(f)+'-'+str(seed)
            family['tasks'].append(q)
