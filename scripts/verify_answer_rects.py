"""
SubjectZone - answerRect Audit
Independently verifies every MCQ answerRect: re-OCRs the full page (same
quality the pipeline saw), collects the OCR boxes overlapping the rect, and
checks that the rect either contains the expected answer text or is a
letter-only rect pointing at the correct option letter.

Run:  python scripts/verify_answer_rects.py [--subject biology|physics|chemistry]
"""
import os
import sys
import json

import fitz

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_answer_highlights import (BOOKS, DATA_FILES, PageOCR, norm,
                                       similarity, answer_text_of, letter_of,
                                       letter_prefix_of, is_letter_box)


def rect_px(rect, pw, ph):
    return {'x0': rect['x'] * pw, 'y0': rect['y'] * ph,
            'x1': (rect['x'] + rect['w']) * pw, 'y1': (rect['y'] + rect['h']) * ph}


def overlaps(a, b):
    return a['x0'] < b['x1'] and a['x1'] > b['x0'] and a['y0'] < b['y1'] and a['y1'] > b['y0']


def judge(rect, boxes, pw, ph, answer):
    """Returns (ok, detail). ok=True if the rect is justified."""
    rp = rect_px(rect, pw, ph)
    inside = [b for b in boxes if overlaps(rp, b)]
    nt = norm(' '.join(b['text'] for b in inside))
    raw_at = answer_text_of(answer)
    at = norm(raw_at)
    letter = letter_of(answer)

    if not at:
        # bare-letter answer (e.g. 'C'): rect should contain that letter
        if letter and letter in nt:
            return True, 'bare letter present'
        return False, f"bare letter {letter!r}, crop reads {nt[:40]!r}"

    def text_matches(expected):
        expected = norm(expected)
        if not expected:
            return False
        if expected in nt or similarity(expected, nt) >= (0.6 if len(expected) <= 3 else 0.55):
            return True
        # per-box comparison tolerates OCR typos in a single option line
        return any(similarity(expected, norm(b['text'])) >= 0.7 for b in inside)

    # compound answers ('X / Y', 'Both a & b'): accept if any part matches.
    # Split the RAW text (norm strips the '/' separator).
    parts = [p.strip() for p in raw_at.split('/') if p.strip()]
    if any(text_matches(p) for p in parts) or text_matches(raw_at):
        return True, 'answer text inside rect'

    # letter-only rect: the option text sits in a sibling box; accept when the
    # rect is small and contains the correct letter label
    if letter and len(nt) <= 8 and (letter in nt or
                                    any(is_letter_box(b) == letter or
                                        letter_prefix_of(b) == letter for b in inside)):
        return True, 'letter-only rect, correct letter'

    detail = f"expected {answer_text_of(answer)[:40]!r}, rect reads {' '.join(b['text'] for b in inside)[:50]!r}"
    return False, detail


def audit(subject):
    with open(DATA_FILES[subject], encoding='utf-8') as f:
        data = json.load(f)
    doc = fitz.open(BOOKS[subject])
    pocr = PageOCR(doc)

    ok = wrong = missing = 0
    flags = []
    for ch in data['chapters']:
        for q in ch['questions']:
            if q.get('type') != 'mcq':
                continue
            rect = q.get('answerRect')
            if not rect:
                missing += 1
                continue
            boxes, pw, ph = pocr.get(q['pdfPage'] - 1)
            good, detail = judge(rect, boxes, pw, ph, q['correctAnswer'])
            if good:
                ok += 1
            else:
                wrong += 1
                flags.append(f"WRONG ch{ch['number']} {q['id']} p{q['pdfPage']}: {detail}")

    print(f'=== {subject}: {ok} verified, {wrong} wrong, {missing} without rect ===')
    for f in flags:
        print(' ', f)


if __name__ == '__main__':
    args = [a.lower() for a in sys.argv[1:]]
    subjects = [a for a in args if a in BOOKS] or ['biology', 'physics', 'chemistry']
    for s in subjects:
        audit(s)
