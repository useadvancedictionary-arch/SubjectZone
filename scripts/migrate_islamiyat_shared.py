#!/usr/bin/env python3
"""Wrap the shared Islamiyat XI-XII solutions into the chapter structure the app expects.

The legacy build_islamiyat_xii_data.py writes a flat JSON array, but the app
reads `data.chapters[].questions`. This script converts the existing solved
list into the same object format used by the other Class XI/XII subjects and
writes it to both class_xi_islamiyat.json and class_xii_islamiyat.json,
because both grades study the same 190-page book.

Duplicate printed IDs are disambiguated with the page number; no item is lost.
"""
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'public', 'data', 'class_xii_islamiyat.json')
OUTS = [
    os.path.join(ROOT, 'public', 'data', 'class_xi_islamiyat.json'),
    os.path.join(ROOT, 'public', 'data', 'class_xii_islamiyat.json'),
]

TOTAL_PAGES = 190
OFFSET = 3  # book page = pdf page - 3

CHAPTERS = [
    (1, 'The Holy Quran', 4, 76),
    (2, 'Hadith \u2014 Translation & Meaning', 77, 115),
    (3, 'Hadith \u2014 Compilation & Preservation', 116, 145),
    (4, 'Faith & Worship', 146, 168),
    (5, 'Ethics & Islamic Values', 169, 189),
]


def main():
    with open(SRC, encoding='utf-8') as f:
        items = json.load(f)
    if not isinstance(items, list):
        raise SystemExit('Expected the legacy flat list')

    seen = Counter()
    fixed = []
    for raw in items:
        item = dict(raw)
        item_id = item['id']
        seen[item_id] += 1
        if seen[item_id] > 1:
            item['id'] = f'{item_id}_p{item["pdfPage"]}'
        fixed.append(item)

    ids = [i['id'] for i in fixed]
    assert len(ids) == len(set(ids)), 'duplicate ids remain'

    chapters = []
    for number, title, start, end in CHAPTERS:
        qs = [q for q in fixed if q['chapter'] == number]
        chapters.append({
            'number': number,
            'title': title,
            'startPage': start,
            'endPage': end,
            'bookStart': start - OFFSET,
            'bookEnd': end - OFFSET,
            'totalQuestions': len(qs),
            'questions': qs,
        })

    pages = {
        f'page_{i:03d}': f'/books/class_xii/islamiyat/pages/page_{i:03d}.webp'
        for i in range(1, TOTAL_PAGES + 1)
    }

    out = {
        'subject': 'Islamiyat',
        'grade': 'Class XI-XII',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': TOTAL_PAGES,
        'totalChapters': len(chapters),
        'totalQuestionsSolved': len(fixed),
        'chapters': chapters,
        'pages': pages,
    }

    for path in OUTS:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print(f'Wrote {path}')

    print(f'{len(fixed)} items, {len(chapters)} chapters '
          f'({[c["totalQuestions"] for c in chapters]})')


if __name__ == '__main__':
    main()
