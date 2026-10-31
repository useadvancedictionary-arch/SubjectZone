import os, subprocess

TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
PAGES = "D:/SubjectZone/public/books/class_ix/sindhi_lazmi/pages"
OUT = "D:/SubjectZone/public/books/class_ix/sindhi_lazmi/ocr"
os.makedirs(OUT, exist_ok=True)

files = sorted(f for f in os.listdir(PAGES) if f.endswith(".png"))
print("pages:", len(files))
for i, f in enumerate(files):
    stem = f[:-4]
    out_txt = os.path.join(OUT, stem + ".txt")
    if os.path.exists(out_txt) and os.path.getsize(out_txt) > 0:
        continue
    subprocess.run([TESS, os.path.join(PAGES, f), "stdout", "-l", "snd", "--psm", "6"],
                   capture_output=True, text=True, encoding="utf-8")
    # rerun capturing to file via temp
    r = subprocess.run([TESS, os.path.join(PAGES, f), os.path.join(OUT, stem), "-l", "snd", "--psm", "6"],
                       capture_output=True, text=True)
    if (i + 1) % 25 == 0:
        print(f"OCR'd {i+1}/{len(files)}")
print("done")
