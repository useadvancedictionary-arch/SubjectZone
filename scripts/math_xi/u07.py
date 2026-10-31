"""Unit 7 - Mathematical Induction and Binomial Theorem (book pp. 214-237, PDF pp. 218-241)."""
from .common import bq, mcq

U = 7
EX1 = 'Exercise 7.1'
EX2 = 'Exercise 7.2'
EX3 = 'Exercise 7.3'
REV = 'Review Exercise 7'

ITEMS = []

# ============================================================ Exercise 7.1 (pdf 222-223)
ITEMS += [
    bq(U, EX1, 'EX7.1', '1(i)',
       "Prove by mathematical induction for every positive integer n: 1 + 3 + 5 + … + (2n − 1) = n².",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 1 and RHS = 1² = 1, so P(1) is true. "
       "<b>Induction hypothesis</b>: assume P(k): 1 + 3 + 5 + … + (2k − 1) = k². "
       "<b>Induction step</b>: the next term is 2(k + 1) − 1 = 2k + 1, so the sum for n = k + 1 is "
       "k² + (2k + 1) = (k + 1)², which is exactly P(k + 1). "
       "<b>Conclusion</b>: P(1) is true and P(k) implies P(k + 1), so by the principle of mathematical induction P(n) is true for all n ∈ ℕ.",
       222),
    bq(U, EX1, 'EX7.1', '1(ii)',
       "Prove by mathematical induction for every positive integer n: 3 + 6 + 9 + … + 3n = (3/2)n(n + 1).",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 3 and RHS = (3/2)(1)(2) = 3, so P(1) is true. "
       "<b>Hypothesis</b>: 3 + 6 + … + 3k = (3/2)k(k + 1). "
       "<b>Step</b>: adding the next term 3(k + 1) gives (3/2)k(k + 1) + 3(k + 1) = (3/2)(k + 1)(k + 2) = (3/2)(k + 1)((k + 1) + 1), which is P(k + 1). "
       "<b>Conclusion</b>: by induction the statement holds for every positive integer n.",
       222),
    bq(U, EX1, 'EX7.1', '1(iii)',
       "Prove by mathematical induction for every positive integer n: 1 + 4 + 7 + … + (3n − 2) = n(3n − 1)/2.",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 1, RHS = 1(3 − 1)/2 = 1, so P(1) is true. "
       "<b>Hypothesis</b>: 1 + 4 + … + (3k − 2) = k(3k − 1)/2. "
       "<b>Step</b>: add 3(k + 1) − 2 = 3k + 1: k(3k − 1)/2 + (3k + 1) = (3k² − k + 6k + 2)/2 = (3k² + 5k + 2)/2 = (k + 1)(3k + 2)/2 = (k + 1)(3(k + 1) − 1)/2, which is P(k + 1). "
       "<b>Conclusion</b>: P(n) is true for all positive integers n.",
       222),
    bq(U, EX1, 'EX7.1', '1(iv)',
       "Prove by mathematical induction for every positive integer n: 1 + 1/2 + 1/4 + … + 1/2<sup>n−1</sup> = 2(1 − 1/2<sup>n</sup>).",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 1 and RHS = 2(1 − 1/2) = 1, so P(1) is true. "
       "<b>Hypothesis</b>: 1 + 1/2 + … + 1/2<sup>k−1</sup> = 2(1 − 2<sup>−k</sup>). "
       "<b>Step</b>: add the next term 1/2<sup>k</sup>: 2(1 − 2<sup>−k</sup>) + 2<sup>−k</sup> = 2 − 2·2<sup>−k</sup> + 2<sup>−k</sup> = 2 − 2<sup>−k</sup> = 2(1 − 2<sup>−(k+1)</sup>), which is P(k + 1). "
       "<b>Conclusion</b>: the formula holds for all n ∈ ℕ.",
       222),
    bq(U, EX1, 'EX7.1', '1(v)',
       "Prove by mathematical induction for every positive integer n: 2 + 6 + 18 + … + 2·3<sup>n−1</sup> = 3<sup>n</sup> − 1.",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 2 and RHS = 3<sup>1</sup> − 1 = 2, so P(1) is true. "
       "<b>Hypothesis</b>: 2 + 6 + … + 2·3<sup>k−1</sup> = 3<sup>k</sup> − 1. "
       "<b>Step</b>: the next term is 2·3<sup>k</sup>, so the sum becomes 3<sup>k</sup> − 1 + 2·3<sup>k</sup> = 3·3<sup>k</sup> − 1 = 3<sup>k+1</sup> − 1, which is P(k + 1). "
       "<b>Conclusion</b>: by induction P(n) is true for every positive integer n.",
       222),
    bq(U, EX1, 'EX7.1', '1(vi)',
       "Prove by mathematical induction for every positive integer n: 2 + 6 + 12 + … + n(n + 1) = (1/3)n(n + 1)(n + 2).",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 1·2 = 2 and RHS = (1/3)(1)(2)(3) = 2, so P(1) is true. "
       "<b>Hypothesis</b>: 2 + 6 + … + k(k + 1) = (1/3)k(k + 1)(k + 2). "
       "<b>Step</b>: add (k + 1)(k + 2): (1/3)k(k + 1)(k + 2) + (k + 1)(k + 2) = (k + 1)(k + 2)(k/3 + 1) = (1/3)(k + 1)(k + 2)(k + 3), which is P(k + 1). "
       "<b>Conclusion</b>: the statement is true for all positive integers n.",
       222),
    bq(U, EX1, 'EX7.1', '1(vii)',
       "Prove by mathematical induction for every positive integer n: 2² + 4² + 6² + … + (2n)² = (2/3)n(n + 1)(2n + 1).",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 2² = 4 and RHS = (2/3)(1)(2)(3) = 4, so P(1) is true. "
       "<b>Hypothesis</b>: 2² + 4² + … + (2k)² = (2/3)k(k + 1)(2k + 1). "
       "<b>Step</b>: add (2k + 2)² = 4(k + 1)²: (2/3)k(k + 1)(2k + 1) + 4(k + 1)² = (2/3)(k + 1)[k(2k + 1) + 6(k + 1)] = (2/3)(k + 1)(2k² + 7k + 6) = (2/3)(k + 1)(k + 2)(2k + 3) = (2/3)(k + 1)((k + 1) + 1)(2(k + 1) + 1), which is P(k + 1). "
       "<b>Conclusion</b>: by induction the formula holds for all n ∈ ℕ.",
       222),
    bq(U, EX1, 'EX7.1', '1(viii)',
       "Prove by mathematical induction for every positive integer n: 1·3 + 2·4 + 3·5 + … + n(n + 2) = (1/6)n(n + 1)(2n + 7).",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 1·3 = 3 and RHS = (1/6)(1)(2)(9) = 3, so P(1) is true. "
       "<b>Hypothesis</b>: 1·3 + 2·4 + … + k(k + 2) = (1/6)k(k + 1)(2k + 7). "
       "<b>Step</b>: add (k + 1)(k + 3): (1/6)k(k + 1)(2k + 7) + (k + 1)(k + 3) = (k + 1)[k(2k + 7) + 6(k + 3)]/6 = (k + 1)(2k² + 13k + 18)/6 = (k + 1)(k + 2)(2k + 9)/6 = (1/6)(k + 1)(k + 2)(2(k + 1) + 7), which is P(k + 1). "
       "<b>Conclusion</b>: P(n) holds for every positive integer n.",
       222),

    bq(U, EX1, 'EX7.1', '1(ix)',
       "Prove by mathematical induction for every positive integer n: 1/(1·2) + 1/(2·3) + 1/(3·4) + … + 1/(n(n + 1)) = n/(n + 1).",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 1/2 and RHS = 1/2, so P(1) is true. "
       "<b>Hypothesis</b>: 1/(1·2) + … + 1/(k(k + 1)) = k/(k + 1). "
       "<b>Step</b>: add 1/((k + 1)(k + 2)): k/(k + 1) + 1/((k + 1)(k + 2)) = [k(k + 2) + 1]/((k + 1)(k + 2)) = (k² + 2k + 1)/((k + 1)(k + 2)) = (k + 1)²/((k + 1)(k + 2)) = (k + 1)/(k + 2), which is P(k + 1). "
       "<b>Conclusion</b>: the identity holds for all n ∈ ℕ.",
       223),
    bq(U, EX1, 'EX7.1', '1(x)',
       "Prove by mathematical induction: 1·2 + 2·2² + 3·2³ + 4·2⁴ + … + n·2<sup>n</sup> = (n − 1)2<sup>n+1</sup> + 2, n a positive integer. (The book misprints the third and fourth terms as 3·2² and 4·2²; the general term n·2<sup>n</sup> and the stated sum require 3·2³ and 4·2⁴.)",
       "Proof shown.",
       "The sum is Σ<sub>r=1</sub><sup>n</sup> r·2<sup>r</sup>. <b>Basis</b> (n = 1): LHS = 1·2 = 2 and RHS = (1 − 1)2² + 2 = 2, so P(1) is true. "
       "<b>Hypothesis</b>: Σ<sub>r=1</sub><sup>k</sup> r·2<sup>r</sup> = (k − 1)2<sup>k+1</sup> + 2. "
       "<b>Step</b>: add (k + 1)2<sup>k+1</sup>: (k − 1)2<sup>k+1</sup> + 2 + (k + 1)2<sup>k+1</sup> = 2k·2<sup>k+1</sup> + 2 = k·2<sup>k+2</sup> + 2 = ((k + 1) − 1)2<sup>(k+1)+1</sup> + 2, which is P(k + 1). "
       "<b>Conclusion</b>: by induction the formula is true for all positive integers n.",
       223),
    bq(U, EX1, 'EX7.1', '1(xi)',
       "Prove by mathematical induction for every positive integer n: 1!·1 + 2!·2 + 3!·3 + … + n!·n = (n + 1)! − 1.",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 1!·1 = 1 and RHS = 2! − 1 = 1, so P(1) is true. "
       "<b>Hypothesis</b>: 1!·1 + 2!·2 + … + k!·k = (k + 1)! − 1. "
       "<b>Step</b>: add (k + 1)!·(k + 1): (k + 1)! − 1 + (k + 1)(k + 1)! = (k + 1)!(1 + k + 1) − 1 = (k + 1)!(k + 2) − 1 = (k + 2)! − 1, which is P(k + 1). "
       "<b>Conclusion</b>: the statement holds for every positive integer n.",
       223),
    bq(U, EX1, 'EX7.1', '1(xii)',
       "Prove by mathematical induction: 1/(a(a + 1)) + 1/((a + 1)(a + 2)) + … + 1/((a + n − 1)(a + n)) = n/(a(a + n)), n a positive integer.",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 1/(a(a + 1)) and RHS = 1/(a(a + 1)), so P(1) is true. "
       "<b>Hypothesis</b>: the sum up to the term 1/((a + k − 1)(a + k)) equals k/(a(a + k)). "
       "<b>Step</b>: add 1/((a + k)(a + k + 1)): k/(a(a + k)) + 1/((a + k)(a + k + 1)) = [k(a + k + 1) + a]/[a(a + k)(a + k + 1)] = (k² + ak + k + a)/[a(a + k)(a + k + 1)] = (k + 1)(k + a)/[a(a + k)(a + k + 1)] = (k + 1)/(a(a + k + 1)), which is P(k + 1). "
       "<b>Conclusion</b>: by induction the identity holds for all positive integers n.",
       223),
    bq(U, EX1, 'EX7.1', '1(xiii)',
       "Prove by mathematical induction for every positive integer n: 1²/(1·3) + 2²/(3·5) + … + n²/((2n − 1)(2n + 1)) = n(n + 1)/(2(2n + 1)).",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 1/3 and RHS = (1)(2)/(2·3) = 1/3, so P(1) is true. "
       "<b>Hypothesis</b>: the sum up to the k-th term equals k(k + 1)/(2(2k + 1)). "
       "<b>Step</b>: add (k + 1)²/((2k + 1)(2k + 3)). With common denominator 2(2k + 1)(2k + 3), the numerator is k(k + 1)(2k + 3) + 2(k + 1)² = (k + 1)[k(2k + 3) + 2(k + 1)] = (k + 1)(2k² + 5k + 2) = (k + 1)(k + 2)(2k + 1). Hence the sum is (k + 1)(k + 2)(2k + 1)/[2(2k + 1)(2k + 3)] = (k + 1)(k + 2)/(2(2k + 3)), which is P(k + 1). "
       "<b>Conclusion</b>: P(n) is true for all n ∈ ℕ.",
       223),
    bq(U, EX1, 'EX7.1', '1(xiv)(i)',
       "Prove by mathematical induction: a + ar + ar² + … + ar<sup>n−1</sup> = a(1 − r<sup>n</sup>)/(1 − r), r ≠ 1, n a positive integer. (The book prints a(a − r<sup>n</sup>)/(1 − r); the repeated a is a misprint.)",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = a and RHS = a(1 − r)/(1 − r) = a (since r ≠ 1), so P(1) is true. "
       "<b>Hypothesis</b>: a + ar + … + ar<sup>k−1</sup> = a(1 − r<sup>k</sup>)/(1 − r). "
       "<b>Step</b>: add the next term ar<sup>k</sup>: a(1 − r<sup>k</sup>)/(1 − r) + ar<sup>k</sup> = [a(1 − r<sup>k</sup>) + ar<sup>k</sup>(1 − r)]/(1 − r) = [a − ar<sup>k</sup> + ar<sup>k</sup> − ar<sup>k+1</sup>]/(1 − r) = a(1 − r<sup>k+1</sup>)/(1 − r), which is P(k + 1). "
       "<b>Conclusion</b>: the geometric-sum formula holds for every positive integer n.",
       223),
    bq(U, EX1, 'EX7.1', '1(xiv)(ii)',
       "Prove by mathematical induction: <sup>n</sup>C<sub>0</sub> + <sup>n</sup>C<sub>1</sub> + <sup>n</sup>C<sub>2</sub> + … + <sup>n</sup>C<sub>n</sub> = 2<sup>n</sup>, n a positive integer.",
       "Proof shown.",
       "<b>Basis</b> (n = 1): <sup>1</sup>C<sub>0</sub> + <sup>1</sup>C<sub>1</sub> = 1 + 1 = 2 = 2<sup>1</sup>, so P(1) is true. "
       "<b>Hypothesis</b>: Σ<sub>r=0</sub><sup>k</sup> <sup>k</sup>C<sub>r</sub> = 2<sup>k</sup>. "
       "<b>Step</b>: using Pascal's rule <sup>k+1</sup>C<sub>r</sub> = <sup>k</sup>C<sub>r−1</sub> + <sup>k</sup>C<sub>r</sub> for 1 ≤ r ≤ k, "
       "Σ<sub>r=0</sub><sup>k+1</sup> <sup>k+1</sup>C<sub>r</sub> = 1 + 1 + Σ<sub>r=1</sub><sup>k</sup>(<sup>k</sup>C<sub>r−1</sub> + <sup>k</sup>C<sub>r</sub>) = 2 + (2<sup>k</sup> − 1) + (2<sup>k</sup> − 1) = 2<sup>k+1</sup>, which is P(k + 1). "
       "<b>Conclusion</b>: by induction the sum of all binomial coefficients is 2<sup>n</sup>.",
       223),
    bq(U, EX1, 'EX7.1', '1(xiv)(iii)',
       "Prove by mathematical induction: <sup>n</sup>C<sub>r−1</sub> + <sup>n</sup>C<sub>r</sub> = <sup>n+1</sup>C<sub>r</sub> for n ≥ r (Pascal's rule).",
       "Proof shown.",
       "Work by induction on n with r fixed. <b>Basis</b> (n = r): <sup>r</sup>C<sub>r−1</sub> + <sup>r</sup>C<sub>r</sub> = r + 1 = <sup>r+1</sup>C<sub>r</sub>, so P(r) is true. "
       "<b>Hypothesis</b>: <sup>k</sup>C<sub>r−1</sub> + <sup>k</sup>C<sub>r</sub> = <sup>k+1</sup>C<sub>r</sub> for some k ≥ r. "
       "<b>Step</b>: for n = k + 1, <sup>k+1</sup>C<sub>r−1</sub> + <sup>k+1</sup>C<sub>r</sub> = (k + 1)!/[(r − 1)!(k − r + 2)!] + (k + 1)!/[r!(k − r + 1)!] = (k + 1)![r + (k − r + 2)]/[r!(k − r + 2)!] = (k + 1)!(k + 2)/[r!(k − r + 2)!] = (k + 2)!/[r!(k + 2 − r)!] = <sup>k+2</sup>C<sub>r</sub>, which is P(k + 1). "
       "<b>Conclusion</b>: Pascal's rule holds for all n ≥ r.",
       223),

    bq(U, EX1, 'EX7.1', '2(i)',
       "Prove by mathematical induction: 2<sup>3n+2</sup> − 28n − 4 is divisible by 49 for all n ∈ ℕ.",
       "Proof shown.",
       "<b>Basis</b> (n = 1): 2<sup>5</sup> − 28 − 4 = 32 − 32 = 0 = 49·0, so P(1) is true. "
       "<b>Hypothesis</b>: 2<sup>3k+2</sup> − 28k − 4 = 49m for some integer m, i.e. 2<sup>3k+2</sup> = 49m + 28k + 4. "
       "<b>Step</b>: 2<sup>3(k+1)+2</sup> − 28(k + 1) − 4 = 8·2<sup>3k+2</sup> − 28k − 32 = 8(49m + 28k + 4) − 28k − 32 = 392m + 224k + 32 − 28k − 32 = 392m + 196k = 49(8m + 4k), which is divisible by 49, so P(k + 1) is true. "
       "<b>Conclusion</b>: by induction the expression is divisible by 49 for every n ∈ ℕ.",
       223),
    bq(U, EX1, 'EX7.1', '2(ii)',
       "Prove by mathematical induction: 3<sup>2n+2</sup> − 8n − 9 is divisible by 64 for all n ∈ ℕ.",
       "Proof shown.",
       "<b>Basis</b> (n = 1): 3<sup>4</sup> − 8 − 9 = 81 − 17 = 64 = 64·1, so P(1) is true. "
       "<b>Hypothesis</b>: 3<sup>2k+2</sup> − 8k − 9 = 64m, i.e. 3<sup>2k+2</sup> = 64m + 8k + 9. "
       "<b>Step</b>: 3<sup>2(k+1)+2</sup> − 8(k + 1) − 9 = 9·3<sup>2k+2</sup> − 8k − 17 = 9(64m + 8k + 9) − 8k − 17 = 576m + 72k + 81 − 8k − 17 = 576m + 64k + 64 = 64(9m + k + 1), which is divisible by 64, so P(k + 1) is true. "
       "<b>Conclusion</b>: the statement holds for every n ∈ ℕ.",
       223),
    bq(U, EX1, 'EX7.1', '2(iii)',
       "Prove by mathematical induction: 7<sup>n</sup> − 4<sup>n</sup> is divisible by 3 (for all n ∈ ℕ).",
       "Proof shown.",
       "<b>Basis</b> (n = 1): 7 − 4 = 3 = 3·1, so P(1) is true. "
       "<b>Hypothesis</b>: 7<sup>k</sup> − 4<sup>k</sup> = 3m, i.e. 7<sup>k</sup> = 4<sup>k</sup> + 3m. "
       "<b>Step</b>: 7<sup>k+1</sup> − 4<sup>k+1</sup> = 7·7<sup>k</sup> − 4·4<sup>k</sup> = 7(4<sup>k</sup> + 3m) − 4·4<sup>k</sup> = 3·4<sup>k</sup> + 21m = 3(4<sup>k</sup> + 7m), which is divisible by 3, so P(k + 1) is true. "
       "<b>Conclusion</b>: by induction 7<sup>n</sup> − 4<sup>n</sup> is divisible by 3 for all n ∈ ℕ.",
       223),

    bq(U, EX1, 'EX7.1', '3(i)',
       "Prove by induction: 2<sup>n+1</sup> > 2n + 3 for all integral values of n ≥ 2.",
       "Proof shown.",
       "<b>Basis</b> (n = 2): 2<sup>3</sup> = 8 > 2(2) + 3 = 7, so P(2) is true. "
       "<b>Hypothesis</b>: 2<sup>k+1</sup> > 2k + 3 for some k ≥ 2. "
       "<b>Step</b>: 2<sup>k+2</sup> = 2·2<sup>k+1</sup> > 2(2k + 3) = 4k + 6 > 2k + 5 = 2(k + 1) + 3, because 4k + 6 − (2k + 5) = 2k + 1 > 0. Hence P(k + 1) is true. "
       "<b>Conclusion</b>: by induction the inequality holds for every integer n ≥ 2.",
       223),
    bq(U, EX1, 'EX7.1', '3(ii)',
       "Prove by induction: 3<sup>n−1</sup> > 2<sup>n</sup> for all integral values of n ≥ 3.",
       "Proof shown.",
       "<b>Basis</b> (n = 3): 3² = 9 > 2³ = 8, so P(3) is true. "
       "<b>Hypothesis</b>: 3<sup>k−1</sup> > 2<sup>k</sup> for some k ≥ 3. "
       "<b>Step</b>: 3<sup>k</sup> = 3·3<sup>k−1</sup> > 3·2<sup>k</sup> > 2·2<sup>k</sup> = 2<sup>k+1</sup>, so P(k + 1) is true. "
       "<b>Conclusion</b>: 3<sup>n−1</sup> > 2<sup>n</sup> for every integer n ≥ 3.",
       223),
    bq(U, EX1, 'EX7.1', '3(iii)',
       "Prove by induction: n! > 3<sup>n−1</sup> for all integral values of n ≥ 5.",
       "Proof shown.",
       "<b>Basis</b> (n = 5): 5! = 120 > 3<sup>4</sup> = 81, so P(5) is true. "
       "<b>Hypothesis</b>: k! > 3<sup>k−1</sup> for some k ≥ 5. "
       "<b>Step</b>: (k + 1)! = (k + 1)·k! > (k + 1)·3<sup>k−1</sup>. Since k + 1 ≥ 6 > 3, (k + 1)·3<sup>k−1</sup> > 3·3<sup>k−1</sup> = 3<sup>k</sup>, so (k + 1)! > 3<sup>k</sup>, which is P(k + 1). "
       "<b>Conclusion</b>: by induction n! > 3<sup>n−1</sup> for every integer n ≥ 5.",
       223),
]

# ============================================================ Exercise 7.2 (pdf 231-232)
ITEMS += [
    bq(U, EX2, 'EX7.2', '1(i)',
       "Expand by means of the binomial theorem: (a + b)<sup>8</sup>.",
       "a<sup>8</sup> + 8a<sup>7</sup>b + 28a<sup>6</sup>b<sup>2</sup> + 56a<sup>5</sup>b<sup>3</sup> + 70a<sup>4</sup>b<sup>4</sup> + 56a<sup>3</sup>b<sup>5</sup> + 28a<sup>2</sup>b<sup>6</sup> + 8ab<sup>7</sup> + b<sup>8</sup>.",
       "(a + b)<sup>8</sup> = Σ<sub>r=0</sub><sup>8</sup> <sup>8</sup>C<sub>r</sub> a<sup>8−r</sup>b<sup>r</sup>. The coefficients are row 8 of Pascal's triangle: 1, 8, 28, 56, 70, 56, 28, 8, 1, giving a<sup>8</sup> + 8a<sup>7</sup>b + 28a<sup>6</sup>b<sup>2</sup> + 56a<sup>5</sup>b<sup>3</sup> + 70a<sup>4</sup>b<sup>4</sup> + 56a<sup>3</sup>b<sup>5</sup> + 28a<sup>2</sup>b<sup>6</sup> + 8ab<sup>7</sup> + b<sup>8</sup>.",
       231),
    bq(U, EX2, 'EX7.2', '1(ii)',
       "Expand by means of the binomial theorem: (2x − 3y)<sup>4</sup>.",
       "16x<sup>4</sup> − 96x<sup>3</sup>y + 216x<sup>2</sup>y<sup>2</sup> − 216xy<sup>3</sup> + 81y<sup>4</sup>.",
       "<sup>4</sup>C<sub>0</sub>(2x)<sup>4</sup> − <sup>4</sup>C<sub>1</sub>(2x)<sup>3</sup>(3y) + <sup>4</sup>C<sub>2</sub>(2x)<sup>2</sup>(3y)<sup>2</sup> − <sup>4</sup>C<sub>3</sub>(2x)(3y)<sup>3</sup> + <sup>4</sup>C<sub>4</sub>(3y)<sup>4</sup> = 16x<sup>4</sup> − 4·8x<sup>3</sup>·3y + 6·4x<sup>2</sup>·9y<sup>2</sup> − 4·2x·27y<sup>3</sup> + 81y<sup>4</sup> = 16x<sup>4</sup> − 96x<sup>3</sup>y + 216x<sup>2</sup>y<sup>2</sup> − 216xy<sup>3</sup> + 81y<sup>4</sup>.",
       231),
    bq(U, EX2, 'EX7.2', '1(iii)',
       "Expand by means of the binomial theorem: (√(x/y) − √(y/x))<sup>4</sup>.",
       "x<sup>2</sup>/y<sup>2</sup> − 4x/y + 6 − 4y/x + y<sup>2</sup>/x<sup>2</sup>.",
       "Let p = √(x/y) and q = √(y/x), so pq = 1, p² = x/y and q² = y/x. Then p<sup>4</sup> = x<sup>2</sup>/y<sup>2</sup>, p<sup>3</sup>q = p² = x/y, p<sup>2</sup>q<sup>2</sup> = 1, pq<sup>3</sup> = q² = y/x and q<sup>4</sup> = y<sup>2</sup>/x<sup>2</sup>. Hence (p − q)<sup>4</sup> = p<sup>4</sup> − 4p<sup>3</sup>q + 6p<sup>2</sup>q<sup>2</sup> − 4pq<sup>3</sup> + q<sup>4</sup> = x<sup>2</sup>/y<sup>2</sup> − 4x/y + 6 − 4y/x + y<sup>2</sup>/x<sup>2</sup>.",
       231),
    bq(U, EX2, 'EX7.2', '1(iv)',
       "Expand by means of the binomial theorem: (x<sup>2</sup>/2 − 2/x)<sup>6</sup>.",
       "x<sup>12</sup>/64 − 3x<sup>9</sup>/8 + 15x<sup>6</sup>/4 − 20x<sup>3</sup> + 60 − 96/x<sup>3</sup> + 64/x<sup>6</sup>.",
       "(x<sup>2</sup>/2 − 2/x)<sup>6</sup> = <sup>6</sup>C<sub>0</sub>(x<sup>2</sup>/2)<sup>6</sup> − <sup>6</sup>C<sub>1</sub>(x<sup>2</sup>/2)<sup>5</sup>(2/x) + <sup>6</sup>C<sub>2</sub>(x<sup>2</sup>/2)<sup>4</sup>(2/x)<sup>2</sup> − <sup>6</sup>C<sub>3</sub>(x<sup>2</sup>/2)<sup>3</sup>(2/x)<sup>3</sup> + <sup>6</sup>C<sub>4</sub>(x<sup>2</sup>/2)<sup>2</sup>(2/x)<sup>4</sup> − <sup>6</sup>C<sub>5</sub>(x<sup>2</sup>/2)(2/x)<sup>5</sup> + <sup>6</sup>C<sub>6</sub>(2/x)<sup>6</sup> "
       "= x<sup>12</sup>/64 − 6(x<sup>10</sup>/32)(2/x) + 15(x<sup>8</sup>/16)(4/x<sup>2</sup>) − 20(x<sup>6</sup>/8)(8/x<sup>3</sup>) + 15(x<sup>4</sup>/4)(16/x<sup>4</sup>) − 6(x<sup>2</sup>/2)(32/x<sup>5</sup>) + 64/x<sup>6</sup> "
       "= x<sup>12</sup>/64 − 3x<sup>9</sup>/8 + 15x<sup>6</sup>/4 − 20x<sup>3</sup> + 60 − 96/x<sup>3</sup> + 64/x<sup>6</sup>.",
       231),
    bq(U, EX2, 'EX7.2', '1(v)',
       "Expand by means of the binomial theorem: (3x<sup>2</sup> − 2y<sup>3</sup>)<sup>5</sup>.",
       "243x<sup>10</sup> − 810x<sup>8</sup>y<sup>3</sup> + 1080x<sup>6</sup>y<sup>6</sup> − 720x<sup>4</sup>y<sup>9</sup> + 240x<sup>2</sup>y<sup>12</sup> − 32y<sup>15</sup>.",
       "(3x<sup>2</sup> − 2y<sup>3</sup>)<sup>5</sup> = (3x<sup>2</sup>)<sup>5</sup> − 5(3x<sup>2</sup>)<sup>4</sup>(2y<sup>3</sup>) + 10(3x<sup>2</sup>)<sup>3</sup>(2y<sup>3</sup>)<sup>2</sup> − 10(3x<sup>2</sup>)<sup>2</sup>(2y<sup>3</sup>)<sup>3</sup> + 5(3x<sup>2</sup>)(2y<sup>3</sup>)<sup>4</sup> − (2y<sup>3</sup>)<sup>5</sup> "
       "= 243x<sup>10</sup> − 5·81x<sup>8</sup>·2y<sup>3</sup> + 10·27x<sup>6</sup>·4y<sup>6</sup> − 10·9x<sup>4</sup>·8y<sup>9</sup> + 5·3x<sup>2</sup>·16y<sup>12</sup> − 32y<sup>15</sup> "
       "= 243x<sup>10</sup> − 810x<sup>8</sup>y<sup>3</sup> + 1080x<sup>6</sup>y<sup>6</sup> − 720x<sup>4</sup>y<sup>9</sup> + 240x<sup>2</sup>y<sup>12</sup> − 32y<sup>15</sup>.",
       231),

    bq(U, EX2, 'EX7.2', '2(a)(i)',
       "Use the binomial theorem to find the value of: (11)<sup>5</sup>.",
       "161051.",
       "(11)<sup>5</sup> = (10 + 1)<sup>5</sup> = 10<sup>5</sup> + 5·10<sup>4</sup> + 10·10<sup>3</sup> + 10·10<sup>2</sup> + 5·10 + 1 = 100000 + 50000 + 10000 + 1000 + 50 + 1 = 161051.",
       231),
    bq(U, EX2, 'EX7.2', '2(a)(ii)',
       "Use the binomial theorem to find the value of: (19)<sup>6</sup>.",
       "47045881.",
       "(19)<sup>6</sup> = (20 − 1)<sup>6</sup> = 20<sup>6</sup> − 6·20<sup>5</sup> + 15·20<sup>4</sup> − 20·20<sup>3</sup> + 15·20<sup>2</sup> − 6·20 + 1 = 64000000 − 19200000 + 2400000 − 160000 + 6000 − 120 + 1 = 47045881.",
       231),
    bq(U, EX2, 'EX7.2', '2(a)(iii)',
       "Use the binomial theorem to find the value of: (99)<sup>4</sup>.",
       "96059601.",
       "(99)<sup>4</sup> = (100 − 1)<sup>4</sup> = 100<sup>4</sup> − 4·100<sup>3</sup> + 6·100<sup>2</sup> − 4·100 + 1 = 100000000 − 4000000 + 60000 − 400 + 1 = 96059601.",
       231),
    bq(U, EX2, 'EX7.2', '2(b)(i)',
       "Use the binomial theorem to compute (1.01)<sup>6</sup> correct to four places of decimal.",
       "1.0615.",
       "(1.01)<sup>6</sup> = (1 + 0.01)<sup>6</sup> = 1 + 6(0.01) + 15(0.01)<sup>2</sup> + 20(0.01)<sup>3</sup> + 15(0.01)<sup>4</sup> + … = 1 + 0.06 + 0.0015 + 0.00002 + 0.00000015 + … = 1.06152015… ≈ 1.0615.",
       231),
    bq(U, EX2, 'EX7.2', '2(b)(ii)',
       "Use the binomial theorem to compute (1.02)<sup>7</sup> correct to four places of decimal.",
       "1.1487.",
       "(1.02)<sup>7</sup> = (1 + 0.02)<sup>7</sup> = 1 + 7(0.02) + 21(0.02)<sup>2</sup> + 35(0.02)<sup>3</sup> + 35(0.02)<sup>4</sup> + … = 1 + 0.14 + 0.0084 + 0.00028 + 0.0000056 + … = 1.1486856… ≈ 1.1487.",
       231),
    bq(U, EX2, 'EX7.2', '2(b)(iii)',
       "Use the binomial theorem to compute (2.03)<sup>5</sup> correct to four places of decimal.",
       "34.4731.",
       "(2.03)<sup>5</sup> = (2 + 0.03)<sup>5</sup> = 2<sup>5</sup> + 5·2<sup>4</sup>(0.03) + 10·2<sup>3</sup>(0.03)<sup>2</sup> + 10·2<sup>2</sup>(0.03)<sup>3</sup> + 5·2(0.03)<sup>4</sup> + (0.03)<sup>5</sup> = 32 + 2.4 + 0.072 + 0.00108 + 0.0000081 + 0.0000000243 ≈ 34.4731.",
       231),

    bq(U, EX2, 'EX7.2', '3(i)',
       "Evaluate: (1 + 2√a)<sup>4</sup> − (1 − 2√a)<sup>4</sup>.",
       "16√a + 64a√a.",
       "For u = 2√a, (1 + u)<sup>4</sup> − (1 − u)<sup>4</sup> = 2[<sup>4</sup>C<sub>1</sub>u + <sup>4</sup>C<sub>3</sub>u<sup>3</sup>] = 2(4u + 4u<sup>3</sup>) = 8u + 8u<sup>3</sup>. Substituting u = 2√a gives 16√a + 8(8a√a) = 16√a + 64a√a.",
       232),
    bq(U, EX2, 'EX7.2', '3(ii)',
       "Evaluate: (2 − √(1 − a))<sup>5</sup> + (2 + √(1 − a))<sup>5</sup>.",
       "20a<sup>2</sup> − 200a + 244.",
       "For u = √(1 − a), (2 + u)<sup>5</sup> + (2 − u)<sup>5</sup> = 2[<sup>5</sup>C<sub>0</sub>2<sup>5</sup> + <sup>5</sup>C<sub>2</sub>2<sup>3</sup>u<sup>2</sup> + <sup>5</sup>C<sub>4</sub>2u<sup>4</sup>] = 2[32 + 10·8(1 − a) + 5·2(1 − a)<sup>2</sup>] = 64 + 160(1 − a) + 20(1 − a)<sup>2</sup> = 64 + 160 − 160a + 20 − 40a + 20a<sup>2</sup> = 20a<sup>2</sup> − 200a + 244.",
       232),
    bq(U, EX2, 'EX7.2', '3(iii)',
       "Evaluate: (2 + √3)<sup>5</sup> − (2 − √3)<sup>5</sup>.",
       "418√3.",
       "(2 + √3)<sup>5</sup> − (2 − √3)<sup>5</sup> = 2[<sup>5</sup>C<sub>1</sub>2<sup>4</sup>√3 + <sup>5</sup>C<sub>3</sub>2<sup>2</sup>(√3)<sup>3</sup> + <sup>5</sup>C<sub>5</sub>(√3)<sup>5</sup>] = 2[80√3 + 10·4·3√3 + 9√3] = 2(80 + 120 + 9)√3 = 418√3.",
       232),

    bq(U, EX2, 'EX7.2', '4(i)',
       "Find the indicated term in the expansion of (2x/3 − 3/2)<sup>10</sup>: the 8<sup>th</sup> term.",
       "−(1215/2)x<sup>3</sup>.",
       "The general term is T<sub>r+1</sub> = <sup>10</sup>C<sub>r</sub>(2x/3)<sup>10−r</sup>(−3/2)<sup>r</sup>. For the 8<sup>th</sup> term r = 7: T<sub>8</sub> = <sup>10</sup>C<sub>7</sub>(2x/3)<sup>3</sup>(−3/2)<sup>7</sup> = 120·(8x<sup>3</sup>/27)·(−2187/128) = −(120·8·2187)/(27·128)x<sup>3</sup> = −(960·81)/128 x<sup>3</sup> = −(1215/2)x<sup>3</sup>.",
       232),
    bq(U, EX2, 'EX7.2', '4(ii)',
       "Find the indicated term in the expansion of (a/b − b/a)<sup>8</sup>: the 7<sup>th</sup> term.",
       "28b<sup>4</sup>/a<sup>4</sup>.",
       "T<sub>r+1</sub> = <sup>8</sup>C<sub>r</sub>(a/b)<sup>8−r</sup>(−b/a)<sup>r</sup>. For the 7<sup>th</sup> term r = 6: T<sub>7</sub> = <sup>8</sup>C<sub>6</sub>(a/b)<sup>2</sup>(−b/a)<sup>6</sup> = 28·(a<sup>2</sup>/b<sup>2</sup>)(b<sup>6</sup>/a<sup>6</sup>) = 28b<sup>4</sup>/a<sup>4</sup>.",
       232),
    bq(U, EX2, 'EX7.2', '4(iii)',
       "Find the indicated term in the expansion of (2x − 1/y)<sup>10</sup>: the last term.",
       "1/y<sup>10</sup>.",
       "The last term corresponds to r = 10: T<sub>11</sub> = <sup>10</sup>C<sub>10</sub>(2x)<sup>0</sup>(−1/y)<sup>10</sup> = (−1)<sup>10</sup>/y<sup>10</sup> = 1/y<sup>10</sup>.",
       232),

    bq(U, EX2, 'EX7.2', '5(i)',
       "Find the middle term in the expansion of (b − 2c/3)<sup>10</sup>.",
       "−(896/27)b<sup>5</sup>c<sup>5</sup>.",
       "Here n = 10 is even, so there is one middle term, the (10/2 + 1) = 6<sup>th</sup> term. T<sub>6</sub> = <sup>10</sup>C<sub>5</sub>b<sup>5</sup>(−2c/3)<sup>5</sup> = 252·(−32/243)b<sup>5</sup>c<sup>5</sup> = −8064/243 b<sup>5</sup>c<sup>5</sup> = −(896/27)b<sup>5</sup>c<sup>5</sup>.",
       232),
    bq(U, EX2, 'EX7.2', '5(ii)',
       "Find the middle term in the expansion of (1 − (1/2)a<sup>2</sup>)<sup>14</sup>.",
       "−(429/16)a<sup>14</sup>.",
       "n = 14 is even, so the middle term is the (14/2 + 1) = 8<sup>th</sup> term. T<sub>8</sub> = <sup>14</sup>C<sub>7</sub>(−a<sup>2</sup>/2)<sup>7</sup> = 3432·(−1/128)a<sup>14</sup> = −(3432/128)a<sup>14</sup> = −(429/16)a<sup>14</sup>.",
       232),
    bq(U, EX2, 'EX7.2', '5(iii)',
       "Find the middle term in the expansion of (a/b − b/a)<sup>18</sup>.",
       "−48620.",
       "n = 18 is even, so the middle term is the 10<sup>th</sup> term. T<sub>10</sub> = <sup>18</sup>C<sub>9</sub>(a/b)<sup>9</sup>(−b/a)<sup>9</sup> = 48620·(a<sup>9</sup>/b<sup>9</sup>)(−b<sup>9</sup>/a<sup>9</sup>) = −48620.",
       232),
    bq(U, EX2, 'EX7.2', '5(iv)',
       "Find the middle term in the expansion of (a − 1/a)<sup>2n</sup>.",
       "(−1)<sup>n</sup>(2n)!/(n!)<sup>2</sup>.",
       "The index 2n is even, so the middle term is the (n + 1)<sup>th</sup> term. T<sub>n+1</sub> = <sup>2n</sup>C<sub>n</sub>a<sup>n</sup>(−1/a)<sup>n</sup> = <sup>2n</sup>C<sub>n</sub>(−1)<sup>n</sup> = (−1)<sup>n</sup>(2n)!/(n!)<sup>2</sup>.",
       232),

    bq(U, EX2, 'EX7.2', '6(i)',
       "Find the two middle terms of (x<sup>3</sup> + 1/x<sup>2</sup>)<sup>7</sup>.",
       "35x<sup>6</sup> and 35x.",
       "n = 7 is odd, so the middle terms are the (7 + 1)/2 = 4<sup>th</sup> and (7 + 3)/2 = 5<sup>th</sup> terms. T<sub>4</sub> = <sup>7</sup>C<sub>3</sub>(x<sup>3</sup>)<sup>4</sup>(x<sup>−2</sup>)<sup>3</sup> = 35x<sup>12</sup>·x<sup>−6</sup> = 35x<sup>6</sup>; T<sub>5</sub> = <sup>7</sup>C<sub>4</sub>(x<sup>3</sup>)<sup>3</sup>(x<sup>−2</sup>)<sup>4</sup> = 35x<sup>9</sup>·x<sup>−8</sup> = 35x.",
       232),
    bq(U, EX2, 'EX7.2', '6(ii)',
       "Find the two middle terms of (2b − b<sup>2</sup>/4)<sup>9</sup>.",
       "(63/4)b<sup>13</sup> and −(63/32)b<sup>14</sup>.",
       "n = 9 is odd, so the middle terms are the 5<sup>th</sup> and 6<sup>th</sup> terms. T<sub>5</sub> = <sup>9</sup>C<sub>4</sub>(2b)<sup>5</sup>(−b<sup>2</sup>/4)<sup>4</sup> = 126·32b<sup>5</sup>·b<sup>8</sup>/256 = (126·32/256)b<sup>13</sup> = (63/4)b<sup>13</sup>; T<sub>6</sub> = <sup>9</sup>C<sub>5</sub>(2b)<sup>4</sup>(−b<sup>2</sup>/4)<sup>5</sup> = 126·16b<sup>4</sup>·(−b<sup>10</sup>/1024) = −(2016/1024)b<sup>14</sup> = −(63/32)b<sup>14</sup>.",
       232),

    bq(U, EX2, 'EX7.2', '7(i)',
       "Write, in simplified form, the term independent of x in (2x + 1/x<sup>2</sup>)<sup>9</sup>.",
       "5376.",
       "T<sub>r+1</sub> = <sup>9</sup>C<sub>r</sub>(2x)<sup>9−r</sup>(1/x<sup>2</sup>)<sup>r</sup> = <sup>9</sup>C<sub>r</sub>2<sup>9−r</sup>x<sup>9−3r</sup>. For the term independent of x, 9 − 3r = 0, so r = 3. Hence T<sub>4</sub> = <sup>9</sup>C<sub>3</sub>2<sup>6</sup> = 84·64 = 5376.",
       232),
    bq(U, EX2, 'EX7.2', '7(ii)',
       "Write, in simplified form, the term independent of x in (2x + 5/x)<sup>6</sup>.",
       "20000.",
       "T<sub>r+1</sub> = <sup>6</sup>C<sub>r</sub>(2x)<sup>6−r</sup>(5/x)<sup>r</sup> = <sup>6</sup>C<sub>r</sub>2<sup>6−r</sup>5<sup>r</sup>x<sup>6−2r</sup>. Independence of x requires 6 − 2r = 0, so r = 3. Hence T<sub>4</sub> = <sup>6</sup>C<sub>3</sub>2<sup>3</sup>5<sup>3</sup> = 20·8·125 = 20000.",
       232),

    bq(U, EX2, 'EX7.2', '8(i)',
       "Obtain in simplified form the term involving x<sup>6</sup> in the expansion of (2x<sup>3</sup> − 1/x<sup>2</sup>)<sup>7</sup>.",
       "−560x<sup>6</sup>.",
       "T<sub>r+1</sub> = <sup>7</sup>C<sub>r</sub>(2x<sup>3</sup>)<sup>7−r</sup>(−1/x<sup>2</sup>)<sup>r</sup> = <sup>7</sup>C<sub>r</sub>2<sup>7−r</sup>(−1)<sup>r</sup>x<sup>21−5r</sup>. For x<sup>6</sup>, 21 − 5r = 6, so r = 3. Then T<sub>4</sub> = <sup>7</sup>C<sub>3</sub>2<sup>4</sup>(−1)<sup>3</sup>x<sup>6</sup> = 35·16·(−1)x<sup>6</sup> = −560x<sup>6</sup>.",
       232),
    bq(U, EX2, 'EX7.2', '8(ii)',
       "Obtain in simplified form the term involving a<sup>8</sup> in the expansion of (a<sup>2</sup> − 1/a<sup>2</sup>)<sup>12</sup>.",
       "495a<sup>8</sup>.",
       "T<sub>r+1</sub> = <sup>12</sup>C<sub>r</sub>(a<sup>2</sup>)<sup>12−r</sup>(−1/a<sup>2</sup>)<sup>r</sup> = <sup>12</sup>C<sub>r</sub>(−1)<sup>r</sup>a<sup>24−4r</sup>. For a<sup>8</sup>, 24 − 4r = 8, so r = 4. Then T<sub>5</sub> = <sup>12</sup>C<sub>4</sub>(−1)<sup>4</sup>a<sup>8</sup> = 495a<sup>8</sup>.",
       232),
    bq(U, EX2, 'EX7.2', '8(iii)',
       "Obtain in simplified form the coefficient of x in the expansion of (x<sup>2</sup> + a<sup>2</sup>/x)<sup>5</sup>.",
       "10a<sup>6</sup>.",
       "T<sub>r+1</sub> = <sup>5</sup>C<sub>r</sub>(x<sup>2</sup>)<sup>5−r</sup>(a<sup>2</sup>/x)<sup>r</sup> = <sup>5</sup>C<sub>r</sub>a<sup>2r</sup>x<sup>10−3r</sup>. For x<sup>1</sup>, 10 − 3r = 1, so r = 3. The coefficient is <sup>5</sup>C<sub>3</sub>a<sup>6</sup> = 10a<sup>6</sup>.",
       232),

    bq(U, EX2, 'EX7.2', '9(i)',
       "Does the expansion of (3a/2 − 1/(3a<sup>3</sup>))<sup>9</sup> contain a term independent of a?",
       "No.",
       "T<sub>r+1</sub> = <sup>9</sup>C<sub>r</sub>(3a/2)<sup>9−r</sup>(−1/(3a<sup>3</sup>))<sup>r</sup>, whose power of a is a<sup>9−r−3r</sup> = a<sup>9−4r</sup>. Independence of a would require 9 − 4r = 0, i.e. r = 9/4, which is not a non-negative integer. Hence no such term exists.",
       232),
    bq(U, EX2, 'EX7.2', '9(ii)',
       "Does the expansion of (3a/2 − 1/(3a<sup>3</sup>))<sup>9</sup> contain a term involving a<sup>10</sup>?",
       "No.",
       "The general term has power a<sup>9−4r</sup>. A term in a<sup>10</sup> would require 9 − 4r = 10, i.e. r = −1/4, which is impossible for r = 0, 1, …, 9. Hence the expansion has no term involving a<sup>10</sup>.",
       232),

    bq(U, EX2, 'EX7.2', '10',
       "The coefficients of the fifth, sixth and seventh terms of the expansion of (1 + x)<sup>n</sup> form an A.P. Find n.",
       "n = 7 or n = 14.",
       "The coefficients are <sup>n</sup>C<sub>4</sub>, <sup>n</sup>C<sub>5</sub>, <sup>n</sup>C<sub>6</sub>. Since they are in A.P., 2<sup>n</sup>C<sub>5</sub> = <sup>n</sup>C<sub>4</sub> + <sup>n</sup>C<sub>6</sub>. Dividing by <sup>n</sup>C<sub>4</sub>: 2(n − 4)/5 = 1 + (n − 4)(n − 5)/30. Put m = n − 4: 12m = 30 + m(m − 1), so m<sup>2</sup> − 13m + 30 = 0, (m − 3)(m − 10) = 0. Thus m = 3 or 10 and n = 7 or 14.",
       232),
]

# ============================================================ Exercise 7.3 (pdf 239-240)
ITEMS += [
    bq(U, EX3, 'EX7.3', '1(i)',
       "Find the first four terms in the expansion of ∛(8 − 16x).",
       "2(1 − 2x/3 − 4x<sup>2</sup>/9 − 40x<sup>3</sup>/81 − …), i.e. 2 − 4x/3 − 8x<sup>2</sup>/9 − 80x<sup>3</sup>/81 − …",
       "∛(8 − 16x) = 8<sup>1/3</sup>(1 − 2x)<sup>1/3</sup> = 2(1 − 2x)<sup>1/3</sup>. Using (1 + u)<sup>1/3</sup> = 1 + u/3 − u<sup>2</sup>/9 + 5u<sup>3</sup>/81 − … with u = −2x gives (1 − 2x)<sup>1/3</sup> = 1 − 2x/3 − 4x<sup>2</sup>/9 − 40x<sup>3</sup>/81 − …, so the expansion is 2(1 − 2x/3 − 4x<sup>2</sup>/9 − 40x<sup>3</sup>/81 − …).",
       239),
    bq(U, EX3, 'EX7.3', '1(ii)',
       "Find the first four terms in the expansion of 3/(3 + x).",
       "1 − x/3 + x<sup>2</sup>/9 − x<sup>3</sup>/27 + … (valid for |x| < 3)",
       "3/(3 + x) = 1/(1 + x/3) = (1 + x/3)<sup>−1</sup>. Using (1 + u)<sup>−1</sup> = 1 − u + u<sup>2</sup> − u<sup>3</sup> + … with u = x/3 gives 1 − x/3 + x<sup>2</sup>/9 − x<sup>3</sup>/27 + ….",
       239),
    bq(U, EX3, 'EX7.3', '1(iii)',
       "Find the first four terms in the expansion of (1 + 3x)<sup>−1/3</sup>.",
       "1 − x + 2x<sup>2</sup> − (14/3)x<sup>3</sup> + …",
       "(1 + u)<sup>−1/3</sup> = 1 − u/3 + (2/9)u<sup>2</sup> − (14/81)u<sup>3</sup> + … since n(n − 1)/2! = (−1/3)(−4/3)/2 = 2/9 and n(n − 1)(n − 2)/3! = (−1/3)(−4/3)(−7/3)/6 = −14/81. Putting u = 3x gives 1 − x + (2/9)(9x<sup>2</sup>) − (14/81)(27x<sup>3</sup>) + … = 1 − x + 2x<sup>2</sup> − (14/3)x<sup>3</sup> + ….",
       239),
    bq(U, EX3, 'EX7.3', '1(iv)',
       "Find the first four terms in the expansion of √(1 + 2x)/(1 − x).",
       "1 + 2x + (3/2)x<sup>2</sup> + 2x<sup>3</sup> + … (valid if |x| < 1/2)",
       "(1 + 2x)<sup>1/2</sup> = 1 + x − x<sup>2</sup>/2 + x<sup>3</sup>/2 − … and (1 − x)<sup>−1</sup> = 1 + x + x<sup>2</sup> + x<sup>3</sup> + …. Multiplying and collecting terms up to x<sup>3</sup>: constant 1; x: 1 + 1 = 2; x<sup>2</sup>: 1 + 1 − 1/2 = 3/2; x<sup>3</sup>: 1 + 1 − 1/2 + 1/2 = 2. Hence 1 + 2x + (3/2)x<sup>2</sup> + 2x<sup>3</sup> + …. The expansion is valid for |2x| < 1 and |x| < 1, i.e. |x| < 1/2.",
       239),

    bq(U, EX3, 'EX7.3', '2(i)',
       "Find the first negative term in the expansion of (1 + y)<sup>4/3</sup>.",
       "−(4/81)y<sup>3</sup> (the fourth term).",
       "(1 + y)<sup>4/3</sup> = 1 + (4/3)y + [(4/3)(1/3)/2]y<sup>2</sup> + [(4/3)(1/3)(−2/3)/6]y<sup>3</sup> + … = 1 + (4/3)y + (2/9)y<sup>2</sup> − (4/81)y<sup>3</sup> + …. The coefficients are positive until the term in y<sup>3</sup>, whose coefficient 4·1·(−2)/(3·3·3·6) = −4/81 is the first negative one. Hence the first negative term is −(4/81)y<sup>3</sup>.",
       239),
    bq(U, EX3, 'EX7.3', '2(ii)',
       "Find the first negative term in the expansion of (1 + 2x)<sup>5/2</sup>.",
       "−(5/8)x<sup>4</sup> (the fifth term).",
       "(1 + u)<sup>5/2</sup> = 1 + (5/2)u + (15/8)u<sup>2</sup> + (5/16)u<sup>3</sup> − (5/128)u<sup>4</sup> + …, since n(n − 1)/2! = 15/8, n(n − 1)(n − 2)/3! = 5/16 and n(n − 1)(n − 2)(n − 3)/4! = −5/128. With u = 2x: 1 + 5x + (15/2)x<sup>2</sup> + (5/2)x<sup>3</sup> − (5/8)x<sup>4</sup> + …. Thus the first negative term is −(5/8)x<sup>4</sup>.",
       239),

    bq(U, EX3, 'EX7.3', '3(i)',
       "If x is so small that its square and higher powers may be neglected, show that √(1 + (1/4)x) ≈ 1 + (1/8)x.",
       "Proof shown.",
       "√(1 + (1/4)x) = (1 + x/4)<sup>1/2</sup> = 1 + (1/2)(x/4) + [(1/2)(−1/2)/2](x/4)<sup>2</sup> + … = 1 + x/8 − x<sup>2</sup>/128 + …. Neglecting x<sup>2</sup> and higher powers leaves 1 + (1/8)x.",
       239),
    bq(U, EX3, 'EX7.3', '3(ii)',
       "If x is so small that its square and higher powers may be neglected, show that ∜(1 + 8x) ≈ 1 + 2x.",
       "Proof shown.",
       "(1 + 8x)<sup>1/4</sup> = 1 + (1/4)(8x) + [(1/4)(−3/4)/2](8x)<sup>2</sup> + … = 1 + 2x − 6x<sup>2</sup> + …. Neglecting x<sup>2</sup> and higher powers leaves 1 + 2x.",
       239),

    bq(U, EX3, 'EX7.3', '4(i)',
       "Using the binomial series, find √24 up to three places of decimals.",
       "≈ 4.899. (The printed key gives 4.898, which is a truncation of 4.89898.)",
       "√24 = √(25 − 1) = 5(1 − 1/25)<sup>1/2</sup> = 5(1 − 0.04)<sup>1/2</sup> = 5[1 − (1/2)(0.04) − (1/8)(0.04)<sup>2</sup> − (1/16)(0.04)<sup>3</sup> − …] = 5[1 − 0.02 − 0.0002 − 0.000004 − …] = 5(0.979796) = 4.89898 ≈ 4.899.",
       239),
    bq(U, EX3, 'EX7.3', '4(ii)',
       "Using the binomial series, find ∛28 up to three places of decimals.",
       "≈ 3.037. (The printed key gives 3.036, which is a truncation of 3.03659.)",
       "∛28 = ∛(27 + 1) = 3(1 + 1/27)<sup>1/3</sup> = 3[1 + (1/3)(1/27) − (1/9)(1/27)<sup>2</sup> + (5/81)(1/27)<sup>3</sup> − …] = 3[1 + 0.0123457 − 0.0001524 + 0.0000031 − …] = 3(1.0121964) = 3.03659 ≈ 3.037.",
       239),
    bq(U, EX3, 'EX7.3', '4(iii)',
       "Using the binomial series, find <sup>5</sup>√241 up to three places of decimals.",
       "≈ 2.995.",
       "<sup>5</sup>√241 = <sup>5</sup>√(243 − 2) = 3(1 − 2/243)<sup>1/5</sup> = 3[1 − (1/5)(2/243) − (2/25)(2/243)<sup>2</sup> − …] = 3[1 − 0.0016461 − 0.0000054 − …] = 3(0.9983485) = 2.995045 ≈ 2.995.",
       239),
    bq(U, EX3, 'EX7.3', '4(iv)',
       "Using the binomial series, find (1280)<sup>1/4</sup> up to three places of decimals.",
       "≈ 5.981.",
       "1280 = 1296 − 16 = 6<sup>4</sup>(1 − 1/81). Hence (1280)<sup>1/4</sup> = 6(1 − 1/81)<sup>1/4</sup> = 6[1 − (1/4)(1/81) − (3/32)(1/81)<sup>2</sup> − …] = 6[1 − 0.0030864 − 0.0000143 − …] = 6(0.9968993) = 5.98140 ≈ 5.981.",
       239),
    bq(U, EX3, 'EX7.3', '4(v)',
       "Using the binomial series, find 1/<sup>5</sup>√252 up to three places of decimals.",
       "≈ 0.331.",
       "<sup>5</sup>√252 = <sup>5</sup>√(243 + 9) = 3(1 + 1/27)<sup>1/5</sup> = 3[1 + (1/5)(1/27) − (2/25)(1/27)<sup>2</sup> + …] = 3[1 + 0.0074074 − 0.0001097 + …] = 3(1.0072977) = 3.021893. Therefore 1/<sup>5</sup>√252 = 1/3.021893 = 0.330918 ≈ 0.331.",
       239),

    bq(U, EX3, 'EX7.3', '5(i)',
       "Identify the series 1 + 3/4 + (3·5)/(4·8) + (3·5·7)/(4·8·12) + … as a binomial expansion and find its sum.",
       "2√2.",
       "Compare with (1 − x)<sup>−3/2</sup> = 1 + (3/2)x + [(3/2)(5/2)/2!]x<sup>2</sup> + [(3/2)(5/2)(7/2)/3!]x<sup>3</sup> + … = 1 + (3/2)x + (15/8)x<sup>2</sup> + (35/16)x<sup>3</sup> + …. Putting x = 1/2 gives 1 + 3/4 + 15/32 + 35/128 + …, and (3·5)/(4·8) = 15/32, (3·5·7)/(4·8·12) = 35/128. Hence the sum is (1 − 1/2)<sup>−3/2</sup> = (1/2)<sup>−3/2</sup> = 2<sup>3/2</sup> = 2√2.",
       239),
    bq(U, EX3, 'EX7.3', '5(ii)',
       "Identify the series 1 + (1/2)(1/5) − (1/(2!·4))(1/5)<sup>2</sup> + … as a binomial expansion and find its sum.",
       "√(6/5).",
       "This is (1 + x)<sup>n</sup> with x = 1/5. Comparing the first two terms gives nx = 1/10 and n(n − 1)x<sup>2</sup>/2 = −1/200. Dividing the second relation by the first gives (n − 1)x/2 = −1/20, so (n − 1)x = −1/10. With x = 1/(10n) this becomes (n − 1)/(10n) = −1/10, hence n − 1 = −n and n = 1/2, x = 1/5. The coefficient −1/8 = −1/(2!·4) agrees with n(n − 1)/2. Therefore the series is (1 + 1/5)<sup>1/2</sup> = √(6/5).",
       239),
    bq(U, EX3, 'EX7.3', '5(iii)',
       "Identify the series 1 − (1/2)(1/4) + (1·3)/(2!·4)(1/4)<sup>2</sup> − (1·3·5)/(3!·8)(1/4)<sup>3</sup> + … as a binomial expansion and find its sum.",
       "2/√5.",
       "The coefficients 1, −1/2, 3/8, −5/16 are those of (1 + x)<sup>−1/2</sup> = 1 − x/2 + (3/8)x<sup>2</sup> − (5/16)x<sup>3</sup> + …, since (1·3)/(2!·4) = 3/8 and (1·3·5)/(3!·8) = 5/16. With x = 1/4 the sum is (1 + 1/4)<sup>−1/2</sup> = (5/4)<sup>−1/2</sup> = 2/√5.",
       239),
    bq(U, EX3, 'EX7.3', '5(iv)',
       "Identify the series 1 − (1/2)(1/2) + (1·3)/(2·4)(1/2)<sup>2</sup> − (1·3·5)/(2·4·6)(1/2)<sup>3</sup> + … as a binomial expansion and find its sum.",
       "√(2/3).",
       "The series is (1 + x)<sup>−1/2</sup> = 1 − x/2 + (1·3)/(2·4)x<sup>2</sup> − (1·3·5)/(2·4·6)x<sup>3</sup> + … evaluated at x = 1/2. Hence the sum is (1 + 1/2)<sup>−1/2</sup> = (3/2)<sup>−1/2</sup> = √(2/3).",
       239),
    bq(U, EX3, 'EX7.3', '5(v)',
       "Identify the series 1 − (1/2)(1/3) + (1·3)/(2·4)(1/3)<sup>2</sup> − (1·3·5)/(2·4·6)(1/3)<sup>3</sup> + … as a binomial expansion and find its sum.",
       "√3/2.",
       "This is the expansion of (1 + x)<sup>−1/2</sup> with x = 1/3: 1 − x/2 + (1·3)/(2·4)x<sup>2</sup> − (1·3·5)/(2·4·6)x<sup>3</sup> + …. Hence the sum is (1 + 1/3)<sup>−1/2</sup> = (4/3)<sup>−1/2</sup> = √3/2.",
       239),

    bq(U, EX3, 'EX7.3', '6(i)',
       "Use the binomial theorem to show that 1 + 1/4 + (1·3)/(4·8) + (1·3·5)/(4·8·12) + … = √2.",
       "Proof shown; the sum is √2.",
       "Take (1 − x)<sup>−1/2</sup> = 1 + (1/2)x + (1·3)/(2·4)x<sup>2</sup> + (1·3·5)/(2·4·6)x<sup>3</sup> + …. At x = 1/2 this becomes 1 + 1/4 + (1·3)/(2·4)·(1/4) + (1·3·5)/(2·4·6)·(1/8) + … = 1 + 1/4 + 3/32 + 5/128 + …, and 3/32 = (1·3)/(4·8), 5/128 = (1·3·5)/(4·8·12). Therefore the sum is (1 − 1/2)<sup>−1/2</sup> = (1/2)<sup>−1/2</sup> = √2.",
       239),
    bq(U, EX3, 'EX7.3', '6(ii)',
       "Use the binomial theorem to show that 1 + 1/4 + (1·3)/(4·6) + (1·3·5)/(4·6·8) + … = ∛4.",
       "Proof shown; the sum is ∛4.",
       "Write (1 − x)<sup>−1/3</sup> = 1 + (1/3)x + (2/9)x<sup>2</sup> + (14/81)x<sup>3</sup> + …, where (1/3)(4/3)/2 = 2/9 and (1/3)(4/3)(7/3)/6 = 14/81. At x = 3/4 the first terms are 1 + 1/4 + (2/9)(9/16) + (14/81)(27/64) + … = 1 + 1/4 + 1/8 + 7/96 + …. Thus the series is (1 − 3/4)<sup>−1/3</sup> = (1/4)<sup>−1/3</sup> = 4<sup>1/3</sup> = ∛4. (The printed fourth term (1·3·5)/(4·6·8) = 5/64 is a misprint; the correct value is 7/96, since the first two terms already force n = −1/3 and x = 3/4.)",
       239),

    bq(U, EX3, 'EX7.3', '7',
       "If y = (1/2)(1/16) − (1/(2!·4))(1/16)<sup>2</sup> + (1/3!)((1·3)/8)(1/16)<sup>3</sup> − …, then show that 16y(y + 2) = 1.",
       "Proof shown.",
       "The series is the binomial expansion of (1 + x)<sup>1/2</sup> − 1 = (1/2)x − (1/8)x<sup>2</sup> + (1/16)x<sup>3</sup> − … at x = 1/16, because 1/(2!·4) = 1/8 and (1/3!)((1·3)/8) = 1/16. Hence y = √(1 + 1/16) − 1 = √17/4 − 1 = (√17 − 4)/4. Then y + 2 = (√17 + 4)/4 and 16y(y + 2) = 16·[(√17 − 4)(√17 + 4)/16] = 17 − 16 = 1.",
       239),
    bq(U, EX3, 'EX7.3', '8',
       "If 1/x = 2/5 + ((1·3)/2!)(2/5)<sup>2</sup> + ((1·3·5)/3!)(2/5)<sup>3</sup> + …, then show that 4x<sup>2</sup> − 2x − 1 = 0.",
       "Proof shown.",
       "The series is (1 − 4/5)<sup>−1/2</sup> − 1 = 1 + (1/2)(4/5) + (3/8)(4/5)<sup>2</sup> + (5/16)(4/5)<sup>3</sup> + … − 1, since (1/2)(4/5) = 2/5, (3/8)(16/25) = (3/2)(4/25) = (1·3)/2!·(2/5)<sup>2</sup> and (5/16)(64/125) = (15/6)(8/125) = (1·3·5)/3!·(2/5)<sup>3</sup>. Hence 1/x = (1/5)<sup>−1/2</sup> − 1 = √5 − 1, so x = 1/(√5 − 1) = (√5 + 1)/4. Then x<sup>2</sup> = (3 + √5)/8, so 4x<sup>2</sup> − 2x − 1 = (3 + √5)/2 − (√5 + 1)/2 − 1 = 1 − 1 = 0.",
       239),
    bq(U, EX3, 'EX7.3', '9',
       "If y/2 = (1/2)(4/9) + ((1·3)/(2<sup>2</sup>·2!))(4/9)<sup>2</sup> + ((1·3·5)/(2<sup>3</sup>·3!))(4/9)<sup>3</sup> + …, then show that 5y<sup>2</sup> + 20y − 16 = 0.",
       "Proof shown.",
       "The right side is (1 − 4/9)<sup>−1/2</sup> − 1 = (1/2)(4/9) + (3/8)(4/9)<sup>2</sup> + (5/16)(4/9)<sup>3</sup> + …, and (3/8)(16/81) = 3/(4·2)·(16/81) = (1·3)/(2<sup>2</sup>·2!)·(4/9)<sup>2</sup>, (5/16)(64/729) = 15/(8·6)·(64/729) = (1·3·5)/(2<sup>3</sup>·3!)·(4/9)<sup>3</sup>. Hence y/2 = (5/9)<sup>−1/2</sup> − 1 = 3/√5 − 1, so y = 6/√5 − 2. Then 5y<sup>2</sup> = 5(36/5 − 24/√5 + 4) = 56 − 24√5 and 20y = 120/√5 − 40 = 24√5 − 40, so 5y<sup>2</sup> + 20y − 16 = (56 − 24√5) + (24√5 − 40) − 16 = 0.",
       240),
]

# ============================================================ Review Exercise 7 (pdf 240-241)
ITEMS += [
    mcq(U, REV, 'REV7', 'i',
        "The general term of the binomial expansion (a + x)<sup>n</sup>, where n ∈ ℕ, is:",
        ["<sup>n</sup>C<sub>r</sub> a<sup>n</sup>x",
         "<sup>n</sup>C<sub>r</sub> a<sup>n−r</sup>x<sup>r</sup>",
         "<sup>n</sup>C<sub>r</sub> a<sup>r</sup>x<sup>n−r</sup>",
         "<sup>n</sup>C<sub>r</sub> (ax)<sup>n−r</sup>"],
        'b',
        "In (a + x)<sup>n</sup> the powers of a decrease from n to 0 while those of x increase from 0 to n, so T<sub>r+1</sub> = <sup>n</sup>C<sub>r</sub> a<sup>n−r</sup>x<sup>r</sup>.",
        240),
    mcq(U, REV, 'REV7', 'ii',
        "The number of terms in the expansion of (a + b)<sup>2n</sup> are:",
        ["n", "2n + 1", "2<sup>n</sup>", "2<sup>n−1</sup>"],
        'b',
        "The expansion of (a + b)<sup>m</sup> has m + 1 terms. With m = 2n this gives 2n + 1 terms.",
        240),
    mcq(U, REV, 'REV7', 'iii',
        "In the expansion (a + x)<sup>n</sup>, the exponent of x:",
        ["decreases from n to 0", "increases from 0 to n", "remains n every where", "becomes 0 at the end"],
        'b',
        "The successive terms are a<sup>n</sup>, <sup>n</sup>C<sub>1</sub>a<sup>n−1</sup>x, …, x<sup>n</sup>, so the exponent of x starts at 0 and increases by 1 up to n.",
        240),
    mcq(U, REV, 'REV7', 'iv',
        "Middle term in the expansion of (a + b)<sup>2n</sup> is:",
        ["nth term", "(n + 1)th term", "(2n + 1)th term", "(2n − 1)th term"],
        'b',
        "(a + b)<sup>2n</sup> has 2n + 1 terms, so the single middle term is the (n + 1)th term.",
        240),
    mcq(U, REV, 'REV7', 'v',
        "The term independent of x in the expansion of (a + 2x)<sup>n</sup> is:",
        ["First term", "Middle term", "Last term", "2<sup>nd</sup> last term"],
        'a',
        "The general term <sup>n</sup>C<sub>r</sub>a<sup>n−r</sup>(2x)<sup>r</sup> contains x<sup>r</sup>. It is independent of x only when r = 0, which gives the first term a<sup>n</sup>.",
        240),
    mcq(U, REV, 'REV7', 'vi',
        "The coefficient of the last term in the expansion of (2 − x)<sup>7</sup> is/are:",
        ["1", "−1", "7", "−7"],
        'b',
        "The last term is (−x)<sup>7</sup> = −x<sup>7</sup>, whose coefficient is −1.",
        240),
    mcq(U, REV, 'REV7', 'vii',
        "In the expansion (a + 1/2)<sup>7</sup>, the number of middle terms is/are:",
        ["one", "two", "three", "four"],
        'b',
        "n = 7 is odd, so the expansion has 8 terms and therefore two middle terms, the 4th and the 5th.",
        240),
    mcq(U, REV, 'REV7', 'viii',
        "Sum of odd binomial coefficients in the expansion of (a + x)<sup>n</sup> is:",
        ["2<sup>n</sup>", "2<sup>n−1</sup>", "2<sup>n+1</sup>", "n + 1"],
        'b',
        "Adding and subtracting (1 + 1)<sup>n</sup> and (1 − 1)<sup>n</sup> gives the sum of the odd coefficients as 2<sup>n</sup>/2 = 2<sup>n−1</sup>.",
        240),
    mcq(U, REV, 'REV7', 'ix',
        "<sup>n+1</sup>C<sub>0</sub> + <sup>n+1</sup>C<sub>1</sub> + <sup>n+1</sup>C<sub>2</sub> + … + <sup>n+1</sup>C<sub>n+1</sub> is equal to:",
        ["2<sup>n</sup>", "2<sup>n+1</sup>", "2<sup>n−1</sup>", "Cannot be determined"],
        'b',
        "This is the sum of all binomial coefficients of (1 + 1)<sup>n+1</sup>, which equals 2<sup>n+1</sup>.",
        240),
    mcq(U, REV, 'REV7', 'x',
        "The number of terms in the expansion of (1 + x)<sup>1/3</sup> is ______.",
        ["4/3", "4", "∞", "2"],
        'c',
        "The index 1/3 is not a positive integer, so the binomial expansion is an infinite series with infinitely many terms.",
        240),
    mcq(U, REV, 'REV7', 'xi',
        "1 − x + x<sup>2</sup> − x<sup>3</sup> + … is equal to:",
        ["(1 + x)<sup>−1</sup>", "(1 − x)<sup>−1</sup>", "(1 + x)<sup>−2</sup>", "(1 − x)<sup>−2</sup>"],
        'a',
        "(1 + x)<sup>−1</sup> = 1 − x + x<sup>2</sup> − x<sup>3</sup> + … for |x| < 1, which is exactly the given series.",
        240),
    mcq(U, REV, 'REV7', 'xii',
        "The expansion of (1 − 2x)<sup>−2</sup> is valid if:",
        ["|x| < 0", "|x| < 1/2", "|x| < 2", "|x| < 1"],
        'b',
        "The binomial series for (1 + u)<sup>n</sup> converges for |u| < 1. Here u = −2x, so |−2x| < 1, i.e. |x| < 1/2.",
        240),
    mcq(U, REV, 'REV7', 'xiii',
        "The middle term in the expansion of (a + b)<sup>n</sup> is (n/2 + 1)th term; then n is:",
        ["Odd", "Even", "Prime", "None of these"],
        'b',
        "A single middle term occurs only when the number of terms n + 1 is odd, i.e. n is even. Then the middle term is the (n/2 + 1)th term.",
        241),
    mcq(U, REV, 'REV7', 'xiv',
        "In (a + 1/a)<sup>8</sup>, the sum of the binomial coefficients is:",
        ["64", "128", "256", "512"],
        'c',
        "The sum of the binomial coefficients of (a + b)<sup>n</sup> is 2<sup>n</sup> (put a = b = 1). Here n = 8, so the sum is 2<sup>8</sup> = 256.",
        241),

    bq(U, REV, 'REV7', '2',
       "Prove by the principle of mathematical induction that 8 × 10<sup>n</sup> − 2 is divisible by 6 for all n ∈ ℕ.",
       "Proof shown.",
       "<b>Basis</b> (n = 1): 8 × 10 − 2 = 78 = 6 × 13, so P(1) is true. "
       "<b>Hypothesis</b>: 8 × 10<sup>k</sup> − 2 = 6m for some integer m. "
       "<b>Step</b>: 8 × 10<sup>k+1</sup> − 2 = 10(8 × 10<sup>k</sup>) − 2 = 10(6m + 2) − 2 = 60m + 18 = 6(10m + 3), which is divisible by 6, so P(k + 1) is true. "
       "<b>Conclusion</b>: by induction 8 × 10<sup>n</sup> − 2 is divisible by 6 for every n ∈ ℕ.",
       241),
    bq(U, REV, 'REV7', '3',
       "Prove by mathematical induction: 1<sup>2</sup> + 3<sup>2</sup> + 5<sup>2</sup> + … + (2n − 1)<sup>2</sup> = (1/3)n(2n − 1)(2n + 1).",
       "Proof shown.",
       "<b>Basis</b> (n = 1): LHS = 1 and RHS = (1/3)(1)(1)(3) = 1, so P(1) is true. "
       "<b>Hypothesis</b>: 1<sup>2</sup> + 3<sup>2</sup> + … + (2k − 1)<sup>2</sup> = (1/3)k(2k − 1)(2k + 1). "
       "<b>Step</b>: add the next odd square (2k + 1)<sup>2</sup>: (1/3)k(4k<sup>2</sup> − 1) + (2k + 1)<sup>2</sup> = (2k + 1)[k(2k − 1)/3 + (2k + 1)] = (2k + 1)(2k<sup>2</sup> + 5k + 3)/3 = (2k + 1)(k + 1)(2k + 3)/3 = (1/3)(k + 1)(2(k + 1) − 1)(2(k + 1) + 1), which is P(k + 1). "
       "<b>Conclusion</b>: the formula holds for every positive integer n.",
       241),
    bq(U, REV, 'REV7', '4',
       "Given that the coefficient of y<sup>2</sup> in the expansion of 1/(1 + my)<sup>2</sup> is 96, find m.",
       "m = ±4√2.",
       "1/(1 + my)<sup>2</sup> = (1 + my)<sup>−2</sup> = 1 − 2my + [(−2)(−3)/2](my)<sup>2</sup> − … = 1 − 2my + 3m<sup>2</sup>y<sup>2</sup> − …. Hence 3m<sup>2</sup> = 96, m<sup>2</sup> = 32 and m = ±√32 = ±4√2.",
       241),
    bq(U, REV, 'REV7', '5',
       "Given that terms involving m<sup>4</sup> and higher powers may be neglected and that 1/(a + bm)<sup>3</sup> − 1/(1 + 3m)<sup>4</sup> = cm<sup>2</sup> + dm<sup>3</sup>, find the values of a, b, c and d.",
       "a = 1, b = 4, c = 6, d = −100.",
       "1/(a + bm)<sup>3</sup> = a<sup>−3</sup>(1 + (b/a)m)<sup>−3</sup> ≈ a<sup>−3</sup>[1 − 3(b/a)m + 6(b/a)<sup>2</sup>m<sup>2</sup> − 10(b/a)<sup>3</sup>m<sup>3</sup>] and 1/(1 + 3m)<sup>4</sup> = (1 + 3m)<sup>−4</sup> ≈ 1 − 12m + 90m<sup>2</sup> − 540m<sup>3</sup>. The difference has no constant term, so a<sup>−3</sup> = 1 and a = 1. The coefficient of m must vanish: −3b + 12 = 0, so b = 4. Then c = 6b<sup>2</sup> − 90 = 96 − 90 = 6 and d = −10b<sup>3</sup> + 540 = −640 + 540 = −100. Check: (1 + 4m)<sup>−3</sup> − (1 + 3m)<sup>−4</sup> = (1 − 12m + 96m<sup>2</sup> − 640m<sup>3</sup>) − (1 − 12m + 90m<sup>2</sup> − 540m<sup>3</sup>) = 6m<sup>2</sup> − 100m<sup>3</sup>.",
       241),
]

