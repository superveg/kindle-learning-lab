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
- Runtime question quality: eight recent initial tasks per topic/level retained in page memory; up to twelve candidate generations preserve balanced variants while reducing recent repeats. Small banks repeat safely. See QUESTION_QUALITY.md.
- Every delivered project change includes a dated CHANGELOG.md entry and relevant status/feature/decision documentation updates.

## Checks and remaining uncertainty

Pages successfully deployed implementation `80af5fe71629552c320d54f337bd5c5739c54534`. Live Chrome completed nine distinct Tens Workshop level-5 expressions, with each block of three using all three variants and no adjacent variant repeat; question 10 remained at level 5 with immediate answers and an optional picture tool. This is browser evidence, not Kindle or child-comprehension validation.

The runtime-quality revision passed both math regression suites (1,296 legacy and 891 higher-level solved questions), direct-answer checks, ES5 parsing, and 1,080 initial quality samples across all sixty combinations. Seeded variety, bounded history, menu return, balanced variants, constant-random fallback and structural constraints were checked.

Math checks passed on 2026-10-10: 1,296 legacy plus 891 higher-level generated questions, including retry stability, correct arithmetic, legal construction, Undo, progression and storage fallback. Additional checks assert that bridge, bundle and regroup questions can be answered without a preliminary tool click.

GitHub Pages successfully deployed implementation commit `1268f4ec04cfa5734687c620757adf3ed3b888a3`. Live Chrome validation confirmed that `63 − 7` at Tens Workshop level 5 could be answered immediately, without unpacking first; the next question stayed at level 5. For `31 + 9`, the optional bundle tool changed the model while preserving the answer options, and completing the question worked. A third initial question visibly showed its passive model, optional tool and answers together. These browser observations do not establish actual Kindle or child comprehension.

The owner reported unclear prerequisite clicks on 2026-10-10 without naming exact questions. Identified patterns have been simplified; other confusing tasks remain an audit priority. Automated correctness does not establish task intuitiveness.

Exact Kindle model/firmware, advanced diagnostic device behavior, upper-level picture comprehension, touch response and E Ink refresh are not fully verified. No offline reload/reopen, cross-device synchronization or per-question math resume is promised.

## Documentation map

| Document | Purpose |
| --- | --- |
| [CHANGELOG.md](CHANGELOG.md) | Dated changes, reasons, checks and unresolved limits |
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
