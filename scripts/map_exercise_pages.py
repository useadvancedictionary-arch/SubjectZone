import fitz
import re

doc = fitz.open(r'd:\SubjectZone\Books and Solutions\Class X\Physics X.pdf')

unit_ranges = [
    (10, "General Wave Properties", 5, 24),
    (11, "Sound", 25, 44),
    (12, "Electromagnetic Spectrum", 45, 60),
    (13, "Geometrical Optics", 61, 89),
    (14, "Electrostatics", 90, 112),
    (15, "Current Electricity", 113, 135),
    (16, "Electromagnetism", 136, 156),
    (17, "Introductory Electronics", 157, 182),
    (18, "Information and Communication Technology (ICT)", 183, 201),
    (19, "Atomic Structure", 202, 211),
    (20, "Nuclear Structure", 212, 242)
]

for u, title, s, e in unit_ranges:
    print(f"\n==========================================")
    print(f"UNIT {u}: {title} (Pages {s} to {e})")
    print(f"==========================================")
    for p in range(s, e + 1):
        txt = doc[p - 1].get_text()
        has_mcq = bool(re.search(r'Multiple Choice|Section\s*\(?\s*A\s*\)?', txt, re.I))
        has_sq = bool(re.search(r'Structured|Short Question|Section\s*\(?\s*B\s*\)?', txt, re.I))
        has_num = bool(re.search(r'Numerical|Section\s*\(?\s*C\s*\)?', txt, re.I))
        has_self = bool(re.search(r'Self-Assessment|Self Assessment', txt, re.I))
        
        # Check if this page is in the last 6 pages of the unit or contains exercises
        if has_mcq or has_sq or has_num or has_self or p >= e - 3:
            first_lines = [l.strip() for l in txt.split('\n') if l.strip()][:4]
            print(f"  PDF Page {p} (Book {p-4}): MCQ={has_mcq}, SQ={has_sq}, Num={has_num}, Self={has_self} | {first_lines}")
