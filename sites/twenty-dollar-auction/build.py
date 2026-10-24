#!/usr/bin/env python3
"""Bundle src/ into two single-file builds:
   index.html     - a normal web page (double-click it, or put it on any static host)
   artifact.html  - the same page without the document skeleton, for publishing as a Claude artifact
Run: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / 'src'
SCRIPTS = ['core.js', 'modes-dream.js', 'modes-food.js', 'modes-action.js', 'art.js', 'ai-sound.js', 'ui.js']

shell = (SRC / 'shell.html').read_text(encoding='utf-8')
css = (SRC / 'styles.css').read_text(encoding='utf-8')
js = '\n'.join((SRC / 'js' / name).read_text(encoding='utf-8') for name in SCRIPTS)
body = shell.replace('/*STYLES*/', css).replace('/*SCRIPTS*/', js.replace('</script', '<\\/script'))

(ROOT / 'artifact.html').write_text(body, encoding='utf-8')
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
(ROOT / 'index.html').write_text(page, encoding='utf-8')
print('built index.html and artifact.html', len(page) // 1024, 'KB')
