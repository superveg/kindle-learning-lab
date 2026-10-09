# Kindle Learning Lab

A small, static learning Hub for children aged 3–4, designed for testing on Kindle E Ink readers.

## Try the Hub

Open `index.html` in a browser. No build step, server, account, or runtime dependency is required.

The entry page offers four bounded samples:

- Count: three questions with feedback, first-try scoring, and a completion state.
- Shapes: identify a circle.
- Letters: match the letter A.
- Little story: choose one of two short endings; read together with an adult.

The grown-up screen check includes a larger-text option, three touch targets, and instructions for testing a brief disconnection.

All styles, script, and activity content are embedded in one HTML file. No content is fetched during interaction. Session progress resets on reload. Offline reload/reopening is not implemented or promised.

## Publish on GitHub Pages

After merging the Hub PR:

1. Open repository **Settings → Pages**.
2. Set **Source** to **Deploy from a branch**.
3. Select **main** and **/(root)**, then save.
4. Wait for deployment to finish and use the site link shown in Pages settings.

Expected URL after successful deployment: https://superveg.github.io/kindle-learning-lab/

This is an expected URL, not confirmation of a live deployment. `.nojekyll` allows the static files to be served without a Jekyll build. See [GitHub's publishing-source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Development checks

The page itself has no dependencies. Optional development checks use Node.js, jsdom, Acorn, and Playwright:

```sh
npm install --no-save --package-lock=false jsdom acorn playwright
node tests/hub-dom.cjs
npx playwright install chromium
node tests/hub-smoke.cjs
```

The DOM check validates ES5 syntax and interaction logic without a browser. The browser smoke check serves the page under the repository path and covers layout, navigation, scoring, finite completion, offline interaction, text size, touch-check state, and the no-JavaScript fallback.

## Device status

The exact Kindle model and firmware are unknown. Desktop browser results do not establish Kindle compatibility. Follow the [Kindle test checklist](docs/KINDLE_TEST.md) on the actual device.

## Documentation

- [Project requirements](docs/PROJECT.md)
- [Agent instructions](AGENTS.md)
- [Development task template](docs/TASK_TEMPLATE.md)
- [Hub design decisions](docs/HUB_DESIGN.md)
- [Kindle test checklist](docs/KINDLE_TEST.md)
