"""Embed a common zoom guard; shipped pages remain self-contained."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parent.parent

def protect_page(page):
    page = re.sub(r'(<meta name="viewport" content=")[^"]*(">)',
                  r'\g<1>width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no\2', page)
    page = re.sub(r'<style id="touch-guard-style">.*?</style>', '', page, flags=re.S)
    page = re.sub(r'<script id="touch-guard">.*?</script>', '', page, flags=re.S)
    page = page.replace('</head>', '<style id="touch-guard-style">html,body{touch-action:manipulation;-ms-touch-action:manipulation}</style></head>')
    script = (ROOT / 'tools/touch-guard.js').read_text()
    return page.replace('</body>', '<script id="touch-guard">' + script + '</script></body>')

if __name__ == '__main__':
    for path in sorted(ROOT.glob('*.html')):
        path.write_text(protect_page(path.read_text()))
