import fitz, os
pdf_path = "D:/SubjectZone/Books and Solutions/Class IX/My English IX.pdf"
out_dir = "D:/SubjectZone/public/books/class_ix/english/pages"
os.makedirs(out_dir, exist_ok=True)
doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")
for i in range(len(doc)):
    page = doc[i]
    mat = fitz.Matrix(200/72, 200/72)
    pix = page.get_pixmap(matrix=mat)
    pix.save(os.path.join(out_dir, f"page_{i:03d}.png"))
    if (i+1) % 50 == 0:
        print(f"Rendered {i+1}/{len(doc)}")
print(f"Done. Rendered {len(doc)} pages.")
doc.close()
