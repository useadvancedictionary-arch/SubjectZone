"""Unit 6 - Permutation, Combination and Probability (book pp. 179-213, PDF pp. 183-217)."""
from .common import bq, mcq

U = 6
EX1 = 'Exercise 6.1'
EX2 = 'Exercise 6.2'
EX3 = 'Exercise 6.3'
EX4 = 'Exercise 6.4'
RE6 = 'Review Exercise 6'


def P(n, r):
    """nPr in textbook notation."""
    return f'<sup>{n}</sup>P<sub>{r}</sub>'


def C(n, r):
    """nCr in textbook notation."""
    return f'<sup>{n}</sup>C<sub>{r}</sub>'


ITEMS = []

# ============================================================== Exercise 6.1 (pdf 184)
ITEMS += [
    bq(U, EX1, 'EX6.1', '1(i)', 'Evaluate: 4!', '24',
       '4! = 4 × 3 × 2 × 1 = 24.', 184),
    bq(U, EX1, 'EX6.1', '1(ii)', 'Evaluate: 6!', '720',
       '6! = 6 × 5 × 4 × 3 × 2 × 1 = 720.', 184),
    bq(U, EX1, 'EX6.1', '1(iii)', 'Evaluate: 8! / 5!', '336',
       '8!/5! = (8 × 7 × 6 × 5!)/5! = 8 × 7 × 6 = 336.', 184),
    bq(U, EX1, 'EX6.1', '1(iv)', 'Evaluate: 10! / 7!', '720',
       '10!/7! = (10 × 9 × 8 × 7!)/7! = 10 × 9 × 8 = 720.', 184),
    bq(U, EX1, 'EX6.1', '1(v)', 'Evaluate: 5! × 7! × 3!', '3,628,800',
       '5! = 120, 7! = 5040, 3! = 6. Product = 120 × 5040 × 6 = 3,628,800.', 184),
    bq(U, EX1, 'EX6.1', '1(vi)', 'Evaluate: 10! ÷ 8! + 5!', '210',
       '10! ÷ 8! = 10 × 9 = 90 and 5! = 120, so the value is 90 + 120 = 210.', 184),
    bq(U, EX1, 'EX6.1', '1(vii)', 'Evaluate: 16! / (8! 12!)', '13/12',
       'Write 16! = 16 × 15 × 14 × 13 × 12!, so 16!/(8! 12!) = (16 × 15 × 14 × 13)/8! '
       '= 43,680/40,320 = 13/12.', 184),
    bq(U, EX1, 'EX6.1', '1(viii)', 'Evaluate: (9!)² / ((5!)³ × 7!)', '378/25 (= 15.12)',
       '(9!)²/7! = 9! × (9!/7!) = 362,880 × 72 = 26,127,360 and (5!)³ = 120³ = 1,728,000. '
       'Hence the value is 26,127,360/1,728,000 = 15.12 = 378/25.', 184),
    bq(U, EX1, 'EX6.1', '1(ix)', 'Evaluate: 9! / (2! × (9 − 2)!)', '36',
       '9!/(2! × 7!) = (9 × 8 × 7!)/(2 × 7!) = 72/2 = 36.', 184),

    bq(U, EX1, 'EX6.1', '2(i)', 'Write in factorial form: 6 · 5 · 4', '6!/3!',
       '6! = 6 × 5 × 4 × 3!, therefore 6 × 5 × 4 = 6!/3!.', 184),
    bq(U, EX1, 'EX6.1', '2(ii)', 'Write in factorial form: 12 · 11 · 10', '12!/9!',
       '12! = 12 × 11 × 10 × 9!, therefore 12 × 11 × 10 = 12!/9!.', 184),
    bq(U, EX1, 'EX6.1', '2(iii)', 'Write in factorial form: n(n + 1)(n + 2)/(6 · 5)',
       '(n + 2)! · 4! / ((n − 1)! · 6!) = (n + 2)!/(30(n − 1)!)',
       'n(n + 1)(n + 2) = (n + 2)!/(n − 1)! and 6 · 5 = 6!/4!. Hence the expression equals '
       '[(n + 2)!/(n − 1)!] ÷ (6!/4!) = (n + 2)! · 4!/((n − 1)! · 6!) = (n + 2)!/(30(n − 1)!).', 184),
    bq(U, EX1, 'EX6.1', '2(iv)', 'Write in factorial form: 20 · 19 · 18 · 17', '20!/16!',
       '20! = 20 × 19 × 18 × 17 × 16!, so 20 × 19 × 18 × 17 = 20!/16!.', 184),

    bq(U, EX1, 'EX6.1', '3(i)', 'Express as a single fraction: (n + 1)!/(r + 1)! + n!/r!',
       'n!(n + r + 2)/(r + 1)!',
       'Write n!/r! = n!(r + 1)/(r + 1)!. Then (n + 1)!/(r + 1)! + n!(r + 1)/(r + 1)! '
       '= [(n + 1)! + n!(r + 1)]/(r + 1)! = n![(n + 1) + (r + 1)]/(r + 1)! = n!(n + r + 2)/(r + 1)!.', 184),
    bq(U, EX1, 'EX6.1', '3(ii)', 'Express as a single fraction: (n + 1)!/r! + n!/(r + 1)!',
       'n!(nr + n + r + 2)/(r + 1)!',
       'Take (r + 1)! as denominator: (n + 1)!/r! = (n + 1)!(r + 1)/(r + 1)! and n!/(r + 1)! stays as it is. '
       'Sum = [(n + 1)!(r + 1) + n!]/(r + 1)! = n![(n + 1)(r + 1) + 1]/(r + 1)! '
       '= n![nr + n + r + 1 + 1]/(r + 1)! = n!(nr + n + r + 2)/(r + 1)!.', 184),
]

# ============================================================== Exercise 6.2 (pdf 195-196)
ITEMS += [
    bq(U, EX2, 'EX6.2', '1(i)', f'Evaluate: {P(20, 3)}', '6840',
       f'{P(20, 3)} = 20 × 19 × 18 = 6840.', 195),
    bq(U, EX2, 'EX6.2', '1(ii)', f'Evaluate: {P(16, 4)}', '43,680',
       f'{P(16, 4)} = 16 × 15 × 14 × 13 = 43,680.', 195),
    bq(U, EX2, 'EX6.2', '1(iii)', f'Evaluate: {P(12, 5)}', '95,040',
       f'{P(12, 5)} = 12 × 11 × 10 × 9 × 8 = 95,040.', 195),
    bq(U, EX2, 'EX6.2', '1(iv)', 'Evaluate the coefficient (8; 3, 2) = 8!/(3! × 2!).', '3360',
       'This coefficient counts the arrangements of 8 objects when 3 are alike of one kind and 2 are alike '
       'of another: 8!/(3! 2!) = 40,320/(6 × 2) = 40,320/12 = 3360.', 195),
    bq(U, EX2, 'EX6.2', '1(v)', 'Evaluate the coefficient (9; 2, 3, 4) = 9!/(2! × 3! × 4!).', '1260',
       '9!/(2! 3! 4!) = 362,880/(2 × 6 × 24) = 362,880/288 = 1260.', 195),

    bq(U, EX2, 'EX6.2', '2(i)', f'Find the value of n: {P("n", 2)} = 30', 'n = 6',
       'n(n − 1) = 30, i.e. n² − n − 30 = 0, so (n − 6)(n + 5) = 0. Since n must be positive, n = 6 '
       '(6 × 5 = 30).', 195),
    bq(U, EX2, 'EX6.2', '2(ii)', f'Find the value of n: {P("n", 3)} = 60', 'n = 5',
       'n(n − 1)(n − 2) = 60 = 5 × 4 × 3, so n = 5.', 195),
    bq(U, EX2, 'EX6.2', '2(iii)', f'Find the value of n: {P(8, "n")} = 8 · 7 · 6', 'n = 3',
       '8!/(8 − n)! = 8 × 7 × 6 = 8!/5!, hence (8 − n)! = 5! and 8 − n = 5, giving n = 3.', 195),
    bq(U, EX2, 'EX6.2', '2(iv)', f'Find the value of n: {P(11, "n")} = 11 · 10 · 9', 'n = 3',
       '11!/(11 − n)! = 11 × 10 × 9 = 11!/8!, hence 11 − n = 8, so n = 3.', 195),
    bq(U, EX2, 'EX6.2', '2(v)', f'Find the value of n: {P("n+2", 4)} : {P("n+1", 3)} = 5 : 1', 'n = 3',
       f'{P("n+2", 4)} = (n + 2)!/(n − 2)! and {P("n+1", 3)} = (n + 1)!/(n − 2)!. Their ratio is '
       '(n + 2)!/(n + 1)! = n + 2 = 5, so n = 3.', 195),
    bq(U, EX2, 'EX6.2', '2(vi)', f'Find the value of n: {P("n", 4)} : {P("n−1", 3)} = 9 : 1', 'n = 9',
       f'{P("n", 4)} = n!/(n − 4)! and {P("n−1", 3)} = (n − 1)!/(n − 4)!. Their ratio is '
       'n!/(n − 1)! = n = 9, so n = 9.', 195),

    bq(U, EX2, 'EX6.2', '3', 'In how many ways are different batting orders possible for a cricket team '
       'consisting of 11 players?', '39,916,800 ways',
       'A batting order uses all 11 players in a definite order: 11! = 11 × 10 × 9 × ... × 2 × 1 = 39,916,800.', 195),
    bq(U, EX2, 'EX6.2', '4', 'In how many ways can two English books, three Chemistry books and four Physics '
       'books be arranged on a shelf so that all the books of the same subject are together?', '1728 ways',
       'Treat the three subjects as three blocks: they can be placed on the shelf in 3! = 6 ways. Within the '
       'blocks the books can be arranged in 2! = 2, 3! = 6 and 4! = 24 ways. Total = 3! × 2! × 3! × 4! '
       '= 6 × 2 × 6 × 24 = 1728.', 195),
    bq(U, EX2, 'EX6.2', '5', 'How many different arrangements can be formed of the word "MATRIX" using all '
       'its letters? Also find the number of arrangements if each of them starts with "R".',
       '720 arrangements in all; 120 of them start with R.',
       'MATRIX has 6 distinct letters, so the number of arrangements is 6! = 720. If the word must begin with '
       'R, the remaining 5 letters (M, A, T, I, X) are arranged in 5! = 120 ways.', 195),
    bq(U, EX2, 'EX6.2', '6', 'How many signals can be given by 8 flags of different colours when 5 of them '
       'are used at a time?', '6720 signals',
       f'A signal is fixed by choosing and ordering 5 of the 8 flags: {P(8, 5)} = 8 × 7 × 6 × 5 × 4 = 6720.', 195),
    bq(U, EX2, 'EX6.2', '7', 'A fair coin is tossed three times. How many outcomes are possible? Find by the '
       'fundamental principle and illustrate using a tree diagram.',
       '2 × 2 × 2 = 8 outcomes: HHH, HHT, HTH, HTT, THH, THT, TTH, TTT.',
       'By the fundamental principle each toss has 2 possible results, so the three tosses together have '
       '2 × 2 × 2 = 8 ordered outcomes. Tree diagram: the first toss gives the branches H and T; from each of '
       'these the second toss again gives H and T; from each of those the third toss gives H and T once more. '
       'The 8 end branches, read from top to bottom, are HHH, HHT, HTH, HTT, THH, THT, TTH, TTT.', 195),

    bq(U, EX2, 'EX6.2', '8(i)', 'How many 5-digit numbers can be formed from the digits 5, 6, 7, 8, 9 without '
       'repeating any digit?', '120 numbers', 'All five digits are used once each: 5! = 120 (none of the digits '
       'is 0, so every arrangement is a genuine 5-digit number).', 195),
    bq(U, EX2, 'EX6.2', '8(ii)', 'How many 5-digit numbers can be formed from the digits 1, 2, 3, 5, 7, 9 '
       'without repeating any digit?', '720 numbers',
       f'Choose and order 5 of the 6 digits: {P(6, 5)} = 6 × 5 × 4 × 3 × 2 = 720.', 195),
    bq(U, EX2, 'EX6.2', '8(iii)', 'How many 5-digit numbers can be formed from the digits 2, 4, 6, 8, 0 '
       'without repeating any digit?', '96 numbers',
       'The first digit cannot be 0, so it has 4 choices (2, 4, 6, 8). The remaining four places take the '
       'other four digits in 4! = 24 ways. Total = 4 × 24 = 96.', 195),

    bq(U, EX2, 'EX6.2', '9(i)', f'Prove that: {P("n", "r")} = {P("n−1", "r")} + r · {P("n−1", "r−1")}',
       'Proved.',
       f'Take the right-hand side with {P("n−1", "r")} = (n − 1)!/(n − r − 1)! and '
       f'{P("n−1", "r−1")} = (n − 1)!/(n − r)!. Then<br>'
       'RHS = (n − 1)!/(n − r − 1)! + r(n − 1)!/(n − r)!<br>'
       '= (n − 1)![(n − r) + r]/(n − r)!  (common denominator (n − r)!)<br>'
       '= n(n − 1)!/(n − r)! = n!/(n − r)! = ' + P('n', 'r') + ' = LHS.', 195),
    bq(U, EX2, 'EX6.2', '9(ii)', f'Prove that: {P("n", "r")} = n · {P("n−1", "r−1")}', 'Proved.',
       f'n · {P("n−1", "r−1")} = n × (n − 1)!/[(n − 1) − (r − 1)]! = n(n − 1)!/(n − r)! = n!/(n − r)! '
       f'= {P("n", "r")}.', 195),

    bq(U, EX2, 'EX6.2', '10(i)', 'How many arrangements can be formed using all the letters of the word '
       'STATISTICS?', '50,400',
       'STATISTICS has 10 letters with S three times, T three times, I twice and A, C once each. Number of '
       'arrangements = 10!/(3! 3! 2!) = 3,628,800/72 = 50,400.', 195),
    bq(U, EX2, 'EX6.2', '10(ii)', 'How many arrangements can be formed using all the letters of the word PLANE?',
       '120', 'PLANE has 5 different letters, so 5! = 120 arrangements.', 195),
    bq(U, EX2, 'EX6.2', '10(iii)', 'How many arrangements can be formed using all the letters of the word OBJECT?',
       '720', 'OBJECT has 6 different letters, so 6! = 720 arrangements.', 195),
    bq(U, EX2, 'EX6.2', '10(iv)', 'How many arrangements can be formed using all the letters of the word FASTENS?',
       '2520', 'FASTENS has 7 letters in which S occurs twice: 7!/2! = 5040/2 = 2520.', 195),
    bq(U, EX2, 'EX6.2', '10(v)', 'How many arrangements can be formed using all the letters of the word '
       'MATHEMATICS?', '4,989,600',
       'MATHEMATICS has 11 letters with M, A and T each occurring twice: 11!/(2! 2! 2!) = 39,916,800/8 '
       '= 4,989,600.', 195),
    bq(U, EX2, 'EX6.2', '10(vi)', 'How many arrangements can be formed using all the letters of the word '
       'ASSISTANCE?', '302,400',
       'ASSISTANCE has 10 letters with A twice and S three times: 10!/(2! 3!) = 3,628,800/12 = 302,400.', 195),

    bq(U, EX2, 'EX6.2', '11', 'How many 8-digit numbers can be formed from the digits 2, 2, 2, 3, 3, 3, 5, 6? '
       'How many among these are greater than 60,000,000?', '1120 numbers; 140 of them exceed 60,000,000.',
       'The 8 digits contain 2 three times and 3 three times, so the count is 8!/(3! 3!) = 40,320/36 = 1120. '
       'For a number greater than 60,000,000 the first digit must be 6 (the only digit not smaller than 6); the '
       'remaining 7 places hold 2, 2, 2, 3, 3, 3, 5, giving 7!/(3! 3!) = 5040/36 = 140 numbers.', 195),
    bq(U, EX2, 'EX6.2', '12', 'How many distinct permutations of the letters of the word "ESSENTIAL" are possible?',
       '90,720',
       'ESSENTIAL has 9 letters with E twice and S twice: 9!/(2! 2!) = 362,880/4 = 90,720.', 195),
    bq(U, EX2, 'EX6.2', '12(i)', 'How many distinct permutations of the letters of the word "ESSENTIAL" have the '
       'two S\'s together?', '20,160',
       'Tie the two S\'s into one block SS. The 8 objects (SS, E, E, N, T, I, A, L) contain E twice, so they '
       'can be arranged in 8!/2! = 40,320/2 = 20,160 ways.', 195),
    bq(U, EX2, 'EX6.2', '12(ii)', 'How many distinct permutations of the letters of the word "ESSENTIAL" have the '
       'two S\'s separate?', '70,560',
       'Separate = all permutations − permutations with the S\'s together = 90,720 − 20,160 = 70,560.', 195),
    bq(U, EX2, 'EX6.2', '13', 'In how many ways can 8 persons be seated around a round table?', '5040 ways',
       'Around a circle only the relative order matters, so fix one person and arrange the other 7: '
       '(8 − 1)! = 7! = 5040.', 195),
    bq(U, EX2, 'EX6.2', '14', 'In how many ways can 7 keys be arranged in a circular key ring?', '360 ways',
       '7 keys in a circle can be arranged in (7 − 1)! = 6! = 720 ways, but a key ring can be turned over, so '
       'clockwise and anticlockwise orders are the same: 720/2 = 360.', 195),
    bq(U, EX2, 'EX6.2', '15', 'How many 3-digit numbers can be formed by using each one of the digits '
       '2, 3, 5, 7, 9 only once?', '60 numbers',
       f'Choose and order 3 of the 5 digits: {P(5, 3)} = 5 × 4 × 3 = 60.', 195),

    bq(U, EX2, 'EX6.2', '16', 'How many numbers greater than 23,000 can be formed from the digits 1, 2, 3, 5, 6 '
       'if digits may repeat?', '2250 numbers',
       'Only 5-digit numbers are meant. (a) First digit 3, 5 or 6: 3 × 5⁴ = 1875 numbers. (b) First digit 2 and '
       'second digit 5 or 6: 2 × 5³ = 250 numbers. (c) First digit 2 and second digit 3: the last three places '
       'are free, 5³ = 125 numbers (all exceed 23,000 because 0 is not available). Total = 1875 + 250 + 125 '
       '= 2250. Note: the printed key gives 1500, which does not match any consistent count for this question.', 196),
    bq(U, EX2, 'EX6.2', '17(i)', 'Find the number of 5-digit numbers that can be formed from the digits '
       '1, 2, 4, 6, 8 (no digit repeated) in which the digits 2 and 8 are next to each other.', '48 numbers',
       'Tie 2 and 8 into one block: the block and the other three digits give 4! = 24 arrangements, and the '
       'block itself can be written 28 or 82 (2 ways). Total = 24 × 2 = 48.', 196),
    bq(U, EX2, 'EX6.2', '17(ii)', 'Find the number of 5-digit numbers that can be formed from the digits '
       '1, 2, 4, 6, 8 (no digit repeated) in which the digits 2 and 8 are not next to each other.', '72 numbers',
       'All 5-digit numbers = 5! = 120; those with 2 and 8 together = 48. Hence 120 − 48 = 72.', 196),
    bq(U, EX2, 'EX6.2', '18', 'How many 6-digit numbers can be formed without repeating any digit from the '
       'digits 0, 1, 2, 3, 4, 5? In how many of them will 0 be at the tens place?', '600 numbers; in 120 of them.',
       'The first (lakh) digit cannot be 0: 5 choices; the remaining five places take the other five digits in '
       '5! = 120 ways, so 5 × 120 = 600. With 0 fixed at the tens place the first digit again has 5 choices and '
       'the other four places are filled by the remaining four digits in 4! = 24 ways: 5 × 24 = 120.', 196),
    bq(U, EX2, 'EX6.2', '19', 'How many 5-digit multiples of 5 can be formed from the digits 2, 3, 5, 7, 9 when '
       'digits may repeat?', '625',
       'A multiple of 5 must end in 5 (the only digit of the set divisible by 5). With 5 fixed in the units '
       'place, each of the other four places can be any of the five digits, and repetition is allowed, '
       'so the count is 5⁴ = 625. The printed key gives 256 = 4⁴, which incorrectly forbids using 5 again '
       'in the other four places even though the question says digits may repeat.', 196),
]

# ============================================================== Exercise 6.3 (pdf 201-202)
ITEMS += [
    bq(U, EX3, 'EX6.3', '1(i)', f'Evaluate: {C(12, 10)}', '66',
       f'{C(12, 10)} = {C(12, 2)} = (12 × 11)/(2 × 1) = 66.', 201),
    bq(U, EX3, 'EX6.3', '1(ii)', f'Evaluate: {C(12, 3)}', '220',
       f'{C(12, 3)} = (12 × 11 × 10)/(3 × 2 × 1) = 1320/6 = 220.', 201),
    bq(U, EX3, 'EX6.3', '1(iii)', f'Evaluate: {C(20, 17)}', '1140',
       f'{C(20, 17)} = {C(20, 3)} = (20 × 19 × 18)/(3 × 2 × 1) = 6840/6 = 1140.', 201),
    bq(U, EX3, 'EX6.3', '1(iv)', f'Evaluate the binomial coefficient "7 over 4", i.e. {C(7, 4)}.', '35',
       '7C4 = 7!/(4! 3!) = (7 × 6 × 5)/(3 × 2 × 1) = 210/6 = 35.', 201),

    bq(U, EX3, 'EX6.3', '2(i)', f'Find the value of n when: {C("n", 2)} = 21', 'n = 7',
       'n(n − 1)/2 = 21 → n² − n − 42 = 0 → (n − 7)(n + 6) = 0. As n is positive, n = 7.', 201),
    bq(U, EX3, 'EX6.3', '2(ii)', f'Find the value of n when: {C("n", 3)} = 4', 'n = 4',
       'n(n − 1)(n − 2)/6 = 4 → n(n − 1)(n − 2) = 24 = 4 × 3 × 2, so n = 4.', 201),
    bq(U, EX3, 'EX6.3', '2(iii)', f'Find the value of n when: {C("n", 12)} = {C("n", 6)}', 'n = 18',
       'nCr = nCs with r ≠ s implies r + s = n. Hence n = 12 + 6 = 18.', 201),
    bq(U, EX3, 'EX6.3', '2(iv)', f'Find the value of n when: {C("n", 15)} = (17 × 16)/2!', 'n = 17',
       f'(17 × 16)/2! = 136 and 136 = {C(17, 15)} = {C(17, 2)}, so n = 17.', 201),
    bq(U, EX3, 'EX6.3', '2(v)', f'Find the value of n when: {C("n", 5)} = {C("n", 4)}', 'n = 9',
       'nC5 = nC4 gives 5 + 4 = n, i.e. n = 9.', 201),
    bq(U, EX3, 'EX6.3', '2(vi)', f'Find the value of n when: {C("n", 10)} = (12 × 11)/2!', 'n = 12',
       f'(12 × 11)/2! = 66 = {C(12, 10)} = {C(12, 2)}, hence n = 12.', 201),

    bq(U, EX3, 'EX6.3', '3(i)', f'Find n and r when {P("n", "r")} = 210 and {C("n", "r")} = 35.',
       'n = 7, r = 3',
       f'{P("n", "r")}/{C("n", "r")} = r!, so r! = 210/35 = 6 and r = 3. Then {P("n", 3)} = n(n − 1)(n − 2) '
       '= 210 = 7 × 6 × 5, giving n = 7.', 201),
    bq(U, EX3, 'EX6.3', '3(ii)',
       f'Find n and r when {C("n−1", "r−1")} : {C("n", "r")} : {C("n+1", "r+1")} = 3 : 6 : 11.',
       'n = 10, r = 5',
       f'{C("n−1", "r−1")}/{C("n", "r")} = r/n = 3/6 = 1/2, so n = 2r.<br>'
       f'{C("n", "r")}/{C("n+1", "r+1")} = (r + 1)/(n + 1) = 6/11, so 11(r + 1) = 6(n + 1).<br>'
       'Substituting n = 2r: 11r + 11 = 12r + 6 → r = 5, hence n = 10.', 201),

    bq(U, EX3, 'EX6.3', '4(i)', f'If {C(12, "r")} = {C(12, "r+4")}, find {C(6, "r")}.', f'r = 4 and {C(6, 4)} = 15',
       'From nCr = nCs with r ≠ s we get r + (r + 4) = 12, so 2r = 8 and r = 4. Then 6C4 = 6!/(4! 2!) '
       '= (6 × 5)/2 = 15.', 201),
    bq(U, EX3, 'EX6.3', '4(ii)', f'If {C("n", 12)} = {C("n", 10)}, find {C(25, "n")}.',
       'n = 22 and 25C22 = 2300',
       'nC12 = nC10 gives n = 12 + 10 = 22. Then 25C22 = 25C3 = (25 × 24 × 23)/(3 × 2 × 1) = 13,800/6 = 2300.', 201),

    bq(U, EX3, 'EX6.3', '5(i)', 'The members of a club are 12 boys and 8 girls. In how many ways can a committee '
       'of 5 members be formed?', '15,504 ways',
       'There are 20 members in all; choose any 5: 20C5 = 20!/(5! 15!) = 15,504.', 201),
    bq(U, EX3, 'EX6.3', '5(ii)', 'The members of a club are 12 boys and 8 girls. In how many ways can a committee '
       'of 4 boys and 3 girls be formed?', '27,720 ways',
       'Choose 4 of the 12 boys and 3 of the 8 girls: 12C4 × 8C3 = 495 × 56 = 27,720.', 201),

    bq(U, EX3, 'EX6.3', '6', 'A box contains 7 red balls and 6 black balls. In how many ways can 5 balls be '
       'selected such that exactly 3 are red?', '525 ways',
       'Choose 3 of the 7 red balls and the remaining 2 from the 6 black balls: 7C3 × 6C2 = 35 × 15 = 525.', 201),

    bq(U, EX3, 'EX6.3', '7(i)', 'How many (a) diagonals and (b) triangles can be drawn in a plane by joining the '
       'vertices of a polygon having 6 sides?', '(a) 9 diagonals; (b) 20 triangles',
       'A hexagon has 6 vertices. Every pair of vertices gives a segment: 6C2 = 15, of which 6 are sides and the '
       'rest diagonals, so diagonals = 15 − 6 = 9. Every set of 3 vertices gives one triangle: 6C3 = 20.', 201),
    bq(U, EX3, 'EX6.3', '7(ii)', 'How many (a) diagonals and (b) triangles can be drawn in a plane by joining the '
       'vertices of a polygon having 8 sides?', '(a) 20 diagonals; (b) 56 triangles',
       'An octagon has 8 vertices. Diagonals = 8C2 − 8 = 28 − 8 = 20. Triangles = 8C3 = 8!/(3! 5!) '
       '= (8 × 7 × 6)/6 = 56.', 201),
    bq(U, EX3, 'EX6.3', '7(iii)', 'How many (a) diagonals and (b) triangles can be drawn in a plane by joining the '
       'vertices of a polygon having 10 sides?', '(a) 35 diagonals; (b) 120 triangles',
       'A decagon has 10 vertices. Diagonals = 10C2 − 10 = 45 − 10 = 35. Triangles = 10C3 = (10 × 9 × 8)/6 = 120.', 201),

    bq(U, EX3, 'EX6.3', '8', f'Show that: {C(9, 6)} + {C(9, 5)} = {C(10, 6)}.', 'Proved: 84 + 126 = 210.',
       '9C6 = 9!/(6! 3!) = 84, 9C5 = 9!/(5! 4!) = 126 and 84 + 126 = 210. Also 10C6 = 10!/(6! 4!) = 210. '
       'The result is the Pascal identity nCr + nCr−1 = n+1Cr with n = 9, r = 6.', 201),

    bq(U, EX3, 'EX6.3', '9(i)', 'There are 11 men and 9 women members of a club. How many committees of 8 members '
       'can be formed, having exactly five men?', '38,808 committees',
       'Choose 5 of the 11 men and 3 of the 9 women: 11C5 × 9C3 = 462 × 84 = 38,808.', 202),
    bq(U, EX3, 'EX6.3', '9(ii)', 'There are 11 men and 9 women members of a club. How many committees of 8 members '
       'can be formed, having at most five women?', '120,945 committees',
       'At most five women means 0, 1, 2, 3, 4 or 5 women (and therefore 8, 7, 6, 5, 4 or 3 men):<br>'
       '9C0·11C8 + 9C1·11C7 + 9C2·11C6 + 9C3·11C5 + 9C4·11C4 + 9C5·11C3<br>'
       '= 165 + 2970 + 16,632 + 38,808 + 41,580 + 20,790 = 120,945.<br>'
       '(Check: 20C8 − [9C6·11C2 + 9C7·11C1 + 9C8·11C0] = 125,970 − [4,620 + 396 + 9] = 120,945.) '
       'The printed key gives 120,780, which leaves out the committee of 8 men (0 women), 165.', 202),
    bq(U, EX3, 'EX6.3', '9(iii)', 'There are 11 men and 9 women members of a club. How many committees of 8 members '
       'can be formed, having at least five women?', '25,815 committees',
       'Take 5, 6, 7 or 8 women: 9C5·11C3 + 9C6·11C2 + 9C7·11C1 + 9C8·11C0 = 20,790 + 4,620 + 396 + 9 = 25,815.', 202),

    bq(U, EX3, 'EX6.3', '10', 'Find the number of combinations of the letters of the word "Question" taken 5 at a '
       'time.', '56 combinations',
       'The word Question has 8 different letters, so the number of 5-letter combinations is 8C5 = 8!/(5! 3!) '
       '= (8 × 7 × 6)/6 = 56.', 202),
    bq(U, EX3, 'EX6.3', '11', 'How many words can be formed by 3 vowels and 4 consonants out of 5 vowels and '
       '7 consonants?', '1,764,000 words',
       'Choose 3 of the 5 vowels and 4 of the 7 consonants, then arrange the 7 chosen letters: 5C3 × 7C4 × 7! '
       '= 10 × 35 × 5040 = 1,764,000.', 202),
]

# ============================================================== Exercise 6.4 (pdf 214-215)
ITEMS += [
    bq(U, EX4, 'EX6.4', '1(i)', 'Two fair coins are tossed. Find the probability of getting same faces.', '1/2',
       'S = {HH, HT, TH, TT}, n(S) = 4. Same faces: HH and TT, so 2 favourable outcomes and P = 2/4 = 1/2.', 214),
    bq(U, EX4, 'EX6.4', '1(ii)', 'Two fair coins are tossed. Find the probability of getting all heads.', '1/4',
       'Only HH is favourable among the 4 outcomes: P = 1/4.', 214),
    bq(U, EX4, 'EX6.4', '1(iii)', 'Two fair coins are tossed. Find the probability of getting at most one head.',
       '3/4',
       'At most one head means 0 or 1 head: TT, HT, TH give 3 favourable outcomes, so P = 3/4. '
       '(The printed key gives 1/2, which is P(exactly one head) = 2/4.)', 214),
    bq(U, EX4, 'EX6.4', '1(iv)', 'Two fair coins are tossed. Find the probability of getting at least two tails.',
       '1/4 (= 0.25)',
       'With two coins, at least two tails means both tails: TT only, so P = 1/4 = 0.25.', 214),
    bq(U, EX4, 'EX6.4', '1(v)', 'Two fair coins are tossed. Find the probability of getting at least one tail.',
       '3/4', 'At least one tail: HT, TH, TT (all except HH) → P = 3/4.', 214),

    bq(U, EX4, 'EX6.4', '2(i)', 'Two dice, one red and the other green, are rolled simultaneously. The numbers of '
       'dots on the tops are added. Find the probability of getting a sum of 8.', '5/36',
       'n(S) = 6 × 6 = 36. Sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) — 5 outcomes, so P = 5/36.', 214),
    bq(U, EX4, 'EX6.4', '2(ii)', 'Two dice, one red and the other green, are rolled simultaneously. The numbers of '
       'dots on the tops are added. Find the probability of getting a sum of 10.', '1/12',
       'Sum 10: (4,6), (5,5), (6,4) — 3 outcomes out of 36, so P = 3/36 = 1/12.', 214),
    bq(U, EX4, 'EX6.4', '2(iii)', 'Two dice, one red and the other green, are rolled simultaneously. The numbers of '
       'dots on the tops are added. Find the probability of getting a sum of 12.', '1/36',
       'Sum 12 is possible only as (6,6), so P = 1/36.', 214),

    bq(U, EX4, 'EX6.4', '3(i)', 'A bag contains 40 balls out of which 5 are green, 15 are red and the remaining are '
       'black. A ball is drawn out of the bag. Find the probability that the ball is green.', '1/8',
       'n(S) = 40 and there are 5 green balls, so P(green) = 5/40 = 1/8.', 214),
    bq(U, EX4, 'EX6.4', '3(ii)', 'A bag contains 40 balls out of which 5 are green, 15 are red and the remaining are '
       'black. A ball is drawn out of the bag. Find the probability that the ball is black.', '1/2',
       'Black balls = 40 − 5 − 15 = 20, so P(black) = 20/40 = 1/2.', 214),
    bq(U, EX4, 'EX6.4', '3(iii)', 'A bag contains 40 balls out of which 5 are green, 15 are red and the remaining '
       'are black. A ball is drawn out of the bag. Find the probability that the ball is not green.', '7/8',
       'Non-green balls = 40 − 5 = 35, so P(not green) = 35/40 = 7/8 (= 1 − 1/8).', 214),

    bq(U, EX4, 'EX6.4', '4(i)', 'A card is drawn from a well shuffled deck of cards. Find the probability of '
       'getting a King.', '1/13',
       'A deck has 52 cards and 4 Kings, so P(King) = 4/52 = 1/13.', 214),
    bq(U, EX4, 'EX6.4', '4(ii)', 'A card is drawn from a well shuffled deck of cards. Find the probability of '
       'getting a club.', '1/4',
       'There are 13 clubs, so P(club) = 13/52 = 1/4.', 214),
    bq(U, EX4, 'EX6.4', '4(iii)', 'A card is drawn from a well shuffled deck of cards. Find the probability of '
       'getting a face card.', '3/13',
       'Face cards are J, Q, K in four suits: 12 cards, so P(face card) = 12/52 = 3/13.', 214),

    bq(U, EX4, 'EX6.4', '5(i)', 'A die is rolled. Using a Venn diagram, find the probability of getting an even '
       'number.', '1/2',
       'S = {1,2,3,4,5,6}. Let A = {2,4,6} (even) and B = {5,6} (greater than 4). The Venn diagram shows '
       'A ∩ B = {6}, A ∪ B = {2,4,5,6} and 1, 3 outside. P(A) = 3/6 = 1/2.', 215),
    bq(U, EX4, 'EX6.4', '5(ii)', 'A die is rolled. Using a Venn diagram, find the probability of getting a number '
       'greater than 4.', '1/3',
       'With A = {2,4,6} and B = {5,6} in S = {1,...,6}, B has 2 outcomes, so P(B) = 2/6 = 1/3.', 215),
    bq(U, EX4, 'EX6.4', '5(iii)', 'A die is rolled. Using a Venn diagram, find the probability of getting a number '
       'which is even and greater than 4.', '1/6',
       'The overlapping part of the two sets is A ∩ B = {6}, a single outcome, so P = 1/6.', 215),

    bq(U, EX4, 'EX6.4', '6(i)', 'In a three child family, by using a tree diagram, find the probability of having '
       'three boys.', '1/8',
       'Each child is B or G, so the tree has 2 × 2 × 2 = 8 equally likely branches: BBB, BBG, BGB, BGG, GBB, '
       'GBG, GGB, GGG. Three boys is the single branch BBB, so P = 1/8.', 215),
    bq(U, EX4, 'EX6.4', '6(ii)', 'In a three child family, by using a tree diagram, find the probability of having '
       'exactly two boys.', '3/8',
       'Exactly two boys occurs for BBG, BGB, GBB — 3 of the 8 branches, so P = 3/8.', 215),
    bq(U, EX4, 'EX6.4', '6(iii)', 'In a three child family, by using a tree diagram, find the probability of having '
       'at least one girl.', '7/8',
       'All branches except BBB contain a girl: 7 out of 8, so P = 7/8.', 215),

    bq(U, EX4, 'EX6.4', '7(i)', 'In a single throw of two fair dice, find the probability that the product of the '
       'numbers on the dice is between 2 and 10 (both inclusive).', '1/2',
       'n(S) = 36. Favourable products: 2 → 2 ways, 3 → 2, 4 → 3, 5 → 2, 6 → 4, 8 → 2, 9 → 1, 10 → 2, total '
       '18 ways. P = 18/36 = 1/2.', 215),
    bq(U, EX4, 'EX6.4', '7(ii)', 'In a single throw of two fair dice, find the probability that the product of the '
       'numbers on the dice is divisible by 5.', '11/36',
       'Products divisible by 5: 5 (2 ways), 10 (2), 15 (2), 20 (2), 25 (1), 30 (2) — 11 ways in all, so '
       'P = 11/36.', 215),

    bq(U, EX4, 'EX6.4', '8(i)', 'A marble is drawn at random from a box containing 20 red, 10 white, 25 orange '
       'and 15 blue marbles. Find the probability that it is orange or red.', '9/14',
       'n(S) = 20 + 10 + 25 + 15 = 70. Orange or red = 25 + 20 = 45, so P = 45/70 = 9/14.', 215),
    bq(U, EX4, 'EX6.4', '8(ii)', 'A marble is drawn at random from a box containing 20 red, 10 white, 25 orange '
       'and 15 blue marbles. Find the probability that it is not blue or red.', '1/2',
       'Not blue and not red = white + orange = 10 + 25 = 35, so P = 35/70 = 1/2.', 215),
    bq(U, EX4, 'EX6.4', '8(iii)', 'A marble is drawn at random from a box containing 20 red, 10 white, 25 orange '
       'and 15 blue marbles. Find the probability that it is red, white or blue.', '9/14',
       'Red + white + blue = 20 + 10 + 15 = 45, so P = 45/70 = 9/14.', 215),

    bq(U, EX4, 'EX6.4', '9(i)', 'The king, queen and jack of clubs are removed from a deck of 52 playing cards and '
       'then shuffled. A card is drawn from the remaining cards. Find the probability of getting a heart.', '13/49',
       'Remaining cards = 52 − 3 = 49. All 13 hearts are still there, so P(heart) = 13/49.', 215),
    bq(U, EX4, 'EX6.4', '9(ii)', 'The king, queen and jack of clubs are removed from a deck of 52 playing cards and '
       'then shuffled. A card is drawn from the remaining cards. Find the probability of getting a queen.', '3/49',
       'The queen of clubs is gone, so 3 queens remain among 49 cards: P = 3/49.', 215),
    bq(U, EX4, 'EX6.4', '9(iii)', 'The king, queen and jack of clubs are removed from a deck of 52 playing cards '
       'and then shuffled. A card is drawn from the remaining cards. Find the probability of getting a club.',
       '10/49', 'Clubs left = 13 − 3 = 10, so P(club) = 10/49.', 215),
    bq(U, EX4, 'EX6.4', '9(iv)', 'The king, queen and jack of clubs are removed from a deck of 52 playing cards and '
       'then shuffled. A card is drawn from the remaining cards. Find the probability of getting a "9" of red '
       'colour.', '2/49',
       'There are two red 9s (hearts and diamonds), both still in the pack: P = 2/49.', 215),

    bq(U, EX4, 'EX6.4', '10(i)', 'A pair of fair dice is thrown. If the two numbers appearing are different, find '
       'the probability that the sum is 10.', '1/15',
       'Of the 36 ordered outcomes, 6 are doubles, so 30 outcomes have different numbers — this is the reduced '
       'sample space. Sum 10 with different numbers: (4,6) and (6,4), so P = 2/30 = 1/15. (The printed key gives '
       '1/18 = 2/36, which is P(sum 10 and different) without conditioning on the 30 outcomes.)', 215),
    bq(U, EX4, 'EX6.4', '10(ii)', 'A pair of fair dice is thrown. If the two numbers appearing are different, find '
       'the probability that the sum is six or less.', '2/5',
       'Among the 30 outcomes with different numbers, sums 2 to 6 occur 15 times, 3 of which are doubles '
       '((1,1), (2,2), (3,3)), leaving 12. Hence P = 12/30 = 2/5. (The printed key gives 1/3 = 12/36, the '
       'unconditional probability.)', 215),

    bq(U, EX4, 'EX6.4', '11(i)', 'Given that P(A) = 0.3, P(B) = 0.7, P(A ∩ B) = 0.21, find P(A/B).', '0.3',
       'P(A/B) = P(A ∩ B)/P(B) = 0.21/0.7 = 0.3.', 215),
    bq(U, EX4, 'EX6.4', '11(ii)', 'Given that P(A) = 0.3, P(B) = 0.7, P(A ∩ B) = 0.21, find P(B/A).', '0.7',
       'P(B/A) = P(A ∩ B)/P(A) = 0.21/0.3 = 0.7.', 215),

    bq(U, EX4, 'EX6.4', '12', 'If one card is selected at random from a deck of 52 playing cards, what is the '
       'probability that the card is a club or a face or both?', '11/26',
       'P(club) = 13/52, P(face) = 12/52 and P(club ∩ face) = 3/52. By the addition rule '
       'P = 13/52 + 12/52 − 3/52 = 22/52 = 11/26.', 215),
    bq(U, EX4, 'EX6.4', '13', 'From two events A and B, P(A) = 0.5, P(B) = 0.2, P(A ∪ B) = 0.4. Find P(A ∩ B).',
       '0.3', 'P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = 0.5 + 0.2 − 0.4 = 0.3.', 215),
    bq(U, EX4, 'EX6.4', '14', 'A natural number is chosen out of the first 35 natural numbers. What is the '
       'probability that the chosen number is divisible by 8 or 9?', '7/35 = 1/5',
       'Multiples of 8 up to 35: 8, 16, 24, 32 (4 numbers). Multiples of 9: 9, 18, 27 (3 numbers). No number is a '
       'multiple of both (72 > 35), so 7 favourable numbers among 35: P = 7/35 = 1/5.', 215),
    bq(U, EX4, 'EX6.4', '15', 'A bag contains 15 black, 25 red and 10 white balls. A ball is drawn at random. '
       'Find the probability that it is either red or white.', '7/10',
       'Total = 50, red or white = 25 + 10 = 35, so P = 35/50 = 7/10.', 215),
    bq(U, EX4, 'EX6.4', '16', 'Two events A and B are such that P(A) = 1/4, P(A/B) = 1/2, P(B/A) = 2/3. Find '
       'P(A ∩ B) and P(B).', 'P(A ∩ B) = 1/6, P(B) = 1/3',
       'P(A ∩ B) = P(B/A) · P(A) = (2/3)(1/4) = 1/6. Then P(B) = P(A ∩ B)/P(A/B) = (1/6)/(1/2) = 1/3.', 215),
    bq(U, EX4, 'EX6.4', '17', 'A fair die is thrown twice. Find the probability that an even number of dots appears '
       'in the first throw and the number of dots in the second throw is less than 4.', '1/4',
       'The throws are independent: P(even) = 3/6 = 1/2 and P(less than 4) = 3/6 = 1/2. Required probability '
       '= 1/2 × 1/2 = 1/4.', 215),
    bq(U, EX4, 'EX6.4', '18', 'Three missiles are fired at a target. If the probabilities of hitting the target are '
       '0.5, 0.3 and 0.6 respectively, and the missiles are fired independently, what is the probability that all '
       'the missiles hit the target?', '0.09',
       'For independent events multiply the probabilities: 0.5 × 0.3 × 0.6 = 0.09.', 215),
]

# ============================================================== Review Exercise 6 (pdf 216-217)
ITEMS += [
    mcq(U, RE6, 'REV6', 'i', 'If n = 0, then (n + 1)!/n! = ______.',
        ['0', '1', 'n', '∞'], 'b',
        '(0 + 1)!/0! = 1!/0! = 1/1 = 1.', 216),
    mcq(U, RE6, 'REV6', 'ii', 'Probability of getting 7 in throwing a dice is:',
        ['0', '1', '−1', 'Not defined'], 'a',
        'A die shows only 1 to 6, so getting 7 is an impossible event and P = 0/6 = 0.', 216),
    mcq(U, RE6, 'REV6', 'iii', 'The factorial form of 12 · 11 · 10 is:',
        ['12!/9!', '12!', '(12/9)!', '(12!) · (9!)'], 'a',
        '12 · 11 · 10 = 12 · 11 · 10 · 9!/9! = 12!/9!.', 216),
    mcq(U, RE6, 'REV6', 'iv', 'If two independent events A and B occur in p and q ways respectively, then the '
        'number of ways that both events can occur is:',
        ['p + q ways', 'p·q ways', '(pq)ʳ ways', 'rp + qr ways'], 'b',
        'By the fundamental (product) principle the two operations together can be performed in p × q ways.', 216),
    mcq(U, RE6, 'REV6', 'v', 'An arrangement of n objects according to some definite order is called:',
        ['Combination', 'Permutation', 'Factorial', 'none of these'], 'b',
        'A permutation is an arrangement in which order matters.', 216),
    mcq(U, RE6, 'REV6', 'vi', 'An arrangement of n objects without any order is called:',
        ['Combination', 'Permutation', 'Factorial', 'none of these'], 'a',
        'A combination is a selection in which the order of the objects is not considered.', 216),
    mcq(U, RE6, 'REV6', 'vii', 'The number of permutations of the letters of the word COMMITTEE is:',
        ['(9; 2, 2, 2)', '(6; 1, 2, 2)', '(9; 2, 2, 1)', '(9; 2, 3, 1)'], 'a',
        'COMMITTEE has 9 letters in which M, T and E each occur twice, so the number is 9!/(2! 2! 2!), i.e. the '
        'coefficient (9; 2, 2, 2) = 45,360.', 216),
    mcq(U, RE6, 'REV6', 'viii', '8 · 7 · 6 is equal to:',
        [P(8, 3), C(8, 3), P(8, 5), C(8, 5)], 'a',
        f'{P(8, 3)} = 8!/(8 − 3)! = 8 × 7 × 6 = 336, whereas {C(8, 3)} = 56.', 216),
    mcq(U, RE6, 'REV6', 'ix', f'If r = n, then {P("n", "r")} is equal to:',
        ['r!', '(n − r)!', '1', '0'], 'a',
        f'{P("n", "n")} = n!/(n − n)! = n!/0! = n! = r!. The printed key gives (c) 1, which is the value of '
        f'{C("n", "n")}, not of {P("n", "n")}.', 216),
    mcq(U, RE6, 'REV6', 'x', 'The number of ways that a necklace of n beads of different colours be made is:',
        ['(n − 1)!', 'n!/2', '(n! − 1)/2', '(n − 1)!/2'], 'd',
        'n beads in a circle give (n − 1)! arrangements; a necklace may be turned over, so clockwise and '
        'anticlockwise orders coincide and the count is (n − 1)!/2.', 216),
    mcq(U, RE6, 'REV6', 'xi', 'Any subset of a sample space is called:',
        ['Sample space', 'an event', 'a Trial', 'Random variable'], 'b',
        'An event is defined as any subset of the sample space S.', 216),
    mcq(U, RE6, 'REV6', 'xii', 'For two events A and B, if A ∩ B = ∅, then events A and B are called:',
        ['Mutually exclusive', 'Not mutually exclusive', 'Overlapping', 'Dependent events'], 'a',
        'A ∩ B = ∅ means the events have no outcome in common, i.e. they are mutually exclusive.', 216),
    mcq(U, RE6, 'REV6', 'xiii', 'When a dice is rolled and a coin is tossed, all possible outcomes are:',
        ['6', '12', '18', '24'], 'b',
        'By the fundamental principle: 6 × 2 = 12 outcomes.', 216),
    mcq(U, RE6, 'REV6', 'xiv', 'If two events A and B have equal chance of occurrence, then the events are:',
        ['Equally likely', 'Not equally likely', 'Dependent', 'Not mutually exclusive'], 'a',
        'Events that have the same probability of occurrence are called equally likely events.', 217),
    mcq(U, RE6, 'REV6', 'xv', 'If E be an event of a sample space S, then:',
        ['P(E) = n(S)/n(E)', '0 ≤ P(E) ≤ 1', '0 < P(E) < 1', 'all of these'], 'b',
        'Probability always lies between 0 and 1 inclusive. Option (a) has the ratio inverted and (c) excludes the '
        'impossible and certain events, so neither is generally true.', 217),
    mcq(U, RE6, 'REV6', 'xvi', 'The probability of getting the tail in a single toss of a coin is:',
        ['1/3', '2/3', '1/2', '1/4'], 'c',
        'S = {H, T}; one favourable outcome out of two gives P(T) = 1/2.', 217),
    mcq(U, RE6, 'REV6', 'xvii', 'Three dice are rolled simultaneously, then n(S) is equal to:',
        ['36', '18', '216', '6'], 'c',
        'Each die has 6 outcomes, so n(S) = 6 × 6 × 6 = 216.', 217),
    mcq(U, RE6, 'REV6', 'xviii', 'Two teams A and B are playing a match, the probability that team A does not '
        'lose is:',
        ['1/3', '2/3', '1/2', '0'], 'c',
        'A match between two teams has two possible results, A wins or B wins. "A does not lose" means A wins, so '
        'the probability is 1/2.', 217),
    mcq(U, RE6, 'REV6', 'xix', f'If {C("n", 6)} = {C("n", 12)}, then n equals:',
        ['18', '12', '6', '20'], 'a',
        'nCr = nCs with r ≠ s gives r + s = n, so n = 6 + 12 = 18.', 217),

    bq(U, RE6, 'REV6', '2(i)', f'Evaluate: ({C(6, 3)} × {C(4, 3)}) / {C(10, 4)}', '8/21',
       '6C3 = 20, 4C3 = 4 and 10C4 = 210. Hence (20 × 4)/210 = 80/210 = 8/21.', 217),
    bq(U, RE6, 'REV6', '2(ii)', f'Evaluate: ({P(6, 3)} × {P(4, 3)}) / {P(10, 4)}', '4/7',
       '6P3 = 6 × 5 × 4 = 120, 4P3 = 4 × 3 × 2 = 24 and 10P4 = 10 × 9 × 8 × 7 = 5040. Hence '
       '(120 × 24)/5040 = 2880/5040 = 4/7.', 217),
    bq(U, RE6, 'REV6', '2(iii)', f'Evaluate: ∑<sub>r=1</sub><sup>3</sup> {C(3, "r")}', '7',
       f'{C(3, 1)} + {C(3, 2)} + {C(3, 3)} = 3 + 3 + 1 = 7.', 217),

    bq(U, RE6, 'REV6', '3', 'There are seven seats available in a compartment. In how many ways can seven persons '
       'be seated?', '5040 ways', 'The 7 persons occupy the 7 seats in order: 7! = 5040.', 217),
    bq(U, RE6, 'REV6', '4', 'A room has 3 lamps. From a collection of 10 light bulbs of which 6 are no good, a '
       'person selects 3 at random and puts them in the sockets. What is the probability that he will have light?',
       '5/6',
       'Only 4 bulbs are good. The room stays dark when all 3 chosen bulbs are from the 6 bad ones: '
       '6C3/10C3 = 20/120 = 1/6. Hence P(light) = 1 − 1/6 = 5/6.', 217),
    bq(U, RE6, 'REV6', '5', 'If two dice are thrown simultaneously, what is the probability of obtaining a sum of '
       '7 or a sum of 11?', '2/9',
       'n(S) = 36. Sum 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 outcomes; sum 11: (5,6), (6,5) = 2 '
       'outcomes. The events are mutually exclusive, so P = 6/36 + 2/36 = 8/36 = 2/9.', 217),
    bq(U, RE6, 'REV6', '6', 'A bag contains 8 white, 10 black and 12 red balls. 3 balls are drawn from the bag. '
       'What is the probability that the first ball is white, the second ball is black and the third ball is red, '
       'when every time the ball is replaced?', '8/225',
       'Total = 30 and the ball is replaced each time, so the draws are independent: '
       '(8/30) × (10/30) × (12/30) = 960/27,000 = 8/225.', 217),
    bq(U, RE6, 'REV6', '7', 'In how many ways can a football team of 11 players be selected out of 15 players? '
       'How many of them will include a particular player?', '1365 teams; 1001 include a particular player.',
       'C(15, 11) = C(15, 4) = 1365. If a particular player must be included, the remaining 10 are chosen from the '
       'other 14: C(14, 10) = C(14, 4) = 1001.', 217),
]
