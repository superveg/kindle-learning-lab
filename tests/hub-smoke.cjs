/* Development-only checks. Requires Node.js and Playwright. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const { chromium } = require('playwright');

(async () => {
  const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'));
  const server = http.createServer((req, res) => {
    if (req.url !== '/kindle-learning-lab/' && req.url !== '/kindle-learning-lab/index.html') {
      res.writeHead(404); res.end(); return;
    }
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }); res.end(html);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  let browser;
  try {
    browser = await chromium.launch({ headless: true });
    const url = 'http://127.0.0.1:' + server.address().port + '/kindle-learning-lab/';
    const context = await browser.newContext({ viewport: { width: 600, height: 800 } });
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(url);
    assert.equal(await page.locator('.screen:visible').count(), 1);
    for (const viewport of [{ width: 360, height: 740 }, { width: 600, height: 800 }, { width: 800, height: 600 }]) {
      await page.setViewportSize(viewport);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), true);
      for (const tile of await page.locator('.tile').all()) { assert.ok((await tile.boundingBox()).height >= 68); }
    }
    await page.setViewportSize({ width: 600, height: 800 });
    await page.screenshot({ path: path.join(require('node:os').tmpdir(), 'kindle-hub-home.png'), fullPage: true });
    await context.setOffline(true);
    await page.locator('#open-count').click();
    assert.equal(await page.locator('#count-next').isDisabled(), true);
    await page.locator('#count-answers button').filter({ hasText: /^1$/ }).click();
    assert.equal(await page.locator('#count-next').isDisabled(), true);
    await page.locator('#count-answers button').filter({ hasText: /^2$/ }).click();
    await page.locator('#count-answers button').filter({ hasText: /^2$/ }).click();
    await page.locator('#count-next').click();
    await page.locator('#count-answers button').filter({ hasText: /^3$/ }).click();
    await page.locator('#count-next').click();
    await page.locator('#count-answers button').filter({ hasText: /^1$/ }).click();
    await page.locator('#count-next').click();
    assert.match(await page.locator('#count-feedback').innerText(), /First-try answers: 2 of 3/);
    assert.equal(await page.locator('#count-next').isVisible(), false);
    await page.locator('#count-home').click();
    await page.locator('#open-count').click();
    assert.equal(await page.locator('#count-progress').innerText(), 'Question 1 of 3');
    await page.locator('#count-home').click();
    await page.locator('#open-shapes').click();
    await page.locator('#shape-square').click();
    assert.match(await page.locator('#shapes-feedback').innerText(), /Look for/);
    await page.locator('#shape-circle').click();
    assert.equal(await page.locator('#shape-square').isDisabled(), true);
    await page.locator('#shapes-home').click();
    await page.locator('#open-letters').click();
    await page.locator('#letter-b').click();
    await page.locator('#letter-a').click();
    assert.match(await page.locator('#letters-feedback').innerText(), /All done/);
    await page.locator('#letters-home').click();
    for (const branch of ['garden', 'pond']) {
      await page.locator('#open-story').click();
      await page.locator('#story-' + branch).click();
      assert.match(await page.locator('#story-feedback').innerText(), /The end/);
      assert.equal(await page.locator('#story-garden').isDisabled(), true);
      await page.locator('#story-home').click();
    }
    await page.locator('#open-check').click();
    assert.equal(await page.locator('#script-status').innerText(), 'JavaScript is working.');
    await page.locator('#text-size').click();
    assert.equal(await page.locator('body').getAttribute('class'), 'large');
    for (const id of ['tap-one', 'tap-two', 'tap-three']) { await page.locator('#' + id).click(); }
    assert.match(await page.locator('#tap-status').innerText(), /Touch check complete/);
    await page.locator('#check-home').click();
    for (const screen of ['home', 'count', 'shapes', 'letters', 'story', 'check']) {
      if (screen !== 'home') { await page.locator('#open-' + screen).click(); }
      await page.setViewportSize({ width: 360, height: 740 });
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), true, screen);
      if (screen !== 'home') { await page.locator('#' + screen + '-home').click(); }
    }
    assert.deepEqual(errors, []);
    const fallback = await browser.newContext({ javaScriptEnabled: false });
    const staticPage = await fallback.newPage();
    await staticPage.goto(url);
    assert.equal(await staticPage.locator('.screen:visible').count(), await staticPage.locator('.screen').count());
    assert.match(await staticPage.locator('noscript').innerText(), /JavaScript is unavailable/);
    assert.equal(await staticPage.locator('#shape-circle').isDisabled(), true);
    console.log('PASS: layout, navigation, scoring, completion, offline interaction, text size, tap checks, no-JavaScript fallback.');
  } finally {
    if (browser) { await browser.close(); }
    await new Promise(resolve => server.close(resolve));
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
