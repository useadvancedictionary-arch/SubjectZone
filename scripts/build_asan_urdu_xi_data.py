#!/usr/bin/env python3
"""Build public/data/class_xi_asan_urdu.json (Asan Urdu XI).

Book: Sindh Textbook Board, Jamshoro — 88 PDF pages, book page = PDF page.
Cover title reads آسان اردو گیارہویں جماعت کے لیے.
24 lesson chapters; pages 5-88 all contain lessons with مشق exercises.

Solved fragments: scripts/asan_urdu_xi_parts/lessons_*.json.
"""
import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, 'scripts', 'asan_urdu_xi_parts')
OUT = os.path.join(ROOT, 'public', 'data', 'class_xi_asan_urdu.json')

TOTAL_PAGES = 88
OFFSET = 0

LESSONS = {
    1: ('حمد', 5), 2: ('نبی کریم ﷺ کی ہجرت', 8),
    3: ('نام وہ ادبیوں کے خطوط', 12), 4: ('حبِ وطن', 16),
    5: ('جیسی کرنی ویسی بھرنی', 19), 6: ('ایران کا بادشاہ', 23),
    7: ('آدمی نامہ', 26), 8: ('نصوح کا خواب', 29),
    9: ('اسلامی حکومت کا امیر سب کا خادم ہوتا ہے', 33),
    10: ('آسمان اور تارے', 36), 11: ('سب سے بڑا اسلامی شاعر', 38),
    12: ('چچا کبر', 40), 13: ('رباعیات', 47),
    14: ('ایک وصیت کی تعمیل', 51),
    15: ('پاکستان کے لیے پہلا جہاد', 56),
    16: ('طالبِ علموں کے نام سرسید کا ایک خط', 60),
    17: ('مردِ مجاہد', 63), 18: ('اردو کی آخری کتاب', 66),
    19: ('مولانا محمد علی جوہر', 69), 20: ('آمدِ بہار', 73),
    21: ('اردو کی کہانی', 76), 22: ('حضرت صدیق اکبرؓ ایک شاعر', 79),
    23: ('اسلامی کردار دار', 81), 24: ('میر معصوم شاہ بکھری', 85),
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
        next_starts = [s for n, (_, s) in LESSONS.items() if s > start]
        end = (min(next_starts) - 1) if next_starts else 88
        chapters.append({
            'number': num,
            'title': title,
            'startPage': start + OFFSET,
            'endPage': end + OFFSET,
            'bookStart': start,
            'bookEnd': end,
            'totalQuestions': len([q for q in items if q['chapter'] == num]),
            'questions': [q for q in items if q['chapter'] == num],
        })

    pages = {
        f'page_{i:03d}': f'/books/class_xi/asan_urdu_xi/pages/page_{i:03d}.webp'
        for i in range(1, TOTAL_PAGES + 1)
    }

    out = {
        'subject': 'Asan Urdu XI',
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
        print(f"  L{c['number']:02d} {c['title']}: {c['totalQuestions']} items")


if __name__ == '__main__':
    main()
