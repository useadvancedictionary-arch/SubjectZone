# Render all 152 pages of Gulzar-E-Urdu Class XII PDF to WebP images.
# Output: D:\SubjectZone\public\books\class_xii\urdu\pages\page_XXX.webp
import os, io, fitz
from PIL import Image

pdf_path = r'D:\SubjectZone\Books and Solutions\Class XII\Gulzar-E-Urdu XII.pdf'
output_dir = r'D:\SubjectZone\public\books\class_xii\urdu\pages'
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
total = len(doc)
print(f"Rendering {total} pages at 150 DPI ...")

for i in range(total):
    page = doc[i]
    pix = page.get_pixmap(dpi=150)
    out_path = os.path.join(output_dir, f"page_{i+1:03d}.webp")
    # PyMuPDF doesn't support WebP directly; convert via JPG intermediate
    jpg_bytes = pix.tobytes("jpg")
    img = Image.open(io.BytesIO(jpg_bytes))
    img.save(out_path, format="WEBP", quality=85, method=4)
    if (i + 1) % 20 == 0 or (i + 1) == total:
        print(f"  [{i+1}/{total}] done")

doc.close()
print(f"Done. {total} WebP pages written to {output_dir}")
