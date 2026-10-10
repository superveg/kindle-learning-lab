# Math topics and levels — v0.10

## Confirmed direction

The owner found the former age 3/4/5 differences too small. On 2026-10-09 they clarified that visible progression matters more than age labels, and authorized choosing a suitable structure. The app now opens with nine topics. Each topic offers levels 1, 2 and 3 with a staircase pictogram. Levels describe tasks, not ages or developmental norms. All are selectable, with no mastery gate or forced advancement.

## Learning progression

| Topic | Level 1: visible matching | Level 2: parts and rules | Level 3: hidden parts and multiple decisions |
| --- | --- | --- | --- |
| Rabbits | One carrot per rabbit | Two carrots per rabbit | Find a hidden carrot group from a total of 8–12 and a visible part |
| Train | Board, move, and fill visible seats | Split a total; find a hidden part of 5–7 | Combine two groups, subtract departures, find hidden passengers |
| Track | Compare aligned equal-unit lengths | Place equal units, then choose the measured length | Find missing units for a total length of 6–10 without countable gaps |
| Counters | Count 2–4 scattered dots | Combine two visible groups totalling 4–7 | Use five/ten structure for 8–12, subtract removed counters, find hidden counters |
| Pattern | One gap in AB | One gap in AAB, with varying stopping points | Two consecutive gaps in AAB, ABB and ABBC |
| Sorting | Shape only | Change between shape and size | Shape AND size: four baskets |
| Shapes | Match an unchanged shape | Match changed size/orientation | Find all three members among six varied choices |
| Comparison | More/fewer/equal | Numeric difference, including zero | First choose the larger group, then its numeric difference |
| Position | Copy above/below/inside from a picture model | Copy two objects in a 3×3 arrangement | Copy three objects using both row and column |

These are original Singapore-inspired pictorial activities, not a licensed curriculum or a validated assessment. On-screen counters are pictures; adult guides suggest related work with physical objects. Some level 1 train rounds introduce visible part-whole relationships as exploration. Task difficulty varies by topic; a number does not certify mastery.

## Interaction and implementation

- Choose a topic, then a clearly numbered level. The filled staircase and level number remain above every round. Topic tiles show separate played marks for each level.
- Three rounds provide a natural stopping point. After completion, a large arrow/staircase offers the next level, without automatically starting it. Back returns to the topic's levels; a second Back returns to topics. Home uses a house and Back uses an arrow.
- Actions have immediate feedback with no submit step. Completed targets become passive. The exploratory train split remains editable and Next becomes available after a move.
- Hidden-part questions show a whole and visible part, not an answer-sized row of empty slots. Correct numerical choices fill the hidden group and show the completed equation.
- Multi-step tasks reveal one decision at a time: the active pattern gap, the current spatial object, and the second comparison question. Correct placements remain visible. Wrong choices preserve the scene and can be retried.
- Sorting baskets are passive until an object is selected. Level 3 size references use the same physical image dimensions as the source, so size is a visible property.
- Quantity, identity, arrangement and answer order vary on a fresh round. Models remain still while answering. No continuous animation, timer or speed pressure.
- Static self-contained HTML, CSS and ES5 JavaScript with embedded monochrome PNG illustrations. No new runtime dependencies or modern browser APIs.
- New completion key `kindle-math-levels-v3` avoids treating prior, easier age-based rounds as completion of the new levels. Previous keys are preserved. Browser saving is optional and marks mean played, not mastered. Per-question resume and offline reopening are not implemented.

## Acceptance and validation

- DOM tests cover 9 topics × 3 levels × 3 rounds × 4 seeded random streams (324 exercised rounds).
- Verify correct equations from displayed quantities, retries without changing models, two-step gating, all three shape matches, four-bin sorting by both attributes, conserved exploratory train totals, copied model positions, passive completed objects, next-level entry, scoped marks and blocked-storage fallback.
- ES5 parsing and original Hub, storage, capability and advanced diagnostic regression checks pass.
- The cloud browser can directly open and operate the published GitHub Pages site. The previous local Playwright executable limitation does not prevent that route.
- Direct published-browser checks confirmed the topic-to-level route, staircase display, level 3 train addition/retry/completion/subtraction, selection-gated four-way sorting, and sequential three-object spatial copying with a passive completed grid. The visual check led to a larger, aligned Back arrow and stable basket-reference alignment. Browser checks do not establish Kindle touch response, E Ink refresh behaviour, picture comprehension or offline reopening; those require actual device testing.

## References

- https://nel.moe.edu.sg/la/numeracy/how-can-you-do-it-/using-concrete-pictorial-abstract--cpa--approach/
- https://www.singaporemath.com/pages/what-is-singapore-math

## v0.10: pictorial relationships and stable interaction

- Hidden carrot, passenger and counter tasks show the whole above a branched pair of actual groups. The hidden part stays one undivided question mark. Train addition uses a question mark for the whole until the child answers; it never displays the answer early.
- Train subtraction is now a concrete action followed by a number decision. Tap the arrow-bearing passenger group to let it get off. Departed passengers become crossed, passive pictures and only then do numerical choices appear. The action does not complete the question.
- After identifying the larger comparison group, double borders mark its unmatched extras. The child then chooses their count; the complete equation appears afterward. Group sizes remain compact enough for a narrow display.
- Sorting preserves the source slots after placement, so other objects do not shift into the tapped location. Vacated slots are passive and the source area disappears when sorting finishes.
- Two-gap patterns retain the same answer order between gaps. Selected shape controls have fixed outer dimensions to avoid growing when a double border appears.
- DOM checks additionally assert departure gating/crossed group size, source-slot conservation, stable pattern choices and the exact unmatched-extra count across all seeded rounds. These are pictorial scaffolds, not new assessed competencies.
