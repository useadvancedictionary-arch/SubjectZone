#!/usr/bin/env python3
"""Builds public/data/class_xi_chemistry.json from per-chapter fragments.

Chemistry XI (Sindh Textbook Board): 12 chapters. Each exercise has:
Multiple Choice Questions (10), Short Questions, Descriptive Questions and,
for most chapters, Numerical Questions.
Printed page = PDF page - 6 (chapter 1 printed p.1 = PDF p.7).
Fragments live in scripts/chemistry_xi_parts/cN.json.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PART_DIR = os.path.join(ROOT, 'scripts', 'chemistry_xi_parts')
OUT = os.path.join(ROOT, 'public', 'data', 'class_xi_chemistry.json')
OFFSET = 6

# (number, title, book start, book end)
UNITS = [
    (1, 'Stoichiometry', 1, 21),
    (2, 'Atomic Structure', 22, 49),
    (3, 'Theories of Covalent Bonding and Shapes of Molecules', 50, 74),
    (4, 'State of Matter I: Gas', 75, 103),
    (5, 'State of Matter II: Liquids', 104, 120),
    (6, 'State of Matter III: Solids', 121, 139),
    (7, 'Chemical Equilibrium', 140, 163),
    (8, 'Acids, Bases and Salts', 164, 180),
    (9, 'Chemical Kinetics', 181, 197),
    (10, 'Solution & Colloids', 198, 217),
    (11, 'Thermochemistry', 218, 238),
    (12, 'Electrochemistry', 239, 259),
]

SEC = {
    'A': ('Exercise {n} MCQs', 'mcq'),
    'B': ('Exercise {n} Short Questions', 'sq'),
    'C': ('Exercise {n} Descriptive Questions', 'erq'),
    'D': ('Exercise {n} Numerical Questions', 'numerical'),
}


def normalize(it, n):
    letter = it['section']
    label, qtype = SEC[letter]
    qtype = it.get('type', qtype)
    number = int(it['number'])
    qid = it.get('id') or f'c{n}_ex{letter}_q{number}'
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
        assert 4 <= len(d['options']) <= 5, f'{qid}: expected 4-5 options'
        key = it['correct']
        assert key in 'abcd' and len(key) == 1, f'{qid}: bad key {key}'
        text = next(o['text'] for o in d['options'] if o['key'] == key)
        d['optionsRaw'] = '  '.join(f"({o['key']}) {o['text']}" for o in d['options'])
        d['correctAnswer'] = f'({key}) {text}'
        if not d['answer']:
            d['answer'] = d['correctAnswer']
    return d


def main():
    title_by_no = {n: t for n, t, _s, _e in UNITS}
    chapters = []
    total = 0
    ids = set()
    for n, title, start, end in UNITS:
        path = os.path.join(PART_DIR, f'c{n}.json')
        if not os.path.exists(path):
            print(f'Chapter {n:2d} {title}: NO FRAGMENT YET (skipped)')
            continue
        raw = json.load(open(path, encoding='utf-8'))
        qs = [normalize(it, n) for it in raw]
        for q in qs:
            assert q['id'] not in ids, f'duplicate id {q["id"]}'
            ids.add(q['id'])
            assert q['question'].strip() and q['answer'].strip(), f'{q["id"]}: empty q/a'
            assert start <= q['bookPage'] <= end, (
                f'{q["id"]}: bookPage {q["bookPage"]} outside chapter {n} range {start}-{end}'
            )
            assert 1 <= q['pdfPage'] <= 275, f'{q["id"]}: bad pdfPage {q["pdfPage"]}'
        order = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
        qs.sort(key=lambda q: (order[q['sectionCode'][-1]], q['number']))
        chapters.append({
            'number': n,
            'title': title,
            'startPage': start + OFFSET,
            'endPage': end + OFFSET,
            'bookStart': start,
            'bookEnd': end,
            'totalQuestions': len(qs),
            'questions': qs,
        })
        total += len(qs)
        print(f'Chapter {n:2d} {title}: {len(qs)} items')

    data = {
        'subjectId': 'chemistry_xi',
        'subjectName': 'Chemistry',
        'gradeId': 'class_xi',
        'gradeName': 'Class XI (HSC Part I)',
        'subject': 'Chemistry',
        'grade': 'XI',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': 275,
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
