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

`tools/author_learning.py` plus `tools/expand_learning.py` maintain original tasks and write `learning/content.json`. `learning/generator.js`, `learning/engine.js` and `learning/style.css` are shared authoring sources. `tools/build_learning.py` embeds their content and monochrome PNG artwork into five self-contained HTML pages. It reuses a small existing math artwork pack, draws instructional diagrams with Pillow, and rasterizes 15 reviewed OpenMoji black SVGs with Inkscape. Original release-pinned SVGs, file mapping and CC BY-SA 4.0 license are retained in `assets/openmoji/`; attribution is available in each grown-up guide and `art-credits.html`. Object/location composites reuse the reviewed pictures. Evaluate noun recognition at the displayed monochrome size and preserve any depicted feature used by a clue; a shoe-sole clue must not depend on laces absent from the artwork. Run authoring then building after edits; commit sources and generated pages together. No runtime framework, task-time network or continuous animation is required. JavaScript parses as ES5; actual device CSS/API support remains unverified.

Storage uses separate `kll-<subject>-played-v1` keys, catches errors and never clears other origin storage. Marks indicate played families only, not mastery or saved question state. No account, synchronization, offline reopening or cross-device resume is promised.

## Verification and remaining work

`tests/learning-dom.cjs` exercises 100 continuous questions per family (9,000 across all 90 families), all 1,252 seeds, stable retries, manual continuation, passive completion, navigation, storage failure and ES5. `tests/learning-quality.cjs` uses independent picture/feature predicates, checks alternate legal orderings, wrong-order Undo/repeated letters, distinct answer artwork, asset references and all 360 authored story-ending paths. `tests/learning-repeat.cjs` checks all 90 families have twelve distinct content seeds, option-order/ID-invariant signatures, 2,250 constant-RNG solved rounds without repeats in the preceding ten, reload exclusions and 2,928 independently validated bounded runtime records. Normal interaction regression also checks the previous ten signatures. `tests/learning-session-repeat.cjs` adds 2,700 presentations across all 90 families under constant and seeded randomness, with 360 fresh-page boundaries (three five-question visits per family per random source), plus 225 storage-failure/malformed-history presentations. It uses an independent full-content oracle, checks bounded history and preserves unrelated storage. These visits deliberately leave questions unanswered and re-enter via Back; solved manual-Next rounds are covered by the existing repeat suite. These are software checks, not a child usability study.

Existing Hub/storage/capability/advanced DOM suites pass. Math regression passed 1,296 legacy and 891 higher-level questions, quality/usability/navigation checks. Live Chrome opened every one of the 90 activity entries across all 30 subject/level combinations: no broken visible images or horizontal overflow at the tested desktop width. It also exercised stable wrong-answer retry, passive completion, Chinese inference/evidence, neutral science prediction/Observe and two-step story consequences/continuation. Desktop Chinese glyphs rendered legibly; actual Kindle remains unverified. The standalone Playwright Hub smoke runner cannot launch because its Chromium binary is unavailable; live Chrome checks are used separately, not reported as a passing Playwright run.

Actual Kindle Chinese glyphs, narrow-screen picture recognition, text density, touch/scroll behavior, E Ink refresh and use with the child remain to be assessed on the device. Higher-level text can require adult narration. Finite banks need gradual editorial expansion; deeper phonics, full Chinese literacy and comprehensive subject curricula remain future strands rather than completed claims.

## Durable repeat-quality rule

An uncapped session with two samples is not adequate varied practice: it repeats on the third turn. Gate every new family on at least twelve substantive seeds plus a recent-ten content test. Do not count renamed characters, reordered choices, changed IDs or more test iterations as meaningful new content. Parameterized records must keep answers, observations and explanation consistent. Story and language banks require editorial review; factual observations remain authored models. Persist only compact recent fingerprints, not private child answers or mastery scores. Storage failure preserves playable in-memory exclusions.

Current live Chrome repeat checks completed 13 rounds each in English picture words, Chinese picture words, Logic same-picture, Science compare-records and Stories unknown-intentions. None repeated the preceding ten content items; English reload also excluded the prior ten. The story bank showed twelve unique scenarios before safely reusing the first. This targeted repeat audit is separate from the earlier 90-entry rendering audit.

Live artwork verification: all five subject pages opened a level-1 activity with loaded visible images and no desktop horizontal overflow. English socks-before-shoes completed from the two picture taps and continued manually to another question. The guide credit link opened the public picture-credit page. The rendered sock/shoe pair was inspected at its actual 100px image size. This is a targeted artwork check, not a rerun of all 90 rendered entries or a child recognition study.

## Focused verification and actionable device tasks

Validation baseline: `1dce02ae98e5221def2c79f465672ffa38de6dce`. The repeat, session-repeat, quality and learning DOM suites pass against that baseline. A fresh live Chrome check solved 13 English level-1 Picture words questions, found no repeat in the previous ten, and reopened the family after a real reload without selecting recent content. All 39 option images loaded at 100px. The rendered shoe/sock pair and an English level-4 Sentence pictures entry were inspected; the latter had three loaded 100px composites and no horizontal overflow at a 1363px viewport. This is targeted desktop evidence, not all-subject live reload coverage or a narrow-screen browser test. Local Playwright remains unavailable because its Chromium executable is missing; no passing local Playwright run is claimed.

The recent-ten contract applies per family in the five additional subjects, on the same origin/browser storage. It does not prohibit repeats across different families, browsers or devices. Storage failure retains page-memory exclusions but cannot retain them after reopening. Math retains eight initial signatures only in page memory, with bounded candidate fallback; math cross-reload exclusions are not delivered. Finite banks may repeat once content leaves the protected window.

Editorial picture inspection used the shipped embedded PNGs at 100px, 80px and 64px (CSS display sizes), covering sock/shoe, cat/dog, cup, bird, book, door and eight object/location composites. Sock/shoe silhouettes differ; cat has pointed ears/whiskers while dog has drooping ears. These are adult visual observations, not recognition results from children. The cup includes a saucer and could be named a bowl; the paired sock could be called boots. Composite inserts are 48px within a 160px bitmap: approximately 30px at 100px display, 24px at 80px and 19px at 64px. Animal face details and book page strokes lose prominence at those sizes. `on` places the object above the tabletop with a visible gap, so it can read as “above” rather than “on”; `in/out` uses a flat rectangle without a clear box opening. Asset loading and distinct bytes cannot resolve these semantic risks.

Pending tasks below follow the objective / inputs / steps / acceptance / evidence structure of TASK_TEMPLATE.md. They are unperformed tests, not observations or claims about Elio.

### Device task: persistence and readable interaction

- Objective and inputs: test English → level 1 → Picture words on the owner's actual Kindle; record model, firmware and URL. Use the existing uncapped manual practice and local recent-history contract.
- Steps: complete 10 questions, recording target noun and all answer pictures in order; return through Back, re-enter and complete two; reload online and complete two; close/reopen the browser online and complete two. Compare each new question against the previous ten within this family. Keep any previous local history; do not clear origin storage. Check large tap targets, feedback, manual Next and any clipping/scrolling or E Ink ghosting.
- Acceptance: none of the new questions duplicates the preceding ten substantive questions on the same browser/origin; every image/control is readable and one tap gives the expected action without automatic advancement. Record each stage separately. If reopening loses history, retain in-page results and mark persistence failed/unverified rather than generalizing earlier marker-test success. Offline reload is out of scope.
- Evidence: model/firmware, sequence of prompts/picture options, transition type, observed duplicate or tap/render issue. Do not infer child ability from marks.

### Child task: recognize high-risk nouns without label cues

- Objective and inputs: assess sock/shoe, cat/dog and cup against the shipped pictures, using English/Chinese level-1 Picture words. Adult narration is allowed; exact device model remains unknown until recorded.
- Steps: when these targets appear naturally, ask in the child's stronger language what each picture is before naming the target; then ask for the target without pointing. Record the exact first name, selected picture and any help. Obtain a second independent encounter with changed answer placement in a later short session; stop if the child wants to stop. Do not count corrected answers as first recognition.
- Acceptance: a picture is provisionally usable for this learner only after two unprompted recognitions/selections without explanatory help; accept ordinary synonyms in free naming. Any persistent sock/boot, shoe/sock, cat/dog or cup/bowl confusion becomes a bounded artwork revision task with the exact picture/context. No population-level or learning-gain claim follows from this small check.
- Evidence: task prompt/options, child's verbatim naming/choice, help given and display/device. Results remain pending.

### Child/device task: object identity and location are separate checks

- Objective and inputs: English/Chinese → level 4 → Sentence pictures; use book/cat/dog/cup with on/under/in/out composites. The adult may read the sentence; do not require independent reading or advanced-task mastery from a three-year-old.
- Steps: first ask what the small object is; separately ask where it is. Compare “on the table” against “above the table”, and “inside/outside the box” against the flat-frame interpretation. Use a real cup/table/open box to establish that the child already understands the spoken relation before attributing a wrong picture choice to artwork. Record whether the object is recognizable at the actual display size and whether enlargement/explanation was needed.
- Acceptance: repeated loss of object identity or a consistent “floating above”/“picture in a frame” interpretation triggers a specific composition revision (larger recognizable insert, contact with tabletop, clear open-container cues), preserving answers/clues and re-running quality checks. If the child does not yet understand the relation with real objects, record the app result as inconclusive. Keep desktop loading/layout passes separate from device and child results.
- Evidence: relation, object, exact first interpretation, real-object control and assistance. All child/device results are pending.
