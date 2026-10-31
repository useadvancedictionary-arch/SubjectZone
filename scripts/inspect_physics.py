import zipfile
import xml.etree.ElementTree as ET
import re

docx_path = r'd:\SubjectZone\Books and Solutions\Class X\Class_X_Physics_Complete_Solutions_Units_10_to_20.docx'

with zipfile.ZipFile(docx_path) as z:
    xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    paras = []
    for p in tree.iterfind('.//w:p', ns):
        texts = [t.text for t in p.iterfind('.//w:t', ns) if t.text]
        if texts:
            paras.append(''.join(texts).strip())

unit_paras = {}
current_u = None
for p in paras:
    m = re.match(r'^Unit\s+(\d+)[:\s]+(.*)', p, re.I)
    if m:
        current_u = int(m.group(1))
        unit_paras[current_u] = {'title': m.group(2).strip(), 'paras': []}
    elif current_u is not None:
        unit_paras[current_u]['paras'].append(p)

for u, data in sorted(unit_paras.items()):
    title = data['title']
    print(f"\n==========================================")
    print(f"UNIT {u}: {title} ({len(data['paras'])} paragraphs)")
    print(f"==========================================")
    sec = "None"
    for p in data['paras']:
        if 'Section' in p or 'Self-Assessment' in p:
            sec = p
            print(f"  [SECTION] {sec}")
        elif p.startswith('Q') or p.startswith('Numerical') or 'Numerical' in p[:15]:
            print(f"     -> {p[:90]}")
