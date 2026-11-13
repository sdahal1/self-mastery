#!/usr/bin/env python3
"""Rebuild dist/ from the source files included in this folder. No dependencies."""
from pathlib import Path
import json
import shutil
import tempfile
from validate import validate

ROOT = Path(__file__).resolve().parents[1]

def build():
    destination = ROOT / 'dist'
    if destination.is_symlink():
        raise RuntimeError('Refusing to replace a symlink at dist/.')
    with tempfile.TemporaryDirectory(prefix='.build-', dir=ROOT) as temp:
        staging = Path(temp) / 'dist'
        shutil.copytree(ROOT / 'src', staging)
        shutil.copytree(ROOT / 'content/library', staging / 'data')
        shutil.copytree(ROOT / 'assets/readers', staging / 'readers')
        weeks = [w for p in sorted((ROOT / 'content').glob('weeks_*.json'))
                 for w in json.loads(p.read_text(encoding='utf-8'))]
        weeks.sort(key=lambda w: w['id'])
        (staging / 'data/weeks.json').write_text(json.dumps(weeks, ensure_ascii=False), encoding='utf-8')
        validate(staging, write_report=False)
        if destination.exists():
            shutil.rmtree(destination)
        shutil.move(str(staging), destination)
    return validate()

if __name__ == '__main__':
    print(json.dumps(build(), indent=2))
    print('Ready: publish the contents of dist/, or run python3 scripts/serve.py --open')
