import json
from pathlib import Path
lessons=json.loads(Path('dist/lessons.json').read_text())
assert len(lessons)==56
categories=set()
for l in lessons:
    categories.add(l['category'])
    assert l['title'] and l['lesson'] and l['problem']
    assert 0<=l['answer']<len(l['options'])
    compile(l['code'],l['title'],'exec')
assert len(categories)==8
assert 'fonts.googleapis.com' not in Path('dist/style.css').read_text()
print('56 learning units, 8 paths, valid quiz answers and Python syntax; no remote font dependency.')
