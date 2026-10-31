# -*- coding: utf-8 -*-
"""Build public/data/class_ix_sindhi.json from solved fragments.

Asaan Sindhi (آسان سنڌي) Class IX - Sindh Textbook Board.
Image-only scanned book; page images rendered at 200 DPI.
Page mapping: printed book page = imageNNN + 2  (e.g. page_005.png = printed p.07)
              pdfPage (1-based) = imageNNN + 1
"""
import json, os, re, glob

PART_DIR = os.path.join(os.path.dirname(__file__), 'sindhi_ix_parts')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'class_ix_sindhi.json')

SUBJECT = 'Asaan Sindhi'
GRADE = 'IX'
BOARD = 'Sindh Textbook Board, Jamshoro'
TOTAL_PAGES = 91
PAGES_DIR = '/books/class_ix/sindhi/pages'

# (unit, title, book_start, book_end)  -- printed page numbers
UNITS = [
    (1,  'حجة الوداع وارو خطبو', 7, 10),
    (2,  'حضرت سلمان فارسي', 11, 13),
    (3,  'حضرت امام جعفر صادق', 14, 16),
    (4,  'قائدِاعظم جا ارشاد', 17, 20),
    (5,  'اتحاد، تنظيم ۽ يقين محڪم', 21, 23),
    (6,  'مولانا دين محمد وفائي', 24, 28),
    (7,  'مائي خيري', 29, 32),
    (8,  'هُنر دولت آهي', 33, 35),
    (9,  'خط', 36, 38),
    (10, 'بين الاقوامي عدالت', 39, 42),
    (11, 'اجرڪ', 43, 46),
    (12, 'ميرن جي دربار', 47, 50),
    (13, 'ڪينجهر ڍنڍ', 51, 53),
    (14, 'سنڌي ادب جي مختصر تاريخ', 54, 58),
    (15, 'رڌ پچاءُ', 59, 61),
    (16, 'ٻہ تہ بارهن', 62, 65),
    (17, 'نصرپور', 66, 68),
    (18, 'جهڙو راڄ تهڙو ياڳ', 69, 74),
    (19, 'آهيون الف آسري', 75, 76),
    (20, 'نيڪي', 77, 78),
    (21, 'دُعا', 79, 80),
    (22, 'سچل سرمست', 81, 82),
    (23, 'ڏيئو', 83, 85),
    (24, 'ٻڌايون سُک جو سنسار', 86, 87),
    (25, 'پيارا وطن', 88, 89),
    (26, 'هاري', 90, 91),
]

# Sindhi part letter -> latin code / sort order
PART_LATIN = {'الف': 'A', 'ب': 'B', 'ج': 'C', 'د': 'D', 'ه': 'E'}
PART_ORDER = {'الف': 0, 'ب': 1, 'ج': 2, 'د': 3, 'ه': 4}

# content-type word (from figure) -> readable Sindhi phrase
TYPE_PHRASE = {
    'سوال': 'سوالن جا جواب',
    'اصطلاح': 'اصطلاح ۽ محاورا',
    'لفظ': 'لفظن جا معنيٰ ۽ جملا',
    'ضد': 'لفظن جا ضد',
}

FIG_RE = re.compile(r'مشق\s*\(([^)]+)\)\s*[-ـ]\s*([^\d]+?)(?:\s+\d+)?\s*$')


def parse_figure(figure, fallback_letter):
    """Return (part_sindhi, type_word)."""
    if figure:
        m = FIG_RE.search(figure.strip())
        if m:
            part = m.group(1).strip()
            tw = m.group(2).strip()
            return part, tw
    # fallback: map agent letter back
    inv = {'A': 'الف', 'B': 'ب', 'C': 'ج', 'D': 'د', 'E': 'ه', 'F': 'و', 'G': 'ز'}
    return inv.get(str(fallback_letter).upper(), 'الف'), 'سوال'


def normalize(item):
    unit = int(item['unit'])
    figure = item.get('figure') or ''
    part, tw = parse_figure(figure, item.get('letter'))
    latin = PART_LATIN.get(part, str(item.get('letter', 'A')).upper())
    phrase = TYPE_PHRASE.get(tw, tw if tw else 'سوالن جا جواب')
    section = 'مشق (%s) ـ %s' % (part, phrase)
    img = int(item['image'])
    out = {
        'id': item['id'],
        'unit': unit,
        'section': section,
        'sectionCode': 'U%d%s' % (unit, latin),
        'type': item.get('type', 'sq'),
        'number': int(item.get('number', 1)),
        'question': item.get('question', ''),
        'answer': item.get('answer', ''),
        'explanation': item.get('explanation', ''),
        'figure': figure if figure else None,
        'pdfPage': img + 1,
        'bookPage': img + 2,
    }
    if out['type'] == 'mcq':
        out['options'] = item.get('options')
        out['optionsRaw'] = item.get('optionsRaw')
        out['correctAnswer'] = item.get('correctAnswer')
    return out, PART_ORDER.get(part, 9)


def main():
    items = []
    for path in sorted(glob.glob(os.path.join(PART_DIR, 'part_*.json'))):
        frag = json.load(open(path, encoding='utf-8'))
        for it in frag:
            norm, _ = normalize(it)
            items.append(norm)

    # validate ids
    ids = [it['id'] for it in items]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit('Duplicate ids: %s' % sorted(dupes)[:20])

    chapters = []
    for unit, title, bs, be in UNITS:
        qs = [it for it in items if it['unit'] == unit]
        # order: by part order then number
        def key(it):
            po = PART_ORDER.get(parse_figure(it['figure'] or '', it['sectionCode'][-1])[0], 9)
            return (po, it['number'])
        qs.sort(key=key)
        for i, q in enumerate(qs, 1):
            q['number'] = i  # continuous per lesson? keep per-part numbering instead
        chapters.append({
            'number': unit,
            'title': title,
            'startPage': bs - 1,   # pdfPage of first book page
            'endPage': be - 1,
            'bookStart': bs,
            'bookEnd': be,
            'totalQuestions': len(qs),
            'questions': qs,
        })

    # pages map: printed page -> image path (only pages that exist as images)
    pages = {}
    for img in range(0, 90):
        printed = img + 2
        if printed >= 1:
            pages['page_%03d' % printed] = '%s/page_%03d.png' % (PAGES_DIR, img)

    total_q = sum(c['totalQuestions'] for c in chapters)
    data = {
        'subject': SUBJECT,
        'grade': GRADE,
        'board': BOARD,
        'totalPages': TOTAL_PAGES,
        'totalChapters': len(chapters),
        'totalQuestionsSolved': total_q,
        'chapters': chapters,
        'pages': pages,
    }
    out_abs = os.path.abspath(OUT_PATH)
    with open(out_abs, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print('Wrote', out_abs)
    print('chapters=%d questions=%d' % (len(chapters), total_q))
    for c in chapters:
        print('  U%-2d %-28s %3d q  (book %d-%d)' % (c['number'], c['title'], c['totalQuestions'], c['bookStart'], c['bookEnd']))


if __name__ == '__main__':
    main()
