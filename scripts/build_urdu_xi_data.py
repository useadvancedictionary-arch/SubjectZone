#!/usr/bin/env python3
"""Build public/data/class_xi_urdu.json (Gulzar-E-Urdu XI).

Book: Sindh Textbook Board, Jamshoro — 192 PDF pages, book page = PDF page.
44 lesson chapters: 19 prose, 25 poetry/ghazal. Pages 181-192 are glossary.

Solved fragments: scripts/urdu_xi_parts/lessons_*.json (JSON arrays with the
schema documented in scripts/urdu_xi_parts/README.md).
"""
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, 'scripts', 'urdu_xi_parts')
OUT = os.path.join(ROOT, 'public', 'data', 'class_xi_urdu.json')

TOTAL_PAGES = 192
OFFSET = 0

LESSONS = {
    1: ('قومی اتفاق', 10), 2: ('زبان گویا', 16), 3: ('فاقہ میں روزہ', 20),
    4: ('پٹرولیم کی کہانی', 26), 5: ('کیچ دھریجہ تعلیم کے باب میں', 32),
    6: ('سندھی شعری کے تراجم', 37), 7: ('زبور کا ٹوٹا', 43),
    8: ('با با نور', 53), 9: ('آب حیات', 60), 10: ('میدان جنگ', 68),
    11: ('بیگم کی بیٹی', 74), 12: ('تھر کی نادیہ کلاچی', 85),
    13: ('مملکت بلقیس کا محسن', 90), 14: ('خواہ مخواہ کی لڑائی', 96),
    15: ('جیوڑیاں', 101), 16: ('ایک انار و صد بیمار', 105),
    17: ('جب نام میر مہدی مجروح', 109), 18: ('خان محمد ناز الدین کے نام', 113),
    19: ('جب نام صدیق جاوید', 116),
    20: ('حمد', 119), 21: ('نعت', 122), 22: ('رے نام اللہ کا', 125),
    23: ('داستانِ تیاری میں باغ کی', 128), 24: ('یا رب! چمن نظم کو', 131),
    25: ('چپ کی داد', 134), 26: ('مردِ مسلمان', 137),
    27: ('نوائے سروش', 140), 28: ('رباعیات', 143),
    29: ('تن بہ تقدیر', 146), 30: ('مہک', 146),
    31: ('سائیڈ ایفیکٹس', 148), 32: ('جانِ میری زمیں', 151),
    33: ('افتتاح', 153), 34: ('مشورہ', 156),
    35: ('غزلیات — خواجہ میر درد', 157), 36: ('غزلیات — میر تقی میر', 160),
    37: ('غزلیات — خواجہ حیدر علی آتش', 163),
    38: ('غزلیات — مرزا اسداللہ خان غالب', 166),
    39: ('غزل — داغ دہلوی', 168), 40: ('غزل — حسرت موہانی', 171),
    41: ('غزل — منیر نیازی', 173), 42: ('غزل — احمد فراز', 174),
    43: ('غزل — قائل امرہوی', 176), 44: ('پیامِ لطیف', 178),
}


def normalize(raw):
    lesson = int(raw['lesson'])
    book_page = int(raw['bookPage'])
    item = {
        'id': raw['id'],
        'chapter': lesson,
        'section': raw.get('section') or 'مشق',
        'sectionCode': raw.get('sectionCode') or f'L{lesson:02d}',
        'type': raw.get('type', 'sq'),
        'number': str(raw.get('number', '')),
        'question': (raw.get('question') or '').strip(),
        'answer': (raw.get('answer') or '').strip(),
        'explanation': (raw.get('explanation') or '').strip(),
        'pdfPage': book_page + OFFSET,
        'bookPage': book_page,
        'options': None,
        'optionsRaw': None,
        'correctAnswer': None,
    }
    if item['type'] == 'mcq':
        opts = raw.get('options') or []
        item['options'] = [{'key': o['key'], 'text': o['text']} for o in opts]
        item['optionsRaw'] = raw.get('optionsRaw') or '   '.join(
            f"({o['key']}) {o['text']}" for o in opts)
        item['correctAnswer'] = raw.get('correctAnswer', '')
    return item


def main():
    paths = sorted(glob.glob(os.path.join(PARTS, 'lessons_*.json')))
    if not paths:
        raise SystemExit('No lesson part files found')
    items = []
    seen = set()
    for path in paths:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise SystemExit(f'{os.path.basename(path)}: expected a JSON array')
        for raw in data:
            item = normalize(raw)
            if item['id'] in seen:
                raise SystemExit(f'Duplicate id: {item["id"]} in {path}')
            seen.add(item['id'])
            items.append(item)

    problems = []
    for item in items:
        if not item['question']:
            problems.append(f"{item['id']}: empty question")
        if not item['answer']:
            problems.append(f"{item['id']}: empty answer")
        if item['type'] == 'mcq' and len(item['options'] or []) != 4:
            problems.append(f"{item['id']}: MCQ without four options")
    if problems:
        raise SystemExit('Validation failed:\n  ' + '\n  '.join(problems[:20]))

    chapters = []
    for num in sorted(LESSONS):
        title, start = LESSONS[num]
        qs = [q for q in items if q['chapter'] == num]
        next_starts = [s for n, (_, s) in LESSONS.items() if s > start]
        end = (min(next_starts) - 1) if next_starts else 180
        chapters.append({
            'number': num,
            'title': title,
            'startPage': start + OFFSET,
            'endPage': end + OFFSET,
            'bookStart': start,
            'bookEnd': end,
            'totalQuestions': len(qs),
            'questions': qs,
        })

    pages = {
        f'page_{i:03d}': f'/books/class_xi/urdu_gulzar/pages/page_{i:03d}.webp'
        for i in range(1, TOTAL_PAGES + 1)
    }

    out = {
        'subject': 'Gulzar-E-Urdu',
        'grade': 'Class XI',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': TOTAL_PAGES,
        'totalChapters': len(chapters),
        'totalQuestionsSolved': len(items),
        'chapters': chapters,
        'pages': pages,
    }

    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f'Built {OUT}: {len(items)} items, {len(chapters)} chapters')
    for c in chapters:
        print(f"  L{c['number']:02d} {c['title']}: {c['totalQuestions']} items "
              f"(book {c['bookStart']}-{c['bookEnd']})")


if __name__ == '__main__':
    main()
