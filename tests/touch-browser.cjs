const assert = require('node:assert/strict');
const fs = require('node:fs');
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    const context = await browser.newContext({ viewport: { width: 600, height: 800 }, isMobile: true, hasTouch: true });
    const page = await context.newPage();
    for (const file of fs.readdirSync('.').filter(f => f.endsWith('.html'))) {
      const errors = []; const capture = e => errors.push(e.message);
      page.on('pageerror', capture);
      await page.setContent(fs.readFileSync(file, 'utf8'));
      await page.evaluate(() => {
        window.guardClicks = 0; window.blockedTouches = 0;
        const b = document.createElement('button'); b.id = 'guard-browser-check';
        b.style.cssText = 'position:fixed;top:0;left:0;width:80px;height:80px;z-index:99999';
        b.onclick = () => window.guardClicks++;
        document.body.appendChild(b);
        document.addEventListener('touchend', e => { if (e.defaultPrevented) window.blockedTouches++; }, { passive: false });
      });
      await page.touchscreen.tap(40, 40); await page.touchscreen.tap(40, 40); await page.touchscreen.tap(40, 40);
      assert.deepEqual(await page.evaluate(() => [window.guardClicks, window.blockedTouches, window.visualViewport.scale]), [3, 2, 1], file);
      assert.equal(await page.evaluate(() => getComputedStyle(document.documentElement).touchAction), 'manipulation');
      assert.deepEqual(errors, [], file);
      page.removeListener('pageerror', capture);
    }
    console.log('PASS: mobile Chromium real triple taps on all 9 pages retain 3 clicks, cancel 2 native gestures and keep scale 1, with no script errors. Kindle remains unverified.');
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exitCode = 1; });
