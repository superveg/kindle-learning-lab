# Local Storage Test — v0.3

The owner reported that this marker test worked on Kindle on 2026-10-09. The exact model, firmware, and separately tested restart behavior were not supplied.

## Scope

The grown-up check includes a small localStorage persistence test. It saves a generated marker only. The marker test itself does not save learning progress. In v0.4, the separate counting-resume check saves actual counting state under a different key. Other activities and settings still reset on reload. No accounts, cloud synchronization, or offline page reopening are implemented.

## Kindle procedure

1. Open the deployed HTTPS page and choose **Grown-up check**.
2. Under **Save test**, choose **Save test marker**.
3. Note the displayed `KLL-...` marker (a photo is sufficient).
4. Refresh the page and reopen Grown-up check. The marker should be found automatically; **Check saved marker** reads it again.
5. Close the browser, reopen the same page on the same device, and confirm that the same marker is found.
6. Optionally repeat after a Kindle restart. Record the model and firmware when reporting results.
7. Choose **Clear test marker**, then refresh to confirm that no marker is found.

The write-and-read result confirms only the current operation. It does not establish persistence after a browser close or device restart. The marker test has an owner-reported success; any untested close/restart scenarios remain pending.

## Implementation

- Store one string under `kindle-learning-lab.storage-test.v1`.
- Verify writes by reading back the same string; report silent write failures.
- Catch unavailable/blocked storage, getter exceptions, and write failures so the activities still work.
- Clear only this key, never call `localStorage.clear()`.
- Read on page startup and when the grown-up check opens; do not run background polling.
- Display stored strings as text, not HTML.
- Keep ES5 syntax and use no dedicated backend or cookie fallback in this test.

localStorage is associated with the site's origin. Use the same browser/device and URL scheme when testing. It does not automatically synchronize with an iPhone, and browser data clearing may remove the marker. See [MDN localStorage documentation](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

## Development verification

Run `node tests/storage-dom.cjs` with the optional jsdom and Acorn dependencies. It checks marker writes/readback, a new-document restoration simulation using retained storage, scoped deletion, absent/blocked/full storage, silent write failure, and continued activity interaction when storage fails. This simulation does not confirm a real browser's disk persistence or Kindle support.
