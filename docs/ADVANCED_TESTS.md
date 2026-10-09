# Advanced Device Checks — v0.5

Open **Grown-up check** and choose numbered checks 5–7. They are adult diagnostics; drag tracking and delayed updates are isolated here, not added as requirements for children's activities. Actual Kindle results for these new checks remain pending.

## 5. Drag input and moving display

Move the black block and release your finger inside the dashed target. The default **Show movement: OFF** mode records the gesture but moves the block only after release. It reports whether release was inside the target, the number of move events, and the selected input path. Enable **Show movement: ON** to observe actual movement updates and compare lag, ghosting, and unintended page scrolling. Reset to repeat.

The implementation uses Pointer Events when available, with touch and mouse fallbacks otherwise. Event-listener option support is probed before requesting non-passive touch movement. Scrolling is prevented only for an active gesture originating on the block. Pointer/touch cancellation, leaving the diagnostic, and window blur cancel an unfinished drag. Release coordinates determine target success. No animation timer or drag-and-drop framework is used.

Check separately that (a) the correct target is recognized, and (b) visible movement feels acceptable on E Ink. A successful drop does not prove that following the finger is comfortable. If either fails, existing tap-to-select controls remain the simpler alternative. These paths need actual device testing; simulated events do not establish browser touch support.

## 6. Timestamp-based elapsed time

Start, wait about 30 seconds with an independent clock, then choose Check or Stop. Also try navigating away and back, and briefly sleeping the Kindle while the same document stays loaded. Elapsed time uses the difference between Date timestamps, rather than counting timer callbacks. The displayed value only updates when requested or when returning to this diagnostic; there is no ticking interval.

Stop retains the displayed final duration. Reset clears it. Reloading or a browser unload loses this diagnostic's timer state. Device clock corrections can affect Date-based durations; a backward jump is reported, while forward clock corrections may overstate elapsed time. Kindle sleep/unload behavior and observed accuracy remain pending.

## 7. One delayed result

Start once; a black result block should appear after about 3 seconds. The displayed actual delay is measured from timestamps, so late browser callbacks are reported honestly. The start control is disabled while waiting and extra invocations are ignored.

Cancel or leave the diagnostic to clear the pending timeout. A generation token prevents an old cancelled callback from affecting a new attempt. Browser scheduling may delay results, especially during sleep/backgrounding; this test does not promise an exact callback time.

## Development verification

`tests/advanced-dom.cjs` validates ES5 syntax; simulated mouse, touch, and pointer paths; release-only versus visible-movement updates; inside/outside/cancelled drops; timestamp-based duration across navigation; stopped timer state; backward clock reporting; and duplicate, cancelled, or stale delayed callbacks. Existing counting, grid, SVG, marker-storage, and Hub DOM checks also pass.

Browser rendering, actual touch scrolling, finger-follow lag, ghosting, and real Kindle sleep/timer behavior require the owner's device test. No new backend, continuous animation, external dependency, or offline capability is introduced in the shipped page.
