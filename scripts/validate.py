#!/usr/bin/env python3
"""Validate the complete portable app using only Python's standard library."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def validate(dist=None, write_report=True):
    dist = Path(dist) if dist is not None else ROOT / 'dist'
    data = dist / 'data'
    index = read(data / 'index.json')
    weeks = read(data / 'weeks.json')
    assert [w['id'] for w in weeks] == [f'{i:02}' for i in range(27)], 'Expected Introduction and Weeks 1-26'
    assert index == read(ROOT / 'content/library/index.json')
    authored = sorted([w for p in sorted((ROOT / 'content').glob('weeks_*.json')) for w in read(p)], key=lambda w: w['id'])
    assert weeks == authored, 'Rebuild after editing the weekly guides'
    assert len(index) == 27
    source_count = segment_count = page_count = story_count = quiz_count = 0
    all_ids = []
    for w in weeks:
        m = next(m for m in index if m['id'] == w['id'])
        filename = f'sources-{w["id"]}.json'
        sources = read(data / filename)
        assert sources == read(ROOT / 'content/library' / filename), 'Source text changed during build'
        ids = {s['id'] for s in sources}
        assert len(ids) == m['sourceCount']
        all_ids += list(ids)
        assert (dist / m['pdf']).is_file()
        assert len(w['overview'].split()) >= 55, (w['id'], 'overview')
        assert len(w['concepts']) >= 4
        assert len(w['visual']['steps']) >= 3
        assert len(w['practice']['steps']) >= 3
        assert len(w['practice']['prompts']) >= 3
        assert len(w['reflection']) >= 3
        assert len(w['cheatsheet']['remember']) >= 4
        assert len(w['quiz']) >= 2
        assert set(w['sourceIds']) <= ids
        assert set(w['practice']['sourceIds']) <= ids
        for c in w['concepts']:
            assert set(c['sourceIds']) <= ids
        for s in w['stories']:
            assert s['sourceId'] in ids and s['locator'].strip()
        for q in w['quiz']:
            assert len(q['options']) >= 3 and q['answer'] in range(len(q['options'])) and q['explanation'].strip()
        for s in sources:
            assert s['pdfPage'] in range(1, m['pdfPages'] + 1)
            assert bool(s['pages']) != bool(s['segments'])
            if s['sourceUrl']:
                assert s['sourceUrl'].startswith(('https://', 'http://'))
            source_count += 1
            segment_count += len(s['segments'])
            page_count += len(s['pages'])
        story_count += len(w['stories'])
        quiz_count += len(w['quiz'])
    assert len(all_ids) == len(set(all_ids)) == 201
    assert segment_count == 29941 and page_count == 396
    for file in ['index.html', 'app.js', 'style.css', 'mark.svg']:
        assert (dist / file).read_bytes() == (ROOT / 'src' / file).read_bytes()
    pdfs = sorted((ROOT / 'assets/readers').glob('*.pdf'))
    assert len(pdfs) == 28, 'Expected 27 weekly PDFs and the combined reader'
    for pdf in pdfs:
        assert (dist / 'readers' / pdf.name).read_bytes() == pdf.read_bytes(), pdf.name
    assert (dist / 'readers/self-mastery-i-complete-course.pdf').is_file()
    result = {'status': 'passed', 'weekly_guides': 27, 'sources': source_count,
              'original_handout_pages': page_count, 'timestamped_segments': segment_count,
              'stories': story_count, 'quiz_questions': quiz_count, 'pdfs': len(pdfs),
              'source_and_asset_fidelity': 'passed'}
    if write_report:
        (ROOT / 'validation.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    return result

if __name__ == '__main__':
    print(json.dumps(validate(), indent=2))
