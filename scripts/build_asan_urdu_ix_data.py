# -*- coding: utf-8 -*-
"""Build public/data/class_ix_asan_urdu.json from solved fragments.

Asan Urdu (آسان اردو) Class IX - Sindh Textbook Board, IX-X combined volume.
Image-only spread scans: page_NNN.png holds two printed pages (right = odd,
left = even). Printed Class IX portion = pp.1-70 (Part 1, lessons 1-17);
Part 2 / Class X begins p.71.
Page mapping (verified against printed folios):
    image index = (printed_page - 1) // 2 ; right half for odd, left for even
Fragments: scripts/asan_urdu_ix_parts/u{N}.json, each carrying explicit
`pdfPage` (1-based image index) and `bookPage` (printed page).
"""
import json, os, glob

PART_DIR = os.path.join(os.path.dirname(__file__), 'asan_urdu_ix_parts')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'class_ix_asan_urdu.json')

SUBJECT = 'Asan Urdu'
GRADE = 'IX'
BOARD = 'Sindh Textbook Board, Jamshoro'
TOTAL_PAGES = 70
PAGES_DIR = '/books/class_ix/asan_urdu/pages'


# (unit, title, book_start, book_end)  -- printed page numbers
UNITS = [
    (1,  'نعت کا پیغام', 7, 9),
    (2,  'جاؤ، آج تم سب آزاد ہو', 10, 12),
    (3,  'پاکستان سے محبت', 13, 16),
    (4,  'حضرت عمر بن عبدالعزیزؒ', 17, 20),
    (5,  'تعصب', 21, 23),
    (6,  'وطن کی خاطر', 24, 27),
    (7,  'آتش بازی', 28, 30),
    (8,  'بہادر یار جنگ', 31, 34),
    (9,  'قائدِ اعظمؒ سے پہلی اور آخری ملاقات', 35, 40),
    (10, 'فضول رسمیں', 41, 44),
    (11, 'نام دیو مالی', 45, 47),
    (12, 'ایک دلچسپ سفر', 48, 50),
    (13, 'ہم سب ایک ہیں', 51, 55),
    (14, 'قومی اور علاقائی زبانیں', 56, 58),
    (15, 'شہیدِ ملت', 59, 62),
    (16, 'آب دوز کشتی', 63, 66),
    (17, 'مرزا غالب کی باتیں', 67, 70),
]


def normalize(it):
    img = int(it['pdfPage']) - 1
    bp = int(it['bookPage'])
    out = {
        'id': it['id'],
        'unit': int(it['unit']),
        'section': it['section'],
        'sectionCode': it.get('sectionCode', 'U%d' % int(it['unit'])),
        'type': it.get('type', 'sq'),
        'number': int(it.get('number', 1)),
        'question': it.get('question', ''),
        'answer': it.get('answer', ''),
        'explanation': it.get('explanation', ''),
        'figure': it.get('figure'),
        'pdfPage': img + 1,
        'bookPage': bp,
    }
    if out['type'] == 'mcq':
        raw = it.get('options') or []
        opts = []
        for i, o in enumerate(raw):
            if isinstance(o, dict):
                opts.append({'key': o.get('key') or chr(97 + i), 'text': o.get('text', '')})
            else:
                opts.append({'key': chr(97 + i), 'text': str(o)})
        ca = it.get('correctAnswer')
        if isinstance(ca, int) and 1 <= ca <= len(opts):
            correct = '(%s) %s' % (opts[ca - 1]['key'], opts[ca - 1]['text'])
        else:
            correct = ca
        out['options'] = opts
        out['optionsRaw'] = it.get('optionsRaw')
        out['correctAnswer'] = correct
    return out


def main():
    items = []
    for path in sorted(glob.glob(os.path.join(PART_DIR, 'u[0-9]*.json'))):
        frag = json.load(open(path, encoding='utf-8'))
        for it in frag:
            items.append(normalize(it))

    ids = [it['id'] for it in items]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit('Duplicate ids: %s' % sorted(dupes)[:20])

    # --- validation -------------------------------------------------------
    problems = []
    units = {u[0]: u for u in UNITS}
    for it in items:
        qid = it['id']
        if it['unit'] not in units:
            problems.append('%s: unknown unit %s' % (qid, it['unit']))
        if not it['question'].strip():
            problems.append('%s: empty question' % qid)
        if not it['answer'].strip():
            problems.append('%s: empty answer' % qid)
        if it['type'] == 'mcq':
            opts = it.get('options') or []
            if len(opts) < 2:
                problems.append('%s: mcq needs >=2 options' % qid)
            keys = [o.get('key') for o in opts if isinstance(o, dict)]
            if len(keys) != len(opts):
                problems.append('%s: malformed option entries' % qid)
            ca = it.get('correctAnswer')
            if not isinstance(ca, str) or not ca.strip():
                problems.append('%s: mcq needs a string correctAnswer' % qid)
            elif not keys or ca[1:ca.find(')')] not in keys:
                problems.append('%s: correctAnswer %r does not reference an option key' % (qid, ca))
        u = units.get(it['unit'])
        if u and not (u[2] <= it['bookPage'] <= u[3]):
            problems.append('%s: bookPage %s outside unit %s range %s-%s'
                            % (qid, it['bookPage'], it['unit'], u[2], u[3]))
    if problems:
        raise SystemExit('Validation failed:\n  ' + '\n  '.join(problems[:40]))

    chapters = []
    for unit, title, bs, be in UNITS:
        qs = [dict(it) for it in items if it['unit'] == unit]
        qs.sort(key=lambda it: (it['number'], it['id']))
        chapters.append({
            'number': unit,
            'title': title,
            'startPage': bs,
            'endPage': be,
            'bookStart': bs,
            'bookEnd': be,
            'totalQuestions': len(qs),
            'questions': qs,
        })

    total_q = sum(c['totalQuestions'] for c in chapters)
    data = {
        'subject': SUBJECT,
        'grade': GRADE,
        'board': BOARD,
        'totalPages': TOTAL_PAGES,
        'totalChapters': len(chapters),
        'totalQuestionsSolved': total_q,
        'chapters': chapters,
        'pages': {},
    }
    out_abs = os.path.abspath(OUT_PATH)
    with open(out_abs, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print('Wrote', out_abs)
    print('chapters=%d questions=%d' % (len(chapters), total_q))
    for c in chapters:
        print('  U%-2d %-45s %3d q  (book %d-%d)' % (c['number'], c['title'], c['totalQuestions'], c['bookStart'], c['bookEnd']))


if __name__ == '__main__':
    main()
