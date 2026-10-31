# -*- coding: utf-8 -*-
"""Build public/data/class_ix_urdu.json from solved fragments.

Urdu Lazmi (اردو لازمی) Class IX - Sindh Textbook Board, IX-X combined volume.
Image-only spread scans: each page_NNN.png holds two printed pages (right = odd,
left = even), with a few single-page images. Printed Class IX portion = pp.1-186.
Page mapping (verified against printed folios):
    right_page(image i) = 1 + 2*i - (number of single-page images before i)
Fragments: scripts/urdu_ix_parts/u{N}.json, each carrying explicit
`pdfPage` (1-based image index) and `bookPage` (printed page).
"""
import json, os, glob

PART_DIR = os.path.join(os.path.dirname(__file__), 'urdu_ix_parts')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'class_ix_urdu.json')

SUBJECT = 'Urdu Lazmi'
GRADE = 'IX'
BOARD = 'Sindh Textbook Board, Jamshoro'
TOTAL_PAGES = 186
PAGES_DIR = '/books/class_ix/urdu/pages'

# single-page images in the PDF (left or right half blank)
SINGLES = {25, 42, 59, 79, 82, 86, 95, 103}


def right_page(i):
    return 1 + 2 * i - sum(1 for s in SINGLES if s < i)


# (unit, title, book_start, book_end)  -- printed page numbers
UNITS = [
    (1,  'اخلاق نبوی ﷺ', 10, 18),
    (2,  'امید کی خوشی', 19, 23),
    (3,  'قومی ہمدردی', 24, 30),
    (4,  'رشتہ ناتا', 31, 39),
    (5,  'نظریۂ پاکستان', 40, 49),
    (6,  'اصغری نے لڑکیوں کا مکتب بٹھایا', 50, 57),
    (7,  'بوڑھی کاکی', 58, 67),
    (8,  'سیانا بادشاہ', 68, 72),
    (9,  'شہید (ڈراما)', 73, 82),
    (10, 'نام دیو مالی', 83, 89),
    (11, 'ڈسٹرکٹ بورڈ کی ڈسپنسری', 90, 97),
    (12, 'اُو نجُھ', 98, 103),
    (13, 'پکھڑو قدیم تاریخ سے', 104, 110),
    (14, 'بنام ہر گوپال کھتے', 111, 115),
    (15, 'بنام میر مہدی مجروح', 113, 115),
    (16, 'حمد', 117, 121),
    (17, 'نعت', 122, 126),
    (18, 'برسات کا تماشا', 127, 131),
    (19, 'دنیائے اسلام', 132, 136),
    (20, 'سر راہ شہادت', 137, 141),
    (21, 'گرمی کی شدت', 142, 146),
    (22, 'جیوے جیوے پاکستان', 147, 150),
    (23, 'کرکٹ اور مشاعرہ', 151, 154),
    (24, 'فقیرانہ آئے صدا کر چلے', 155, 159),
    (25, 'دہن پر ہیں اُن کے گماں کیسے کیسے', 160, 163),
    (26, 'ہر ایک بات پہ کہتے ہو تم کہ "تُو کیا ہے؟"', 164, 167),
    (27, 'لگتا نہیں ہے جی مرا اُجڑے دیار میں', 168, 172),
    (28, 'دعا میں ذکر کیوں ہو مدعا کا', 173, 177),
    (29, 'جب تک انسان پاک طینت ہی نہیں', 178, 181),
    (30, 'ہونٹوں پہ کبھی اُن کے مرا نام ہی آئے', 182, 185),
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
            if isinstance(it.get('optionsRaw'), list) and len(it['optionsRaw']) != len(opts):
                problems.append('%s: optionsRaw/options length mismatch' % qid)
        else:
            if it.get('options') or it.get('correctAnswer') is not None:
                problems.append('%s: non-mcq carries mcq fields' % qid)
        u = units.get(it['unit'])
        if u and not (u[2] <= it['bookPage'] <= u[3]):
            problems.append('%s: bookPage %s outside unit %s range %s-%s'
                            % (qid, it['bookPage'], it['unit'], u[2], u[3]))
    if problems:
        raise SystemExit('Validation failed:\n  ' + '\n  '.join(problems[:40]))

    chapters = []
    for unit, title, bs, be in UNITS:
        qs = [dict(it) for it in items if it['unit'] == unit]

        def key(it):
            return (it['number'], it['id'])

        qs.sort(key=key)
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
