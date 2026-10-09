# Math stories — v0.7

## Objective and confirmed inputs

The owner approved a Singapore-inspired concept sequence on 2026-10-09 and requested less cumbersome input, clearer actionable objects, better illustrations and randomized/dynamic pictures. Replace the v0.6 nine-activity menu with three linked story activities plus scattered-dot counting. Preserve the original Hub samples, diagnostics, GitHub Pages hosting and browser compatibility conventions. Exact Kindle model is unknown.

## Implementation steps and decisions

1. Offer suggested age levels 3/4/5 and four picture tiles. Each tile ends after three rounds. Ages are starting difficulty, not developmental cutoffs.
2. Feed rabbits: match one carrot to each rabbit. Hungry rabbits are tappable; fed rabbits are passive. Carrot inventory updates after each action. Rabbit order stays stable within a round.
3. Train: board a fixed total; explore arbitrary splits of that total; fill the missing part given passengers in the first carriage. The split round intentionally stays editable after Next becomes available. Moving one passenger conserves the total. The last needed seat automatically completes the missing-part round.
4. Track: younger level compares two equal-unit tracks with randomized longer side. Older levels place equal-size sleepers in gaps. Units become passive pictures; the final gap completes the round. Real-world measuring is an adult-guided extension.
5. Dots: select a numeral for randomly scattered, nonoverlapping dots. Quantities, positions and choice order vary. A wrong answer does not regenerate the problem. Use 12 cells with bounded jitter; dots have equal diameter.
6. Replace submit/check with immediate answer feedback and automatic detection of explicit terminal goals. Keep Next manual, allowing inspection of the result and avoiding automatic page jumps.
7. Reference pictures are not buttons. Freeze completed controls into passive elements. Open exploration is the exception: editable passenger buttons remain visibly actionable.
8. Embed all PNG art and scripts. Draw original conservative black-and-white rabbits, carrots, bears with varied hats, locomotive, ruler and dot icons. Art generation uses Pillow during development only. No timer, continuous animation, SVG, CSS transition, canvas, fetch or additional runtime dependencies.
9. Use new `kindle-math-stories-v2` completion marks, with scoped clear and storage-failure fallback. Leave old marks intact. Completion denotes played, not mastery; per-question resume is not implemented.

## Acceptance and verification

- Passed ES5 parsing and DOM checks for all 12 age/activity combinations, 36 rounds each across four seeded random streams (144 exercised rounds).
- Passed immediate completion, Next gating, wrong answer recovery, stable rabbit order and dot layout during a round, nonoverlapping dot coordinates, varied layouts across seeds, conserved train totals, editable splits, arbitrary seat order, completed controls becoming passive, restart, completion marks and blocked storage.
- Regression: original Hub, storage, capability and advanced diagnostics checked separately against the refreshed main-branch source, preserving the newer timer change.
- PNG contact sheet inspected visually. Full browser layout check unavailable because no browser executable is installed. Device input, picture comprehension, clipping, touch sizes and E Ink refresh remain pending.
- Kindle acceptance: demonstrate feeding; try a wrong dot answer then correct; verify the picture stays still; move a passenger twice and inspect total; fill a seat out of order; complete/reopen a story and inspect the played mark. Reopening offline is a separate unimplemented capability.

## Educational references and limits

- https://nel.moe.edu.sg/la/numeracy/how-can-you-do-it-/using-concrete-pictorial-abstract--cpa--approach/
- https://www.singaporemath.com/pages/what-is-singapore-math

These are original story activities inspired by CPA and part-whole relationships, not a complete Singapore Math curriculum. On-screen objects are pictorial, not replacements for the physical concrete stage. Adult guides connect each experience with physical toys. The current rabbit rounds practise one-to-one correspondence; they do not yet cover shortages or leftovers. Track filling models equal units; it does not assess a child's general measurement ability. Difficulty across domains is intentionally not uniform.
