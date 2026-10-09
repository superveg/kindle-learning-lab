# Math playground — v0.6

## Objective and confirmed inputs

The owner requested interactive mathematics content for ages 3, 4 and 5 on 2026-10-09. This explicitly expands the former 3–4 scope. Preserve static GitHub Pages, black-and-white pictures, large controls, minimal reading, ES5 and finite sessions. Exact Kindle model remains unknown. Previously reported successful capability checks do not establish compatibility with this new page.

## Implementation

1. Keep the original Hub and device checks; add a pictogram tile linking to the self-contained `math.html`.
2. Offer three suggested age levels, with unrestricted switching and nine activities at each level. Each activity ends after three rounds; it never advances automatically.
3. Use tap manipulation instead of requiring drag events, continuous animation or timing.
4. Embed required image assets and script. Navigation from Hub to math needs an initial page load; offline reopening is not promised.
5. Save only completion marks in the browser with a namespaced key and scoped clear. Storage failure leaves activities available. Completing rounds is not evidence of mastery. Per-question resume is not implemented.
6. Provide an English adult guide per prompt; adults can explain in Chinese or another home language. Age levels are curriculum starting points, not population averages or diagnostic milestones.

## Activity map

| Activity | Suggested 3 | Suggested 4 | Suggested 5 |
| --- | --- | --- | --- |
| Count each one | Mark/count 2–4 blocks | Mark/count 4–6 | Mark/count 6–10 |
| Pack the wagon | Build quantities 2–4 | Build 4–6 | Build 6–10 |
| Compare groups | More / equal; larger side changes | More / equal | Differences 1, 0, 2 |
| Join and take away | 2+1, 2−1, 2+2 with blocks | 4+1, 4−1, 4+2 with blocks | 4+1, 4−1, split 5 into 2+3 |
| Shapes | Match circle, square, triangle | Match shapes | Choose by corners/sides |
| Patterns | AB with changing symbols | AAB | ABC |
| Sort blocks | Three blocks by shape | Four blocks by shape | Five blocks; middle round changes to length |
| Measure | Compare longer tracks | Build 3–5 equal units | Build 3–5 equal units |
| Position | Above, below, inside | Above, below, inside | Above, below, inside |

Some foundational concepts intentionally recur at multiple ages; levels do not imply every domain becomes harder. The length sorting round contrasts short square blocks with long circles, so adult real-object follow-up is needed to test sorting independent of shape. Position instructions benefit from adult demonstration. Shape rotation, structured small-set recognition, general classification, number conservation, and authentic measurement of real objects are follow-up opportunities rather than claims about the current screen content.

## Acceptance and verification

- 27 selectable activities / 81 finite rounds; wrong answers remain editable, Next is gated on correctness, repeated checking does not advance.
- Completion marks distinguish finished activities, restart resets the round, storage failure has an in-memory fallback, clearing targets only math marks.
- All application JavaScript parses as ES5. No external runtime dependencies or content requests during an active math session.
- Passed `tests/math-dom.cjs` for all ages, activities, correct solutions, retries, completion, restart and blocked storage.
- Passed existing hub, storage, capabilities and advanced DOM checks.
- Browser visual verification could not run: installed Playwright has no browser executable. No actual Kindle test performed for v0.6.
- Device acceptance: open new tile; try all nine activity types, inspect width/touch sizes and PNG arrows, show the child the prompts once, complete three rounds, return/reopen and inspect completion marks. Verify fresh navigation/reload online separately from interaction during disconnection.

## Educational basis

The activity sequence adapts Head Start's 36–48 month, 48–60 month and by-60-month mathematics framework and NAEYC/NCTM's early mathematics guidance. Numeric ranges above are implementation choices, not diagnostic age cutoffs.

- https://headstart.gov/school-readiness/article/math-preschool
- https://www.naeyc.org/positionstatements/mathematics
