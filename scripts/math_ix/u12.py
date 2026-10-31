"""Unit 12 - Sides and Angles of a Triangle (book pp. 214-222, PDF pp. 217-225)."""
from .common import bq, mcq

U = 12
EX1 = 'Exercise 12.1'
RE12 = 'Review Exercise 12'

ITEMS = []

# ============================================================== Exercise 12.1 (pdf 221)
ITEMS += [
    bq(U, EX1, 'EX12.1', '1', 'O is an interior point of the &Delta;ABC. Show that m OA + m OB + m OC &gt; &frac12;(m AB + m BC + m CA).',
       'OA + OB + OC &gt; &frac12;(AB + BC + CA).',
       'Proof: By the triangle inequality: in &Delta;AOB, OA + OB &gt; AB; in &Delta;BOC, OB + OC &gt; BC; in &Delta;COA, OC + OA &gt; CA. Adding these three inequalities gives 2(OA + OB + OC) &gt; AB + BC + CA, hence OA + OB + OC &gt; &frac12;(AB + BC + CA). Q.E.D.', 221),
    bq(U, EX1, 'EX12.1', '2', 'In &Delta;ABC, m&ang;B = 70&deg; and m&ang;C = 45&deg;. Which of the sides of the triangle is the longest?',
       'Side AC is the longest.',
       'The third angle is &ang;A = 180&deg; &minus; (70&deg; + 45&deg;) = 65&deg;. The greatest angle is &ang;B = 70&deg;, and the side opposite the greatest angle is the longest. The side opposite &ang;B is AC. Hence AC is the longest side.', 221),
    bq(U, EX1, 'EX12.1', '3', 'In &Delta;ABC, m&ang;A = 55&deg; and m&ang;B = 65&deg;. Which of the sides of the triangle is the smallest?',
       'Side BC is the smallest.',
       'The third angle is &ang;C = 180&deg; &minus; (55&deg; + 65&deg;) = 60&deg;. The smallest angle is &ang;A = 55&deg;, and the side opposite the smallest angle is the smallest. The side opposite &ang;A is BC. Hence BC is the smallest side.', 221),
]

# ============================================================== Review Exercise 12 (pdf 221-222)
ITEMS += [
    # ---- Q1 True / False
    bq(U, RE12, 'RE12', '1(i)', 'True or False: The sum of the two sides of a triangle is greater than the third side.',
       'True', 'This is the triangle inequality: the sum of the lengths of any two sides of a triangle is greater than the third side.', 221),
    bq(U, RE12, 'RE12', '1(ii)', 'True or False: The difference of two sides of a triangle is larger than the third side.',
       'False', 'The difference of any two sides of a triangle is always less than the third side (from the triangle inequality), so the statement is false.', 221),
    bq(U, RE12, 'RE12', '1(iii)', 'True or False: The perpendicular distance from a point to a line is the longest distance between them.',
       'False', 'The perpendicular from a point to a line is the shortest (not longest) distance from the point to the line.', 221),
    bq(U, RE12, 'RE12', '1(iv)', 'True or False: In a right-angled triangle the largest angle is of 100&deg;.',
       'False', 'In a right-angled triangle the largest angle is the right angle, 90&deg;, not 100&deg;.', 221),
    bq(U, RE12, 'RE12', '1(v)', 'True or False: A perpendicular on a line always makes an angle of 90&deg;.',
       'True', 'By definition a perpendicular to a line meets it at 90&deg;.', 221),

    # ---- Q2 Fill in the blanks
    bq(U, RE12, 'RE12', '2(i)', 'Fill in the blank: In any right-angled triangle, ________ is the longest side of the triangle.',
       'hypotenuse', 'The hypotenuse (the side opposite the right angle) is the longest side of a right-angled triangle.', 221),
    bq(U, RE12, 'RE12', '2(ii)', 'Fill in the blank: In a right-angled triangle, the sum of the measures of the sides containing the right angle is ________ than the measure of the hypotenuse.',
       'greater', 'The two legs add up to more than the hypotenuse (triangle inequality), so the sum is greater.', 221),
    bq(U, RE12, 'RE12', '2(iii)', 'Fill in the blank: In &Delta;ABC, m&ang;A = 50&deg; and m&ang;B = 30&deg;. Side ________ will be longer than its other sides.',
       'AB', 'The third angle is &ang;C = 180&deg; &minus; (50&deg; + 30&deg;) = 100&deg;, the greatest angle. The side opposite the greatest angle is the longest, and AB is opposite &ang;C. Hence side AB is the longest.', 221),
    bq(U, RE12, 'RE12', '2(iv)', 'Fill in the blank: The length of a diagonal of any quadrilateral is ________ than the sum of the measures of its two adjacent sides.',
       'smaller (less)', 'Considering the triangle formed by the diagonal and two adjacent sides, the diagonal is less than the sum of the other two sides (triangle inequality).', 221),

    # ---- Q3 Multiple choice
    mcq(U, RE12, 'RE12', '3(i)', 'The measure of one side of an equilateral triangle is 6 cm; then the length of its median is ________ 9 cm.', ['less than', 'greater than', 'equal to', 'none of the above'], 'a',
        'The median of an equilateral triangle of side a is (&radic;3/2)a = (&radic;3/2)&times;6 = 3&radic;3 &asymp; 5.2 cm, which is less than 9 cm.', 222),
    mcq(U, RE12, 'RE12', '3(ii)', 'The perimeter of a rectangle is 22 cm; then the length of its diagonal is ________ 11 cm.', ['equal to', 'greater than', 'less than', 'none of the above'], 'c',
        'Perimeter 22 cm means the sum of two adjacent sides is 11 cm. The diagonal is the hypotenuse of the right triangle formed by the two adjacent sides, so it is less than their sum, i.e. less than 11 cm.', 222),
]
