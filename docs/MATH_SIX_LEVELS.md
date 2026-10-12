# Math levels 1–12: implementation and original 1–6 foundations

## Current levels 7–12

All twelve topics now expose levels through 12; the three later-starting topics keep their original minimum levels (4, 5 and 6). There are 132 available topic/level entries. Six picture previews appear per menu page; 7–12 use a second page. Played marks keep the existing storage key and legacy `level + 2` index. Manual Next stays at the current level, and optional advance ends at 12. Levels are independently selectable skills, not age or grade assignments.

`learning/higher-math.js` provides bounded generators, and `learning/pictures.js` renders exact static grids, rule diagrams and equal-part fraction strips. `tools/build_math_extensions.py` embeds both in self-contained `math.html`; commit sources and page together. Arithmetic extensions share small-operand symbolic challenges across the original arithmetic topic contexts: multiplication/addition, distributive grouping, missing factors, balance equations, ratios and inverse expressions. They increase relationship complexity rather than assigning every child larger addition/subtraction.

| Strand | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- |
| Shapes | Rotate then reflect | Composed reflection | Several operations | Inverse composition | Transform then combine two grids by XOR | Another composed grid/XOR condition |
| Position | Turn relative to current facing | Reverse turns from an endpoint | Shortest path around walls | Shortest path through a waypoint | Get a key, visit a locked door, then reach the flag | Key plus ordered waypoint/door conditions |
| Patterns | Alternating increments | Two interleaved sequences | Transformed grid/XOR | Increasing differences | Inverse affine relation | Increasing step size |
| Sorting | Exactly one of two features | Three features together | OR within a negative condition | Two alternative conjunctions | Counterexample to an implication | Combine features while excluding one exact card |
| Fractions | Like-denominator addition | Like-denominator subtraction | Equivalent numerators | Groups of a fraction | Complete one whole | Missing addend |

Every route is constructed from a witness satisfying its conditions; obstacles stay off that witness. An independent state-space search verifies shortest distances. All matching selection cards are checked; wrong attempts preserve task state and completion makes choices passive. Math action prose is visually replaced by phase-specific symbols while full text remains accessible and in the adult guide. Essential equations and model quantities stay visible. These are initial original challenge strands, not comprehensive later-grade curricula.

Verification: `tests/extended-quality.cjs` uses independent coordinate transformations, set predicates, arithmetic/fraction calculations and a route-state search across 4,320 new generated tasks; it exercises all 72 new entry lifecycles and the level-12 boundary. The original math DOM, higher-level, quality, usability and navigation checks still protect 1–6. `tests/math-navigation.cjs` verifies 132 passive previews without consuming practice randomness. Actual child understanding of composed rules, symbols, relative turns and minimum-path counting remains a device/use check.

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

This is an original pictorial activity bank inspired by concrete–pictorial–abstract progression. It is not a complete Singapore Mathematics syllabus, licensed course, or validated assessment. Fractions do not yet include fraction arithmetic; multiplication uses small equal groups, not a full times-table curriculum. The goal is conceptual progression before expanding breadth.

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
