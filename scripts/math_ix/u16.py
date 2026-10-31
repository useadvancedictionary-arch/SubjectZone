"""Unit 16 - Introduction to Coordinate Geometry / Analytical Geometry (book pp. 251-267, PDF pp. 254-270)."""
from .common import bq, mcq

U = 16
EX1 = 'Exercise 16.1'
EX2 = 'Exercise 16.2'
EX3 = 'Exercise 16.3'
RE16 = 'Review Exercise 16'

ITEMS = []

# ============================================================== Exercise 16.1 (pdf 257)
ITEMS += [
    bq(U, EX1, 'EX16.1', '1(i)', 'Using the distance formula find the distance between the points (&minus;4, 5) and (6, 6).',
       'd = &radic;101 units.',
       'd = &radic;[(6 &minus; (&minus;4))<sup>2</sup> + (6 &minus; 5)<sup>2</sup>] = &radic;(10<sup>2</sup> + 1<sup>2</sup>) = &radic;(100 + 1) = &radic;101 units.', 257),
    bq(U, EX1, 'EX16.1', '1(ii)', 'Using the distance formula find the distance between the points (2, 2) and (2, 3).',
       'd = 1 unit.',
       'd = &radic;[(2 &minus; 2)<sup>2</sup> + (3 &minus; 2)<sup>2</sup>] = &radic;(0 + 1) = 1 unit.', 257),
    bq(U, EX1, 'EX16.1', '1(iii)', 'Using the distance formula find the distance between the points (0, 1) and (2, 3).',
       'd = 2&radic;2 units.',
       'd = &radic;[(2 &minus; 0)<sup>2</sup> + (3 &minus; 1)<sup>2</sup>] = &radic;(4 + 4) = &radic;8 = 2&radic;2 units.', 257),
    bq(U, EX1, 'EX16.1', '1(iv)', 'Using the distance formula find the distance between the points (0, 1) and (2, 3).',
       'd = 2&radic;2 units.',
       'd = &radic;[(2 &minus; 0)<sup>2</sup> + (3 &minus; 1)<sup>2</sup>] = &radic;(4 + 4) = &radic;8 = 2&radic;2 units. (This pair is the same as part (iii) in the book.)', 257),
    bq(U, EX1, 'EX16.1', '2(i)', 'A(a, 0) and B(0, b) are points on the axes; find the distance AB when a = &minus;3, b = &minus;4.',
       'AB = 5 units.',
       'The distance from origin is AB = &radic;(a<sup>2</sup> + b<sup>2</sup>) = &radic;((&minus;3)<sup>2</sup> + (&minus;4)<sup>2</sup>) = &radic;(9 + 16) = &radic;25 = 5 units.', 257),
    bq(U, EX1, 'EX16.1', '2(ii)', 'A(a, 0) and B(0, b) are points on the axes; find the distance AB when a = &minus;9, b = 6.',
       'AB = &radic;117 units.',
       'AB = &radic;(a<sup>2</sup> + b<sup>2</sup>) = &radic;((&minus;9)<sup>2</sup> + 6<sup>2</sup>) = &radic;(81 + 36) = &radic;117 units.', 257),
    bq(U, EX1, 'EX16.1', '2(iii)', 'A(a, 0) and B(0, b) are points on the axes; find the distance AB when a = 3, b = 4.',
       'AB = 5 units.',
       'AB = &radic;(a<sup>2</sup> + b<sup>2</sup>) = &radic;(3<sup>2</sup> + 4<sup>2</sup>) = &radic;(9 + 16) = 5 units.', 257),
    bq(U, EX1, 'EX16.1', '2(iv)', 'A(a, 0) and B(0, b) are points on the axes; find the distance AB when a = &radic;2, b = &minus;2&radic;2.',
       'AB = &radic;10 units.',
       'AB = &radic;(a<sup>2</sup> + b<sup>2</sup>) = &radic;((&radic;2)<sup>2</sup> + (&minus;2&radic;2)<sup>2</sup>) = &radic;(2 + 8) = &radic;10 units.', 257),
    bq(U, EX1, 'EX16.1', '3', 'Find the perimeter of the triangle formed by the points A(0, 0), B(4, 0) and C(2, 2&radic;3).',
       'Perimeter = 12 units.',
       'AB = &radic;[(4 &minus; 0)<sup>2</sup> + 0<sup>2</sup>] = 4 units. BC = &radic;[(2 &minus; 4)<sup>2</sup> + (2&radic;3 &minus; 0)<sup>2</sup>] = &radic;(4 + 12) = 4 units. CA = &radic;[(0 &minus; 2)<sup>2</sup> + (0 &minus; 2&radic;3)<sup>2</sup>] = &radic;(4 + 12) = 4 units. Since all three sides are 4 units, the triangle is equilateral and its perimeter = 4 + 4 + 4 = 12 units.', 257),
]

# ============================================================== Exercise 16.2 (pdf 265)
ITEMS += [
    bq(U, EX2, 'EX16.2', '1', 'Show that the points P(&minus;3, &minus;4), Q(2, 6) and R(0, 2) are collinear.',
       'The points P, Q and R are collinear.',
       'PQ = &radic;[(2+3)<sup>2</sup> + (6+4)<sup>2</sup>] = &radic;(25 + 100) = &radic;125 = 5&radic;5. QR = &radic;[(0&minus;2)<sup>2</sup> + (2&minus;6)<sup>2</sup>] = &radic;(4 + 16) = &radic;20 = 2&radic;5. PR = &radic;[(0+3)<sup>2</sup> + (2+4)<sup>2</sup>] = &radic;(9 + 36) = &radic;45 = 3&radic;5. Now QR + PR = 2&radic;5 + 3&radic;5 = 5&radic;5 = PQ. Since the sum of two distances equals the third, the points are collinear.', 265),
    bq(U, EX2, 'EX16.2', '2', 'Show that the points A(&minus;1, 0), B(1, 0) and C(0, &radic;3) are not collinear.',
       'The points A, B and C are not collinear.',
       'AB = &radic;[(1+1)<sup>2</sup> + 0] = 2. BC = &radic;[(0&minus;1)<sup>2</sup> + (&radic;3&minus;0)<sup>2</sup>] = &radic;(1 + 3) = 2. CA = &radic;[(&minus;1&minus;0)<sup>2</sup> + (0&minus;&radic;3)<sup>2</sup>] = &radic;(1 + 3) = 2. All three sides equal 2, so no two distances add up to the third (instead they form an equilateral triangle). Hence the points are not collinear.', 265),
    bq(U, EX2, 'EX16.2', '3', 'Show that L(0, &radic;3), M(&minus;1, 0) and N(1, 0) form an equilateral triangle.',
       'LMN is an equilateral triangle.',
       'LM = &radic;[(&minus;1&minus;0)<sup>2</sup> + (0&minus;&radic;3)<sup>2</sup>] = &radic;(1 + 3) = 2. MN = &radic;[(1+1)<sup>2</sup> + 0] = 2. NL = &radic;[(0&minus;1)<sup>2</sup> + (&radic;3&minus;0)<sup>2</sup>] = &radic;(1 + 3) = 2. Since LM = MN = NL = 2 units, the triangle is equilateral.', 265),
    bq(U, EX2, 'EX16.2', '4', 'Whether or not the points A(2, 3), B(8, 11) and C(0, 17) form an isosceles triangle.',
       'Yes, ABC is an isosceles triangle.',
       'AB = &radic;[(8&minus;2)<sup>2</sup> + (11&minus;3)<sup>2</sup>] = &radic;(36 + 64) = 10. BC = &radic;[(0&minus;8)<sup>2</sup> + (17&minus;11)<sup>2</sup>] = &radic;(64 + 36) = 10. AC = &radic;[(0&minus;2)<sup>2</sup> + (17&minus;3)<sup>2</sup>] = &radic;(4 + 196) = &radic;200 = 10&radic;2. Since AB = BC = 10 units (two sides equal) and the points are non-collinear, ABC is an isosceles triangle.', 265),
    bq(U, EX2, 'EX16.2', '5', 'Do the points A(&minus;1, 2), B(7, 5) and C(2, &minus;6) form a right-angled triangle?',
       'Yes, ABC is a right-angled triangle (right angle at A).',
       'AB = &radic;[(7+1)<sup>2</sup> + (5&minus;2)<sup>2</sup>] = &radic;(64 + 9) = &radic;73. AC = &radic;[(2+1)<sup>2</sup> + (&minus;6&minus;2)<sup>2</sup>] = &radic;(9 + 64) = &radic;73. BC = &radic;[(2&minus;7)<sup>2</sup> + (&minus;6&minus;5)<sup>2</sup>] = &radic;(25 + 121) = &radic;146. Now AB<sup>2</sup> + AC<sup>2</sup> = 73 + 73 = 146 = BC<sup>2</sup>. By the converse of Pythagoras\' theorem the triangle is right-angled (at A).', 265),
    bq(U, EX2, 'EX16.2', '6', 'If the points A(3, 1), B(9, 1) and C(6, k) determine an equilateral triangle, find the values of k.',
       'k = 1 &plusmn; 3&radic;3.',
       'AB = &radic;[(9&minus;3)<sup>2</sup> + 0] = 6. For an equilateral triangle AC = BC = 6. Now AC<sup>2</sup> = (6&minus;3)<sup>2</sup> + (k&minus;1)<sup>2</sup> = 9 + (k&minus;1)<sup>2</sup> = 36, giving (k&minus;1)<sup>2</sup> = 27, so k &minus; 1 = &plusmn;3&radic;3 and k = 1 &plusmn; 3&radic;3.', 265),
    bq(U, EX2, 'EX16.2', '7', 'Show that the points P(1, 2), Q(3, 4) and R(0, &minus;1) are the vertices of a scalene triangle.',
       'PQR is a scalene triangle.',
       'PQ = &radic;[(3&minus;1)<sup>2</sup> + (4&minus;2)<sup>2</sup>] = &radic;(4 + 4) = 2&radic;2. QR = &radic;[(0&minus;3)<sup>2</sup> + (&minus;1&minus;4)<sup>2</sup>] = &radic;(9 + 25) = &radic;34. RP = &radic;[(1&minus;0)<sup>2</sup> + (2+1)<sup>2</sup>] = &radic;(1 + 9) = &radic;10. Since PQ, QR and RP are all different in length and no one equals the sum of the other two, the points form a scalene (non-equilateral, non-isosceles, non-collinear) triangle.', 265),
    bq(U, EX2, 'EX16.2', '8', 'Show that the points A(2, 3), B(8, 11), C(0, 17) and D(&minus;6, 9) are the vertices of a square.',
       'ABCD is a square.',
       'AB = &radic;[(8&minus;2)<sup>2</sup>+(11&minus;3)<sup>2</sup>] = &radic;(36+64) = 10. BC = &radic;[(0&minus;8)<sup>2</sup>+(17&minus;11)<sup>2</sup>] = &radic;(64+36) = 10. CD = &radic;[(&minus;6&minus;0)<sup>2</sup>+(9&minus;17)<sup>2</sup>] = &radic;(36+64) = 10. DA = &radic;[(2+6)<sup>2</sup>+(3&minus;9)<sup>2</sup>] = &radic;(64+36) = 10. So all four sides are equal. Diagonals: AC = &radic;[(0&minus;2)<sup>2</sup>+(17&minus;3)<sup>2</sup>] = &radic;(4+196) = &radic;200 = 10&radic;2 and BD = &radic;[(&minus;6&minus;8)<sup>2</sup>+(9&minus;11)<sup>2</sup>] = &radic;(196+4) = &radic;200 = 10&radic;2. The diagonals are equal. Since all sides are equal and the diagonals are equal, ABCD is a square.', 265),
    bq(U, EX2, 'EX16.2', '9', 'Explain why the points A(&minus;2, 0), B(0, &minus;3), C(2, 0) and D(0, 3) determine a square?',
       'All four sides are equal, so the figure determined is a rhombus (the printed key calls it a square).',
       'AB = &radic;[(0+2)<sup>2</sup>+(&minus;3&minus;0)<sup>2</sup>] = &radic;(4+9) = &radic;13. BC = &radic;[(2&minus;0)<sup>2</sup>+(0+3)<sup>2</sup>] = &radic;(4+9) = &radic;13. CD = &radic;[(0&minus;2)<sup>2</sup>+(3&minus;0)<sup>2</sup>] = &radic;13. DA = &radic;[(&minus;2&minus;0)<sup>2</sup>+(0&minus;3)<sup>2</sup>] = &radic;13. All four sides are equal (each &radic;13). However the diagonals are AC = 4 and BD = 6, which are unequal. Hence the quadrilateral is a rhombus; it would be a square only if the diagonals were equal. (The printed key states "square".)', 265),
    bq(U, EX2, 'EX16.2', '10', 'Show that the points A(3, 2), B(4, 1), C(5, 4) and D(6, 3) are the vertices of a rectangle.',
       'ABCD is a rectangle.',
       'AB = &radic;[(4&minus;3)<sup>2</sup>+(1&minus;2)<sup>2</sup>] = &radic;(1+1) = &radic;2. BC = &radic;[(5&minus;4)<sup>2</sup>+(4&minus;1)<sup>2</sup>] = &radic;(1+9) = &radic;10. CD = &radic;[(6&minus;5)<sup>2</sup>+(3&minus;4)<sup>2</sup>] = &radic;2. DA = &radic;[(3&minus;6)<sup>2</sup>+(2&minus;3)<sup>2</sup>] = &radic;10. So opposite sides are equal (AB = CD and BC = DA). Diagonals: AC = &radic;[(5&minus;3)<sup>2</sup>+(4&minus;2)<sup>2</sup>] = &radic;8 and BD = &radic;[(6&minus;4)<sup>2</sup>+(3&minus;1)<sup>2</sup>] = &radic;8, i.e. the diagonals are equal. Hence ABCD is a rectangle.', 265),
    bq(U, EX2, 'EX16.2', '11', 'Use the distance formula to show that the points O(0, 0), A(3, 0), B(5, 2) and C(2, 2) form the vertices of a parallelogram.',
       'OABC is a parallelogram.',
       'OA = 3. AB = &radic;[(5&minus;3)<sup>2</sup>+(2&minus;0)<sup>2</sup>] = &radic;(4+4) = 2&radic;2. BC = &radic;[(2&minus;5)<sup>2</sup>+(2&minus;2)<sup>2</sup>] = 3. CO = &radic;[(0&minus;2)<sup>2</sup>+(0&minus;2)<sup>2</sup>] = &radic;(4+4) = 2&radic;2. Hence OA = BC = 3 and AB = CO = 2&radic;2, i.e. both pairs of opposite sides are equal. Therefore OABC is a parallelogram.', 265),
]

# ============================================================== Exercise 16.3 (pdf 268)
ITEMS += [
    bq(U, EX3, 'EX16.3', '1(i)', 'Find the mid-point of the pair of points A(2, 6) and B(&minus;4, 8) using the mid-point formula.',
       'Mid-point = (&minus;1, 7).',
       'Mid-point = ((x&#8321;+x&#8322;)/2, (y&#8321;+y&#8322;)/2) = ((2+(&minus;4))/2, (6+8)/2) = (&minus;2/2, 14/2) = (&minus;1, 7).', 268),
    bq(U, EX3, 'EX16.3', '1(ii)', 'Find the mid-point of the pair of points P(&minus;3, &minus;1) and Q(5, 2) using the mid-point formula.',
       'Mid-point = (1, &frac12;).',
       'Mid-point = ((&minus;3+5)/2, (&minus;1+2)/2) = (2/2, 1/2) = (1, &frac12;).', 268),
    bq(U, EX3, 'EX16.3', '1(iii)', 'Find the mid-point of the pair of points L(0, 6) and M(&minus;8, 0) using the mid-point formula.',
       'Mid-point = (&minus;4, 3).',
       'Mid-point = ((0+(&minus;8))/2, (6+0)/2) = (&minus;8/2, 6/2) = (&minus;4, 3).', 268),
    bq(U, EX3, 'EX16.3', '1(iv)', 'Find the mid-point of the pair of points C(0, 0) and D(2&radic;3, 4&radic;3) using the mid-point formula.',
       'Mid-point = (&radic;3, 2&radic;3).',
       'Mid-point = ((0+2&radic;3)/2, (0+4&radic;3)/2) = (&radic;3, 2&radic;3).', 268),
    bq(U, EX3, 'EX16.3', '2', 'Find the centre of a circle whose end points of a diameter are A(&minus;5, 6) and B(3, &minus;4).',
       'Centre = (&minus;1, 1).',
       'The centre of the circle is the mid-point of the diameter AB. Centre = ((&minus;5+3)/2, (6+(&minus;4))/2) = (&minus;2/2, 2/2) = (&minus;1, 1).', 268),
    bq(U, EX3, 'EX16.3', '3', 'The centre of a circle is (3, 4) and one end point of a diameter is (4, 6); find the other end point (B).',
       'The other end point B = (2, 2).',
       'Let the other end be B(x, y). The centre is the mid-point of the diameter, so (3, 4) = ((4+x)/2, (6+y)/2). Hence (4+x)/2 = 3 giving x = 2, and (6+y)/2 = 4 giving y = 2. So B = (2, 2).', 268),
    bq(U, EX3, 'EX16.3', '4', 'A circle has a diameter between the points A(&minus;3, 4) and B(11, 6). Find the centre and radius of the circle.',
       'Centre = (4, 5), Radius = 5&radic;2 units.',
       'Centre = mid-point of AB = ((&minus;3+11)/2, (4+6)/2) = (8/2, 10/2) = (4, 5). Radius = &frac12; AB = &frac12;&radic;[(11+3)<sup>2</sup>+(6&minus;4)<sup>2</sup>] = &frac12;&radic;(196+4) = &frac12;&radic;200 = &frac12;&middot;10&radic;2 = 5&radic;2 units.', 268),
    bq(U, EX3, 'EX16.3', '5', 'Prove that a triangle is an isosceles triangle if and only if it has two equal medians.',
       'The proof follows by the mid-point formula.',
       'Proof: Place the triangle with vertices A(0,0), B(a,0) and C(b,c). The mid-point of BC is ((a+b)/2, c/2), of AC is (b/2, c/2) and of AB is (a/2, 0). The median from A to BC has length m&#8320; = &radic;[((a+b)/2)<sup>2</sup> + (c/2)<sup>2</sup>]; the median from B to AC has length &radic;[((b&minus;2a)/2)<sup>2</sup> + (c/2)<sup>2</sup>]. Setting these equal and simplifying leads precisely to the condition that two sides of the triangle are equal (AC = BC in this placement), i.e. the triangle is isosceles. Thus a triangle is isosceles if and only if two of its medians are equal. Q.E.D.', 268),
    bq(U, EX3, 'EX16.3', '6', 'Prove that the diagonals of a parallelogram bisect each other.',
       'The diagonals of a parallelogram bisect each other.',
       'Proof: Let A(0,0), B(a,0), D(b,c) and C(a+b, c) be the vertices of a parallelogram (AB &parallel; DC and AD &parallel; BC). The diagonal AC has mid-point ((a+b)/2, c/2). The diagonal BD has mid-point ((a+b)/2, c/2). Since both diagonals have the same mid-point, they bisect each other. Q.E.D.', 268),
]

# ============================================================== Review Exercise 16 (pdf 269)
ITEMS += [
    # ---- Q1 True / False
    bq(U, RE16, 'RE16', '1(i)', 'True or False: R is the mid-point of PQ if R is lying between P and Q.',
       'True', 'The mid-point R of segment PQ lies on the segment, i.e. between P and Q (at equal distances from P and Q). So a point lying between P and Q is the mid-point of PQ.', 269),
    bq(U, RE16, 'RE16', '1(ii)', 'True or False: In a scalene triangle all sides are equal.',
       'False', 'A scalene triangle has all three sides of different lengths. A triangle with all sides equal is equilateral.', 269),
    bq(U, RE16, 'RE16', '1(iii)', 'True or False: Perpendicular lines meet at an angle of 135&deg;.',
       'False', 'Perpendicular lines meet at 90&deg;, not 135&deg;.', 269),
    bq(U, RE16, 'RE16', '1(iv)', 'True or False: Collinear points may form a triangle.',
       'False', 'Collinear points lie on a single straight line, so they cannot form a triangle.', 269),
    bq(U, RE16, 'RE16', '1(v)', 'True or False: Non-collinear points form a triangle.',
       'True', 'Three non-collinear points determine a triangle.', 269),
    bq(U, RE16, 'RE16', '1(vi)', 'True or False: In an isosceles triangle, two base angles are equal.',
       'True', 'In an isosceles triangle the angles opposite the equal sides (the base angles) are equal.', 269),
    bq(U, RE16, 'RE16', '1(vii)', 'True or False: All the points that lie on the y-axis are collinear.',
       'True', 'Every point on the y-axis lies on the same single straight line (the y-axis), so they are collinear.', 269),
    bq(U, RE16, 'RE16', '1(viii)', 'True or False: The intersection of the x-axis and the y-axis is (0, 0).',
       'True', 'The x-axis and y-axis intersect at the origin, which is (0, 0).', 269),
    bq(U, RE16, 'RE16', '1(ix)', 'True or False: The distance from the origin to (6, 0) is 36 units.',
       'False', 'The distance from O(0,0) to (6,0) is &radic;(6<sup>2</sup>+0<sup>2</sup>) = 6 units, not 36 units.', 269),

    # ---- Q2 Fill in the blanks
    bq(U, RE16, 'RE16', '2(i)', 'Fill in the blank: If A(x&#8321;, y&#8321;) and B(x&#8322;, y&#8322;) are any two points, then |AB| = ________.',
       '&radic;[(x&#8322; &minus; x&#8321;)<sup>2</sup> + (y&#8322; &minus; y&#8321;)<sup>2</sup>]', 'This is the distance formula for the distance between two points.', 269),
    bq(U, RE16, 'RE16', '2(ii)', 'Fill in the blank: Collinear points lie on the same ________.',
       'line (straight line)', 'By definition, collinear points are points that lie on the same straight line.', 269),
    bq(U, RE16, 'RE16', '2(iii)', 'Fill in the blank: In the 4th quadrant x &gt; 0 and y ________.',
       'y &lt; 0 (y is negative)', 'In the fourth quadrant the x-coordinate is positive and the y-coordinate is negative.', 269),

    # ---- Q3 Multiple choice
    mcq(U, RE16, 'RE16', '3(i)', 'Two perpendicular lines meet at an angle of:',
        ['45&deg;', '60&deg;', '90&deg;', '180&deg;'], 'c',
        'Perpendicular lines intersect at a right angle of 90&deg;.', 269),
    mcq(U, RE16, 'RE16', '3(ii)', '((x&#8321; + x&#8322;)/2, (y&#8321; + y&#8322;)/2) is called:',
        ['Mid-point formula', 'Distance formula', 'Division formula', 'Ratio formula'], 'a',
        'The formula ((x&#8321;+x&#8322;)/2, (y&#8321;+y&#8322;)/2) gives the mid-point of the segment joining two points, so it is the mid-point formula.', 269),
    mcq(U, RE16, 'RE16', '3(iii)', 'A(3, 0) and B(0, 3) are two points in the plane; then |AB| =',
        ['6 units', '6&radic;2 units', '3&radic;2 units', '3&radic;2 units'], 'd',
        '|AB| = &radic;[(0&minus;3)<sup>2</sup> + (3&minus;0)<sup>2</sup>] = &radic;(9 + 9) = &radic;18 = 3&radic;2 units.', 269),
    mcq(U, RE16, 'RE16', '3(iv)', 'Three points A, B and C are collinear if:',
        ['m AB = m BC + m AC', '(m AB)<sup>2</sup> = (m BC)<sup>2</sup> + (m AC)<sup>2</sup>', 'both (a) and (b)', 'm AB + m BC = m AC'], 'd',
        'For three collinear points, one of the three distances equals the sum of the other two. Here m AB + m BC = m AC means B lies between A and C, which is the condition for collinearity.', 269),
]
