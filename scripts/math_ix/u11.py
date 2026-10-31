"""Unit 11 - Line Bisectors and Angle Bisectors (book pp. 203-213, PDF pp. 206-216)."""
from .common import bq, mcq

U = 11
EX1 = 'Exercise 11.1'
EX2 = 'Exercise 11.2'
EX3 = 'Exercise 11.3'
RE11 = 'Review Exercise 11'

ITEMS = []

# ============================================================== Exercise 11.1 (pdf 207)
ITEMS += [
    bq(U, EX1, 'EX11.1', '1', 'Prove that the point of intersection of the right bisectors of any two sides of a triangle is equidistant from all the vertices of the triangle.',
       'The point is equidistant from all three vertices.',
       'Given: &Delta;ABC with the right bisectors of AB and AC meeting at O. To prove: OA &cong; OB &cong; OC. Proof: O lies on the right bisector of AB, so OA &cong; OB. O also lies on the right bisector of AC, so OA &cong; OC. Hence OA &cong; OB &cong; OC, i.e. O is equidistant from the three vertices. Q.E.D.', 207),
    bq(U, EX1, 'EX11.1', '2', 'Prove that the centre of a circle is on the right bisectors of each of its chords.',
       'The centre lies on the right bisector of every chord.',
       'Given: A circle with centre O and a chord AB. To prove: O lies on the right bisector of AB. Proof: OA &cong; OB (radii of the same circle). A point equidistant from the two ends of a line segment lies on the right bisector of that segment. Hence O lies on the right bisector of AB. As AB is an arbitrary chord, the result holds for every chord. Q.E.D.', 207),
    bq(U, EX1, 'EX11.1', '3', 'Where will be the centre of a circle passing through three non-collinear points, and why?',
       'At the point of intersection of the right bisectors of the segments joining the points.',
       'Let A, B, C be three non-collinear points. Draw the right bisectors of AB and BC; let them meet at O. Since O lies on the right bisector of AB, OA &cong; OB; since O lies on the right bisector of BC, OB &cong; OC. Hence OA &cong; OB &cong; OC, so O is equidistant from A, B and C. Therefore a circle with centre O and radius OA passes through all three points, i.e. the centre is the point of intersection of the right bisectors of the segments joining the points.', 207),
    bq(U, EX1, 'EX11.1', '4', 'If two circles intersect each other at points A and B, prove that the line passing through their centres will be the right bisector of AB.',
       'The line of centres is the right bisector of the common chord AB.',
       'Given: Two circles with centres O and O&prime; intersecting at A and B. To prove: OO&prime; is the right bisector of AB. Proof: OA &cong; OB (radii of the same circle) and O&prime;A &cong; O&prime;B (radii of the same circle). Thus each of O and O&prime; is equidistant from A and B, so each lies on the right bisector of AB. Since two points determine a line, the line OO&prime; is the right bisector of AB. Q.E.D.', 207),
    bq(U, EX1, 'EX11.1', '5', 'Three markets A, B and C are not on the same line. The business men of these markets want to construct a Masjid at a place equidistant from these markets. Prove that this place is equidistant from all three markets.',
       'The Masjid is at the circumcentre of &Delta;ABC (intersection of right bisectors of AB, BC, CA).',
       'The required point must be equidistant from A, B and C. Join A, B and C to form &Delta;ABC. Draw the right bisectors of AB and AC; let them meet at O. Since O is on the right bisector of AB, OA &cong; OB; since O is on the right bisector of AC, OA &cong; OC. Hence OA &cong; OB &cong; OC. Therefore the Masjid built at O is equidistant from all three markets. Q.E.D.', 207),
]

# ============================================================== Exercise 11.2 (pdf 208)
ITEMS += [
    bq(U, EX2, 'EX11.2', '1', 'Prove that in an acute triangle the circumcentre falls in the interior of the triangle.',
       'The circumcentre lies inside an acute triangle.',
       'Let O be the circumcentre of &Delta;ABC. Then &ang;BOC = 2&ang;A, &ang;COA = 2&ang;B and &ang;AOB = 2&ang;C (angle at the centre is twice the angle at the circumference). Since &Delta;ABC is acute, &ang;A, &ang;B, &ang;C are each less than 90&deg;, so each central angle (&ang;BOC, &ang;COA, &ang;AOB) is less than 180&deg;. When all three central angles are less than 180&deg;, the centre O lies strictly inside the triangle. Hence in an acute triangle the circumcentre falls in the interior. Q.E.D.', 208),
    bq(U, EX2, 'EX11.2', '2', 'Prove that the right bisectors of the four sides of an isosceles trapezium are concurrent.',
       'All four right bisectors pass through one point.',
       'Given: An isosceles trapezium ABCD with AB &parallel; DC and AD &cong; BC. To prove: the right bisectors of AB, BC, CD, DA are concurrent. Proof: Every isosceles trapezium is cyclic; let O be the centre of its circumcircle. Then OA &cong; OB &cong; OC &cong; OD (radii). Since O is equidistant from the endpoints of each side, O lies on the right bisector of each of the four sides. Hence all four right bisectors pass through O, i.e. they are concurrent. Q.E.D.', 208),
    bq(U, EX2, 'EX11.2', '3', 'Prove that the altitudes of a triangle are concurrent.',
       'The three altitudes of a triangle are concurrent (at the orthocentre).',
       'Given: &Delta;ABC with altitudes AD &perp; BC, BE &perp; CA, CF &perp; AB. To prove: AD, BE and CF are concurrent. Proof: Through A draw a line parallel to BC, through B a line parallel to CA and through C a line parallel to AB; these lines form a larger triangle A&prime;B&prime;C&prime; in which A, B, C are the mid-points of the sides B&prime;C&prime;, C&prime;A&prime;, A&prime;B&prime; respectively. Since AD &perp; BC and BC &parallel; B&prime;C&prime;, we get AD &perp; B&prime;C&prime;; and A is the mid-point of B&prime;C&prime;. Hence AD is the right bisector of B&prime;C&prime;. Similarly BE and CF are the right bisectors of C&prime;A&prime; and A&prime;B&prime;. The right bisectors of a triangle are concurrent, so AD, BE and CF are concurrent. Q.E.D.', 208),
]

# ============================================================== Exercise 11.3 (pdf 212)
ITEMS += [
    bq(U, EX3, 'EX11.3', '1', 'Two isosceles triangles have a common base; prove that the line joining the vertices bisects the common base at right angle.',
       'The line joining the vertices is the right bisector of the common base.',
       'Given: Isosceles &Delta;ABC and &Delta;DBC on the same base BC, with AB &cong; AC and DB &cong; DC. To prove: AD bisects BC at right angles. Proof: In &Delta;ABC, AB &cong; AC, so A is equidistant from B and C and lies on the right bisector of BC. In &Delta;DBC, DB &cong; DC, so D also lies on the right bisector of BC. Hence the line AD is the right bisector of BC, i.e. it bisects BC at right angles. Q.E.D.', 212),
    bq(U, EX3, 'EX11.3', '2', 'If the bisector of an angle of a triangle bisects the opposite side, prove that the triangle is isosceles.',
       'The triangle is isosceles (AB &cong; AC).',
       'Given: In &Delta;ABC, AD bisects &ang;A and BD &cong; DC. To prove: AB &cong; AC. Proof: Produce AD to E such that AD &cong; DE, and join C to E. In &Delta;ADB &harr; &Delta;EDC: AD &cong; DE (construction), BD &cong; DC (given) and &ang;ADB &cong; &ang;EDC (vertically opposite). So &Delta;ADB &cong; &Delta;EDC (S.A.S.), giving &ang;BAD &cong; &ang;CED and AB &cong; EC. But &ang;BAD &cong; &ang;DAC (AD bisects &ang;A), so &ang;CED &cong; &ang;DAC, i.e. &ang;CEA &cong; &ang;CAE, whence AC &cong; CE. Hence AB &cong; EC &cong; AC, so AB &cong; AC. Q.E.D.', 212),
    bq(U, EX3, 'EX11.3', '3', 'In an isosceles &Delta;ABC, m AB = m AC. Prove that the perpendiculars from the vertices B and C to their opposite sides are equal.',
       'BE &cong; CF.',
       'Given: &Delta;ABC with AB &cong; AC; BE &perp; AC and CF &perp; AB. To prove: BE &cong; CF. Proof: In &Delta;BEC &harr; &Delta;CFB: &ang;BEC &cong; &ang;CFB (= 90&deg;); BC &cong; BC (common); and &ang;EBC &cong; &ang;FCB (each equals 90&deg; &minus; a base angle, and the base angles are equal). Hence &Delta;BEC &cong; &Delta;CFB (A.A.S.), so BE &cong; CF. Q.E.D.', 212),
]

# ============================================================== Review Exercise 11 (pdf 212-213)
ITEMS += [
    # ---- Q1-Q2 proofs
    bq(U, RE11, 'RE11', '1', 'Prove that, if two altitudes of a triangle are congruent, the triangle is an isosceles.',
       'The triangle is isosceles.',
       'Given: &Delta;ABC with altitudes BE &perp; AC and CF &perp; AB such that BE &cong; CF. To prove: &Delta;ABC is isosceles. Proof: The area of &Delta;ABC is &frac12;(AC)(BE) = &frac12;(AB)(CF). Since BE &cong; CF, we get AC &cong; AB. Hence the triangle is isosceles. Q.E.D.', 212),
    bq(U, RE11, 'RE11', '2', 'Prove that a point in the interior of a triangle equidistant from all three sides lies on the bisector of all the three angles of the triangle.',
       'The point lies on the bisectors of all three angles.',
       'Given: A point P inside &Delta;ABC that is equidistant from the three sides AB, BC and CA. To prove: P lies on the bisectors of &ang;A, &ang;B and &ang;C. Proof: Since P is equidistant from the arms AB and AC of &ang;A, by the converse of the angle-bisector theorem P lies on the bisector of &ang;A. Similarly, being equidistant from the arms of &ang;B, P lies on the bisector of &ang;B; and being equidistant from the arms of &ang;C, P lies on the bisector of &ang;C. Hence P lies on the bisectors of all three angles. Q.E.D.', 212),

    # ---- Q3 True / False
    bq(U, RE11, 'RE11', '3(i)', "Write 'T' for True or 'F' for False: Bisection of a side means we divide the given side into two equal parts.",
       'True', 'To bisect a side means to divide it into two equal parts.', 212),
    bq(U, RE11, 'RE11', '3(ii)', "Write 'T' for True or 'F' for False: In a right-angled isosceles triangle each angle on the base is 45&deg;.",
       'True', 'A right-angled isosceles triangle has one angle 90&deg; and two equal base angles; each base angle = (180&deg; &minus; 90&deg;)/2 = 45&deg;.', 212),
    bq(U, RE11, 'RE11', '3(iii)', "Write 'T' for True or 'F' for False: A triangle of congruent sides has congruent angles.",
       'True', 'If the sides of a triangle are congruent (equal), the angles opposite them are also congruent (equal).', 212),

    # ---- Q4 Multiple choice
    mcq(U, RE11, 'RE11', '4(i)', 'There are ________ acute angles in an acute-angled triangle.', ['One', 'Two', 'Three', 'None'], 'c',
        'In an acute-angled triangle all three angles are acute, so there are three acute angles.', 213),
    mcq(U, RE11, 'RE11', '4(ii)', 'A point equidistant from the end points of a line segment is on the ________ of it.', ['Right bisector', 'Perpendicular', 'Centre', 'Mid-point'], 'a',
        'The set of all points equidistant from the ends of a segment is its right (perpendicular) bisector.', 213),
    mcq(U, RE11, 'RE11', '4(iii)', '________ of the sides of an acute-angled triangle intersect each other inside the triangle.', ['Perpendicular', 'The right bisector', 'Obtuse', 'Acute'], 'b',
        'The right bisectors of the sides of an acute triangle meet (intersect) at a point inside the triangle (its circumcentre).', 213),
    mcq(U, RE11, 'RE11', '4(iv)', 'The bisectors of the angles of a triangle are ________.', ['Concurrent', 'Collinear', 'Do not intersect', 'Unequal'], 'a',
        'The bisectors of the three angles of a triangle are concurrent (they meet at the incentre).', 213),
]
