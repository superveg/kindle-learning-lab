# Four Capability Checks — v0.4

## Kindle results — 2026-10-09

The owner reported that all four checks passed on their Kindle:

- Real counting progress restoration.
- Nine-cell selection and deselection.
- The manual local-update check, including the observed display behavior.
- The tested static SVG circle/square comparison against PNG.

This is owner-reported actual-device evidence. The exact Kindle model and firmware were not supplied. It confirms these exercised checks on that device, not every browser API, every SVG feature, or other Kindle models. The excluded offline check was not part of this test.

Open **Grown-up check** and choose one of the four numbered buttons. These are diagnostic tools for an adult; the child's Hub keeps its existing pictogram entries.

## 1. Resume actual counting progress

Choose **Start counting test**. Answer the first question with 2, advance to question 2, and answer with 3. Refresh or close/reopen the same deployed page, return to this check, and choose **Resume saved counting**.

Expected: question 2, its selected correct answer, an enabled Next button, and score 2 are restored. Continue and finish; reopening and resuming a completed round should retain its completion state. Wrong-attempt state is also saved, so retrying after resume cannot turn a prior wrong attempt into a first-try point.

- Save the real count activity after a new round, each answer attempt, question advance, and completion.
- Store a versioned JSON object under `kindle-learning-lab.counting.v1` with question, score, answered, firstTry, and completed fields.
- Validate restored fields before applying them. Invalid/inaccessible storage does not break counting; the adult sees an error and can start a new round or clear only this counting key.
- Opening Count from the child's Hub deliberately starts a fresh round. Restoring is explicit from this adult check while the feature is being tested.
- The owner previously reported that the simple localStorage marker test worked. JSON state restoration and precise closed-browser behavior still require this device test.

## 2. Nine touch targets

Select cells **1, 5, 9**, then tap **5** again. Expected selection: **1, 9** only. Selected cells have double borders and matching aria-pressed state. Try corners and center; check that nearby cells do not change and the grid does not shift. Clear selection resets all nine.

The layout uses inline-block controls without drag gestures, canvas, or continuous pointer tracking. This helps assess future matching/classification activities.

## 3. Manual local DOM updates

Tap **Change the small area** slowly six times. A bounded number panel alternates black/white while the reference lines remain unchanged. The test stops at six; **Restart this check** resets it.

Watch for residual numerals, border ghosting, full-screen flashing, and noticeable delay. The code changes only the number panel and its progress text. It cannot command an E Ink partial-refresh waveform; the browser/device controls the physical display update. There are no timers or animations.

## 4. Static SVG comparison

Compare the PNG reference with an inline SVG drawing of the same circle and square. Both should have the same relative positions and black outlines. Report whether they look correct using the provided buttons.

This is a manual report, not automatic SVG support detection. Inline SVG is isolated to this adult diagnostic panel; children's existing raster pictograms and CSS shapes remain available. The test does not establish support for every SVG feature.

## Development validation

`tests/capabilities-dom.cjs` checks ES5 syntax, real-state restoration including solved/retry/completed states, score integrity, malformed or blocked storage fallback, scoped deletion, nine-cell toggles, finite updates/reset, static comparison markup, report controls, and return navigation. Existing Hub and storage checks also pass.

These DOM checks do not establish Kindle SVG rendering, layout/hit-target accuracy, physical refresh behavior, or disk persistence. Record the device model and firmware with actual results. The requested scope covers these four checks only.
