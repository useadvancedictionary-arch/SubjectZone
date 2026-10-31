"""Unit 13 - Practical Geometry - Triangles (book pp. 223-234, PDF pp. 226-237)."""
from .common import bq, mcq

U = 13
EX1 = 'Exercise 13.1'
EX2 = 'Exercise 13.2'
EX3 = 'Exercise 13.3'
RE13 = 'Review Exercise 13'

ITEMS = []

# ============================================================== Exercise 13.1 (pdf 226-227)
ITEMS += [
    bq(U, EX1, 'EX13.1', '1', 'Construct &Delta;PQR such that m PQ = m QR = 4.6 cm and m&ang;Q = 35&deg;.',
       'Construction of an isosceles triangle with equal sides 4.6 cm and included angle 35&deg;.',
       'Steps: (i) Draw QR = 4.6 cm. (ii) At Q construct &ang;RQX = 35&deg;. (iii) With Q as centre and radius 4.6 cm, mark P on QX. (iv) Join P to R. &Delta;PQR is the required triangle.', 226),
    bq(U, EX1, 'EX13.1', '2', 'Construct &Delta;ABC such that m AB = m AC = 5.1 cm and m&ang;A = 65&deg;.',
       'Construction of an isosceles triangle with equal sides 5.1 cm and included angle 65&deg;.',
       'Steps: (i) Draw AB = 5.1 cm. (ii) At A construct &ang;BAX = 65&deg;. (iii) With A as centre and radius 5.1 cm, mark C on AX. (iv) Join B to C. &Delta;ABC is the required triangle.', 226),
    bq(U, EX1, 'EX13.1', '3', 'Construct &Delta;LMN such that m LM = 3.7 cm, m MN = 2.5 cm and &ang;M = 50&deg;.',
       'Construction of a triangle with two sides and the included angle (S.A.S.).',
       'Steps: (i) Draw LM = 3.7 cm. (ii) At M construct &ang;LMX = 50&deg;. (iii) With M as centre and radius 2.5 cm, mark N on MX. (iv) Join L to N. &Delta;LMN is the required triangle.', 226),
    bq(U, EX1, 'EX13.1', '4', 'Construct &Delta;ABC such that m AB = 3.5 cm, m BC = 2.7 cm and &ang;B = 110&deg;.',
       'Construction of a triangle with two sides and the included angle (S.A.S.).',
       'Steps: (i) Draw AB = 3.5 cm. (ii) At B construct &ang;ABX = 110&deg;. (iii) With B as centre and radius 2.7 cm, mark C on BX. (iv) Join A to C. &Delta;ABC is the required triangle.', 226),
    bq(U, EX1, 'EX13.1', '5', 'Construct &Delta;XYZ such that m XY = 4.1 cm, m YZ = 5 cm and &ang;Z = 80&deg;.',
       'Construction of a triangle with two sides and an angle opposite one of them.',
       'Steps: (i) Draw YZ = 5 cm. (ii) At Z construct &ang;YZX = 80&deg;. (iii) With Y as centre and radius 4.1 cm, draw an arc cutting ZX at X. (iv) Join X to Y. &Delta;XYZ is the required triangle.', 226),
    bq(U, EX1, 'EX13.1', '6(i)', 'Construct &Delta;DEF given m DE = 5 cm, m&ang;D = 45&deg; and m&ang;E = 60&deg;.',
       'Construction of a triangle with one side and two angles (A.S.A.).',
       'Steps: (i) Draw DE = 5 cm. (ii) At D construct &ang;XDE = 45&deg;. (iii) At E construct &ang;YED = 60&deg;. (iv) Let DX and EY meet at F. &Delta;DEF is the required triangle.', 227),
    bq(U, EX1, 'EX13.1', '6(ii)', 'Construct &Delta;LMN given m LM = 6 cm, m&ang;L = 75&deg; and m&ang;M = 45&deg;.',
       'Construction of a triangle with one side and two angles (A.S.A.).',
       'Steps: (i) Draw LM = 6 cm. (ii) At L construct &ang;XLM = 75&deg;. (iii) At M construct &ang;YML = 45&deg;. (iv) Let LX and MY meet at N. &Delta;LMN is the required triangle.', 227),
    bq(U, EX1, 'EX13.1', '6(iii)', 'Construct &Delta;ABC given m BC = 5.8 cm, m&ang;A = 30&deg; and m&ang;B = 45&deg;.',
       'Construction of a triangle (A.S.A. after finding &ang;C = 105&deg;).',
       'Steps: (i) &ang;C = 180&deg; &minus; (30&deg; + 45&deg;) = 105&deg;. (ii) Draw BC = 5.8 cm. (iii) At B construct &ang;B = 45&deg;. (iv) At C construct &ang;C = 105&deg;. (v) The two rays meet at A. &Delta;ABC is the required triangle.', 227),
    bq(U, EX1, 'EX13.1', '7(i)', 'Construct &Delta;ABC when m AC = 4.5 cm, m BC = 4.1 cm and m&ang;B = 75&deg;.',
       'Construction of a triangle with two sides and an angle opposite one of them.',
       'Steps: (i) Draw BC = 4.1 cm. (ii) At B construct &ang;CBX = 75&deg;. (iii) With C as centre and radius 4.5 cm, draw an arc cutting BX at A. (iv) Join A to C. &Delta;ABC is the required triangle.', 227),
    bq(U, EX1, 'EX13.1', '7(ii)', 'Construct &Delta;ABC when m BC = 5 cm, m AB = 5.5 cm and m&ang;C = 70&deg;.',
       'Construction of a triangle with two sides and an angle opposite one of them.',
       'Steps: (i) Draw BC = 5 cm. (ii) At C construct &ang;BCX = 70&deg;. (iii) With B as centre and radius 5.5 cm, draw an arc cutting CX at A. (iv) Join A to B. &Delta;ABC is the required triangle.', 227),
    bq(U, EX1, 'EX13.1', '7(iii)', 'Construct &Delta;ABC when m AB = 5 cm, m BC = 5.5 cm and m&ang;A = 45&deg;.',
       'Construction of a triangle with two sides and an angle opposite one of them.',
       'Steps: (i) Draw AB = 5 cm. (ii) At A construct &ang;BAX = 45&deg;. (iii) With B as centre and radius 5.5 cm, draw an arc cutting AX at C. (iv) Join B to C. &Delta;ABC is the required triangle.', 227),
]

# ============================================================== Exercise 13.2 (pdf 230)
ITEMS += [
    bq(U, EX2, 'EX13.2', '1', 'Take a triangle and draw the medians; prove that they are concurrent.',
       'The three medians are concurrent (at the centroid).',
       'Construction: Draw a triangle ABC; bisect the sides to find their mid-points D, E, F; join each vertex to the mid-point of the opposite side to obtain the medians AD, BE and CF. Conclusion: All three medians pass through a single common point G, so the medians of a triangle are concurrent. That point G is the centroid, and it divides each median in the ratio 2 : 1.', 230),
    bq(U, EX2, 'EX13.2', '2', 'Take a triangle and draw the altitudes; prove that they are concurrent.',
       'The three altitudes are concurrent (at the orthocentre).',
       'Construction: Draw a triangle ABC and construct the perpendicular from each vertex to the opposite side: AD &perp; BC, BE &perp; CA, CF &perp; AB. Conclusion: The three altitudes pass through a single common point O, so the altitudes of a triangle are concurrent. That point O is called the orthocentre.', 230),
    bq(U, EX2, 'EX13.2', '3', 'Take a triangle and draw the internal bisectors of the angles; prove that they are concurrent.',
       'The three angle bisectors are concurrent (at the incentre).',
       'Construction: Draw a triangle ABC and construct the internal bisectors of &ang;A, &ang;B and &ang;C. Conclusion: The three bisectors pass through a single common point I, so the internal bisectors of a triangle are concurrent. That point I is called the incentre, and it is equidistant from the three sides.', 230),
    bq(U, EX2, 'EX13.2', '4', 'Construct a triangle ABC in which m BC = 6 cm, m CA = 4 cm and m AB = 5 cm; draw the bisectors of angles A and B.',
       'Construction of &Delta;ABC (sides 6, 4, 5 cm) and its angle bisectors at A and B.',
       'Steps: (i) Draw BC = 6 cm. (ii) With B as centre and radius 5 cm, and with C as centre and radius 4 cm, draw arcs intersecting at A. (iii) Join A to B and A to C. (iv) Construct the bisector of &ang;A and the bisector of &ang;B; they meet at the incentre I.', 230),
    bq(U, EX2, 'EX13.2', '5', 'Construct a triangle PQR in which m PQ = 5.7 cm, m QR = 6.4 cm and m PR = 4.4 cm; draw the altitudes from vertex R and vertex Q.',
       'Construction of &Delta;PQR (sides 5.7, 6.4, 4.4 cm) and two altitudes.',
       'Steps: (i) Draw QR = 6.4 cm. (ii) With Q as centre and radius 5.7 cm, and with R as centre and radius 4.4 cm, draw arcs intersecting at P. (iii) Join P to Q and P to R. (iv) From R draw RN &perp; PQ and from Q draw QM &perp; PR; these are the required altitudes.', 230),
    bq(U, EX2, 'EX13.2', '6', 'Construct a triangle STU in which &ang;T = 60&deg;, &ang;U = 30&deg; and m TU = 7 cm. Find the perpendicular bisectors of the sides of the triangle and prove that they are concurrent.',
       'The perpendicular bisectors are concurrent (at the circumcentre).',
       'Steps: (i) Draw TU = 7 cm. (ii) At T construct &ang;T = 60&deg; and at U construct &ang;U = 30&deg;; their rays meet at S. (iii) Construct the perpendicular bisectors of ST, TU and US. Conclusion: All three perpendicular bisectors pass through a common point O, so they are concurrent. O is the circumcentre and is equidistant from S, T and U.', 230),
    bq(U, EX2, 'EX13.2', '7', 'Construct a right triangle ABC in which &ang;C = 90&deg;, &ang;B = 45&deg; and m CB = 5 cm; draw the medians of the triangle.',
       'Construction of the right triangle and its medians.',
       'Steps: (i) Draw CB = 5 cm. (ii) At C construct &ang;BCX = 90&deg;. (iii) At B construct &ang;CBY = 45&deg;; the rays CX and BY meet at A. (iv) Bisect the three sides to find their mid-points and join each vertex to the mid-point of the opposite side to obtain the three medians, which meet at the centroid G.', 230),
    bq(U, EX2, 'EX13.2', '8(i)', 'Construct &Delta;XYZ, where m YZ = 4.4 cm, m&ang;Y = 45&deg; and m&ang;Z = 75&deg;; draw its three medians and show that they are concurrent.',
       'The three medians are concurrent.',
       'Steps: (i) Draw YZ = 4.4 cm. (ii) At Y construct &ang;Y = 45&deg; and at Z construct &ang;Z = 75&deg;; the rays meet at X. (iii) Bisect each side and join each vertex to the mid-point of the opposite side to draw the three medians. All three medians pass through a single common point (the centroid), hence they are concurrent.', 230),
    bq(U, EX2, 'EX13.2', '8(ii)', 'Construct &Delta;XYZ, where m XY = 4.6 cm, m XZ = 4.6 cm and m&ang;Y = 60&deg;; draw its three medians and show that they are concurrent.',
       'The three medians are concurrent.',
       'Steps: (i) Draw XY = 4.6 cm. (ii) At Y construct &ang;Y = 60&deg;. (iii) With X as centre and radius 4.6 cm, draw an arc cutting the ray at Z. (iv) Join X to Z. (v) Bisect each side and join each vertex to the mid-point of the opposite side to draw the three medians, which meet at a single point (the centroid). Hence they are concurrent.', 230),
    bq(U, EX2, 'EX13.2', '9', 'Construct the &Delta;KLM in which m KL = 4.8 cm, m LM = 5.2 cm and m MK = 4.5 cm; draw its altitudes and verify their concurrency.',
       'The three altitudes are concurrent (orthocentre).',
       'Steps: (i) Draw LM = 5.2 cm. (ii) With L as centre radius 4.8 cm and with M as centre radius 4.5 cm, draw arcs intersecting at K. (iii) Join K to L and K to M. (iv) Draw the perpendiculars from K to LM, from L to MK and from M to KL. All three altitudes pass through a single common point O, verifying their concurrency (O is the orthocentre).', 230),
    bq(U, EX2, 'EX13.2', '10', 'Construct the &Delta;PQR in which m PQ = 7 cm, m QR = 6.5 cm and m PR = 5.8 cm; find its perpendicular bisectors and verify their concurrency.',
       'The three perpendicular bisectors are concurrent (circumcentre).',
       'Steps: (i) Draw QR = 6.5 cm. (ii) With Q as centre radius 7 cm and with R as centre radius 5.8 cm, draw arcs intersecting at P. (iii) Join P to Q and P to R. (iv) Construct the perpendicular bisectors of PQ, QR and RP. All three pass through a single common point O, verifying their concurrency (O is the circumcentre).', 230),
]

# ============================================================== Exercise 13.3 (pdf 232)
ITEMS += [
    bq(U, EX3, 'EX13.3', '1', 'Construct a rectangle whose adjacent sides are 2.5 cm and 5 cm respectively. Construct a square having area equal to the given rectangle.',
       'Square of side &radic;(2.5 &times; 5) = &radic;12.5 &asymp; 3.54 cm.',
       'The area of the rectangle = 2.5 &times; 5 = 12.5 cm<sup>2</sup>. The required square has area 12.5 cm<sup>2</sup>, so its side = &radic;12.5 &asymp; 3.54 cm. Construction: (i) Draw rectangle ABCD with AB = 5 cm, BC = 2.5 cm. (ii) Produce AB and on it mark AE = BC (so that the rectangle on AB with side BC becomes a square of side AB+...). Standard method: Produce AB to E such that BE = BC; bisect AE at M; draw a semicircle on AE; produce BC to meet the semicircle at F; then BF is the side of the required square. Construct the square on BF.', 232),
    bq(U, EX3, 'EX13.3', '2', 'Construct a square equal in area to a rectangle whose adjacent sides are 4.5 cm and 2.2 cm respectively. Measure the side of the square and find its area; compare with the area of the rectangle. Also verify that the perimeter of the square is less than that of the rectangle.',
       'Square side &asymp; 3.15 cm; area &asymp; 9.9 cm<sup>2</sup>; perimeter of square &lt; perimeter of rectangle.',
       'Area of rectangle = 4.5 &times; 2.2 = 9.9 cm<sup>2</sup>. The square of equal area has side = &radic;9.9 &asymp; 3.15 cm, so its area &asymp; 9.9 cm<sup>2</sup>, which equals the rectangle\'s area. Perimeter of square = 4 &times; 3.15 &asymp; 12.6 cm; perimeter of rectangle = 2(4.5 + 2.2) = 13.4 cm. Hence the perimeter of the square (12.6 cm) is less than that of the rectangle (13.4 cm).', 232),
    bq(U, EX3, 'EX13.3', '3', 'Construct a triangle having base 4 cm and the other two sides equal to 3.6 cm and 3.8 cm each. Transform it into a rectangle with equal area.',
       'The rectangle has area equal to that of the triangle (base &times; &frac12; height).',
       'Steps: (i) Draw AB = 4 cm. (ii) With A as centre radius 3.6 cm and with B as centre radius 3.8 cm, draw arcs meeting at C; join C to A and B. (iii) Draw CD &perp; AB (the height h). The area of the triangle is &frac12; &times; 4 &times; h. (iv) Construct a rectangle on base AD (or on a convenient side) and of the same height half... standard method: construct a rectangle whose base equals the half of AB and whose height equals CD, so that its area = &frac12; &times; AB &times; CD = area of the triangle. Hence the required rectangle has equal area to the triangle.', 232),
    bq(U, EX3, 'EX13.3', '4', 'Construct a triangle having base 6 cm and the other two sides equal to 5 cm and 6 cm each. Construct a rectangle equal in area to the given triangle.',
       'The rectangle has the same area as the triangle.',
       'Steps: (i) Draw AB = 6 cm. (ii) With A as centre radius 5 cm and with B as centre radius 6 cm, draw arcs meeting at C; join C to A and B. (iii) Draw CD &perp; AB (height h). Area of the triangle = &frac12; &times; AB &times; h = &frac12; &times; 6 &times; h = 3h cm<sup>2</sup>. (iv) Construct a rectangle with base 3 cm and height h; its area = 3 &times; h = area of the triangle. Hence the required rectangle has area equal to that of &Delta;ABC.', 232),
]

# ============================================================== Review Exercise 13 (pdf 232-233)
ITEMS += [
    # ---- Q1 Fill in the blanks
    bq(U, RE13, 'RE13', '1(i)', 'Fill in the blank: The side of a right triangle opposite to the right angle is ________.',
       'hypotenuse', 'The side opposite the right angle in a right triangle is called the hypotenuse.', 232),
    bq(U, RE13, 'RE13', '1(ii)', 'Fill in the blank: The line segment joining a vertex of a triangle and perpendicular to its opposite side is called an ________.',
       'altitude', 'A segment from a vertex perpendicular to the opposite side is an altitude of the triangle.', 232),
    bq(U, RE13, 'RE13', '1(iii)', 'Fill in the blank: A line segment drawn from a vertex of a triangle and meeting the mid-point of its opposite side is called a ________.',
       'median', 'A segment from a vertex to the mid-point of the opposite side is a median.', 232),
    bq(U, RE13, 'RE13', '1(iv)', 'Fill in the blank: The perpendicular bisectors of the sides of a triangle are ________.',
       'concurrent', 'The perpendicular bisectors of the sides of a triangle are concurrent (they meet at the circumcentre).', 232),
    bq(U, RE13, 'RE13', '1(v)', 'Fill in the blank: Two or more than two triangles are said to be congruent if they are equiangular and the measures of their corresponding sides are ________.',
       'equal', 'Congruent triangles are equiangular with equal (corresponding) sides.', 233),

    # ---- Q2 Multiple choice
    mcq(U, RE13, 'RE13', '2(i)', 'A triangle having all three sides congruent is called a ________ triangle.', ['scalene', 'right angled', 'equilateral', 'isosceles'], 'c',
        'A triangle with all three sides equal is an equilateral triangle.', 233),
    mcq(U, RE13, 'RE13', '2(ii)', 'A quadrilateral having each angle equal to 90&deg; and all sides congruent is called a ________.', ['parallelogram', 'rectangle', 'trapezium', 'square'], 'd',
        'A quadrilateral with four right angles and four equal sides is a square.', 233),
    mcq(U, RE13, 'RE13', '2(iii)', 'The medians of a triangle are ________.', ['collinear', 'congruent', 'concurrent', 'parallel'], 'c',
        'The three medians of a triangle are concurrent (they meet at the centroid).', 233),
    mcq(U, RE13, 'RE13', '2(iv)', 'The ________ altitudes of an equilateral triangle are congruent.', ['two', 'three', 'four', 'none'], 'b',
        'In an equilateral triangle all three altitudes are equal in length.', 233),
    mcq(U, RE13, 'RE13', '2(v)', 'The diagonals of a rectangle ________ each other.', ['bisect', 'trisect', 'bisect at right angle', 'none of these'], 'a',
        'The diagonals of a rectangle bisect each other (they are also equal, but they do not meet at right angles unless it is a square).', 233),
    mcq(U, RE13, 'RE13', '2(vi)', 'The ________ of a triangle cut each other in the ratio 2 : 1.', ['Altitudes', 'Angle bisectors', 'Right bisectors', 'Medians'], 'd',
        'The centroid divides each median in the ratio 2 : 1, so it is the medians that cut each other in the ratio 2 : 1.', 233),
    mcq(U, RE13, 'RE13', '2(vii)', 'If each angle on the base of an isosceles triangle is 45&deg;, then the measure of the third angle is ________.', ['30&deg;', '60&deg;', '90&deg;', '120&deg;'], 'c',
        'The two base angles are each 45&deg;, so the third angle = 180&deg; &minus; (45&deg; + 45&deg;) = 90&deg;.', 233),
    mcq(U, RE13, 'RE13', '2(viii)', 'If the three medians of a triangle are congruent, then the triangle is ________.', ['Right angled', 'equilateral', 'Isosceles', 'acute angled'], 'b',
        'If all three medians are equal, the triangle is equilateral.', 233),
    mcq(U, RE13, 'RE13', '2(ix)', 'If two ________ of a triangle are congruent, then the triangle will be isosceles.', ['Altitudes', 'Medians', 'Right bisectors', 'sides'], 'd',
        'If two sides of a triangle are congruent, then by definition the triangle is isosceles.', 233),
]
