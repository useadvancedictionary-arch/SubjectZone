"""Unit 14 - Theorems Related with Area (book pp. 235-242, PDF pp. 238-245)."""
from .common import bq, mcq

U = 14
EX1 = 'Exercise 14.1'
RE14 = 'Review Exercise 14'

ITEMS = []

# ============================================================== Exercise 14.1 (pdf 243)
ITEMS += [
    bq(U, EX1, 'EX14.1', '1', 'In the given figure ABCD is a parallelogram and EFCD is a rectangle, also AL &perp; DC. Prove that (i) &#9632;ABCD = &#9632;EFCD, (ii) &#9632;ABCD = mDC &times; mAL.',
       '(i) &#9632;ABCD = &#9632;EFCD.  (ii) &#9632;ABCD = mDC &times; mAL.',
       'Proof (i): ABCD is a parallelogram and EFCD is a rectangle on the same base DC and between the same parallels DC and AF (since AE and DF are parallel to the base DC). By Theorem 14.1.1, parallelograms on the same base and between the same parallel lines are equal in area, so &#9632;ABCD = &#9632;EFCD. Q.E.D.  Proof (ii): &#9632;EFCD is a rectangle, so its area = length &times; breadth = mDC &times; mED. Since AL &perp; DC and ED &perp; DC, AL and ED are each the perpendicular distance between the parallels DC and AF, hence mED = mAL. Therefore &#9632;ABCD = &#9632;EFCD = mDC &times; mAL. Q.E.D.', 243,
       figure='u14_ex141_q1'),
    bq(U, EX1, 'EX14.1', '2', 'In the given figure, if the diagonals of a quadrilateral separate it into four triangles of equal area, show that it is a parallelogram.',
       'The quadrilateral ABCD is a parallelogram.',
       'Proof: Let the diagonals AC and BD of quadrilateral ABCD meet at O and let &#9632;AOB = &#9632;BOC = &#9632;COD = &#9632;DOA (all equal in area). Consider &#9632;ABC: the median BO (O is the midpoint of AC because BO divides &#9632;ABC into two equal triangles AOB and BOC) meets AC at O. Similarly, from &#9632;BOC and &#9632;COD equal in area, O is the midpoint of BD. Since the diagonals AC and BD bisect each other at O, the quadrilateral ABCD is a parallelogram. Q.E.D.', 243,
       figure='u14_ex141_q2'),
    bq(U, EX1, 'EX14.1', '3', 'In the given figure BC &parallel; AD. ABC is a right-angled triangle at vertex B with mBC = 7 cm and mAC = 11 cm; also &Delta;ABC and &Delta;BCD are on the same base BC. Find the area of &Delta;BCD.',
       'Area of &Delta;BCD = 21&radic;2 cm<sup>2</sup>.',
       'Since &Delta;ABC is right-angled at B, mAB = &radic;(mAC<sup>2</sup> &minus; mBC<sup>2</sup>) = &radic;(11<sup>2</sup> &minus; 7<sup>2</sup>) = &radic;(121 &minus; 49) = &radic;72 = 6&radic;2 cm. So area of &Delta;ABC = &frac12; &times; mBC &times; mAB = &frac12; &times; 7 &times; 6&radic;2 = 21&radic;2 cm<sup>2</sup>. Because BC &parallel; AD, the triangles ABC and BCD stand on the same base BC and between the same parallel lines, so by Theorem 14.1.3 they are equal in area. Hence area of &Delta;BCD = 21&radic;2 cm<sup>2</sup>.', 243,
       figure='u14_ex141_q3'),
    bq(U, EX1, 'EX14.1', '4', 'Show that a median of a triangle divides it into two triangles of equal area.',
       'A median divides the triangle into two triangles of equal area.',
       'Proof: In &Delta;ABC let AD be the median to BC, so D is the midpoint of BC, i.e. mBD = mDC. Drop the perpendicular (altitude) from A to BC; let its length be h. Then area of &Delta;ABD = &frac12; &times; mBD &times; h and area of &Delta;ADC = &frac12; &times; mDC &times; h. Since mBD = mDC, the two areas are equal. Hence &#9650;ABD = &#9650;ADC. Q.E.D.', 243),
    bq(U, EX1, 'EX14.1', '5', 'Show that the line segment joining the mid-points of the opposite sides of a rectangle divides it into two equal rectangles.',
       'The two resulting rectangles are equal in area.',
       'Proof: Let ABCD be a rectangle and let E and F be the mid-points of the opposite sides AD and BC respectively. The segment EF is perpendicular to AD and BC and is parallel to AB and DC. So ABFE and EFCD are both rectangles on equal bases mAE = mED (since E is the midpoint of AD) and having the same altitude mAB = mDC. By Theorem 14.1.2 (parallelograms on equal bases and of equal altitudes are equal in area), &#9632;ABFE = &#9632;EFCD. Hence the rectangle is divided into two equal rectangles. Q.E.D.', 243),
    bq(U, EX1, 'EX14.1', '6', 'If two parallelograms of equal areas have the same or equal bases, their altitudes are equal.',
       'The altitudes of the two parallelograms are equal.',
       'Proof: Let ABCD and EFGH be two parallelograms with equal areas, &#9632;ABCD = &#9632;EFGH, on equal bases mBC = mFG, with altitudes h&#8321; and h&#8322; respectively. Area = base &times; altitude, so &#9632;ABCD = mBC &times; h&#8321; and &#9632;EFGH = mFG &times; h&#8322;. Since the areas and the bases are equal, mBC &times; h&#8321; = mFG &times; h&#8322; gives h&#8321; = h&#8322;. Hence the altitudes are equal. Q.E.D.', 243),
    bq(U, EX1, 'EX14.1', '7', 'Show that an angle bisector of an equilateral triangle divides it into two triangles of equal areas.',
       'The angle bisector divides the equilateral triangle into two triangles of equal area.',
       'Proof: Let ABC be an equilateral triangle with mAB = mBC = mCA, and let the bisector of &ang;A meet BC at D. In an equilateral triangle the angle bisector of a vertex is also the median to the opposite side, so D is the midpoint of BC, i.e. mBD = mDC. Using the common altitude from A to BC (length h), area of &Delta;ABD = &frac12; &times; mBD &times; h = &frac12; &times; mDC &times; h = area of &Delta;ADC. Hence &#9650;ABD = &#9650;ADC, i.e. the two triangles have equal areas. Q.E.D.', 243),
    bq(U, EX1, 'EX14.1', '8', 'Prove that a rhombus is divided by its diagonals into four triangles of equal areas.',
       'Each of the four triangles has equal area.',
       'Proof: Let the diagonals of rhombus ABCD meet at O. The diagonals of a rhombus bisect each other at right angles, so O is the midpoint of both AC and BD. Consider &Delta;ABC: BO is a median (O is the midpoint of AC), so it divides &Delta;ABC into two equal-area triangles &#9650;AOB = &#9650;BOC. Similarly in &Delta;BCD, CO is a median (O is the midpoint of BD), so &#9650;BOC = &#9650;COD, and likewise &#9650;COD = &#9650;DOA. Thus &#9650;AOB = &#9650;BOC = &#9650;COD = &#9650;DOA; the rhombus is divided by its diagonals into four triangles of equal area. Q.E.D.', 243),
]

# ============================================================== Review Exercise 14 (pdf 244-245)
ITEMS += [
    # ---- Q1 True / False (pdf 244)
    bq(U, RE14, 'RE14', '1(i)', 'True or False: Area of a closed figure means the region enclosed by the bounding lines of the figure.',
       'True', 'By definition the area of a closed figure is the measure of the region enclosed by its boundary (bounding) lines.', 244),
    bq(U, RE14, 'RE14', '1(ii)', 'True or False: A diagonal of a rectangle divides it into two congruent triangles.',
       'True', 'A diagonal of a rectangle divides it into two right-angled triangles that are congruent (S.A.S.), since opposite sides are equal and each angle is 90&deg;.', 244),
    bq(U, RE14, 'RE14', '1(iii)', 'True or False: Congruent figures have different areas.',
       'False', 'Congruent figures are exactly alike in shape and size, so they always have equal areas, not different areas.', 244),
    bq(U, RE14, 'RE14', '1(iv)', 'True or False: The area of a parallelogram is equal to the product of base and height.',
       'True', 'The area of a parallelogram equals base &times; perpendicular height (its altitude).', 244),
    bq(U, RE14, 'RE14', '1(v)', 'True or False: Median of a triangle means the perpendicular from a vertex to the opposite side (base).',
       'False', 'A median joins a vertex to the midpoint of the opposite side. The perpendicular from a vertex to the opposite side is the altitude, not the median.', 244),
    bq(U, RE14, 'RE14', '1(vi)', 'True or False: Perpendicular distance between two parallel lines can sometimes be different.',
       'False', 'The perpendicular distance between two parallel lines is the same (constant) everywhere along them.', 244),
    bq(U, RE14, 'RE14', '1(vii)', 'True or False: An altitude drawn from a vertex always bisects the opposite side.',
       'False', 'An altitude is perpendicular to the opposite side but does not necessarily bisect it. (It bisects the opposite side only in special triangles such as isosceles or equilateral.)', 244),
    bq(U, RE14, 'RE14', '1(viii)', 'True or False: Two triangles are equal in area, if they have the same base and equal altitude.',
       'True', 'By Theorem 14.1.3 / 14.1.4, triangles on the same (or equal) bases and of equal altitudes are equal in area.', 244),

    # ---- Q2 Multiple choice (pdf 244-245)
    mcq(U, RE14, 'RE14', '2(i)', 'If the perpendicular distance between two lines is the same, the lines are ________.',
        ['Perpendicular to each other', 'Parallel to each other', 'Intersecting to each other', 'None of these'], 'b',
        'Two lines whose perpendicular distance is the same (constant) everywhere are parallel to each other.', 244),
    mcq(U, RE14, 'RE14', '2(ii)', 'If two triangles have equal areas then they will ________ be congruent as well.',
        ['Not necessarily', 'Necessarily', 'Definitely', 'None of these'], 'a',
        'Equal areas do not force equal shapes. Two triangles of equal area need not be congruent (e.g. a tall thin triangle and a short wide triangle can have the same area). Hence they are "not necessarily" congruent. (Note: the printed key gives "Necessarily", which is mathematically incorrect.)', 244),
    mcq(U, RE14, 'RE14', '2(iii)', 'Perpendicular from a vertex of a triangle to its opposite side is called ________.',
        ['Median', 'Perpendicular bisector', 'Altitude', 'Angle bisector'], 'c',
        'The perpendicular drawn from a vertex of a triangle to its opposite side (the base) is called the altitude of the triangle.', 244),
    mcq(U, RE14, 'RE14', '2(iv)', 'Parallelograms having the same base and the same altitude are ________.',
        ['Congruent', 'Equal in areas', 'Similar', 'All of these'], 'b',
        'By Theorem 14.1.1 / 14.1.2, parallelograms on the same base and between the same parallels (of the same altitude) are equal in area. They need not be congruent or similar, so the correct answer is "equal in areas". (Note: the printed key gives "All of these", which is mathematically incorrect.)', 245),
    mcq(U, RE14, 'RE14', '2(v)', 'Two parallelograms have equal bases. They will have the same area, if ________.',
        ['Their altitudes are equal', 'Their altitude is the same', 'They lie between the same parallel lines', 'All of these'], 'd',
        'All three conditions describe the same requirement: equal bases and equal altitudes (i.e. lying between the same parallel lines) give equal areas by Theorem 14.1.2. So all of these are correct.', 245),
    mcq(U, RE14, 'RE14', '2(vi)', '&Delta;ABC and &Delta;DEF have equal bases and equal altitudes, then the triangles are ________.',
        ['Equal in area', 'Congruent', 'Similar', 'None of these'], 'a',
        'By Theorem 14.1.4, triangles on equal bases and of equal altitudes are equal in area. Equal bases and altitudes do not make them congruent or similar. (Note: the printed key gives "Congruent", which is mathematically incorrect.)', 245),
]
