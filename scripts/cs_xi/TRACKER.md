# Computer Science XI — Build Tracker

**Book:** Sindh Textbook Board, Jamshoro — Computer Science XI (240 PDF pages)
**Book page = PDF page − 5** (PDF 6 = printed page 1)
**No printed answer key** — answers derived from unit content and standard CS knowledge.

## Unit map

| Unit | Title | Book pages | PDF pages | Exercise PDF pages |
|---|---|---|---|---|
| 1 | Computer Systems | 1–70 | 6–75 | 74–75 |
| 2 | Computational Thinking & Algorithm | 71–90 | 76–95 | 94–95 |
| 3 | Programming Fundamentals | 91–138 | 96–143 | 141–143 |
| 4 | Data and Analysis | 139–173 | 144–178 | 176–178 |
| 5 | Applications and Impacts of Computing | 174–198 | 179–203 | 201–203 |
| 6 | Digital Literacy | 199–218 | 204–223 | 221–223 |

Glossary (book 219–225) and Teaching Guide (book 226–234) contain no exercises.

## Exercise shape

Each unit: **A** Encircle the correct answer (10 MCQs), **B** Fill in the Blanks (5),
**C** short descriptive answers (5), **D** detailed answers (3–5), **E** Activities.
Unit 4 has only three detailed questions; Unit 5 has seven activities.

## Progress

| Unit | Module | Items | Status |
|---|---|---|---|
| 1 | u01.py | 33 | solved, audited |
| 2 | u02.py | 28 | solved, audited |
| 3 | u03.py | 28 | solved, audited |
| 4 | u04.py | 28 | solved, audited |
| 5 | u05.py | 32 | solved, audited |
| 6 | u06.py | 29 | solved, audited |
| — | **total** | **178** | 60 MCQs |

Audited 2026-10-25: two independent passes confirmed every printed question and
sub-part is present. Derived JSON: 178 items, 60 MCQs, 178 unique IDs, no
structural problems. App-tested: catalog card, all six sidebar units, 32 cards
in Unit 5, MCQ options/key/explanation, multi-line table answers.

## Build

```
cd scripts
python build_cs_xi_data.py
```

Output: `public/data/class_xi_cs.json`.

## Notes / errata

- **U3 Q1(iii)** is ambiguous: both `(a) if (condition):` and `(c) if (1):` are
  syntactically valid Python (1 is truthy). The key gives the canonical form
  `(a)`; the explanation records the ambiguity.
- **U3 Q1(ii)** `my-var` is illegal because `-` is parsed as subtraction.
- **U3 Q1(vii)** CPython's PEP 8 standard is 4 spaces; accept 4 spaces as key.
- **U1 B(i)** expects **XNOR** (output 1 when both inputs are the same).
- **U1 Activities 6** depends on the reader's own ping output; a model output is
  supplied and the OSI layer (Network) / protocol (ICMP) identified.
- **U2 D(iii)/(iv)** algorithms are written as numbered steps, matching the
  pseudocode style used in the unit.
- **U4 D** has only three printed questions; all three are solved.
- **U5/U6** activity answers are model responses/guides because the tasks are
  open-ended (local context, own device, own survey).
- No printed answer key exists for this book; every MCQ answer was derived and
  checked against the unit text.
- **U2 A(viii)** is printed at the top of book page 90 (PDF 95), not on PDF 94;
  page reference corrected.
- **MIME, not JPEG**, is listed as a Presentation-layer example in U1 D(iv) and
  Activity 7. JPEG is a format, not a protocol.
- **U4 A(viii)** stem is kept verbatim ("Which database objects provides …"),
  including the book's grammar; it is not silently corrected.
- **U4 A(vi)** ambiguous: a candidate key also uniquely identifies records. Key
  is (b) Primary Key, and the explanation records why (d) is technically unique
  too.
- **U4 Activity 5** requires adding a Department field before creating the
  relationship; the step-by-step now includes it.
- **U6 C(iii)** distinguishes plagiarism (using others' work without
  acknowledgement) from copyright infringement (using protected work without
  permission); the bullets cover both.
