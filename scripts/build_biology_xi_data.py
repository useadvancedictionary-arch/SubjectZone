#!/usr/bin/env python3
"""Builds public/data/class_xi_biology.json from per-chapter fragments.

Biology XI (Sindh Textbook Board): 14 chapters. Each exercise has
1. Encircle the correct choice (10 MCQs)
2. Short answers (7)
3. Detailed answers (7)

Printed page = PDF page - 5 (chapter 1 printed p.1 = PDF p.6).
Fragments live in scripts/biology_xi_parts/cN.json.
"""
import json
import os
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PART_DIR = os.path.join(ROOT, 'scripts', 'biology_xi_parts')
OUT = os.path.join(ROOT, 'public', 'data', 'class_xi_biology.json')
OFFSET = 5

# (number, title, book start, book end)
UNITS = [
    (1, 'Biological Molecules', 1, 27),
    (2, 'Enzymes', 28, 40),
    (3, 'Cell Structure and Function', 41, 69),
    (4, 'Bioenergetics', 70, 95),
    (5, 'Acellular Life', 96, 116),
    (6, 'Prokaryotes', 117, 146),
    (7, 'Protoctists and Fungi', 147, 164),
    (8, 'Diversity Among Plants', 165, 191),
    (9, 'Diversity Among Animals', 192, 220),
    (10, 'Forms and Functions in Plant', 221, 249),
    (11, 'Holozoic Nutrition', 250, 271),
    (12, 'Circulation', 272, 293),
    (13, 'Immunity', 294, 316),
    (14, 'Gaseous Exchange', 317, 333),
]

SEC = {
    'A': ('Exercise {n} MCQs', 'mcq'),
    'B': ('Exercise {n} Short Questions', 'sq'),
    'C': ('Exercise {n} Detailed Answers', 'erq'),
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
    range_by_no = {n: (s, e) for n, _t, s, e in UNITS}
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
            assert 1 <= q['pdfPage'] <= 338, f'{q["id"]}: bad pdfPage {q["pdfPage"]}'
        # order by section then number
        order = {'A': 0, 'B': 1, 'C': 2}
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
        'subjectId': 'biology_xi',
        'subjectName': 'Biology',
        'gradeId': 'class_xi',
        'gradeName': 'Class XI (HSC Part I)',
        'subject': 'Biology',
        'grade': 'XI',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': 338,
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
