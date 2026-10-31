# English XI — Build Tracker

**Book:** Sindh Textbook Board, Jamshoro — English XI (262 PDF pages)
**Book page = PDF page − 7** (PDF 8 = printed page 1)
**No printed answer key** — comprehension answers come from the reading texts;
writing/oral tasks get model responses.

## Structure

| Chapter | Title | Book pages | PDF pages |
|---|---|---|---|
| 1 | Democratic Citizenship | 1–16 | 8–23 |
| 2 | Preservation of Nature | 17–34 | 24–41 |
| 3 | Managing Change | 35–53 | 42–60 |
| 4 | Technology Smart & Tech-Savvy | 54–71 | 61–78 |
| 5 | Civic Sense and Civic Activities | 72–89 | 79–96 |
| 6 | Respecting Self & Others | 90–106 | 97–113 |
| 7 | Self-Grooming | 107–121 | 114–128 |
| 8 | Places of Historical / Cultural Importance | 122–141 | 129–148 |
| 9 | Choosing Career | 142–160 | 149–167 |
| 10 | Practicing Positive Work Ethics | 161–176 | 168–183 |
| 11 | Section B: Poetry (Elements + 7 poems) | 177–223 | 184–230 |
| 12 | Section C: Play — A Visit to a Small Planet | 224–255 | 231–262 |

Each unit has four sections: **1 Reading Comprehension** (pre-reading,
while-reading exercises 1–3, post-reading exercises 4–6), **2 Writing**,
**3 Oral Communication**, **4 Grammar**.

Poems each carry 6–9 exercises; the poetry introduction carries Exercises 1–6.
The play has Exercises 1–11 after Scene III (book 243–249); the biographies
(book 250–255) are reading material with no exercises.

## Progress

| Part | File | Book pages | Status |
|---|---|---|---|
| Unit 1 | unit_01.json | 1–16 | solved (92 items) |
| Unit 2 | unit_02.json + unit_02_ext.json | 17–34 | solved (44 items) |
| Unit 3 | unit_03.json | 35–53 | solved (66 items) |
| Unit 4 | unit_04.json | 54–71 | solved (36 items) |
| Unit 5 | unit_05.json | 72–89 | solved (38 items) |
| Unit 6 | unit_06.json | 90–106 | solved (41 items) |
| Unit 7 | unit_07.json | 107–121 | solved (40 items) |
| Unit 8 | unit_08.json | 122–141 | solved (45 items) |
| Unit 9 | unit_09.json | 142–160 | solved (55 items) |
| Unit 10 | unit_10.json | 161–176 | solved (39 items) |
| Poetry A | poetry_a.json | 177–223 (Elements + Poems 1–4) | solved (144 items) |
| Poetry B | poetry_b.json | 177–223 (Poems 5–7) | solved (154 items) |
| Play | play.json | 224–249 (text + Exercises 1–11) | solved (58 items) |

## Build

```
cd scripts
python build_english_xi_data.py
```

Output: `public/data/class_xi_english.json`.

Build result: **852 items, 12 chapters, 182 MCQs, 49 section labels**.
`subjects.json` english_xi: `totalChapters: 12`, `totalQuestionsSolved: 852`.

## Audit / errata (2026-10-27)

All parts were re-read against the printed pages: every exercise, sub-part and
activity is present (zero omissions). Answer-quality fixes applied:

- **U2S1 Ex4 (similes):** the abridged extract contains only one strict simile;
  rows 2–5 are implied comparisons. A note was added at the top of the answer.
- **U3S1 Q7:** both (c) "moneylenders" and (d) "house loan" lack textual
  support. Key kept at (c); explanation now flags the defective option set.
- **U5S4 Ex2 Q1:** matching rows 4/5 carried two letters each; rows corrected to
  D and B. Row 7 cited "Part B" for "more intelligent" — corrected to Part A.
  Explanation rewritten with the printed A–D labels.
- **U10S1 Ex3 Q2:** keyed "servant" though the speaker is the destitute
  (younger) brother. Key changed to **(a) elder brother** — the only printed
  option naming a brother — with the looseness of the printed options explained.

## Notes / conventions

- Item schema: `id, sectionCode, type ('sq'|'mcq'), number, question, answer,
  explanation, bookPage, options, optionsRaw, correctAnswer`. The builder adds
  `chapter`, `section`, `pdfPage`.
- Section codes: `U{n}S{1-4}` for units, `P{0-7}S1` for poetry (`P0` = Elements
  of Poetry), `C1S1` for the play.
- IDs: `u1_r_ex1_q1`, `u1_w_ex1_qa`, `u1_o_ex1_q1`, `u1_g_ex1_q1`, `p1_ex1_q1`,
  `play_ex1_q1`; table rows get their printed number.
- MCQs carry four options and `correctAnswer` in `(x) text` form.
- Matching/vocabulary tables are one card per exercise with every row answered
  in a newline-formatted table in `answer`.
- Writing and oral tasks are open-ended; each gets a model response and an
  explanation noting that other valid answers are acceptable.
