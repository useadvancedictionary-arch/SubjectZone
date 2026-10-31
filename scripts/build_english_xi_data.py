#!/usr/bin/env python3
"""Build public/data/class_xi_english.json for the SubjectZone app.

English XI (Sindh Textbook Board, Jamshoro) — 262 PDF pages.
Structure:
  * Units 1-10, each with four sections:
      1 Reading Comprehension, 2 Writing, 3 Oral Communication, 4 Grammar
  * Section B: Poetry — Elements of Poetry + 7 poems
  * Section C: Play — A Visit to a Small Planet, exercises after Scene III
    (biographies are reading material with no exercise)

The PDF text layer only carries running heads, so the solved items were written
from the rendered pages in public/books/class_xi/english/pages/.
Book page = PDF page - 7 (book 1 = PDF 8).

Solution fragments live in scripts/english_xi_parts/*.json and are merged here.
Each fragment is a JSON array of items with these keys:
  id, sectionCode, type ('sq'|'mcq'), number, question, answer, explanation,
  bookPage, options (MCQ only), optionsRaw (MCQ only), correctAnswer (MCQ only)
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, 'scripts', 'english_xi_parts')
OUT = os.path.join(ROOT, 'public', 'data', 'class_xi_english.json')

OFFSET = 7
TOTAL_PAGES = 262

UNIT_TITLES = {
    1: 'Democratic Citizenship',
    2: 'Preservation of Nature',
    3: 'Managing Change',
    4: 'Technology Smart & Tech-Savvy',
    5: 'Civic Sense and Civic Activities',
    6: 'Respecting Self & Others',
    7: 'Self-Grooming',
    8: 'Places of Historical / Cultural Importance',
    9: 'Choosing Career',
    10: 'Practicing Positive Work Ethics',
}
UNIT_RANGES = {
    1: (1, 16),
    2: (17, 34),
    3: (35, 53),
    4: (54, 71),
    5: (72, 89),
    6: (90, 106),
    7: (107, 121),
    8: (122, 141),
    9: (142, 160),
    10: (161, 176),
}
POEM_TITLES = {
    0: 'Elements of Poetry',
    1: 'Poem 1 \u2014 The Character of a Happy Life',
    2: "Poem 2 \u2014 Don't Quit",
    3: 'Poem 3 \u2014 Ozymandias',
    4: 'Poem 4 \u2014 Good Timber',
    5: 'Poem 5 \u2014 Lucy Gray',
    6: 'Poem 6 \u2014 The Abbot of Canterbury',
    7: 'Poem 7 \u2014 Surr Khahori',
}
POETRY_RANGE = (177, 223)
PLAY_RANGE = (224, 255)

SECTION_NAMES = {
    1: 'Reading Comprehension',
    2: 'Writing',
    3: 'Oral Communication',
    4: 'Grammar',
}

# Part files are read in this order; items keep their printed order inside.
PART_ORDER = (
    [f'unit_{n:02d}.json' for n in range(1, 3)]
    + ['unit_02_ext.json']
    + [f'unit_{n:02d}.json' for n in range(3, 11)]
    + ['poetry_a.json', 'poetry_b.json', 'play.json']
)


def chapter_of(code):
    if code.startswith('U'):
        return int(re.match(r'U(\d+)S', code).group(1))
    if code.startswith('P'):
        return 11
    if code.startswith('C'):
        return 12
    raise ValueError(f'Unknown section code: {code}')


def section_label(code):
    m = re.match(r'U(\d+)S(\d)$', code)
    if m:
        unit, sec = int(m.group(1)), int(m.group(2))
        return f'Unit {unit}.{sec} \u2014 {SECTION_NAMES[sec]}'
    m = re.match(r'P(\d+)S1$', code)
    if m:
        return POEM_TITLES[int(m.group(1))]
    if code == 'C1S1':
        return 'Play \u2014 Exercises 1\u201311'
    raise ValueError(f'Unknown section code: {code}')


def normalize(raw):
    code = raw['sectionCode']
    book_page = int(raw['bookPage'])
    item = {
        'id': raw['id'],
        'chapter': chapter_of(code),
        'section': section_label(code),
        'sectionCode': code,
        'type': raw.get('type', 'sq'),
        'number': str(raw.get('number', '')),
        'question': raw.get('question', '').strip(),
        'answer': raw.get('answer', '').strip(),
        'explanation': raw.get('explanation', '').strip(),
        'pdfPage': book_page + OFFSET,
        'bookPage': book_page,
        'options': None,
        'optionsRaw': None,
        'correctAnswer': None,
    }
    if item['type'] == 'mcq':
        opts = raw.get('options') or []
        item['options'] = [{'key': o['key'], 'text': o['text']} for o in opts]
        item['optionsRaw'] = raw.get('optionsRaw') or '   '.join(
            f"({o['key']}) {o['text']}" for o in opts)
        item['correctAnswer'] = raw.get('correctAnswer', '')
    return item


def load_items():
    items = []
    seen = set()
    for name in PART_ORDER:
        path = os.path.join(PARTS, name)
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise SystemExit(f'{name}: expected a JSON array')
        for raw in data:
            item = normalize(raw)
            if item['id'] in seen:
                raise SystemExit(f'Duplicate id: {item["id"]} (in {name})')
            seen.add(item['id'])
            items.append(item)
    return items


def build():
    items = load_items()
    if not items:
        raise SystemExit('No part files found')

    chapters = []
    for n in range(1, 11):
        start, end = UNIT_RANGES[n]
        qs = [q for q in items if q['chapter'] == n]
        chapters.append({
            'number': n,
            'title': UNIT_TITLES[n],
            'startPage': start + OFFSET,
            'endPage': end + OFFSET,
            'bookStart': start,
            'bookEnd': end,
            'totalQuestions': len(qs),
            'questions': qs,
        })

    poetry_items = [q for q in items if q['chapter'] == 11]
    chapters.append({
        'number': 11,
        'title': 'Section B: Poetry',
        'startPage': POETRY_RANGE[0] + OFFSET,
        'endPage': POETRY_RANGE[1] + OFFSET,
        'bookStart': POETRY_RANGE[0],
        'bookEnd': POETRY_RANGE[1],
        'totalQuestions': len(poetry_items),
        'questions': poetry_items,
    })

    play_items = [q for q in items if q['chapter'] == 12]
    chapters.append({
        'number': 12,
        'title': 'Section C: Play \u2014 A Visit to a Small Planet',
        'startPage': PLAY_RANGE[0] + OFFSET,
        'endPage': PLAY_RANGE[1] + OFFSET,
        'bookStart': PLAY_RANGE[0],
        'bookEnd': PLAY_RANGE[1],
        'totalQuestions': len(play_items),
        'questions': play_items,
    })

    pages_map = {
        f'page_{i:03d}': f'/books/class_xi/english/pages/page_{i:03d}.png'
        for i in range(1, TOTAL_PAGES + 1)
    }

    out = {
        'subject': 'English',
        'grade': 'Class XI',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': TOTAL_PAGES,
        'totalChapters': len(chapters),
        'totalQuestionsSolved': len(items),
        'chapters': chapters,
        'pages': pages_map,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f'Built {OUT}: {len(items)} solved items, {len(chapters)} chapters.')
    for c in chapters:
        print(f"  Ch {c['number']} {c['title']}: {c['totalQuestions']} items "
              f"(book {c['bookStart']}-{c['bookEnd']})")


if __name__ == '__main__':
    build()
