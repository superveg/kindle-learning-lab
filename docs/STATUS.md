# Current project status

Updated: 2026-10-10. For decisions and continuity, read [SESSION_HANDOFF.md](SESSION_HANDOFF.md). Historical v0.x notes explain earlier implementations; their pending statements do not supersede newer evidence here.

## Delivered

- Static Hub and adult diagnostics, deployed through GitHub Pages.
- Optional marker persistence and a separate real counting-resume diagnostic.
- Four capability checks owner-reported passing on Kindle.
- Drag/release diagnostics, timestamp-based elapsed time with approximately ten-second refreshes, and cancellable delayed-result diagnostics.
- Twelve math themes and six task levels; sixty available combinations. Same-level random practice has no fixed question cap.
- Levels 4–6 include tens, regrouping, grouping/remainders, multistep stories, constraint-based construction, spatial reasoning and introductory fractions.
- Latest interaction revision: immediate numeric answers, passive reference models and optional explicit tools in bridge/bundle/regroup questions; visible upper-level task cues; one optional hint instead of a discovery ladder.
- Picture-led interface: six topics per page, 60 passive level examples, played marks on level selection, compact toolbar, evenly spaced numeric answers and distinct Continue/level-change controls.
- Runtime question quality: eight recent initial tasks per topic/level retained in page memory; up to twelve candidate generations preserve balanced variants while reducing recent repeats. Small banks repeat safely. See QUESTION_QUALITY.md.
- After changes, maintain useful long-term project knowledge in place; no chronological change log or mandatory per-change report.

## Checks and remaining uncertainty

All four math suites and the interface navigation check pass: 1,296 legacy and 891 higher-level solved questions, ES5 parsing, 1,080 quality samples across all sixty combinations, and focused interaction checks. Coverage includes arithmetic, legal construction, retries, Undo, passive completion, history, variant balance and storage fallback. Guidance checks also cover current-step hints opened before/after phase changes, route targets, known comparison portions and completion without stale cross-level summaries.

Published interaction contracts include immediate numeric answers, optional picture tools, valid remainder identities, fresh feedback, specific fraction modes, tile anchor/footprint previews, spatial set destinations and segmented comparison models. Task cues and opened hints follow the current phase; completion offers another question at the same level or Back instead of repeating an unfinished action. See MATH_SIX_LEVELS.md.

Prior live Chrome verification covered nine themes and tile preview/rotation/Undo/completion/continuation. Compact set/tile scenes were inspected; desktop measurements do not guarantee Kindle layout. GitHub Pages deployed successfully. Live Chrome rechecked reverse-stop hint refresh, comparison step cues and known B values, route target changes and Undo through completion, three fraction variants, completion summaries and same-level continuation. These checks establish desktop behavior, not child comprehension or Kindle compatibility.

Exact Kindle model/firmware, advanced diagnostic device behavior, upper-level picture comprehension, touch response and E Ink refresh are not fully verified. No offline reload/reopen, cross-device synchronization or per-question math resume is promised.

The interface navigation check covers topic paging and return continuity, all 60 previews without random-number consumption, toolbar state, played marks, same-level continuation and explicit level change. Live Chrome verified both topic pages, preserved paging after Back, rabbit and Tens level previews, compact task navigation, evenly spaced numeric choices, stable wrong-answer retries and distinct continuation/advance controls. Desktop layout does not establish small-screen or Kindle fit; actual Kindle layout and comprehension remain pending.

## Beyond-math release

Logic, Chinese, English, Everyday Science and Stories/Social Situations are implemented through `subjects.html`: six freely selectable levels per subject, three families per level, 1,252 authored seeds. Every family supports uncapped manual continuation, shuffled banks and stable retries. See [LEARNING_MODULES.md](LEARNING_MODULES.md) for current contracts, coverage and verification limits; [LEARNING_EXPANSION_PLAN.md](LEARNING_EXPANSION_PLAN.md) retains the detailed academic direction.

Software checks exercise 9,000 continuous questions across all 90 families, independent picture/feature predicates, alternate legal orders, wrong-order Undo, repeated letters, 360 authored story-ending paths, storage failure and ES5 parsing. Live Chrome opened all 90 activity entries, with no broken visible images or desktop horizontal overflow, and checked wrong retries, passive completion, Chinese inference/evidence, science prediction/Observe and story consequences/continuation. Multi-stage clues remain visible after advancing. This establishes implementation behavior, not educational effectiveness. English audio/phonics and actual Kindle Chinese glyphs are unverified; early language and text-based logic tasks need adult narration. Every family has at least twelve seeds, recent-ten content exclusions with storage-backed reload continuity, and bounded frontend science records. 2,250 constant-RNG rounds and 2,928 independent numeric-record checks pass. Finite narrative banks still eventually repeat. Current live Chrome repeat checks completed 13 rounds in a representative family from each of the five subjects without repeats in the preceding ten; English reload preserved exclusions. Fifteen everyday-object/animal pictures use reviewed OpenMoji black SVGs, rasterized into embedded PNGs with retained CC BY-SA 4.0 source/license and guide attribution. Sock/shoe silhouettes are distinct; cat/dog and position composites were inspected at display size. Live Chrome checked a level-1 entry in each subject for loaded images/no horizontal overflow, completed socks-before-shoes with immediate feedback and continued to another question, and opened public picture credits from the guide. Actual child recognition and Kindle rendering remain pending.

## Documentation map

| Document | Purpose |
| --- | --- |
| [LEARNING_EXPANSION_PLAN.md](LEARNING_EXPANSION_PLAN.md) | Five subject outlines, six-level details, interaction and delivery plan |
| [QUESTION_QUALITY.md](QUESTION_QUALITY.md) | Runtime generation, recent repeats, balance and structural level boundaries |
| [PROJECT.md](PROJECT.md) | Product and implementation constraints |
| [SESSION_HANDOFF.md](SESSION_HANDOFF.md) | Durable owner decisions, engineering context, evidence and next priorities |
| [MATH_PLAYGROUND.md](MATH_PLAYGROUND.md) | Initial math themes and evolution |
| [MATH_SIX_LEVELS.md](MATH_SIX_LEVELS.md) | Higher-level curriculum and generator rules |
| [KINDLE_TEST.md](KINDLE_TEST.md) | Actual-device checklist, not an automatically completed report |
| [CAPABILITY_TESTS.md](CAPABILITY_TESTS.md) | Four tests and owner-reported results |
| [ADVANCED_TESTS.md](ADVANCED_TESTS.md) | Adult drag and timing diagnostics |
| [LOCAL_STORAGE_TEST.md](LOCAL_STORAGE_TEST.md) | Marker storage scope and procedure |
| [PICTOGRAMS.md](PICTOGRAMS.md), [HUB_DESIGN.md](HUB_DESIGN.md) | Historical design decisions |
| [TASK_TEMPLATE.md](TASK_TEMPLATE.md) | Development task format |

