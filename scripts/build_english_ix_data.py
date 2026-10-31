#!/usr/bin/env python3
"""Builds public/data/class_ix_english.json for the SubjectZone app.

"My English IX" (Sindh Textbook Board, Jamshoro) — 8 units, each with six
sections: Reading Comprehension, Listening and Speaking, Language Practice,
Writing, Study Skills, and Fun.  Unit 8 additionally carries two extra reading
passages (8.7 The Healthy Living, 8.8 You are what you eat).

The PDF is image-only (no extractable text), so the solved items were written
from rendered page images (public/books/class_ix/english/pages/page_NNN.png).

Page mapping: image page_NNN.png = book page (NNN - 5); pdf page = NNN + 1.
The per-unit solution fragments were produced in scripts/english_ix_parts/ and
are merged here.
"""
import json
import os
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, 'scripts', 'english_ix_parts')
OUT = os.path.join(ROOT, 'public', 'data', 'class_ix_english.json')

SEC_LABEL = {
    1: 'Reading Comprehension',
    2: 'Listening and Speaking',
    3: 'Language Practice',
    4: 'Writing',
    5: 'Study Skills',
    6: 'Fun',
    7: 'The Healthy Living',
    8: 'You are what you eat',
}

# (unit_number, title, book_start, book_end)
UNITS = [
    (1, 'Ethics \u2013 Character Building',          1,   23),
    (2, 'Role Model',                                 24,  48),
    (3, 'Education and Careers',                      49,  74),
    (4, 'Pakistan and National Pride',                75,  101),
    (5, 'Healthy Life Style',                         108, 129),
    (6, 'Gender Equity',                              130, 156),
    (7, 'Life Skills',                                157, 176),
    (8, 'People and Places',                          177, 215),
]

TOTAL_PAGES = 228
OFFSET = 5  # book page = image number - 5


def normalize(item):
    """Rebuild section fields from sectionCode and compute page numbers."""
    sc = item['sectionCode']               # e.g. 'U11', 'U87'
    unit = int(sc[1])
    sdigit = int(sc[2])
    out = {
        'id': item['id'],
        'unit': unit,
        'section': f'Unit {unit} {SEC_LABEL[sdigit]}',
        'sectionCode': f'U{unit}{sdigit}',
        'type': item.get('type', 'activity'),
        'number': item.get('number', 0),
        'question': item.get('question', ''),
        'answer': item.get('answer', ''),
        'explanation': item.get('explanation', ''),
        'figure': item.get('figure', None),
    }
    img = item.get('image')
    if img is not None:
        out['pdfPage'] = img + 1
        out['bookPage'] = img - OFFSET
    else:
        out['pdfPage'] = item.get('pdfPage', 0)
        out['bookPage'] = item.get('bookPage', 0)
    if item.get('options'):
        out['options'] = item['options']
        out['optionsRaw'] = item.get('optionsRaw', '')
        out['correctAnswer'] = item.get('correctAnswer', '')
    return out


def load_items():
    all_items = []
    seen = set()
    for path in sorted(glob.glob(os.path.join(PARTS, 'unit_*.json'))):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        for raw in data:
            it = normalize(raw)
            if it['id'] in seen:
                raise SystemExit(f'Duplicate id: {it["id"]} (in {os.path.basename(path)})')
            seen.add(it['id'])
            all_items.append(it)
    return all_items


def build():
    all_items = load_items()

    chapters = []
    for unit_num, unit_title, bstart, bend in UNITS:
        unit_items = [q for q in all_items if q['unit'] == unit_num]
        # order by section code then question number
        unit_items.sort(key=lambda q: (q['sectionCode'], q['number']))
        chapters.append({
            'number': unit_num,
            'title': unit_title,
            'startPage': bstart + OFFSET + 1,   # pdf page of first book page
            'endPage': bend + OFFSET + 1,
            'bookStart': bstart,
            'bookEnd': bend,
            'totalQuestions': len(unit_items),
            'questions': unit_items,
        })

    pages_map = {f'page_{i:03d}': f'/books/class_ix/english/pages/page_{i - 1:03d}.png'
                 for i in range(1, TOTAL_PAGES + 1)}

    out = {
        'subject': 'Secondary Stage English',
        'grade': 'IX',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': TOTAL_PAGES,
        'totalChapters': len(UNITS),
        'totalQuestionsSolved': len(all_items),
        'chapters': chapters,
        'pages': pages_map,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f'Built {OUT}: {len(all_items)} solved items across {len(UNITS)} units.')
    for c in chapters:
        print(f"  Unit {c['number']} {c['title']}: {c['totalQuestions']} items "
              f"(book {c['bookStart']}-{c['bookEnd']})")


if __name__ == '__main__':
    build()
