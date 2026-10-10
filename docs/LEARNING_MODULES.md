# Current additional learning modules

All five subjects have a first usable release: six freely selectable task levels, three families per level, 1,252 authored seeds. The six levels describe skills rather than age, grade or mastery. `subjects.html` is the shared entry; the original math app stays separate.

## Delivered coverage

| Subject | Level | Goal | Activity families | Examples |
| --- | --- | --- | --- | --- |
| Logic Detective | 1: Notice | Compare one visible feature | Same picture; What changed?; Part and whole | 48 |
| Logic Detective | 2: Connect | Use a relationship or one rule | Useful pairs; One pictured rule; First, then | 36 |
| Logic Detective | 3: Combine | Combine two features or apply a transformation | Two features; Apply a change; Picture patterns | 66 |
| Logic Detective | 4: Use clues | Use two clues together | Use both clues; Before and after; Two clues, one object | 48 |
| Logic Detective | 5: Plan | Arrange several things under constraints | Assign the places; Make a workable plan; Repair a plan | 60 |
| Logic Detective | 6: Explain | Test a rule or choose useful evidence | Find a counterexample; Which clue helps?; Plan, then explain | 54 |
| 中文故事屋 | 1: 观察与听说 | 熟悉物品和动作 | 看图认词; 动作词; 听小故事 | 40 |
| 中文故事屋 | 2: 认识文字 | 常见字、标签和生活顺序 | 字和图; 生活标签; 生活顺序 | 44 |
| 中文故事屋 | 3: 组合词语 | 组合熟悉词语，理解关系 | 组合词语; 读短语; 谁做什么 | 36 |
| 中文故事屋 | 4: 读懂短句 | 理解动作、位置和句子顺序 | 读句子选图; 排列句子; 补上词语 | 48 |
| 中文故事屋 | 5: 理解故事 | 联系几句话中的信息 | 故事顺序; 原因和结果; 指的是谁 | 40 |
| 中文故事屋 | 6: 推断与解释 | 用故事中的证据支持答案 | 推断和证据; 合适的结尾; 把话说清楚 | 40 |
| English Explorer | 1: Notice and listen | Recognize familiar objects and actions | Picture words; Action words; A tiny story | 40 |
| English Explorer | 2: Connect print | Recognize letter forms, labels and simple order | Letter pairs; Word labels; First and next | 54 |
| English Explorer | 3: Build meaning | Construct familiar words and phrases | Build a printed word; Phrase pictures; Who does what? | 38 |
| English Explorer | 4: Read sentences | Understand actions, positions and sentence order | Sentence pictures; Sentence order; Complete the meaning | 48 |
| English Explorer | 5: Connect a story | Connect information across short sentences | Story sequence; Cause in the story; Who is meant? | 40 |
| English Explorer | 6: Infer and explain | Use passage evidence to support an answer | Inference and evidence; A consistent ending; Clearer sentences | 40 |
| Everyday Science | 1: Observe | Notice parts and visible details | Plant parts; Everyday uses; Notice the scene | 36 |
| Everyday Science | 2: Compare | Group observations and order changes | Compare visible features; Weather preparation; A growing plant | 36 |
| Everyday Science | 3: Predict | Link a condition with a possible result | Predict and observe; Conditions matter; Compare records | 36 |
| Everyday Science | 4: Use evidence | Separate observation from prediction | Observation or prediction?; Read an evidence record; A question we can test | 36 |
| Everyday Science | 5: Investigate | Compare fairly and interpret records | Compare fairly; Evidence and conclusion; Revise a prediction | 36 |
| Everyday Science | 6: Explain limits | Consider alternatives and a useful next test | Competing explanations; Choose the next investigation; Explain with limits | 36 |
| Stories & Feelings | 1: Notice | Notice an event and possible feelings | What happened?; Possible feelings; Offer comfort | 36 |
| Stories & Feelings | 2: Respond | Link events, needs and help | Story order; Ask for help; What might be needed? | 36 |
| Stories & Feelings | 3: Understand others | Consider two viewpoints and boundaries | Two viewpoints; Say a boundary; Repair a mistake | 36 |
| Stories & Feelings | 4: Explore choices | Compare actions and possible consequences | Explore consequences; Feeling and action; A helpful plan | 36 |
| Stories & Feelings | 5: Resolve | Plan for several needs | Meet two needs; Intent and impact; A safe help-seeking plan | 36 |
| Stories & Feelings | 6: Consider possibilities | Handle uncertainty and tradeoffs | Unknown intentions; Compare reasonable plans; Ask, then revise | 36 |

## Interaction and content contracts

- Every family contains reviewed real tasks. Practice continues manually at the same level with no fixed cap. Every family has at least 12 distinct content seeds. Banks shuffle; content signatures exclude IDs, feedback and choice positions. The previous ten content signatures per family are excluded and saved under `kll-<subject>-recent-v1` when storage works, including across reloads. The immediately preceding seed is also excluded within a loaded session. Science change/trial records vary bounded numeric data in frontend JavaScript (61 variants per record seed). Static narrative banks still eventually repeat; no endless unique-story claim is made. A future exhausted/undersized bank degrades safely instead of looping.
- Choice and final required selection/ordering complete immediately. Pictures/clues and completed objects are passive. Task content stays stable through wrong attempts, Hint and Undo. The visible cue identifies each phase; completion clears obsolete hints and Undo controls. Multi-stage questions retain the preceding story/prompt and reference pictures as passive clues, so evidence questions do not require recalling a vanished passage.
- Ordering validates all authored constraints, accepting every legal arrangement rather than a single witness. Language sequences with repeated identical tokens accept interchangeable tokens. Incorrect complete orders remain undoable.
- Science prediction is neutral and separate from the provided observation. Observe is an explicitly labeled stage transition, not a correctness submission. Datasets are authored observations for reasoning, not measurements made by this app or universal claims about materials.
- Social story branches explore possible consequences and needs. Feelings are not scored right or wrong. All paths terminate; physical boundaries and trusted-adult help remain valid options. A completion check means the path finished.
- Adults may narrate early language tasks and written logic/science/story clues. Do not claim independent three-year-old reading or infer ability from played marks. Chinese uses simplified live text; desktop rendering and actual Kindle rendering are separate checks.
- English currently covers vocabulary, print, spelling and comprehension. Silent letter sequencing is not phonics. Listening/phonemic tasks require a separately verified audio design; they are not delivered here.
- Academic frameworks in the expansion plan inform these original introductory strands. This is not a complete licensed curriculum, an evaluated intervention or evidence of learning gains.

## Engineering

`tools/author_learning.py` plus `tools/expand_learning.py` maintain original tasks and write `learning/content.json`. `learning/generator.js`, `learning/engine.js` and `learning/style.css` are shared authoring sources. `tools/build_learning.py` embeds their content and monochrome PNG artwork into five self-contained HTML pages. It reuses a small existing math artwork pack and draws additional assets with Pillow. Run authoring then building after edits; commit sources and generated pages together. No runtime framework, task-time network or continuous animation is required. JavaScript parses as ES5; actual device CSS/API support remains unverified.

Storage uses separate `kll-<subject>-played-v1` keys, catches errors and never clears other origin storage. Marks indicate played families only, not mastery or saved question state. No account, synchronization, offline reopening or cross-device resume is promised.

## Verification and remaining work

`tests/learning-dom.cjs` exercises 100 continuous questions per family (9,000 across all 90 families), all 1,252 seeds, stable retries, manual continuation, passive completion, navigation, storage failure and ES5. `tests/learning-quality.cjs` uses independent picture/feature predicates, checks alternate legal orderings, wrong-order Undo/repeated letters, distinct answer artwork, asset references and all 360 authored story-ending paths. `tests/learning-repeat.cjs` checks all 90 families have twelve distinct content seeds, option-order/ID-invariant signatures, 2,250 constant-RNG solved rounds without repeats in the preceding ten, reload exclusions and 2,928 independently validated bounded runtime records. Normal interaction regression also checks the previous ten signatures. These are software checks, not a child usability study.

Existing Hub/storage/capability/advanced DOM suites pass. Math regression passed 1,296 legacy and 891 higher-level questions, quality/usability/navigation checks. Live Chrome opened every one of the 90 activity entries across all 30 subject/level combinations: no broken visible images or horizontal overflow at the tested desktop width. It also exercised stable wrong-answer retry, passive completion, Chinese inference/evidence, neutral science prediction/Observe and two-step story consequences/continuation. Desktop Chinese glyphs rendered legibly; actual Kindle remains unverified. The standalone Playwright Hub smoke runner cannot launch because its Chromium binary is unavailable; live Chrome checks are used separately, not reported as a passing Playwright run.

Actual Kindle Chinese glyphs, narrow-screen picture recognition, text density, touch/scroll behavior, E Ink refresh and use with the child remain to be assessed on the device. Higher-level text can require adult narration. Finite banks need gradual editorial expansion; deeper phonics, full Chinese literacy and comprehensive subject curricula remain future strands rather than completed claims.

## Durable repeat-quality rule

An uncapped session with two samples is not adequate varied practice: it repeats on the third turn. Gate every new family on at least twelve substantive seeds plus a recent-ten content test. Do not count renamed characters, reordered choices, changed IDs or more test iterations as meaningful new content. Parameterized records must keep answers, observations and explanation consistent. Story and language banks require editorial review; factual observations remain authored models. Persist only compact recent fingerprints, not private child answers or mastery scores. Storage failure preserves playable in-memory exclusions.
