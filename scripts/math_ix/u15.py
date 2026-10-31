"""Unit 15 - Projection of a Side of a Triangle (book pp. 243-250, PDF pp. 246-253)."""
from .common import bq, mcq

U = 15
EX1 = 'Exercise 15.1'
EX2 = 'Exercise 15.2'
RE15 = 'Review Exercise 15'

ITEMS = []

# ============================================================== Exercise 15.1 (pdf 249)
ITEMS += [
    bq(U, EX1, 'EX15.1', '1(i)', 'Find the length of AB and the area of &Delta;ABC when mAC = 3 cm, mBC = 6 cm and m&ang;C = 120&deg;.',
       'mAB = 3&radic;7 cm, Area = 9&radic;3 / 2 cm<sup>2</sup>.',
       'The obtuse angle is at C. By the law of cosines on &Delta;ABC, AB<sup>2</sup> = AC<sup>2</sup> + BC<sup>2</sup> &minus; 2&middot;AC&middot;BC&middot;cos C = 3<sup>2</sup> + 6<sup>2</sup> &minus; 2&middot;3&middot;6&middot;cos120&deg; = 9 + 36 &minus; 36&middot;(&minus;&frac12;) = 45 + 18 = 63. So mAB = &radic;63 = 3&radic;7 cm. Area = &frac12;&middot;AC&middot;BC&middot;sin C = &frac12;&middot;3&middot;6&middot;sin120&deg; = 9&middot;(&radic;3/2) = 9&radic;3/2 cm<sup>2</sup>.', 249),
    bq(U, EX1, 'EX15.1', '1(ii)', 'Find the length of AB and the area of &Delta;ABC when mAC = 40 mm, mBC = 80 mm and m&ang;C = 120&deg;.',
       'mAB = 4&radic;7 cm (40&radic;7 mm), Area = 8&radic;3 cm<sup>2</sup>.',
       'Convert to cm: AC = 4 cm, BC = 8 cm; the obtuse angle is at C. By the law of cosines, AB<sup>2</sup> = AC<sup>2</sup> + BC<sup>2</sup> &minus; 2&middot;AC&middot;BC&middot;cos C = 4<sup>2</sup> + 8<sup>2</sup> &minus; 2&middot;4&middot;8&middot;cos120&deg; = 16 + 64 + 32 = 112. So mAB = &radic;112 = 4&radic;7 cm. Area = &frac12;&middot;4&middot;8&middot;sin120&deg; = 16&middot;(&radic;3/2) = 8&radic;3 cm<sup>2</sup>.', 249),
    bq(U, EX1, 'EX15.1', '2', 'Find the length of AC in &Delta;ABC when mBC = 6 cm, mAB = 4&radic;2 cm and m&ang;ABC = 135&deg;. If possible find the area of &Delta;ABC.',
       'mAC = &radic;116 cm, Area = 12 cm<sup>2</sup>.',
       'The side opposite &ang;B is AC. By the law of cosines, AC<sup>2</sup> = AB<sup>2</sup> + BC<sup>2</sup> &minus; 2&middot;AB&middot;BC&middot;cos B = (4&radic;2)<sup>2</sup> + 6<sup>2</sup> &minus; 2&middot;4&radic;2&middot;6&middot;cos135&deg; = 32 + 36 &minus; 48&radic;2&middot;(&minus;&radic;2/2) = 68 + 48 = 116. So mAC = &radic;116 cm. Area = &frac12;&middot;AB&middot;BC&middot;sin B = &frac12;&middot;4&radic;2&middot;6&middot;sin135&deg; = 12&radic;2&middot;(&radic;2/2) = 12 cm<sup>2</sup>.', 249),
    bq(U, EX1, 'EX15.1', '3', 'Find the length of AC in &Delta;ABC when mBC = 6&radic;2 cm, mAB = 8 cm and m&ang;ABC = 135&deg;. If possible find the area of &Delta;ABC.',
       'mAC = &radic;232 cm, Area = 24 cm<sup>2</sup>.',
       'The side opposite &ang;B is AC. By the law of cosines, AC<sup>2</sup> = AB<sup>2</sup> + BC<sup>2</sup> &minus; 2&middot;AB&middot;BC&middot;cos B = 8<sup>2</sup> + (6&radic;2)<sup>2</sup> &minus; 2&middot;8&middot;6&radic;2&middot;cos135&deg; = 64 + 72 &minus; 96&radic;2&middot;(&minus;&radic;2/2) = 136 + 96 = 232. So mAC = &radic;232 cm. Area = &frac12;&middot;AB&middot;BC&middot;sin B = &frac12;&middot;8&middot;6&radic;2&middot;sin135&deg; = 24&radic;2&middot;(&radic;2/2) = 24 cm<sup>2</sup>.', 249),
]

# ============================================================== Exercise 15.2 (pdf 252)
ITEMS += [
    bq(U, EX2, 'EX15.2', '1', 'In &Delta;ABC, m&ang;A = 30&deg;, prove that (mBC)<sup>2</sup> = (mAC)<sup>2</sup> + (mAB)<sup>2</sup> &minus; &radic;3(mAB)(mAC).',
       '(mBC)<sup>2</sup> = (mAC)<sup>2</sup> + (mAB)<sup>2</sup> &minus; &radic;3(mAB)(mAC).',
       'Proof: &ang;A is acute, so by Theorem 15.1.2, BC<sup>2</sup> = AC<sup>2</sup> + AB<sup>2</sup> &minus; 2(AB)(projection of AC on AB). The projection of AC on AB is AD = AC&middot;cos A = AC&middot;cos30&deg; = AC&middot;(&radic;3/2). Hence BC<sup>2</sup> = AC<sup>2</sup> + AB<sup>2</sup> &minus; 2(AB)(AC)(&radic;3/2) = AC<sup>2</sup> + AB<sup>2</sup> &minus; &radic;3(AB)(AC). Q.E.D.', 252),
    bq(U, EX2, 'EX15.2', '2', 'In &Delta;ABC, calculate mBC when mAB = 6 cm, mAC = 5 cm and m&ang;A = 60&deg;.',
       'mBC = &radic;31 cm &asymp; 5.57 cm.',
       'By the law of cosines, BC<sup>2</sup> = AB<sup>2</sup> + AC<sup>2</sup> &minus; 2&middot;AB&middot;AC&middot;cos A = 6<sup>2</sup> + 5<sup>2</sup> &minus; 2&middot;6&middot;5&middot;cos60&deg; = 36 + 25 &minus; 60&middot;(&frac12;) = 61 &minus; 30 = 31. Hence mBC = &radic;31 cm &asymp; 5.57 cm.', 252),
    bq(U, EX2, 'EX15.2', '3', 'Whether the triangle with sides 3 cm, 4 cm and 5 cm is acute, obtuse or right-angled?',
       'It is a right-angled triangle.',
       'Check the largest side: 5<sup>2</sup> = 25 and 3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = 25. Since the square of the largest side equals the sum of the squares of the other two, the triangle is right-angled (converse of Pythagoras theorem).', 252),
    bq(U, EX2, 'EX15.2', '4', 'Find the length of the median of side BC of &Delta;ABC where mAB = 4 cm, mAC = 3 cm and mBC = 6 cm.',
       'Median of BC = &radic;(7/2) cm (&asymp; 1.87 cm).',
       'Let AD be the median to BC, so D is the midpoint of BC and mBD = mCD = 3 cm. By Apollonius\' theorem, AB<sup>2</sup> + AC<sup>2</sup> = 2(BD)<sup>2</sup> + 2(AD)<sup>2</sup>. So 4<sup>2</sup> + 3<sup>2</sup> = 2(3)<sup>2</sup> + 2(AD)<sup>2</sup>, i.e. 16 + 9 = 18 + 2(AD)<sup>2</sup>, giving 2(AD)<sup>2</sup> = 7 and AD = &radic;(7/2) = &radic;14/2 cm &asymp; 1.87 cm.', 252),
]

# ============================================================== Review Exercise 15 (pdf 252)
ITEMS += [
    bq(U, RE15, 'RE15', '1(i)', 'Fill in the blank: In a right-angled &Delta;ABC, (mAB)<sup>2</sup> + ________ = (mAC)<sup>2</sup>.',
       '(mBC)<sup>2</sup>', 'In a right-angled triangle the square on the hypotenuse equals the sum of the squares on the other two sides. Here AC is the hypotenuse, so (mAB)<sup>2</sup> + (mBC)<sup>2</sup> = (mAC)<sup>2</sup>; the blank is (mBC)<sup>2</sup>.', 252),
    bq(U, RE15, 'RE15', '1(ii)', 'Fill in the blank: In &Delta;ABC, two sides are equal to 4 cm; it is called ________ triangle.',
       'an isosceles', 'A triangle with two equal sides is called an isosceles triangle.', 252),
    bq(U, RE15, 'RE15', '1(iii)', 'Fill in the blank: In &Delta;ABC with m&ang;B = 90&deg;, then (mAB)<sup>2</sup> + (mBC)<sup>2</sup> = ________.',
       '(mAC)<sup>2</sup>', 'With the right angle at B, AC is the hypotenuse, so by Pythagoras\' theorem (mAB)<sup>2</sup> + (mBC)<sup>2</sup> = (mAC)<sup>2</sup>.', 252),
    bq(U, RE15, 'RE15', '1(iv)', 'Fill in the blank: 8 cm, 15 cm and 17 cm are the sides of a ________.',
       'right-angled triangle', 'Check the largest side: 17<sup>2</sup> = 289 and 8<sup>2</sup> + 15<sup>2</sup> = 64 + 225 = 289. Since the square of the largest side equals the sum of the squares of the other two, the triangle is right-angled.', 252),
    bq(U, RE15, 'RE15', '2', 'In &Delta;ABC, mAC = 3 cm, mBC = 6 cm and m&ang;C = 120&deg;. Compute mAB.',
       'mAB = 3&radic;7 cm &asymp; 7.94 cm.',
       'The obtuse angle is at C. By the law of cosines, AB<sup>2</sup> = AC<sup>2</sup> + BC<sup>2</sup> &minus; 2&middot;AC&middot;BC&middot;cos C = 3<sup>2</sup> + 6<sup>2</sup> &minus; 2&middot;3&middot;6&middot;cos120&deg; = 9 + 36 + 18 = 63. Hence mAB = &radic;63 = 3&radic;7 cm &asymp; 7.94 cm.', 252),
]
