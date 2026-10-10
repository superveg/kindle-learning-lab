# Current additional learning modules

All five subjects have a first usable release: six freely selectable task levels, three families per level, 201 authored examples. The six levels describe skills rather than age, grade or mastery. `subjects.html` is the shared entry; the original math app stays separate.

## Delivered coverage

| Subject | Level | Goal | Activity families | Examples |
| --- | --- | --- | --- | --- |
| Logic Detective | 1: Notice | Compare one visible feature | Same picture; What changed?; Part and whole | 15 |
| Logic Detective | 2: Connect | Use a relationship or one rule | Useful pairs; One pictured rule; First, then | 6 |
| Logic Detective | 3: Combine | Combine two features or apply a transformation | Two features; Apply a change; Picture patterns | 6 |
| Logic Detective | 4: Use clues | Use two clues together | Use both clues; Before and after; Two clues, one object | 6 |
| Logic Detective | 5: Plan | Arrange several things under constraints | Assign the places; Make a workable plan; Repair a plan | 6 |
| Logic Detective | 6: Explain | Test a rule or choose useful evidence | Find a counterexample; Which clue helps?; Plan, then explain | 6 |
| 中文故事屋 | 1: 观察与听说 | 熟悉物品和动作 | 看图认词; 动作词; 听小故事 | 11 |
| 中文故事屋 | 2: 认识文字 | 常见字、标签和生活顺序 | 字和图; 生活标签; 生活顺序 | 6 |
| 中文故事屋 | 3: 组合词语 | 组合熟悉词语，理解关系 | 组合词语; 读短语; 谁做什么 | 6 |
| 中文故事屋 | 4: 读懂短句 | 理解动作、位置和句子顺序 | 读句子选图; 排列句子; 补上词语 | 6 |
| 中文故事屋 | 5: 理解故事 | 联系几句话中的信息 | 故事顺序; 原因和结果; 指的是谁 | 6 |
| 中文故事屋 | 6: 推断与解释 | 用故事中的证据支持答案 | 推断和证据; 合适的结尾; 把话说清楚 | 6 |
| English Explorer | 1: Notice and listen | Recognize familiar objects and actions | Picture words; Action words; A tiny story | 11 |
| English Explorer | 2: Connect print | Recognize letter forms, labels and simple order | Letter pairs; Word labels; First and next | 8 |
| English Explorer | 3: Build meaning | Construct familiar words and phrases | Build a printed word; Phrase pictures; Who does what? | 6 |
| English Explorer | 4: Read sentences | Understand actions, positions and sentence order | Sentence pictures; Sentence order; Complete the meaning | 6 |
| English Explorer | 5: Connect a story | Connect information across short sentences | Story sequence; Cause in the story; Who is meant? | 6 |
| English Explorer | 6: Infer and explain | Use passage evidence to support an answer | Inference and evidence; A consistent ending; Clearer sentences | 6 |
| Everyday Science | 1: Observe | Notice parts and visible details | Plant parts; Everyday uses; Notice the scene | 6 |
| Everyday Science | 2: Compare | Group observations and order changes | Compare visible features; Weather preparation; A growing plant | 6 |
| Everyday Science | 3: Predict | Link a condition with a possible result | Predict and observe; Conditions matter; Compare records | 6 |
| Everyday Science | 4: Use evidence | Separate observation from prediction | Observation or prediction?; Read an evidence record; A question we can test | 6 |
| Everyday Science | 5: Investigate | Compare fairly and interpret records | Compare fairly; Evidence and conclusion; Revise a prediction | 6 |
| Everyday Science | 6: Explain limits | Consider alternatives and a useful next test | Competing explanations; Choose the next investigation; Explain with limits | 6 |
| Stories & Feelings | 1: Notice | Notice an event and possible feelings | What happened?; Possible feelings; Offer comfort | 6 |
| Stories & Feelings | 2: Respond | Link events, needs and help | Story order; Ask for help; What might be needed? | 6 |
| Stories & Feelings | 3: Understand others | Consider two viewpoints and boundaries | Two viewpoints; Say a boundary; Repair a mistake | 6 |
| Stories & Feelings | 4: Explore choices | Compare actions and possible consequences | Explore consequences; Feeling and action; A helpful plan | 6 |
| Stories & Feelings | 5: Resolve | Plan for several needs | Meet two needs; Intent and impact; A safe help-seeking plan | 6 |
| Stories & Feelings | 6: Consider possibilities | Handle uncertainty and tradeoffs | Unknown intentions; Compare reasonable plans; Ask, then revise | 6 |

## Interaction and content contracts

- Every family contains reviewed real tasks. Practice continues manually at the same level with no fixed cap. Each bank shuffles, then repeats; immediate identical task repetition is avoided. Random option positions do not constitute new content. No endless unique-question claim is made.
- Choice and final required selection/ordering complete immediately. Pictures/clues and completed objects are passive. Task content stays stable through wrong attempts, Hint and Undo. The visible cue identifies each phase. Multi-stage questions retain the preceding story/prompt and reference pictures as passive clues, so evidence questions do not require recalling a vanished passage.
- Ordering validates all authored constraints, accepting every legal arrangement rather than a single witness. Language sequences with repeated identical tokens accept interchangeable tokens. Incorrect complete orders remain undoable.
- Science prediction is neutral and separate from the provided observation. Observe is an explicitly labeled stage transition, not a correctness submission. Datasets are authored observations for reasoning, not measurements made by this app or universal claims about materials.
- Social story branches explore possible consequences and needs. Feelings are not scored right or wrong. All paths terminate; physical boundaries and trusted-adult help remain valid options. A completion check means the path finished.
- Adults may narrate early language tasks and written logic/science/story clues. Do not claim independent three-year-old reading or infer ability from played marks. Chinese uses simplified live text; desktop rendering and actual Kindle rendering are separate checks.
- English currently covers vocabulary, print, spelling and comprehension. Silent letter sequencing is not phonics. Listening/phonemic tasks require a separately verified audio design; they are not delivered here.
- Academic frameworks in the expansion plan inform these original introductory strands. This is not a complete licensed curriculum, an evaluated intervention or evidence of learning gains.

## Engineering

`tools/author_learning.py` maintains original tasks and writes `learning/content.json`. `learning/engine.js` and `learning/style.css` are shared authoring sources. `tools/build_learning.py` embeds their content and monochrome PNG artwork into five self-contained HTML pages. It reuses a small existing math artwork pack and draws additional assets with Pillow. Run authoring then building after edits; commit sources and generated pages together. No runtime framework, task-time network or continuous animation is required. JavaScript parses as ES5; actual device CSS/API support remains unverified.

Storage uses separate `kll-<subject>-played-v1` keys, catches errors and never clears other origin storage. Marks indicate played families only, not mastery or saved question state. No account, synchronization, offline reopening or cross-device resume is promised.

## Verification and remaining work

`tests/learning-dom.cjs` exercises 100 continuous questions per family (9,000 across all 90 families), all 201 samples, stable retries, manual continuation, passive completion, navigation, storage failure and ES5. `tests/learning-quality.cjs` uses independent picture/feature predicates, checks alternate legal orderings, wrong-order Undo/repeated letters, distinct answer artwork, asset references and all 60 authored story-ending paths. These are software checks, not a child usability study.

Existing Hub/storage/capability/advanced DOM suites pass. Math regression passed 1,296 legacy and 891 higher-level questions, quality/usability/navigation checks. Live Chrome opened every one of the 90 activity entries across all 30 subject/level combinations: no broken visible images or horizontal overflow at the tested desktop width. It also exercised stable wrong-answer retry, passive completion, Chinese inference/evidence, neutral science prediction/Observe and two-step story consequences/continuation. Desktop Chinese glyphs rendered legibly; actual Kindle remains unverified. The standalone Playwright Hub smoke runner cannot launch because its Chromium binary is unavailable; live Chrome checks are used separately, not reported as a passing Playwright run.

Actual Kindle Chinese glyphs, narrow-screen picture recognition, text density, touch/scroll behavior, E Ink refresh and use with the child remain to be assessed on the device. Higher-level text can require adult narration. Finite banks need gradual editorial expansion; deeper phonics, full Chinese literacy and comprehensive subject curricula remain future strands rather than completed claims.
