#!/usr/bin/env python3
"""Builds public/data/class_ix_islamiyat.json for the SubjectZone app.

Islamiyat (Compulsory) for Class IX-X (Sindh Textbook Board, Jamshoro).
The pdf "Islamiyat IX-X.pdf" is image-only (no extractable text), so the solved
items were written from rendered page images in
public/books/class_ix/islamiyat/pages/page_NNN.png (176 pages).

Page mapping: image page_NNN.png = book page (NNN - 3); pdfPage = NNN + 1.
Book page 1 = image page_004.png.

The book has 4 chapters containing 23 lessons. Each lesson ends with an
Exercise of up to three parts:
  (A) detailed answers  -> section "Descriptive Questions" (type 'descriptive')
  (B) brief answers     -> section "Short Questions"        (type 'sq')
  (C) multiple choice   -> section "MCQs"                   (type 'mcq')

Per-lesson solution fragments live in scripts/islamiyat_ix_parts/ and are merged
here.  Each fragment item carries: id, unit, letter, type, number, question,
answer, explanation, image, figure (+ options/optionsRaw/correctAnswer for MCQ).
"""
import json
import os
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, 'scripts', 'islamiyat_ix_parts')
OUT = os.path.join(ROOT, 'public', 'data', 'class_ix_islamiyat.json')

OFFSET = 3  # book page = image number - 3 ; pdfPage = image + 1

SEC_LABEL = {
    'A': 'Descriptive Questions',
    'B': 'Short Questions',
    'C': 'MCQs',
}

# (unit_number, title, book_start, book_end) — lessons in book order
UNITS = [
    (1,  'Introduction and Significances',                                             1,   7),
    (2,  'The Translation and Explanation of the Selected Verses',                     8,   35),
    (3,  'Introduction to Hadith and Sunnah and Their Effects on Practical Life',      36,  41),
    (4,  'Translation and Explanation of Selected Ahadith',                            42,  64),
    (5,  'Belief in Oneness of Allah (Attributes of Allah and the Requisite of Tawheed)', 65, 70),
    (6,  'Belief in Prophethood',                                                      71,  78),
    (7,  'The Importance and Significance of Worship',                                 79,  81),
    (8,  'Jihad (Introduction, Importance and Types)',                                 82,  89),
    (9,  'Commencement of Prophethood',                                                90,  94),
    (10, 'Invitation and Preaching',                                                   95,  100),
    (11, 'Migration to Medina and Ghaz\'wat (Battles)',                                101, 109),
    (12, 'Qualities and Characteristics of The Holy Prophet (S.A.W)',                  110, 115),
    (13, 'Qualities of the Purified Family',                                           116, 125),
    (14, 'Greatness of Companions and The Ten Blessed',                                126, 132),
    (15, 'Importance and Excellence of Knowledge',                                     133, 135),
    (16, 'Significance of Family in Islam',                                            136, 140),
    (17, 'Dignity of Humanity',                                                        141, 143),
    (18, 'Collective Justice',                                                         144, 147),
    (19, 'Modesty',                                                                    148, 152),
    (20, 'Hazrat Imam Hussain (R.A.)',                                                 153, 159),
    (21, 'Hazrat Abu Ubaidah Bin Jarrah (R.A.)',                                       160, 164),
    (22, 'Jabir Bin Hayyan',                                                           165, 167),
    (23, 'Hazrat Muhammad Rashid Raudhe Dhanni',                                       168, 172),
]

TOTAL_PAGES = 172

TYPE_FOR_LETTER = {'A': 'descriptive', 'B': 'sq', 'C': 'mcq'}


def normalize(item):
    unit = int(item['unit'])
    letter = item['letter']
    qtype = item.get('type') or TYPE_FOR_LETTER[letter]
    out = {
        'id': item.get('id') or f'u{unit}_{letter}_q{item["number"]}',
        'unit': unit,
        'section': SEC_LABEL[letter],
        'sectionCode': f'U{unit}{letter}',
        'type': qtype,
        'number': item['number'],
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
    if qtype == 'mcq':
        out['options'] = item.get('options', [])
        out['optionsRaw'] = item.get('optionsRaw', '')
        out['correctAnswer'] = item.get('correctAnswer', '')
    return out


def load_items():
    items = []
    seen = set()
    for path in sorted(glob.glob(os.path.join(PARTS, 'part_*.json'))):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        for raw in data:
            it = normalize(raw)
            if it['id'] in seen:
                raise SystemExit(f'Duplicate id: {it["id"]}')
            seen.add(it['id'])
            items.append(it)
    return items


def build():
    all_items = load_items()

    chapters = []
    for unit_num, unit_title, bstart, bend in UNITS:
        unit_items = [q for q in all_items if q['unit'] == unit_num]
        # order A -> B -> C then question number
        order = {'A': 0, 'B': 1, 'C': 2}
        unit_items.sort(key=lambda q: (order.get(q['sectionCode'][-1], 9), q['number']))
        chapters.append({
            'number': unit_num,
            'title': unit_title,
            'startPage': bstart + OFFSET + 1,   # pdf page (1-indexed)
            'endPage': bend + OFFSET + 1,
            'bookStart': bstart,
            'bookEnd': bend,
            'totalQuestions': len(unit_items),
            'questions': unit_items,
        })

    pages_map = {f'page_{p:03d}': f'/books/class_ix/islamiyat/pages/page_{p + OFFSET:03d}.png'
                 for p in range(1, TOTAL_PAGES + 1)}

    out = {
        'subject': 'Islamiyat (Compulsory)',
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

    print(f'Built {OUT}: {len(all_items)} solved items across {len(UNITS)} lessons.')
    for c in chapters:
        print(f"  Unit {c['number']} {c['title']}: {c['totalQuestions']} items "
              f"(book {c['bookStart']}-{c['bookEnd']})")


if __name__ == '__main__':
    build()
