#!/usr/bin/env python3
"""Render CS XI (Class XI, Sindh board) pages to PNG for visual solving.

PDF: Books and Solutions/Class XI/Computer Science XI.pdf (240 pages)
Output: public/books/class_xi/cs/pages/page_001.png ... page_240.png
Printed page = PDF page - 5.
"""
import os
import fitz

PDF = 'Books and Solutions/Class XI/Computer Science XI.pdf'
OUT = 'public/books/class_xi/cs/pages'
DPI = 140


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
        if (i + 1) % 20 == 0 or i + 1 == total:
            print(f'rendered {i + 1}/{total}', flush=True)
    print('done', flush=True)


if __name__ == '__main__':
    main()
