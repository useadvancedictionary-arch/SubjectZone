"""Unit 9 - Congruent Triangles (book pp. 181-191, PDF pp. 184-194)."""
from .common import bq, mcq

U = 9
EX1 = 'Exercise 9.1'
EX2 = 'Exercise 9.2'
EX3 = 'Exercise 9.3'
EX4 = 'Exercise 9.4'
RE9 = 'Review Exercise 9'

ITEMS = []

# ============================================================== Exercise 9.1 (pdf 185)
ITEMS += [
    bq(U, EX1, 'EX9.1', '1', 'In the adjacent figure, m AB = m CB and &ang;A &cong; &ang;C. Prove that &Delta;ABD &cong; &Delta;CBE.',
       '&Delta;ABD &cong; &Delta;CBE (by A.S.A.)',
       'Proof: In &Delta;ABD &harr; &Delta;CBE: (i) &ang;A &cong; &ang;C (given); (ii) AB &cong; CB (given); (iii) &ang;ABD &cong; &ang;CBE (vertically opposite angles). Hence &Delta;ABD &cong; &Delta;CBE by the A.S.A. postulate. Q.E.D.', 185),
    bq(U, EX1, 'EX9.1', '2', 'From a point on the line bisector of an angle, perpendiculars are drawn to the arms of the angle. Prove that these perpendiculars are equal in measure.',
       'The two perpendiculars are congruent.',
       'Given: OB bisects &ang;AOC; P is a point on OB; PQ &perp; OA and PR &perp; OC. To prove: PQ &cong; PR. Proof: In &Delta;POQ &harr; &Delta;POR: (i) &ang;PQO &cong; &ang;PRO (= 90&deg;, given); (ii) &ang;POQ &cong; &ang;POR (OB bisects &ang;AOC); (iii) OP &cong; OP (common). Hence &Delta;POQ &cong; &Delta;POR by A.A.S., so PQ &cong; PR. Q.E.D.', 185),
    bq(U, EX1, 'EX9.1', '3', 'In the given figure, &Delta;ACE &cong; &Delta;BDE, such that m&ang;A = (3x + 1)&deg;, m&ang;B = (x + 35)&deg;, m&ang;AEC = (3y &minus; 2)&deg; and m&ang;DEB = (y + 8)&deg;. Find the values of x and y.',
       'x = 17, y = 5',
       'Since &Delta;ACE &cong; &Delta;BDE, corresponding angles are equal. &ang;A = &ang;B &rArr; 3x + 1 = x + 35 &rArr; 2x = 34 &rArr; x = 17. Also &ang;AEC = &ang;DEB &rArr; 3y &minus; 2 = y + 8 &rArr; 2y = 10 &rArr; y = 5.', 185),
    bq(U, EX1, 'EX9.1', '4', 'In the given figure, &Delta;DEF &cong; &Delta;PQR, such that m DE = (6x + 1) cm, m EF = 8 cm, m RQ = (5y &minus; 7) cm and m PQ = (10x &minus; 19) cm. Find the values of x and y.',
       'x = 5, y = 3',
       'In &Delta;DEF &harr; &Delta;PQR, DE &harr; PQ and EF &harr; QR. So 6x + 1 = 10x &minus; 19 &rArr; 4x = 20 &rArr; x = 5. Also EF = QR &rArr; 8 = 5y &minus; 7 &rArr; 5y = 15 &rArr; y = 3.', 185),
]

# ============================================================== Exercise 9.2 (pdf 186)
ITEMS += [
    bq(U, EX2, 'EX9.2', '1', 'ABC is a triangle in which m&ang;A = 35&deg; and m&ang;B = 100&deg;, BD &perp; AC. Prove that &Delta;BDC is an isosceles triangle.',
       '&Delta;BDC is isosceles (DB &cong; DC).',
       'Proof: In &Delta;ABC, &ang;C = 180&deg; &minus; (35&deg; + 100&deg;) = 45&deg;. Since BD &perp; AC, &ang;BDC = 90&deg;. In right &Delta;BDC, &ang;DBC = 90&deg; &minus; &ang;C = 90&deg; &minus; 45&deg; = 45&deg;. Thus &ang;DBC &cong; &ang;BCD (each 45&deg;), so the sides opposite them are equal: DB &cong; DC. Hence &Delta;BDC is isosceles. Q.E.D.', 186),
    bq(U, EX2, 'EX9.2', '2', 'If the bisector of an angle of a triangle is perpendicular to its opposite side, then prove that triangle is an isosceles triangle.',
       'The triangle is isosceles (AB &cong; AC).',
       'Given: In &Delta;ABC, AD bisects &ang;A and AD &perp; BC. To prove: &Delta;ABC is isosceles. Proof: In &Delta;ADB &harr; &Delta;ADC: (i) &ang;BAD &cong; &ang;DAC (AD bisects &ang;A); (ii) &ang;ADB &cong; &ang;ADC (= 90&deg;, AD &perp; BC); (iii) AD &cong; AD (common). Hence &Delta;ADB &cong; &Delta;ADC by A.S.A., so AB &cong; AC. Q.E.D.', 186),
    bq(U, EX2, 'EX9.2', '3', 'ABC is a triangle in which m&ang;B = 45&deg; and CD &perp; AB. Prove that &Delta;DBC is an isosceles triangle.',
       '&Delta;DBC is isosceles (DB &cong; DC).',
       'Proof: Since CD &perp; AB, &ang;BDC = 90&deg;. In right &Delta;DBC, &ang;B = 45&deg;, so &ang;BCD = 90&deg; &minus; 45&deg; = 45&deg;. Thus &ang;B &cong; &ang;BCD, so the opposite sides are equal: DB &cong; DC. Hence &Delta;DBC is isosceles. Q.E.D.', 186),
]

# ============================================================== Exercise 9.3 (pdf 188)
ITEMS += [
    bq(U, EX3, 'EX9.3', '1', 'ABC is an isosceles triangle. D is the mid-point of base BC. Prove that AD bisects &ang;A and AD &perp; BC.',
       'AD bisects &ang;A and AD &perp; BC.',
       'Proof: In &Delta;ABD &harr; &Delta;ACD: (i) AB &cong; AC (isosceles); (ii) BD &cong; DC (D is mid-point); (iii) AD &cong; AD (common). Hence &Delta;ABD &cong; &Delta;ACD by S.S.S. So &ang;BAD &cong; &ang;DAC (AD bisects &ang;A) and &ang;ADB &cong; &ang;ADC. Since BD and DC are collinear, &ang;ADB + &ang;ADC = 180&deg;; being equal, each is 90&deg;. Hence AD &perp; BC. Q.E.D.', 188),
    bq(U, EX3, 'EX9.3', '2', 'ABC and DBC are two isosceles triangles on the same side of a common base BC. Prove that AD is the right bisector of BC.',
       'AD is the right bisector of BC.',
       'Proof: In isosceles &Delta;ABC, AB &cong; AC, so A is equidistant from B and C and therefore lies on the perpendicular bisector of BC. In isosceles &Delta;DBC, DB &cong; DC, so D is also equidistant from B and C and lies on the perpendicular bisector of BC. Since A and D both lie on the perpendicular bisector of BC, the line AD is that perpendicular bisector, i.e. AD is the right bisector of BC. Q.E.D.', 188),
    bq(U, EX3, 'EX9.3', '3', 'PQRS is a square. X, Y and Z are the mid-points of PQ, QR and RS respectively. Prove that &Delta;PXY &cong; &Delta;SZY.',
       '&Delta;PXY &cong; &Delta;SZY (by S.S.S.)',
       'Proof: Let the side of the square be a. Since X, Y, Z are mid-points: PX = &frac12;a, SZ = &frac12;a. In right &Delta;PQY, PY = &radic;(a<sup>2</sup> + (&frac12;a)<sup>2</sup>) = &frac12;a&radic;5; likewise in right &Delta;SRY, SY = &frac12;a&radic;5, so PY &cong; SY. In right &Delta;QXY, XY = &radic;((&frac12;a)<sup>2</sup> + (&frac12;a)<sup>2</sup>) = &frac12;a&radic;2; likewise in right &Delta;ZRY, ZY = &frac12;a&radic;2, so XY &cong; ZY. Thus PX &cong; SZ, PY &cong; SY and XY &cong; ZY, giving &Delta;PXY &cong; &Delta;SZY by S.S.S. Q.E.D.', 188),
    bq(U, EX3, 'EX9.3', '4', 'Prove that, in an equilateral triangle, any two medians are congruent.',
       'Any two medians of an equilateral triangle are congruent.',
       'Proof: Let ABC be equilateral and let BM, CN be two medians (M mid-point of AC, N mid-point of AB). Then AB &cong; AC (equilateral), AM &cong; AN (halves of equal sides) and &ang;BAM &cong; &ang;CAN (the common angle A). Hence &Delta;BAM &cong; &Delta;CAN by S.A.S., so BM &cong; CN. Q.E.D.', 188),
]

# ============================================================== Exercise 9.4 (pdf 190)
ITEMS += [
    bq(U, EX4, 'EX9.4', '1', 'Prove that the perpendiculars from the vertices of the base to opposite sides of an isosceles triangle are congruent.',
       'The two perpendiculars are congruent.',
       'Given: &Delta;ABC with AB &cong; AC; BE &perp; AC and CF &perp; AB. To prove: BE &cong; CF. Proof: In &Delta;BEC &harr; &Delta;CFB: (i) &ang;BEC &cong; &ang;CFB (= 90&deg;); (ii) BC &cong; BC (common); (iii) &ang;EBC &cong; &ang;FCB (both equal 90&deg; &minus; base angle, and base angles are equal). Hence &Delta;BEC &cong; &Delta;CFB by A.A.S., so BE &cong; CF. Q.E.D.', 190),
    bq(U, EX4, 'EX9.4', '2', 'Prove that, if the bisector of an angle of a triangle bisects its opposite side, then the triangle will be an isosceles triangle.',
       'The triangle is isosceles (AB &cong; AC).',
       'Given: In &Delta;ABC, AD bisects &ang;A and BD &cong; DC. To prove: AB &cong; AC. Proof: Produce AD to E such that AD &cong; DE, and join C to E. In &Delta;ADB &harr; &Delta;EDC: AD &cong; DE (construction), BD &cong; DC (given) and &ang;ADB &cong; &ang;EDC (vertically opposite). So &Delta;ADB &cong; &Delta;EDC by S.A.S., giving AB &cong; EC and &ang;BAD &cong; &ang;CED. But &ang;BAD &cong; &ang;DAC (AD bisects &ang;A), so &ang;CED &cong; &ang;DAC, i.e. &ang;CEA &cong; &ang;CAE. Hence AC &cong; CE. Therefore AB &cong; CE &cong; AC, i.e. AB &cong; AC. Q.E.D.', 190),
    bq(U, EX4, 'EX9.4', '3', 'Prove that the median bisecting the base of an isosceles triangle bisects the vertical angle and is perpendicular to the base.',
       'AD bisects &ang;A and AD &perp; BC.',
       'Given: &Delta;ABC with AB &cong; AC and AD the median to base BC (BD &cong; DC). To prove: AD bisects &ang;A and AD &perp; BC. Proof: In &Delta;ABD &harr; &Delta;ACD: AB &cong; AC (given), BD &cong; DC (given), AD &cong; AD (common). Hence &Delta;ABD &cong; &Delta;ACD by S.S.S. So &ang;BAD &cong; &ang;DAC (AD bisects &ang;A) and &ang;ADB &cong; &ang;ADC. Since &ang;ADB + &ang;ADC = 180&deg; and they are equal, each equals 90&deg;; hence AD &perp; BC. Q.E.D.', 190),
    bq(U, EX4, 'EX9.4', '4', 'Prove that if three altitudes of a triangle are congruent, then the triangle is equilateral.',
       'The triangle is equilateral.',
       'Given: &Delta;ABC with altitudes AD &perp; BC, BE &perp; CA, CF &perp; AB such that AD &cong; BE &cong; CF. Proof: The area of &Delta;ABC computed from each base is equal: &frac12;(BC)(AD) = &frac12;(CA)(BE) = &frac12;(AB)(CF). Since AD &cong; BE &cong; CF, the products being equal forces BC &cong; CA &cong; AB. Hence the triangle is equilateral. Q.E.D.', 190),
]

# ============================================================== Review Exercise 9 (pdf 190-191)
ITEMS += [
    # ---- Q1 MCQ
    mcq(U, RE9, 'RE9', '1', 'If &Delta;ABC &cong; &Delta;DEF, m&ang;F is equal to (from the figure m&ang;A = 120&deg; and m&ang;B = 30&deg;):', ['90&deg;', '60&deg;', '30&deg;', '20&deg;'], 'c',
        'In &Delta;ABC, m&ang;C = 180&deg; &minus; (120&deg; + 30&deg;) = 30&deg;. Since &Delta;ABC &cong; &Delta;DEF, &ang;F corresponds to &ang;C, so m&ang;F = 30&deg;.', 190),

    # ---- Q2 True / False
    bq(U, RE9, 'RE9', '2(i)', 'True or False: The sum of the measures of all angles in a quadrilateral is 360&deg;.',
       'True', 'A quadrilateral can be divided into two triangles, so the sum of its angles is 2 &times; 180&deg; = 360&deg;.', 190),
    bq(U, RE9, 'RE9', '2(ii)', 'True or False: The sum of the measures of all angles in a triangle is 270&deg;.',
       'False', 'The sum of the angles of a triangle is 180&deg;, not 270&deg;.', 190),
    bq(U, RE9, 'RE9', '2(iii)', 'True or False: In an equilateral triangle, angles are of the same measurement.',
       'True', 'An equilateral triangle is equiangular; all three angles equal 60&deg;.', 190),
    bq(U, RE9, 'RE9', '2(iv)', 'True or False: There are two right angles in a triangle.',
       'False', 'A triangle can have at most one right angle, since the sum of the angles is only 180&deg;.', 190),
    bq(U, RE9, 'RE9', '2(v)', 'True or False: In an isosceles triangle, corresponding angles and corresponding sides are equal in measure.',
       'False', 'In an isosceles triangle only the two base angles are equal and the two legs (opposite them) are equal; not every corresponding angle and side is equal.', 190),

    # ---- Q3 Fill in the blanks
    bq(U, RE9, 'RE9', '3(i)', 'Fill in the blank: If &Delta;ABC &harr; &Delta;DEF, then AC corresponds to ________.',
       'DF', 'In the correspondence &Delta;ABC &harr; &Delta;DEF, the orders are A&harr;D, B&harr;E, C&harr;F, so side AC corresponds to side DF.', 190),
    bq(U, RE9, 'RE9', '3(ii)', 'Fill in the blank: In &Delta;KLM &harr; &Delta;PQR, then &ang;MKL corresponds to ________.',
       '&ang;RPQ', 'In &Delta;KLM &harr; &Delta;PQR we have K&harr;P, L&harr;Q, M&harr;R. The angle MKL (at K) corresponds to the angle RPQ (at P).', 190),
    bq(U, RE9, 'RE9', '3(iii)', 'Fill in the blank: In an isosceles triangle, the base angles are ________.',
       'congruent (equal)', 'The base angles of an isosceles triangle are equal in measure.', 190),
    bq(U, RE9, 'RE9', '3(iv)', 'Fill in the blank: If the measure of each angle of a triangle is 60&deg;, then the triangle is ________.',
       'equilateral', 'If all three angles are 60&deg;, all three sides are equal, so the triangle is equilateral.', 190),
    bq(U, RE9, 'RE9', '3(v)', 'Fill in the blank: In a right-angled triangle, the side opposite to the right angle is called the ________.',
       'hypotenuse', 'The side opposite the right angle in a right-angled triangle is the hypotenuse.', 190),
    bq(U, RE9, 'RE9', '3(vi)', 'Fill in the blank: The sum of the measures of the acute angles of a right triangle is ________.',
       '90&deg;', 'In a right triangle one angle is 90&deg;, so the two acute angles sum to 180&deg; &minus; 90&deg; = 90&deg;.', 190),

    # ---- Q4 Multiple choice
    mcq(U, RE9, 'RE9', '4(i)', 'Which of the following is not a sufficient condition for congruence of two triangles?', ['A.S.A &cong; A.S.A', 'H.S &cong; H.S', 'S.A.A &cong; S.A.A', 'A.A.A &cong; A.A.A'], 'd',
        'A.A.A (Angle-Angle-Angle) guarantees only similarity, not congruence, because equal angles do not fix the size of the triangles. Without a pair of corresponding equal sides, the triangles need not be congruent.', 191),
    mcq(U, RE9, 'RE9', '4(ii)', 'In &Delta;ABC, if &ang;A &cong; &ang;B, then the bisector of the ________ angle divides the triangle into two congruent triangles.', ['&ang;A', '&ang;B', '&ang;C', 'any one of its angles'], 'c',
        'Since &ang;A &cong; &ang;B, the sides opposite them are equal (CA &cong; CB). The bisector of the vertical angle &ang;C divides the isosceles &Delta;ABC into two congruent triangles (by S.A.S.).', 191),
    mcq(U, RE9, 'RE9', '4(iii)', 'The diagonal of a ________ does not divide it into two congruent triangles.', ['Rectangle', 'Trapezium', 'Parallelogram', 'Square'], 'b',
        'A diagonal of a rectangle, parallelogram or square divides it into two congruent triangles, but a diagonal of a trapezium does not (the two triangles formed are not congruent in general).', 191),
    mcq(U, RE9, 'RE9', '4(iv)', 'How many acute angles are there in an acute-angled triangle?', ['1', '2', '3', 'not more than 2'], 'c',
        'In an acute-angled triangle all three angles are acute, so there are 3 acute angles.', 191),
]
