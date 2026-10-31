"""Builds public/data/class_ix_math.json for the SubjectZone app.

Sindh Textbook Board, Class IX Mathematics. PDF has 312 pages; book page = PDF page - 3.
Solutions live in scripts/math_ix/uXX.py (one module per unit); this file assembles them
and writes the chapter/page map consumed by src/js/app.js.
"""
import json
import os

from math_ix import u01, u02, u03, u04, u05, u06, u07, u08
from math_ix import u09, u10, u11, u12, u13, u14, u15, u16

OUT = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'class_ix_math.json')

# (number, title, pdf_start, pdf_end, book_start, book_end)  -- titles from the book CONTENTS page
UNITS = [
    (1,  'Real and Complex Numbers',                                  4,   28,  1,   25),
    (2,  'Logarithms',                                                29,  55,  26,  52),
    (3,  'Algebraic Expression and Formulas',                         56,  84,  53,  81),
    (4,  'Factorization',                                             85,  106, 82,  103),
    (5,  'Algebraic Manipulation',                                    107, 125, 104, 122),
    (6,  'Linear Equation and Inequalities',                          126, 139, 123, 136),
    (7,  'Linear Graphs and their Applications',                      140, 163, 137, 160),
    (8,  'Quadratic Equations',                                       164, 183, 161, 180),
    (9,  'Congruent Triangles',                                       184, 194, 181, 191),
    (10, 'Parallelograms and Triangles',                              195, 205, 192, 202),
    (11, 'Line Bisectors and Angles Bisectors',                       206, 216, 203, 213),
    (12, 'Sides and Angles of a Triangle',                            217, 225, 214, 222),
    (13, 'Practical Geometry - Triangles',                            226, 237, 223, 234),
    (14, 'Theorems Related with Area',                                238, 245, 235, 242),
    (15, 'Projection of a side of a Triangle',                        246, 253, 243, 250),
    (16, 'Introduction to Coordinate Geometry/Analytical Geometry',   254, 270, 251, 267),
]
TOTAL_PAGES = 312
BOOK_OFFSET = 3

MODULES = [u01, u02, u03, u04, u05, u06, u07, u08,
           u09, u10, u11, u12, u13, u14, u15, u16]

SOLVED_TYPES = ('sq',)


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
        'grade': 'Class IX',
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
        print(f"  Unit {ch['number']:>2} {ch['title'][:42]:<44} {ch['totalQuestions']}")
    print('TOTAL:', len(solved))


if __name__ == '__main__':
    build()
