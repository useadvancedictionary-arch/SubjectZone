"""
SubjectZone - MCQ Answer Highlight Extraction
Locates each MCQ's correct option on the book page (via OCR at 200 DPI) and
stores a normalized answerRect {x, y, w, h} (0-1 fractions of page size) on
each MCQ question in public/data/class_x_<subject>.json.

For questions whose options are printed on the previous/next page (page-spanning
layout), the question's pdfPage is remapped to the page where its options are
printed, so panel grouping matches the printed book. pagesMap is rebuilt from
chapters afterwards (it is fully derived data).

Run:  python scripts/extract_answer_highlights.py [--debug] [--subject biology|physics|chemistry]

--debug also writes annotated preview images to scripts/debug_highlights/.
"""
import os
import re
import sys
import json
import difflib
from PIL import Image, ImageDraw

import fitz
from rapidocr_onnxruntime import RapidOCR

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = {
    'biology': os.path.join(BASE, 'Books and Solutions', 'Class X', 'Biology X.pdf'),
    'physics': os.path.join(BASE, 'Books and Solutions', 'Class X', 'Physics X.pdf'),
    'chemistry': os.path.join(BASE, 'Books and Solutions', 'Class X', 'Chemsitry X.pdf'),
}
DATA_FILES = {
    'biology': os.path.join(BASE, 'public', 'data', 'class_x_biology.json'),
    'physics': os.path.join(BASE, 'public', 'data', 'class_x_physics.json'),
    'chemistry': os.path.join(BASE, 'public', 'data', 'class_x_chemistry.json'),
}
DEBUG_DIR = os.path.join(BASE, 'scripts', 'debug_highlights')

OCR_DPI = 200
PAD_PX = 10          # padding around matched boxes at OCR_DPI
LINE_TOL_PX = 14     # vertical tolerance for "same text line"
LETTER = 'abcd'
ROMAN = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii',
         8: 'viii', 9: 'ix', 10: 'x', 11: 'xi', 12: 'xii', 13: 'xiii',
         14: 'xiv', 15: 'xv', 16: 'xvi', 17: 'xvii', 18: 'xviii', 19: 'xix', 20: 'xx'}

ocr_engine = None


def get_ocr():
    global ocr_engine
    if ocr_engine is None:
        ocr_engine = RapidOCR()
    return ocr_engine


def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())


def similarity(a, b):
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


# ---------------------------------------------------------------- OCR layer

class PageOCR:
    """Caches OCR boxes per PDF page."""

    def __init__(self, doc):
        self.doc = doc
        self.cache = {}

    def get(self, page_idx):
        if page_idx in self.cache:
            return self.cache[page_idx]
        page = self.doc[page_idx]
        pix = page.get_pixmap(dpi=OCR_DPI)
        result, _ = get_ocr()(pix.tobytes('png'))
        boxes = []
        if result:
            for item in result:
                box, text = item[0], item[1]
                xs = [p[0] for p in box]
                ys = [p[1] for p in box]
                boxes.append({'x0': float(min(xs)), 'y0': float(min(ys)),
                              'x1': float(max(xs)), 'y1': float(max(ys)),
                              'text': str(text).strip()})
        boxes.sort(key=lambda b: (b['y0'], b['x0']))
        self.cache[page_idx] = (boxes, pix.width, pix.height)
        return self.cache[page_idx]


# ------------------------------------------------------- pattern helpers

def question_patterns(qnum, subject):
    pats = [f'{qnum}.', f'{qnum})', f'({qnum})', f'{qnum},']
    if qnum in ROMAN:
        r = ROMAN[qnum]
        pats += [f'{r})', f'{r}.', f'({r})', f'{r},']
    return pats


def letter_patterns(ch):
    return [f'{ch})', f'{ch}.', f'({ch})', f'{ch},']


def box_matches_prefix(box, prefix):
    t = box['text'].lower().strip()
    if not t:
        return False
    if t == prefix:
        return True
    if t.startswith(prefix):
        rest = t[len(prefix):]
        return rest[:1] in (' ', '', '.', ')')
    return False


def is_letter_box(box):
    t = box['text'].lower().strip()
    for ch in LETTER:
        for p in letter_patterns(ch):
            if t == p:
                return ch
    return None


def letter_prefix_of(box):
    """Letter of an option box: exact label ('b)', 'C.') or glued ('(b) text')."""
    ch = is_letter_box(box)
    if ch:
        return ch
    t = box['text'].lower().strip()
    for c in LETTER:
        for p in letter_patterns(c):
            if t.startswith(p) and len(t) > len(p) and t[len(p)] == ' ':
                return c
    return None


def letter_of(correct_answer):
    m = re.match(r'^\s*\(?([a-dA-D])[\).\]:\s]', correct_answer)
    if m:
        return m.group(1).lower()
    m = re.match(r'^\s*\(?([a-dA-D])\)?\s*$', correct_answer)
    if m:
        return m.group(1).lower()
    return None


def answer_text_of(answer):
    """correctAnswer minus a leading option-letter label."""
    m = re.match(r'^\s*\(?[a-dA-D][\)\.\]:,]\s*', answer)
    if m:
        return answer[m.end():]
    m = re.match(r'^\s*\(?[a-dA-D]\)?\s+', answer)
    if m:
        return answer[m.end():]
    return answer


def rect_text(boxes, rect):
    """OCR text of the boxes that fall inside the rect."""
    hits = [b for b in boxes
            if b['x0'] < rect['x1'] and b['x1'] > rect['x0']
            and b['y0'] < rect['y1'] and b['y1'] > rect['y0']]
    return ' '.join(b['text'] for b in sorted(hits, key=lambda b: (b['y0'], b['x0'])))


def verify_rect_text(boxes, rect, answer):
    """Guard against wrong-question matches: the OCR text inside the rect must
    resemble the expected answer text. Used whenever the anchor was weak or
    absent, so a question that is not printed in the book can never get a rect."""
    at = norm(answer_text_of(answer))
    if not at:
        return True
    rt = norm(rect_text(boxes, rect))
    if not rt:
        return False
    if len(at) <= 3:
        return similarity(at, rt) >= 0.6
    return at in rt or similarity(at, rt) >= 0.55


def answer_present_on_page(boxes, answer):
    """True if the expected answer text is legibly somewhere on the page. A
    strong anchor whose answer text appears nowhere means the anchor matched the
    wrong question (or the question is not printed here) — do not highlight.
    Compound answers ('X / Y') are accepted if any part is present, since the
    rect usually covers only one part."""
    raw = answer_text_of(answer)
    parts = [p.strip() for p in raw.split('/') if p.strip()] or [raw]
    page_nt = norm(' '.join(b['text'] for b in boxes))

    def present(text):
        at = norm(text)
        if len(at) < 12:
            return True  # too short / bare letter to require page-wide evidence
        if at in page_nt:
            return True
        return any(len(norm(b['text'])) >= 8 and similarity(at, norm(b['text'])) >= 0.55
                   for b in boxes)

    return any(present(p) for p in parts)


# ------------------------------------------------------- anchor detection

def find_question_anchor(boxes, q, subject):
    """Returns (anchor_box, confidence_score) — score < 0.45 means weak match."""
    qnum = q.get('number')
    qtext = norm(q.get('question', ''))[:40]

    cands = []
    if qnum is not None:
        pats = question_patterns(qnum, subject)
        for b in boxes:
            for p in pats:
                if box_matches_prefix(b, p):
                    cands.append(b)
                    break

    def text_below(box):
        y0 = box['y0']
        parts = [b['text'] for b in boxes
                 if -LINE_TOL_PX <= b['y0'] - y0 < 130 and b['x0'] >= box['x0'] - 260]
        return norm(' '.join(parts))[:60]

    best, best_score = None, 0.0
    for c in cands:
        score = similarity(text_below(c), qtext)
        if score > best_score:
            best, best_score = c, score
    if best and best_score >= 0.45:
        return best, best_score
    if len(cands) == 1 and best_score >= 0.30:
        return cands[0], best_score

    # text-similarity fallback (short questions need a near-exact match)
    min_thresh = 0.60 if len(qtext) >= 10 else 0.85
    best, best_score = None, 0.0
    for b in boxes:
        bt = norm(b['text'])[:40]
        if len(bt) < 4:
            continue
        score = similarity(bt, qtext)
        if score > best_score:
            best, best_score = b, score
    if best and best_score >= min_thresh:
        return best, best_score
    return None, 0.0


def all_number_anchors(boxes, numbers, subject):
    anchors = []
    for n in numbers:
        for p in question_patterns(n, subject):
            for b in boxes:
                if box_matches_prefix(b, p):
                    anchors.append(b)
    return anchors


# ------------------------------------------------------- option location

def same_line_boxes(boxes, y_center, tol=LINE_TOL_PX):
    return [b for b in boxes
            if abs((b['y0'] + b['y1']) / 2 - y_center) <= tol]


def normalize_rect(rect, pw, ph):
    rect['x0'] = max(0, rect['x0']); rect['y0'] = max(0, rect['y0'])
    rect['x1'] = min(pw, rect['x1']); rect['y1'] = min(ph, rect['y1'])
    w, h = rect['x1'] - rect['x0'], rect['y1'] - rect['y0']
    if w <= 8 or h <= 8:
        return None
    return {'x': round(rect['x0'] / pw, 4), 'y': round(rect['y0'] / ph, 4),
            'w': round(w / pw, 4), 'h': round(h / ph, 4)}


def is_section_heading(box, region):
    """Standalone uppercase letter-label ('A.', 'B.') that heads an ALL-CAPS
    section title on the same line (e.g. 'B. SHORT QUESTIONS:') — not an MCQ
    option. Must be filtered out of the region before letter matching."""
    if not re.fullmatch(r'[A-D][\.\)]', box['text'].strip()):
        return False
    yc = (box['y0'] + box['y1']) / 2
    for b in region:
        if b is box or b['x0'] <= box['x1']:
            continue
        if abs((b['y0'] + b['y1']) / 2 - yc) > LINE_TOL_PX:
            continue
        letters = [c for c in b['text'] if c.isalpha()]
        if len(letters) >= 3 and all(c.isupper() for c in letters):
            return True
    return False


def letter_box_in_region(region, letter):
    """Find the box that labels `letter` (exact label or letter+text glued)."""
    for b in region:
        if is_letter_box(b) == letter:
            return b
    for b in region:
        t = b['text'].lower().strip()
        for p in letter_patterns(letter):
            if t.startswith(p) and len(t) > len(p):
                return b
    return None


def rect_from_letter_box(box, region):
    """Expand a letter box along its line to cover the option text."""
    if len(box['text'].strip()) > 3:
        return {'x0': box['x0'] - PAD_PX, 'y0': box['y0'] - PAD_PX,
                'x1': box['x1'] + PAD_PX, 'y1': box['y1'] + PAD_PX}
    y_center = (box['y0'] + box['y1']) / 2
    line = sorted(same_line_boxes(region, y_center), key=lambda b: b['x0'])
    x1 = box['x1']
    for b in line:
        if b['x0'] <= box['x1']:
            continue
        ch = is_letter_box(b)
        if ch and ch != letter_of_box(box):
            break
        if any(box_matches_prefix(b, p) for ch2 in LETTER
               for p in letter_patterns(ch2)):
            break
        x1 = max(x1, b['x1'])
    row = [b for b in line if b['x0'] >= box['x0'] - LINE_TOL_PX]
    y0m = min([b['y0'] for b in row] or [box['y0']])
    y1m = max([b['y1'] for b in row] or [box['y1']])
    return {'x0': box['x0'] - PAD_PX, 'y0': min(y0m, box['y0']) - PAD_PX,
            'x1': x1 + PAD_PX, 'y1': max(y1m, box['y1']) + PAD_PX}


def letter_of_box(box):
    t = box['text'].lower().strip()
    for ch in LETTER:
        for p in letter_patterns(ch):
            if t == p or t.startswith(p):
                return ch
    return None


def interpolated_rect(region, anchor, letter):
    """Estimate the correct option's line from sibling option letters."""
    found = {}
    for b in region:
        ch = letter_prefix_of(b)
        if ch and ch not in found:
            found[ch] = b
    if len(found) < 2:
        return None
    ys = {ch: (b['y0'] + b['y1']) / 2 for ch, b in found.items()}
    idx = LETTER.index(letter)
    before = [c for c in LETTER if c in ys and LETTER.index(c) < idx]
    after = [c for c in LETTER if c in ys and LETTER.index(c) > idx]
    if not before or not after:
        return None
    y0, y1 = ys[before[-1]], ys[after[0]]
    n = LETTER.index(after[0]) - LETTER.index(before[-1])
    if n <= 0:
        return None
    est = y0 + (y1 - y0) * (idx - LETTER.index(before[-1])) / n
    line = [b for b in same_line_boxes(region, est, tol=18) if not letter_prefix_of(b)]
    if not line:
        return None
    return {'x0': min(b['x0'] for b in line) - PAD_PX,
            'y0': min(b['y0'] for b in line) - PAD_PX,
            'x1': max(b['x1'] for b in line) + PAD_PX,
            'y1': max(b['y1'] for b in line) + PAD_PX}


def grid_missing_rect(region, letter, region_top, region_bottom):
    """Two-column option grids: infer the missing letter's cell from siblings
    (row taken from the same-row letter, column from the same-column letter)."""
    found = {}
    for b in region:
        ch = letter_prefix_of(b)
        if ch and ch not in found:
            found[ch] = b
    if letter in found or len(found) < 2:
        return None

    def yc(b):
        return (b['y0'] + b['y1']) / 2

    two_col = any(
        abs(yc(found[c1]) - yc(found[c2])) <= LINE_TOL_PX and
        (found[c1]['x1'] < found[c2]['x0'] - 20 or
         found[c2]['x1'] < found[c1]['x0'] - 20)
        for c1 in found for c2 in found if c1 < c2)
    if not two_col:
        return None

    idx = LETTER.index(letter)
    row_mate = found.get(LETTER[idx ^ 1])
    col_mate = found.get(LETTER[(idx + 2) % 4])
    if col_mate is None:
        return None
    if row_mate:
        y0, y1 = row_mate['y0'], row_mate['y1']
    else:
        # whole row missed: extrapolate one row from the nearest known row
        row_h = None
        if idx <= 1:
            ref = min(found.values(), key=lambda b: b['y0'])
            row_h = ref['y1'] - ref['y0']
            y1 = ref['y0'] - 6
            y0 = y1 - row_h
            if y0 < region_top - PAD_PX:
                return None
        else:
            ref = max(found.values(), key=lambda b: b['y1'])
            row_h = ref['y1'] - ref['y0']
            y0 = ref['y1'] + 6
            y1 = y0 + row_h
            if y1 > region_bottom + PAD_PX:
                return None
    return {'x0': col_mate['x0'] - PAD_PX, 'x1': col_mate['x1'] + PAD_PX,
            'y0': y0 - PAD_PX, 'y1': y1 + PAD_PX}


def answer_text_rect(region, answer):
    """Fallback for rows where the letter label was misread by OCR
    (e.g. '(d)' -> '(p'): match the expected answer text against option
    lines in the region and highlight the best match's whole line."""
    at = norm(answer_text_of(answer))
    if len(at) < 4:
        return None
    best, best_score = None, 0.0
    for b in region:
        if letter_prefix_of(b):
            continue
        bt = norm(b['text'])
        if len(bt) < 4:
            continue
        score = similarity(bt, at)
        if score > best_score:
            best, best_score = b, score
    if best is None or best_score < 0.75:
        return None
    yc = (best['y0'] + best['y1']) / 2
    line = [b for b in region if abs((b['y0'] + b['y1']) / 2 - yc) <= LINE_TOL_PX]
    return {'x0': min(b['x0'] for b in line) - PAD_PX,
            'y0': min(b['y0'] for b in line) - PAD_PX,
            'x1': max(b['x1'] for b in line) + PAD_PX,
            'y1': max(b['y1'] for b in line) + PAD_PX}


def standalone_letter_rect(region, boxes, letter, answer):
    """Diagram-style MCQs: options are bare letters (usually uppercase A-D)."""
    bare = [b for b in region if b['text'].strip() in (letter, letter.upper())]
    if not bare:
        return None
    exact_case = [b for b in bare
                  if b['text'].strip() == (letter.upper() if answer[0].isupper() else letter)]
    target = exact_case or bare
    box = sorted(target, key=lambda b: b['y0'])[0]
    y_center = (box['y0'] + box['y1']) / 2
    line = sorted(same_line_boxes(boxes, y_center), key=lambda b: b['x0'])
    x1 = box['x1']
    for b in line:
        if b['x0'] > box['x1']:
            x1 = max(x1, b['x1'])
    return {'x0': box['x0'] - PAD_PX * 2, 'y0': box['y0'] - PAD_PX * 2,
            'x1': x1 + PAD_PX * 2, 'y1': box['y1'] + PAD_PX * 2}


def find_option_rect(boxes, anchor, letter, region_bottom, answer):
    """Returns (rect, method) — method tells how confident the match is."""
    region_top = anchor['y1'] - LINE_TOL_PX
    region = [b for b in boxes if region_top <= b['y0'] <= region_bottom]
    region = [b for b in region if not is_section_heading(b, region)]

    box = letter_box_in_region(region, letter)
    if box:
        rect = rect_from_letter_box(box, region)
        if verify_rect_text(boxes, rect, answer):
            return rect, 'letter'
        # The letter label matched but the option text does not — the region
        # likely bled into a neighbouring question, or OCR lost the option's
        # paren (e.g. '(c) Hormones' -> 'C Hormones'). Try a direct answer-text
        # match before falling back to the letter box.
        trect = answer_text_rect(region, answer)
        if trect:
            return trect, 'text'
        return rect, 'letter'

    rect = interpolated_rect(region, anchor, letter)
    if rect:
        return rect, 'interpolated'

    rect = grid_missing_rect(region, letter, region_top, region_bottom)
    if rect:
        return rect, 'grid'

    rect = answer_text_rect(region, answer)
    if rect:
        return rect, 'text'

    if len(answer.strip()) <= 2:
        return standalone_letter_rect(region, boxes, letter, answer.strip()), 'standalone'
    return None, None


# ------------------------------------------------------- per-question flow

def locate_on_page(pocr, page_idx, q, subject, numbers):
    """Try to locate q's answer rect on this page. Returns rect or None."""
    boxes, pw, ph = pocr.get(page_idx)
    letter = letter_of(q['correctAnswer'])
    anchor, score = find_question_anchor(boxes, q, subject)
    if anchor is not None and letter is not None:
        anchors_all = all_number_anchors(boxes, numbers, subject)
        # Only same-column anchors bound the region; sub-items of the question
        # itself (e.g. 'i. Blurred vision') sit ~100px right of the number
        # column and must not cut the region above the real options.
        below = [a['y0'] for a in anchors_all
                 if a['y0'] > anchor['y1'] + 5
                 and abs(a['x0'] - anchor['x0']) <= 60]
        region_bottom = min(below) if below else ph
        rect, method = find_option_rect(boxes, anchor, letter,
                                        region_bottom, q['correctAnswer'])
        if rect:
            if score >= 0.45:
                if answer_present_on_page(boxes, q['correctAnswer']):
                    return normalize_rect(rect, pw, ph)
                # Strong anchor but the expected answer text is nowhere on this
                # page: the anchor matched the wrong question. Fall through.
            elif method in ('letter', 'standalone') and \
                    verify_rect_text(boxes, rect, q['correctAnswer']):
                # Weak anchor: the question may not be printed here at all.
                # Only direct letter/standalone matches whose text matches the
                # expected answer are trusted; geometric inference is not.
                return normalize_rect(rect, pw, ph)

    if letter is None:
        return None

    # continuation: options at top of page without the question label
    top_region = [b for b in boxes if b['y0'] < ph * 0.35]
    top_region = [b for b in top_region if not is_section_heading(b, top_region)]
    box = letter_box_in_region(top_region, letter)
    if box:
        n_letters = sum(1 for b in top_region if letter_prefix_of(b))
        if n_letters >= 2:
            rect = rect_from_letter_box(box, top_region)
            if verify_rect_text(boxes, rect, q['correctAnswer']):
                return normalize_rect(rect, pw, ph)
    return None


def rebuild_pages_map(data):
    """pagesMap questions are fully derived from chapters[].questions."""
    for pg_str, pm in data['pagesMap'].items():
        qs = [q for ch in data['chapters'] for q in ch['questions']
              if str(q.get('pdfPage')) == pg_str]
        # preserve original ordering by chapter then question order
        pm['questions'] = qs
        pm['hasExercise'] = len(qs) > 0


def draw_debug(pocr, doc, subject, rects_by_page):
    os.makedirs(DEBUG_DIR, exist_ok=True)
    for page_idx, items in rects_by_page.items():
        boxes, pw, ph = pocr.get(page_idx)
        pix = doc[page_idx].get_pixmap(dpi=OCR_DPI)
        img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        draw = ImageDraw.Draw(img)
        for qid, r in items:
            if not r:
                continue
            x0, y0 = r['x'] * pw, r['y'] * ph
            x1, y1 = x0 + r['w'] * pw, y0 + r['h'] * ph
            draw.rectangle([x0, y0, x1, y1], outline=(16, 185, 129), width=4)
        img.save(os.path.join(DEBUG_DIR, f'{subject}_p{page_idx + 1:03d}.jpg'), quality=80)


def run(subject, debug=False):
    data_path = DATA_FILES[subject]
    with open(data_path, encoding='utf-8') as f:
        data = json.load(f)

    doc = fitz.open(BOOKS[subject])
    pocr = PageOCR(doc)

    # all question numbers that can appear on exercise pages (for region bounds)
    all_numbers = sorted({q.get('number') for ch in data['chapters']
                          for q in ch['questions'] if q.get('number') is not None})

    by_page = {}
    for ch in data['chapters']:
        for q in ch['questions']:
            by_page.setdefault(q.get('pdfPage'), []).append(q)

    total = found = remapped = 0
    rects_by_page = {}
    for page_no in sorted(p for p in by_page if p):
        mcqs = [q for q in by_page[page_no] if q.get('type') == 'mcq']
        if not mcqs:
            continue
        page_idx = page_no - 1
        rects_by_page.setdefault(page_idx, [])
        for q in mcqs:
            total += 1
            rect = locate_on_page(pocr, page_idx, q, subject, all_numbers)
            if rect:
                q['answerRect'] = rect
                rects_by_page[page_idx].append((q['id'], rect))
                found += 1
                continue
            # retry neighbouring pages (page-spanning questions)
            for delta in (1, -1, 2, -2):
                n_idx = page_idx + delta
                if not (0 <= n_idx < len(doc)):
                    continue
                rect = locate_on_page(pocr, n_idx, q, subject, all_numbers)
                if rect:
                    q['pdfPage'] = n_idx + 1
                    pm = data['pagesMap'].get(str(n_idx + 1))
                    if pm:
                        q['bookPage'] = pm.get('bookPage', q.get('bookPage'))
                    q['answerRect'] = rect
                    rects_by_page.setdefault(n_idx, []).append((q['id'], rect))
                    found += 1
                    remapped += 1
                    break
            else:
                if 'answerRect' in q:
                    del q['answerRect']
                rects_by_page[page_idx].append((q['id'], None))
        print(f'  page {page_no}: {sum(1 for _, r in rects_by_page[page_idx] if r)}/{len(mcqs)} MCQs located', flush=True)

    rebuild_pages_map(data)

    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    if debug:
        draw_debug(pocr, doc, subject, rects_by_page)

    print(f'{subject}: {found}/{total} MCQs located ({100 * found / max(total, 1):.0f}%), '
          f'{remapped} remapped to neighbour page')


if __name__ == '__main__':
    args = [a.lower() for a in sys.argv[1:]]
    debug = '--debug' in args
    subjects = [a for a in args if a in BOOKS] or ['biology', 'physics', 'chemistry']
    for s in subjects:
        print(f'=== {s} ===', flush=True)
        run(s, debug=debug)
