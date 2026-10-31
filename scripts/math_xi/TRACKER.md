# Math XI solution tracker

Sindh Textbook Board, Class XI Mathematics. PDF has 424 pages; **book page = PDF page − 4**.
Source pages: `public/books/class_xi/math/pages/page_NNN.png` (140 dpi, already de-rotated).
Exercise headings are vector pills; sections below were located geometrically and read visually.

## Units (PDF page ranges)

| # | Title | PDF pages | Book pages |
| - | ----- | --------- | ---------- |
| 1  | Complex Numbers | 5-28 | 1-24 |
| 2  | Matrices and Determinants | 29-77 | 25-73 |
| 3  | Vectors | 78-127 | 74-123 |
| 4  | Sequences and Series | 128-165 | 124-161 |
| 5  | Miscellaneous Series | 166-182 | 162-178 |
| 6  | Permutation, Combination and Probability | 183-217 | 179-213 |
| 7  | Mathematical Induction and Binomial Theorem | 218-241 | 214-237 |
| 8  | Functions and Graphs | 242-270 | 238-266 |
| 9  | Linear Programming | 271-295 | 267-291 |
| 10 | Trigonometric Identities of Sum and Difference of Angles | 296-320 | 292-316 |
| 11 | Application of Trigonometry | 321-340 | 317-336 |
| 12 | Graphs of Trigonometric and Inverse Trigonometric Functions and Solution of Trigonometric Equations | 341-391 | 337-387 |

Answers key: PDF 392-424 (book 388-420). Answer-key headings: 392 (1.1, 1.2), 393 (1.3, R1),
394 (2.1, 2.2), 395 (2.3, 2.5), 396 (2.6, R2), 397 (3.1, 3.2), 398 (3.3-3.5), 399 (3.6, R3, 4.1),
400 (4.2-4.5), 401 (4.6-4.9), 402 (R4, 5.1), 403 (5.2-5.4, R5, 6.1), 404 (6.2-6.4),
405 (R6 MCQs, 6.1?), 406 (R6 Q2-7, 7.2, 7.3), 407 (R7, 8.1), 408 (8.2, 8.3), 410 (8.4), 411 (R8),
412 (9.1), 414 (9.2), 415 (9.3), 416 (R9), 417 (10.1-10.3), 418 (10.4, R10, 11.1, 11.2),
419 (11.3, 11.4), 420 (R11, 12.1), 422 (12.2-12.5), 423 (R12). **Exercise 7.1's induction
proofs have no printed answers** (key jumps from Review 6 to Exercise 7.2).

## Exercise page map (PDF pages; heading page -> page before next heading)

| Unit | Sections |
| ---- | -------- |
| 1 | 1.1 p11-21, 1.2 p22-25, 1.3 p26, R1 p26-28 |
| 2 | 2.1 p37-43, 2.2 p44-49, 2.3 p50-55, 2.4 p56-62, 2.5 p63-73, 2.6 p74, R2 p74-77 |
| 3 | 3.1 p90-96, 3.2 p97-101, 3.3 p102-109, 3.4 p110-118, 3.5 p119-124, 3.6 p125, R3 p125-127 |
| 4 | 4.1 p132-134, 4.2 p135-137, 4.3 p138-142, 4.4 p143-147, 4.5 p148-149, 4.6 p150-155, 4.7 p156-158, 4.8 p159-162, 4.9 p163, R4 p164-165 |
| 5 | 5.1 p171-173, 5.2 p174-177, 5.3 p178-180, 5.4 p181, R5 p181-182 |
| 6 | 6.1 p184-194, 6.2 p195-200, 6.3 p201-213, 6.4 p214-215, R6 p216-217 |
| 7 | 7.1 p222-230, 7.2 p231-238, 7.3 p239, R7 p240-241 |
| 8 | 8.1 p246-249, 8.2 p250-261, 8.3 p262-266, 8.4 p267, R8 p268-270 |
| 9 | 9.1 p278-282, 9.2 p283-291, 9.3 p292, R9 p293-295 |
| 10 | 10.1 p303-307, 10.2 p308-313, 10.3 p314-317, 10.4 p318, R10 p319-320 |
| 11 | 11.1 p323-329, 11.2 p330-332, 11.3 p333-336, 11.4 p337, R11 p338-340 |
| 12 | 12.1 p348-366, 12.2 p367-371, 12.3 p372-384, 12.4 p385-388, 12.5 p389, R12 p390-391 |

## Progress

| Unit | Module | Items | Status |
| ---- | ------ | ----- | ------ |
| 1  | u01.py | 159 | audited — complete |
| 2  | u02.py | 168 | audited — complete |
| 3  | u03.py | 160 | audited — complete |
| 4  | u04.py | 181 | audited — complete |
| 5  | u05.py | 51  | audited — complete |
| 6  | u06.py | 147 | audited — complete |
| 7  | u07.py | 94  | audited — complete |
| 8  | u08.py | 106 | audited — complete |
| 9  | u09.py | 48  | audited — complete |
| 10 | u10.py | 124 | audited — complete |
| 11 | u11.py | 100 | audited — complete |
| 12 | u12.py | 153 | audited — complete |
| —  | **total** | **1491** | 207 MCQs, 57 figure descriptions |

Build: `cd scripts && python build_math_xi_data.py` → `public/data/class_xi_math.json`.
All 12 units were independently audited against the printed exercise pages and key pages 392–424:
inventory matched exactly (no missing sub-parts), all MCQ keys checked, and all non-MCQ answers
recomputed or verified. Printed-key errata are recorded inside the affected items' explanations.

### Confirmed printed-key / print errata (documented, not silently copied)

- 2.5 Q2(i), 2.5 Q2(iii): key RREFs have rank 2; printed matrices are non-singular → module gives I₃/correct RREF.
- 2.6 Q1(i): key gives only the trivial solution; det = 0, so non-trivial family x = −4k, y = 3k, z = k.
- Review 2 MCQ xii: key letter (b) is Scalar matrix; correct option is (c) Square matrix.
- 3.2 Q1(iv): key prints 7k; correct is 5k.
- Review 3 MCQ xi: key (b) π/3; correct (c) π/6 (2 sin θ = 1).
- 4.2 Q10: printed identity is false in general (counterexample in item).
- 4.5 Q3: key repeats the negative-ratio family; correct pair is (2/3)ⁿ or (−2/3)ⁿ.
- Review 4 Q5: key says 12 terms; correct 13. Key answer misnumbered “11.” for Q10.
- 5.3 Q6: key [36n+3(5ⁿ−15)]/16; correct [36n+3(5ⁿ−1)]/16.
- 5.4 Q6: key n/[6(3n+2)]; correct n/[2(3n+2)].
- 6.2 Q16: key 1500; correct 2250. 6.2 Q19: key 256; correct 625 (digits may repeat).
- 6.3 Q9(ii): key 120780; correct 120945. 6.4 Q1(iii): key 1/2; correct 3/4.
- 6.4 Q10(i),(ii): key gives joint probabilities 1/18, 1/3; conditional answers are 1/15, 2/5.
- Review 6 MCQ ix: key (c); correct (a) r! (ⁿPₙ = n!).
- 7.3 Q4(i),(ii): key truncates √24 and ∛28; correct 4.899 and 3.037.
- 7.3 Q6(ii): printed 5/64 coefficient is inconsistent; correct 7/96.
- 8.1 Q9: key range y ≥ 0; correct [1, ∞). 8.1 Q10: key [0, ∞); correct (0, 1].
- 8.2 Q4(v): key domain ℝ; correct [0, ∞). 8.2 Q3(xii): printed x ≠ 1/2 should be x ≠ −1/2.
- 9.3 Q1(i): key 30.6; exact 92/3. Review 9 Q4: key minimum 10 at (5/2, 0); correct −18 at (0, 6).
- 10.2 Q3(vi),(vii): key answers interchanged. 10.3 Q20(iii): key −44/125; correct −44/117.
- 11.1 Q2: shadow printed 12 cm; key 53°7′ requires 12 m. 11.2 Q4(ii): “a = 37” misprint for c = 37.
- 11.2 Q3(iii), 11.3 Q1(vi), 11.3 Q1(ii),(iv), 11.4 Q1(iii): rounding slips in key.
- Review 11 MCQ xi: key letter misprint (▲/s is option (d)). Review 11 Q6: key 8.6 km is correct under N55°E.
- 12.1 Q4(vi): key’s finite max/min impossible (vertical asymptotes).
- 12.3 Q11–Q14; 12.4 Q1(iv), Q4(i),(iv); 12.5 Q3, Q12, Q14–Q17; Review 12 MCQ xii and Q4(i), Q6 — key omissions/errors corrected in items.
- PDF 320 (Review 10 MCQs xiv–xvii) is blank in this copy; only its key answers survive, so those four stems cannot be added.
