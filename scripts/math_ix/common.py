"""Helpers for the Math IX (Sindh Textbook Board) solution builder.

Math IX PDF has 312 pages; book page = PDF page - 3 (front matter is 3 pages).
Item shape matches public/data/class_x_math.json.
"""
BOOK_OFFSET = 3


def _slug(text):
    out = []
    for ch in str(text).lower():
        if ch.isalnum():
            out.append(ch)
    return ''.join(out)


def bq(unit, section, code, number, question, answer, explanation, pdf_page, figure=None):
    """A structured / short-answer solution item."""
    item = {
        'id': f'u{unit}_{_slug(code)}_q{_slug(number)}',
        'chapter': unit,
        'section': section,
        'sectionCode': code,
        'type': 'sq',
        'number': number,
        'question': question,
        'answer': answer,
        'explanation': explanation,
        'pdfPage': pdf_page,
        'bookPage': pdf_page - BOOK_OFFSET,
        'options': None,
        'optionsRaw': None,
        'correctAnswer': None,
    }
    if figure:
        item['figure'] = figure
    return item


def mcq(unit, section, code, number, question, opts, correct, explanation, pdf_page):
    """A multiple-choice item.

    opts: list of option texts in order (a, b, c, d).
    correct: the letter of the correct option, e.g. 'c'.
    """
    letters = 'abcd'
    options = [{'key': letters[i], 'text': t} for i, t in enumerate(opts)]
    options_raw = '  '.join(f'{letters[i]}) {t}' for i, t in enumerate(opts))
    return {
        'id': f'u{unit}_{_slug(code)}_q{_slug(number)}_mcq',
        'chapter': unit,
        'section': section,
        'sectionCode': code,
        'type': 'mcq',
        'number': number,
        'question': question,
        'answer': f'({correct}) {opts[letters.index(correct)]}',
        'explanation': explanation,
        'pdfPage': pdf_page,
        'bookPage': pdf_page - BOOK_OFFSET,
        'options': options,
        'optionsRaw': options_raw,
        'correctAnswer': f'({correct}) {opts[letters.index(correct)]}',
    }
