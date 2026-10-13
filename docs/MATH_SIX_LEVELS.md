# Math levels 1–12: implementation and original 1–6 foundations

## Current depth and breadth: levels 6–12

The owner requested an individual quality review of levels 6–12: improve weak diagrams and unclear processes, deepen the existing strands and introduce additional mathematical topics as prerequisites accumulate. The app now has sixteen topics and 160 selectable topic/level entries. Four later-starting strands begin at 6; the original minimum levels remain unchanged. Topic menus use three pages of at most six pictures; level menus use two pages. Original topic IDs and played-mark storage identities are unchanged.

Levels remain independent task structures, not ages, school grades or a complete Singapore course. An easy spatial level does not establish arithmetic readiness. Difficulty should connect representations and relationships, not merely enlarge operands or add unfamiliar symbols.

### Quality findings and resulting contracts

- The earlier seven arithmetic-themed extensions reused the same six symbolic expressions with one decorative topic image. The new train, track, comparison, place-value and sharing generators have different mathematical structures. Rabbit equal-group tasks use actual groups; counter tasks use arrays, including a visible per-row split for distributivity.
- A picture must encode the quantities or relationship being used. Decorative nouns cannot substitute for the model. Unknown groups are shown as unknowns, not as a countable hidden answer. Matching unknown bar portions are equal; known extras have different dashed borders. Unknown quantity bars are schematic, not a scale from which to measure the answer.
- Transformation tasks show intermediate operations rather than only two disconnected grids. Visible keys explain quarter-turns, mirror axes, exactly-one overlap, relative turns, route constraints and feature conditions. Logic uses short AND/OR wording and examples; essential meaning is not confined to a folded adult guide.
- Every upper task offers optional thinking steps. Answers stay available immediately; opening guidance does not regenerate the task or change the answer. Wrong retries preserve both model and shown guidance. Completion removes obsolete guidance, retains the result and allows manual same-level continuation.
- Numeric distractors include plausible errors where applicable: forgetting extras, reading the endpoint instead of ruler length, ignoring chart scale or confusing perimeter and area. They remain distinct from the valid answer.
- Carry, borrow, shifted-ruler and hour-crossing generators enforce their named structural conditions. Unit conversions preserve explicit units. There is no timer, animation loop or automatic advancement.

### Existing arithmetic strands: topic-specific progression

| Strand | 6 foundation | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rabbits | Full servings and leftovers | Groups plus extras | Split each group | Unknown group size | Balanced totals | Multiplicative comparison | Inverse grouping and removal |
| Train | Undo two stops | Apply two changes | Undo two changes | Connect three changes | Transfer to another train | Transfer until equal | Undo three changes |
| Track | Length and piece-count constraints | Combine two lengths | Infer short-piece count | Infer long-piece count | Find piece count | Difference from all-long stock | Infer unknown piece length |
| Counters | Array and hidden counters | Array plus extras | Distributive row split | Unknown array dimension | Balance totals | Equal array units | Recover a dimension |
| Comparison | Sum and difference | Sum and difference model | Multiplicative sum | Multiplicative difference | Equalize by transfer | Relation then change | Ratio with an extra |
| Tens | Missing amount | Carry with tens/ones | Borrow with tens/ones | Compensate around ten | Missing amount | Exchange one ten | Compose two changes |
| Sharing | Whole shares/remainders | Equal shares plus leftover | Remainder | Number of groups | Only full groups | Complete equal sharing | Reverse group relation |

### Existing spatial, rule and fraction strands

| Strand | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- |
| Shapes | Turn then reflect | Composed reflection | Three transformations | Recover original grid | Transform plus exactly-one overlap | Another composition and mask |
| Position | Relative turns | Recover start | Shortest legal route | Shortest through waypoint | Key before door before flag | Key plus ordered visits |
| Patterns | Alternating increments | Separate interleaved rows | Transformed-grid pattern | Increasing differences | Inverse number machine | Increasing step size |
| Sorting | Exactly one feature | Three features | Either feature with exclusion | Alternative conjunctions | Counterexample | Combined features excluding one card |
| Fractions | Like-denominator addition | Like-denominator subtraction | Equivalent partitions | Groups of one third | Complete one whole | Missing fraction addend |

These strands still need child observation, especially exactly-one grid overlap, implication counterexamples and shortest-route counting. More operations do not automatically constitute better geometry or a balanced curriculum. Do not describe these puzzles as a comprehensive geometry progression.

### New breadth strands, each starting at level 6

| Topic | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bar Model Lab | Whole and missing part | Sum/difference | Multiplicative total | Multiplicative difference | Equalizing transfer | Relation followed by change | Equal units with an extra |
| Measure and Build | Ruler starting away from zero | Scaled ruler | Metres and centimetres | Missing rectangle side from perimeter | Rectangular area | L-shaped area by removing a corner | Equal area, different perimeter |
| Data Detective | Read picture graph | Apply mark scale | Scaled category difference | Combine categories | Recover the scale | Infer missing category | Largest/smallest difference |
| Time Journey | Within-hour elapsed time | Across-hour elapsed time | Hours/minutes conversion | Ending time | Starting time | Work versus breaks | Reverse a timetable |

The new topics introduce different mathematical objects, units and representations rather than relabeling an existing equation. They currently use bounded generated original tasks and passive diagrams. Time uses explicit same-day digital times and timelines; analog clock reading, dates, midnight crossings and calendars are not delivered. Measurements cover length/area/perimeter; mass and liquid volume remain future work.

### Source, navigation and verification

`learning/higher-math.js` owns the generated upper/new tasks, mathematical model renderer, meaningful hints, visible keys, topic descriptions and passive previews. `learning/higher-math.css` owns their layout. `tools/build_math_extensions.py` embeds these and shared `learning/pictures.js` into self-contained `math.html`; commit all authoring and generated changes together. Math-specific models do not change the other subject pages. Menus never generate practice tasks or consume randomness.

`tests/extended-quality.cjs` independently solves 6,000 generated tasks across all 100 upper/new entries, preserves the other-subject diagram checks, and tests retries, passive completion, same-level Next and the level-12 limit. `tests/math-depth-models.cjs` checks 1,848 exact diagrams, named generator conditions, optional guidance, stable retries, result cleanup and continuation for all 100 entries under normal and blocked storage. `tests/math-navigation.cjs` checks 160 passive previews and all three topic pages without randomness consumption. Existing math suites protect levels 1–6; these software checks do not establish rendered layout, Kindle support or child comprehension. Live Chrome independently solved representative tasks in all twelve original topics and five entries across the four new strands, including wrong retry, guidance, completion and same-level continuation. The initial rendered baseline is recorded in STATUS.md. Normal area grids target 36px cells; paired same-area diagrams use the same 24px unit scale. Model accessible descriptions expose the known quantities and relations rather than only a generic picture title. Actual Kindle layout and child comprehension remain unverified.

### Next breadth and depth, with prerequisites

| Next strand or refinement | Required foundation | Meaningful extension |
| --- | --- | --- |
| Money and budgeting | Value equivalence and base-ten units | Coins, cents/dollars, change, constrained purchase choices |
| Mass and capacity | Reading scales and units | Compare measurements, unit conversion and combining quantities |
| Geometry beyond grid operations | Shape properties and measurement | Angles, symmetry axes, 3D faces/nets and spatial explanations |
| Fractions beyond same denominators | Same whole, equal partitions and equivalence | Unlike-denominator comparison/addition and fractions of a set |
| Decimals and percentage | Place value and fraction equivalence | Tenths/hundredths, decimal measurement and proportional quantities |
| Reasoning and strategy | Understand the current mathematical model | Choose a valid model, explain an error, find multiple solutions and check by an inverse relation |

Prioritize model-choice and error-explanation activities before adding more symbolic operation chains. Use concrete objects outside the screen where useful, then connect an accurate diagram to notation. The app can provide original bounded practice; its results do not measure mastery or validate a child's readiness.

Curriculum reference: Singapore MOE [Primary Mathematics syllabus, updated October 2025](https://www.moe.gov.sg/-/media/files/primary/2021-primary-mathematics-syllabus-p1-to-p6-updated-october-2025.pdf) organizes Number/Algebra, Measurement/Geometry and Statistics with mathematical processes across them. The indexed Primary Two content includes measurement, time and scaled picture graphs; the PDF download itself was blocked during this review, so no complete syllabus-coverage claim is made. NIE/NTU's [CPA course description](https://www.ntu.edu.sg/admissions/continuing-education-programmes/detail/nie-cme0002-singapore-primary-mathematics-concrete-pictorial-abstract) emphasizes connecting concrete materials, representations and notation. These inform this original design, not a licensed course, grade map or effectiveness claim.

## Original levels 1–6: direction and delivery order

On 2026-10-09 the owner approved extending the existing topic-first math page to six task levels, roughly corresponding to ages 3–8, and authorized autonomous implementation, verification and publication. Age references are not gates or developmental assessments. Each topic has its own progression. Existing uncapped, manual same-level continuation remains in place.

Implementation order: six-level navigation; level 4 arithmetic; level 4 spatial/rule tasks and Tens Workshop; level 5 and sharing; level 6 and fractions; generated-question checks and published-browser checks. Higher-level entries are published together with their working activities, not as empty placeholders.

## Curriculum map

| Topic | Level 4 | Level 5 | Level 6 |
| --- | --- | --- | --- |
| Rabbits | Add, subtract and complete number bonds within 20 | Equal groups, multiplication and exact shares | Full servings followed by leftover count |
| Train | Within-20 whole/part relationships | Two station changes, one answer at each step | Undo station 2, then station 1 to find the original quantity |
| Track | Combine reusable lengths 2, 3 and 5 | Reach a target with a finite tray | Reach both target length and required piece count |
| Counters | Move counters to bridge through ten | Regroup tens/ones arithmetic with optional picture tools | Row/column arrays, division and hidden array counters |
| Pattern | Growing quantities, alternating shapes plus growing quantities | Constant forward/backward jumps | Identify the wrong term, repair it, then fill the gap |
| Sorting | Find all objects meeting shape AND size | Shape AND NOT a size | Four membership regions: A only, B only, both, neither |
| Shapes | Fill a rectangle with three pieces | Reflect a 3×3 picture across a vertical mirror | Rotate and place mixed pieces without overlap |
| Comparison | Add enough to make two quantities equal | More-than/fewer-than relationships | Find both quantities from their total and difference |
| Position | Follow six screen-direction arrows | Reach a flag through one waypoint around walls | Reach the flag after two ordered waypoints around walls |
| Tens Workshop | Find leftover ones, with optional bundling | Carry and borrow arithmetic, including two-digit additions | Find a missing quantity with a place-value picture |
| Share Fairly | Not offered | Exact fair shares and equal grouping | Largest equal whole shares, or whole groups and remainders |
| Fraction Kitchen | Not offered | Not offered | Shade halves/thirds/quarters, match fractions, compare unit fractions, identify equal partitions, and connect one half with two quarters |

The first nine topics retain their existing levels 1–3. Tens Workshop begins at 4, Share Fairly at 5, Fraction Kitchen at 6. Topic tiles show marks only for available levels. Every available level is selectable. Six staircase bars and a persistent numeric badge identify the current level.

This is an original pictorial activity bank inspired by concrete–pictorial–abstract progression. It is not a complete Singapore Mathematics syllabus, licensed course, or validated assessment. The original level-6 fraction foundation is introductory; the current upper levels add like-denominator arithmetic. Multiplication still uses bounded small equal groups, not a full times-table curriculum. Current breadth and remaining gaps are described above.

## Generators and mathematical conditions

- Three task variants use shuffled bags with no adjacent variant repetition. Within a variant, valid quantities, positions, layouts, conditions or choice order vary. New questions never imply a forced next level.
- The page now retains eight initial task signatures per topic/level and rerolls at most twelve times within the already selected variant to reduce recent repetition. Retry does not regenerate a question. Small fixed banks use a bounded fallback; reload clears history. See [QUESTION_QUALITY.md](QUESTION_QUALITY.md).
- Within-20 bridge tasks use first parts 6–9 and second parts 3–9. When their total reaches ten, addition offers a concrete transfer to fill the first frame. Subtraction and missing-part variants preserve the whole/part relation.
- Regrouping starts with 2–6 tens and 1–4 ones. Addition chooses enough added ones to require a carry; a variant adds another 1–2 tens too. Subtraction removes 6–9 ones so borrowing is necessary. Bundled/unpacked representations conserve total quantity. Subtraction offers an optional explicit removal action; numerical answers are available from entry.
- Train starts at 10–18 with station changes 2–8. Generated departures never exceed the available passengers. Forward and reverse tasks ask one step at a time.
- Groups use 2–5 groups of 2–5 objects. Whole-serving remainder tasks use a remainder from 1 to divisor minus 1. Fair-sharing remainder tasks instead use a remainder smaller than the recipient count. These are distinct questions.
- Track targets are generated from an available witness combination. Finite stock is consumed at most once; reusable stock can be reused. The validator checks conditions, not the witness. Excess length and wrong piece count remain editable with Undo.
- Comparison sum/difference problems are generated from two integer quantities, so both answers are whole numbers.
- Constant-jump sequences show five values and one gap. Repair questions change exactly one interior value; correct surrounding values establish the intended jump.
- Sorting always contains examples of every shape/size combination, so required selections and distractors exist. Membership bins use both predicates.
- Tiling uses solvable three-piece silhouettes; rotations are normalized to the selected top-left origin. Fit, walls and occupied cells are checked before placement. Every complete legal tiling is accepted.
- Mirror options are distinct; the correct reflection switches columns without switching rows.
- Grid routes are generated from a legal path. Walls are chosen outside that path; waypoints occur in the required order. Solvers may find different valid paths.
- Fraction wholes have the same width. Partition sizes sum to the whole; equal-part questions include both equal and unequal divisions. No comparison silently changes whole size.

## Interaction

A single numerical choice, last correct selection or final placement completes the task. Multi-step questions expose the next decision only after the previous one is correct. No submit button, animation loop or timer is introduced.

Manipulatives use large taps. Track placement, tile placement, gifts and route moves have Undo. Invalid placement changes feedback without altering the model. A correct answer freezes scene controls as passive pictures. Main Next stays in the same level indefinitely; optional advance offers the next available level, and level 12 has no advance action. Back is always present.

Numerical picture models are visible from entry; an optional current-step hint adds guidance. Models stay fixed during retry. Early tasks remain pictogram-based; advanced tasks add mathematical symbols, short labels and a folded adult guide. Models do not require discovery taps; optional hints explain the current step. No adaptive mastery inference is implemented.

## Persistence and compatibility

One self-contained `math.html` holds CSS, ES5 JavaScript, embedded PNG art and all task generators. There is no runtime package or content request. Existing `kindle-math-levels-v3` played marks retain their identity and are extended to levels 4–6 and new topics. Marks mean practised, not mastery. Questions restart on reload; no per-question resume or offline reopening claim is added. Blocked localStorage still permits all tasks.

## Acceptance checks

- Legacy checks: 9 topics × 3 levels × 12 questions × 4 seeds = 1,296 solved questions, plus restart, advance and storage checks.
- Higher-level checks: 10 level-4 topics, 11 level-5 topics and 12 level-6 topics × 9 questions × 3 seeds = 891 solved questions, plus blocked-storage checks.
- Independent checks calculate arithmetic from displayed expressions, conserve regrouped quantities, search legal track combinations and tilings, find routes through visible conditions, check reflected cells, fraction widths, multi-step gating, retries and Undo.
- Every completed scene becomes passive, each topic stays active beyond question 3, and each question keeps its current level.
- Full script parses as ES5. Published-browser checks follow deployment; actual Kindle touch response, picture comprehension, layout and E Ink behavior remain device tests.

## Published-browser validation

The live page showed twelve topics, six entries for original topics, and only the eligible upper levels for new topics. Level-5 subtraction exercised unpacking, removal, answer and same-level continuation. This caught a representation bug where unpacked ones were normalized back into tens; the fix preserves the actual unpacked tens/ones and adds exact representation assertions. Level-6 fraction checks exercised retry, half/quarter equivalence, shading and matching; after eight answers the live page remained in level 6 at question 9. Desktop browser evidence does not establish Kindle rendering or E Ink performance.

## 2026-10-10: remove discovery taps

The owner reported unclear prerequisite taps, without identifying exact tasks. Bridge-through-ten, bundle and regroup questions now display numeric choices immediately. Diagrams are passive and explicit optional tool buttons can demonstrate transformations. Numerical picture models start visible; one optional current-step hint replaces the three-click ladder. Upper-level tasks show a current action cue. This supersedes earlier required manipulation and hidden-model descriptions; manipulation remains the task in sharing, placement and construction. Direct-answer regression checks supplement the existing generated-question checks. Other unclear tasks remain an audit priority.

## Current representation and interaction contracts

Remainder tasks ask for full groups without claiming exact division. Completed results use `total = divisor × quotient + remainder`. Valid actions clear old failure feedback. Route failures identify bounds/obstacles or order constraints. Fraction modes have specific action cues rather than a shared generic instruction.

Tile tasks use an explicitly marked bounding anchor, tap-to-preview and a second tap at the same anchor to place. Preview footprints identify conflicts; no piece is consumed until a valid placement. Rotation, different anchors and Undo reset the preview appropriately. Membership controls lie within the overlapping-set diagram with an outside destination below. Scaled item identities are preserved in bins. Comparison models show matching unknown segments and a separate known difference.

Grouping rows, classification sources and task spacing are more compact while interactive targets remain large. Tile trays use compact previews with full board-scale footprints on the board. Actual Kindle fit, legibility and child interpretation remain to be checked.

`node tests/math-usability.cjs` checks intermediate expressions, direct train answering, stale-feedback regression, preview/place/Undo, spatial set controls, segmented comparison models and all fraction cues, alongside the existing complete math suites. Final-answer correctness and solvability alone are insufficient evidence for displayed mathematics or task clarity.

Task guidance follows state: multistep arithmetic identifies the current step, an opened hint refreshes when advancing, route cues name the next arrow/star/flag and follow Undo, and solved comparison portions display the known B value. Completion replaces action instructions with an explicit same-level continuation or Back option, retains remainder/fraction summaries, and removes obsolete hint text. Completion cues must not borrow state from an earlier question or level.
