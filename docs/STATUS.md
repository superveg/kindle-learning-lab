# Current project status

Updated: 2026-10-12. For decisions and continuity, read [SESSION_HANDOFF.md](SESSION_HANDOFF.md). Historical v0.x notes explain earlier implementations; their pending statements do not supersede newer evidence here.

## Delivered

- Static Hub and adult diagnostics, deployed through GitHub Pages.
- Optional marker persistence and a separate real counting-resume diagnostic.
- Four capability checks owner-reported passing on Kindle.
- Drag/release diagnostics, timestamp-based elapsed time with approximately ten-second refreshes, and cancellable delayed-result diagnostics.
- Sixteen math themes and twelve task levels; 160 available combinations. Four new strands begin at 6: bar models, measurement, data and time. Same-level random practice has no fixed question cap.
- Levels 4–6 include tens, regrouping, grouping/remainders, multistep stories, constraint-based construction, spatial reasoning and introductory fractions.
- Latest interaction revision: immediate numeric answers, passive reference models and optional explicit tools in bridge/bundle/regroup questions; visible upper-level task cues; one optional hint instead of a discovery ladder.
- Picture-led interface: six topics per page across three pages, 160 passive level examples, played marks on level selection, compact toolbar, evenly spaced numeric answers and distinct Continue/level-change controls.
- Runtime question quality: eight recent initial tasks per topic/level retained in page memory; up to twelve candidate generations preserve balanced variants while reducing recent repeats. Small banks repeat safely. See QUESTION_QUALITY.md.
- After changes, maintain useful long-term project knowledge in place; no chronological change log or mandatory per-change report.

## Current delivery and device decisions

Development, verification, direct-main delivery and ongoing skill/documentation maintenance follow [AGENT_WORKFLOW.md](AGENT_WORKFLOW.md). Current product and device evidence remains below.

The owner reports that iOS Home Screen web-app use avoids unwanted zoom in their setup. PR #4 for application-level zoom suppression was declined and closed without merging; its viewport and touch-guard changes are not deployed. This does not establish Kindle behavior.

## Checks and remaining uncertainty

Current upper-math quality revision replaces shared decorative arithmetic extensions with topic-specific quantity/process models, visible symbol keys and optional thinking steps. New strands use units, scaled picture graphs, area/perimeter and time relationships. Independent checks pass 6,000 generated upper/new tasks and 1,848 exact representations; all 100 upper/new entries have hint/retry/completion/continuation coverage with normal and blocked storage. Navigation checks cover 160 passive previews. Live Chrome independently solved a representative upper task in each of the twelve original topics, plus Bar Model Lab 12, Measure and Build 6/11, Data Detective 11 and Time Journey 12 against the initial quality-release baseline `38fc30501f8bd57c35bca2dcb364ec02f4a6c15c`. No desktop horizontal overflow appeared. Wrong retry, optional guidance, passive completion, same-level continuation and the level-12 limit were exercised. Follow-up model-only improvements enlarge normal area tiles to 36px, keep paired equal-area diagrams at the same 24px unit scale, and expose known model quantities in accessible descriptions. These pixel values are layout targets, not Kindle evidence. See MATH_SIX_LEVELS.md for progression and remaining curriculum gaps.


The twelve-level release adds 1,080 authored tasks (180 families total), picture-led paged menus and compact action cues. Independent software checks pass 4,320 new generated math tasks and all 72 new math-entry lifecycles; the 18,000-question learning DOM, authored quality, and 4,500-round recent-ten suites pass. Original math and Hub diagnostics pass. Reading content and necessary narrative/record conditions remain visible; higher written tasks can still require adult narration. Live Chrome verified the new paged menus and 17 representative activity entries across all five subjects: Logic levels 1/7/12 in all three families, plus the first family at 7/12 in each other subject. No broken visible images or desktop horizontal overflow appeared. An English level-12 evidence task retained its passage after a wrong retry, advanced its cue, completed passively and continued at the same level. Math level-7 rotate/reflection checked a stable wrong retry and completion; grid cells were measured at 24px in a correct 3×3 layout. This is targeted desktop evidence, not every rendered entry or child/Kindle validation. Actual-child/device comprehension remains pending.


All four math suites and the interface navigation check pass: 1,296 legacy and 891 higher-level solved questions, ES5 parsing, 1,080 quality samples across all sixty combinations, and focused interaction checks. Coverage includes arithmetic, legal construction, retries, Undo, passive completion, history, variant balance and storage fallback. Guidance checks also cover current-step hints opened before/after phase changes, route targets, known comparison portions and completion without stale cross-level summaries.

Published interaction contracts include immediate numeric answers, optional picture tools, valid remainder identities, fresh feedback, specific fraction modes, tile anchor/footprint previews, spatial set destinations and segmented comparison models. Task cues and opened hints follow the current phase; completion offers another question at the same level or Back instead of repeating an unfinished action. See MATH_SIX_LEVELS.md.

Prior live Chrome verification covered nine themes and tile preview/rotation/Undo/completion/continuation. Compact set/tile scenes were inspected; desktop measurements do not guarantee Kindle layout. GitHub Pages deployed successfully. Live Chrome rechecked reverse-stop hint refresh, comparison step cues and known B values, route target changes and Undo through completion, three fraction variants, completion summaries and same-level continuation. These checks establish desktop behavior, not child comprehension or Kindle compatibility.

Exact Kindle model/firmware, advanced diagnostic device behavior, upper-level picture comprehension, touch response and E Ink refresh are not fully verified. No offline reload/reopen, cross-device synchronization or per-question math resume is promised.

The interface navigation check covers topic paging and return continuity, all 60 previews without random-number consumption, toolbar state, played marks, same-level continuation and explicit level change. Live Chrome verified both topic pages, preserved paging after Back, rabbit and Tens level previews, compact task navigation, evenly spaced numeric choices, stable wrong-answer retries and distinct continuation/advance controls. Desktop layout does not establish small-screen or Kindle fit; actual Kindle layout and comprehension remain pending.

## Beyond-math release

Current upper-subject quality revision rewrites the 90 families at 7–12, preserving the 180-family/2,332-seed total and the level-6 foundation. Language now includes contextual meaning, inference, summaries, revision and actual evidence fragments; science uses labeled units/conditions, plausible record directions, repeated trials, competing explanations and investigation plans; stories focus on stated needs, boundaries, reasonable branches and revision rather than quantity copying. Logic has explicit keys/intermediate pictures and a deduction strand. Shared panels retain clues/observations across phases, with compact passive previews and consistent text-choice formatting. See LEARNING_MODULES.md for the per-subject map, source ownership and verification limits.

Focused checks cover all 1,080 rewritten seeds and all 90 upper entry lifecycles; full app checks pass 18,000 selections, 4,500 recent-ten rounds and 5,400 presentations across 720 fresh-page boundaries, including 225 storage-failure/malformed-history presentations. All 984 current story-ending paths are checked. The language checks establish authored consistency and evidence references, not an independent proof of natural-language meaning or child understanding. Published-browser evidence must be kept separate from these software results.


All five pages remain self-contained and reached through subjects.html. Recent-ten history is per family on the same browser/origin; storage failure remains playable in memory. Necessary reading, scientific conditions and story replies stay visible. Played marks do not mean mastery. English audio/phonics, actual Kindle Chinese glyphs, narrow-screen layout and child interpretation remain unverified. Existing picture-recognition tasks and lower-level object/location-composite risks remain recorded in LEARNING_MODULES.md; asset loading alone does not resolve them.

## Documentation map

| Document | Purpose |
| --- | --- |
| [AGENT_WORKFLOW.md](AGENT_WORKFLOW.md) | Agent procedure, delivery and ongoing instruction/skill upkeep |
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


## Upper-subject published-browser check (2026-10-13)

Chrome opened all three activities at levels 7 and 12 in each of the five subjects (30 entry states). At the tested 1363px viewport, these states had no horizontal overflow or broken visible images. Representative completed flows covered English contextual vocabulary, Chinese passage/evidence, logic clue revision, science claim limits and story checking/revision. Level-9 science also saved a neutral prediction, revealed the supplied observation only through Observe, and retained the record afterward. Browser review caught and corrected a sufficient alternate paper-boat evidence set, repeated story-opening prose, and a misleading two-clue label when size was a third condition. Identical condition panels across science stages are rendered once. These checks do not establish semantic correctness of every reading interpretation, small-screen/Kindle/iOS rendering, or child comprehension.
