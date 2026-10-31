# Render Class XI Urdu textbooks to page images.
#   Gulzar-E-Urdu XI (192 pp) -> public/books/class_xi/urdu_gulzar/pages/page_XXX.webp
#   Asan Urdu XI      (88 pp)  -> public/books/class_xi/asan_urdu_xi/pages/page_XXX.webp
import io
import os

import fitz
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'Books and Solutions', 'Class XI')

BOOKS = [
    ('Gulzar-E-Urdu XI.pdf', os.path.join(ROOT, 'public', 'books', 'class_xi', 'urdu_gulzar', 'pages')),
    ('Asan Urdu XI.pdf', os.path.join(ROOT, 'public', 'books', 'class_xi', 'asan_urdu_xi', 'pages')),
]


def render(pdf_name, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(os.path.join(SRC, pdf_name))
    total = len(doc)
    print(f'{pdf_name}: {total} pages -> {out_dir}')
    for i in range(total):
        out_path = os.path.join(out_dir, f'page_{i + 1:03d}.webp')
        if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
            continue
        pix = doc[i].get_pixmap(dpi=150)
        img = Image.open(io.BytesIO(pix.tobytes('jpg')))
        img.save(out_path, format='WEBP', quality=85, method=4)
        if (i + 1) % 20 == 0 or i + 1 == total:
            print(f'  [{i + 1}/{total}]')
    doc.close()


if __name__ == '__main__':
    for name, out in BOOKS:
        render(name, out)
    print('Done.')
