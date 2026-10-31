import zipfile
import xml.etree.ElementTree as ET
import json
import re
import os

def parse_chemistry_docx():
    docx_path = r'd:\SubjectZone\Books and Solutions\Class X\Class_10_Chemistry_Complete_Solutions.docx'
    output_path = r'd:\SubjectZone\public\data\class_x_chemistry.json'
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

    chapter_paras = {}
    current_ch = None
    for p in paragraphs:
        m = re.match(r'^Chapter\s+(\d+)[:\s]+(.*)', p, re.I)
        if m:
            current_ch = int(m.group(1))
            chapter_paras[current_ch] = {'title': m.group(2).strip(), 'paras': []}
        elif current_ch is not None:
            chapter_paras[current_ch]['paras'].append(p)

    chapter_meta = {
        1: {"title": "Chemical Equilibrium", "startPage": 5, "endPage": 22, "bookStart": 1, "bookEnd": 18, "mcqPage": 20, "sqPage": 21, "dqPage": 22, "numPage": 22},
        2: {"title": "Acids, Bases and Salts", "startPage": 23, "endPage": 36, "bookStart": 19, "bookEnd": 32, "mcqPage": 34, "sqPage": 35, "dqPage": 36, "numPage": 36},
        3: {"title": "Organic Chemistry", "startPage": 37, "endPage": 59, "bookStart": 33, "bookEnd": 55, "mcqPage": 57, "sqPage": 58, "dqPage": 59, "numPage": 59},
        4: {"title": "Biochemistry", "startPage": 60, "endPage": 76, "bookStart": 56, "bookEnd": 72, "mcqPage": 74, "sqPage": 75, "dqPage": 76, "numPage": 76},
        5: {"title": "Environmental Chemistry I: The Atmosphere", "startPage": 77, "endPage": 91, "bookStart": 73, "bookEnd": 87, "mcqPage": 89, "sqPage": 90, "dqPage": 91, "numPage": 91},
        6: {"title": "Environmental Chemistry II: Water", "startPage": 92, "endPage": 106, "bookStart": 88, "bookEnd": 102, "mcqPage": 104, "sqPage": 105, "dqPage": 106, "numPage": 106},
        7: {"title": "Analytical Chemistry", "startPage": 107, "endPage": 125, "bookStart": 103, "bookEnd": 121, "mcqPage": 123, "sqPage": 124, "dqPage": 125, "numPage": 125},
        8: {"title": "Industrial Chemistry", "startPage": 126, "endPage": 139, "bookStart": 122, "bookEnd": 135, "mcqPage": 137, "sqPage": 138, "dqPage": 139, "numPage": 139}
    }

    parsed_chapters = []
    total_q_count = 0

    for ch_num in sorted(chapter_paras.keys()):
        meta = chapter_meta.get(ch_num, {
            "title": chapter_paras[ch_num]['title'],
            "startPage": 5, "endPage": 139, "bookStart": 1, "bookEnd": 135,
            "mcqPage": 137, "sqPage": 138, "dqPage": 139, "numPage": 139
        })
        paras = chapter_paras[ch_num]['paras']
        
        questions = []
        current_sec = None
        current_q = None

        def finalize_q(q):
            if not q: return
            # Clean up text
            q['question'] = q['question'].strip()
            if 'answer' in q:
                q['answer'] = q['answer'].strip()
            if 'explanation' in q:
                q['explanation'] = q['explanation'].strip()
            questions.append(q)

        i = 0
        while i < len(paras):
            p = paras[i]
            
            # Check for section header
            if 'SECTION- A' in p or 'SECTION A' in p or 'Multiple Choice Questions' in p:
                current_sec = 'mcq'
                i += 1
                continue
            elif 'SECTION- B' in p or 'SECTION B' in p or 'Short Questions' in p:
                finalize_q(current_q)
                current_q = None
                current_sec = 'sq'
                i += 1
                continue
            elif 'SECTION- C' in p or 'SECTION C' in p or 'Detailed Questions' in p:
                finalize_q(current_q)
                current_q = None
                current_sec = 'dq'
                i += 1
                continue
            elif 'SECTION- D' in p or 'SECTION D' in p or 'Numerical' in p:
                finalize_q(current_q)
                current_q = None
                current_sec = 'num'
                i += 1
                continue

            # Parse questions based on section
            if current_sec == 'mcq':
                m_q = re.match(r'^Q(\d+)\.\s*(.*)', p)
                if m_q:
                    finalize_q(current_q)
                    q_num = int(m_q.group(1))
                    q_text = m_q.group(2)
                    pdf_p = meta['mcqPage']
                    book_p = pdf_p - 4
                    current_q = {
                        'id': f'chem_ch{ch_num}_mcq_{q_num}',
                        'chapter': ch_num,
                        'section': 'Multiple Choice Questions',
                        'sectionCode': 'A',
                        'type': 'mcq',
                        'number': q_num,
                        'question': q_text,
                        'options': [],
                        'optionsRaw': '',
                        'correctAnswer': '',
                        'explanation': '',
                        'pdfPage': pdf_p,
                        'bookPage': book_p
                    }
                elif current_q and current_q['type'] == 'mcq':
                    if p.startswith('Correct Answer:'):
                        ans_val = p.replace('Correct Answer:', '').strip()
                        current_q['correctAnswer'] = ans_val
                        current_q['optionsRaw'] = ans_val
                    elif p.startswith('Explanation:'):
                        current_q['explanation'] = p.replace('Explanation:', '').strip()
                    elif re.match(r'^\([a-d]\)', p):
                        # Option line
                        opt_m = re.match(r'^\(([a-d])\)\s*(.*)', p)
                        if opt_m:
                            current_q['options'].append({'key': opt_m.group(1), 'text': opt_m.group(2)})
                    else:
                        if not current_q.get('correctAnswer') and not current_q.get('explanation'):
                            current_q['question'] += ' ' + p
                        elif current_q.get('explanation'):
                            current_q['explanation'] += ' ' + p

            elif current_sec in ['sq', 'dq', 'num']:
                m_q = re.match(r'^Q(\d+)[:\.]\s*(.*)', p, re.I)
                if m_q:
                    finalize_q(current_q)
                    q_num = int(m_q.group(1))
                    q_text = m_q.group(2)
                    sec_name = 'Short Questions' if current_sec == 'sq' else ('Detailed Questions' if current_sec == 'dq' else 'Numerical Questions')
                    sec_code = 'B' if current_sec == 'sq' else ('C' if current_sec == 'dq' else 'D')
                    q_type = 'short' if current_sec == 'sq' else ('long' if current_sec == 'dq' else 'numerical')
                    pdf_p = meta['sqPage'] if current_sec == 'sq' else (meta['dqPage'] if current_sec == 'dq' else meta['numPage'])
                    book_p = pdf_p - 4
                    current_q = {
                        'id': f'chem_ch{ch_num}_{q_type}_{q_num}',
                        'chapter': ch_num,
                        'section': sec_name,
                        'sectionCode': sec_code,
                        'type': q_type,
                        'number': q_num,
                        'question': q_text,
                        'answer': '',
                        'explanation': '',
                        'pdfPage': pdf_p,
                        'bookPage': book_p
                    }
                elif current_q:
                    if p.startswith('Answer:'):
                        current_q['answer'] = p.replace('Answer:', '').strip()
                    elif p.startswith('Explanation:'):
                        current_q['explanation'] = p.replace('Explanation:', '').strip()
                    else:
                        if 'answer' in current_q and current_q['answer'] != '':
                            current_q['answer'] += '\n' + p
                        elif 'explanation' in current_q and current_q['explanation'] != '':
                            current_q['explanation'] += '\n' + p
                        else:
                            current_q['question'] += ' ' + p

            i += 1

        finalize_q(current_q)
        total_q_count += len(questions)

        parsed_chapters.append({
            'number': ch_num,
            'title': meta['title'],
            'startPage': meta['startPage'],
            'endPage': meta['endPage'],
            'bookStart': meta['bookStart'],
            'bookEnd': meta['bookEnd'],
            'totalQuestions': len(questions),
            'questions': questions
        })

    # Build pagesMap
    pages_map = {}
    for p_num in range(1, 140):
        # find matching chapter
        matched_ch = None
        for ch in parsed_chapters:
            if ch['startPage'] <= p_num <= ch['endPage']:
                matched_ch = ch
                break

        ch_num = matched_ch['number'] if matched_ch else None
        is_front = (p_num < 5)
        book_p = (p_num - 4) if p_num >= 5 else p_num

        page_qs = []
        if matched_ch:
            for q in matched_ch['questions']:
                if q['pdfPage'] == p_num:
                    page_qs.append(q)

        pages_map[str(p_num)] = {
            'pdfPage': p_num,
            'bookPage': book_p,
            'chapterNumber': ch_num,
            'isFrontMatter': is_front,
            'hasExercise': len(page_qs) > 0,
            'questions': page_qs
        }

    dataset = {
        'subjectId': 'chemistry_x',
        'subjectName': 'Chemistry Class X',
        'gradeId': 'class_x',
        'gradeName': 'Class X (Grade 10)',
        'board': 'Sindh Textbook Board (Jamshoro)',
        'totalPages': 139,
        'totalQuestionsSolved': total_q_count,
        'chapters': parsed_chapters,
        'pagesMap': pages_map
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print(f"Parsed {len(parsed_chapters)} chapters, {total_q_count} questions total.")
    print(f"Saved dataset to {output_path}")

if __name__ == '__main__':
    parse_chemistry_docx()
