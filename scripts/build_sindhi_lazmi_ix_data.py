# -*- coding: utf-8 -*-
"""Build public/data/class_ix_sindhi_lazmi.json from solved fragments.

Sindhi Lazmi (سنڌي لازمي) Class IX - Sindh Textbook Board.
Image-only scanned book; page images rendered at 200 DPI; OCR'd with tesseract (snd).
Page mapping: printed book page = imageNNN (offset 0; page_006.png = printed p.6)
              pdfPage (1-based) = imageNNN + 1
Fragments: scripts/sindhi_lazmi_ix_parts/u{N}.json (one per lesson).
"""
import json, os, re, glob

PART_DIR = os.path.join(os.path.dirname(__file__), 'sindhi_lazmi_ix_parts')
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'class_ix_sindhi_lazmi.json')

SUBJECT = 'Sindhi Lazmi'
GRADE = 'IX'
BOARD = 'Sindh Textbook Board, Jamshoro'
TOTAL_PAGES = 209
PAGES_DIR = '/books/class_ix/sindhi_lazmi/pages'

# (unit, title, book_start, book_end)  -- printed page numbers
UNITS = [
    (1,  'حضرت اکرم ﷺ جن جا اخلاق مبارڪ', 6, 13),
    (2,  'حضرت امام حسين عليه السلام', 14, 18),
    (3,  'علامه آءِ. آءِ. قاضي', 19, 24),
    (4,  'گنجي ٽڪر جو سير', 25, 28),
    (5,  'سنڌي ادب جي مختصر تاريخ', 29, 34),
    (6,  'سڄائي', 35, 38),
    (7,  'ڪاهوءَ جو دڙو', 39, 45),
    (8,  'وسڪارو', 46, 50),
    (9,  'ساڻيهه جي سِڪ', 51, 55),
    (10, 'ٻين جا عيب برداشت ڪرڻ', 56, 58),
    (11, 'شاه جي ٻوليءَ جو معيار', 59, 62),
    (12, 'جمشيد نسروانجي ۽ هڪ نيڪ دل انسان', 63, 68),
    (13, 'ڪوٽڙي جو سير', 69, 72),
    (14, 'شخصيت ۽ لباس', 73, 77),
    (15, 'ڇريائي', 78, 80),
    (16, 'موڪلائڻي', 81, 86),
    (17, 'بد تميز', 87, 90),
    (18, 'سورٺ ۽ راءِ ڏياچ', 91, 96),
    (19, 'اونداهي ڌرتي روشن هٿ', 97, 103),
    (20, 'ڇنڊ ۽ ماني (درامو)', 104, 108),
    (21, 'منهنجي آتم ڪهاڻي', 109, 114),
    (22, 'سنگاپور ۾ ست ڏينهن', 115, 119),
    (23, 'علو موچيءَ جو راڳُ سِکڻ (طنز و مزاح)', 120, 126),
    (24, 'چانڊوڪيءَ مان (ادبي خط)', 127, 129),
    (25, 'شاه عبداللطيف ڀٽائيؒ', 130, 132),
    (26, 'ميان سرفراز ڪلهوڙو', 133, 135),
    (27, 'سچل سرمستؒ', 136, 138),
    (28, 'سامي', 139, 142),
    (29, 'سيد ثابت علي شاھ', 143, 145),
    (30, 'مير عبدالحسين ”سانگي“', 146, 148),
    (31, 'محمد صديق ”مسافر“', 149, 152),
    (32, 'ڪشنچند ”بيوس“', 153, 156),
    (33, 'عبدالڪريم ”گدائي“', 157, 160),
    (34, 'حيدر بخش جتوئي', 161, 164),
    (35, 'غلام احمد نظامي', 165, 167),
    (36, 'مخدوم محمد زمان ”طالب الموليٰ“', 168, 170),
    (37, 'شيخ اياز', 171, 173),
    (38, 'نياز همايوني', 174, 176),
    (39, 'شمشير الحيدري', 177, 179),
    (40, 'تنوير عباسي', 180, 183),
    (41, 'امداد حسيني', 184, 186),
    (42, 'مريم مجيدي', 187, 189),
    (43, 'سانوڻ فقير (لوڪ شاعري)', 190, 193),
    # p.194-200: 'نوان لفظ' glossary appendix (lessons 1-19) -- not a lesson, no exercises
]

# printed part label -> latin code / sort order
PART_LATIN = {'الف': 'A', 'ب': 'B', 'ج': 'C', 'د': 'D', 'هـ': 'E', 'ه': 'E', 'و': 'F', 'ز': 'G'}
PART_ORDER = {'الف': 0, 'ب': 1, 'ج': 2, 'د': 3, 'هـ': 4, 'ه': 4, 'و': 5, 'ز': 6}

# content-type word (from figure) -> readable Sindhi phrase
TYPE_PHRASE = {
    'سوال': 'سوالن جا جواب',
    'اصطلاح': 'اصطلاح ۽ محاورا',
    'لفظ': 'لفظن جا معنيٰ ۽ جملا',
    'ضد': 'لفظن جا ضد',
    'خال': 'خال ڀريو',
    'جملو': 'جملاسازي',
    'گرامر': 'گرامر',
    'اسم': 'گرامر (اسم)',
    'سرگرمي': 'سرگرمي',
    'شعر': 'شعر جي سمجھاني',
    'حوالو': 'حوالن جي سمجهاڻي',
    'معنيٰ': 'معنيٰ',
    'موسم': 'گرامر (اسم)',
    'شهر': 'گرامر (اسم)',
}

FIG_RE = re.compile(r'(?:مشق\s*)?\(([^)]+)\)\s*[-ـ]\s*([^\d]+?)(?:\s+\d+)?\s*$')


def parse_figure(figure, fallback_letter):
    if figure:
        m = FIG_RE.search(figure.strip())
        if m:
            return m.group(1).strip(), m.group(2).strip()
        # bare labels like 'نوان لفظ 1' / 'سرگرمي 1'
        m2 = re.match(r'\s*([^\d]+?)\s+\d+\s*$', figure.strip())
        if m2:
            return None, m2.group(1).strip()
    inv = {'A': 'الف', 'B': 'ب', 'C': 'ج', 'D': 'د', 'E': 'هـ', 'F': 'و', 'G': 'ز'}
    return inv.get(str(fallback_letter).upper(), 'الف'), 'سوال'


def normalize(item):
    unit = int(item['unit'])
    figure = item.get('figure') or ''
    part, tw = parse_figure(figure, item.get('letter'))
    latin = PART_LATIN.get(part, str(item.get('letter', 'A')).upper()) if part else str(item.get('letter', 'A')).upper()
    phrase = TYPE_PHRASE.get(tw, tw if tw else 'سوالن جا جواب')
    if part:
        section = 'مشق (%s) ـ %s' % (part, phrase)
    else:
        section = phrase
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
        'bookPage': img,
    }
    if out['type'] == 'mcq':
        raw = item.get('options') or []
        opts = []
        for i, o in enumerate(raw):
            if isinstance(o, dict):
                opts.append({'key': o.get('key') or chr(97 + i), 'text': o.get('text', '')})
            else:
                opts.append({'key': chr(97 + i), 'text': str(o)})
        ca = item.get('correctAnswer')
        if isinstance(ca, int) and 1 <= ca <= len(opts):
            correct = '(%s) %s' % (opts[ca - 1]['key'], opts[ca - 1]['text'])
        else:
            correct = ca
        out['options'] = opts
        out['optionsRaw'] = item.get('optionsRaw')
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

    chapters = []
    for unit, title, bs, be in UNITS:
        qs = [dict(it) for it in items if it['unit'] == unit]

        def key(it):
            fig = it['figure'] or ''
            m = re.search(r'\(([^)]+)\)', fig)
            po = PART_ORDER.get(m.group(1).strip(), 9) if m else 9
            return (po, it['number'])

        qs.sort(key=key)
        chapters.append({
            'number': unit,
            'title': title,
            'startPage': bs + 1,   # pdfPage of lesson start
            'endPage': be + 1,
            'bookStart': bs,
            'bookEnd': be,
            'totalQuestions': len(qs),
            'questions': qs,
        })

    pages = {}
    for img in range(0, 209):
        pages['page_%03d' % img] = '%s/page_%03d.png' % (PAGES_DIR, img)

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
        print('  U%-2d %-40s %3d q  (book %d-%d)' % (c['number'], c['title'], c['totalQuestions'], c['bookStart'], c['bookEnd']))


if __name__ == '__main__':
    main()
