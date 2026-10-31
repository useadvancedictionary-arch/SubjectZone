#!/usr/bin/env python3
"""Render Math XI (Class XI, Sindh board) pages to PNG for page-image solving.

PDF: Books and Solutions/Class XI/Math XI.pdf (424 pages)
Output: public/books/class_xi/math/pages/page_001.png ... page_424.png
Printed page = PDF page - 4.
"""
import os
import fitz
from PIL import Image

PDF = 'Books and Solutions/Class XI/Math XI.pdf'
OUT = 'public/books/class_xi/math/pages'
DPI = 140

# These PDF pages scan upside down (8-page signatures, detected via text
# direction); rotate them so every rendered page is upright.
UPSIDE_DOWN = {
    85, 86, 87, 88, 89, 90, 91, 92,
    101, 102, 103, 104, 105, 106, 107, 108,
    117, 118, 119, 120, 121, 122, 123, 124,
    133, 134, 135, 136, 137, 138, 139, 140,
    149, 150, 151, 152, 153, 154, 155, 156, 160,
    245, 246, 247, 248, 249, 250, 251, 252,
    261, 262, 263, 264, 265, 266, 267,
    277, 278, 279, 280, 281, 282, 283, 284,
    293, 294, 295, 296, 297, 298, 299, 300,
    309, 310, 311, 312, 313, 314, 315, 316,
}


def main():
    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(PDF)
    total = len(doc)
    print(f'{total} pages -> {OUT}', flush=True)
    for i in range(total):
        path = os.path.join(OUT, f'page_{i + 1:03d}.png')
        if os.path.exists(path) and os.path.getsize(path) > 5000:
            continue
        pix = doc[i].get_pixmap(matrix=fitz.Matrix(DPI / 72, DPI / 72))
        pix.save(path)
        if i + 1 in UPSIDE_DOWN:
            im = Image.open(path)
            im.rotate(180, expand=False).save(path)
        if (i + 1) % 20 == 0 or i + 1 == total:
            print(f'rendered {i + 1}/{total}', flush=True)
    print('done', flush=True)


if __name__ == '__main__':
    main()
