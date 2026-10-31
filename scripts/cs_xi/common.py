"""Shared helpers for the Computer Science XI solution modules.

Book page = PDF page - 5 (PDF page 6 is printed page 1).
Every exercise in CS XI has the same five-part shape:
  A  Encircle the correct answer (10 MCQs)
  B  Fill in the Blanks (5)
  C  Provide short descriptive answers (5)
  D  Provide detailed answers (variable: 3-5)
  E  Activities (variable: 3-8)
The book has no printed answer key; answers are derived from the unit content
plus standard computer-science knowledge.
"""
import re

BOOK_OFFSET = 5

SECTION_LABELS = {
    'A': 'MCQs',
    'B': 'Fill in the Blanks',
    'C': 'Short Questions',
    'D': 'Detailed Questions',
    'E': 'Activities',
}


def section_name(chapter, code):
    return f'Exercise {chapter} \u2014 {SECTION_LABELS.get(code, code)}'


def _slug(value):
    text = re.sub(r'[^a-z0-9]+', '', str(value).lower())
    return text or 'x'


def _base(chapter, code, number, qtype, question, answer, explanation, pdf_page):
    return {
        'id': f'u{chapter}_ex{code}_q{_slug(number)}',
        'chapter': chapter,
        'section': section_name(chapter, code),
        'sectionCode': f'EX{chapter}{code}',
        'type': qtype,
        'number': str(number),
        'question': question,
        'answer': answer,
        'explanation': explanation,
        'pdfPage': pdf_page,
        'bookPage': pdf_page - BOOK_OFFSET,
        'options': None,
        'optionsRaw': None,
        'correctAnswer': None,
    }


def bq(chapter, code, number, question, answer, explanation, pdf_page):
    """A written-answer item (fill in the blank, short, detailed, activity)."""
    return _base(chapter, code, number, 'sq', question, answer, explanation, pdf_page)


def mcq(chapter, code, number, question, opts, correct, explanation, pdf_page):
    """An MCQ; opts is [(key, text), ...], correct is the key letter."""
    item = _base(chapter, code, number, 'mcq', question, '', explanation, pdf_page)
    item['options'] = [{'key': k, 'text': t} for k, t in opts]
    item['optionsRaw'] = '   '.join(f'({k}) {t}' for k, t in opts)
    answer_text = dict(opts)[correct]
    item['answer'] = f'({correct}) {answer_text}'
    item['correctAnswer'] = item['answer']
    return item
