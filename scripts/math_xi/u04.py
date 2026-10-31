"""Unit 4 - Sequences and Series (book pp. 124-161, PDF pp. 128-165)."""
from .common import bq, mcq

U = 4
EX1 = 'Exercise 4.1'
EX2 = 'Exercise 4.2'
EX3 = 'Exercise 4.3'
EX4 = 'Exercise 4.4'
EX5 = 'Exercise 4.5'
EX6 = 'Exercise 4.6'
EX7 = 'Exercise 4.7'
EX8 = 'Exercise 4.8'
EX9 = 'Exercise 4.9'
REV = 'Review Exercise 4'

ITEMS = []

# ============================================================== Exercise 4.1 (pdf 132-133)
ITEMS += [
    bq(U, EX1, 'EX4.1', '1(i)', 'Find the nth term (rule of formation) of the sequence: 2, 4, 6, ...',
       'a<sub>n</sub> = 2n',
       'The terms are 2(1), 2(2), 2(3), ... — an A.P. with first term a = 2 and common difference d = 2. '
       'Hence a<sub>n</sub> = a + (n − 1)d = 2 + (n − 1)2 = 2n.', 132),
    bq(U, EX1, 'EX4.1', '1(ii)', 'Find the nth term (rule of formation) of the sequence: 1², 2², 3², ...',
       'a<sub>n</sub> = n²',
       'Each term is the square of its position: 1², 2², 3². Hence the nth term is a<sub>n</sub> = n².', 132),
    bq(U, EX1, 'EX4.1', '1(iii)', 'Find the nth term (rule of formation) of the sequence: 3, 9, 27, ...',
       'a<sub>n</sub> = 3<sup>n</sup>',
       'The terms are 3¹, 3², 3³ — a G.P. with a = 3 and r = 3. Hence a<sub>n</sub> = ar<sup>n−1</sup> = 3·3<sup>n−1</sup> = 3<sup>n</sup>.', 132),
    bq(U, EX1, 'EX4.1', '1(iv)', 'Find the nth term (rule of formation) of the sequence: 1/2, 2/3, 3/4, 4/5, ...',
       'a<sub>n</sub> = n/(n + 1)',
       'The numerator of each term equals its position n and the denominator is one more than the numerator: '
       '1/2, 2/3, 3/4, 4/5, ... Hence a<sub>n</sub> = n/(n + 1).', 132),
    bq(U, EX1, 'EX4.1', '1(v)', 'Find the nth term (rule of formation) of the sequence: 1, −1/3, 1/9, −1/27, ...',
       'a<sub>n</sub> = (−1/3)<sup>n−1</sup> = (−1)<sup>n−1</sup>/3<sup>n−1</sup>',
       'Each term is obtained by multiplying the previous term by r = −1/3, so it is a G.P. with a = 1, r = −1/3. '
       'Hence a<sub>n</sub> = ar<sup>n−1</sup> = (−1/3)<sup>n−1</sup>, which is the same as (−1)<sup>n−1</sup>/3<sup>n−1</sup>.', 132),
    bq(U, EX1, 'EX4.1', '1(vi)', 'Find the nth term (rule of formation) of the sequence: 1, 8, 27, 64, ...',
       'a<sub>n</sub> = n³',
       'The terms are 1³, 2³, 3³, 4³, i.e. the cubes of the natural numbers, so a<sub>n</sub> = n³.', 132),

    bq(U, EX1, 'EX4.1', '2(i)', 'Find the first five terms of the sequence with general term a<sub>n</sub> = (2n/3)(n + 1).',
       '4/3, 4, 8, 40/3, 20',
       'Put n = 1, 2, 3, 4, 5: a<sub>1</sub> = (2/3)(2) = 4/3; a<sub>2</sub> = (4/3)(3) = 4; a<sub>3</sub> = (6/3)(4) = 8; '
       'a<sub>4</sub> = (8/3)(5) = 40/3; a<sub>5</sub> = (10/3)(6) = 20.', 132),
    bq(U, EX1, 'EX4.1', '2(ii)', 'Find the first five terms of the sequence with general term a<sub>n</sub> = (−1)<sup>n+1</sup> · 3<sup>n−1</sup>.',
       '1, −3, 9, −27, 81',
       'a<sub>1</sub> = (−1)²·3⁰ = 1; a<sub>2</sub> = (−1)³·3¹ = −3; a<sub>3</sub> = (−1)⁴·3² = 9; a<sub>4</sub> = (−1)⁵·3³ = −27; '
       'a<sub>5</sub> = (−1)⁶·3⁴ = 81. This is a G.P. with a = 1, r = −3.', 132),
    bq(U, EX1, 'EX4.1', '2(iii)', 'Find the first five terms of the sequence with general term a<sub>n</sub> = (1/4)n²(n + 1)².',
       '1, 9, 36, 100, 225',
       'a<sub>1</sub> = (1/4)(1)(4) = 1; a<sub>2</sub> = (1/4)(4)(9) = 9; a<sub>3</sub> = (1/4)(9)(16) = 36; '
       'a<sub>4</sub> = (1/4)(16)(25) = 100; a<sub>5</sub> = (1/4)(25)(36) = 225.', 132),
    bq(U, EX1, 'EX4.1', '2(iv)', 'Find the first five terms of the sequence with general term a<sub>n</sub> = n/(3n + 1).',
       '1/4, 2/7, 3/10, 4/13, 5/16',
       'a<sub>1</sub> = 1/4; a<sub>2</sub> = 2/7; a<sub>3</sub> = 3/10; a<sub>4</sub> = 4/13; a<sub>5</sub> = 5/16.', 132),
    bq(U, EX1, 'EX4.1', '2(v)', 'Find the first five terms of the sequence with general term a<sub>n</sub> = (1/6)n(n + 1)(n + 2).',
       '1, 4, 10, 20, 35',
       'a<sub>1</sub> = (1/6)(1)(2)(3) = 1; a<sub>2</sub> = (1/6)(2)(3)(4) = 4; a<sub>3</sub> = (1/6)(3)(4)(5) = 10; '
       'a<sub>4</sub> = (1/6)(4)(5)(6) = 20; a<sub>5</sub> = (1/6)(5)(6)(7) = 35.', 132),
    bq(U, EX1, 'EX4.1', '2(vi)', 'Find the first five terms of the sequence with general term a<sub>n</sub> = (1/6)n(n + 1)(2n + 7).',
       '3, 11, 26, 50, 85',
       'a<sub>1</sub> = (1/6)(1)(2)(9) = 3; a<sub>2</sub> = (1/6)(2)(3)(11) = 11; a<sub>3</sub> = (1/6)(3)(4)(13) = 26; '
       'a<sub>4</sub> = (1/6)(4)(5)(15) = 50; a<sub>5</sub> = (1/6)(5)(6)(17) = 85.', 132),
    bq(U, EX1, 'EX4.1', '2(vii)', 'Find the first five terms of the sequence defined by a<sub>n+1</sub> = 6 + a<sub>n</sub>, where a<sub>1</sub> = 2.',
       '2, 8, 14, 20, 26',
       'The rule adds 6 each time. a<sub>1</sub> = 2; a<sub>2</sub> = 6 + 2 = 8; a<sub>3</sub> = 6 + 8 = 14; a<sub>4</sub> = 6 + 14 = 20; '
       'a<sub>5</sub> = 6 + 20 = 26. It is an A.P. with a = 2, d = 6.', 132),
    bq(U, EX1, 'EX4.1', '2(viii)', 'Find the first five terms of the sequence defined by a<sub>n</sub> = (n/2)a<sub>n+1</sub>, where a<sub>1</sub> = 1.',
       '1, 2, 2, 4/3, 2/3',
       'Rewrite the rule as a<sub>n+1</sub> = (2/n)a<sub>n</sub>. Then a<sub>2</sub> = (2/1)(1) = 2; a<sub>3</sub> = (2/2)(2) = 2; '
       'a<sub>4</sub> = (2/3)(2) = 4/3; a<sub>5</sub> = (2/4)(4/3) = 2/3.', 132),

    bq(U, EX1, 'EX4.1', '3', 'Find the sequence by using T<sub>n+1</sub> = (n + 1)T<sub>n</sub>, where T<sub>1</sub> = 2.',
       '2, 4, 12, 48, 240, ... (T<sub>n</sub> = 2·n!)',
       'T<sub>2</sub> = (2)T<sub>1</sub> = 2·2 = 4; T<sub>3</sub> = (3)T<sub>2</sub> = 3·4 = 12; T<sub>4</sub> = (4)T<sub>3</sub> = 4·12 = 48; '
       'T<sub>5</sub> = (5)T<sub>4</sub> = 5·48 = 240. In general T<sub>n</sub> = n!·T<sub>1</sub> = 2·n!, so the sequence is 2, 4, 12, 48, 240, ...', 133),
    bq(U, EX1, 'EX4.1', '4', 'Find the values of the nth term of the triangular sequence when n = 7, 9, 12 and 16.',
       'T<sub>7</sub> = 28, T<sub>9</sub> = 45, T<sub>12</sub> = 78, T<sub>16</sub> = 136',
       'The nth triangular number is T<sub>n</sub> = n(n + 1)/2. Hence T<sub>7</sub> = 7·8/2 = 28; T<sub>9</sub> = 9·10/2 = 45; '
       'T<sub>12</sub> = 12·13/2 = 78; T<sub>16</sub> = 16·17/2 = 136.', 133),
    bq(U, EX1, 'EX4.1', '5', 'Find the first five terms of the sequence with general term a<sub>n</sub> = (n + 1)!/2!.',
       '1, 3, 12, 60, 360',
       'Since 2! = 2: a<sub>1</sub> = 2!/2 = 1; a<sub>2</sub> = 3!/2 = 3; a<sub>3</sub> = 4!/2 = 12; a<sub>4</sub> = 5!/2 = 60; a<sub>5</sub> = 6!/2 = 360.', 133),
    bq(U, EX1, 'EX4.1', '6', 'Find the Pascal sequence when n = 5, 6, 7 and 8 (using the formula n!/(r!(n − r)!) for r = 0, 1, ..., n).',
       'n = 5: 1, 5, 10, 10, 5, 1;  n = 6: 1, 6, 15, 20, 15, 6, 1;  n = 7: 1, 7, 21, 35, 35, 21, 7, 1;  '
       'n = 8: 1, 8, 28, 56, 70, 56, 28, 8, 1',
       'Each entry of row n is <sup>n</sup>C<sub>r</sub> = n!/(r!(n − r)!). For n = 5 these are 1, 5, 10, 10, 5, 1; for n = 6 they are '
       '1, 6, 15, 20, 15, 6, 1 (each inner entry is the sum of the two above it); for n = 7, 1, 7, 21, 35, 35, 21, 7, 1; and for n = 8, '
       '1, 8, 28, 56, 70, 56, 28, 8, 1.', 133),
]

# ============================================================== Exercise 4.2 (pdf 135-136)
ITEMS += [
    bq(U, EX2, 'EX4.2', '1(i)', 'Find the indicated term of the A.P. 1, 5, 9, ... ; find a<sub>12</sub>.',
       'a<sub>12</sub> = 45',
       'Here a = 1 and d = 5 − 1 = 4. Using a<sub>n</sub> = a + (n − 1)d: a<sub>12</sub> = 1 + (12 − 1)4 = 1 + 44 = 45.', 135),
    bq(U, EX2, 'EX4.2', '1(ii)', 'Find the indicated term of the A.P. −15, −9, −3, ... ; find a<sub>10</sub>.',
       'a<sub>10</sub> = 39',
       'Here a = −15 and d = −9 − (−15) = 6. a<sub>10</sub> = −15 + (10 − 1)6 = −15 + 54 = 39.', 135),
    bq(U, EX2, 'EX4.2', '1(iii)', 'Find the indicated term of the A.P. 2, 6, 10, 14, ... ; find a<sub>7</sub>.',
       'a<sub>7</sub> = 26',
       'Here a = 2 and d = 4. a<sub>7</sub> = 2 + (7 − 1)4 = 2 + 24 = 26.', 135),
    bq(U, EX2, 'EX4.2', '1(iv)', 'Find the indicated term of the A.P. −5, 4, 13, ... ; find a<sub>30</sub>.',
       'a<sub>30</sub> = 256',
       'Here a = −5 and d = 4 − (−5) = 9. a<sub>30</sub> = −5 + (30 − 1)9 = −5 + 261 = 256.', 135),
    bq(U, EX2, 'EX4.2', '1(v)', 'Find the indicated term of the A.P. 23, 26, 29, ... ; find a<sub>14</sub>.',
       'a<sub>14</sub> = 62',
       'Here a = 23 and d = 3. a<sub>14</sub> = 23 + (14 − 1)3 = 23 + 39 = 62.', 135),
    bq(U, EX2, 'EX4.2', '1(vi)', 'Find the indicated term of the A.P. 1/3, 1/2, 2/3, ... ; find a<sub>6</sub>.',
       'a<sub>6</sub> = 7/6',
       'Here a = 1/3 and d = 1/2 − 1/3 = 1/6. a<sub>6</sub> = 1/3 + (6 − 1)(1/6) = 2/6 + 5/6 = 7/6.', 135),

    bq(U, EX2, 'EX4.2', '2(i)', 'Find the first five terms of the arithmetic sequence for which a<sub>n</sub> = 2n − 3.',
       '−1, 1, 3, 5, 7',
       'a<sub>1</sub> = 2(1) − 3 = −1; a<sub>2</sub> = 1; a<sub>3</sub> = 3; a<sub>4</sub> = 5; a<sub>5</sub> = 7 (an A.P. with d = 2).', 135),
    bq(U, EX2, 'EX4.2', '2(ii)', 'Find the first five terms of the arithmetic sequence for which a<sub>n−2</sub> = 3n − 5.',
       '4, 7, 10, 13, 16',
       'Take n = 3, 4, 5, 6, 7 to obtain a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>5</sub>: a<sub>1</sub> = 3(3) − 5 = 4; a<sub>2</sub> = 3(4) − 5 = 7; '
       'a<sub>3</sub> = 10; a<sub>4</sub> = 13; a<sub>5</sub> = 16. The common difference is 3.', 135),
    bq(U, EX2, 'EX4.2', '2(iii)', 'Find the first five terms of the sequence for which a<sub>n</sub> = n/(2n + 1).',
       '1/3, 2/5, 3/7, 4/9, 5/11',
       'a<sub>1</sub> = 1/3; a<sub>2</sub> = 2/5; a<sub>3</sub> = 3/7; a<sub>4</sub> = 4/9; a<sub>5</sub> = 5/11.', 135),
    bq(U, EX2, 'EX4.2', '2(iv)', 'Find the first five terms of the sequence for which a<sub>n</sub> = (n + 1)a<sub>n−1</sub> and a<sub>1</sub> = 1.',
       '1, 3, 12, 60, 360',
       'a<sub>1</sub> = 1; a<sub>2</sub> = (2 + 1)a<sub>1</sub> = 3; a<sub>3</sub> = (3 + 1)a<sub>2</sub> = 4(3) = 12; a<sub>4</sub> = 5(12) = 60; '
       'a<sub>5</sub> = 6(60) = 360.', 135),
    bq(U, EX2, 'EX4.2', '2(v)', 'Find the first five terms of the sequence for which a<sub>n</sub> − a<sub>n−1</sub> = n + 2 and a<sub>1</sub> = 2.',
       '2, 6, 11, 17, 24',
       'a<sub>n</sub> = a<sub>n−1</sub> + n + 2. So a<sub>2</sub> = 2 + 2 + 2 = 6; a<sub>3</sub> = 6 + 3 + 2 = 11; a<sub>4</sub> = 11 + 4 + 2 = 17; '
       'a<sub>5</sub> = 17 + 5 + 2 = 24.', 135),
    bq(U, EX2, 'EX4.2', '2(vi)', 'Find the first five terms of the arithmetic sequence whose first term is a = 5 and which contains the three consecutive terms 23, 26, 29.',
       '5, 8, 11, 14, 17',
       'The consecutive terms 23, 26, 29 show that d = 26 − 23 = 3. With a = 5 the first five terms are 5, 8, 11, 14, 17 '
       '(indeed 23 is the 7th, 26 the 8th and 29 the 9th term).', 135),

    bq(U, EX2, 'EX4.2', '3', 'If a<sub>n−3</sub> = 2n − 5, find the nth term of the sequence.',
       'a<sub>n</sub> = 2n + 1',
       'Replace n by n + 3 in the given relation: a<sub>(n+3)−3</sub> = 2(n + 3) − 5, i.e. a<sub>n</sub> = 2n + 6 − 5 = 2n + 1. '
       '(Check: n = 4 gives a<sub>1</sub> = 3 = 2(4) − 5.)', 136),
    bq(U, EX2, 'EX4.2', '4', 'Find the 20th term of the sequence 1, 2 − x, 3 − 2x, ...',
       'a<sub>20</sub> = 20 − 19x',
       'a = 1 and d = (2 − x) − 1 = 1 − x. Hence a<sub>20</sub> = 1 + (20 − 1)(1 − x) = 1 + 19 − 19x = 20 − 19x.', 136),
    bq(U, EX2, 'EX4.2', '5', 'Find the 21st term of the A.P. whose 6th term is 11 and whose 15th term is 47.',
       'a<sub>21</sub> = 71',
       'a<sub>6</sub> = a + 5d = 11 and a<sub>15</sub> = a + 14d = 47. Subtracting gives 9d = 36, so d = 4 and a = 11 − 5(4) = −9. '
       'Then a<sub>21</sub> = −9 + 20(4) = 71.', 136),
    bq(U, EX2, 'EX4.2', '6(a)', 'Which term of the sequence −15, −9, −3, ... is 75?',
       'The 16th term',
       'a = −15, d = 6. Put a<sub>n</sub> = 75: −15 + (n − 1)6 = 75, so (n − 1)6 = 90, n − 1 = 15 and n = 16.', 136),
    bq(U, EX2, 'EX4.2', '6(b)', 'Which term of the sequence 5, 2, −1, ... is −85?',
       'The 31st term',
       'a = 5, d = −3. Put 5 + (n − 1)(−3) = −85, so (n − 1)(−3) = −90, n − 1 = 30 and n = 31.', 136),
    bq(U, EX2, 'EX4.2', '6(c)', 'Which term of the sequence −2, 4, 10, ... is 148?',
       'The 26th term',
       'a = −2, d = 6. Put −2 + (n − 1)6 = 148, so (n − 1)6 = 150, n − 1 = 25 and n = 26.', 136),
    bq(U, EX2, 'EX4.2', '7', 'Find the nth term of the sequence (6/7)², (11/7)², (16/7)², ...',
       'a<sub>n</sub> = ((5n + 1)/7)²',
       'The bases 6/7, 11/7, 16/7 form an A.P. with a = 6/7 and d = 5/7. Their nth term is 6/7 + (n − 1)(5/7) = (5n + 1)/7. '
       'Squaring gives a<sub>n</sub> = ((5n + 1)/7)².', 136),
    bq(U, EX2, 'EX4.2', '8(i)', 'If a, b, c are the lth, mth and nth terms of an A.P., show that a(m − n) + b(n − l) + c(l − m) = 0.',
       'a(m − n) + b(n − l) + c(l − m) = 0',
       'Let A be the first term and d the common difference of the A.P. Then a = A + (l − 1)d, b = A + (m − 1)d, c = A + (n − 1)d. '
       'Hence a(m − n) + b(n − l) + c(l − m) = A[(m − n) + (n − l) + (l − m)] + d[(l − 1)(m − n) + (m − 1)(n − l) + (n − 1)(l − m)]. '
       'The first bracket is 0. Expanding the second: (lm − ln − m + n) + (mn − ml − n + l) + (nl − nm − l + m) = 0, since every term cancels. '
       'Thus the whole expression equals 0.', 136),
    bq(U, EX2, 'EX4.2', '8(ii)', 'If a, b, c are the lth, mth and nth terms of an A.P., show that l(b − c) + m(c − a) + n(a − b) = 0.',
       'l(b − c) + m(c − a) + n(a − b) = 0',
       'With a = A + (l − 1)d, b = A + (m − 1)d, c = A + (n − 1)d we get b − c = (m − n)d, c − a = (n − l)d and a − b = (l − m)d. Hence '
       'l(b − c) + m(c − a) + n(a − b) = d[l(m − n) + m(n − l) + n(l − m)] = d[lm − ln + mn − ml + nl − nm] = 0.', 136),
    bq(U, EX2, 'EX4.2', '9', 'If 1/a, 1/b, 1/c are in A.P., show that b = 2ac/(a + c).',
       'b = 2ac/(a + c)',
       'Since 1/a, 1/b, 1/c are in A.P., the middle term is the average of the other two: 2/b = 1/a + 1/c = (a + c)/(ac). '
       'Taking reciprocals, b = 2ac/(a + c).', 136),
    bq(U, EX2, 'EX4.2', '10', 'If 1/(a − b), 1/(b − c), 1/(c − a) are in A.P., then show that (a + c)/(a − b) = (a + b)/(c − a).',
       'The hypothesis is equivalent to (a − b)² + (c − a)² = 2(b − c)²; the printed identity does not follow in general '
       '(it is equivalent to b² + c² = 2a², an extra condition).',
       'Put x = a − b, y = b − c, z = c − a, so that x + y + z = 0. The A.P. condition 2/(b − c) = 1/(a − b) + 1/(c − a) gives '
       '2/y = (x + z)/(xz) = −y/(xz), i.e. 2xz = −y². Then x² + 2xz + z² = x² + z² − y², so (x + z)² = x² + z² − y²; but x + z = −y, '
       'hence y² = x² + z² − y², that is x² + z² = 2y², i.e. (a − b)² + (c − a)² = 2(b − c)² — the squares of the three differences are in A.P. '
       'On the other hand (a + c)/(a − b) = (a + b)/(c − a) is equivalent to (a + c)(c − a) = (a + b)(a − b), i.e. to b² + c² = 2a². '
       'This is an additional condition, not a consequence of the hypothesis: for a = 3, b = 4 − √3, c = 2 − √3 the reciprocals '
       '(√3 + 1)/2, 1/2, −(√3 − 1)/2 do form an A.P. (common difference −√3/2), yet (a + c)/(a − b) ≈ 4.46 while (a + b)/(c − a) ≈ −1.93. '
       'So the identity as printed is not valid in general.', 136),
    bq(U, EX2, 'EX4.2', '11', 'An object falling from rest falls 12 metres during the first second, 24 metres during the next second, 36 metres during the third second and so on. How much will it fall during the 8th second?',
       '96 metres',
       'The distances 12, 24, 36, ... form an A.P. with a = 12 and d = 12. For the 8th second, n = 8: '
       'a<sub>8</sub> = 12 + (8 − 1)12 = 12 + 84 = 96 metres.', 136),
    bq(U, EX2, 'EX4.2', '12', 'A man deposits Rs. 13,000 in a bank in the first month, Rs. 14,500 in the second month, Rs. 16,000 in the third month and so on. Find how much he has to deposit in the bank at the end of a year (i.e. in the 12th month).',
       'Rs. 29,500',
       'The deposits 13000, 14500, 16000, ... form an A.P. with a = 13000 and d = 1500. At the end of a year, n = 12: '
       'a<sub>12</sub> = 13000 + (12 − 1)1500 = 13000 + 16500 = Rs. 29,500.', 136),
    bq(U, EX2, 'EX4.2', '13', 'A boy saves Rs. 200 at the end of the first week and goes on increasing his saving by Rs. 25 weekly. After how many weeks will his weekly saving be Rs. 2000?',
       '73 weeks',
       'The weekly savings 200, 225, 250, ... form an A.P. with a = 200 and d = 25. Put a<sub>n</sub> = 2000: '
       '200 + (n − 1)25 = 2000, so (n − 1)25 = 1800, n − 1 = 72 and n = 73.', 136),
]

# ============================================================== Exercise 4.3 (pdf 138)
ITEMS += [
    bq(U, EX3, 'EX4.3', '1(i)', 'Find the arithmetic mean between 18 and 26.',
       'A.M. = 22',
       'A.M. = (a + b)/2 = (18 + 26)/2 = 44/2 = 22.', 138),
    bq(U, EX3, 'EX4.3', '1(ii)', 'Find the arithmetic mean between 10 + 5√3 and 4 − 5√3.',
       'A.M. = 7',
       'A.M. = [(10 + 5√3) + (4 − 5√3)]/2 = 14/2 = 7. The irrational parts cancel.', 138),
    bq(U, EX3, 'EX4.3', '1(iii)', 'Find the arithmetic mean between 3a + 2b and 5a − 6b.',
       'A.M. = 4a − 2b',
       'A.M. = [(3a + 2b) + (5a − 6b)]/2 = (8a − 4b)/2 = 4a − 2b.', 138),
    bq(U, EX3, 'EX4.3', '1(iv)', 'Find the arithmetic mean between 5 + 7√5 i and 8 − 7√5 i.',
       'A.M. = 13/2',
       'A.M. = [(5 + 7√5 i) + (8 − 7√5 i)]/2 = 13/2. The imaginary parts cancel.', 138),
    bq(U, EX3, 'EX4.3', '1(v)', 'Find the arithmetic mean between 3a² − 5a + 6 and −a² + 7a − 4.',
       'A.M. = a² + a + 1',
       'A.M. = [(3a² − 5a + 6) + (−a² + 7a − 4)]/2 = (2a² + 2a + 2)/2 = a² + a + 1.', 138),
    bq(U, EX3, 'EX4.3', '1(vi)', 'Find the arithmetic mean between 3a − 5 and 5a + 3.',
       'A.M. = 4a − 1',
       'A.M. = [(3a − 5) + (5a + 3)]/2 = (8a − 2)/2 = 4a − 1.', 138),
    bq(U, EX3, 'EX4.3', '2', 'Insert three arithmetic means between 3 and 11.',
       '5, 7, 9',
       'Let the means be A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub>. Then 3, A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub>, 11 are 5 terms of an A.P., so '
       'd = (11 − 3)/(5 − 1) = 8/4 = 2. Hence the means are 3 + 2 = 5, 7 and 9.', 138),
    bq(U, EX3, 'EX4.3', '3', 'Insert four arithmetic means between √2 and 12/√2.',
       '2√2, 3√2, 4√2, 5√2',
       'Here b = 12/√2 = 6√2. The six terms √2, A<sub>1</sub>, ..., A<sub>4</sub>, 6√2 form an A.P., so d = (6√2 − √2)/(6 − 1) = 5√2/5 = √2. '
       'The means are √2 + √2 = 2√2, 3√2, 4√2 and 5√2.', 138),
    bq(U, EX3, 'EX4.3', '4', 'Insert five arithmetic means between √5/2 and 4√5.',
       '13√5/12, 5√5/3, 9√5/4, 17√5/6, 41√5/12',
       'There are 7 terms in all, so d = (4√5 − √5/2)/(7 − 1) = (7√5/2)/6 = 7√5/12. Adding repeatedly: '
       '√5/2 + 7√5/12 = 13√5/12, then 20√5/12 = 5√5/3, 27√5/12 = 9√5/4, 34√5/12 = 17√5/6 and 41√5/12 '
       '(and 41√5/12 + 7√5/12 = 4√5, as required).', 138),
    bq(U, EX3, 'EX4.3', '5', 'Insert six arithmetic means between −30 and 30.',
       '−150/7, −90/7, −30/7, 30/7, 90/7, 150/7',
       'There are 8 terms, so d = (30 − (−30))/(8 − 1) = 60/7. The means are −30 + 60/7 = −150/7, then −90/7, −30/7, 30/7, 90/7 and 150/7.', 138),
    bq(U, EX3, 'EX4.3', '6', 'If 5 and 8 are two arithmetic means between c and d, find c and d.',
       'c = 2 and d = 11',
       'Since c, 5, 8, d are in A.P. the common difference is 8 − 5 = 3. Hence d = 8 + 3 = 11 and c = 5 − 3 = 2.', 138),
    bq(U, EX3, 'EX4.3', '7', 'Find n so that (a<sup>n+5</sup> + b<sup>n+5</sup>)/(a<sup>n+4</sup> + b<sup>n+4</sup>) may be the arithmetic mean between a and b.',
       'n = −4',
       'We need (a<sup>n+5</sup> + b<sup>n+5</sup>)/(a<sup>n+4</sup> + b<sup>n+4</sup>) = (a + b)/2. Cross-multiplying: '
       '2a<sup>n+5</sup> + 2b<sup>n+5</sup> = a<sup>n+5</sup> + ab<sup>n+4</sup> + ba<sup>n+4</sup> + b<sup>n+5</sup>, i.e. '
       'a<sup>n+5</sup> + b<sup>n+5</sup> = ab<sup>n+4</sup> + ba<sup>n+4</sup>. Rearranging, a<sup>n+4</sup>(a − b) = b<sup>n+4</sup>(a − b), '
       'so for a ≠ b we need a<sup>n+4</sup> = b<sup>n+4</sup>, i.e. n + 4 = 0 and n = −4. '
       '(Check: n = −4 gives (a + b)/(1 + 1) = (a + b)/2.)', 138),
]

# ============================================================== Exercise 4.4 (pdf 143-144)
ITEMS += [
    bq(U, EX4, 'EX4.4', '1(i)', 'Sum the series 3 + 8 + 13 + ... to 16 terms.',
       'S<sub>16</sub> = 648',
       'a = 3, d = 5, n = 16. S<sub>n</sub> = (n/2)[2a + (n − 1)d] = (16/2)[6 + 15(5)] = 8(6 + 75) = 8(81) = 648.', 143),
    bq(U, EX4, 'EX4.4', '1(ii)', 'Sum the series (−3) + (−1) + 1 + 3 + 5 + ... to 18 terms.',
       'S<sub>18</sub> = 252',
       'a = −3, d = 2, n = 18. S<sub>18</sub> = (18/2)[2(−3) + 17(2)] = 9(−6 + 34) = 9(28) = 252.', 143),
    bq(U, EX4, 'EX4.4', '1(iii)', 'Sum the series 4.57 + 4.87 + 5.17 + ... to 22 terms.',
       'S<sub>22</sub> = 169.84',
       'a = 4.57, d = 0.30, n = 22. S<sub>22</sub> = (22/2)[2(4.57) + 21(0.30)] = 11(9.14 + 6.30) = 11(15.44) = 169.84.', 143),
    bq(U, EX4, 'EX4.4', '1(iv)', 'Sum the series 3/√2 + 2√2 + 5/√2 + ... to n terms.',
       'S<sub>n</sub> = n(n + 5)/(2√2)',
       'a = 3/√2 and d = 2√2 − 3/√2 = 4/√2 − 3/√2 = 1/√2. Hence S<sub>n</sub> = (n/2)[2(3/√2) + (n − 1)(1/√2)] = (n/2)[(6 + n − 1)/√2] '
       '= n(n + 5)/(2√2).', 143),
    bq(U, EX4, 'EX4.4', '1(v)', 'Sum the series 3/√2 + 2√2 + 5/√2 + ... to 15 terms.',
       'S<sub>15</sub> = 75√2',
       'From part (iv), S<sub>n</sub> = n(n + 5)/(2√2). With n = 15: S<sub>15</sub> = 15(20)/(2√2) = 300/(2√2) = 150/√2 = 75√2.', 143),

    bq(U, EX4, 'EX4.4', '2(i)', 'Find the number of terms of (−7) + (−5) + (−3) + ... if the sum is 65.',
       '13 terms',
       'a = −7, d = 2. (n/2)[2(−7) + (n − 1)2] = 65 gives n(n − 8) = 65, i.e. n² − 8n − 65 = 0, (n − 13)(n + 5) = 0. '
       'As n must be positive, n = 13.', 143),
    bq(U, EX4, 'EX4.4', '2(ii)', 'Find the number of terms of −7 + (−4) + (−1) + ... if the sum is 114.',
       '12 terms',
       'a = −7, d = 3. (n/2)[2(−7) + (n − 1)3] = 114 gives n(3n − 17) = 228, i.e. 3n² − 17n − 228 = 0. '
       'Solving, n = (17 ± √(289 + 2736))/6 = (17 ± 55)/6, so n = 12 (the other root is negative).', 143),
    bq(U, EX4, 'EX4.4', '2(iii)', 'Find the number of terms of −9 + (−6) + (−3) + ... if the sum is 3225.',
       '50 terms',
       'a = −9, d = 3. (n/2)[2(−9) + (n − 1)3] = 3225 gives n(3n − 21) = 6450, i.e. n² − 7n − 2150 = 0. '
       'Solving, n = (7 + √(49 + 8600))/2 = (7 + 93)/2 = 50.', 144),
    bq(U, EX4, 'EX4.4', '2(iv)', 'Find the number of terms of −9 − 6 − 3 + 0 + ... if the sum is 66.',
       '11 terms',
       'a = −9, d = 3. (n/2)[2(−9) + (n − 1)3] = 66 gives n(3n − 21) = 132, i.e. n² − 7n − 44 = 0, (n − 11)(n + 4) = 0. '
       'Hence n = 11.', 144),

    bq(U, EX4, 'EX4.4', '3(i)', 'Sum the series 3 + 5 − 7 + 9 + 11 − 13 + 15 + 17 − 19 + ... to 3n terms.',
       'S<sub>3n</sub> = n(3n − 2)',
       'Group the terms in threes: (3 + 5 − 7) + (9 + 11 − 13) + (15 + 17 − 19) + ... The first terms 3, 9, 15, ... have kth term 6k − 3, '
       'the second terms are 6k − 1 and the third are 6k + 1. The kth group is (6k − 3) + (6k − 1) − (6k + 1) = 6k − 5. '
       'There are n groups, so S<sub>3n</sub> = Σ(6k − 5) = 6·n(n + 1)/2 − 5n = 3n² + 3n − 5n = 3n² − 2n = n(3n − 2).', 144),
    bq(U, EX4, 'EX4.4', '3(ii)', 'Sum the series 1 + 4 − 7 + 10 + 13 − 16 + 19 + 22 − 25 + ... to 3n terms.',
       'S<sub>3n</sub> = (n/2)(9n − 13)',
       'Group in threes: (1 + 4 − 7) + (10 + 13 − 16) + (19 + 22 − 25) + ... In the kth group the terms are 9k − 8, 9k − 5 and 9k − 2, '
       'so the group sum is (9k − 8) + (9k − 5) − (9k − 2) = 9k − 11. Hence S<sub>3n</sub> = 9·n(n + 1)/2 − 11n = (9n² + 9n − 22n)/2 '
       '= (9n² − 13n)/2 = (n/2)(9n − 13).', 144),
    bq(U, EX4, 'EX4.4', '3(iii)', 'Sum the series 9 + 12 − 15 + 18 + 21 − 24 + 27 + 30 − 33 + ... to 3n terms.',
       'S<sub>3n</sub> = 3n(3n + 1)/2',
       'Group in threes: (9 + 12 − 15) + (18 + 21 − 24) + (27 + 30 − 33) + ... In the kth group the terms are 9k, 9k + 3 and 9k + 6, '
       'so the group sum is 9k + 9k + 3 − (9k + 6) = 9k − 3. Hence S<sub>3n</sub> = 9·n(n + 1)/2 − 3n = (9n² + 9n − 6n)/2 '
       '= (9n² + 3n)/2 = 3n(3n + 1)/2.', 144),
    bq(U, EX4, 'EX4.4', '4', 'If S<sub>n</sub> = n(2n − 1), then find the series.',
       '1 + 5 + 9 + 13 + ... up to n terms',
       'The nth term is t<sub>n</sub> = S<sub>n</sub> − S<sub>n−1</sub> = n(2n − 1) − (n − 1)(2n − 3) = 2n² − n − (2n² − 5n + 3) = 4n − 3. '
       'Hence the series is 1 + 5 + 9 + 13 + ... (an A.P. with a = 1, d = 4).', 144),
    bq(U, EX4, 'EX4.4', '5', 'Find the sum of the first 100 natural numbers which are neither exactly divisible by 3 nor by 7.',
       '2842',
       'Sum of 1 to 100 = 100·101/2 = 5050. Multiples of 3: 3 + 6 + ... + 99 = 3(1 + 2 + ... + 33) = 3·561 = 1683. '
       'Multiples of 7: 7 + ... + 98 = 7(1 + ... + 14) = 7·105 = 735. Multiples of 21 (counted twice): 21 + 42 + 63 + 84 = 210. '
       'Required sum = 5050 − 1683 − 735 + 210 = 2842.', 144),
    bq(U, EX4, 'EX4.4', '6', 'If S<sub>2</sub>, S<sub>3</sub>, S<sub>5</sub> are the sums of 2n, 3n and 5n terms of an A.P., show that S<sub>5</sub> = 5(S<sub>3</sub> − S<sub>2</sub>).',
       'S<sub>5</sub> = 5(S<sub>3</sub> − S<sub>2</sub>)',
       'For an A.P. with first term a and common difference d, the sum of kn terms is S<sub>k</sub> = (kn/2)[2a + (kn − 1)d]. Hence '
       'S<sub>3</sub> − S<sub>2</sub> = (3n/2)[2a + (3n − 1)d] − (2n/2)[2a + (2n − 1)d] = (n/2)[6a + 3n(3n − 1)d − 4a − 2n(2n − 1)d] '
       '= (n/2)[2a + (9n² − 3n − 4n² + 2n)d] = (n/2)[2a + (5n² − n)d] = (n/2)[2a + (5n − 1)d]. '
       'Multiplying by 5 gives (5n/2)[2a + (5n − 1)d] = S<sub>5</sub>, as required.', 144),
    bq(U, EX4, 'EX4.4', '7', 'The sums of n terms of two arithmetic series are in the ratio (3n + 2) : (n + 1). Find the ratio of their 8th terms.',
       '47 : 16',
       'Let the first terms be a, a′ and the common differences d, d′. Then S<sub>n</sub>/S′<sub>n</sub> = [2a + (n − 1)d]/[2a′ + (n − 1)d′] '
       '= (3n + 2)/(n + 1). The ratio of the 8th terms is [a + 7d]/[a′ + 7d′], which equals S<sub>n</sub>/S′<sub>n</sub> when (n − 1)/2 = 7, '
       'i.e. n = 15. Hence the ratio is (3·15 + 2)/(15 + 1) = 47/16.', 144),
    bq(U, EX4, 'EX4.4', '8', 'The sum of three numbers in A.P. is 27 and their product is 405. Find the numbers.',
       '3, 9, 15 or 15, 9, 3',
       'Let the numbers be a − d, a, a + d. Their sum is 3a = 27, so a = 9. Their product is (9 − d)(9)(9 + d) = 405, i.e. 9(81 − d²) = 405, '
       '81 − d² = 45, d² = 36, d = ±6. For d = 6 the numbers are 3, 9, 15; for d = −6 they are 15, 9, 3.', 144),
    bq(U, EX4, 'EX4.4', '9', 'Find five numbers in A.P. whose sum is 25 and the sum of whose squares is 135.',
       '3, 4, 5, 6, 7 or 7, 6, 5, 4, 3',
       'Let the numbers be a − 2d, a − d, a, a + d, a + 2d. Their sum is 5a = 25, so a = 5. The sum of squares is '
       '(25 − 20d + 4d²) + (25 − 10d + d²) + 25 + (25 + 10d + d²) + (25 + 20d + 4d²) = 125 + 10d² = 135, so d² = 1 and d = ±1. '
       'The numbers are 3, 4, 5, 6, 7 (or 7, 6, 5, 4, 3).', 144),
    bq(U, EX4, 'EX4.4', '10', 'The sum of Rs. 42,000 is distributed among five persons so that each person after the first receives Rs. 80 less than the preceding person. How much does each person receive?',
       'Rs. 8560, Rs. 8480, Rs. 8400, Rs. 8320 and Rs. 8240',
       'Let the shares be a, a − 80, a − 160, a − 240, a − 320 (an A.P. with d = −80). Their sum is 5a − 800 = 42000, so 5a = 42800 and a = 8560. '
       'The shares are Rs. 8560, Rs. 8480, Rs. 8400, Rs. 8320 and Rs. 8240.', 144),
    bq(U, EX4, 'EX4.4', '11', 'A well digging company charges Rs. 1,250 for the first metre, Rs. 1,500 for the second metre and Rs. 1,750 for the third metre and so on. What is the depth of a well that costs Rs. 50,000?',
       '16 metres',
       'a = 1250, d = 250. S<sub>n</sub> = (n/2)[2(1250) + (n − 1)250] = (n/2)(2250 + 250n) = 50000. So n(2250 + 250n) = 100000, '
       'i.e. n² + 9n − 400 = 0, giving n = (−9 + √(81 + 1600))/2 = (−9 + 41)/2 = 16. The depth is 16 metres.', 144),
    bq(U, EX4, 'EX4.4', '12', 'A man borrows Rs. 25,000 and agrees to repay with a total profit of Rs. 10,000 in 10 installments, each installment being less than the preceding by Rs. 200. What should be his first installment?',
       'Rs. 4,400',
       'The total repayment is 25000 + 10000 = 35000 in 10 installments forming an A.P. with d = −200. '
       'S<sub>10</sub> = (10/2)[2a + 9(−200)] = 5(2a − 1800) = 35000, so 2a − 1800 = 7000 and a = 4400. The first installment is Rs. 4,400.', 144),
]

# ============================================================== Exercise 4.5 (pdf 148)
ITEMS += [
    bq(U, EX5, 'EX4.5', '1(i)', 'Find the indicated term of the G.P. 3, 6, 12, ... ; find the 5th term.',
       'a<sub>5</sub> = 48',
       'a = 3 and r = 6/3 = 2. a<sub>5</sub> = ar<sup>5−1</sup> = 3·2⁴ = 3(16) = 48.', 148),
    bq(U, EX5, 'EX4.5', '1(ii)', 'Find the indicated term of the G.P. 32, 16, 8, ... ; find the 9th term.',
       'a<sub>9</sub> = 1/8',
       'a = 32 and r = 16/32 = 1/2. a<sub>9</sub> = 32(1/2)⁸ = 32/256 = 1/8.', 148),
    bq(U, EX5, 'EX4.5', '1(iii)', 'Find the indicated term of the G.P. 4, 2√2, 2, ... ; find the 12th term.',
       'a<sub>12</sub> = √2/16',
       'a = 4 and r = 2√2/4 = √2/2 = 1/√2. Then a<sub>12</sub> = 4(1/√2)<sup>11</sup> = 4/(2<sup>11/2</sup>) = 2²·2<sup>−11/2</sup> = 2<sup>−7/2</sup> = 1/(8√2) = √2/16.', 148),
    bq(U, EX5, 'EX4.5', '1(iv)', 'Find the indicated term of the G.P. i, 1, −i, ... ; find the 16th term.',
       'a<sub>16</sub> = −1',
       'a = i and r = 1/i = −i. Then a<sub>16</sub> = i(−i)<sup>15</sup>. Now (−i)<sup>15</sup> = ((−i)²)⁷(−i) = (−1)⁷(−i) = i, '
       'so a<sub>16</sub> = i·i = −1.', 148),
    bq(U, EX5, 'EX4.5', '1(v)', 'Find the indicated term of the G.P. b² − c², b + c, (b + c)/(b − c), ... ; find the 9th term.',
       'a<sub>9</sub> = (b + c)/(b − c)⁷',
       'r = (b + c)/(b² − c²) = 1/(b − c). Hence a<sub>9</sub> = (b² − c²)[1/(b − c)]⁸ = (b² − c²)/(b − c)⁸ = (b + c)/(b − c)⁷.', 148),

    bq(U, EX5, 'EX4.5', '2', 'In a G.P., a<sub>1</sub> = 5/9 and a<sub>6</sub> = 15625/9. Find its nth term.',
       'a<sub>n</sub> = 5<sup>n</sup>/9',
       'a<sub>6</sub>/a<sub>1</sub> = r⁵ = (15625/9)/(5/9) = 3125 = 5⁵, so r = 5. Then a<sub>n</sub> = a<sub>1</sub>r<sup>n−1</sup> = (5/9)5<sup>n−1</sup> = 5<sup>n</sup>/9.', 148),
    bq(U, EX5, 'EX4.5', '3', 'Find the nth term of the geometric sequence if a<sub>5</sub>/a<sub>3</sub> = 4/9 and a<sub>2</sub> = 4/9.',
       'a<sub>n</sub> = (2/3)<sup>n</sup> or a<sub>n</sub> = (−2/3)<sup>n</sup>',
       'a<sub>5</sub>/a<sub>3</sub> = r² = 4/9, so r = ±2/3. Since a<sub>2</sub> = a<sub>1</sub>r = 4/9, a<sub>1</sub> = (4/9)/r. '
       'For r = 2/3, a<sub>1</sub> = 2/3 and a<sub>n</sub> = (2/3)(2/3)<sup>n−1</sup> = (2/3)<sup>n</sup>; for r = −2/3, a<sub>1</sub> = −2/3 and '
       'a<sub>n</sub> = (−2/3)(−2/3)<sup>n−1</sup> = (−2/3)<sup>n</sup>. The printed key gives (−1)<sup>n</sup>(2/3)<sup>n</sup> or (−2/3)<sup>n</sup>, '
       'but these are the same sequence, so the key omits the equally valid positive ratio r = 2/3, which gives a<sub>n</sub> = (2/3)<sup>n</sup>.', 148),
    bq(U, EX5, 'EX4.5', '4', 'Show that the reciprocals of the terms of the G.P. a<sub>1</sub>, a<sub>1</sub>r², a<sub>1</sub>r⁴, ... form another G.P.',
       'The reciprocals 1/a<sub>1</sub>, 1/(a<sub>1</sub>r²), 1/(a<sub>1</sub>r⁴), ... form a G.P. with common ratio 1/r².',
       'The given terms have the constant ratio a<sub>1</sub>r²/a<sub>1</sub> = r², so they form a G.P. The reciprocals are '
       '1/a<sub>1</sub>, 1/(a<sub>1</sub>r²), 1/(a<sub>1</sub>r⁴), ... and the ratio of any term to the previous one is '
       '[1/(a<sub>1</sub>r²)]/[1/a<sub>1</sub>] = 1/r², which is constant. Hence the reciprocals form a G.P. with common ratio 1/r².', 148),
    bq(U, EX5, 'EX4.5', '5', 'How many terms are there in the G.P. 1/3, 1/12, 1/48, ..., 1/196608?',
       '9 terms',
       'a = 1/3 and r = (1/12)/(1/3) = 1/4. Put a<sub>n</sub> = 1/196608: (1/3)(1/4)<sup>n−1</sup> = 1/196608, so 4<sup>n−1</sup> = 196608/3 = 65536 = 4⁸. '
       'Hence n − 1 = 8 and n = 9.', 148),
    bq(U, EX5, 'EX4.5', '6', 'Find three consecutive numbers in G.P. whose sum is 39 and whose product is 729.',
       '3, 9, 27 (or 27, 9, 3)',
       'Let the numbers be a/r, a, ar. Their product is a³ = 729, so a = 9. Their sum is 9(1/r + 1 + r) = 39, i.e. 9r² − 30r + 9 = 0, '
       'or 3r² − 10r + 3 = 0, giving r = 3 or r = 1/3. The numbers are 3, 9, 27 (or 27, 9, 3).', 148),
    bq(U, EX5, 'EX4.5', '7', 'The number of bacteria in a culture increased in G.P. from 515,000 to 15,45,000 in 7 days. Find the daily rate of increase, assuming the rate of increase to be constant.',
       'r = 3<sup>1/7</sup> ≈ 1.17, i.e. about 17% per day',
       'Let a<sub>1</sub> = 515000 and a<sub>8</sub> = 1545000 (7 days later). Then a<sub>8</sub> = a<sub>1</sub>r⁷ gives r⁷ = 1545000/515000 = 3, '
       'so r = 3<sup>1/7</sup> ≈ 1.1699. The number increases by a factor of about 1.17 each day, i.e. the daily rate of increase is about 17%.', 148),
    bq(U, EX5, 'EX4.5', '8', 'Find the profit on Rs. 1000 for 5 years at 4% per annum compound profit.',
       'Profit = 1000(1.04⁵ − 1) ≈ Rs. 216.65',
       'The amount after 5 years is A = 1000(1 + 4/100)⁵ = 1000(1.04)⁵ = 1000(1.2166529) ≈ 1216.65. '
       'Profit = A − 1000 = 1000(1.04⁵ − 1) ≈ Rs. 216.65.', 148),
]

# ============================================================== Exercise 4.6 (pdf 150-151)
ITEMS += [
    bq(U, EX6, 'EX4.6', '1(i)', 'Find the geometric mean between −2 and −8.',
       'G.M. = ±4',
       'G = ±√(ab) = ±√[(−2)(−8)] = ±√16 = ±4.', 150),
    bq(U, EX6, 'EX4.6', '1(ii)', 'Find the geometric mean between 3 and 1/3.',
       'G.M. = ±1',
       'G = ±√(3 × 1/3) = ±√1 = ±1.', 150),
    bq(U, EX6, 'EX4.6', '1(iii)', 'Find the geometric mean between 8√2 and 9√2.',
       'G.M. = ±12',
       'G = ±√[(8√2)(9√2)] = ±√(72 × 2) = ±√144 = ±12.', 150),
    bq(U, EX6, 'EX4.6', '1(iv)', 'Find the geometric mean between −2i and 8i.',
       'G.M. = ±4',
       'G = ±√[(−2i)(8i)] = ±√(−16i²) = ±√16 = ±4 (since i² = −1).', 150),
    bq(U, EX6, 'EX4.6', '1(v)', 'Find the geometric mean between 7 + i and 7 − i.',
       'G.M. = ±5√2',
       'G = ±√[(7 + i)(7 − i)] = ±√(49 − i²) = ±√(49 + 1) = ±√50 = ±5√2.', 150),
    bq(U, EX6, 'EX4.6', '1(vi)', 'Find the geometric mean between 16/9 and 9/25.',
       'G.M. = ±4/5',
       'G = ±√[(16/9)(9/25)] = ±√(16/25) = ±4/5.', 150),

    bq(U, EX6, 'EX4.6', '2(i)', 'Insert two geometric means between 3 and 81.',
       '9 and 27',
       'The four terms 3, G<sub>1</sub>, G<sub>2</sub>, 81 form a G.P., so 81 = 3r³, r³ = 27, r = 3. Hence G<sub>1</sub> = 3(3) = 9 and G<sub>2</sub> = 9(3) = 27.', 151),
    bq(U, EX6, 'EX4.6', '2(ii)', 'Insert three geometric means between 2 and 1/2.',
       '√2, 1, √2/2',
       'There are 5 terms, so 1/2 = 2r⁴, r⁴ = 1/4, r = ±1/√2. Taking r = 1/√2: 2, 2/√2 = √2, 1, 1/√2 = √2/2, 1/2. '
       '(With r = −1/√2 the means are −√2, 1, −√2/2.)', 151),
    bq(U, EX6, 'EX4.6', '2(iii)', 'Insert four geometric means between 3 and 96.',
       '6, 12, 24, 48',
       'There are 6 terms, so 96 = 3r⁵, r⁵ = 32, r = 2. The means are 3(2) = 6, 12, 24 and 48.', 151),
    bq(U, EX6, 'EX4.6', '2(iv)', 'Insert five geometric means between 16 and 1024.',
       '32, 64, 128, 256, 512',
       'There are 7 terms, so 1024 = 16r⁶, r⁶ = 64, r = 2. The means are 32, 64, 128, 256 and 512.', 151),

    bq(U, EX6, 'EX4.6', '3', 'The arithmetic mean between two numbers is 29 and the geometric mean is 21; find the numbers.',
       '9 and 49',
       'Let the numbers be a and b. Then (a + b)/2 = 29, so a + b = 58; and √(ab) = 21, so ab = 441. The numbers are the roots of '
       't² − 58t + 441 = 0, i.e. t = [58 ± √(3364 − 1764)]/2 = (58 ± 40)/2. Hence the numbers are 49 and 9.', 151),
    bq(U, EX6, 'EX4.6', '4', 'For what value of n is (a<sup>n−2</sup> + b<sup>n−2</sup>)/(a<sup>n−3</sup> + b<sup>n−3</sup>) the geometric mean between a and b?',
       'n = 5/2',
       'We need (a<sup>n−2</sup> + b<sup>n−2</sup>)/(a<sup>n−3</sup> + b<sup>n−3</sup>) = √(ab) = a<sup>1/2</sup>b<sup>1/2</sup>. '
       'With n = 5/2 the expression becomes (a<sup>1/2</sup> + b<sup>1/2</sup>)/(a<sup>−1/2</sup> + b<sup>−1/2</sup>). '
       'Now a<sup>−1/2</sup> + b<sup>−1/2</sup> = 1/√a + 1/√b = (√a + √b)/√(ab), so the quotient is '
       '(√a + √b) · √(ab)/(√a + √b) = √(ab). Hence n = 5/2.', 151),
    bq(U, EX6, 'EX4.6', '5', 'Show that the nth root of the product of n geometric means between x and y is the geometric mean between x and y.',
       'The nth root of the product is √(xy), the G.M. of x and y.',
       'Let the n geometric means be G<sub>1</sub>, G<sub>2</sub>, ..., G<sub>n</sub>, so that x, G<sub>1</sub>, ..., G<sub>n</sub>, y is a G.P. with '
       'ratio r = (y/x)<sup>1/(n+1)</sup> and G<sub>k</sub> = xr<sup>k</sup>. Their product is '
       'G<sub>1</sub>G<sub>2</sub>...G<sub>n</sub> = x<sup>n</sup>r<sup>1+2+...+n</sup> = x<sup>n</sup>r<sup>n(n+1)/2</sup> '
       '= x<sup>n</sup>[(y/x)<sup>1/(n+1)</sup>]<sup>n(n+1)/2</sup> = x<sup>n</sup>(y/x)<sup>n/2</sup> = (xy)<sup>n/2</sup>. '
       'Taking the nth root gives (xy)<sup>1/2</sup> = √(xy), which is the geometric mean of x and y.', 151),
    bq(U, EX6, 'EX4.6', '6', 'The arithmetic mean of two positive integral numbers exceeds their (positive) geometric mean by 2 and their sum is 20. Find the numbers.',
       '16 and 4',
       'Let the numbers be a and b, with a + b = 20 and (a + b)/2 − √(ab) = 2. Then 10 − √(ab) = 2, so √(ab) = 8 and ab = 64. '
       'The numbers are the roots of t² − 20t + 64 = 0, i.e. (t − 16)(t − 4) = 0, giving 16 and 4.', 151),
    bq(U, EX6, 'EX4.6', '7', 'The arithmetic mean between two numbers is 5 and their (positive) geometric mean is 4. Find the numbers.',
       '8 and 2',
       'Let the numbers be a and b. Then a + b = 10 and ab = 4² = 16. They are the roots of t² − 10t + 16 = 0, i.e. (t − 8)(t − 2) = 0, '
       'giving 8 and 2.', 151),
]

# ============================================================== Exercise 4.7 (pdf 156)
ITEMS += [
    bq(U, EX7, 'EX4.7', '1(i)', 'Find the sum: 1 + 1/2 + 1/4 + ... + 1/512.',
       'S = 1 511/512',
       'This is a G.P. with a = 1 and r = 1/2. Since 1/512 = (1/2)⁹, there are n = 10 terms. '
       'S<sub>10</sub> = a(1 − r<sup>n</sup>)/(1 − r) = 1(1 − (1/2)<sup>10</sup>)/(1/2) = 2(1 − 1/1024) = 2 − 1/512 = 1023/512 = 1 511/512.', 156),
    bq(U, EX7, 'EX4.7', '1(ii)', 'Find the sum: 2⁶ + 2⁷ + 2⁸ + ... + 2¹³.',
       'S = 16320',
       'This is a G.P. with a = 2⁶ = 64, r = 2 and n = 13 − 6 + 1 = 8 terms. '
       'S<sub>8</sub> = 64(2⁸ − 1)/(2 − 1) = 64(256 − 1) = 64(255) = 16320.', 156),
    bq(U, EX7, 'EX4.7', '1(iii)', 'Find the sum: 1/x + 1/x² + 1/x³ + ... + 1/x⁸.',
       'S = (x⁸ − 1)/(x⁸(x − 1))',
       'a = 1/x, r = 1/x and n = 8. S = (1/x)[1 − (1/x)⁸]/[1 − 1/x] = (1/x)(1 − x<sup>−8</sup>)/[(x − 1)/x] = (1 − x<sup>−8</sup>)/(x − 1) '
       '= (x⁸ − 1)/(x⁸(x − 1)).', 156),
    bq(U, EX7, 'EX4.7', '1(iv)', 'Find the sum: 0.9 + 0.99 + 0.999 + ... to n terms.',
       'S<sub>n</sub> = n − (1/9)(1 − 1/10<sup>n</sup>)',
       'Write each term as 1 minus a power of 1/10: (1 − 0.1) + (1 − 0.01) + ... + (1 − 1/10<sup>n</sup>). Hence '
       'S<sub>n</sub> = n − (0.1 + 0.01 + ... + 1/10<sup>n</sup>) = n − (1/10)(1 − (1/10)<sup>n</sup>)/(1 − 1/10) = n − (1/9)(1 − 1/10<sup>n</sup>).', 156),
    bq(U, EX7, 'EX4.7', '1(v)', 'Find the sum: 7 + 77 + 777 + ... to n terms.',
       'S<sub>n</sub> = (7/9)[(10/9)(10<sup>n</sup> − 1) − n]',
       '7 + 77 + 777 + ... = (7/9)(9 + 99 + 999 + ...) = (7/9)[(10 − 1) + (10² − 1) + ... + (10<sup>n</sup> − 1)] '
       '= (7/9)[(10 + 10² + ... + 10<sup>n</sup>) − n] = (7/9)[10(10<sup>n</sup> − 1)/9 − n] = (7/9)[(10/9)(10<sup>n</sup> − 1) − n].', 156),
    bq(U, EX7, 'EX4.7', '1(vi)', 'Find the sum: 0.2 + 0.22 + 0.222 + ... to n terms.',
       'S<sub>n</sub> = (2/9)[n − (1/9)(1 − 1/10<sup>n</sup>)]',
       '0.2 + 0.22 + 0.222 + ... = (2/10)(1 + 1.1 + 1.11 + ...) = (2/9)(0.9 + 0.99 + 0.999 + ...). '
       'Using the result of part (iv), S<sub>n</sub> = (2/9)[n − (1/9)(1 − 1/10<sup>n</sup>)].', 156),
    bq(U, EX7, 'EX4.7', '1(vii)', 'Find the sum: 3 + 33 + 333 + ... to n terms.',
       'S<sub>n</sub> = (1/3)[(10/9)(10<sup>n</sup> − 1) − n]',
       '3 + 33 + 333 + ... = (3/9)(9 + 99 + 999 + ...) = (1/3)[(10 + 10² + ... + 10<sup>n</sup>) − n] '
       '= (1/3)[10(10<sup>n</sup> − 1)/9 − n] = (1/3)[(10/9)(10<sup>n</sup> − 1) − n].', 156),

    bq(U, EX7, 'EX4.7', '2(i)', 'Find the sum to n terms of the series 1 + (a + b) + (a² + ab + b²) + (a³ + a²b + ab² + b³) + ..., where a &gt; 1, b &gt; 1 and a &gt; b.',
       'S<sub>n</sub> = (1/(a − b)){a(a<sup>n</sup> − 1)/(a − 1) − b(b<sup>n</sup> − 1)/(b − 1)}',
       'The kth term is a<sup>k−1</sup> + a<sup>k−2</sup>b + ... + b<sup>k−1</sup> = (a<sup>k</sup> − b<sup>k</sup>)/(a − b). Hence '
       'S<sub>n</sub> = (1/(a − b))Σ<sub>k=1</sub><sup>n</sup>(a<sup>k</sup> − b<sup>k</sup>) '
       '= (1/(a − b)){a(a<sup>n</sup> − 1)/(a − 1) − b(b<sup>n</sup> − 1)/(b − 1)}.', 156),
    bq(U, EX7, 'EX4.7', '2(ii)', 'Find the sum to n terms of the series r + (1 + k)r² + (1 + k + k²)r³ + ..., where k and r are proper fractions.',
       'S<sub>n</sub> = (r/(1 − k)){(1 − r<sup>n</sup>)/(1 − r) − k(1 − k<sup>n</sup>r<sup>n</sup>)/(1 − kr)}',
       'The nth term is r<sup>n</sup>(1 + k + ... + k<sup>n−1</sup>) = r<sup>n</sup>(1 − k<sup>n</sup>)/(1 − k) = [r<sup>n</sup> − (kr)<sup>n</sup>]/(1 − k). Hence '
       'S<sub>n</sub> = (1/(1 − k))[Σr<sup>n</sup> − Σ(kr)<sup>n</sup>] = (1/(1 − k))[r(1 − r<sup>n</sup>)/(1 − r) − kr(1 − k<sup>n</sup>r<sup>n</sup>)/(1 − kr)] '
       '= (r/(1 − k))[(1 − r<sup>n</sup>)/(1 − r) − k(1 − k<sup>n</sup>r<sup>n</sup>)/(1 − kr)].', 156),
    bq(U, EX7, 'EX4.7', '3', 'If a<sub>n</sub> = (1/4)<sup>n</sup>, then find the sum of the sequence up to n terms.',
       'S<sub>n</sub> = (4<sup>n</sup> − 1)/(3·4<sup>n</sup>)',
       'This is a G.P. with a<sub>1</sub> = 1/4 and r = 1/4. S<sub>n</sub> = (1/4)[1 − (1/4)<sup>n</sup>]/(1 − 1/4) = (1/4)(1 − 4<sup>−n</sup>)/(3/4) '
       '= (1/3)(1 − 4<sup>−n</sup>) = (4<sup>n</sup> − 1)/(3·4<sup>n</sup>).', 156),

    bq(U, EX7, 'EX4.7', '4(i)', 'Find the sum of the infinite geometric series 1/5 + 1/25 + 1/125 + ...',
       'S<sub>∞</sub> = 1/4',
       'a = 1/5, r = 1/5, and |r| &lt; 1. S<sub>∞</sub> = a/(1 − r) = (1/5)/(1 − 1/5) = (1/5)/(4/5) = 1/4.', 156),
    bq(U, EX7, 'EX4.7', '4(ii)', 'Find the sum of the infinite geometric series 1/2 + 1/4 + 1/8 + ...',
       'S<sub>∞</sub> = 1',
       'a = 1/2, r = 1/2. S<sub>∞</sub> = (1/2)/(1 − 1/2) = (1/2)/(1/2) = 1.', 156),
    bq(U, EX7, 'EX4.7', '4(iii)', 'Find the sum of the infinite geometric series 9/4 + 3/2 + 1 + 2/3 + ...',
       'S<sub>∞</sub> = 27/4',
       'a = 9/4 and r = (3/2)/(9/4) = 2/3. S<sub>∞</sub> = (9/4)/(1 − 2/3) = (9/4)/(1/3) = 27/4.', 156),
    bq(U, EX7, 'EX4.7', '4(iv)', 'Find the sum of the infinite geometric series 2 + √2 + 1 + ...',
       'S<sub>∞</sub> = 4 + 2√2',
       'a = 2 and r = √2/2 = 1/√2. S<sub>∞</sub> = 2/(1 − 1/√2) = 2√2/(√2 − 1) = 2√2(√2 + 1) = 4 + 2√2.', 156),
    bq(U, EX7, 'EX4.7', '4(v)', 'Find the sum of the infinite geometric series 2 + 1 + 0.5 + ...',
       'S<sub>∞</sub> = 4',
       'a = 2 and r = 1/2. S<sub>∞</sub> = 2/(1 − 1/2) = 4.', 156),
    bq(U, EX7, 'EX4.7', '4(vi)', 'Find the sum of the infinite geometric series 4 + 2√2 + 2 + √2 + 1 + ...',
       'S<sub>∞</sub> = 4(2 + √2) = 8 + 4√2',
       'a = 4 and r = (2√2)/4 = 1/√2. S<sub>∞</sub> = 4/(1 − 1/√2) = 4√2/(√2 − 1) = 4√2(√2 + 1) = 8 + 4√2 = 4(2 + √2).', 156),
    bq(U, EX7, 'EX4.7', '4(vii)', 'Find the sum of the infinite geometric series 0.1 + 0.05 + 0.025 + ...',
       'S<sub>∞</sub> = 0.2',
       'a = 0.1 and r = 0.05/0.1 = 0.5. S<sub>∞</sub> = 0.1/(1 − 0.5) = 0.1/0.5 = 0.2.', 156),

    bq(U, EX7, 'EX4.7', '5(i)', 'Find the vulgar fraction equivalent to the recurring decimal 0.7̇ (the digit 7 repeats).',
       '7/9',
       'Let x = 0.777... Then 10x = 7.777..., so 10x − x = 7, i.e. 9x = 7 and x = 7/9.', 156),
    bq(U, EX7, 'EX4.7', '5(ii)', 'Find the vulgar fraction equivalent to the recurring decimal 1.7̇4̇ (the block 74 repeats).',
       '1 74/99 = 173/99',
       'Let x = 1.747474... Then 100x = 174.7474..., so 100x − x = 173 and 99x = 173, giving x = 173/99 = 1 74/99.', 156),
    bq(U, EX7, 'EX4.7', '5(iii)', 'Find the vulgar fraction equivalent to the recurring decimal 0.2̇5̇9̇ (the block 259 repeats).',
       '259/999',
       'Let x = 0.259259... Then 1000x = 259.259259..., so 1000x − x = 259 and 999x = 259, giving x = 259/999.', 156),
    bq(U, EX7, 'EX4.7', '5(iv)', 'Find the vulgar fraction equivalent to the recurring decimal 1.14̇8̇ (the block 48 repeats).',
       '1 147/990 = 379/330',
       'Let x = 1.1484848... Then 10x = 11.484848... and 1000x = 1148.484848..., so 990x = 1137 and x = 1137/990 = 379/330 = 1 147/990.', 156),
    bq(U, EX7, 'EX4.7', '5(v)', 'Find the vulgar fraction equivalent to the recurring decimal 2.2̇3̇ (the block 23 repeats).',
       '2 23/99 = 221/99',
       'Let x = 2.232323... Then 100x = 223.2323..., so 99x = 221 and x = 221/99 = 2 23/99.', 156),

    bq(U, EX7, 'EX4.7', '6', 'If a = b/2 + b²/4 + b³/8 + ... where 0 &lt; b &lt; 2, then prove that b = 2a/(1 + a).',
       'b = 2a/(1 + a)',
       'The right side is an infinite G.P. with first term b/2 and common ratio b/2, and 0 &lt; b &lt; 2 gives |b/2| &lt; 1. Hence '
       'a = (b/2)/(1 − b/2) = b/(2 − b). Then a(2 − b) = b, i.e. 2a − ab = b, so 2a = b(1 + a) and b = 2a/(1 + a).', 156),
    bq(U, EX7, 'EX4.7', '7', 'The sum of an infinite geometric series is half the sum of the squares of its terms. If the sum of its first two terms is 4 1/2, find the series.',
       '3 + 3/2 + 3/4 + 3/8 + ...',
       'Let the first term be a and the ratio r. Then S = a/(1 − r) and the sum of the squares is a²/(1 − r²). The condition '
       'a/(1 − r) = (1/2)a²/(1 − r²) gives 2(1 − r²) = a(1 − r), i.e. 2(1 − r)(1 + r) = a(1 − r), so a = 2(1 + r). '
       'Also a + ar = 9/2, i.e. a(1 + r) = 9/2, so 2(1 + r)² = 9/2, (1 + r)² = 9/4 and 1 + r = 3/2. Hence r = 1/2 and a = 3. '
       'The series is 3 + 3/2 + 3/4 + 3/8 + ...', 156),
    bq(U, EX7, 'EX4.7', '8', 'Joining the midpoints of the sides of an equilateral triangle, an equilateral triangle having half the perimeter of the original triangle is obtained. We form a sequence of nested equilateral triangles in this manner with the original triangle having perimeter 5/2. What will be the total perimeter of all the triangles formed in this way?',
       'Total perimeter = 5',
       'The perimeters are 5/2, 5/4, 5/8, ... — an infinite G.P. with a = 5/2 and r = 1/2. Their total is '
       'S<sub>∞</sub> = (5/2)/(1 − 1/2) = (5/2)/(1/2) = 5.', 156),
]

# ============================================================== Exercise 4.8 (pdf 159)
ITEMS += [
    bq(U, EX8, 'EX4.8', '1(i)', 'Find the indicated term of the harmonic progression 1/3, 1/7, 1/11, ... ; find the 9th term.',
       'T<sub>9</sub> = 1/35',
       'The reciprocals 3, 7, 11, ... form an A.P. with a = 3 and d = 4. Its 9th term is 3 + 8(4) = 35. '
       'Hence the 9th term of the H.P. is the reciprocal, 1/35.', 159),
    bq(U, EX8, 'EX4.8', '1(ii)', 'Find the indicated term of the harmonic progression 1/3, 1/5, 1/7, ... ; find the 12th term.',
       'T<sub>12</sub> = 1/25',
       'The reciprocals 3, 5, 7, ... form an A.P. with a = 3 and d = 2. Its 12th term is 3 + 11(2) = 25, so the 12th term of the H.P. is 1/25.', 159),
    bq(U, EX8, 'EX4.8', '1(iii)', 'Find the indicated term of the harmonic progression 9/5, 9/13, 9/21, ... ; find the 8th term.',
       'T<sub>8</sub> = 9/61',
       'The reciprocals 5/9, 13/9, 21/9, ... form an A.P. with a = 5/9 and d = 8/9. Its 8th term is 5/9 + 7(8/9) = 61/9. '
       'Hence the 8th term of the H.P. is 9/61.', 159),
    bq(U, EX8, 'EX4.8', '1(iv)', 'Find the indicated term of the harmonic progression −1/5, −1/3, −1, ... ; find the 15th term.',
       'T<sub>15</sub> = 1/23',
       'The reciprocals −5, −3, −1, ... form an A.P. with a = −5 and d = 2. Its 15th term is −5 + 14(2) = 23, so the 15th term of the H.P. is 1/23.', 159),
    bq(U, EX8, 'EX4.8', '1(v)', 'Find the indicated term of the harmonic progression 1/2, 1/5, 1/8, ... ; find the 8th term.',
       'T<sub>8</sub> = 1/23',
       'The reciprocals 2, 5, 8, ... form an A.P. with a = 2 and d = 3. Its 8th term is 2 + 7(3) = 23, so the 8th term of the H.P. is 1/23.', 159),
    bq(U, EX8, 'EX4.8', '1(vi)', 'Find the indicated term of the harmonic progression 1/3, 1/8, 1/13, ... ; find the 11th term.',
       'T<sub>11</sub> = 1/53',
       'The reciprocals 3, 8, 13, ... form an A.P. with a = 3 and d = 5. Its 11th term is 3 + 10(5) = 53, so the 11th term of the H.P. is 1/53.', 159),

    bq(U, EX8, 'EX4.8', '2', 'If the 7th and 10th terms of an H.P. are 1/3 and 5/21 respectively, find its 14th and 20th terms.',
       'T<sub>14</sub> = 5/29 and T<sub>20</sub> = 5/41',
       'The corresponding A.P. of reciprocals has 7th term 3 and 10th term 21/5. Hence 3d = 21/5 − 3 = 6/5, so d = 2/5 and '
       'a = 3 − 6(2/5) = 3/5. Then a<sub>14</sub> = 3/5 + 13(2/5) = 29/5, so T<sub>14</sub> = 5/29; and a<sub>20</sub> = 3/5 + 19(2/5) = 41/5, '
       'so T<sub>20</sub> = 5/41.', 159),
    bq(U, EX8, 'EX4.8', '3', 'If the sum of the first and sixth terms of an H.P. is 31/116, find the harmonic sequence if the first term is 1/4.',
       '1/4, 5/74, 5/128, ...',
       'The corresponding A.P. has first term 4. Let its sixth term be x. Then 1/4 + 1/x = 31/116, so 1/x = 31/116 − 29/116 = 2/116 = 1/58, '
       'i.e. x = 58. Hence 4 + 5d = 58, d = 54/5, and the A.P. is 4, 74/5, 128/5, ... . Taking reciprocals, the H.P. is '
       '1/4, 5/74, 5/128, ...', 159),
    bq(U, EX8, 'EX4.8', '4', 'The first term of an H.P. is −1/3 and the fifth term is 1/5. Find its 9th term.',
       'T<sub>9</sub> = 1/13',
       'The corresponding A.P. has first term −3 and fifth term 5, so 4d = 5 − (−3) = 8 and d = 2. Its 9th term is '
       '−3 + 8(2) = 13, so the 9th term of the H.P. is 1/13.', 159),
    bq(U, EX8, 'EX4.8', '5', 'If the pth term of an H.P. is q and the qth term is p, prove that the (p + q)th term is pq/(p + q).',
       'T<sub>p+q</sub> = pq/(p + q)',
       'For the corresponding A.P., the pth term is 1/q and the qth term is 1/p. Hence (p − q)d = 1/q − 1/p = (p − q)/(pq), so d = 1/(pq). '
       'Then A<sub>1</sub> = 1/q − (p − 1)d = 1/q − (p − 1)/(pq) = (p − p + 1)/(pq) = 1/(pq). Therefore '
       'A<sub>p+q</sub> = 1/(pq) + (p + q − 1)/(pq) = (p + q)/(pq), and the (p + q)th term of the H.P. is its reciprocal, pq/(p + q).', 159),
]

# ============================================================== Exercise 4.9 (pdf 163)
ITEMS += [
    bq(U, EX9, 'EX4.9', '1(i)', 'Insert the harmonic mean between 1/64 and 1/81.',
       'H.M. = 2/145',
       'H = 2ab/(a + b) with a = 1/64, b = 1/81: H = 2/(64·81) ÷ (1/64 + 1/81) = [2/(64·81)] ÷ [(81 + 64)/(64·81)] = 2/145.', 163),
    bq(U, EX9, 'EX4.9', '1(ii)', 'Insert the harmonic mean between 1/5 and 1/17.',
       'H.M. = 1/11',
       'H = 2ab/(a + b) = [2/(5·17)] ÷ (1/5 + 1/17) = [2/85] ÷ [(17 + 5)/85] = 2/22 = 1/11.', 163),
    bq(U, EX9, 'EX4.9', '1(iii)', 'Insert the harmonic mean between 3 + √2 and 3 − √2.',
       'H.M. = 2 1/3 = 7/3',
       'Here ab = (3 + √2)(3 − √2) = 9 − 2 = 7 and a + b = 6. So H = 2ab/(a + b) = 14/6 = 7/3 = 2 1/3.', 163),
    bq(U, EX9, 'EX4.9', '1(iv)', 'Insert the harmonic mean between 2 + 3i and 2 − 3i.',
       'H.M. = 6 1/2 = 13/2',
       'Here ab = (2 + 3i)(2 − 3i) = 4 + 9 = 13 and a + b = 4. So H = 2ab/(a + b) = 26/4 = 13/2 = 6 1/2.', 163),
    bq(U, EX9, 'EX4.9', '1(v)', 'Insert the harmonic mean between 1/7 and 1/11.',
       'H.M. = 1/9',
       'H = [2/(7·11)] ÷ (1/7 + 1/11) = [2/77] ÷ [(11 + 7)/77] = 2/18 = 1/9.', 163),
    bq(U, EX9, 'EX4.9', '1(vi)', 'Insert the harmonic mean between 3 and 7.',
       'H.M. = 21/5',
       'H = 2ab/(a + b) = 2(3)(7)/(3 + 7) = 42/10 = 21/5.', 163),

    bq(U, EX9, 'EX4.9', '2(i)', 'Insert four harmonic means between 4 and 20.',
       '100/21, 100/17, 100/13, 100/9',
       'The reciprocals 1/4 and 1/20 must be the first and sixth terms of an A.P., so d = (1/20 − 1/4)/5 = (−4/20)/5 = −1/25. '
       'The A.P. is 1/4, 21/100, 17/100, 13/100, 9/100, 1/20, and taking reciprocals of the four middle terms gives '
       '100/21, 100/17, 100/13, 100/9.', 163),
    bq(U, EX9, 'EX4.9', '2(ii)', 'Insert four harmonic means between 1/9 and 1/81.',
       '5/117, 5/189, 5/261, 5/333',
       'The reciprocals 9 and 81 are the first and sixth terms of an A.P., so d = (81 − 9)/5 = 72/5. The A.P. is '
       '9, 117/5, 189/5, 261/5, 333/5, 81, and the harmonic means are 5/117, 5/189, 5/261, 5/333.', 163),
    bq(U, EX9, 'EX4.9', '3', 'Insert five harmonic means between 1/4 and 1/24.',
       '3/22, 3/32, 1/14, 3/52, 3/62',
       'The reciprocals 4 and 24 are the first and seventh terms of an A.P., so d = (24 − 4)/6 = 10/3. The A.P. is '
       '4, 22/3, 32/3, 14, 52/3, 62/3, 24, and the harmonic means are 3/22, 3/32, 1/14, 3/52, 3/62.', 163),
    bq(U, EX9, 'EX4.9', '4', 'Prove that the square of the geometric mean of two numbers equals the product of the arithmetic mean and the harmonic mean of the two numbers.',
       'G² = A·H',
       'For two numbers a and b: G = √(ab), A = (a + b)/2 and H = 2ab/(a + b). Then '
       'A·H = [(a + b)/2]·[2ab/(a + b)] = ab = G², as required.', 163),
    bq(U, EX9, 'EX4.9', '5', 'Find n so that (x<sup>n−5</sup> + y<sup>n−5</sup>)/(x<sup>n−6</sup> + y<sup>n−6</sup>) may be the harmonic mean between x and y.',
       'n = 5',
       'We need (x<sup>n−5</sup> + y<sup>n−5</sup>)/(x<sup>n−6</sup> + y<sup>n−6</sup>) = 2xy/(x + y). Cross-multiplying: '
       '(x + y)(x<sup>n−5</sup> + y<sup>n−5</sup>) = 2xy(x<sup>n−6</sup> + y<sup>n−6</sup>), i.e. '
       'x<sup>n−4</sup> + xy<sup>n−5</sup> + yx<sup>n−5</sup> + y<sup>n−4</sup> = 2x<sup>n−5</sup>y + 2xy<sup>n−5</sup>. Hence '
       'x<sup>n−4</sup> + y<sup>n−4</sup> = x<sup>n−5</sup>y + xy<sup>n−5</sup>, i.e. x<sup>n−5</sup>(x − y) = y<sup>n−5</sup>(x − y), so for x ≠ y '
       'x<sup>n−5</sup> = y<sup>n−5</sup> and n − 5 = 0, giving n = 5.', 163),
    bq(U, EX9, 'EX4.9', '6', 'If 5 is the harmonic mean between 2 and b, find b.',
       'b = −10',
       'H = 2ab/(a + b) gives 5 = 2(2)b/(2 + b) = 4b/(2 + b). Hence 5(2 + b) = 4b, i.e. 10 + 5b = 4b and b = −10.', 163),
    bq(U, EX9, 'EX4.9', '7', 'Find the arithmetic, harmonic and geometric means between 1 and 9. Also verify that AH = G².',
       'A.M. = 5, G.M. = ±3, H.M. = 9/5; AH = 9 = G²',
       'A = (1 + 9)/2 = 5; G = ±√(1·9) = ±3; H = 2(1)(9)/(1 + 9) = 18/10 = 9/5. Verification: AH = 5(9/5) = 9 and G² = (±3)² = 9, so AH = G².', 163),
    bq(U, EX9, 'EX4.9', '8', 'The arithmetic mean of two numbers is 8 and the harmonic mean is 6. Find the numbers.',
       '4 and 12',
       'Let the numbers be a and b. Then (a + b)/2 = 8, so a + b = 16, and 2ab/(a + b) = 6 gives 2ab/16 = 6, i.e. ab = 48. '
       'The numbers are the roots of t² − 16t + 48 = 0, i.e. (t − 12)(t − 4) = 0, giving 12 and 4.', 163),
    bq(U, EX9, 'EX4.9', '9', 'The harmonic mean of two numbers is 24/5 and the geometric mean is 6. Find the numbers.',
       '3 and 12',
       'Let the numbers be a and b. Then ab = 6² = 36 and 2ab/(a + b) = 24/5 gives 72/(a + b) = 24/5, so a + b = 15. '
       'The numbers are the roots of t² − 15t + 36 = 0, i.e. (t − 12)(t − 3) = 0, giving 12 and 3.', 163),
]

# ============================================================== Review Exercise 4 (pdf 164-165)
ITEMS += [
    mcq(U, REV, 'REV4', 'i', 'A sequence is a function whose domain is set of:',
        ['integers', 'rational numbers', 'natural numbers', 'real numbers'], 'c',
        'A sequence is a function whose domain is the set of natural numbers (or a subset of it), i.e. it is a list indexed by 1, 2, 3, ...', 164),
    mcq(U, REV, 'REV4', 'ii', 'If H is the harmonic mean between x and y then H is:',
        ['2(x + y)/(xy)', '(x + y)/(2xy)', '2xy/(x + y)', 'xy/(x + y)'], 'c',
        'The harmonic mean of x and y is the reciprocal of the arithmetic mean of the reciprocals: '
        'H = 2/(1/x + 1/y) = 2xy/(x + y).', 164),
    mcq(U, REV, 'REV4', 'iii', 'If a<sub>n</sub> − a<sub>n−1</sub> = n + 1 and a<sub>4</sub> = 14 then a<sub>5</sub> = ----------:',
        ['3', '5', '14', '20'], 'd',
        'Put n = 5: a<sub>5</sub> − a<sub>4</sub> = 5 + 1 = 6, so a<sub>5</sub> = 14 + 6 = 20.', 164),
    mcq(U, REV, 'REV4', 'iv', 'A sequence {a<sub>n</sub>} in which a<sub>n+1</sub> − a<sub>n</sub> is the same number for all n ∈ ℕ is called:',
        ['A.P', 'G.P', 'H.P', 'None of these'], 'a',
        'A constant difference between consecutive terms is the defining property of an arithmetic progression (A.P.).', 164),
    mcq(U, REV, 'REV4', 'v', 'If a<sub>n−1</sub>, a<sub>n</sub>, a<sub>n+1</sub> are in A.P, then a<sub>n</sub> is called:',
        ['A.M', 'G.M', 'H.M', 'Mid-point'], 'a',
        'In an A.P. the middle term is the arithmetic mean of the two neighbouring terms: a<sub>n</sub> = (a<sub>n−1</sub> + a<sub>n+1</sub>)/2.', 164),
    mcq(U, REV, 'REV4', 'vi', 'Arithmetic mean between c and d is:',
        ['(c + d)/2', '(c + d)/(2cd)', '2cd/(c + d)', '2/(c + d)'], 'a',
        'The arithmetic mean of two numbers is half their sum: (c + d)/2.', 164),
    mcq(U, REV, 'REV4', 'vii', 'The harmonic mean between √2 and 3√2 is:',
        ['4√2', '4/√2', '(3/2)√2', 'None of these'], 'c',
        'H = 2ab/(a + b) = 2(√2)(3√2)/(√2 + 3√2) = 12/(4√2) = 3/√2 = 3√2/2, i.e. (3/2)√2.', 164),
    mcq(U, REV, 'REV4', 'viii', 'For any G.P the common ratio r is equal to:',
        ['a<sub>n</sub>/a<sub>n+1</sub>', 'a<sub>n−1</sub>/a<sub>n</sub>', 'a<sub>n</sub>/a<sub>n−1</sub>', 'a<sub>n+1</sub> − a<sub>n</sub> for n ∈ ℕ, n &gt; 1'], 'c',
        'In a G.P. each term is r times the previous one, so r = a<sub>n</sub>/a<sub>n−1</sub>. '
        'Option (a) gives 1/r and (d) is the difference of consecutive terms, not a ratio.', 164),
    mcq(U, REV, 'REV4', 'ix', 'No term of a G.P is:',
        ['0', '1', 'Negative', 'Imaginary number'], 'a',
        'If a term of a G.P. were 0, every later term (being a fixed multiple of it) would also be 0 and the common ratio would be undefined. '
        'Hence no term of a G.P. is zero (terms may be 1, negative or imaginary).', 164),
    mcq(U, REV, 'REV4', 'x', 'The sum of infinite geometric series is a finite number if:',
        ['|r| &gt; 1', '|r| = 1', '|r| ≥ 1', '|r| &lt; 1'], 'd',
        'S<sub>∞</sub> = a/(1 − r) exists as a finite number only when |r| &lt; 1, because then r<sup>n</sup> → 0.', 164),
    mcq(U, REV, 'REV4', 'xi', 'If the reciprocals of the terms of a sequence form an A.P, then it is:',
        ['Harmonic sequence', 'Arithmetic sequence', 'Reciprocal sequence', 'Series'], 'a',
        'A sequence whose reciprocals form an A.P. is, by definition, a harmonic sequence (harmonic progression).', 164),
    mcq(U, REV, 'REV4', 'xii', 'If (a<sup>n+1</sup> + b<sup>n+1</sup>)/(a<sup>n</sup> + b<sup>n</sup>) is A.M between a and b, then n is equal to:',
        ['0', '−1', '1', '1/2'], 'a',
        'The A.M. of a and b is (a + b)/2. For n = 0 the expression becomes (a + b)/(1 + 1) = (a + b)/2, so n = 0. '
        '(n = 1 gives a² + b² over a + b, which is not the A.M.)', 164),
    mcq(U, REV, 'REV4', 'xiii', 'If 1, x − 1, 3 are in A.P., then x = ----------:',
        ['0', '1', '2', '3'], 'd',
        'For an A.P. the middle term is the average of the extremes: 2(x − 1) = 1 + 3 = 4, so x − 1 = 2 and x = 3.', 164),
    mcq(U, REV, 'REV4', 'xiv', 'G.M between −2 and 8 is:',
        ['4i or −4i', '4 or −4', '16 or −16', '3 or −5'], 'a',
        'G = ±√[(−2)(8)] = ±√(−16) = ±4i. (Options (b) and (c) ignore that the product is negative.)', 165),
    mcq(U, REV, 'REV4', 'xv', 'General term of a sequence is (−1)<sup>n</sup>n². Its 4th term is:',
        ['−4', '−16', '16', '4'], 'c',
        'a<sub>4</sub> = (−1)⁴(4)² = 1 × 16 = 16.', 165),
    mcq(U, REV, 'REV4', 'xvi', 'If |r| &gt; 1 then infinite geometric series is ----------:',
        ['Convergent', 'Divergent', 'Undefined', 'both a and b'], 'b',
        'When |r| &gt; 1 the terms grow without bound (r<sup>n</sup> → ±∞) and the partial sums do not approach a finite limit, so the series diverges.', 165),
    mcq(U, REV, 'REV4', 'xvii', 'The harmonic mean of 1/3 and 2/5 is:',
        ['4/11', '3/4', '5/11', '11/4'], 'a',
        'H = 2ab/(a + b) = 2(1/3)(2/5)/(1/3 + 2/5) = (4/15)/(11/15) = 4/11.', 165),
    mcq(U, REV, 'REV4', 'xviii', 'If (a − b)/(b − c) = a/b, then a, b and c are in:',
        ['A.P', 'G.P', 'H.P', 'None of these'], 'b',
        'Cross-multiplying: b(a − b) = a(b − c), i.e. ab − b² = ab − ac, so b² = ac. This means b is the geometric mean of a and c, '
        'hence a, b, c are in G.P.', 165),

    bq(U, REV, 'REV4', '2', 'The 5th term of an arithmetic sequence is 60 and the 8th term is 90. Find the 12th term.',
       'a<sub>12</sub> = 130',
       'a<sub>5</sub> = a + 4d = 60 and a<sub>8</sub> = a + 7d = 90. Subtracting, 3d = 30, so d = 10 and a = 60 − 40 = 20. '
       'Hence a<sub>12</sub> = 20 + 11(10) = 130.', 165),
    bq(U, REV, 'REV4', '3', 'There are n arithmetic means between 8 and 32 such that the ratio of the third and 7th means is 3 : 5. Find the value of n.',
       'n = 8',
       'The common difference is d = (32 − 8)/(n + 1) = 24/(n + 1). The third mean is 8 + 3d and the seventh is 8 + 7d, so '
       '(8 + 3d)/(8 + 7d) = 3/5. Cross-multiplying: 40 + 15d = 24 + 21d, i.e. 6d = 16 and d = 8/3. Then 24/(n + 1) = 8/3 gives '
       'n + 1 = 9, so n = 8.', 165),
    bq(U, REV, 'REV4', '4', 'Find the sum of all the integers between 280 and 350 which are exactly divisible by 9.',
       'Sum = 2205',
       'The multiples of 9 between 280 and 350 are 288, 297, ..., 342 (288 = 9 × 32, 342 = 9 × 38), so there are 7 terms with a = 288, '
       'd = 9. S<sub>7</sub> = (7/2)(288 + 342) = (7/2)(630) = 7(315) = 2205.', 165),
    bq(U, REV, 'REV4', '5', 'How many terms are there in a G.P. if a = 8, a<sub>n</sub> = 1/512 and r = 1/2?',
       '13 terms',
       'a<sub>n</sub> = ar<sup>n−1</sup> gives 8(1/2)<sup>n−1</sup> = 1/512. As 8 = 2³ and 1/512 = 2<sup>−9</sup>, we get 3 − (n − 1) = −9, '
       'so n − 1 = 12 and n = 13. (Check: a<sub>13</sub> = 8(1/2)¹² = 2³·2<sup>−12</sup> = 2<sup>−9</sup> = 1/512.) '
       'The printed key gives 12 terms, which is incorrect since a<sub>12</sub> = 1/256, not 1/512.', 165),
    bq(U, REV, 'REV4', '6', 'The yearly depreciation of a certain machine is 20% of the value at the beginning of the year. If the original cost of the machine is Rs. 50,000, find the value after 5 years.',
       'Rs. 16,384',
       'Each year the value is multiplied by 1 − 20/100 = 0.8, so after 5 years it is 50000(0.8)⁵. Now (0.8)⁵ = 0.32768, hence '
       'the value is 50000 × 0.32768 = Rs. 16,384.', 165),
    bq(U, REV, 'REV4', '7', 'Find r, if S<sub>10</sub> = 244 S<sub>5</sub> in a G.P.',
       'r = 3',
       'For a G.P., S<sub>10</sub>/S<sub>5</sub> = [a(1 − r<sup>10</sup>)/(1 − r)]/[a(1 − r<sup>5</sup>)/(1 − r)] = (1 − r<sup>10</sup>)/(1 − r<sup>5</sup>) '
       '= 1 + r⁵. Hence 1 + r⁵ = 244, r⁵ = 243 = 3⁵ and r = 3.', 165),
    bq(U, REV, 'REV4', '8', 'If the A.M. and H.M. between two numbers are 5 and 4 1/5 respectively, find the numbers.',
       '3 and 7',
       'Let the numbers be a and b. Then (a + b)/2 = 5 gives a + b = 10, and 2ab/(a + b) = 21/5 gives 2ab/10 = 21/5, i.e. ab = 21. '
       'The numbers are the roots of t² − 10t + 21 = 0, i.e. (t − 7)(t − 3) = 0, giving 7 and 3.', 165),
    bq(U, REV, 'REV4', '9', 'If the G.M. and H.M. between two numbers are 15 and 5 10/13 respectively, find the numbers.',
       '3 and 75',
       'Let the numbers be a and b. Then ab = 15² = 225 and 2ab/(a + b) = 75/13 gives 450/(a + b) = 75/13, so a + b = 78. '
       'The numbers are the roots of t² − 78t + 225 = 0, i.e. (t − 75)(t − 3) = 0, giving 75 and 3.', 165),
    bq(U, REV, 'REV4', '10', 'The second term of an H.P. is 1/2 and the fifth term is −1/4. Find the 12th term.',
       'T<sub>12</sub> = −1/18',
       'For the corresponding A.P. the 2nd term is 2 and the 5th term is −4, so 3d = −6 and d = −2, giving a = 2 − (−2) = 4. '
       'Then a<sub>12</sub> = 4 + 11(−2) = −18, so the 12th term of the H.P. is −1/18. '
       '(The printed key labels this answer 11 instead of 10.)', 165),
]

# === End of Unit 4 ===
