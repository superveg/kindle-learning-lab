# Runtime question quality

Updated: 2026-10-10. Questions are generated in frontend ES5 JavaScript when a level is opened or Next is chosen. Regression samples are not the site's question bank. No content server, pre-generated list or model call is needed while playing.

## Balanced variation and recent history

- Each topic/level uses a shuffled bag of three variants: every block of three contains all three, with no adjacent equal variants across bags. A new session has a random first variant.
- Quantity, construction, layout and answer order vary within valid generator conditions. Rerolling does not consume another variant or increment the displayed question counter.
- Retain the last eight initial task signatures per topic/level in page memory, including when returning through the menu. Reload clears this history; it is not saved progress and needs no localStorage.
- A signature records initial prompt/model structure and meaningful picture identity. It ignores answer-option order, scattered-dot positions and cosmetic rabbit/carrot/bear artwork variants. This reduces cosmetic changes being treated as a new arithmetic question. It is a practical comparison, not a proof that every mathematically equivalent puzzle is recognized.
- Try at most twelve candidates for the chosen variant. Prefer a task outside the recent window; if none is found, retain the last valid candidate. Small fixed banks, such as half-to-quarters equivalence, inevitably repeat. This bounded fallback also works with a pathological constant random source.
- Once shown, the task stays fixed through wrong attempts, hints, optional model actions and Undo. Only intentional Next or level entry generates another task. No timer, automatic next or adaptive assessment is introduced.

## Structural difficulty review

| Topic | Earlier structure | Later structure |
| --- | --- | --- |
| Counting | Small scattered quantities; then combine parts and use ten frames | Bridge through ten (4), regroup tens/ones (5), reason from arrays/hidden cells (6) |
| Train | Visible boarding/splits and one-step whole/part questions | Two forward changes (5), undo two changes in reverse order (6) |
| Track | Longer comparison, equal-unit measurement, missing length | Reusable lengths (4), finite stock (5), stock plus exact piece count (6) |
| Pattern | Repeating units and consecutive gaps | Growing/dual-attribute pattern (4), larger forward/backward jumps (5), repair plus completion (6) |
| Sorting | One attribute, switched rules, then four shape/size baskets | Conjunction (4), conjunction with negation (5), overlapping set membership (6) |
| Shapes | Identity, rotation/size invariance, all matches | Tiling (4), reflection (5), rotated silhouette placement (6) |
| Position | Relative placement, then copy two/three objects | Follow arrows (4), one waypoint/walls (5), ordered waypoints/more walls (6) |
| Comparison | More/fewer/equal, numeric difference | Missing part (4), relational statement (5), solve sum/difference in two steps (6) |

Topics are parallel learning strands, not interchangeable scores. Some scaffolding and concepts intentionally overlap; a level number does not prove a uniform difficulty across topics or suitability for an age. Negation may be harder to interpret while selecting an equivalent shape/size group. Device/child observation is still required. Preserve these structural boundaries when adding generators; do not merely enlarge numbers.

## Validation

Run `node tests/math-quality.cjs` alongside both existing math regression suites. The quality check samples 1,080 initial questions across all sixty combinations, verifies three-variant balance, bounded history, menu continuity and arithmetic recent-repeat avoidance with a seeded random source. A constant-source check exercises fallback; structural checks inspect routes, finite stock, reverse stories, negation, membership, arrays and repair tasks. Tests do not establish child intuitiveness or actual Kindle performance.
