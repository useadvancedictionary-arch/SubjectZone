"""Unit 10 - Parallelograms and Triangles (book pp. 192-202, PDF pp. 195-205)."""
from .common import bq, mcq

U = 10
EX1 = 'Exercise 10.1'
EX2 = 'Exercise 10.2'
EX3 = 'Exercise 10.3'
EX4 = 'Exercise 10.4'
EX5 = 'Exercise 10.5'
RE10 = 'Review Exercise 10'

ITEMS = []

# ============================================================== Exercise 10.1 (pdf 195)
ITEMS += [
    bq(U, EX1, 'EX10.1', '1', 'Prove that the line joining the mid-points of two opposite sides of a parallelogram is parallel to the other sides.',
       'The joining line is parallel to the other two sides.',
       'Given: ABCD is a parallelogram; M and N are the mid-points of AB and CD. To prove: MN &parallel; AD &parallel; BC. Proof: AM = &frac12;AB = &frac12;CD = DN, and AB &parallel; CD so AM &parallel; DN. Hence AMND has one pair of opposite sides equal and parallel, so it is a parallelogram. Therefore MN &parallel; AD. Since AD &parallel; BC, we get MN &parallel; AD &parallel; BC. Q.E.D.', 195),
    bq(U, EX1, 'EX10.1', '2', 'Prove that interior angles on any side of a parallelogram are supplementary.',
       'Each pair of interior angles on the same side is supplementary.',
       'Given: ABCD is a parallelogram. To prove: &ang;A + &ang;B = 180&deg; (and likewise &ang;B + &ang;C = 180&deg;, etc.). Proof: AD &parallel; BC with AB as transversal, so the interior angles on the same side are supplementary: &ang;A + &ang;B = 180&deg;. Similarly AB &parallel; CD with BC as transversal gives &ang;B + &ang;C = 180&deg;, and so on. Q.E.D.', 195),
    bq(U, EX1, 'EX10.1', '3', 'Prove that the bisectors of two angles on the same side of a parallelogram cut each other at right angle.',
       'The bisectors meet at 90&deg;.',
       'Given: ABCD is a parallelogram; the bisectors of &ang;A and &ang;B meet at P. To prove: &ang;APB = 90&deg;. Proof: Since interior angles on the same side are supplementary, &ang;A + &ang;B = 180&deg;. Also &ang;PAB = &frac12;&ang;A and &ang;PBA = &frac12;&ang;B. In &Delta;APB: &ang;APB = 180&deg; &minus; (&ang;PAB + &ang;PBA) = 180&deg; &minus; &frac12;(&ang;A + &ang;B) = 180&deg; &minus; 90&deg; = 90&deg;. Q.E.D.', 195),
    bq(U, EX1, 'EX10.1', '4', 'If the diagonals of a quadrilateral bisect each other, then prove that it is a parallelogram.',
       'The quadrilateral is a parallelogram.',
       'Given: Quadrilateral ABCD whose diagonals AC and BD bisect each other at O (AO &cong; OC, BO &cong; OD). To prove: ABCD is a parallelogram. Proof: In &Delta;AOB &harr; &Delta;COD: AO &cong; OC (given), BO &cong; OD (given) and &ang;AOB &cong; &ang;COD (vertically opposite). So &Delta;AOB &cong; &Delta;COD (S.A.S.), giving &ang;OAB &cong; &ang;OCD, which are alternate angles &rArr; AB &parallel; CD. Similarly &Delta;AOD &cong; &Delta;COB gives AD &parallel; BC. Hence ABCD is a parallelogram. Q.E.D.', 195),
    bq(U, EX1, 'EX10.1', '5', 'Prove that in a parallelogram opposite angles are congruent.',
       '&ang;A &cong; &ang;C and &ang;B &cong; &ang;D.',
       'Given: ABCD is a parallelogram. To prove: &ang;A &cong; &ang;C and &ang;B &cong; &ang;D. Proof: Consecutive angles are supplementary: &ang;A + &ang;B = 180&deg; and &ang;C + &ang;B = 180&deg;. Hence &ang;A = 180&deg; &minus; &ang;B = &ang;C, so &ang;A &cong; &ang;C. Similarly &ang;B = 180&deg; &minus; &ang;A = &ang;D, so &ang;B &cong; &ang;D. Q.E.D.', 195),
]

# ============================================================== Exercise 10.2 (pdf 196)
ITEMS += [
    bq(U, EX2, 'EX10.2', '1', 'Prove that a quadrilateral is a parallelogram if its opposite angles are congruent.',
       'The quadrilateral is a parallelogram.',
       'Given: Quadrilateral ABCD with &ang;A &cong; &ang;C and &ang;B &cong; &ang;D. To prove: ABCD is a parallelogram. Proof: The sum of the angles is 360&deg;, so &ang;A + &ang;B + &ang;C + &ang;D = 360&deg; &rArr; 2&ang;A + 2&ang;B = 360&deg; &rArr; &ang;A + &ang;B = 180&deg;. These are consecutive interior angles, so AD &parallel; BC. Similarly &ang;B + &ang;C = 180&deg; gives AB &parallel; CD. Hence ABCD is a parallelogram. Q.E.D.', 196),
    bq(U, EX2, 'EX10.2', '2', 'Prove that a quadrilateral is a parallelogram if its diagonals bisect each other.',
       'The quadrilateral is a parallelogram.',
       'Given: Quadrilateral ABCD whose diagonals AC and BD bisect each other at O. To prove: ABCD is a parallelogram. Proof: In &Delta;AOB &harr; &Delta;COD: AO &cong; OC, BO &cong; OD and &ang;AOB &cong; &ang;COD (vertically opposite). So &Delta;AOB &cong; &Delta;COD (S.A.S.), giving &ang;OAB &cong; &ang;OCD &rArr; AB &parallel; CD. Similarly &Delta;AOD &cong; &Delta;COB gives AD &parallel; BC. Hence ABCD is a parallelogram. Q.E.D.', 196),
    bq(U, EX2, 'EX10.2', '3', 'Prove that if both pairs of opposite sides of a quadrilateral are congruent, then the quadrilateral is a parallelogram.',
       'The quadrilateral is a parallelogram.',
       'Given: Quadrilateral ABCD with AB &cong; CD and AD &cong; BC. To prove: ABCD is a parallelogram. Proof: Draw the diagonal BD. In &Delta;ABD &harr; &Delta;CDB: AB &cong; CD (given), AD &cong; CB (given), BD &cong; BD (common). So &Delta;ABD &cong; &Delta;CDB (S.S.S.), giving &ang;ABD &cong; &ang;CDB and &ang;ADB &cong; &ang;CBD. These are pairs of alternate angles, so AB &parallel; CD and AD &parallel; BC. Hence ABCD is a parallelogram. Q.E.D.', 196),
    bq(U, EX2, 'EX10.2', '4', 'Prove that if a quadrilateral is a parallelogram, its diagonals form two congruent triangles.',
       'Each diagonal divides the parallelogram into two congruent triangles.',
       'Given: ABCD is a parallelogram with diagonal AC. To prove: &Delta;ABC &cong; &Delta;CDA. Proof: AB &cong; CD and BC &cong; DA (opposite sides of a parallelogram are congruent), and AC &cong; AC (common). Hence &Delta;ABC &cong; &Delta;CDA by S.S.S. Similarly, diagonal BD gives &Delta;ABD &cong; &Delta;CDB. Q.E.D.', 196),
    bq(U, EX2, 'EX10.2', '5', 'Prove that if the angles formed with every side of a quadrilateral are supplementary, then it is a parallelogram.',
       'The quadrilateral is a parallelogram.',
       'Given: Quadrilateral ABCD in which the interior angles on each side are supplementary, e.g. &ang;A + &ang;B = 180&deg; and &ang;B + &ang;C = 180&deg;. To prove: ABCD is a parallelogram. Proof: &ang;A + &ang;B = 180&deg; means the interior angles on the same side of the line AB are supplementary, so AD &parallel; BC. Similarly &ang;B + &ang;C = 180&deg; gives AB &parallel; CD. Hence ABCD is a parallelogram. Q.E.D.', 196),
]

# ============================================================== Exercise 10.3 (pdf 197)
ITEMS += [
    bq(U, EX3, 'EX10.3', '1', 'If the line segment joining the mid-points of two sides of a triangle is parallel to the third side and its length is 4 cm, what is the length of the third side?',
       '8 cm',
       'The segment joining the mid-points of two sides of a triangle is equal to half the third side. So 4 = &frac12;(third side) &rArr; third side = 8 cm.', 197),
    bq(U, EX3, 'EX10.3', '2', 'Prove that the line segments joining the mid-points of the opposite sides of a quadrilateral bisect each other.',
       'The two joining segments bisect each other.',
       'Given: Quadrilateral ABCD with P, Q, R, S the mid-points of AB, BC, CD, DA. To prove: the segments PR and QS bisect each other. Proof: In &Delta;ABC, PQ joins the mid-points of AB and BC, so PQ &parallel; AC and PQ = &frac12;AC. In &Delta;ADC, SR joins the mid-points of AD and DC, so SR &parallel; AC and SR = &frac12;AC. Thus PQ &parallel; SR and PQ &cong; SR, so PQRS is a parallelogram. The diagonals of a parallelogram bisect each other, hence PR and QS bisect each other. Q.E.D.', 197),
    bq(U, EX3, 'EX10.3', '3', 'Prove that the line segments joining the mid-points of the sides of a quadrilateral, taken in order, form a parallelogram.',
       'PQRS is a parallelogram (Varignon parallelogram).',
       'Given: Quadrilateral ABCD with P, Q, R, S the mid-points of AB, BC, CD, DA. To prove: PQRS is a parallelogram. Proof: In &Delta;ABC, PQ joins mid-points so PQ &parallel; AC and PQ = &frac12;AC. In &Delta;ADC, SR joins mid-points so SR &parallel; AC and SR = &frac12;AC. Hence PQ &parallel; SR and PQ &cong; SR, so one pair of opposite sides of PQRS are equal and parallel; therefore PQRS is a parallelogram. Q.E.D.', 197),
    bq(U, EX3, 'EX10.3', '4', 'Prove that the line segment passing through the mid-point of one side and parallel to another side of a triangle also bisects the third side.',
       'The line bisects the third side.',
       'Given: &Delta;ABC with M the mid-point of AB; through M a line is drawn parallel to BC meeting AC at N. To prove: N is the mid-point of AC. Proof: The segment joining the mid-points of AB and AC is parallel to BC. Through M there is only one line parallel to BC, so this segment must be MN. Hence N is the mid-point of AC, i.e. the line bisects AC. Q.E.D.', 197),
    bq(U, EX3, 'EX10.3', '5', 'Prove that the four triangles obtained by joining the mid-points of the three sides of a triangle are all congruent to each other.',
       'All four small triangles are congruent.',
       'Given: &Delta;ABC with D, E, F the mid-points of BC, CA, AB. To prove: &Delta;AFE &cong; &Delta;FBD &cong; &Delta;EDC &cong; &Delta;DEF. Proof: By the mid-point theorem, EF = &frac12;BC = BD = DC, FD = &frac12;AC = AE = EC and DE = &frac12;AB = AF = FB. Each of the four triangles therefore has sides &frac12;AB, &frac12;BC, &frac12;CA. Hence all four triangles are congruent by S.S.S. Q.E.D.', 197),
]

# ============================================================== Exercise 10.4 (pdf 199)
ITEMS += [
    bq(U, EX4, 'EX10.4', '1', 'If the three medians of a triangle are congruent, prove that the triangle is equilateral.',
       'The triangle is equilateral.',
       'Given: &Delta;ABC with medians of lengths m<sub>a</sub>, m<sub>b</sub>, m<sub>c</sub> such that m<sub>a</sub> = m<sub>b</sub> = m<sub>c</sub>. Proof: Using m<sub>a</sub> = &frac12;&radic;(2b<sup>2</sup> + 2c<sup>2</sup> &minus; a<sup>2</sup>), the equality m<sub>a</sub> = m<sub>b</sub> gives 2b<sup>2</sup> + 2c<sup>2</sup> &minus; a<sup>2</sup> = 2c<sup>2</sup> + 2a<sup>2</sup> &minus; b<sup>2</sup> &rArr; 3b<sup>2</sup> = 3a<sup>2</sup> &rArr; a = b. Similarly m<sub>b</sub> = m<sub>c</sub> gives b = c. Hence a = b = c and the triangle is equilateral. Q.E.D.', 199),
    bq(U, EX4, 'EX10.4', '2', 'The medians PB, QC and RA of &Delta;PQR meet at point G. Show that G is the centroid of &Delta;PQR.',
       'G is the centroid of &Delta;PQR.',
       'Since PB, QC and RA are the three medians of &Delta;PQR and they are concurrent at G, and by definition the point of concurrency of the medians of a triangle is its centroid, G is the centroid of &Delta;PQR. Moreover, by Theorem 10.1.4 the centroid G is the point of trisection of each median, so PG : GB = QG : GC = RG : GA = 2 : 1. Q.E.D.', 199),
    bq(U, EX4, 'EX10.4', '3', 'In the given figure, the length of GR is 2 cm; find the length of AG.',
       'AG = 1 cm',
       'G is the centroid, so it divides the median RA in the ratio RG : GA = 2 : 1. Given GR = 2 cm, we get GA = &frac12; &times; 2 = 1 cm. Hence AG = 1 cm.', 199),
]

# ============================================================== Exercise 10.5 (pdf 203)
ITEMS += [
    bq(U, EX5, 'EX10.5', '1', 'The triangle formed by joining the mid-points of the sides of a triangle is similar to (equivalent in shape to) the original triangle.',
       'The medial triangle is similar to the original triangle (each side is half, area one-fourth).',
       'Given: &Delta;ABC with D, E, F the mid-points of BC, CA, AB. To prove: &Delta;DEF is similar to &Delta;ABC. Proof: By the mid-point theorem, DE &parallel; AB, EF &parallel; BC and FD &parallel; CA. Hence the corresponding angles are equal (e.g. &ang;DEF = &ang;B, &ang;DFE = &ang;A), so &Delta;DEF ~ &Delta;ABC. Also each side of &Delta;DEF is half the corresponding side of &Delta;ABC, so the area of &Delta;DEF is one-fourth the area of &Delta;ABC. Q.E.D.', 203),
    bq(U, EX5, 'EX10.5', '2', 'Prove that the line segment joining the mid-points of the non-parallel sides of a trapezium is parallel to the parallel sides and is equal to half their sum.',
       'The median of the trapezium = &frac12;(sum of parallel sides) and is parallel to them.',
       'Given: Trapezium ABCD with AB &parallel; DC; M, N are the mid-points of the non-parallel sides AD, BC. To prove: MN &parallel; AB &parallel; DC and MN = &frac12;(AB + DC). Proof: Draw diagonal AC, meeting MN at P. In &Delta;ADC, M is the mid-point of AD and MP &parallel; DC, so P is the mid-point of AC and MP = &frac12;DC. In &Delta;ABC, P is the mid-point of AC and N is the mid-point of BC, so PN &parallel; AB and PN = &frac12;AB. Thus M, P, N are collinear, MN &parallel; AB &parallel; DC, and MN = MP + PN = &frac12;DC + &frac12;AB = &frac12;(AB + DC). Q.E.D.', 203),
    bq(U, EX5, 'EX10.5', '3', 'Prove that every line segment drawn from the vertex to the base of a triangle is bisected by the line joining the mid-points of the other two sides.',
       'The mid-segment bisects any cevian from the vertex to the base.',
       'Given: &Delta;ABC with M, N the mid-points of AB, AC; a segment from A meets BC at D and meets MN at E. To prove: AE &cong; ED (MN bisects AD). Proof: MN joins the mid-points of AB and AC, so MN &parallel; BC, hence ME &parallel; BD. In &Delta;ABD, M is the mid-point of AB and ME &parallel; BD, so by the converse of the mid-point theorem E is the mid-point of AD. Hence AE &cong; ED. Q.E.D.', 203),
]

# ============================================================== Review Exercise 10 (pdf 203-204)
ITEMS += [
    # ---- Q1 Fill in the blanks
    bq(U, RE10, 'RE10', '1(i)', 'Fill in the blank: In a parallelogram, opposite sides are ________.',
       'congruent (equal)', 'The opposite sides of a parallelogram are equal in length (congruent).', 203),
    bq(U, RE10, 'RE10', '1(ii)', 'Fill in the blank: In a parallelogram, opposite angles are ________.',
       'congruent (equal)', 'The opposite (and corresponding) angles of a parallelogram are equal in measure.', 203),
    bq(U, RE10, 'RE10', '1(iii)', 'Fill in the blank: In a triangle, medians are ________.',
       'concurrent', 'The three medians of a triangle are concurrent (they meet at a single point, the centroid).', 203),
    bq(U, RE10, 'RE10', '1(iv)', 'Fill in the blank: In a parallelogram, the diagonals ________ each other.',
       'bisect', 'The diagonals of a parallelogram bisect each other.', 203),
    bq(U, RE10, 'RE10', '1(v)', 'Fill in the blank: In a parallelogram, corresponding angles are ________.',
       'equal', 'Corresponding (and opposite) angles of a parallelogram are equal in measure.', 203),
    bq(U, RE10, 'RE10', '1(vi)', 'Fill in the blank: The sum of the measures of the interior angles of a quadrilateral is equal to ________.',
       '360&deg;', 'A quadrilateral can be split into two triangles, so the sum of its interior angles is 2 &times; 180&deg; = 360&deg;.', 203),

    # ---- Q2 Multiple choice
    mcq(U, RE10, 'RE10', '2(i)', 'The diagonals of a square are ________ to each other.', ['Perpendicular', 'Non congruent', 'Congruent', "Both 'a' and 'c'"], 'd',
        'The diagonals of a square are equal (congruent) and they bisect each other at right angles (perpendicular). Hence both (a) and (c) are correct.', 204),
    mcq(U, RE10, 'RE10', '2(ii)', 'The sum of the measures of the interior angles of a quadrilateral is:', ['2 right angles', '4 right angles', '3 right angles', 'none of these'], 'b',
        'The sum of the interior angles of a quadrilateral is 360&deg; = 4 right angles.', 204),
    mcq(U, RE10, 'RE10', '2(iii)', 'The measure of the line segment joining the mid-points of AB and AC of &Delta;ABC is 3.5 cm, then m BC =', ['4.5 cm', '5.5 cm', '6 cm', '7 cm'], 'd',
        'The mid-segment equals half the third side: 3.5 = &frac12;(BC) &rArr; BC = 7 cm.', 204),
    mcq(U, RE10, 'RE10', '2(iv)', 'Two medians AD and BE of &Delta;ABC intersect each other at G. If m GD = 1.7 cm, then m AG =', ['2.7 cm', '8.85 cm', '3.4 cm', '5.1 cm'], 'c',
        'The centroid G divides a median in the ratio 2 : 1, so AG = 2 &times; GD = 2 &times; 1.7 = 3.4 cm.', 204),
    mcq(U, RE10, 'RE10', '2(v)', 'If the sum of the measures of &ang;A and &ang;C of a parallelogram ABCD is 130&deg;, then m&ang;B =', ['25&deg;', '115&deg;', '65&deg;', 'none of these'], 'b',
        'In a parallelogram &ang;A &cong; &ang;C, so each = 65&deg;. Consecutive angles are supplementary: &ang;B = 180&deg; &minus; 65&deg; = 115&deg;.', 204),
    mcq(U, RE10, 'RE10', '2(vi)', 'If the opposite angles of a quadrilateral are equal in measure and none of them is a right angle, then the quadrilateral is a:', ['Square', 'Parallelogram', 'Trapezium', 'Rectangle'], 'b',
        'A quadrilateral with both pairs of opposite angles equal is a parallelogram. Since none of the angles is a right angle, it is not a rectangle or square, so it is a (non-rectangular) parallelogram.', 204),
    mcq(U, RE10, 'RE10', '2(vii)', 'Centroid is the common point of intersection of:', ['Medians of a triangle', 'Diagonals of a parallelogram', 'Angle bisectors of a triangle', 'Perpendicular bisectors of a triangle'], 'a',
        'The centroid is the point of concurrency of the three medians of a triangle.', 204),
    mcq(U, RE10, 'RE10', '2(viii)', 'A point on a median of a triangle is:', ['equidistant from its vertices', 'equidistant from the mid-points of its sides', 'equidistant from its altitudes', 'none of these'], 'd',
        'None of the listed properties holds for an arbitrary point on a median. (The circumcentre, not a general median point, is equidistant from the vertices, and it need not lie on a median.) Hence the correct option is (d) none of these.', 204),
]
