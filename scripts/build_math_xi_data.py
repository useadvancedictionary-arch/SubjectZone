"""Builds public/data/class_xi_math.json for the SubjectZone app.

Sindh Textbook Board, Class XI Mathematics. PDF has 424 pages; book page = PDF page - 4.
Solutions live in scripts/math_xi/uXX.py (one module per unit); this file assembles them
and writes the chapter/page map consumed by src/js/app.js.
"""
import json
import os

from math_xi import u01, u02, u03, u04, u05, u06, u07, u08, u09, u10, u11, u12

OUT = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'class_xi_math.json')

# (number, title, pdf_start, pdf_end, book_start, book_end)  -- titles from the book CONTENTS page
UNITS = [
    (1,  'Complex Numbers',                                                     5,   28,  1,   24),
    (2,  'Matrices and Determinants',                                           29,  77,  25,  73),
    (3,  'Vectors',                                                             78,  127, 74,  123),
    (4,  'Sequences and Series',                                                128, 165, 124, 161),
    (5,  'Miscellaneous Series',                                                166, 182, 162, 178),
    (6,  'Permutation, Combination and Probability',                            183, 217, 179, 213),
    (7,  'Mathematical Induction and Binomial Theorem',                         218, 241, 214, 237),
    (8,  'Functions and Graphs',                                                242, 270, 238, 266),
    (9,  'Linear Programming',                                                  271, 295, 267, 291),
    (10, 'Trigonometric Identities of Sum and Difference of Angles',            296, 320, 292, 316),
    (11, 'Application of Trigonometry',                                         321, 340, 317, 336),
    (12, 'Graphs of Trigonometric and Inverse Trigonometric Functions and Solution of Trigonometric Equations',
                                                                                341, 391, 337, 387),
]
TOTAL_PAGES = 424
BOOK_OFFSET = 4

MODULES = [u01, u02, u03, u04, u05, u06, u07, u08, u09, u10, u11, u12]

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
        'subject': 'Mathematics',
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
