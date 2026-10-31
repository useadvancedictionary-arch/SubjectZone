#!/usr/bin/env python3
"""Builds public/data/class_xi_cs.json for the SubjectZone app.

Computer Science XI (Sindh Textbook Board, Jamshoro): 6 units.
The PDF is image-only, so the exercises were transcribed from the rendered
page images (public/books/class_xi/cs/pages). Book page = PDF page - 5.
The book contains NO printed answer key, so answers are derived from the
unit content and standard computer-science knowledge.
"""
import json
import os

from cs_xi import u01, u02, u03, u04, u05, u06

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'public', 'data', 'class_xi_cs.json')

# (unit_number, title, pdf_start, pdf_end, book_start, book_end)
UNITS = [
    (1, 'Computer Systems',                            6,   75,  1,   70),
    (2, 'Computational Thinking & Algorithm',          76,  95,  71,  90),
    (3, 'Programming Fundamentals',                    96,  143, 91,  138),
    (4, 'Data and Analysis',                           144, 178, 139, 173),
    (5, 'Applications and Impacts of Computing',       179, 203, 174, 198),
    (6, 'Digital Literacy',                            204, 223, 199, 218),
]
TOTAL_PAGES = 240
BOOK_OFFSET = 5

MODULES = [u01, u02, u03, u04, u05, u06]

SOLVED_TYPES = ('sq', 'mcq')


def collect():
    items = []
    for m in MODULES:
        items.extend(getattr(m, 'ITEMS', []))
    return items


def build():
    solved = collect()
    by_unit = {}
    for it in solved:
        by_unit.setdefault(it['chapter'], []).append(it)

    chapters = []
    for num, title, ps, pe, bs, be in UNITS:
        qs = by_unit.get(num, [])
        chapters.append({
            'number': num, 'title': title,
            'startPage': ps, 'endPage': pe,
            'bookStart': bs, 'bookEnd': be,
            'totalQuestions': len(qs),
            'questions': qs,
        })

    solved_pages = {}
    for it in solved:
        solved_pages.setdefault(it['pdfPage'], []).append(it)

    pages_map = {}
    for p in range(1, TOTAL_PAGES + 1):
        chapter_number = None
        for num, _t, ps, pe, _bs, _be in UNITS:
            if ps <= p <= pe:
                chapter_number = num
                break
        pages_map[str(p)] = {
            'pdfPage': p,
            'bookPage': p - BOOK_OFFSET,
            'chapterNumber': chapter_number,
            'isFrontMatter': p <= BOOK_OFFSET,
            'hasExercise': p in solved_pages,
            'questions': solved_pages.get(p, []),
        }

    data = {
        'subject': 'Computer Science',
        'grade': 'Class XI',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': TOTAL_PAGES,
        'totalChapters': len(UNITS),
        'totalQuestionsSolved': len(solved),
        'chapters': chapters,
        'pages': pages_map,
    }

    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f'Built {OUT}: {len(solved)} items across {len(chapters)} units.')
    for ch in chapters:
        print(f"  Unit {ch['number']:>2} {ch['title'][:52]:<54} {ch['totalQuestions']}")
    print('TOTAL:', len(solved))


if __name__ == '__main__':
    build()
