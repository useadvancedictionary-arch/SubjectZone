#!/usr/bin/env python3
"""Renders Sindhi Lazmi XII PDF pages to WebP for the SubjectZone app.

Sindhi Lazmi XII for Class XII (Sindh Textbook Board, Jamshoro):
248 PDF pages rendered to WebP at 150 DPI.
Output: public/books/class_xii/sindhi/pages/
"""
import os
import io
import fitz
from PIL import Image

def extract_all_pages():
    pdf_path = r'D:\SubjectZone\Books and Solutions\Class XII\Sindhi Lazmi XII.pdf'
    output_dir = r'D:\SubjectZone\public\books\class_xii\sindhi\pages'
    os.makedirs(output_dir, exist_ok=True)

    print(f"Opening PDF: {pdf_path}")
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    print(f"Total pages to extract: {total_pages}")

    for i in range(total_pages):
        page_num = i + 1
        out_filename = f"page_{page_num:03d}.webp"
        out_path = os.path.join(output_dir, out_filename)

        # Check if already extracted and valid size
        if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
            if page_num % 20 == 0 or page_num == total_pages:
                print(f"Page {page_num}/{total_pages} already exists, skipping.")
            continue

        page = doc[i]
        # 150 DPI gives razor-sharp clarity for textbook typography and diagrams
        pix = page.get_pixmap(dpi=150)
        jpg_bytes = pix.tobytes("jpg")

        img = Image.open(io.BytesIO(jpg_bytes))
        img.save(out_path, format="WEBP", quality=85, method=4)

        if page_num % 10 == 0 or page_num == total_pages:
            print(f"Extracted page {page_num}/{total_pages} -> {out_filename} ({os.path.getsize(out_path):,} bytes)")

    print("Page extraction completed successfully!")

if __name__ == '__main__':
    extract_all_pages()
