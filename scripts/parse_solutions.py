import zipfile
import xml.etree.ElementTree as ET
import json
import re
import os

def parse_docx_and_map():
    docx_path = r'd:\SubjectZone\Books and Solutions\Class X\Biology_X_Complete_Solutions.docx'
    output_path = r'd:\SubjectZone\public\data\class_x_biology.json'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        paragraphs = []
        for p in tree.iterfind('.//w:p', ns):
            texts = [t.text for t in p.iterfind('.//w:t', ns) if t.text]
            if texts:
                paragraphs.append(''.join(texts).strip())

    chapters_raw = {}
    current_ch = None
    for p in paragraphs:
        m = re.match(r'Chapter\s+(\d+):\s*(.*)', p, re.I)
        if m:
            current_ch = int(m.group(1))
            chapters_raw[current_ch] = {'title': m.group(2).strip(), 'paras': []}
        elif current_ch is not None:
            chapters_raw[current_ch]['paras'].append(p)

    # Chapters metadata with PDF page bounds
    chapter_meta = {
        1: {"title": "Gaseous Exchange", "startPage": 6, "endPage": 20, "bookStart": 1, "bookEnd": 15},
        2: {"title": "Homeostasis", "startPage": 21, "endPage": 44, "bookStart": 16, "bookEnd": 39},
        3: {"title": "Coordination and Control", "startPage": 45, "endPage": 71, "bookStart": 40, "bookEnd": 65},
        4: {"title": "Support and Movement", "startPage": 72, "endPage": 88, "bookStart": 66, "bookEnd": 82},
        5: {"title": "Reproduction", "startPage": 89, "endPage": 110, "bookStart": 83, "bookEnd": 104},
        6: {"title": "Inheritance", "startPage": 111, "endPage": 138, "bookStart": 105, "bookEnd": 132},
        7: {"title": "Man and His Environment", "startPage": 139, "endPage": 173, "bookStart": 133, "bookEnd": 167},
        8: {"title": "Biotechnology", "startPage": 174, "endPage": 190, "bookStart": 168, "bookEnd": 184},
        9: {"title": "Pharmacology", "startPage": 191, "endPage": 203, "bookStart": 185, "bookEnd": 197}
    }

    # Exercise page mapping rules per chapter
    # (ch_num, section_type, q_num) -> (pdf_page, book_page)
    def get_page_for_question(ch, sec_type, q_num):
        if ch == 1:
            if sec_type == 'mcq' and q_num <= 8:
                return (19, 14)
            return (20, 15)
        elif ch == 2:
            if sec_type == 'mcq':
                return (43, 38)
            return (44, 39)
        elif ch == 3:
            if sec_type == 'mcq' and q_num <= 11:
                return (70, 64)
            return (71, 65)
        elif ch == 4:
            if sec_type == 'mcq':
                return (87, 81)
            return (88, 82)
        elif ch == 5:
            if sec_type == 'mcq' and q_num <= 5:
                return (109, 103)
            return (110, 104)
        elif ch == 6:
            if sec_type == 'mcq':
                return (136, 130)
            elif sec_type == 'sq':
                return (137, 131)
            return (138, 132)
        elif ch == 7:
            if sec_type == 'mcq':
                return (172, 166)
            return (173, 167)
        elif ch == 8:
            if sec_type == 'mcq':
                return (189, 183)
            return (190, 184)
        elif ch == 9:
            if sec_type == 'mcq':
                return (202, 196)
            return (203, 197)
        return (chapter_meta[ch]["endPage"], chapter_meta[ch]["bookEnd"])

    parsed_chapters = []
    total_q_count = 0

    for ch_num in sorted(chapters_raw.keys()):
        meta = chapter_meta[ch_num]
        paras = chapters_raw[ch_num]['paras']
        
        current_section = None
        questions = []
        
        i = 0
        while i < len(paras):
            p = paras[i]
            
            # Check for section headers
            if 'multiple choice questions' in p.lower():
                current_section = 'mcq'
                i += 1
                continue
            elif 'short questions' in p.lower():
                current_section = 'sq'
                i += 1
                continue
            elif 'extensive response questions' in p.lower():
                current_section = 'erq'
                i += 1
                continue
            elif 'answer the following questions' in p.lower():
                current_section = 'sq' # In Ch 8, Section B
                i += 1
                continue

            # Question detector
            q_match = re.match(r'Q(\d+)\.\s*(.*)', p)
            if q_match and current_section:
                q_num = int(q_match.group(1))
                q_text = q_match.group(2).strip()
                pdf_pg, book_pg = get_page_for_question(ch_num, current_section, q_num)
                
                if current_section == 'mcq':
                    options_str = ""
                    correct_ans = ""
                    explanation = ""
                    
                    # Next paragraph is usually options
                    if i + 1 < len(paras) and re.search(r'\([a-d]\)', paras[i+1], re.I):
                        i += 1
                        options_str = paras[i]
                    
                    # Next paragraph is correct answer
                    if i + 1 < len(paras) and paras[i+1].startswith('Correct Answer:'):
                        i += 1
                        correct_ans = paras[i].replace('Correct Answer:', '').strip()
                        
                    # Next paragraph is explanation
                    if i + 1 < len(paras) and paras[i+1].startswith('Explanation:'):
                        i += 1
                        explanation = paras[i].replace('Explanation:', '').strip()
                        
                    # Parse options array
                    # Format: (a) Text (b) Text (c) Text (d) Text
                    opt_matches = re.findall(r'\(([a-d])\)\s*([^(\n]+)', options_str)
                    options = [{"key": k.lower(), "text": t.strip()} for k, t in opt_matches]
                    
                    questions.append({
                        "id": f"ch{ch_num}_mcq_{q_num}",
                        "chapter": ch_num,
                        "section": "Multiple Choice Questions",
                        "sectionCode": "A",
                        "type": "mcq",
                        "number": q_num,
                        "question": q_text,
                        "options": options,
                        "optionsRaw": options_str,
                        "correctAnswer": correct_ans,
                        "explanation": explanation,
                        "pdfPage": pdf_pg,
                        "bookPage": book_pg
                    })
                    total_q_count += 1
                    
                else: # 'sq' or 'erq'
                    sec_name = "Short Questions" if current_section == 'sq' else "Extensive Response Questions"
                    sec_code = "B" if current_section == 'sq' else "C"
                    answer_text = ""
                    
                    if i + 1 < len(paras) and paras[i+1].startswith('Answer:'):
                        i += 1
                        answer_text = paras[i].replace('Answer:', '').strip()
                        
                    questions.append({
                        "id": f"ch{ch_num}_{current_section}_{q_num}",
                        "chapter": ch_num,
                        "section": sec_name,
                        "sectionCode": sec_code,
                        "type": current_section,
                        "number": q_num,
                        "question": q_text,
                        "answer": answer_text,
                        "pdfPage": pdf_pg,
                        "bookPage": book_pg
                    })
                    total_q_count += 1
                    
            i += 1

        parsed_chapters.append({
            "number": ch_num,
            "title": meta["title"],
            "startPage": meta["startPage"],
            "endPage": meta["endPage"],
            "bookStart": meta["bookStart"],
            "bookEnd": meta["bookEnd"],
            "totalQuestions": len(questions),
            "questions": questions
        })

    # Group all questions by PDF page for quick lookup
    pages_map = {}
    for p in range(1, 204):
        # find which chapter this page belongs to
        curr_ch_num = None
        for ch in parsed_chapters:
            if ch["startPage"] <= p <= ch["endPage"]:
                curr_ch_num = ch["number"]
                break
        book_pg = p - 5 if p > 5 else None
        pages_map[p] = {
            "pdfPage": p,
            "bookPage": book_pg,
            "chapterNumber": curr_ch_num,
            "isFrontMatter": p <= 5,
            "hasExercise": False,
            "questions": []
        }

    for ch in parsed_chapters:
        for q in ch["questions"]:
            pg = q["pdfPage"]
            if pg in pages_map:
                pages_map[pg]["hasExercise"] = True
                pages_map[pg]["questions"].append(q)

    full_dataset = {
        "subjectId": "biology_x",
        "subjectName": "Biology",
        "gradeId": "class_x",
        "gradeName": "Class X (SSC Part II)",
        "board": "Sindh Textbook Board, Jamshoro",
        "totalPages": 203,
        "totalQuestionsSolved": total_q_count,
        "chapters": parsed_chapters,
        "pagesMap": pages_map
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(full_dataset, f, indent=2, ensure_ascii=False)

    print(f"Parsed {len(parsed_chapters)} chapters, {total_q_count} questions.")
    print(f"Dataset successfully saved to: {output_path}")

if __name__ == '__main__':
    parse_docx_and_map()
