#!/usr/bin/env python3
"""Builds public/data/class_xi_physics.json from per-unit fragments.

Physics XI (Sindh Textbook Board): 14 units. Each unit ends with an exercise:
Section (A) Multiple Choice Questions, then Section (B) Structured Questions
containing CRQs, ERQs and (for most units) Numerical questions.
Printed page = PDF page - 4 (printed p.1 = PDF p.5).
Fragments live in scripts/physics_xi_parts/uN.json.
"""
import json
import re
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PART_DIR = os.path.join(ROOT, 'scripts', 'physics_xi_parts')
OUT = os.path.join(ROOT, 'public', 'data', 'class_xi_physics.json')
OFFSET = 4

# (number, title, book start, book end, pdf start, pdf end)
UNITS = [
    (1, 'Physics and Measurements', 1, 29, 5, 33),
    (2, 'Kinematics', 30, 56, 34, 60),
    (3, 'Dynamics', 57, 72, 61, 76),
    (4, 'Rotational and Circular Motion', 73, 97, 77, 101),
    (5, 'Work, Energy and Power', 98, 121, 102, 125),
    (6, 'Fluid Statics', 122, 140, 126, 144),
    (7, 'Fluid Dynamics', 141, 160, 145, 164),
    (8, 'Electric Fields', 161, 182, 165, 186),
    (9, 'Capacitors', 183, 196, 187, 200),
    (10, 'D.C Circuits', 197, 223, 201, 227),
    (11, 'Oscillations', 224, 247, 228, 251),
    (12, 'Acoustics', 248, 274, 252, 278),
    (13, 'Physical Optics', 275, 304, 279, 308),
    (14, 'Communication', 305, 321, 309, 325),
]

SEC = {
    'A': ('Exercise {n} (A) MCQs', 'mcq'),
    'B': ('Exercise {n} (B) CRQs', 'sq'),
    'C': ('Exercise {n} (C) ERQs', 'erq'),
    'D': ('Exercise {n} (D) Numericals', 'numerical'),
}


def normalize(it, n):
    letter = it['section']
    label, qtype = SEC[letter]
    qtype = it.get('type', qtype)
    number = int(it['number'])
    qid = it.get('id') or f'u{n}_ex{letter}_q{number}'
    pdf_page = int(it['pdfPage'])
    book_page = int(it.get('bookPage', pdf_page - OFFSET))
    d = {
        'id': qid,
        'chapter': n,
        'section': label.format(n=n),
        'sectionCode': f'EX{n}{letter}',
        'type': qtype,
        'number': number,
        'question': it['question'],
        'answer': it.get('answer', ''),
        'explanation': it.get('explanation', ''),
        'pdfPage': pdf_page,
        'bookPage': book_page,
        'figure': it.get('figure'),
    }
    if qtype == 'mcq':
        opts = it['options']
        if isinstance(opts[0], dict):
            d['options'] = [{'key': o['key'], 'text': o['text']} for o in opts]
        else:
            d['options'] = [{'key': chr(97 + i), 'text': t} for i, t in enumerate(opts)]
        # Some fragments kept the printed letter label inside the option text;
        # strip it only when it matches that option's own key (so text such as
        # "(a) and (b)" in option (d) is preserved).
        for o in d['options']:
            m = re.match(r'^\s*\(?([a-eA-E])[\).]\s+(.*)$', o['text'])
            if m and m.group(1).lower() == o['key']:
                o['text'] = m.group(2).strip()
        assert 4 <= len(d['options']) <= 5, f'{qid}: expected 4-5 options'
        key = it['correct']
        assert key in 'abcde' and len(key) == 1, f'{qid}: bad key {key}'
        text = next(o['text'] for o in d['options'] if o['key'] == key)
        d['optionsRaw'] = '  '.join(f"({o['key']}) {o['text']}" for o in d['options'])
        d['correctAnswer'] = f'({key}) {text}'
        if not d['answer']:
            d['answer'] = d['correctAnswer']
    return d


def main():
    chapters = []
    total = 0
    ids = set()
    for n, title, start, end, pdf_start, pdf_end in UNITS:
        path = os.path.join(PART_DIR, f'u{n}.json')
        if not os.path.exists(path):
            print(f'Unit {n:2d} {title}: NO FRAGMENT YET (skipped)')
            continue
        raw = json.load(open(path, encoding='utf-8'))
        qs = [normalize(it, n) for it in raw]
        for q in qs:
            assert q['id'] not in ids, f'duplicate id {q["id"]}'
            ids.add(q['id'])
            assert q['question'].strip() and q['answer'].strip(), f'{q["id"]}: empty q/a'
            assert start <= q['bookPage'] <= end, (
                f'{q["id"]}: bookPage {q["bookPage"]} outside unit {n} range {start}-{end}'
            )
            assert pdf_start <= q['pdfPage'] <= pdf_end, (
                f'{q["id"]}: pdfPage {q["pdfPage"]} outside unit {n} range {pdf_start}-{pdf_end}'
            )
        order = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
        qs.sort(key=lambda q: (order[q['sectionCode'][-1]], q['number']))
        chapters.append({
            'number': n,
            'title': title,
            'startPage': pdf_start,
            'endPage': pdf_end,
            'bookStart': start,
            'bookEnd': end,
            'totalQuestions': len(qs),
            'questions': qs,
        })
        total += len(qs)
        print(f'Unit {n:2d} {title}: {len(qs)} items')

    data = {
        'subjectId': 'physics_xi',
        'subjectName': 'Physics',
        'gradeId': 'class_xi',
        'gradeName': 'Class XI (HSC Part I)',
        'subject': 'Physics',
        'grade': 'XI',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': 325,
        'totalChapters': len(chapters),
        'totalQuestionsSolved': total,
        'chapters': chapters,
        'pagesMap': {},
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'TOTAL {total} items -> {OUT}')


if __name__ == '__main__':
    main()
