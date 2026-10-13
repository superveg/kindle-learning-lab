"""Embed reviewed diagram and high-level math sources into the standalone math page."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parent.parent
p=ROOT/'math.html';s=p.read_text()
source=(ROOT/'learning/pictures.js').read_text()+'\n'+(ROOT/'learning/higher-math.js').read_text()
block='/* BEGIN EXTENDED SOURCES */\n'+source+'/* END EXTENDED SOURCES */\n'
if '/* BEGIN EXTENDED SOURCES */' in s:
 s=re.sub(r'/\* BEGIN EXTENDED SOURCES \*/.*?/\* END EXTENDED SOURCES \*/\n',lambda _:block,s,flags=re.S)
else:s=s.replace('<script>','<script>\n'+block,1)
styles=(ROOT/'learning/higher-math.css').read_text()
if '/* BEGIN MATH MODEL STYLES */' in s:
 s=re.sub(r'/\* BEGIN MATH MODEL STYLES \*/.*?/\* END MATH MODEL STYLES \*/\n',lambda _:styles,s,flags=re.S)
else:s=s.replace('</style>',styles+'</style>',1)
p.write_text(s)
