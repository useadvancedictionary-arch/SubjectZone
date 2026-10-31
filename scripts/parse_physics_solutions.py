import zipfile
import xml.etree.ElementTree as ET
import json
import re
import os

def parse_physics_docx():
    docx_path = r'd:\SubjectZone\Books and Solutions\Class X\Class_X_Physics_Complete_Solutions_Units_10_to_20.docx'
    output_path = r'd:\SubjectZone\public\data\class_x_physics.json'
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

    unit_paras = {}
    current_u = None
    for p in paragraphs:
        m = re.match(r'^Unit\s+(\d+)[:\s]+(.*)', p, re.I)
        if m:
            current_u = int(m.group(1))
            unit_paras[current_u] = {'title': m.group(2).strip(), 'paras': []}
        elif current_u is not None:
            unit_paras[current_u]['paras'].append(p)

    unit_meta = {
        10: {"title": "General Wave Properties", "startPage": 5, "endPage": 24, "bookStart": 1, "bookEnd": 20},
        11: {"title": "Sound", "startPage": 25, "endPage": 44, "bookStart": 21, "bookEnd": 40},
        12: {"title": "Electromagnetic Spectrum", "startPage": 45, "endPage": 60, "bookStart": 41, "bookEnd": 56},
        13: {"title": "Geometrical Optics", "startPage": 61, "endPage": 89, "bookStart": 57, "bookEnd": 85},
        14: {"title": "Electrostatics", "startPage": 90, "endPage": 112, "bookStart": 86, "bookEnd": 108},
        15: {"title": "Current Electricity", "startPage": 113, "endPage": 135, "bookStart": 109, "bookEnd": 131},
        16: {"title": "Electromagnetism", "startPage": 136, "endPage": 156, "bookStart": 132, "bookEnd": 152},
        17: {"title": "Introductory Electronics", "startPage": 157, "endPage": 182, "bookStart": 153, "bookEnd": 178},
        18: {"title": "Information and Communication Technology (ICT)", "startPage": 183, "endPage": 201, "bookStart": 179, "bookEnd": 197},
        19: {"title": "Atomic Structure", "startPage": 202, "endPage": 211, "bookStart": 198, "bookEnd": 207},
        20: {"title": "Nuclear Structure", "startPage": 212, "endPage": 242, "bookStart": 208, "bookEnd": 238}
    }

    def get_physics_question_page(ch, sec_type, q_num):
        if ch == 10:
            if sec_type == 'mcq': return (22, 18)
            if sec_type == 'self': return (22, 18)
            if sec_type == 'sq': return (23, 19)
            if sec_type == 'numerical': return (24, 20)
        elif ch == 11:
            if sec_type == 'mcq': return (42, 38)
            if sec_type == 'sq': return (43, 39)
            if sec_type == 'numerical': return (44, 40)
        elif ch == 12:
            if sec_type == 'mcq': return (58, 54)
            if sec_type == 'sq': return (59, 55)
            if sec_type == 'numerical': return (60, 56)
        elif ch == 13:
            if sec_type == 'mcq': return (86, 82)
            if sec_type == 'sq':
                return (87, 83) if q_num <= 8 else (88, 84)
            if sec_type == 'numerical': return (89, 85)
        elif ch == 14:
            if sec_type == 'mcq': return (111, 107)
            return (112, 108)
        elif ch == 15:
            if sec_type == 'mcq': return (133, 129)
            if sec_type == 'sq': return (134, 130)
            if sec_type == 'numerical': return (135, 131)
        elif ch == 16:
            if sec_type == 'mcq': return (155, 151)
            return (156, 152)
        elif ch == 17:
            if sec_type == 'mcq': return (181, 177)
            return (182, 178)
        elif ch == 18:
            if sec_type == 'mcq': return (200, 196)
            return (201, 197)
        elif ch == 19:
            if sec_type == 'mcq': return (210, 206)
            return (211, 207)
        elif ch == 20:
            if sec_type == 'mcq': return (233, 229)
            if sec_type == 'sq': return (234, 230)
            if sec_type == 'numerical': return (236, 232)
        
        meta = unit_meta.get(ch, {"endPage": 242, "bookEnd": 238})
        return (meta["endPage"], meta["bookEnd"])

    parsed_chapters = []
    total_q_count = 0

    for ch_num in sorted(unit_paras.keys()):
        meta = unit_meta.get(ch_num, {
            "title": unit_paras[ch_num]['title'],
            "startPage": 5, "endPage": 242, "bookStart": 1, "bookEnd": 238
        })
        paras = unit_paras[ch_num]['paras']
        
        current_section = None
        questions = []
        
        i = 0
        while i < len(paras):
            p = paras[i]
            
            # Check for section headers
            if re.search(r'Multiple Choice|Section\s*\(?\s*A\s*\)?', p, re.I):
                current_section = 'mcq'
                i += 1
                continue
            elif re.search(r'Self-Assessment|Self Assessment', p, re.I):
                current_section = 'self'
                i += 1
                continue
            elif re.search(r'Structured Questions|Short Questions|Section\s*\(?\s*B\s*\)?', p, re.I):
                current_section = 'sq'
                i += 1
                continue
            elif re.search(r'Numericals|Section\s*\(?\s*C\s*\)?', p, re.I):
                current_section = 'numerical'
                i += 1
                continue

            # Case A: Numerical question
            num_match = re.match(r'Numerical\s+(\d+)[:\s]+(.*)', p, re.I)
            if num_match:
                q_num = int(num_match.group(1))
                num_title = num_match.group(2).strip()
                pdf_pg, book_pg = get_physics_question_page(ch_num, 'numerical', q_num)
                
                # Next paras often contain Given Data and Explanation
                given_data_text = ""
                expl_text = ""
                
                if i + 1 < len(paras) and ('Given Data:' in paras[i+1] or 'Formula:' in paras[i+1]):
                    i += 1
                    given_data_text = paras[i]
                
                if i + 1 < len(paras) and paras[i+1].startswith('Explanation:'):
                    i += 1
                    expl_text = paras[i].replace('Explanation:', '').strip()
                
                # Format the answer cleanly: break Given Data, Formula, Calculation, Result into readable lines
                formatted_answer = given_data_text
                for key_token in ['Formula:', 'Calculation:', 'Result:']:
                    formatted_answer = formatted_answer.replace(key_token, f'\n\n{key_token} ')
                formatted_answer = formatted_answer.replace('Given Data:', 'Given Data:\n')

                questions.append({
                    "id": f"ch{ch_num}_numerical_{q_num}",
                    "chapter": ch_num,
                    "section": "Numericals",
                    "sectionCode": "C",
                    "type": "numerical",
                    "number": q_num,
                    "question": f"Numerical {q_num}: {num_title}",
                    "answer": formatted_answer.strip(),
                    "explanation": expl_text,
                    "pdfPage": pdf_pg,
                    "bookPage": book_pg
                })
                total_q_count += 1
                i += 1
                continue

            # Case B: Q(\d+) Question
            q_match = re.match(r'^Q(\d+)[:.]?\s*(.*)', p)
            if q_match:
                q_num = int(q_match.group(1))
                rest = q_match.group(2).strip()
                sec_type = current_section or 'sq'
                pdf_pg, book_pg = get_physics_question_page(ch_num, sec_type, q_num)

                # Extract Answer: and Explanation: from the rest of the text
                question_text = rest
                answer_text = ""
                expl_text = ""

                # Check if Answer: is embedded in the line
                if 'Answer:' in rest:
                    q_part, a_part = rest.split('Answer:', 1)
                    question_text = q_part.strip()
                    if 'Explanation:' in a_part:
                        ans_part, expl_part = a_part.split('Explanation:', 1)
                        answer_text = ans_part.strip()
                        expl_text = expl_part.strip()
                    else:
                        answer_text = a_part.strip()
                elif i + 1 < len(paras) and paras[i+1].startswith('Answer:'):
                    i += 1
                    a_part = paras[i].replace('Answer:', '', 1).strip()
                    if 'Explanation:' in a_part:
                        ans_part, expl_part = a_part.split('Explanation:', 1)
                        answer_text = ans_part.strip()
                        expl_text = expl_part.strip()
                    else:
                        answer_text = a_part
                
                # Check if next paragraph is Explanation:
                if not expl_text and i + 1 < len(paras) and paras[i+1].startswith('Explanation:'):
                    i += 1
                    expl_text = paras[i].replace('Explanation:', '', 1).strip()

                if sec_type == 'mcq':
                    # Parse out options if present in answer or question
                    correct_ans = answer_text
                    options = []
                    
                    # If answer text has "c) 2.0 Hz", create option badge
                    m_opt = re.match(r'^([a-d])\)\s*(.*)', correct_ans, re.I)
                    if m_opt:
                        options.append({
                            "key": m_opt.group(1).lower(),
                            "text": m_opt.group(2).strip()
                        })

                    questions.append({
                        "id": f"ch{ch_num}_mcq_{q_num}",
                        "chapter": ch_num,
                        "section": "Multiple Choice Questions",
                        "sectionCode": "A",
                        "type": "mcq",
                        "number": q_num,
                        "question": question_text,
                        "options": options,
                        "optionsRaw": answer_text,
                        "correctAnswer": correct_ans,
                        "explanation": expl_text,
                        "pdfPage": pdf_pg,
                        "bookPage": book_pg
                    })
                    total_q_count += 1

                elif sec_type == 'self':
                    questions.append({
                        "id": f"ch{ch_num}_self_{q_num}",
                        "chapter": ch_num,
                        "section": "Self-Assessment Questions",
                        "sectionCode": "D",
                        "type": "self",
                        "number": q_num,
                        "question": question_text,
                        "answer": answer_text,
                        "explanation": expl_text,
                        "pdfPage": pdf_pg,
                        "bookPage": book_pg
                    })
                    total_q_count += 1

                else: # 'sq'
                    questions.append({
                        "id": f"ch{ch_num}_sq_{q_num}",
                        "chapter": ch_num,
                        "section": "Structured Questions",
                        "sectionCode": "B",
                        "type": "sq",
                        "number": q_num,
                        "question": question_text,
                        "answer": answer_text,
                        "explanation": expl_text,
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
    for p in range(1, 243):
        curr_ch_num = None
        for ch in parsed_chapters:
            if ch["startPage"] <= p <= ch["endPage"]:
                curr_ch_num = ch["number"]
                break
        book_pg = p - 4 if p >= 5 else None
        pages_map[p] = {
            "pdfPage": p,
            "bookPage": book_pg,
            "chapterNumber": curr_ch_num,
            "isFrontMatter": p < 5,
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
        "subjectId": "physics_x",
        "subjectName": "Physics",
        "gradeId": "class_x",
        "gradeName": "Class X (SSC Part II)",
        "board": "Sindh Textbook Board, Jamshoro",
        "totalPages": 242,
        "totalQuestionsSolved": total_q_count,
        "chapters": parsed_chapters,
        "pagesMap": pages_map
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(full_dataset, f, indent=2, ensure_ascii=False)

    print(f"Parsed {len(parsed_chapters)} units, {total_q_count} questions.")
    print(f"Dataset successfully saved to: {output_path}")

if __name__ == '__main__':
    parse_physics_docx()
