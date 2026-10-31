import zipfile
import xml.etree.ElementTree as ET

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

for i, p in enumerate(paras[:40]):
    print(f"[{i:03d}] {p}")
