#!/usr/bin/env python3
"""Maintain existing public preview URLs alongside the product homepage."""
from pathlib import Path
import shutil

root=Path(__file__).resolve().parent
out=root/'docs'
preview=out/'preview'
for file in ['index.html','en/index.html','privacy/index.html','support/index.html','en/privacy/index.html','en/support/index.html','carplay/index.html','en/carplay/index.html']:
    html=(out/file).read_text()
    html=html.replace('href="/memory-music-support/','href="/memory-music-support/preview/').replace('src="/memory-music-support/','src="/memory-music-support/preview/')
    html=html.replace('<head>','<head><meta name="robots" content="noindex,nofollow">',1)
    dest=preview/file
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(html)
for file in ['style.css','product.css','product.js','carplay.css','icon.png']:
    shutil.copyfile(out/file,preview/file)
shutil.copytree(out/'assets',preview/'assets',dirs_exist_ok=True)
print('Built bilingual /preview/ pages with matching local assets.')
