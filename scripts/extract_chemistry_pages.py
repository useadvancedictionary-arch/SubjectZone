import os
import io
import fitz
from PIL import Image

def extract_chemistry_pages():
    pdf_path = r'd:\SubjectZone\Books and Solutions\Class X\Chemsitry X.pdf'
    output_dir = r'd:\SubjectZone\public\books\class_x\chemistry\pages'
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Opening Chemistry PDF: {pdf_path}")
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    print(f"Total pages to extract: {total_pages}")
    
    for i in range(total_pages):
        page_num = i + 1
        out_filename = f"page_{page_num:03d}.webp"
        out_path = os.path.join(output_dir, out_filename)
        
        if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
            if page_num % 20 == 0 or page_num == total_pages:
                print(f"Page {page_num}/{total_pages} already exists, skipping.")
            continue
            
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        jpg_bytes = pix.tobytes("jpg")
        
        img = Image.open(io.BytesIO(jpg_bytes))
        img.save(out_path, format="WEBP", quality=85, method=4)
        
        if page_num % 10 == 0 or page_num == total_pages:
            print(f"Extracted page {page_num}/{total_pages} -> {out_filename} ({os.path.getsize(out_path):,} bytes)")

    print("Chemistry page extraction completed successfully!")

if __name__ == '__main__':
    extract_chemistry_pages()
