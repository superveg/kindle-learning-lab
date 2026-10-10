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
- After changes, maintain useful long-term project knowledge in place; no chronological change log or mandatory per-change report.

## Checks and remaining uncertainty

Current math verification (2026-10-10): 1,296 legacy and 891 higher-level solved questions, direct-answer checks, ES5 parsing and 1,080 quality samples across all sixty combinations passed. Checks cover arithmetic, legal construction, retries, Undo, bounded history, menu continuity, balanced variants, constant-random fallback and structural constraints.

GitHub Pages deployment succeeded. Live Chrome verified direct answers and optional regrouping with stable choices, then nine distinct level-5 expressions with balanced variants and same-level continuation to question 10. Browser checks do not establish Kindle performance or child comprehension.

The reviewed implementation patterns now have fixes: valid remainder identities, fresh feedback after actions, immediate train answers, specific fraction cues, tile anchor/footprint preview, spatial set destinations, segmented comparison models and more compact group/classification layouts. All four math suites passed: 1,296 legacy and 891 higher-level solved questions, 1,080 quality samples, and focused checks for the revised mathematics/interaction contracts. GitHub Pages deployment succeeded. Live Chrome rechecked nine themes: corrected remainder identities, direct train subtraction, error recovery in patterns/routes/tiles, three fraction modes, complete set classification, equal-width comparison segments, counters and tile preview/rotation/Undo/completion/continuation. The compact set scene measured 372 pixels high, and a representative final tile scene 442 pixels high in the desktop viewport; this does not guarantee every layout fits a Kindle. Child comprehension and actual Kindle layout remain unverified.

Exact Kindle model/firmware, advanced diagnostic device behavior, upper-level picture comprehension, touch response and E Ink refresh are not fully verified. No offline reload/reopen, cross-device synchronization or per-question math resume is promised.

## Documentation map

| Document | Purpose |
| --- | --- |
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
