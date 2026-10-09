# Hub v0.1 — Design Decisions

## Purpose

Validate the entry layout, text size, touch targets, navigation, simple feedback, and screen refresh behavior before expanding the learning content. These samples are intentionally shorter than a full 10–15 minute activity.

## Decisions

| Decision | Rationale | Validation status |
| --- | --- | --- |
| One self-contained HTML file | No build step or requests needed while switching activities; simple GitHub Pages deployment | Implementation complete; actual Kindle pending |
| Conservative JavaScript syntax and basic DOM methods | Avoid dependencies on modern browser APIs | Exact Kindle browser support pending |
| White background, black text, 3px control borders | Clear separation in grayscale without relying on color | E Ink appearance pending |
| 24px body text and controls at least 68px high | Starting values for readability and touch testing | Actual physical size and comfort pending |
| Two columns at widths of at least 540 CSS pixels; stacked controls otherwise | Fit a portrait Hub while allowing narrow browser layouts | Kindle viewport and media-query behavior pending |
| User-driven screen changes only | Avoid timers, continuous animation, and automatic refresh | E Ink ghosting and response pending |
| No external fonts, images, canvas, SVG, or emoji | Keep loading simple and avoid special glyph requirements | System-font rendering pending |
| CSS borders draw blocks and shapes | Avoid network assets; circle uses border-radius | Circle rendering pending; use the shape test to verify |
| In-memory state only | Core activities do not require cookies or persistent storage | No saved progress or offline reload support |
| Readable static sections if JavaScript is disabled | Keep content accessible and explain unavailable interaction | No-JavaScript navigation uses ordinary anchor links |

## Scope

The four samples demonstrate the planned categories; they are not complete curricula. The story is labeled for reading together. The larger-text setting lasts only until reload. Counting records correct first attempts, allows retrying a wrong answer, and ends after three questions. Repeated taps on a solved question cannot add score.

GitHub Pages enablement is a repository setting and must be confirmed independently. No service worker, persistent storage, or modern offline API is required by this prototype.

## Development validation — 2026-10-09

- Passed: ES5 parsing with Acorn and interaction logic checks in jsdom, including scoring, retries, repeated taps, completion, navigation, resetting activities, story endings, text-size toggle, and touch-check state.
- Passed: static inspection that the page has no external script, image, or stylesheet assets.
- Pending: browser smoke checks, visual layout at the proposed viewport sizes, and network-disconnection behavior in a real browser. Chromium installation failed because the downloaded archive was invalid in the development environment. The browser test is included for rerunning where Chromium is available.
- Pending: every actual Kindle test and GitHub Pages deployment.

DOM checks do not verify CSS rendering, physical button sizes, browser networking behavior, or E Ink refresh.
