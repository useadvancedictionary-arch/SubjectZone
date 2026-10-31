"""Builds public/data/class_xii_math.json for the SubjectZone app.

Sources:
  - Unit page ranges: visually verified inventory of Math XII (Sindh Textbook Board), PDF pp. 5-412.
  - Solved questions: appended here exercise-by-exercise as solutions are completed
    (mirrors Solutions/Unit NN/*.md). Book page = PDF page - 4.
"""
import json
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'class_xii_math.json')

UNITS = [
    (1,  'Introduction to Symbolic Package: MAPLE', 5,   23,  1,   19),
    (2,  'Functions and Limits',                    24,  61,  20,  57),
    (3,  'Differentiation',                         62,  106, 58,  102),
    (4,  'Higher Order Derivatives and Applications', 107, 136, 103, 132),
    (5,  'Differentiation of Vector Functions',     137, 151, 133, 147),
    (6,  'Integration',                             152, 195, 148, 191),
    (7,  'Plane Analytic Geometry: Straight Line',  196, 244, 192, 240),
    (8,  'Circle',                                  245, 277, 241, 273),
    (9,  'Parabola, Ellipse and Hyperbola',         278, 354, 274, 350),
    (10, 'Differential Equations',                  355, 378, 351, 374),
    (11, 'Partial Differentiation',                 379, 391, 375, 387),
    (12, 'Introduction to Numerical Methods',       392, 412, 388, 408),
]
TOTAL_PAGES = 440  # pp. 413-440 = Answers key (book pp. 409-436)


def q(qid, unit, section, code, number, question, answer, explanation, pdf_page, figure=None):
    item = {
        'id': qid, 'chapter': unit, 'section': section, 'sectionCode': code,
        'type': 'sq', 'number': number, 'question': question, 'answer': answer,
        'explanation': explanation, 'pdfPage': pdf_page, 'bookPage': pdf_page - 4,
    }
    if figure:
        item['figure'] = figure
    return item


EX1 = 'Exercise 1'
SOLVED = [
    q('u1_ex1_q1', 1, EX1, 'EX1', 1,
      'Expand the following expressions using the <b>expand</b> command in Maple: '
      '(i) (x + y)&sup3;  (ii) cos(x + y) + sin(x &minus; y)  (iii) (2a &minus; b)&sup2; + (a + 3b)&sup2;  '
      '(iv) eˣ(x + y) &minus; eˣ(x &minus; y)  (v) (x + 2)(x &minus; 3)  (vi) sqrt(x + y)',
      '(i) x&sup3; + 3x&sup2;y + 3xy&sup2; + y&sup3;<br>(ii) cos(x)cos(y) &minus; sin(x)sin(y) + sin(x)cos(y) &minus; cos(x)sin(y)<br>'
      '(iii) 5a&sup2; + 2ab + 10b&sup2;<br>(iv) 2eˣy<br>(v) x&sup2; &minus; x &minus; 6<br>(vi) &radic;(x + y) &mdash; unchanged',
      'expand distributes products/powers and applies sum formulae: binomial theorem in (i); addition formulae cos(x+y) and sin(x&minus;y) in (ii); '
      '(iii) (4a&sup2;&minus;4ab+b&sup2;)+(a&sup2;+6ab+9b&sup2;); (iv) eˣ[(x+y)&minus;(x&minus;y)] = 2yeˣ; (vi) a sum under a radical has no expansion rule, so Maple returns it as is.',
      23),
    q('u1_ex1_q2', 1, EX1, 'EX1', 2,
      'Use the <b>factor</b> command in Maple to factorize: (i) x&sup3; &minus; 8  (ii) x&#8308; &minus; y&#8308;  (iii) x&sup2; &minus; 4  '
      '(iv) 3x&sup3; + 12x&sup2; &minus; 15x  (v) 2x&sup2; + 6xy + 4y&sup2;  (vi) x&sup2; + 4x + 4',
      '(i) (x &minus; 2)(x&sup2; + 2x + 4)<br>(ii) (x &minus; y)(x + y)(x&sup2; + y&sup2;)<br>(iii) (x &minus; 2)(x + 2)<br>'
      '(iv) 3x(x + 5)(x &minus; 1)<br>(v) 2(x + 2y)(x + y)<br>(vi) (x + 2)&sup2;',
      'factor reverses expansion over the rationals: (i) difference of cubes a&sup3;&minus;b&sup3;; (ii) difference of squares applied twice; '
      '(iv) take 3x common then split x&sup2;+4x&minus;5; (v) take 2 common then split x&sup2;+3xy+2y&sup2;; (vi) perfect square trinomial.',
      23),
    q('u1_ex1_q3', 1, EX1, 'EX1', 3,
      'Simplify using the <b>simplify</b> command in Maple: (i) (x&sup2;+2x+1)/(x+1)  (ii) (x&sup3;&minus;x&sup2;&minus;x+1)/(x&sup2;+1)  '
      '(iii) sin(x)&sup2; + cos(x)&sup2;  (iv) (3x&sup2;+2x&minus;1)/(x&sup2;+1)',
      '(i) x + 1<br>(ii) (x+1)(x&minus;1)&sup2; / (x&sup2;+1)<br>(iii) 1<br>(iv) (3x&sup2;+2x&minus;1)/(x&sup2;+1) &mdash; unchanged',
      '(i) numerator = (x+1)&sup2;, one factor cancels; (ii) numerator = x&sup2;(x&minus;1)&minus;(x&minus;1) = (x&minus;1)(x&sup2;&minus;1) = (x&minus;1)&sup2;(x+1), '
      'nothing cancels with x&sup2;+1; (iii) Pythagorean identity; (iv) numerator (3x&minus;1)(x+1) shares no factor with x&sup2;+1.',
      23),
    q('u1_ex1_q4', 1, EX1, 'EX1', 4,
      'Evaluate the numerical value of sin(&pi;/6) using the <b>evalf</b> command in Maple.',
      '0.5',
      'sin(Pi/6) stays exact (= 1/2) symbolically; evalf forces floating-point evaluation, giving 0.5.',
      23),
    q('u1_ex1_q5', 1, EX1, 'EX1', 5,
      'Find the inverse of the matrix A := Matrix(2, [1, 2, 3, 4]) using the Matrix Inverse command in Maple. '
      '(Run with(LinearAlgebra): first.)',
      'A&sup1;&nbsp;= [&minus;2, 1; 3/2, &minus;1/2] i.e. row 1: &minus;2, 1 &mdash; row 2: 3/2, &minus;1/2',
      'A = [[1,2],[3,4]]; det A = 1&middot;4 &minus; 2&middot;3 = &minus;2; A&sup1; = (1/det)&middot;[[4,&minus;2],[&minus;3,1]]. Command: MatrixInverse(A).',
      23),
    q('u1_ex1_q6', 1, EX1, 'EX1', 6,
      'Find the transpose of the matrix B := Matrix(2, 3, [1, 2, 3, 4, 5, 6]) using the Transpose command in Maple. '
      '(Run with(LinearAlgebra): first.)',
      'B&#11388; = [1, 4; 2, 5; 3, 6] i.e. row 1: 1, 4 &mdash; row 2: 2, 5 &mdash; row 3: 3, 6',
      'B is 2&times;3 = [[1,2,3],[4,5,6]]; Transpose swaps rows and columns giving a 3&times;2 matrix. Command: Transpose(B).',
      23),
    q('u1_ex1_q7', 1, EX1, 'EX1', 7,
      'Perform matrix multiplication for matrices A := Matrix(2, [1, 2, 3, 4]) and B := Matrix(2, [5, 6, 7, 8]) using the command in Maple. '
      '(Run with(LinearAlgebra): first.)',
      'A.B = [19, 22; 43, 50] i.e. row 1: 19, 22 &mdash; row 2: 43, 50',
      'Row-by-column products: (1,1)=1&middot;5+2&middot;7=19; (1,2)=1&middot;6+2&middot;8=22; (2,1)=3&middot;5+4&middot;7=43; (2,2)=3&middot;6+4&middot;8=50. Command: A.B',
      23),
    q('u1_ex1_q8', 1, EX1, 'EX1', 8,
      'Plot the functions f(x) = x&sup2; and g(x) = 2x &minus; 1 on the same graph in the range [&minus;5, 5].',
      'Maple command: plot([x^2, 2*x-1], x = -5..5); &mdash; a parabola through the origin together with a straight line of slope 2, '
      'tangent to it at (1, 1). See the generated graph in the solution notes.',
      'plot accepts a list of expressions to draw several curves in one window; x&sup2; = 2x&minus;1 &rArr; (x&minus;1)&sup2; = 0, so the line touches the parabola only at x = 1.',
      23),
    q('u1_ex1_q9', 1, EX1, 'EX1', 9,
      'Generate a graph that includes the functions h(x) = sin(x) and k(x) = cos(x) in the interval [0, 2&pi;].',
      'Maple command: plot([sin(x), cos(x)], x = 0..2*Pi); &mdash; two unit-amplitude waves phase-shifted by &pi;/2: '
      'sin starts at 0 and cos starts at 1; they cross at x = &pi;/4 and x = 5&pi;/4.',
      'Both curves have amplitude 1 and period 2&pi;; cos(x) = sin(x + &pi;/2), which is the visible horizontal shift between the two waves.',
      23),
    q('u1_ex1_q10', 1, EX1, 'EX1', 10,
      'Plot the parametric curves x(t) = cos(2t) and y(t) = sin(3t) for t in the range [&minus;2&pi;, 2&pi;].',
      'Maple command: plot([cos(2*t), sin(3*t), t = -2*Pi..2*Pi]); &mdash; a closed Lissajous figure inside the square [&minus;1,1]&times;[&minus;1,1].',
      'The third list entry makes Maple plot parametrically (x(t), y(t)); frequency ratio 2:3 with periods dividing 4&pi; makes the curve close on itself.',
      23),
]

EX2_1 = 'Exercise 2.1'
SOLVED += [
    q('u2_ex21_q1', 2, EX2_1, 'EX2.1', 1,
      'Identify the domain and range of the functions through the following graphs (figure below): '
      '(i) parabola y = x&sup2; with vertex at the origin, opening upward  (ii) straight line y = x through the origin  '
      '(iii) curve y = &radic;x starting at the origin  (iv) curve y = 1/x&sup2; (two branches above the x-axis)  '
      '(v) curve y = 1/x (branches in the first and third quadrants).',
      '(i) Domain = &#8477;; Range = {y &isin; &#8477; : y &ge; 0}<br>(ii) Domain = &#8477;; Range = &#8477;<br>'
      '(iii) Domain = {x &isin; &#8477; : x &ge; 0}; Range = {y &isin; &#8477; : y &ge; 0}<br>'
      '(iv) Domain = {x &isin; &#8477; : x &ne; 0}; Range = {y &isin; &#8477; : y > 0}<br>'
      '(v) Domain = {x &isin; &#8477; : x &ne; 0}; Range = {y &isin; &#8477; : y &ne; 0}',
      'Domain = horizontal extent of the curve, range = vertical extent: (i) the parabola spans all x and its lowest point is y = 0; '
      '(ii) the line covers the whole plane; (iii) &radic;x exists only for x &ge; 0 and starts at y = 0; '
      '(iv) a gap at x = 0 and both branches lie strictly above the x-axis; (v) a gap at x = 0 and y = 0 is never attained.',
      27, figure='/figures/math_xii/ex21_q1_graphs.png'),
    q('u2_ex21_q2', 2, EX2_1, 'EX2.1', 2,
      'If f(x) = 5x + 2 and g(x) = 2x&sup2; &minus; 3, then find: (i) fog  (ii) gof  (iii) fof  (iv) gog',
      '(i) 10x&sup2; &minus; 13<br>(ii) 50x&sup2; + 40x + 5<br>(iii) 25x + 12<br>(iv) 8x&#8308; &minus; 24x&sup2; + 15',
      'Substitute the inner function into the outer one: (i) 5(2x&sup2;&minus;3)+2; (ii) 2(5x+2)&sup2;&minus;3 = 2(25x&sup2;+20x+4)&minus;3; '
      '(iii) 5(5x+2)+2; (iv) 2(2x&sup2;&minus;3)&sup2;&minus;3 = 2(4x&#8308;&minus;12x&sup2;+9)&minus;3.',
      27),
    q('u2_ex21_q3', 2, EX2_1, 'EX2.1', 3,
      'If f(x) = 2x and g(x) = x + 1, then find fog(x) for x = &minus;5.',
      '&minus;8',
      '(fog)(x) = f(g(x)) = 2(x + 1) = 2x + 2; at x = &minus;5: 2(&minus;5) + 2 = &minus;8.',
      27),
    q('u2_ex21_q4', 2, EX2_1, 'EX2.1', 4,
      'If f(x) = x + 3 and g(x) = x&sup2;, then find gof(x) for x = 1.',
      '16',
      '(gof)(x) = g(f(x)) = (x + 3)&sup2;; at x = 1: (1 + 3)&sup2; = 16.',
      27),
    q('u2_ex21_q5', 2, EX2_1, 'EX2.1', 5,
      'If c(x) = cos x and p(x) = x&sup3; + 1, then find poc(x).',
      'cos&sup3;x + 1',
      '(poc)(x) = p(c(x)) = (cos x)&sup3; + 1 = cos&sup3;x + 1.',
      27),
    q('u2_ex21_q6', 2, EX2_1, 'EX2.1', 6,
      'If f(x) = x + 2 and g(x) = 3x &minus; 2, then find (fog)&#8315;&sup1; and (gof)&#8315;&sup1;, '
      'and show that (gof)&#8315;&sup1; = f&#8315;&sup1;og&#8315;&sup1;.',
      '(fog)&#8315;&sup1; = x/3 ; (gof)&#8315;&sup1; = (x &minus; 4)/3<br>'
      'Shown: f&#8315;&sup1;(x) = x &minus; 2 and g&#8315;&sup1;(x) = (x + 2)/3 &rArr; '
      '(f&#8315;&sup1;og&#8315;&sup1;)(x) = (x + 2)/3 &minus; 2 = (x &minus; 4)/3 = (gof)&#8315;&sup1;(x).',
      'fog(x) = (3x&minus;2)+2 = 3x and gof(x) = 3(x+2)&minus;2 = 3x+4; invert each by solving y = &hellip; for x. '
      'The inverse of a composition reverses the order of the factors, which the f&#8315;&sup1;og&#8315;&sup1; computation confirms.',
      28),
    q('u2_ex21_q7', 2, EX2_1, 'EX2.1', 7,
      'If h(x) = x &minus; 3 and k(x) = 2x + 5, then verify: (i) hok &ne; koh  '
      '(ii) (hok)&#8315;&sup1; = k&#8315;&sup1;oh&#8315;&sup1;  (iii) (koh)&#8315;&sup1; = h&#8315;&sup1;ok&#8315;&sup1;',
      '(i) hok = 2x + 2 while koh = 2x &minus; 1 &rArr; hok &ne; koh<br>'
      '(ii) (hok)&#8315;&sup1; = (x &minus; 2)/2 = k&#8315;&sup1;(h&#8315;&sup1;(x)) &mdash; verified<br>'
      '(iii) (koh)&#8315;&sup1; = (x + 1)/2 = h&#8315;&sup1;(k&#8315;&sup1;(x)) &mdash; verified',
      'hok(x) = (2x+5)&minus;3 = 2x+2 and koh(x) = 2(x&minus;3)+5 = 2x&minus;1, so the two orders differ. '
      'With h&#8315;&sup1;(x) = x+3 and k&#8315;&sup1;(x) = (x&minus;5)/2: k&#8315;&sup1;oh&#8315;&sup1; = ((x+3)&minus;5)/2 = (x&minus;2)/2 '
      'and h&#8315;&sup1;ok&#8315;&sup1; = (x&minus;5)/2+3 = (x+1)/2, matching the inverses obtained directly from hok and koh.',
      28),
]

EX2_2 = 'Exercise 2.2'
SOLVED += [
    q('u2_ex22_q1', 2, EX2_2, 'EX2.2', 1,
      'Which of the following are algebraic, exponential, logarithmic, trigonometric, inverse trigonometric, '
      'hyperbolic and inverse hyperbolic functions: (i) y = x&sup2; + 5x + 6  (ii) f(x) = tan&#8315;&sup1;x  '
      '(iii) y = 2^(x+1)  (iv) y = log&#8325;(x + 2)  (v) f(x) = 3sin x  (vi) y = a^(sin x)  '
      '(vii) f(x) = (x&sup2; + 5x + 7)/(x + 9)  (viii) f(x) = sin x / sec x  (ix) y = log&#8345; sin x  '
      '(x) f(x) = cosec&#8315;&sup1;&radic;(x&sup2; &minus; 1)  (xi) f(x) = tan(sin x)  (xii) y = x/(x + 3)  '
      '(xiii) f(x) = sinh x  (xiv) y = ln cosh x  (xv) y = tanh&#8315;&sup1;x  (xvi) y = cos&#8315;&sup1;(ln x)',
      '(i) algebraic<br>(ii) inverse trigonometric<br>(iii) exponential<br>(iv) logarithmic<br>(v) trigonometric<br>'
      '(vi) exponential<br>(vii) algebraic<br>(viii) trigonometric<br>(ix) logarithmic<br>(x) inverse trigonometric<br>'
      '(xi) trigonometric<br>(xii) algebraic<br>(xiii) hyperbolic<br>(xiv) logarithmic<br>(xv) inverse hyperbolic<br>'
      '(xvi) inverse trigonometric',
      'Classify by the dominant operation: polynomials and ratios of polynomials are algebraic; a variable exponent '
      'with constant base is exponential ((iii), (vi)); a log of an expression is logarithmic ((iv), (ix), (xiv)); '
      'sin/cos/tan/sec compositions are trigonometric ((v), (viii), (xi)); tan&#8315;&sup1;, cosec&#8315;&sup1;, cos&#8315;&sup1; '
      'are inverse trigonometric ((ii), (x), (xvi)); sinh is hyperbolic ((xiii)); tanh&#8315;&sup1; is inverse hyperbolic ((xv)).',
      38),
    q('u2_ex22_q2', 2, EX2_2, 'EX2.2', 2,
      'Identify whether y is the explicit or implicit function of the independent variable x: '
      '(i) xy&sup2; + 5xy + 7 = 0  (ii) y = 3x&sup2; &minus; 3x + 5  (iii) yx&sup2; + y&sup2;x = 3 &minus; 5y  '
      '(iv) x&sup2; + xy&sup2; = 2 + 3xy  (v) y = (x + 3)/(x&sup2; + 5)  (vi) x/y = 3x&sup3;y &minus; 5',
      '(i) implicit function<br>(ii) explicit function<br>(iii) implicit function<br>(iv) implicit function<br>'
      '(v) explicit function<br>(vi) implicit function',
      'y is explicit only when the equation is already solved for y in terms of x alone ((ii), (v)); '
      'wherever y remains mixed with x or un-isolated ((i), (iii), (iv), (vi)) the function is implicit.',
      39),
    q('u2_ex22_q3', 2, EX2_2, 'EX2.2', 3,
      'Draw the graph of the following functions: (i) f(x) = e^(3x)  (ii) f(x) = 3log&#8321;&#8320;x  '
      '(iii) y = &radic;(36 &minus; x&sup2;)  (iv) x&sup2;/16 + y&sup2;/25 = 1',
      'See the four plotted curves in the figure: (i) exponential through (0, 1) hugging y = 0 on the left; '
      '(ii) log curve for x > 0 crossing the x-axis at 1; (iii) upper half of the circle centre O radius 6; '
      '(iv) ellipse with semi-axes 4 (x) and 5 (y).',
      '(iii) squaring gives x&sup2; + y&sup2; = 36 with y &ge; 0 &mdash; a semicircle; (iv) is the standard ellipse '
      'x&sup2;/4&sup2; + y&sup2;/5&sup2; = 1. MAPLE: plot(exp(3*x), x=-1..1.2); plot(3*log10(x), x=0..9); '
      'plot(sqrt(36-x^2), x=-6..6); implicitplot(x^2/16+y^2/25=1, ...).',
      39, figure='/figures/math_xii/ex22_q3.png'),
    q('u2_ex22_q4', 2, EX2_2, 'EX2.2', 4,
      'Draw the graph of the parametric equations of function x = at&sup2;, y = 2at, when a = 4 and &minus;5 &le; t &le; 5.',
      'A right-opening parabola y&sup2; = 16x from (100, &minus;40) through the vertex (0, 0) to (100, 40) &mdash; see figure.',
      'With a = 4: x = 4t&sup2;, y = 8t; eliminating t (t = y/8) gives x = y&sup2;/16, i.e. y&sup2; = 16x. '
      'MAPLE: plot([4*t^2, 8*t, t = -5..5]);',
      39, figure='/figures/math_xii/ex22_q4.png'),
    q('u2_ex22_q5', 2, EX2_2, 'EX2.2', 5,
      'Draw the graph of the parametric equations of function x = a sec &theta;, y = b tan &theta;, '
      'when a = 3, b = 4 and &minus;&pi; &le; &theta; &le; &pi;.',
      'The hyperbola x&sup2;/9 &minus; y&sup2;/16 = 1: two branches opening left/right with vertices (&plusmn;3, 0) '
      'and asymptotes y = &plusmn;(4/3)x &mdash; see figure.',
      'sec&sup2;&theta; &minus; tan&sup2;&theta; = 1 turns the parametrisation into (x/3)&sup2; &minus; (y/4)&sup2; = 1. '
      '&theta; &isin; (&minus;&pi;/2, &pi;/2) traces the right branch, the remaining intervals the left branch. '
      'MAPLE: plot([3*sec(t), 4*tan(t), t = -Pi..Pi], discont = true);',
      39, figure='/figures/math_xii/ex22_q5.png'),
    q('u2_ex22_q6', 2, EX2_2, 'EX2.2', 6,
      'Draw the graph of f(x) = x&sup2; for x &le; 1 and f(x) = 2x for x > 1.',
      'Parabola y = x&sup2; up to the closed point (1, 1), then the line y = 2x starting from the open point (1, 2) '
      '&mdash; a jump of 1 at x = 1; see figure.',
      'Each piece is drawn on its own interval; at x = 1 the first piece gives 1 (included) while the second piece '
      'would give 2 (excluded), so the curve breaks there. MAPLE: plot(piecewise(x <= 1, x^2, 2*x), x = -3..4);',
      39, figure='/figures/math_xii/ex22_q6.png'),
]

EX2_3 = 'Exercise 2.3'
SOLVED += [
    q('u2_ex23_q1', 2, EX2_3, 'EX2.3', 1,
      'Solve the following: (i) [2, &infin;) &cup; (3, 5)  (ii) [&minus;1, 1] &minus; (2, &infin;)  '
      '(iii) (5, &infin;) &cap; (&minus;3, 6)  (iv) [3, 5] &minus; (3, 5)  (v) [1, 10] &cap; [3, 11]  '
      '(vi) (&minus;&infin;, 5) &minus; (&minus;&infin;, 3)',
      '(i) [2, &infin;)<br>(ii) [&minus;1, 1]<br>(iii) (5, 6)<br>(iv) {3, 5}<br>(v) [3, 10]<br>(vi) [3, 5)',
      'Union keeps all points of either set, intersection the common points, and A &minus; B deletes B from A: '
      '(i) (3,5) lies inside [2,&infin;); (ii) (2,&infin;) is disjoint from [&minus;1,1]; (iv) only the endpoints survive; '
      '(vi) 3 itself is not removed. (The key prints open brackets in (i), (ii), (v) &mdash; those endpoints do belong.)',
      49),
    q('u2_ex23_q2', 2, EX2_3, 'EX2.3', 2,
      'Find the nth term and limit of the following sequences: (i) 1, 1/2, 1/4, 1/8, &hellip;  '
      '(ii) 1&middot;2/3&middot;4, 3&middot;4/5&middot;6, 5&middot;6/7&middot;8, &hellip;',
      '(i) a&#8345; = 1/2^(&#8345;&#8315;&sup1;), limit 0<br>(ii) a&#8345; = (2n&minus;1)(2n) / [(2n+1)(2n+2)], limit 1',
      '(i) each term halves, a geometric sequence with ratio 1/2 &rarr; 0; (ii) numerator is the pair-product '
      '(2n&minus;1)(2n), denominator the next pair (2n+1)(2n+2); leading terms 4n&sup2;/4n&sup2; &rarr; 1.',
      49),
    q('u2_ex23_q3', 2, EX2_3, 'EX2.3', 3,
      'Find the limit of the following sequences whose nth terms are: (i) a&#8345; = (1+5n)/(7n)  '
      '(ii) a&#8345; = (3n&minus;1)(n&#8308;&minus;n) / [(n&sup2;+5)(n&sup3;&minus;7)]  '
      '(iii) a&#8345; = (n+1)! / [n! &minus; (n+1)!]',
      '(i) 5/7<br>(ii) 3<br>(iii) &minus;1',
      '(i) divide by n: (1/n+5)/7 &rarr; 5/7; (ii) ratio of leading terms 3n&#8309;/n&#8309; = 3; '
      '(iii) n! &minus; (n+1)! = n!(1&minus;(n+1)) so a&#8345; = (n+1)/(&minus;n) &rarr; &minus;1.',
      49),
    q('u2_ex23_q4', 2, EX2_3, 'EX2.3', 4,
      'Find the limit of the function y = 5x/(x + 1) for x &rarr; &infin;.',
      '5',
      'Divide top and bottom by x: y = 5/(1 + 1/x) &rarr; 5/(1+0) = 5.',
      50),
    q('u2_ex23_q5', 2, EX2_3, 'EX2.3', 5,
      'Evaluate by using theorems on limits: (i) lim<sub>x&rarr;2</sub> (x&#8309; + x&sup2; + x + 1)  '
      '(ii) lim<sub>x&rarr;5</sub> ((1+x)/x&sup2;)  (iii) lim<sub>x&rarr;1</sub> [(2x&sup3; + 3x&sup2;)(x + 1)]  '
      '(iv) lim<sub>x&rarr;5</sub> {(x + 1) &minus; (x&sup2; + 2x + 3)}',
      '(i) 39<br>(ii) 6/25<br>(iii) 10<br>(iv) &minus;32',
      'Polynomials are continuous, so substitute: (i) 32+4+2+1; (ii) 6/25 (quotient theorem, denominator &ne; 0); '
      '(iii) (2+3)(2) by the product theorem; (iv) 6 &minus; 38 by the difference theorem.',
      50),
    q('u2_ex23_q6', 2, EX2_3, 'EX2.3', 6,
      'Evaluate the limits: (i) lim<sub>x&rarr;1</sub> (x&sup2;+4)&sup3;  (ii) lim<sub>x&rarr;0</sub> 4/(x&minus;4)  '
      '(iii) lim<sub>x&rarr;&infin;</sub> 5/(5x+10)  (iv) lim<sub>x&rarr;7</sub> (x&sup2;&minus;49)/(x&minus;7)  '
      '(v) lim<sub>x&rarr;0</sub> (&radic;(x+3)&minus;&radic;3)/x  (vi) lim<sub>x&rarr;7</sub> (x&minus;7)/(&radic;x&minus;&radic;7)  '
      '(vii) lim<sub>x&rarr;0</sub> (1+x/3)^(5/x)  (viii) lim<sub>x&rarr;0</sub> (1+ax)^(a/x)  (ix) lim<sub>x&rarr;&infin;</sub> (1+p/x)^(px)  '
      '(x) lim<sub>x&rarr;&infin;</sub> (1&minus;pq/x)^(x/p)  (xi) lim<sub>x&rarr;0</sub> (17^x&minus;1)/x  (xii) lim<sub>h&rarr;0</sub> [(1+2h)^n&minus;1]/(5h)  '
      '(xiii) lim<sub>x&rarr;0</sub> (2^x&minus;4^x&minus;8^x&minus;1)/(x+2)  (xiv) lim<sub>x&rarr;0</sub> [(1+7x)/(1&minus;9x)]^(1/x)  '
      '(xv) lim<sub>x&rarr;0</sub> (a^x&minus;b^x)/x  (xvi) lim<sub>x&rarr;0</sub> (e^(&minus;2x)&minus;e^(&minus;11x))/x  '
      '(xvii) lim<sub>x&rarr;0</sub> (3e^(&minus;5x)&minus;5e^(&minus;2x)+2)/x  (xviii) lim<sub>x&rarr;0</sub> (1+3tan x)^(cot x)  '
      '(xix) lim<sub>x&rarr;2</sub> (x&#8308;&minus;16)/(x&sup3;&minus;8)  (xx) lim<sub>x&rarr;&infin;</sub> (2x&minus;x&sup2;)/(3x&sup2;&minus;4x+1)',
      '(i) 125<br>(ii) &minus;1<br>(iii) 0<br>(iv) 14<br>(v) 1/(2&radic;3)<br>(vi) 2&radic;7<br>(vii) e^(5/3)<br>'
      '(viii) e^(a&sup2;)<br>(ix) e^(p&sup2;)<br>(x) e^(&minus;q)<br>(xi) ln 17<br>(xii) 2n/5<br>(xiii) &minus;1<br>'
      '(xiv) e^16<br>(xv) ln(a/b)<br>(xvi) 9<br>(xvii) &minus;5<br>(xviii) e&sup3;<br>(xix) 8/3<br>(xx) &minus;1/3',
      'Substitute where continuous ((i)&ndash;(iii), (xiii)); factor or rationalise the 0/0 forms ((iv) x+7; '
      '(v) conjugate gives 1/(&radic;(x+3)+&radic;3); (vi) &radic;x+&radic;7); use (1+u)^(1/u) &rarr; e for '
      '(vii)&ndash;(x), (xiv), (xviii); (a^x&minus;1)/x &rarr; ln a for (xi), (xv), (xvi), (xvii); binomial expansion '
      'for (xii); factor (x&minus;2) in (xix). (xx): leading terms &minus;x&sup2;/3x&sup2; = &minus;1/3 &mdash; the '
      'book key misprints &minus;3.',
      50),
    q('u2_ex23_q7', 2, EX2_3, 'EX2.3', 7,
      'Evaluate the limits: (i) lim<sub>x&rarr;0</sub> a sin(ax)/x  (ii) lim<sub>x&rarr;0</sub> sin(&radic;a&middot;x)/(x/&radic;a)  '
      '(iii) lim<sub>x&rarr;0</sub> (3cos x + 2tan x)&sup3;  (iv) lim<sub>x&rarr;0</sub> (3sin x &minus; x&sup3;)/(2x)  '
      '(v) lim<sub>x&rarr;0</sub> sin(px)/sin(qx)  (vi) lim<sub>x&rarr;0</sub> (2&pi;&minus;x)sec(&pi;&minus;x)/(&pi;/2)  '
      '(vii) lim<sub>x&rarr;0</sub> sin(x&deg;)/x  (viii) lim<sub>x&rarr;0</sub> (1&minus;cos mx)/(1&minus;cos nx)  '
      '(ix) lim<sub>x&rarr;0</sub> (sin 3x sin 5x)/(7x&sup2;)',
      '(i) a&sup2;<br>(ii) a<br>(iii) 27<br>(iv) 3/2<br>(v) p/q<br>(vi) &minus;4<br>(vii) &pi;/180<br>'
      '(viii) m&sup2;/n&sup2;<br>(ix) 15/7',
      'Use sin(kx)/x &rarr; k and (1&minus;cos kx)/x&sup2; &rarr; k&sup2;/2: (i) a&middot;a; (ii) (&radic;a&middot;x)(&radic;a/x); '
      '(iii) substitute (3&middot;1+0)&sup3;; (iv) (3/2)(sin x/x) &minus; x&sup2;/2; (v) px/qx; (vi) substitute: '
      '(2&pi;)(sec &pi;)(2/&pi;) = &minus;4; (vii) x&deg; = (&pi;/180)x rad; (viii) (m&sup2;x&sup2;/2)/(n&sup2;x&sup2;/2); '
      '(ix) (3&middot;5)/7.',
      50),
    q('u2_ex23_q8', 2, EX2_3, 'EX2.3', 8,
      'Evaluate the limits: (i) lim<sub>x&rarr;0</sub> sin&sup2;(x/2)/(4x&sup2;)  (ii) lim<sub>x&rarr;&infin;</sub> x sin(1/x)  '
      '(iii) lim<sub>x&rarr;&infin;</sub> [&radic;(x&sup2;+x+1) &minus; x]  (iv) lim<sub>x&rarr;0</sub> (1&minus;cos&sup3;x)/sin&sup2;x  '
      '(v) lim<sub>x&rarr;0</sub> (a^x+a^(&minus;x)&minus;2)/x&sup2;  (vi) lim<sub>x&rarr;0</sub> (6^x&minus;3^x&minus;2^x+1)/x&sup2;  '
      '(vii) lim<sub>x&rarr;3</sub> [x/(x+2) &minus; 3/5]/(x&minus;3)  (viii) lim<sub>y&rarr;4</sub> (y^(5/2)&minus;16y^(1/2))/(y&minus;4)  '
      '(ix) lim<sub>x&rarr;1</sub> (1/&radic;x &minus; 1)/(1&minus;x)  (x) lim<sub>x&rarr;&pi;</sub> (&radic;(5+cos x)&minus;2)/(&pi;&minus;x)  '
      '(xi) lim<sub>x&rarr;1</sub> x^(1/(x&minus;1))  (xii) lim<sub>x&rarr;1</sub> (x&sup2;&minus;&radic;x)/(&radic;x&minus;1)  '
      '(xiii) lim<sub>x&rarr;&pi;/4</sub> (&radic;2&minus;cos x&minus;sin x)/(4x&minus;&pi;)&sup2;  (xiv) lim<sub>x&rarr;e</sub> (ln x&minus;1)/(x&minus;e)  '
      '(xv) lim<sub>x&rarr;2</sub> (x+1)sin(x&minus;2)/(x&sup2;&minus;4)',
      '(i) 1/16<br>(ii) 1<br>(iii) 1/2<br>(iv) 3/2<br>(v) (ln a)&sup2;<br>(vi) (ln 2)(ln 3)<br>(vii) 2/25<br>'
      '(viii) 16<br>(ix) 1/2<br>(x) 0<br>(xi) e<br>(xii) 3<br>(xiii) 1/(16&radic;2)<br>(xiv) 1/e<br>(xv) 3/4',
      '(i) (x/2)&sup2;/4x&sup2;; (ii) h = 1/x gives sin h/h; (iii) conjugate gives (x+1)/(&radic;(x&sup2;+x+1)+x); '
      '(iv) (1&minus;cos x)(1+cos x+cos&sup2;x)/sin&sup2;x; (v) (a^(x/2)&minus;a^(&minus;x/2))&sup2;/x&sup2;; '
      '(vi) (2^x&minus;1)(3^x&minus;1)/x&sup2;; (vii) numerator = 2(x&minus;3)/[5(x+2)]; (viii) &radic;y(y+4); '
      '(ix) 1/[&radic;x(1+&radic;x)]; (x) numerator and its slope vanish at &pi;; (xi) (1+h)^(1/h); '
      '(xii) u = &radic;x gives u(u&sup2;+u+1); (xiii) x = &pi;/4+h gives &radic;2(1&minus;cos h)/16h&sup2;; '
      '(xiv) slope of ln x at e; (xv) (x+1)/(x+2) &middot; sin(x&minus;2)/(x&minus;2).',
      50),
]

EX2_4 = 'Exercise 2.4'
SOLVED += [
    q('u2_ex24_q1', 2, EX2_4, 'EX2.4', 1,
      'Evaluate the following limits: (i) lim<sub>x&rarr;2&#8314;</sub> (x&minus;2)/|x&minus;2|  '
      '(ii) lim<sub>x&rarr;1&#8315;</sub> (x&sup2;+2x&minus;3)/|x&minus;1|  '
      '(iii) lim<sub>x&rarr;2</sub> (x&sup2;+4x&minus;12)/|x&minus;2|',
      '(i) 1<br>(ii) &minus;4<br>(iii) does not exist',
      '|x&minus;a| = (x&minus;a) on the right of a and &minus;(x&minus;a) on the left: (i) ratio 1; '
      '(ii) (x&minus;1)(x+3)/[&minus;(x&minus;1)] = &minus;(x+3) &rarr; &minus;4; (iii) (x&minus;2)(x+6)/|x&minus;2| '
      'gives +8 from the right and &minus;8 from the left, so the two-sided limit fails.',
      57),
    q('u2_ex24_q2', 2, EX2_4, 'EX2.4', 2,
      'Determine whether lim<sub>x&rarr;1</sub> f(x), lim<sub>x&rarr;2</sub> f(x), lim<sub>x&rarr;3</sub> f(x) and '
      'lim<sub>x&rarr;4</sub> f(x) exist when f(x) = 2x+1 (0 &le; x &lt; 2), x&minus;7 (2 &le; x &lt; 4), x (4 &le; x &le; 6).',
      'lim<sub>x&rarr;1</sub> f = 3 (exists); lim<sub>x&rarr;2</sub> f does not exist; lim<sub>x&rarr;3</sub> f = &minus;4 (exists); '
      'lim<sub>x&rarr;4</sub> f does not exist',
      'At 1 and 3 the point lies inside a single piece (values 3 and &minus;4); at 2 the one-sided limits are 5 and &minus;5, '
      'and at 4 they are &minus;3 and 4, so those limits do not exist.',
      57),
    q('u2_ex24_q3', 2, EX2_4, 'EX2.4', 3,
      'Test the continuity and discontinuity of: (i) f(x) = sin(x&sup2; + &pi;x) + 7x&sup2; + x at x = 0  '
      '(ii) f(x) = (2 &minus; cos 3x &minus; cos 4x)/x at x = 0  '
      '(iii) f(x) = 7+3x (x &lt; 1), 1&minus;5x (x &ge; 1) at x = 1',
      '(i) continuous<br>(ii) discontinuous<br>(iii) discontinuous',
      '(i) f(0) = 0 = lim f; (ii) the limit exists (&asymp;12.5x &rarr; 0) but f(0) is undefined (0/0 form), so f is '
      'discontinuous at 0; (iii) left limit 10 &ne; right limit and value &minus;4 &mdash; a jump.',
      57),
    q('u2_ex24_q4', 2, EX2_4, 'EX2.4', 4,
      'Determine whether the following functions are continuous at x = 2: (i) f(x) = (x&sup2;&minus;4)/(x&minus;2)  '
      '(ii) g(x) = (x&sup2;&minus;4)/(x&minus;2) for x &ne; 2, 3 for x = 2  '
      '(iii) h(x) = (x&sup2;&minus;4)/(x&minus;2) for x &ne; 2, 4 for x = 2',
      '(i) discontinuous<br>(ii) discontinuous<br>(iii) continuous',
      '(x&sup2;&minus;4)/(x&minus;2) = x+2 for x &ne; 2, so the limit at 2 is 4 in every case: (i) f(2) undefined; '
      '(ii) g(2) = 3 &ne; 4; (iii) h(2) = 4 = lim &mdash; only (iii) satisfies lim = value.',
      57),
    q('u2_ex24_q5', 2, EX2_4, 'EX2.4', 5,
      'Suppose f(x) = &minus;x&#8308; + 3 for x &le; 2 and x&sup2; + 9 for x > 2. Is f continuous everywhere?',
      'Continuous everywhere except at x = 2 (left/value &minus;13 vs right 13 &mdash; a jump).',
      'Both pieces are polynomials, hence continuous on their intervals; at x = 2 the one-sided values '
      '&minus;16+3 = &minus;13 and 4+9 = 13 disagree, so continuity fails only there.',
      57),
    q('u2_ex24_q6', 2, EX2_4, 'EX2.4', 6,
      'Find the value of k if f(x) = sin(kx)/x for x &ne; 0 and 2 for x = 0 is continuous at x = 0.',
      'k = 2',
      'lim<sub>x&rarr;0</sub> sin(kx)/x = k must equal f(0) = 2.',
      57),
    q('u2_ex24_q7', 2, EX2_4, 'EX2.4', 7,
      'Find the value of k if f(x) = kx &minus; 9 (x &lt; 5), 9x &minus; k (x > 5), 36 (x = 5) is continuous at x = 5.',
      'k = 9',
      'Left limit 5k&minus;9 = 36 and right limit 45&minus;k = 36 both give k = 9, so the three values agree.',
      58),
    q('u2_ex24_q8', 2, EX2_4, 'EX2.4', 8,
      'Find the values of m and n so that f is continuous at x = 3: '
      '(i) f(x) = mx (x &lt; 3), n (x = 3), &minus;2x+9 (x > 3)  (ii) f(x) = mx (x &lt; 3), x&sup2; (x &ge; 3)',
      '(i) m = 1, n = 3<br>(ii) m = 3',
      '(i) left 3m, right &minus;6+9 = 3, value n &rArr; 3m = 3, n = 3; (ii) left 3m must equal right 9 &rArr; m = 3.',
      58),
    q('u2_ex24_q9', 2, EX2_4, 'EX2.4', 9,
      'If f(x) = [&radic;(2x+5) &minus; &radic;(x+7)]/(x&minus;2) for x &ne; 2 and k for x = 2, find k so that f is '
      'continuous at x = 2.',
      'k = 1/6',
      'Rationalising: numerator becomes (2x+5)&minus;(x+7) = x&minus;2, cancelling the denominator, so '
      'f(x) = 1/[&radic;(2x+5)+&radic;(x+7)] &rarr; 1/(3+3) = 1/6; continuity needs f(2) = k = 1/6.',
      58),
]

REV2 = 'Review Exercise 2'
SOLVED += [
    q('u2_rev2_q1', 2, REV2, 'REV2', 1,
      'Choose the correct answer: (i) f(x) = x is called  (ii) the set {x | x &isin; &real;} as an interval  '
      '(iii) [3,5] &minus; (3,5)  (iv) R = {(x,y) | x,y &isin; &real; and y = 5}  (v) f(x) = x/|x|, x &ne; 0  '
      '(vi) f(x) = 4&#739; &rArr; f(x+1) &minus; f(x)  (vii) limit of a&#8345; = 1/2&#8345;  '
      '(viii) lim<sub>x&rarr;0</sub> sin(ax)/x  (ix) lim<sub>x&rarr;3</sub> (x&sup2;&minus;9)/(x&minus;3)  '
      '(x) f : [&minus;1,4] &rarr; &real;, f(x) = x&sup2;, f(&minus;3)  (xi) lim<sub>h&rarr;0</sub> sin(&pi;/2+h)  '
      '(xii) lim<sub>x&rarr;0</sub> e^(&minus;1/x)  (xiii) lim<sub>x&rarr;c</sub> f(x) exists iff  '
      '(xiv) lim<sub>n&rarr;&infin;</sub> (1+1/n)^(&minus;7n)  (xv) limit of 1, &pi;&#8315;&sup1;, &pi;&#8315;&sup2;, &hellip;  '
      '(xvi) which represents a parametric function  (xvii) g(x) = 3x+2, g(f(x)) = x &rArr; f(2)  '
      '(xviii) k making x/tan 3x (x &ne; 0), k (x = 0) continuous  (xix) lim<sub>x&rarr;0</sub> (1&minus;x)^(1/x)  '
      '(xx) sech&#8315;&sup1;x equals',
      '(i) (c) identity function<br>(ii) (c) (&minus;&infin;, &infin;)<br>(iii) (d) {3,5}<br>(iv) (a) set of real numbers<br>'
      '(v) (a) odd function<br>(vi) (c) 3f(x)<br>(vii) (a) 0<br>(viii) (b) a<br>(ix) (d) 6<br>(x) (c) does not exist<br>'
      '(xi) (a) 1<br>(xii) (a) 0<br>(xiii) (c) both one-sided limits exist and are equal<br>(xiv) (a) e&#8315;&#8327;<br>'
      '(xv) (d) 0<br>(xvi) (c) x = f(t), y = g(t)<br>(xvii) (c) 0<br>(xviii) (d) 1/3<br>(xix) (d) e&#8315;&sup1;<br>'
      '(xx) (b) ln(1/x + &radic;(1&minus;x&sup2;)/x)',
      '(i) maps every element to itself; (ii) endpoints &plusmn;&infin; are never included; (iii) only the endpoints survive; '
      '(iv) each pair (x,5) is determined by x, so R matches &real; one-to-one; (v) f(&minus;x) = &minus;f(x); '
      '(vi) 4&middot;4&#739;&minus;4&#739; = 3&middot;4&#739;; (vii) 2&#8345; &rarr; &infin;; (viii) sin(kx)/x &rarr; k; (ix) x+3 at 3; '
      '(x) &minus;3 &notin; [&minus;1,4]; (xi) sin(&pi;/2) = 1; (xii) right-hand limit 0 (key answer; two-sided limit fails); '
      '(xiv) [(1+1/n)&#8319;]&#8315;&#8327;; (xv) 1/&pi;&#8345; &rarr; 0; (xvii) f = g&#8315;&sup1; = (x&minus;2)/3; '
      '(xviii) lim x/tan 3x = 1/3; (xix) (1+u)^(1/u) &rarr; e with u = &minus;x; (xx) solving y = sech&#8315;&sup1;x.',
      58),
    q('u2_rev2_q2', 2, REV2, 'REV2', 2,
      'If h(x) = &radic;(x&sup2;+3) and k(x) = x&sup2; &minus; 2, find: (i) hok(x)  (ii) koh  (iii) hoh  (iv) kok',
      '(i) &radic;(x&#8308; &minus; 4x&sup2; + 7)<br>(ii) x&sup2; + 1<br>(iii) &radic;(x&sup2; + 6)<br>(iv) x&#8308; &minus; 4x&sup2; + 2',
      'Substitute the inner function: (i) &radic;((x&sup2;&minus;2)&sup2;+3); (ii) (&radic;(x&sup2;+3))&sup2;&minus;2; '
      '(iii) &radic;((&radic;(x&sup2;+3))&sup2;+3); (iv) (x&sup2;&minus;2)&sup2;&minus;2.',
      60),
    q('u2_rev2_q3', 2, REV2, 'REV2', 3,
      'If f(x) = x + 3 and g(x) = x&sup2;, find gof(x) for x = 1.',
      '16',
      'gof(x) = (x+3)&sup2;; at x = 1: 4&sup2; = 16.',
      60),
    q('u2_rev2_q4', 2, REV2, 'REV2', 4,
      'f(x) = (x+1)/3 and g(x) = 3x + 5 are given; verify that (i) (fog)&#8315;&sup1; = g&#8315;&sup1;of&#8315;&sup1;  '
      '(ii) (gof)&#8315;&sup1; = f&#8315;&sup1;og&#8315;&sup1;',
      '(i) fog = x+2 &rArr; (fog)&#8315;&sup1; = x&minus;2 = g&#8315;&sup1;(f&#8315;&sup1;(x)) &mdash; verified<br>'
      '(ii) gof = x+6 &rArr; (gof)&#8315;&sup1; = x&minus;6 = f&#8315;&sup1;(g&#8315;&sup1;(x)) &mdash; verified',
      'f&#8315;&sup1;(x) = 3x&minus;1 and g&#8315;&sup1;(x) = (x&minus;5)/3; then g&#8315;&sup1;of&#8315;&sup1; = (3x&minus;1&minus;5)/3 = x&minus;2 '
      'and f&#8315;&sup1;og&#8315;&sup1; = 3(x&minus;5)/3&minus;1 = x&minus;6, matching the direct inverses of fog = x+2 and gof = x+6.',
      60),
    q('u2_rev2_q5', 2, REV2, 'REV2', 5,
      'Recognize as explicit or implicit functions and express the implicit ones explicitly where possible: '
      '(i) x&sup3; + 2xy = 5x&sup2; &minus; 3y  (ii) 3y = 5x&sup2; &minus; 3x  (iii) x&sup2;y + xy = 5y &minus; 3  '
      '(iv) 2x&sup2;y &minus; xy = 5 + 3xy',
      '(i) implicit; y = (5x&sup2; &minus; x&sup3;)/(2x+3)<br>(ii) explicit; y = (5x&sup2; &minus; 3x)/3<br>'
      '(iii) implicit; y = &minus;3/(x&sup2; + x &minus; 5)<br>(iv) implicit; y = 5/[2x(x &minus; 2)]',
      'Collect the y terms and divide: (i) y(2x+3) = 5x&sup2;&minus;x&sup3;; (iii) y(x&sup2;+x&minus;5) = &minus;3; '
      '(iv) y(2x&sup2;&minus;4x) = 5. (ii) is already solved for y. (The key misprints (iv) as 5/[2x(x&minus;1)].)',
      60),
    q('u2_rev2_q6', 2, REV2, 'REV2', 6,
      'Show that the parametric equations x = a sec &theta;, y = b tan &theta; represent the equation '
      'x&sup2;/a&sup2; &minus; y&sup2;/b&sup2; = 1.',
      'x/a = sec &theta; and y/b = tan &theta;; since sec&sup2;&theta; &minus; tan&sup2;&theta; = 1, '
      '(x/a)&sup2; &minus; (y/b)&sup2; = 1, i.e. x&sup2;/a&sup2; &minus; y&sup2;/b&sup2; = 1 &mdash; shown.',
      'Dividing each parametric equation by its constant isolates sec &theta; and tan &theta;, and the Pythagorean-type '
      'identity sec&sup2; &minus; tan&sup2; = 1 eliminates &theta;.',
      60),
    q('u2_rev2_q7', 2, REV2, 'REV2', 7,
      'Draw and explain the graph of: (i) f(x) = e^(5x)  (ii) y = &radic;(4 &minus; x&sup2;)  '
      '(iii) x&sup2;/9 + y&sup2;/16 = 1',
      '(i) exponential through (0,1), flat on the left, steep rise on the right; (ii) upper semicircle of radius 2; '
      '(iii) ellipse with semi-axes 3 (x) and 4 (y) &mdash; see figure.',
      '(ii) squaring gives x&sup2;+y&sup2; = 4 with y &ge; 0; (iii) is the standard ellipse x&sup2;/3&sup2; + y&sup2;/4&sup2; = 1.',
      60, figure='/figures/math_xii/rev2_q7.png'),
    q('u2_rev2_q8', 2, REV2, 'REV2', 8,
      'Draw the graph of the parametric equations x = at&sup2;, y = 2at when a = 6 and &minus;5 &le; t &le; 5.',
      'Right-opening parabola y&sup2; = 24x from (150, &minus;60) through (0,0) to (150, 60) &mdash; see figure.',
      'x = 6t&sup2;, y = 12t &rArr; t = y/12 &rArr; x = y&sup2;/24, i.e. y&sup2; = 24x.',
      60, figure='/figures/math_xii/rev2_q8.png'),
    q('u2_rev2_q9', 2, REV2, 'REV2', 9,
      'Draw the graph of the parametric equations x = a sec &theta;, y = b tan &theta; when a = 4, b = 3 '
      'and &minus;&pi; &le; &theta; &le; &pi;.',
      'Hyperbola x&sup2;/16 &minus; y&sup2;/9 = 1: branches opening left/right, vertices (&plusmn;4, 0), '
      'asymptotes y = &plusmn;(3/4)x &mdash; see figure.',
      'sec&sup2;&theta; &minus; tan&sup2;&theta; = 1 gives (x/4)&sup2; &minus; (y/3)&sup2; = 1; the two &theta;-intervals '
      'around &plusmn;&pi;/2 trace the left branch, the middle one the right branch.',
      60, figure='/figures/math_xii/rev2_q9.png'),
    q('u2_rev2_q10', 2, REV2, 'REV2', 10,
      'Solve the following: (i) [1, &infin;) &cup; (2, 3)  (ii) [&minus;1, 1] &cap; (2, &infin;)  '
      '(iii) (4, &infin;) &cap; (&minus;3, 3)  (iv) [2, 3] &minus; (2, 3)  (v) [1, 9] &cap; [3, 12]  '
      '(vi) (&minus;&infin;, 7) &minus; (&minus;&infin;, 2)',
      '(i) [1, &infin;)<br>(ii) &empty;<br>(iii) &empty;<br>(iv) {2, 3}<br>(v) [3, 9]<br>(vi) [2, 7)',
      '(i) (2,3) lies inside [1,&infin;); (ii) and (iii) the intervals do not overlap &mdash; empty set (the key misprints '
      '(iii) as (4,3)); (iv) removing the open middle leaves the endpoints (key misprints [2,3]); (v) common part 3..9; '
      '(vi) 2 itself is not removed.',
      60),
    q('u2_rev2_q11', 2, REV2, 'REV2', 11,
      'Find the limit of the sequence 1, 1/4, 1/16, 1/64, &hellip;',
      '0',
      'a&#8345; = 1/4^(&#8345;&#8315;&sup1;); 4&#8345; &rarr; &infin; so the terms tend to 0.',
      60),
    q('u2_rev2_q12', 2, REV2, 'REV2', 12,
      'Find the limit of a&#8345; = &minus;1 + (1/5)&#8319;.',
      '&minus;1',
      '(1/5)&#8319; &rarr; 0, leaving &minus;1.',
      60),
    q('u2_rev2_q13', 2, REV2, 'REV2', 13,
      'Find the limit of the function y = 1/x&sup3; for x &rarr; &infin;.',
      '0',
      'The denominator grows without bound while the numerator stays 1.',
      60),
    q('u2_rev2_q14', 2, REV2, 'REV2', 14,
      'Evaluate: (i) lim<sub>x&rarr;3</sub> (x&sup3; + x&#8308; + x + 5)  (ii) lim<sub>x&rarr;7</sub> (1+x)/x&#8327;  '
      '(iii) lim<sub>x&rarr;1</sub> [(2x&#8308; + 3x&sup3;)(x + 3)]  (iv) lim<sub>x&rarr;3</sub> [(x+3) &minus; (x&sup3; + 5x + 5)]  '
      '(v) lim<sub>x&rarr;&pi;/4</sub> (cosec&sup2;x &minus; 2)/(cot x &minus; 1)  (vi) lim<sub>x&rarr;&pi;</sub> sin(&pi;&minus;x)/[&pi;(&pi;&minus;x)]  '
      '(vii) lim<sub>x&rarr;0</sub> (1+2x)^(5/x)  (viii) lim<sub>x&rarr;0</sub> (3^(2x) &minus; 1)/sin x',
      '(i) 116<br>(ii) 8/7&#8327;<br>(iii) 20<br>(iv) &minus;41<br>(v) 2<br>(vi) 1/&pi;<br>(vii) e&sup1;&#8320;<br>(viii) 2 ln 3',
      '(i)&ndash;(iv) substitute (polynomials are continuous); (v) cosec&sup2;x&minus;2 = cot&sup2;x&minus;1 = '
      '(cot x&minus;1)(cot x+1); (vi) sin u/u &rarr; 1 with u = &pi;&minus;x; (vii) (1+u)^(1/u) &rarr; e with u = 2x, '
      'exponent 5/x = (1/u)&middot;10; (viii) [(3^(2x)&minus;1)/(2x)]&middot;[2x/sin x] &rarr; ln 3 &middot; 2.',
      61),
    q('u2_rev2_q15', 2, REV2, 'REV2', 15,
      'Determine whether the following are continuous at x = 3: (i) f(x) = (x&sup2;&minus;9)/(x&minus;3)  '
      '(ii) g(x) = (x&sup2;&minus;9)/(x&minus;3) for x &ne; 3, 5 for x = 3  '
      '(iii) h(x) = (x&sup2;&minus;9)/(x&minus;3) for x &ne; 3, 6 for x = 3',
      '(i) discontinuous<br>(ii) discontinuous<br>(iii) continuous',
      'For x &ne; 3 the expression equals x+3, so the limit at 3 is 6: (i) f(3) undefined; (ii) g(3) = 5 &ne; 6; '
      '(iii) h(3) = 6 = lim.',
      61),
    q('u2_rev2_q16', 2, REV2, 'REV2', 16,
      'If f(x) = 3x (x &le; &minus;2), x&sup2; &minus; 1 (&minus;2 &lt; x &lt; 2), 3 (x &ge; 2), discuss the continuity '
      'or discontinuity at x = 2 and x = &minus;2.',
      'Continuous at x = 2; discontinuous at x = &minus;2.',
      'At 2: left limit x&sup2;&minus;1 &rarr; 3 equals right limit and value 3; at &minus;2: left limit and value '
      '3(&minus;2) = &minus;6 but right limit x&sup2;&minus;1 &rarr; 3 &mdash; a jump.',
      61),
]

EX3_1 = 'Exercise 3.1'
SOLVED += [
    q('u3_ex31_q1', 3, EX3_1, 'EX3.1', 1,
      'Find the average rate of change of the function between the given values: '
      '(i) f(x) = x&sup2; + 4, a = 2, b = 2.3  (ii) f(x) = x&sup3; &minus; 4, a = 2, b = 2.3  '
      '(iii) f(x) = x&sup3; &minus; 8, a = 3, b = 2.5',
      '(i) 4.3<br>(ii) 13.89<br>(iii) 22.75',
      '(i) [(2.3&sup2;+4)&minus;(2&sup2;+4)]/(2.3&minus;2) = 1.29/0.3 = 4.3; '
      '(ii) [(2.3&sup3;&minus;4)&minus;(2&sup3;&minus;4)]/0.3 = 4.167/0.3 = 13.89; '
      '(iii) [(2.5&sup3;&minus;8)&minus;(3&sup3;&minus;8)]/(2.5&minus;3) = (&minus;11.375)/(&minus;0.5) = 22.75.',
      64),
    q('u3_ex31_q2', 3, EX3_1, 'EX3.1', 2,
      'Find the average rate of change: (i) the area of a circle A = &pi;x&sup2; when the radius changes from '
      'a = 3 to b = 3.1 cm  (ii) the volume of a sphere V = (4/3)&pi;x&sup3; when the radius changes from '
      'a = 2 to b = 1.9 cm',
      '(i) 6.1&pi; cm&sup2;/cm<br>(ii) &asymp; 47.8 cm&sup3;/cm',
      '(i) [&pi;(3.1)&sup2; &minus; &pi;(3)&sup2;]/(3.1&minus;3) = 0.61&pi;/0.1 = 6.1&pi;. '
      '(ii) (4/3)&pi;[(1.9)&sup3;&minus;(2)&sup3;]/(1.9&minus;2) = (4/3)&pi;(&minus;1.141)/(&minus;0.1) '
      '= 15.213&pi; &asymp; 47.8.',
      64),
    q('u3_ex31_q3', 3, EX3_1, 'EX3.1', 3,
      'The annual profit p of a small business is given by p(t) = 3t&sup2; + t + 1, where t &ge; 0 measures the '
      'years since 1995. Find the average rate of change of profit between t = 3 and t = 3.5.',
      'Rs. 20.5 per year',
      '[p(3.5) &minus; p(3)]/(3.5&minus;3) = [(36.75+3.5+1) &minus; (27+3+1)]/0.5 = 10.25/0.5 = 20.5.',
      64),
    q('u3_ex31_q4', 3, EX3_1, 'EX3.1', 4,
      'A ball is thrown straight up with an initial velocity of 80 feet/second; its height after t seconds is '
      'h(t) = &minus;16t&sup2; + 80t feet. Find the average velocity during the interval: '
      '(a) t = 2 to t = 2.1 s  (b) t = 2 to t = 2.01 s',
      '(a) 14.4 ft/s<br>(b) 15.84 ft/s',
      'h(2) = 96. (a) h(2.1) = 97.44, so (97.44&minus;96)/0.1 = 14.4 ft/s. '
      '(b) h(2.01) = 96.1584, so (96.1584&minus;96)/0.01 = 15.84 ft/s.',
      64),
]

EX3_2 = 'Exercise 3.2'
SOLVED += [
    q('u3_ex32_q1', 3, EX3_2, 'EX3.2', 1,
      'Find by definition (ab-initio) the derivatives of: (i) f(x) = 2x  (ii) f(x) = 1 &minus; &radic;x  '
      '(iii) f(x) = 1/&radic;x  (iv) f(x) = 3 &minus; x&sup2;  (v) f(x) = x(x+1)  (vi) f(x) = x&sup2; &minus; 3  '
      '(vii) f(x) = x&sup3; + 5  (viii) f(x) = 4x&sup2; &minus; 3x  (ix) f(x) = 1/(x+2)  (x) f(x) = 3/(2x+5)',
      '(i) 2<br>(ii) &minus;1/(2&radic;x)<br>(iii) &minus;1/(2x&radic;x)<br>(iv) &minus;2x<br>(v) 2x + 1<br>'
      '(vi) 2x<br>(vii) 3x&sup2;<br>(viii) 8x &minus; 3<br>(ix) &minus;1/(x+2)&sup2;<br>(x) &minus;6/(2x+5)&sup2;',
      'Using f&prime;(x) = lim<sub>&delta;x&rarr;0</sub> [f(x+&delta;x) &minus; f(x)]/&delta;x: expand, cancel, and '
      'take the limit. E.g. (ix): [1/(x+&delta;x+2) &minus; 1/(x+2)]/&delta;x = &minus;1/[(x+&delta;x+2)(x+2)] '
      '&rarr; &minus;1/(x+2)&sup2;. Roots are handled by rationalizing (multiply by the conjugate); fractions by '
      'combining over a common denominator. All ten results match the Answers key (printed p. 412).',
      70),
    q('u3_ex32_q2', 3, EX3_2, 'EX3.2', 2,
      'Find f&prime;(x) using the definition of derivative: (i) f(x) = &sup3;&radic;(2x+1)  '
      '(ii) f(x) = (2x&minus;1)^(&minus;1/2)  (iii) f(x) = (6x+7)^(5/2)  (iv) f(x) = (3x&minus;5)^(&minus;3/2)',
      '(i) 2/[3(2x+1)^(2/3)]<br>(ii) &minus;1/(2x&minus;1)^(3/2)<br>(iii) 15(6x+7)^(3/2)<br>'
      '(iv) &minus;9/[2(3x&minus;5)^(5/2)]',
      'First-principles limits with algebraic identities: (i) a&sup3; &minus; b&sup3; = (a&minus;b)(a&sup2;+ab+b&sup2;) '
      'on cube roots; (ii)/(iv) rationalization and a&sup3;&minus;b&sup3; on square roots; (iii) split u^(5/2) as '
      'u&sup2;&radic;u and add-subtract a common term. Chain-rule checks: (5/2)(6x+7)^(3/2)&middot;6 = 15(6x+7)^(3/2); '
      '(&minus;3/2)(3x&minus;5)^(&minus;5/2)&middot;3 = &minus;9/[2(3x&minus;5)^(5/2)]. All four match the key.',
      70),
]

EX3_3 = 'Exercise 3.3'
SOLVED += [
    q('u3_ex33_q1', 3, EX3_3, 'EX3.3', 1,
      'Differentiate the following w.r.t. x: (i) 5x&#8309;  (ii) (7/9)x&#8313;  (iii) &minus;25x^(&minus;3/5)  '
      '(iv) 124&radic;x  (v) (1/22)x&sup2;&sup2;  (vi) x^(&minus;100)  (vii) 15&sup3;&radic;x  '
      '(viii) 16&middot;&#8308;&radic;(x^(3/4))  (ix) &minus;4/x^(3/4)  (x) 3/&sup3;&radic;(x&sup2;)',
      '(i) 25x&#8308;<br>(ii) 7x&#8312;<br>(iii) 15x^(&minus;8/5)<br>(iv) 62/&radic;x<br>(v) x&sup2;&sup1;<br>'
      '(vi) &minus;100x^(&minus;101)<br>(vii) 5/x^(2/3)<br>(viii) 3/x^(13/4)<br>(ix) 3/x^(7/4)<br>'
      '(x) &minus;2/x^(5/3)',
      'Power rule d/dx x&#8345; = n&middot;x^(&#8345;&minus;&sup1;) on each term after rewriting roots as fractional '
      'powers; e.g. (viii) 16&middot;&#8308;&radic;(x^(3/4)) = 16x^(3/16) &rarr; 3x^(&minus;13/4).',
      77),
    q('u3_ex33_q2', 3, EX3_3, 'EX3.3', 2,
      'Differentiate the following w.r.t. x: (i) x&#8309;/(a&sup2;+b&sup2;) + x&sup2;/(a&sup2;&minus;b&sup2;)  '
      '(ii) 2x + (1/2)x&#8310;  (iii) &sup3;&radic;(x&sup2;) + &radic;x  (iv) (1/21)x&sup2;&sup1; + (1/22)x&sup2;&sup2;  '
      '(v) &minus;(5/4)x^(&minus;4/5) + (2/3)x^(&minus;3/2)',
      '(i) 5x&#8308;/(a&sup2;+b&sup2;) + 2x/(a&sup2;&minus;b&sup2;)<br>(ii) 2 + 3x&#8309;<br>'
      '(iii) 2/(3&sup3;&radic;x) + 1/(2&radic;x)<br>(iv) x&sup2;&#8304; + x&sup2;&sup1;<br>'
      '(v) x^(&minus;9/5) &minus; x^(&minus;5/2)',
      'Term-by-term power rule; a and b are constants so 1/(a&sup2;+b&sup2;) etc. are constant coefficients.',
      77),
    q('u3_ex33_q3', 3, EX3_3, 'EX3.3', 3,
      'Differentiate the following w.r.t. x: (i) 2ax&sup3; &minus; x&sup2;/b + 6  (ii) x&sup3; &minus; (3/7)x^(7/3)  '
      '(iii) 5x^(3/5) &minus; (1/7)x^(7/3)  (iv) x&sup1;&#8304; &minus; 10x&sup1;&#8309;  '
      '(v) 3&sup3;&radic;(x&sup2;) &minus; 4&middot;&#8308;&radic;x',
      '(i) 6ax&sup2; &minus; 2x/b<br>(ii) 3x&sup2; &minus; x^(4/3)<br>(iii) 3x^(&minus;2/5) &minus; (1/3)x^(4/3)<br>'
      '(iv) 10x&#8313; &minus; 150x&sup1;&#8308;<br>(v) 2x^(&minus;1/3) &minus; x^(&minus;3/4)',
      'Power rule with constant parameters a, b; roots converted to fractional exponents first.',
      77),
    q('u3_ex33_q4', 3, EX3_3, 'EX3.3', 4,
      'Differentiate the following polynomial functions w.r.t. x: (i) p(x) = x&sup3; &minus; 3x&sup2; + 2x + 1  '
      '(ii) p(x) = x&#8308; &minus; 3x&sup2; + 2x &minus; 3  (iii) p(x) = x&#8310; &minus; x&#8308; + x&sup3; + x  '
      '(iv) p(x) = 9x&#8313; + 7x&#8311; + (1/5)x&#8309; &minus; (1/4)x&#8308; + x + 1',
      '(i) 3x&sup2; &minus; 6x + 2<br>(ii) 4x&sup3; &minus; 6x + 2<br>(iii) 6x&#8309; &minus; 4x&sup3; + 3x&sup2; + 1<br>'
      '(iv) 81x&#8312; + 49x&#8310; + x&#8308; &minus; x&sup3; + 1',
      'Term-by-term power rule on each polynomial.',
      77),
    q('u3_ex33_q5', 3, EX3_3, 'EX3.3', 5,
      'Find the derivative using the product rule: (i) h(x) = (2x&minus;5)(5x+7)  '
      '(ii) h(x) = x&middot;&radic;(3x&sup2;+4)  (iii) h(x) = &sup3;&radic;(x+1)&middot;&#8309;&radic;(x&sup2;+1)  '
      '(iv) h(x) = x&sup2;(&radic;x + 1)  (v) h(x) = (x+1)&sup3;&middot;x^(&minus;3/2)',
      '(i) 20x &minus; 11<br>(ii) (6x&sup2;+4)/&radic;(3x&sup2;+4)<br>'
      '(iii) (11x&sup2;+6x+5)/[15(x+1)^(2/3)(x&sup2;+1)^(4/5)]<br>(iv) (x/2)(5&radic;x + 4)<br>'
      '(v) 3(x&minus;1)(x+1)&sup2;/(2x^(5/2))',
      '(uv)&prime; = u&prime;v + uv&prime;. (ii) u&prime;v+uv&prime; = &radic;(3x&sup2;+4) + 3x&sup2;/&radic;(3x&sup2;+4); '
      '(iii) combine over 15(x+1)^(2/3)(x&sup2;+1)^(4/5); (v) factor (3/2)x^(&minus;5/2)(x+1)&sup2; leaving '
      '[2x &minus; (x+1)] = x&minus;1.',
      77),
    q('u3_ex33_q6', 3, EX3_3, 'EX3.3', 6,
      'Find the derivative using the quotient rule: (i) h(x) = (3x+4)/(2x&minus;3)  '
      '(ii) h(x) = (x&sup2;&minus;1)(x&sup2;+1)^(&minus;1)  (iii) h(x) = (x&sup2;&minus;x+1)/(x&sup2;+x&minus;1)  '
      '(iv) h(x) = 2x&#8308;/(b&sup2;&minus;x&sup2;)  (v) h(x) = (&radic;x+1)/(&radic;x&minus;1)',
      '(i) &minus;17/(2x&minus;3)&sup2;<br>(ii) 4x/(x&sup2;+1)&sup2;<br>(iii) 2x(x&minus;2)/(x&sup2;+x&minus;1)&sup2;<br>'
      '(iv) 4x&sup3;(2b&sup2;&minus;x&sup2;)/(b&sup2;&minus;x&sup2;)&sup2;<br>(v) &minus;1/[&radic;x(&radic;x&minus;1)&sup2;]',
      '(u/v)&prime; = (u&prime;v &minus; uv&prime;)/v&sup2;. (iii) numerator simplifies to 2x&sup2;&minus;4x; '
      '(v) the &radic;x terms cancel leaving &minus;2/(2&radic;x) in the numerator.',
      77),
]

EX3_4 = 'Exercise 3.4'
SOLVED += [
    q('u3_ex34_q1', 3, EX3_4, 'EX3.4', 1,
      'Find the derivatives using the chain rule: (i) y = (x&#8308;+5x&sup2;+6)^(3/2)  '
      '(ii) y = ((x&minus;1)/(x+1))^(3/4)  (iii) y = &radic;((2+x)/(3+x))  (iv) y = (x+&radic;(x&sup2;&minus;1))&#8345;  '
      '(v) y = &sup3;&radic;((x&sup3;+1)/(x&sup3;&minus;1))',
      '(i) 3x(2x&sup2;+5)(x&#8308;+5x&sup2;+6)^(1/2)<br>(ii) 3/[2(x&minus;1)^(1/4)(x+1)^(7/4)]<br>'
      '(iii) 1/[2(2+x)^(1/2)(3+x)^(3/2)]<br>(iv) n(x+&radic;(x&sup2;&minus;1))&#8345;/&radic;(x&sup2;&minus;1)<br>'
      '(v) &minus;2x&sup2;/[(x&sup3;+1)^(2/3)(x&sup3;&minus;1)^(4/3)]',
      'Outer-power rule times inner derivative; e.g. (ii) inner derivative is 2/(x+1)&sup2; and the '
      '(&minus;1/4) power flips the fraction.',
      89),
    q('u3_ex34_q2', 3, EX3_4, 'EX3.4', 2,
      'Differentiate x&sup3;/(1+x&sup3;) w.r.t. x&sup3;.',
      '1/(1+x&sup3;)&sup2;',
      'With t = x&sup3; the expression is t/(1+t), whose derivative is 1/(1+t)&sup2;.',
      89),
    q('u3_ex34_q3', 3, EX3_4, 'EX3.4', 3,
      'If y = f(x) is given implicitly, find dy/dx: (i) y &minus; xy &minus; sin y = 0  (ii) y&sup3; &minus; 3y + 2x = 0  '
      '(iii) x&sup2; + y&sup2; + 4x + 6y &minus; 12 = 0  (iv) sin(xy) + sec x = 2  '
      '(v) x&radic;(1+y) + y&radic;(1+x) = 0  (vi) y(x&sup2;+1) = x(y&sup2;+1)',
      '(i) y/(1 &minus; x &minus; cos y)<br>(ii) 2/[3(1&minus;y&sup2;)]<br>(iii) &minus;(x+2)/(y+3)<br>'
      '(iv) &minus;[y cos(xy) + sec x tan x]/[x cos(xy)]<br>'
      '(v) &minus;&radic;((1+y)/(1+x))&middot;[y + 2&radic;((1+x)(1+y))]/[x + 2&radic;((1+x)(1+y))]<br>'
      '(vi) (y&sup2;+1&minus;2xy)/(x&sup2;+1&minus;2xy)',
      'Differentiate both sides treating y as y(x), collect y&prime; terms and solve; (v) multiply through by '
      '2&radic;(1+y)&radic;(1+x) before isolating y&prime;.',
      89),
    q('u3_ex34_q4', 3, EX3_4, 'EX3.4', 4,
      'If u&sup2;/a&sup2; + v&sup2;/b&sup2; = 1 (a, b non-zero constants), find du/dv and dv/du.',
      'du/dv = &minus;(a&sup2;v)/(b&sup2;u) and dv/du = &minus;(b&sup2;u)/(a&sup2;v)',
      'Differentiate w.r.t. v: (2u/a&sup2;)(du/dv) + 2v/b&sup2; = 0; the other derivative is its reciprocal.',
      90),
    q('u3_ex34_q5', 3, EX3_4, 'EX3.4', 5,
      'Find the slope of the tangent to the curve 3x&sup2; &minus; 7y&sup2; + 14y &minus; 27 = 0 at the point (&minus;3, 0).',
      '9/7',
      '6x &minus; 14yy&prime; + 14y&prime; = 0; at (&minus;3,0): &minus;18 + 14y&prime; = 0 &rArr; y&prime; = 9/7.',
      90),
    q('u3_ex34_q6', 3, EX3_4, 'EX3.4', 6,
      'Differentiate by the first-principle method: (i) sin 4x  (ii) cos&sup2;2x  (iii) sec &radic;x  '
      '(iv) &radic;(tan x)  (v) csc 3x  (vi) cot 2x',
      '(i) 4cos 4x<br>(ii) &minus;2 sin 4x<br>(iii) sec&radic;x tan&radic;x/(2&radic;x)<br>'
      '(iv) sec&sup2;x/(2&radic;(tan x))<br>(v) &minus;3 csc 3x cot 3x<br>(vi) &minus;2 csc&sup2;2x',
      'lim<sub>&delta;x&rarr;0</sub>[f(x+&delta;x)&minus;f(x)]/&delta;x with sum-to-product / conjugate tricks; '
      '(ii) &minus;4 sin2x cos2x collapses to &minus;2 sin4x.',
      90),
    q('u3_ex34_q7', 3, EX3_4, 'EX3.4', 7,
      'Using differentiation rules, differentiate w.r.t. their involved variables: (i) f(x) = (x+2)sin x  '
      '(ii) f(&theta;) = tan&sup2;&theta;&middot;sec&sup3;&theta;  (iii) f(t) = sin&sup2;3t&middot;cos&sup3;t  '
      '(iv) f(x) = &radic;(sin2x/cos x)  (v) f(&theta;) = (tan&theta;&minus;1)/sec&theta;  '
      '(vi) f(x) = sin x&sup2; + sin&sup2;x',
      '(i) sin x + (x+2)cos x<br>(ii) sec&sup3;&theta; tan&theta;(2sec&sup2;&theta; + 3tan&sup2;&theta;)<br>'
      '(iii) 3cos&sup2;t(sin6t cos t &minus; sin&sup2;3t sin t)<br>(iv) cos x/&radic;(2 sin x)<br>'
      '(v) sin&theta; + cos&theta;<br>(vi) 2x cos x&sup2; + sin 2x',
      'Product/quotient rules; (iv) simplifies first: sin2x/cos x = 2 sin x; (v) simplifies to sin&theta; &minus; cos&theta;.',
      90),
    q('u3_ex34_q8', 3, EX3_4, 'EX3.4', 8,
      'Differentiate (1+tan&sup2;x)/(1&minus;tan&sup2;x) w.r.t. tan&sup2;x.',
      '2/(1&minus;tan&sup2;x)&sup2;',
      'With t = tan&sup2;x: d/dt[(1+t)/(1&minus;t)] = [(1&minus;t)+(1+t)]/(1&minus;t)&sup2; = 2/(1&minus;t)&sup2;.',
      90),
    q('u3_ex34_q9', 3, EX3_4, 'EX3.4', 9,
      'Find dy/dx: (i) y = sin&#8315;&sup1;&radic;((1&minus;cos x)/2)  '
      '(ii) y = cot&#8315;&sup1;&radic;((1+cos x)/(1&minus;cos x))  (iii) y = tan&#8315;&sup1;(sin2x/(1+cos2x))  '
      '(iv) y = x + cos&#8315;&sup1;x&middot;&radic;(1&minus;x&sup2;)  (v) y = x tan&#8315;&sup1;x/(1+x&sup2;)  '
      '(vi) y = tan&#8315;&sup1;[(&radic;(1+x)&minus;&radic;(1&minus;x))/(&radic;(1+x)+&radic;(1&minus;x))]',
      '(i) 1/2<br>(ii) 1/2<br>(iii) 1<br>(iv) &minus;x cos&#8315;&sup1;x/&radic;(1&minus;x&sup2;)<br>'
      '(v) [x + (1&minus;x&sup2;)tan&#8315;&sup1;x]/(1+x&sup2;)&sup2;<br>(vi) 1/(2&radic;(1&minus;x&sup2;))',
      'Half-angle simplifications: (i) sin&#8315;&sup1;(sin x/2) = x/2; (ii) cot&#8315;&sup1;(cot x/2) = x/2; '
      '(iii) tan&#8315;&sup1;(tan x) = x; (vi) x = cos&theta; reduces the argument to tan(&pi;/4 &minus; &theta;/2).',
      90),
    q('u3_ex34_q10', 3, EX3_4, 'EX3.4', 10,
      'If y = tan(2 tan&#8315;&sup1;(x/2)), prove that dy/dx = 4(1+y&sup2;)/(4+x&sup2;).',
      'Proved: dy/dx = 4(1+y&sup2;)/(4+x&sup2;)',
      'With t = tan&#8315;&sup1;(x/2): dy/dt = 2sec&sup2;2t = 2(1+y&sup2;) and dt/dx = 2/(4+x&sup2;); multiply.',
      90),
    q('u3_ex34_q11', 3, EX3_4, 'EX3.4', 11,
      'If y/x = tan&#8315;&sup1;(x/y), show that dy/dx = y/x.',
      'Shown: dy/dx = y/x',
      'Differentiating both sides gives (xy&prime;&minus;y)/x&sup2; = (y&minus;xy&prime;)/(x&sup2;+y&sup2;); '
      'factoring (xy&prime;&minus;y) forces it to zero, so xy&prime; = y.',
      90),
    q('u3_ex34_q12', 3, EX3_4, 'EX3.4', 12,
      'Given that tan y(1+tan x) = 1 &minus; tan x, show that dy/dx = &minus;1.',
      'Shown: dy/dx = &minus;1',
      'tan y = (1&minus;tan x)/(1+tan x) = tan(&pi;/4 &minus; x), so y = &pi;/4 &minus; x.',
      90),
    q('u3_ex34_q13', 3, EX3_4, 'EX3.4', 13,
      'If y = tan(a tan&#8315;&sup1;x), show that (1+x&sup2;)dy/dx &minus; a(1+y&sup2;) = 0.',
      'Shown: (1+x&sup2;)y&prime; &minus; a(1+y&sup2;) = 0',
      'y&prime; = sec&sup2;(a tan&#8315;&sup1;x)&middot;a/(1+x&sup2;) = a(1+y&sup2;)/(1+x&sup2;).',
      90),
    q('u3_ex34_q14', 3, EX3_4, 'EX3.4', 14,
      'Find dy/dx when: (i) x = a sin&theta;, y = a cos&theta;  (ii) x = t + 1/t, y = t + 1  '
      '(iii) x = a(1&minus;t&sup2;)/(1+t&sup2;), y = 2bt/(1+t&sup2;)  (iv) x = a&theta;&sup2;, y = 2a&theta;',
      '(i) &minus;tan&theta;<br>(ii) t&sup2;/(t&sup2;&minus;1)<br>(iii) b(t&sup2;&minus;1)/(2at)<br>(iv) 1/&theta;',
      'Parametric rule dy/dx = (dy/dt)/(dx/dt); (iii) dx/dt = &minus;4at/(1+t&sup2;)&sup2;, '
      'dy/dt = 2b(1&minus;t&sup2;)/(1+t&sup2;)&sup2;.',
      90),
    q('u3_ex34_q15', 3, EX3_4, 'EX3.4', 15,
      'If y = &radic;(tan x + &radic;(tan x + &radic;(tan x + &hellip;))), prove that (2y &minus; 1)dy/dx = sec&sup2;x.',
      'Proved: (2y &minus; 1)y&prime; = sec&sup2;x',
      'The infinite nesting means y&sup2; = tan x + y; differentiating gives 2yy&prime; = sec&sup2;x + y&prime;.',
      91),
    q('u3_ex34_q16', 3, EX3_4, 'EX3.4', 16,
      'Find the derivatives of cos&#8315;&sup1;x, csc&#8315;&sup1;x and cot&#8315;&sup1;x by using the differentiation formula.',
      'd/dx cos&#8315;&sup1;x = &minus;1/&radic;(1&minus;x&sup2;); d/dx csc&#8315;&sup1;x = &minus;1/(x&radic;(x&sup2;&minus;1)); '
      'd/dx cot&#8315;&sup1;x = &minus;1/(1+x&sup2;)',
      'Standard inverse-trigonometric derivative formulas (csc&#8315;&sup1; valid for |x| &gt; 1).',
      91),
]

EX3_5 = 'Exercise 3.5'
SOLVED += [
    q('u3_ex35_q1', 3, EX3_5, 'EX3.5', 1,
      'Differentiate the following w.r.t. x: (i) x&sup2; + 2&#739;  (ii) 4&#739; + 5&#739;  '
      '(iii) e^(tan x + cot x)  (iv) e^(tan x&sup2;)  (v) e^(2 ln(2x+1))  (vi) log&#8321;&#8304;x  '
      '(vii) e&#739;/(x&sup2;+1)  (viii) x&sup2; + 2&#739; + a^(2x)  (ix) (ln x)&#739;  '
      '(x) ln(&radic;(e^(3x)+e^(&minus;3x)))  (xi) ln(sin(ln x))  (xii) ln[tan(x/2 + &pi;/4)]',
      '(i) 2x + 2&#739;ln2<br>(ii) 4&#739;ln4 + 5&#739;ln5<br>(iii) (sec&sup2;x &minus; csc&sup2;x)e^(tan x+cot x)<br>'
      '(iv) 2x sec&sup2;(x&sup2;)e^(tan x&sup2;)<br>(v) 4(2x+1)<br>(vi) 1/(x ln10)<br>'
      '(vii) (x&minus;1)&sup2;e&#739;/(x&sup2;+1)&sup2;<br>(viii) 2x + 2&#739;ln2 + 2a^(2x)ln a (a &gt; 0)<br>'
      '(ix) (ln x)&#739;[1/ln x + ln(ln x)]<br>(x) (3/2)tanh 3x<br>(xi) cot(ln x)/x<br>(xii) sec x',
      'd/dx a&#739; = a&#739;ln a; (v) collapses to (2x+1)&sup2;; (ix) take ln y = x ln(ln x); '
      '(xii) the derivative reduces to 1/sin(x+&pi;/2).',
      96),
    q('u3_ex35_q2', 3, EX3_5, 'EX3.5', 2,
      'Using logarithmic differentiation find dy/dx if: (i) y = &radic;((x&sup2;&minus;1)/(x&sup2;+1))  '
      '(ii) y = x&sup3;&radic;x  (iii) y = xe^(cos x)  (iv) y = e^(&minus;2x)(x&sup2;+2x+1)  '
      '(v) y = ln(e&#739;/(1+e&#739;))  (vi) y = &radic;((1+e&#739;)/(1&minus;e&#739;))',
      '(i) 2x/[(x&sup2;+1)&radic;(x&#8308;&minus;1)]<br>(ii) (7/2)x^(5/2)<br>(iii) (1 &minus; x sin x)e^(cos x)<br>'
      '(iv) &minus;2xe^(&minus;2x)(x+1)<br>(v) 1/(1+e&#739;)<br>(vi) e&#739;/[(1&minus;e&#739;)&radic;(1&minus;e^(2x))]',
      'Take ln of both sides, differentiate, then multiply back by y; (ii) is simply x^(7/2).',
      97),
    q('u3_ex35_q3', 3, EX3_5, 'EX3.5', 3,
      'Find dy/dx if: (i) y = (1&minus;x&sup2;)/&radic;(1+x&sup2;)  (ii) y = &radic;((1&minus;x)/(1+x))',
      '(i) &minus;x(3+x&sup2;)/(1+x&sup2;)^(3/2)<br>(ii) &minus;1/[(1&minus;x)^(1/2)(1+x)^(3/2)]',
      'Quotient/chain rule; in (i) factor (1+x&sup2;)^(&minus;3/2) to combine the two terms.',
      97),
    q('u3_ex35_q4', 3, EX3_5, 'EX3.5', 4,
      'Find dy/dx if: (i) y = x^(sin x)  (ii) y = (sin&#8315;&sup1;x)^(ln x)  '
      '(iii) y = (tan&#8315;&sup1;x)^(sin x+cos x)  (iv) y = (ln x)^(cos x)  (v) y = x&#739;  '
      '(vi) y = ln[(&radic;(x&sup2;+1)&minus;x)/(&radic;(x&sup2;+1)+x)]',
      '(i) x^(sin x)(sin x/x + cos x ln x)<br>'
      '(ii) (sin&#8315;&sup1;x)^(ln x)[ln x/(&radic;(1&minus;x&sup2;) sin&#8315;&sup1;x) + ln(sin&#8315;&sup1;x)/x]<br>'
      '(iii) (tan&#8315;&sup1;x)^(sin x+cos x)[(sin x+cos x)/((1+x&sup2;)tan&#8315;&sup1;x) + (cos x &minus; sin x)ln(tan&#8315;&sup1;x)]<br>'
      '(iv) (ln x)^(cos x)[cos x/(x ln x) &minus; sin x ln(ln x)]<br>(v) x&#739;(1 + ln x)<br>'
      '(vi) &minus;2/&radic;(x&sup2;+1)',
      'Variable base and exponent: ln y = (exponent)&middot;ln(base), then product rule. '
      '(vi) the fraction equals (&radic;(x&sup2;+1)&minus;x)&sup2;, so y = 2ln(&radic;(x&sup2;+1)&minus;x).',
      97),
    q('u3_ex35_q5', 3, EX3_5, 'EX3.5', 5,
      'Find dy/dx when: (i) x^y&middot;y&#739; = 1  (ii) ln(xy) = x&sup2; + y&sup2;  '
      '(iii) y = sin&#8315;&sup1;(cos x) + cos&#8315;&sup1;(sin x)  (iv) y = x^y  (v) y = cos x&middot;ln(sin&#8315;&sup1;x)  '
      '(vi) x&#8345;&middot;y&#8345; = a&#8345;',
      '(i) &minus;(y/x)(x ln y + y)/(y ln x + x)<br>(ii) &minus;(y/x)(2x&sup2;&minus;1)/(2y&sup2;&minus;1)<br>(iii) &minus;2<br>'
      '(iv) y&sup2;/[x(1 &minus; y ln x)]<br>(v) cos x/[&radic;(1&minus;x&sup2;) sin&#8315;&sup1;x] &minus; sin x&middot;ln(sin&#8315;&sup1;x)<br>'
      '(vi) &minus;y/x',
      'Take logs to linearize products/powers, then differentiate implicitly; '
      '(iii) sin&#8315;&sup1;(cos x) = &pi;/2 &minus; x and cos&#8315;&sup1;(sin x) = &pi;/2 &minus; x.',
      97),
]

EX3_6 = 'Exercise 3.6'
SOLVED += [
    q('u3_ex36_q1', 3, EX3_6, 'EX3.6', 1,
      'Differentiate the following w.r.t. x: (i) sinh[ln(x+3)]  (ii) sinh(e^(3x))  (iii) cosh(2x&sup2;+3x)  '
      '(iv) tanh&radic;x/&radic;(cosh x)  (v) tan(e^(sinh&#8315;&sup1;x))  (vi) sinh&#8315;&sup1;x/sech&#8315;&sup1;x  '
      '(vii) cosh x&middot;coth x&sup2;  (viii) sinh x&middot;tanh x&sup2;  (ix) ln[tanh(x&sup2;+2x+1)]',
      '(i) cosh[ln(x+3)]/(x+3)<br>(ii) 3e^(3x)cosh(e^(3x))<br>(iii) (4x+3)sinh(2x&sup2;+3x)<br>'
      '(iv) [cosh x&middot;sech&sup2;&radic;x &minus; &radic;x&middot;sinh x&middot;tanh&radic;x]/(2&radic;x&middot;cosh^(3/2)x)<br>'
      '(v) e^(sinh&#8315;&sup1;x)&middot;sec&sup2;(e^(sinh&#8315;&sup1;x))/&radic;(1+x&sup2;)<br>'
      '(vi) [x&radic;(1&minus;x&sup2;)&middot;sech&#8315;&sup1;x + &radic;(1+x&sup2;)&middot;sinh&#8315;&sup1;x]/'
      '[x&radic;(1&minus;x&#8308;)(sech&#8315;&sup1;x)&sup2;]<br>'
      '(vii) sinh x&middot;coth x&sup2; &minus; 2x&middot;cosh x&middot;csch&sup2;x&sup2;<br>'
      '(viii) cosh x&middot;tanh x&sup2; + 2x&middot;sinh x&middot;sech&sup2;x&sup2;<br>'
      '(ix) 2(x+1)csch(x&sup2;+2x+1)sech(x&sup2;+2x+1)',
      'Chain rule with d/dx sinh u = cosh u&middot;u&prime; etc.; (vi) uses d/dx sech&#8315;&sup1;x = '
      '&minus;1/(x&radic;(1&minus;x&sup2;)). Note: the printed key shows &quot;+&quot; in (iv)&#39;s numerator; '
      'the correct sign is &minus; (key misprint).',
      104),
    q('u3_ex36_q2', 3, EX3_6, 'EX3.6', 2,
      'Find dy/dx for: (i) y = x cosh&#8315;&sup1;x &minus; &radic;(x&sup2;&minus;1)  (ii) y = x tanh&#8315;&sup1;(3x)  '
      '(iii) ln(cosh&#8315;&sup1;x) + sinh&#8315;&sup1;y = C  (iv) y = ln(1&minus;x&sup2;) + 2x tanh&#8315;&sup1;x  '
      '(v) y = tanh&#8315;&sup1;(tan x&sup3;)  (vi) y = x sech&#8315;&sup1;(&radic;x)',
      '(i) cosh&#8315;&sup1;x<br>(ii) [3x + (1&minus;9x&sup2;)tanh&#8315;&sup1;(3x)]/(1&minus;9x&sup2;)<br>'
      '(iii) &minus;&radic;(y&sup2;+1)/[&radic;(x&sup2;&minus;1)cosh&#8315;&sup1;x]<br>(iv) 2tanh&#8315;&sup1;x<br>'
      '(v) 3x&sup2;sec&sup2;(x&sup3;)/(1&minus;tan&sup2;(x&sup3;))<br>'
      '(vi) [2&radic;(1&minus;x)sech&#8315;&sup1;(&radic;x) &minus; 1]/(2&radic;(1&minus;x))',
      'In (i) and (iv) the algebraic terms cancel exactly; (vi) uses d/dx sech&#8315;&sup1;(&radic;x) = '
      '&minus;1/(2x&radic;(1&minus;x)).',
      104),
    q('u3_ex36_q3', 3, EX3_6, 'EX3.6', 3,
      'Write the MAPLE command diff to differentiate: (i) f(x) = 2x&sup3;+3x&sup2;+6  (ii) f(x) = sin(2x+3)  '
      '(iii) f(x) = (x+1)(x+2)  (iv) f(x) = (x&sup2;&minus;3x+2)/(x&sup2;&minus;4)',
      '(i) &gt; diff(2*x^3+3*x^2+6, [x]);<br>(ii) &gt; diff(sin(2*x+3), [x]);<br>'
      '(iii) &gt; diff((x+1)*(x+2), [x]);<br>(iv) &gt; diff((x^2-3*x+2)/(x^2-4), [x]);',
      'MAPLE syntax: diff(expression, [variable]); with explicit * for multiplication.',
      104),
    q('u3_ex36_q4', 3, EX3_6, 'EX3.6', 4,
      'Write the MAPLE command &gt; d/dx to differentiate: (i) f(x) = x&sup3;+5x&sup2;+3x+7  (ii) f(x) = sin x&sup2;  '
      '(iii) f(x) = (&radic;x+1)/(x&sup2;+1)',
      '(i) &gt; diff(x^3+5*x^2+3*x+7, x);<br>(ii) &gt; diff(sin(x^2), x);<br>'
      '(iii) &gt; diff((sqrt(x)+1)/(x^2+1), x);',
      'The &gt; d/dx prompt form takes the expression and the variable x directly.',
      104),
]

REV3 = 'Review Exercise 3'
SOLVED += [
    q('u3_rev3_q1', 3, REV3, 'REV3', 1,
      'Select the correct options: (i) derivative of 2/x&sup3;  (ii) derivative of &radic;x + x&radic;x  '
      '(iii) y = (x+1)(x&sup2;&minus;2)  (iv) ax&sup2;+by&sup2; = ab  (v) y = &radic;(tan x &minus; y)  '
      '(vi) y = tan&#8315;&sup1;&radic;x  (vii) derivative of tan x w.r.t. cot x  '
      '(viii) f(x) = ax&sup2;&minus;3x&minus;5, f&prime;(2) = 9  (ix) derivative of x&sup2;e^(2x)  '
      '(x) derivative of a&#739; if a &lt; 0  (xi) y = tan&#8315;&sup1;&radic;((1&minus;cos2x)/(1+cos2x))  '
      '(xii) d/dx(sinh&#8315;&sup1;x + cosh&#8315;&sup1;x)  (xiii) derivative of tanh ax  '
      '(xiv) derivative of coth&#8315;&sup1;(2x)  (xv) f(x) = ln 2x, g inverse of f, g&prime;(x)  '
      '(xvi) f(x) = a cos 3x, f&prime;(&pi;/2) = 6',
      '(i) (d) &minus;6/x&#8308;<br>(ii) (a) 1/(2&radic;x) + (3/2)&radic;x<br>(iii) (b) 3x&sup2;+2x&minus;2<br>'
      '(iv) (c) &minus;ax/(by)<br>(v) (d) sec&sup2;x/(2y+1)<br>(vi) (d) 1/[2(&radic;x+x&radic;x)]<br>'
      '(vii) (b) &minus;tan&sup2;x<br>(viii) (b) 3<br>(ix) (c) 2e^(2x)(x&sup2;+x)<br>(x) (d) does not exist<br>'
      '(xi) (a) 1<br>(xii) (c) 1/&radic;(x&sup2;+1) + 1/&radic;(x&sup2;&minus;1)<br>(xiii) (c) a sech&sup2;ax<br>'
      '(xiv) (b) 2/(1&minus;4x&sup2;)<br>(xv) (d) e&#739;/2<br>(xvi) (c) 2',
      'Each option verified by direct differentiation; (v) and (xi) use y&sup2; = tan x &minus; y and the '
      'half-angle identity respectively; (xv) the inverse of ln 2x is e&#739;/2.',
      104),
    q('u3_rev3_q2', 3, REV3, 'REV3', 2,
      'Find the derivative of &radic;(cos x) and sec&radic;x by first principle.',
      '&minus;sin x/(2&radic;(cos x)) and sec&radic;x&middot;tan&radic;x/(2&radic;x)',
      'Rationalize / use sec A &minus; sec B = sec A sec B(cos B &minus; cos A) with sum-to-product, then take '
      'lim<sub>&delta;x&rarr;0</sub>.',
      106),
    q('u3_rev3_q3', 3, REV3, 'REV3', 3,
      'If y = (sin x)^(ln x), find dy/dx.',
      '(sin x)^(ln x)[ln(sin x)/x + cot x&middot;ln x]',
      'ln y = ln x&middot;ln(sin x); differentiate and multiply back by y.',
      106),
    q('u3_rev3_q4', 3, REV3, 'REV3', 4,
      'Find dy/dx if ax&sup2; + 2hxy + by&sup2; = 0.',
      'dy/dx = &minus;(ax+hy)/(hx+by)',
      'Implicit differentiation: 2ax + 2h(y + xy&prime;) + 2byy&prime; = 0.',
      106),
    q('u3_rev3_q5', 3, REV3, 'REV3', 5,
      'Let f(x) = cot&#8315;&sup1;(2x/(1&minus;x&sup2;)); find f&prime;(x) and f&prime;(&minus;&radic;3).',
      'f&prime;(x) = &minus;2/(1+x&sup2;); f&prime;(&minus;&radic;3) = &minus;1/2',
      'With x = tan&theta; the argument is tan 2&theta;, so f = &pi;/2 &minus; 2&theta; per branch and '
      'f&prime; = &minus;2/(1+x&sup2;). Note: the printed key&#39;s second value &pi;/6 is f(&minus;&radic;3), '
      'not f&prime;(&minus;&radic;3) (key misprint).',
      106),
    q('u3_rev3_q6', 3, REV3, 'REV3', 6,
      'x = 4(t &minus; sin t) and y = 4(1 + cos t); find dy/dx.',
      'dy/dx = &minus;cot(t/2)',
      '(dy/dt)/(dx/dt) = &minus;sin t/(1&minus;cos t) = &minus;cot(t/2) by half-angle identities.',
      106),
    q('u3_rev3_q7', 3, REV3, 'REV3', 7,
      'Differentiate w.r.t. x: (i) (x&sup2;+x&#8315;&sup1;)/(x&sup2;&minus;x&#8315;&sup1;)  '
      '(ii) (3x&minus;2)/&radic;(x&sup2;+1)',
      '(i) &minus;6x&sup2;/(x&sup3;&minus;1)&sup2; = &minus;6/(x&sup2;&minus;x&#8315;&sup1;)&sup2;<br>'
      '(ii) (2x+3)/(x&sup2;+1)^(3/2)',
      '(i) multiply top and bottom by x to get (x&sup3;+1)/(x&sup3;&minus;1); (ii) quotient rule then combine '
      'over (x&sup2;+1)^(3/2).',
      106),
    q('u3_rev3_q8', 3, REV3, 'REV3', 8,
      'If y = x&#8308; + 2x&sup2;, show that dy/dx = 4x&radic;(y+1).',
      'Shown: dy/dx = 4x&radic;(y+1)',
      'y+1 = (x&sup2;+1)&sup2;, so &radic;(y+1) = x&sup2;+1 and 4x(x&sup2;+1) = 4x&sup3;+4x = y&prime;.',
      106),
    q('u3_rev3_q9', 3, REV3, 'REV3', 9,
      'If y = &radic;(sin x + &radic;(sin x + &radic;(sin x + &hellip;))), show that (2y &minus; 1)y&prime; = cos x.',
      'Shown: (2y &minus; 1)y&prime; = cos x',
      'Infinite nesting gives y&sup2; = sin x + y; differentiate: 2yy&prime; = cos x + y&prime;.',
      106),
    q('u3_rev3_q10', 3, REV3, 'REV3', 10,
      'Differentiate w.r.t. x: (i) cosh(cos&#8315;&sup1;&radic;x)  (ii) tanh&#8315;&sup1;(cos 2x)',
      '(i) &minus;sinh(cos&#8315;&sup1;&radic;x)/(2&radic;(x&minus;x&sup2;))<br>(ii) &minus;2 cosec 2x',
      '(i) chain rule with d/dx cos&#8315;&sup1;&radic;x = &minus;1/(2&radic;x&radic;(1&minus;x)); '
      '(ii) (&minus;2 sin 2x)/(1&minus;cos&sup2;2x) = &minus;2/sin 2x.',
      106),
]

EX4_1 = 'Exercise 4.1'
SOLVED += [
    q('u4_ex41_q1', 4, EX4_1, 'EX4.1', 1,
      'Calculate the first, second and third order derivatives of y = cos&sup2;x.',
      'y&prime; = &minus;sin 2x, y&Prime; = &minus;2cos 2x, y&Prime;&prime; = 4 sin 2x',
      'Write y = (1+cos 2x)/2 first; each differentiation then doubles the coefficient.',
      114),
    q('u4_ex41_q2', 4, EX4_1, 'EX4.1', 2,
      'Find the 2nd order derivative of f(x) = cos x/(1+sin x).',
      'f&Prime;(x) = cos x/(1+sin x)&sup2;',
      'f&prime; simplifies to &minus;1/(1+sin x) because &minus;sin x(1+sin x) &minus; cos&sup2;x = &minus;(1+sin x).',
      114),
    q('u4_ex41_q3', 4, EX4_1, 'EX4.1', 3,
      'Find the fourth order derivatives: (i) h(t) = 3t&#8311; &minus; 6t&#8308; + 8t&sup3; &minus; 12t + 18  '
      '(ii) f(x) = &sup3;&radic;x &minus; 1/(8x&sup2;) &minus; &radic;x',
      '(i) h&#8308;(t) = 2520t&sup3; &minus; 144<br>'
      '(ii) f&#8308;(x) = &minus;80/(81&sup3;&radic;(x&sup1;&sup1;)) &minus; 15/x&#8310; + 15/(16&radic;(x&#8311;))',
      'Differentiate four times term by term; in (ii) keep fractional/negative powers until the end.',
      114),
    q('u4_ex41_q4', 4, EX4_1, 'EX4.1', 4,
      'Determine the fourth order derivative: (i) r(t) = 3t&sup2; + 8&radic;t  (ii) y = cos x  '
      '(iii) f(y) = sin 3y + e^(&minus;2y) + ln(7y)',
      '(i) &minus;15/(2t^(7/2))<br>(ii) cos x<br>(iii) 81 sin 3y + 16e^(&minus;2y) &minus; 6/y&#8308;',
      '(ii) the fourth derivative of cos x cycles back to cos x; (iii) ln(7y) contributes &minus;6/y&#8308;.',
      114),
    q('u4_ex41_q5', 4, EX4_1, 'EX4.1', 5,
      'If x&sup2; + y&sup2; = 10, find y&Prime;.',
      'y&Prime; = &minus;(x&sup2;+y&sup2;)/y&sup3;',
      'y&prime; = &minus;x/y, then differentiate the quotient and substitute back.',
      114),
    q('u4_ex41_q6', 4, EX4_1, 'EX4.1', 6,
      'Find d&sup2;y/dx&sup2; if: (i) 2y&sup2; + 6x&sup2; = 76  (ii) x&sup3; + y&sup3; = 1',
      '(i) &minus;3(3x&sup2;+y&sup2;)/y&sup3;<br>(ii) &minus;2x(x&sup3;+y&sup3;)/y&#8309;',
      'Implicit differentiation twice; in (ii) y&prime; = &minus;x&sup2;/y&sup2; and the numerator collapses using '
      'the original equation.',
      114),
    q('u4_ex41_q7', 4, EX4_1, 'EX4.1', 7,
      'Find d&sup2;y/dx&sup2; if: (i) x = &minus;5t&sup3; &minus; 7 and y = 3t&sup2; + 16  '
      '(ii) x = cos&theta; and y = sin&theta;',
      '(i) &minus;2/(75t&#8308;)<br>(ii) &minus;cosec&sup3;&theta;',
      'Parametric second derivative: d&sup2;y/dx&sup2; = [d/dt(dy/dx)]/(dx/dt).',
      115),
    q('u4_ex41_q8', 4, EX4_1, 'EX4.1', 8,
      'The derivative of r(t) is r&prime;(t) = 6t + 4t^(&minus;1/2) + e&#748;; find r&Prime;(t), r&Prime;&prime;(t) and '
      'r&#8308;(t).',
      'r&Prime;(t) = 6 &minus; 2t^(&minus;3/2) + e&#748;; r&Prime;&prime;(t) = 3t^(&minus;5/2) + e&#748;; '
      'r&#8308;(t) = &minus;(15/2)t^(&minus;7/2) + e&#748;',
      'Differentiate the given first derivative three more times.',
      115),
    q('u4_ex41_q9', 4, EX4_1, 'EX4.1', 9,
      'If x&sup2; + y&sup2; = 25, find d&sup2;y/dx&sup2; at the point (4, 3).',
      '&minus;25/27',
      'y&Prime; = &minus;(x&sup2;+y&sup2;)/y&sup3; = &minus;25/y&sup3;; at y = 3 this is &minus;25/27.',
      115),
    q('u4_ex41_q12', 4, EX4_1, 'EX4.1', 12,
      'Write MAPLE commands to find higher order derivatives: (i) f(x) = x&sup3;+3x&sup2;+6x+8 (third)  '
      '(ii) f(x) = cos&radic;(2x+3) (second)  (iii) f(x) = e^(x&sup2;+5x+3) (third)  '
      '(iv) f(x) = ln&radic;(3x+2) (second)  (v) f(x) = e^(sin x) (third)',
      '(i) &gt; diff(x^3+3*x^2+6*x+8, x$3);<br>(ii) &gt; diff(cos(sqrt(2*x+3)), x$2);<br>'
      '(iii) &gt; diff(exp(x^2+5*x+3), x$3);<br>(iv) &gt; diff(ln(sqrt(3*x+2)), x$2);<br>'
      '(v) &gt; diff(exp(sin(x)), x$3);',
      'MAPLE&#39;s x$n syntax repeats differentiation n times. The book skips Q10&ndash;11 and the key lists this '
      'item as 10.',
      115),
]

EX4_2 = 'Exercise 4.2'
SOLVED += [
    q('u4_ex42_q1', 4, EX4_2, 'EX4.2', 1,
      'Obtain the first three terms of the Maclaurin&#39;s series for: (i) cos x  (ii) e&#739;  (iii) ln(1+x)  '
      '(iv) sin&sup2;x  (v) e^(sin x)  (vi) xe^(&minus;x)  (vii) 1/(1+x)',
      '(i) 1 &minus; x&sup2;/2! + x&#8308;/4!<br>(ii) 1 + x + x&sup2;/2!<br>(iii) x &minus; x&sup2;/2 + x&sup3;/3<br>'
      '(iv) x&sup2; &minus; x&#8308;/3 + 2x&#8310;/45<br>(v) 1 + x + x&sup2;/2!<br>(vi) x &minus; x&sup2; + x&sup3;/2<br>'
      '(vii) 1 &minus; x + x&sup2;',
      'Evaluate f and its derivatives at 0; (iv) uses sin&sup2;x = (1&minus;cos 2x)/2.',
      122),
    q('u4_ex42_q2', 4, EX4_2, 'EX4.2', 2,
      'Find the first four terms of the Taylor&#39;s series: (i) ln x centered at a = 1  (ii) 1/x centered at a = 1  '
      '(iii) sin x centered at a = &pi;/4  (iv) cos x centered at a = &pi;/2',
      '(i) (x&minus;1) &minus; (x&minus;1)&sup2;/2 + (x&minus;1)&sup3;/3 &minus; (x&minus;1)&#8308;/4<br>'
      '(ii) 1 &minus; (x&minus;1) + (x&minus;1)&sup2; &minus; (x&minus;1)&sup3;<br>'
      '(iii) (1/&radic;2)[1 + (x&minus;&pi;/4) &minus; (x&minus;&pi;/4)&sup2;/2! &minus; (x&minus;&pi;/4)&sup3;/3!]<br>'
      '(iv) &minus;(x&minus;&pi;/2) + (x&minus;&pi;/2)&sup3;/3! &minus; (x&minus;&pi;/2)&#8309;/5! + (x&minus;&pi;/2)&#8311;/7!',
      'Taylor coefficients f&#8345;(a)/n!; in (iv) the even-order terms vanish at &pi;/2.',
      122),
    q('u4_ex42_q3', 4, EX4_2, 'EX4.2', 3,
      'Does the Maclaurin&#39;s series of f(x) = 1/x, g(x) = cosec x and h(x) = &radic;x exist? If not, why? '
      'Give appropriate justification.',
      'No &mdash; none of the three has a Maclaurin series.',
      'f and g are not defined at x = 0, and for all three the derivatives of all orders fail to exist at 0 '
      '(h&prime;(x) = 1/(2&radic;x) &rarr; &infin; as x &rarr; 0&#8314;).',
      122),
    q('u4_ex42_q4', 4, EX4_2, 'EX4.2', 4,
      'Write MAPLE commands to find the Taylor expression: (i) e&#739; at x = 1 upto 10 terms  '
      '(ii) sin x at x = &pi; upto 10 terms  (iii) cos x at x = &pi; upto 10 terms  (iv) ln(1+x) at x = 0 upto 10 terms  '
      '(v) 1/x at x = 1 upto 5 terms  (vi) 1/x at x = 2 upto 5 terms',
      '(i) &gt; taylor(exp(x), x = 1, 10)<br>(ii) &gt; taylor(sin(x), x = &pi;, 10)<br>'
      '(iii) &gt; taylor(cos(x), x = &pi;, 10)<br>(iv) &gt; taylor(ln(1+x), x = 0, 10)<br>'
      '(v) &gt; taylor(1/x, x = 1, 5)<br>(vi) &gt; taylor(1/x, x = 2, 5)',
      'taylor(expression, x = a, n) expands about a with n terms.',
      123),
]

EX4_3 = 'Exercise 4.3'
SOLVED += [
    q('u4_ex43_q1', 4, EX4_3, 'EX4.3', 1,
      'Determine the slope of the tangent to the curve y = x&sup3; at the point (3/2, 27/8).',
      '27/4',
      'y&prime; = 3x&sup2; evaluated at x = 3/2.',
      127),
    q('u4_ex43_q2', 4, EX4_3, 'EX4.3', 2,
      'Find the slope of the tangents to the curve x&sup2; + y&sup2; = 25 at the points on it whose x-coordinate is 2.',
      '2/&radic;21 or &minus;2/&radic;21',
      'y = &plusmn;&radic;21 and y&prime; = &minus;x/y.',
      127),
    q('u4_ex43_q3', 4, EX4_3, 'EX4.3', 3,
      'Find the equation of the tangent and the equation of the normal to the curve y = x + 1/x at the point '
      'where x = 2.',
      'Tangent: 3x &minus; 4y + 4 = 0; Normal: 8x + 6y &minus; 31 = 0',
      'Point (2, 5/2), slope 3/4; normal slope &minus;4/3.',
      127),
    q('u4_ex43_q4', 4, EX4_3, 'EX4.3', 4,
      'Given two curves y = x&sup2; and y = (x&minus;3)&sup2;. Find the angle between them.',
      '&theta; = tan&#8315;&sup1;(3/4) &asymp; 37&deg;',
      'They meet at (3/2, 9/4) with slopes 3 and &minus;3; tan&theta; = |(m&#8321;&minus;m&#8322;)/(1+m&#8321;m&#8322;)| = 3/4.',
      127),
    q('u4_ex43_q5', 4, EX4_3, 'EX4.3', 5,
      'Prove that the tangent lines to the curve y&sup2; = 4ax at the points where x = a are at right angles '
      'to each other.',
      'Proved: slopes 1 and &minus;1, product &minus;1',
      'y&prime; = 2a/y and at x = a, y = &plusmn;2a.',
      127),
    q('u4_ex43_q6', 4, EX4_3, 'EX4.3', 6,
      'At what points on the curve x&sup2; + y&sup2; &minus; 2x &minus; 4y + 1 = 0 is the tangent parallel to the y-axis?',
      '(3, 2) and (&minus;1, 2)',
      'y&prime; = (1&minus;x)/(y&minus;2) is undefined at y = 2; substituting gives x&sup2;&minus;2x&minus;3 = 0.',
      127),
]

EX4_4 = 'Exercise 4.4'
SOLVED += [
    q('u4_ex44_q1', 4, EX4_4, 'EX4.4', 1,
      'Show that the function f(x) = &minus;x&sup2; + 10x + 9 is increasing at x = 4.',
      'Shown: f&prime;(4) = 2 &gt; 0, so f is increasing at x = 4',
      'f&prime;(x) = &minus;2x + 10.',
      134),
    q('u4_ex44_q2', 4, EX4_4, 'EX4.4', 2,
      'Show that f(x) = tan&sup2;x is decreasing at x = 3&pi;/4.',
      'Shown: f&prime;(3&pi;/4) = &minus;4 &lt; 0, so f is decreasing there',
      'f&prime;(x) = 2 tan x sec&sup2;x; tan(3&pi;/4) = &minus;1, sec&sup2;(3&pi;/4) = 2.',
      134),
    q('u4_ex44_q3', 4, EX4_4, 'EX4.4', 3,
      'Find the maximum and minimum values, if any, of f : &real; &rarr; &real;: (i) x&sup2;&minus;2x+3  '
      '(ii) x&sup3;&minus;9x&sup2;+15x+3  (iii) &minus;x&#8308;+2x&sup2;  (iv) e&#739; sin x  (v) 2e&#739; + e^(&minus;x)  '
      '(vi) 2x &minus; x&sup2;',
      '(i) minimum at x = 1 (value 2)<br>(ii) relative maximum f(1) = 10; relative minimum f(5) = &minus;22<br>'
      '(iii) relative minimum f(0) = 0; relative maxima f(&plusmn;1) = 1<br>'
      '(iv) relative minimum &minus;e^(&minus;&pi;/4)/&radic;2 &asymp; &minus;0.322 at x = &minus;&pi;/4; relative maximum '
      'e^(3&pi;/4)/&radic;2 &asymp; 7.46 at x = 3&pi;/4<br>(v) relative minimum 2&radic;2 &asymp; 2.828 at '
      'x = &minus;(ln 2)/2<br>(vi) relative maximum f(1) = 1',
      'Second-derivative test at each critical point. Key&#39;s printed values for (ii) and (iv) are garbled '
      '(see solution file flags); the values above are the verified ones.',
      134),
    q('u4_ex44_q4', 4, EX4_4, 'EX4.4', 4,
      'A rectangular reservoir with a square bottom and open top is to be lined inside with lead. Find the '
      'dimensions to hold a&sup3;/2 cubic metres so that the lead required is minimum.',
      'Length = a, breadth = a, height = a/2',
      'S = x&sup2; + 2a&sup3;/x with x the base side; S&prime; = 0 gives x = a and then h = a/2.',
      134),
    q('u4_ex44_q5', 4, EX4_4, 'EX4.4', 5,
      'Find a right-angled triangle of maximum area with a hypotenuse of length h.',
      'Isosceles right triangle with legs h/&radic;2; maximum area h&sup2;/4',
      'Maximize A&sup2; = x&sup2;(h&sup2;&minus;x&sup2;)/4 over the leg x.',
      134),
    q('u4_ex44_q6', 4, EX4_4, 'EX4.4', 6,
      'A particle moves so that its distance s at time t is given by s = ut + &frac12;at&sup2; (u, a fixed). '
      'Find its speed and the magnitude of its acceleration at time t.',
      'Speed = u + at; acceleration = a',
      'v = ds/dt and a = dv/dt.',
      134),
]

REV4 = 'Review Exercise 4'
SOLVED += [
    q('u4_rev4_q1', 4, REV4, 'REV4', 1,
      'Choose the correct answer: (i) If y = 1/x then y&#8244;(1) = (a) 6 (b) &minus;6 (c) 2 (d) none  '
      '(ii) The nth derivative of 2e&#739; is (a) 2ne&#739; (b) 2e^(nx) (c) 2e&#739; (d) e&#739;/2  '
      '(iii) If xy = k&sup2; then y&Prime; = (a) 2k&sup2;/x (b) &minus;2k&sup2;/x&sup3; (c) 3k&sup2;/x&sup3; (d) 2k&sup2;/x&sup3;  '
      '(iv) The third derivative of 2&#739; is (a) (ln3)&sup2;e^(xln2) (b) (ln2)&sup3;e^(xln3) (c) (ln2)&sup3;e^(xln2) (d) none  '
      '(v) The second derivative of A sin x + B cos x is (a) f(x) (b) &minus;f(x) (c) &plusmn;f(x) (d) none  '
      '(vi) d&sup2;S/dt&sup2; gives (a) velocity (b) deceleration (c) acceleration (d) average velocity  '
      '(vii) If y = tan&#8315;&sup1;x then y&Prime;(1) = (a) &minus;1/2 (b) 1/4 (c) &minus;1/4 (d) 1/2  '
      '(viii) y = x &minus; x&sup3;/3! + x&#8309;/5! &minus; &hellip; is the Maclaurin series of (a) sin x (b) cos x (c) e&#739; (d) none  '
      '(ix) f is decreasing when for x<sub>1</sub> &lt; x<sub>2</sub> (a) f(x<sub>1</sub>) &lt; f(x<sub>2</sub>) '
      '(b) f(x<sub>1</sub>) &gt; f(x<sub>2</sub>) (c) &ge; (d) &le;  '
      '(x) A point where f&prime;(c) = 0 is called (a) maximum (b) minimum (c) stationary (d) critical',
      '(i) (b) &minus;6<br>(ii) (c) 2e&#739;<br>(iii) (d) 2k&sup2;/x&sup3;<br>(iv) (c) (ln2)&sup3;e^(xln2)<br>'
      '(v) (b) &minus;f(x)<br>(vi) (c) acceleration<br>(vii) (a) &minus;1/2<br>(viii) (a) sin x<br>'
      '(ix) (b) f(x<sub>1</sub>) &gt; f(x<sub>2</sub>)<br>(x) (c) stationary point',
      '(i) y&#8244; = &minus;6x^(&minus;4). (iii) y = k&sup2;/x. (iv) 2&#739; = e^(x ln2). '
      '(vii) y&Prime; = &minus;2x/(1+x&sup2;)&sup2;. All ten match the answers key.',
      134),
    q('u4_rev4_q2', 4, REV4, 'REV4', 2,
      'Find the second derivative of ln(1 + x&sup2;).',
      '2(1 &minus; x&sup2;)/(1 + x&sup2;)&sup2;',
      'y&prime; = 2x/(1+x&sup2;); quotient rule gives y&Prime; = [2(1+x&sup2;) &minus; 4x&sup2;]/(1+x&sup2;)&sup2;.',
      135),
    q('u4_rev4_q3', 4, REV4, 'REV4', 3,
      'If x = 3u&sup2; + 1 and y = 3u&sup2; + 5u, find d&sup2;y/dx&sup2;.',
      '&minus;5/(36u&sup3;)',
      'dy/dx = (6u+5)/(6u) = 1 + (5/6)u^(&minus;1); differentiate in u and divide by dx/du = 6u.',
      135),
    q('u4_rev4_q4', 4, REV4, 'REV4', 4,
      'Find the third derivatives: (i) v = x&sup3; &minus; x&sup2; + x &minus; 1  '
      '(ii) f = 7 sin(x/3) + cos(1 &minus; 2x)  (iii) y = e^(&minus;5x) + 8 ln(2x&#8308;)',
      '(i) 6<br>(ii) &minus;(7/27) cos(x/3) &minus; 8 sin(1 &minus; 2x)<br>(iii) &minus;125e^(&minus;5x) + 64/x&sup3;',
      '(iii) 8 ln(2x&#8308;) = 8 ln 2 + 32 ln x, so y&prime; = &minus;5e^(&minus;5x) + 32/x.',
      135),
    q('u4_rev4_q5', 4, REV4, 'REV4', 5,
      'Find the second derivatives: (i) g = sin(2x&sup3; &minus; 9x)  (ii) z = ln(7 &minus; x&sup3;)  '
      '(iii) q = 2/(6 + 2x &minus; x&sup2;)&#8308;  (iv) h = cos&sup2;(7t)  (v) 2x&sup3; + y&sup2; = 1 &minus; 4y  '
      '(vi) 6y &minus; xy&sup2; = 1',
      '(i) 12x cos(2x&sup3;&minus;9x) &minus; (6x&sup2;&minus;9)&sup2; sin(2x&sup3;&minus;9x)<br>'
      '(ii) (&minus;42x &minus; 3x&#8308;)/(7 &minus; x&sup3;)&sup2;<br>'
      '(iii) 16(6+2x&minus;x&sup2;)^(&minus;5) + 40(2&minus;2x)&sup2;(6+2x&minus;x&sup2;)^(&minus;6)<br>'
      '(iv) 98 sin&sup2;(7t) &minus; 98 cos&sup2;(7t)<br>'
      '(v) &minus;6x(y+2)^(&minus;1) &minus; 9x&#8308;(y+2)^(&minus;3)<br>'
      '(vi) 2y&sup3;(6&minus;2xy)^(&minus;2) [2 + xy(6&minus;2xy)^(&minus;1)]',
      '(v) implicit: y&prime; = &minus;3x&sup2;/(y+2). (vi) implicit: y&prime; = y&sup2;/(6&minus;2xy). '
      '(iv) h&prime; = &minus;7 sin(14t), h&Prime; = &minus;98 cos(14t).',
      135),
    q('u4_rev4_q6', 4, REV4, 'REV4', 6,
      'If y = cos x, find y&prime;, y&Prime;, y&#8244; and y&#8279;.',
      'y&prime; = &minus;sin x; y&Prime; = &minus;cos x; y&#8244; = sin x; y&#8279; = cos x',
      'Successive differentiation cycles with period 4.',
      135),
    q('u4_rev4_q7', 4, REV4, 'REV4', 7,
      'If x = 4 sin t and y = 5 cos t, find d&sup2;y/dx&sup2;.',
      '&minus;5/(16 cos&sup3;t)',
      'dy/dx = &minus;(5/4) tan t; divide d/dt of that by dx/dt = 4 cos t.',
      135),
    q('u4_rev4_q8', 4, REV4, 'REV4', 8,
      'Find the rth derivative of x&#8345; for r &le; n.',
      'n!/(n &minus; r)! &middot; x^(n &minus; r)',
      'Each differentiation drops the exponent by 1 and multiplies by the current exponent; '
      'the key&#39;s printed form is garbled (see solution file flags).',
      135),
    q('u4_rev4_q9', 4, REV4, 'REV4', 9,
      'Obtain the Taylor series for f(x) = x&#8308; + x &minus; 2 at a = 1.',
      '5(x&minus;1) + 6(x&minus;1)&sup2; + 4(x&minus;1)&sup3; + (x&minus;1)&#8308;',
      'f(1) = 0, f&prime;(1) = 5, f&Prime;(1)/2! = 6, f&#8244;(1)/3! = 4, f&#8279;(1)/4! = 1.',
      135),
    q('u4_rev4_q10', 4, REV4, 'REV4', 10,
      'Obtain the Taylor series for the function (x &minus; 1)e&#739; near x = 1.',
      'e(x&minus;1) + e(x&minus;1)&sup2; + (e/2)(x&minus;1)&sup3; + (e/6)(x&minus;1)&#8308; + &hellip;',
      'f(1) = 0; f&prime; = xe&#739;, f&Prime; = (1+x)e&#739;, f&#8244; = (2+x)e&#739;, '
      'f&#8279; = (3+x)e&#739;, evaluated at x = 1 and divided by k!.',
      136),
    q('u4_rev4_q11', 4, REV4, 'REV4', 11,
      'Find the Maclaurin series for ln(1 + x) and hence find that for ln((1+x)/(1&minus;x)).',
      'ln(1+x) = x &minus; x&sup2;/2 + x&sup3;/3 &minus; &hellip;;  '
      'ln((1+x)/(1&minus;x)) = 2(x + x&sup3;/3 + x&#8309;/5 + &hellip;) = 2&Sigma; x^(2n&minus;1)/(2n&minus;1)',
      'Subtract the series of ln(1&minus;x) = &minus;(x + x&sup2;/2 + x&sup3;/3 + &hellip;) from that of ln(1+x); '
      'even powers cancel.',
      136),
    q('u4_rev4_q12', 4, REV4, 'REV4', 12,
      'Find the equation of the tangent line to the curve y = x&sup3; &minus; 3x&sup2; + x at the point (2, &minus;2).',
      'y = x &minus; 4',
      'y&prime; = 3x&sup2; &minus; 6x + 1 gives slope 1 at x = 2; point-slope form.',
      136),
    q('u4_rev4_q13', 4, REV4, 'REV4', 13,
      'At what point on the graph of y = x&sup2; is the tangent line parallel to the line 3x &minus; y = 2?',
      '(3/2, 9/4)',
      'Slope of the line is 3; set y&prime; = 2x = 3.',
      136),
    q('u4_rev4_q14', 4, REV4, 'REV4', 14,
      'Determine the interval on which the function f(x) = x&sup2; &minus; 3x + 1 is increasing and decreasing.',
      'Increasing on (3/2, &infin;); decreasing on (&minus;&infin;, 3/2)',
      'f&prime;(x) = 2x &minus; 3 changes sign at x = 3/2.',
      136),
]

EX5_1 = 'Exercise 5.1'
SOLVED += [
    q('u5_ex51_q1', 5, EX5_1, 'EX5.1', 1,
      'Find the domain of the following vector functions: (i) r(t) = 2t i&#770; &minus; 3t j&#770; + (1/t) k&#770;  '
      '(ii) r(t) = sin t i&#770; + cos t j&#770; + tan t k&#770;  (iii) r(t) = (1 &minus; t) i&#770; + &radic;t j&#770; + (1/t&sup2;) k&#770;  '
      '(iv) g(t) = cos t i&#770; &minus; cot t j&#770; + cosec t k&#770;',
      '(i) &reals; &minus; {0}<br>(ii) &reals; &minus; {(2n+1)&pi;/2, n &isin; &integers;}<br>'
      '(iii) &reals;&plus; (t &gt; 0)<br>(iv) &reals; &minus; {n&pi;, n &isin; &integers;}',
      'The domain is the intersection of the component domains: (i) 1/t needs t &ne; 0; (ii) tan t fails at odd '
      'multiples of &pi;/2; (iii) &radic;t needs t &ge; 0 and 1/t&sup2; needs t &ne; 0; (iv) cot t and cosec t fail at n&pi;.',
      141),
    q('u5_ex51_q2', 5, EX5_1, 'EX5.1', 2,
      'Find the limit of the vector function r(t) = (e^(3t) &minus; 1) i&#770; + (&radic;(3+t) &minus; &radic;3)/(3t) j&#770; '
      '+ 1/(9t+1) k&#770; at t = 0.',
      '(1/(6&radic;3)) j&#770; + k&#770;',
      'Component limits: e^(3t)&minus;1 &rarr; 0; rationalizing the j&#770; component gives '
      '1/(3(&radic;(3+t)+&radic;3)) &rarr; 1/(6&radic;3); 1/(9t+1) &rarr; 1.',
      141),
    q('u5_ex51_q3', 5, EX5_1, 'EX5.1', 3,
      'If u(t) = t&sup2; i&#770; &minus; 2 j&#770; and v(t) = 2t i&#770; &minus; 5 k&#770; are vector functions and h = 3t is a '
      'scalar function, find: (i) lim<sub>t&rarr;0</sub> [u(t) + v(t)]  (ii) lim<sub>t&rarr;1</sub> [u(t) &middot; v(t)]  '
      '(iii) lim<sub>t&rarr;1</sub> [u(t) &times; v(t)]  (iv) lim<sub>t&rarr;5</sub> [h u(t)]',
      '(i) &minus;2 j&#770; &minus; 5 k&#770;<br>(ii) 2<br>(iii) 10 i&#770; + 5 j&#770; + 4 k&#770;<br>(iv) 375 i&#770; &minus; 30 j&#770;',
      'Evaluate componentwise at the limit point; (iii) (i&#770; &minus; 2j&#770;) &times; (2i&#770; &minus; 5k&#770;) = '
      '5j&#770; + 4k&#770; + 10i&#770;. The key prints (i) as &minus;2i&#770; &minus; 5k&#770; (unit-vector misprint); '
      'the verified sum is &minus;2j&#770; &minus; 5k&#770;.',
      142),
    q('u5_ex51_q4', 5, EX5_1, 'EX5.1', 4,
      'Show that the function R(t) = sin&sup2;t i&#770; + tan t j&#770; + (1/t) k&#770; is continuous at t = &pi;/4.',
      'Shown: lim<sub>t&rarr;&pi;/4</sub> R(t) = &frac12; i&#770; + j&#770; + (4/&pi;) k&#770; = R(&pi;/4)',
      'Each component (sin&sup2;t, tan t, 1/t) is continuous at &pi;/4, so the limit equals the value.',
      142),
    q('u5_ex51_q5', 5, EX5_1, 'EX5.1', 5,
      'Show that the function r(t) = (2/t) i&#770; + t&sup3;/(2t&sup3; &minus; 5) j&#770; + (1/e&#748;) k&#770; is continuous '
      'as t &rarr; &infin;.',
      'Shown: lim<sub>t&rarr;&infin;</sub> r(t) = &frac12; j&#770;, a finite vector, so the limit exists',
      '2/t &rarr; 0; t&sup3;/(2t&sup3;&minus;5) = 1/(2 &minus; 5/t&sup3;) &rarr; 1/2; e^(&minus;t) &rarr; 0.',
      142),
    q('u5_ex51_q6', 5, EX5_1, 'EX5.1', 6,
      'For what values of t are the following vector functions continuous: (i) r(t) = ln(t+3) i&#770; + 1/(t&minus;1) j&#770; '
      '+ (t+2)/(t&sup2;&minus;4) k&#770;  (ii) r(t) = 1/(3t+1) i&#770; + (1/t) j&#770;',
      '(i) all t &gt; &minus;3 with t &ne; 1 and t &ne; &plusmn;2<br>(ii) all t &ne; 0 and t &ne; &minus;1/3',
      'Intersect the component continuity sets: (i) ln(t+3) needs t &gt; &minus;3, 1/(t&minus;1) needs t &ne; 1, '
      '(t+2)/(t&sup2;&minus;4) needs t &ne; &plusmn;2.',
      142),
]

EX5_2 = 'Exercise 5.2'
SOLVED += [
    q('u5_ex52_q1', 5, EX5_2, 'EX5.2', 1,
      'Find the derivative of the following vector functions: (i) f(t) = ln t&sup2; i&#770; + e^(2t) j&#770; + (2t&sup2; + 1) k&#770;  '
      '(ii) f(t) = (t + 1) i&#770; + ln(t + 2) j&#770;  (iii) f(t) = sec t i&#770; + cos t&sup2; j&#770; + (t&sup2; + t + 1) k&#770;',
      '(i) (2/t) i&#770; + 2e^(2t) j&#770; + 4t k&#770;<br>(ii) i&#770; + 1/(t+2) j&#770;<br>'
      '(iii) sec t tan t i&#770; &minus; 2t sin t&sup2; j&#770; + (2t + 1) k&#770;',
      'Differentiate componentwise; (i) d/dt ln t&sup2; = 2t/t&sup2; = 2/t; (iii) chain rule on cos t&sup2; and sec t.',
      149),
    q('u5_ex52_q2', 5, EX5_2, 'EX5.2', 2,
      'If x(t) = t i&#770; + 2t j&#770; and y(t) = 2t i&#770; + 3t k&#770; are vector functions and &Oslash;(t) = 3t is a scalar '
      'function, find: (i) d/dt [x &minus; y]  (ii) d/dt [x &middot; y]  (iii) d/dt [x &times; y]  (iv) d/dt [&Oslash; x]',
      '(i) &minus;i&#770; + 2 j&#770; &minus; 3 k&#770;<br>(ii) 4t<br>(iii) 12t i&#770; &minus; 6t j&#770; &minus; 8t k&#770;<br>'
      '(iv) 6t i&#770; + 12t j&#770;',
      '(ii) x&middot;y = 2t&sup2;. (iii) x&times;y = 6t&sup2; i&#770; &minus; 3t&sup2; j&#770; &minus; 4t&sup2; k&#770;. '
      '(iv) &Oslash;x = 3t&sup2; i&#770; + 6t&sup2; j&#770;.',
      149),
    q('u5_ex52_q3', 5, EX5_2, 'EX5.2', 3,
      'A particle moves so that its position as a function of time is r(t) = i&#770; + 4t&sup2; j&#770; + t k&#770;. '
      'Write expressions for its (a) velocity and (b) acceleration as functions of time.',
      '(a) v = 8t j&#770; + k&#770;<br>(b) a = 8 j&#770;',
      'v = dr/dt and a = dv/dt, componentwise.',
      149),
    q('u5_ex52_q4', 5, EX5_2, 'EX5.2', 4,
      'The path of a particle is given for time t &gt; 0 by x = t&sup2; &minus; 3t and y = (2/3)t&sup3;. Find the magnitude '
      'of velocity and acceleration of the particle at t = 5.',
      '|v| = &radic;2549; |a| = &radic;404',
      'v = (2t&minus;3, 2t&sup2;) &rarr; (7, 50); a = (2, 4t) &rarr; (2, 20); take magnitudes.',
      149),
    q('u5_ex52_q5', 5, EX5_2, 'EX5.2', 5,
      'A particle moves along the curve x = 2t&sup2; and y = 4t. Find the component of velocity and acceleration '
      'at t = 2 in the direction of 2 i&#770; + j&#770;.',
      'Velocity component = 4&radic;5; acceleration component = 8/&radic;5 = 8&radic;5/5 &asymp; 3.58',
      'v(2) = (8, 4), a = (4, 0); project on u = (2i&#770;+j&#770;)/&radic;5. The key&#39;s &quot;acceleration component = 4&quot; '
      'is |a|, not the component along 2i&#770;+j&#770; (see solution file flags).',
      150),
]

REV5 = 'Review Exercise 5'
SOLVED += [
    q('u5_rev5_q1', 5, REV5, 'REV5', 1,
      'Choose the correct answer: (i) domain of r(t) = t&sup3; i&#770; + 1/(t&minus;1) j&#770; + ln(t&minus;2) k&#770; is '
      '(a) {t &gt; 2} (b) {t &lt; 2} (c) {t &gt; 0} (d) {t &gt; 1}  (ii) F(t) = cos t i&#770; + sin 2t k&#770; at t = &pi; is '
      '(a) not continuous (b) continuous (c) limit does not exist (d) none  (iii) F(t) = 1/(t&minus;2) i&#770; + sin t j&#770; '
      'is continuous for (a) t &ne; 2 (b) t &gt; 2 (c) t &le; 2 (d) all t  (iv) u = t&sup2; i&#770; &minus; e^(2t) j&#770;, '
      'h(t) = t&sup2;+2t&minus;2: lim<sub>t&rarr;0</sub> [h u] = (a) &minus;j&#770; (b) j&#770; (c) 2j&#770; (d) &minus;2j&#770;  '
      '(v) u = t&sup2; i&#770; &minus; e^(2t) j&#770;, v = &minus;2 i&#770; &minus; t&sup2; k&#770;: lim<sub>t&rarr;0</sub> [u&middot;v] = '
      '(a) 0 (b) t&#8308; (c) t&sup2;&minus;e^(2t) (d) &minus;2t&sup2;  (vi) f(t) = t&sup2; i&#770; &minus; e^(2t) j&#770; then f&prime;(t) = '
      '(a) 2t i&#770;&minus;2e^(2t) j&#770; (b) 2t i&#770;&minus;e^(2t) j&#770; (c) 2t i&#770;&minus;2te^(2t) j&#770; (d) none  '
      '(vii) velocity of r(t) = (1/(2&pi;)) t i&#770; + 3 cos t j&#770; at t = &pi;/2 is (a) (1/2&pi;)i&#770;+3j&#770; (b) (1/2&pi;)i&#770; '
      '(c) (1/2&pi;)i&#770;&minus;3j&#770; (d) none  (viii) magnitude of velocity of r(t) = 4cos t i&#770; + 4sin t j&#770; + '
      '(3/(2&pi;))t&sup2; k&#770; at t = &pi; is (a) &radic;5 (b) 5 (c) &radic;(5&pi;) (d) 5&pi;  (ix) magnitude of acceleration of the '
      'same r at t = &pi;/2 is (a) &radic;(16&pi;&sup2;+9)/&pi; (b) &radic;(16&pi;&sup2;+9) (c) &radic;(16&pi;&sup2;+9)/&pi;&sup2; '
      '(d) &radic;(16+9&pi;&sup2;)/&pi;  (x) if a = 2 i&#770; + 3 j&#770; + 5 k&#770; then da/dt = (a) 10 (b) &radic;38 (c) 0 (d) none',
      '(i) (a) {t &gt; 2}<br>(ii) (b) is continuous<br>(iii) (a) t &ne; 2<br>(iv) (c) 2j&#770;<br>(v) (a) 0<br>'
      '(vi) (a) 2t i&#770; &minus; 2e^(2t) j&#770;<br>(vii) (c) (1/2&pi;) i&#770; &minus; 3 j&#770;<br>(viii) (b) 5<br>'
      '(ix) (a) &radic;(16&pi;&sup2;+9)/&pi;<br>(x) (c) 0',
      '(iv) h(0)u(0) = (&minus;2)(&minus;j&#770;) = 2j&#770;. (viii) v(&pi;) = (0,&minus;4,3). (ix) a(&pi;/2) = (0,&minus;4,3/&pi;). '
      '(x) a is constant. All ten match the answers key.',
      150),
    q('u5_rev5_q2', 5, REV5, 'REV5', 2,
      'Find the limit of the vector function r(t) = 2t i&#770; + t&sup3; j&#770; + k&#770; when t &rarr; 2.',
      '4 i&#770; + 8 j&#770; + k&#770;',
      'Take the limit of each component at t = 2.',
      151),
    q('u5_rev5_q3', 5, REV5, 'REV5', 3,
      'If u = 5 i&#770; &minus; 2t j&#770; and v = i&#770; &minus; 3t k&#770; are vector functions and k = t + 1 is a scalar function, '
      'find: (i) lim<sub>t&rarr;0</sub> [u &minus; v]  (ii) lim<sub>t&rarr;1</sub> [u &middot; v]  '
      '(iii) lim<sub>t&rarr;1</sub> [u &times; v]  (iv) lim<sub>t&rarr;5</sub> [k u]',
      '(i) 4 i&#770;<br>(ii) 5<br>(iii) 6 i&#770; + 15 j&#770; + 2 k&#770;<br>(iv) 30 i&#770; &minus; 60 j&#770;',
      '(iii) (5i&#770;&minus;2j&#770;)&times;(i&#770;&minus;3k&#770;) = 15j&#770; + 2k&#770; + 6i&#770;. (iv) k(5)u(5) = 6(5i&#770;&minus;10j&#770;).',
      151),
    q('u5_rev5_q4', 5, REV5, 'REV5', 4,
      'Check the continuity of the function G(t) = (t + 8) i&#770; + 6/(t&minus;8) j&#770; + ln(t + 8) k&#770; at t = 0.',
      'Continuous: lim<sub>t&rarr;0</sub> G(t) = 8 i&#770; &minus; (3/4) j&#770; + ln 8 k&#770; = G(0)',
      'Each component is continuous at t = 0 (t = 8 and t = &minus;8 are the only trouble points).',
      151),
    q('u5_rev5_q5', 5, REV5, 'REV5', 5,
      'For what values of t is the vector function r(t) = &radic;(36 &minus; t&sup2;) i&#770; + ln(t + 4) j&#770; continuous?',
      '&minus;4 &lt; t &le; 6',
      '36 &minus; t&sup2; &ge; 0 gives &minus;6 &le; t &le; 6; ln(t+4) needs t &gt; &minus;4; intersect.',
      151),
    q('u5_rev5_q6', 5, REV5, 'REV5', 6,
      'Find f&prime;(t) of the following vector functions: (i) f(t) = e^(t&#8308;) i&#770; + (t&sup3; + 3) j&#770; + cosec t&sup2; k&#770;  '
      '(ii) f(t) = (1/t) i&#770; + e^(2t&sup3;) j&#770; + sec t&sup3; k&#770;',
      '(i) 4t&sup3;e^(t&#8308;) i&#770; + 3t&sup2; j&#770; &minus; 2t cosec t&sup2; cot t&sup2; k&#770;<br>'
      '(ii) &minus;(1/t&sup2;) i&#770; + 6t&sup2;e^(2t&sup3;) j&#770; + 3t&sup2; sec t&sup3; tan t&sup3; k&#770;',
      'Chain rule on each component. The key prints the i&#770; component of (ii) as &quot;ln t&quot; (misprint); '
      'd/dt(1/t) = &minus;1/t&sup2;.',
      151),
    q('u5_rev5_q7', 5, REV5, 'REV5', 7,
      'A particle moves along the curve x = t&sup3; + 2t, y = 3e^(&minus;2t), z = 2 sin(5t) (distances in cm, time in s). '
      'Find the magnitude of the acceleration of the particle at t = 0.',
      '|a| = 12',
      'a = (6t, 12e^(&minus;2t), &minus;50 sin 5t); at t = 0 this is (0, 12, 0).',
      151),
    q('u5_rev5_q8', 5, REV5, 'REV5', 8,
      'The path of a particle is given for time t &gt; 0 by x = t + 2/t and y = 3t&sup2;. Find the velocity of the particle '
      'when t = 1 and the acceleration at t = 2.',
      'v(1) = &minus;i&#770; + 6 j&#770;; a(2) = &frac12; i&#770; + 6 j&#770;',
      'v = (1 &minus; 2/t&sup2;, 6t); a = (4/t&sup3;, 6).',
      151),
]

EX6_1 = 'Exercise 6.1'
SOLVED += [
    q('u6_ex61_q1', 6, EX6_1, 'EX6.1', 1,
      'Evaluate by standard formulae: (i) &int;9x&#8309; dx  (ii) &int;15/x&sup3; dx  (iii) &int;a/&radic;(bx) dx  '
      '(iv) &int;b y^(2/3) dy  (v) &int;(3x&sup2;&minus;9x+5) dx  (vi) &int;(2x&#8315;&#8309;+3x&#8315;&sup2;) dx  '
      '(vii) &int;(x&#8309;+3x&sup3;&minus;5x+6)/x&#8308; dx  (viii) &int;(cos x+3 sin x) dx  (ix) &int;(3 sec x&minus;cosec x) dx  '
      '(x) &int;(2 tan x&minus;5 sec x) dx  (xi) &int;(9e&#739;&minus;3 cos x&minus;5 sin x) dx  (xii) &int;(sec&sup2;x+cosec&sup2;x) dx',
      '(i) (3/2)x&#8310; + C<br>(ii) &minus;15/(2x&sup2;) + C<br>(iii) 2a&radic;(x/b) + C<br>(iv) (3/5)b y^(5/3) + C<br>'
      '(v) x&sup3; &minus; (9/2)x&sup2; + 5x + C<br>(vi) &minus;1/(2x&#8308;) &minus; 3/x + C<br>'
      '(vii) x&sup2;/2 + 3 ln|x| + 5/(2x&sup2;) &minus; 2/x&sup3; + C<br>(viii) sin x &minus; 3 cos x + C<br>'
      '(ix) ln|(sec x+tan x)&sup3;/(cosec x&minus;cot x)| + C<br>(x) ln|sec&sup2;x/(sec x+tan x)&#8309;| + C<br>'
      '(xi) 9e&#739; &minus; 3 sin x + 5 cos x + C<br>(xii) tan x &minus; cot x + C',
      'Power rule term by term; (ix)&ndash;(x) use &int;sec = ln|sec+tan|, &int;cosec = ln|cosec&minus;cot|, &int;tan = ln|sec|.',
      159),
    q('u6_ex61_q2', 6, EX6_1, 'EX6.1', 2,
      'Evaluate: (i) &int;(3x&sup2;+9x+3)^&frac12; (6x+9) dx  (ii) &int;&radic;(ax&sup2;+2bx+c) (ax+b) dx  '
      '(iii) &int;(6x+5)/&radic;(3x&sup2;+5x+2) dx  (iv) &int;(x&sup2;+4x+3)^(&minus;9) (2x+4) dx  '
      '(v) &int;(x&minus;2)(x&minus;3)(x&minus;4) dx  (vi) &int;(2x&sup2;&minus;3)&sup2; dx  '
      '(vii) &int;(x&sup3;&minus;3x&sup2;+9)^(7/2) (x&sup2;&minus;2x) dx  (viii) &int;(x&sup2;&minus;5)&sup3; dx  '
      '(ix) &int;(cos x+sin x)^(3/2) (cos x&minus;sin x) dx  (x) &int;(tan x+sin x)(sec&sup2;x+cos x) dx',
      '(i) (2/3)(3x&sup2;+9x+3)^(3/2) + C<br>(ii) (1/3)(ax&sup2;+2bx+c)^(3/2) + C<br>'
      '(iii) 2&radic;(3x&sup2;+5x+2) + C<br>(iv) &minus;1/(8(x&sup2;+4x+3)&#8308;) + C<br>'
      '(v) x&#8308;/4 &minus; 3x&sup3; + 13x&sup2; &minus; 24x + C<br>(vi) (4/5)x&#8309; &minus; 4x&sup3; + 9x + C<br>'
      '(vii) (2/27)(x&sup3;&minus;3x&sup2;+9)^(9/2) + C<br>(viii) x&#8311;/7 &minus; 3x&#8309; + 25x&sup3; &minus; 125x + C<br>'
      '(ix) (2/5)(cos x+sin x)^(5/2) + C<br>(x) &frac12;(tan x+sin x)&sup2; + C',
      'In (i)&ndash;(iv), (vii), (ix), (x) the second factor is (a multiple of) the derivative of the inner function; '
      '(v), (vi), (viii) expand first.',
      159),
    q('u6_ex61_q3', 6, EX6_1, 'EX6.1', 3,
      'Evaluate: (i) &int;x/(x&sup2;+3) dx  (ii) &int;(sec&sup2;x+cos x)/(tan x+sin x) dx  '
      '(iii) &int;(5x&#8308;+4x&sup3;&minus;3x&sup2;+2x)/(x&#8309;+x&#8308;&minus;x&sup3;+x&sup2;) dx  '
      '(iv) &int;(e&#739;+1/x)/(e&#739;+ln x) dx  (v) &int;(5x&sup2;&minus;2x+2)/(5x&sup3;&minus;3x&sup2;+6x&minus;9) dx  '
      '(vi) &int;dx/(x+&radic;x)',
      '(i) &frac12; ln|x&sup2;+3| + C<br>(ii) ln|tan x+sin x| + C<br>(iii) ln|x&#8309;+x&#8308;&minus;x&sup3;+x&sup2;| + C<br>'
      '(iv) ln|e&#739;+ln x| + C<br>(v) (1/3) ln|5x&sup3;&minus;3x&sup2;+6x&minus;9| + C<br>(vi) 2 ln|&radic;x+1| + C',
      'Each is of the form &int;f&prime;/f = ln|f|; in (v) the numerator is one third of the derivative; '
      'in (vi) write x+&radic;x = &radic;x(&radic;x+1) and substitute u = &radic;x+1.',
      159),
    q('u6_ex61_q4', 6, EX6_1, 'EX6.1', 4,
      'Evaluate: (i) &int;e&#739;(sin x+cos x) dx  (ii) &int;e&#739;(sin&#8315;&sup1;x + 1/&radic;(1&minus;x&sup2;)) dx  '
      '(iii) &int;e&#739;(tan&#8315;&sup1;x + 1/(1+x&sup2;)) dx  (iv) &int;e&#739;(sec&sup2;x+tan x) dx  '
      '(v) &int;e&#739;(1/x+ln x) dx',
      '(i) e&#739; sin x + C<br>(ii) e&#739; sin&#8315;&sup1;x + C<br>(iii) e&#739; tan&#8315;&sup1;x + C<br>'
      '(iv) e&#739; tan x + C<br>(v) e&#739; ln x + C',
      'Each integrand is e&#739;(f + f&prime;), whose integral is e&#739;f.',
      159),
    q('u6_ex61_q5', 6, EX6_1, 'EX6.1', 5,
      'Evaluate: (i) &int;dx/(x&sup2;+9)  (ii) &int;dt/&radic;(4&minus;t&sup2;)  (iii) &int;dy/(y&radic;(y&sup2;&minus;9))  '
      '(iv) &int;dt/(4t&sup2;&minus;9)  (v) &int;dx/&radic;(9x&sup2;+16)  (vi) &int;dx/&radic;(16x&sup2;&minus;9)  '
      '(vii) &int;dx/(9&minus;x&sup2;)  (viii) &int;dx/(x&radic;(4x&sup2;&minus;16))  (ix) &int;&radic;(9&minus;4x&sup2;) dx  '
      '(x) &int;&radic;(25+9x&sup2;) dx  (xi) &int;dy/(9y&sup2;+81)  (xii) &int;dx/(4x&sup2;&minus;16)',
      '(i) (1/3) tan&#8315;&sup1;(x/3) + C<br>(ii) sin&#8315;&sup1;(t/2) + C<br>(iii) (1/3) sec&#8315;&sup1;(y/3) + C<br>'
      '(iv) (1/6) ln|(2t&minus;3)/(2t+3)| + C<br>(v) (1/3) ln|3x+&radic;(9x&sup2;+16)| + C<br>'
      '(vi) (1/4) ln|4x+&radic;(16x&sup2;&minus;9)| + C<br>(vii) (1/6) ln|(3+x)/(3&minus;x)| + C<br>'
      '(viii) (1/4) sec&#8315;&sup1;(x/2) + C<br>(ix) (x/2)&radic;(9&minus;4x&sup2;) + (9/4) sin&#8315;&sup1;(2x/3) + C<br>'
      '(x) (x/2)&radic;(25+9x&sup2;) + (25/6) ln|3x+&radic;(25+9x&sup2;)| + C<br>(xi) (1/27) tan&#8315;&sup1;(y/3) + C<br>'
      '(xii) (1/16) ln|(x&minus;2)/(x+2)| + C',
      'Standard inverse-trig and logarithmic forms after scaling the variable (u = 2x, 3x or 4x as needed); '
      '(ix), (x) use the &radic;(a&sup2;&minus;u&sup2;) and &radic;(a&sup2;+u&sup2;) area-type formulae.',
      160),
]

EX6_2 = 'Exercise 6.2'
SOLVED += [
    q('u6_ex62_q1', 6, EX6_2, 'EX6.2', 1,
      'Evaluate by substitution: (i) &int;3x/&radic;(x&sup2;+7) dx  (ii) &int;x^(4/3)(a^(7/3) &minus; x^(7/3))^(5/2) dx  '
      '(iii) &int;(1+2x)/&radic;(1&minus;x) dx  (iv) &int;(2x&sup2;+4x+5)^(3/2)(x+1) dx  (v) &int;x/&radic;(1&minus;x&sup2;) dx  '
      '(vi) &int;(x+1)/(x&sup2;+2x+5) dx  (vii) &int;x&sup3;(9+x&sup2;)^(3/2) dx  (viii) &int;(x&sup3;&minus;9)^(5/2) x&#8309; dx  '
      '(ix) &int;x&#8313;(x&#8309;+3)^(2/5) dx  (x) &int;(3x&sup2;+2x+5)/(x&sup3;+x&sup2;+5x&minus;1) dx',
      '(i) 3&radic;(x&sup2;+7) + C<br>(ii) &minus;(6/49)(a^(7/3)&minus;x^(7/3))^(7/2) + C<br>'
      '(iii) (4/3)(1&minus;x)^(3/2) &minus; 6&radic;(1&minus;x) + C<br>(iv) (1/10)(2x&sup2;+4x+5)^(5/2) + C<br>'
      '(v) &minus;&radic;(1&minus;x&sup2;) + C<br>(vi) ln&radic;(x&sup2;+2x+5) + C<br>'
      '(vii) (1/7)(9+x&sup2;)^(7/2) &minus; (9/5)(9+x&sup2;)^(5/2) + C<br>'
      '(viii) (2/27)(x&sup3;&minus;9)^(9/2) + (6/7)(x&sup3;&minus;9)^(7/2) + C<br>'
      '(ix) (1/12)(x&#8309;+3)^(12/5) &minus; (3/7)(x&#8309;+3)^(7/5) + C<br>(x) ln|x&sup3;+x&sup2;+5x&minus;1| + C',
      'In each case the algebraic factor outside is (a multiple of) the derivative of the inner function; in '
      '(vii)&ndash;(ix) the leftover power of x is also rewritten in u. The key&#39;s plus sign in (ii) is a misprint.',
      163),
    q('u6_ex62_q2', 6, EX6_2, 'EX6.2', 2,
      'Evaluate by substitution: (i) &int;(ln x)/x dx  (ii) &int;dx/(x ln x)  (iii) &int;tan x/ln(cos x) dx  '
      '(iv) &int;tan(ln x)/x dx  (v) &int;(1+e^(2x))^(&minus;&frac12;) e^(2x) dx  (vi) &int;5e^(5 tan x)/cos&sup2;x dx  '
      '(vii) &int;e^(2x)/(e&#739;+e^(&minus;x)) dx  (viii) &int;e^(cosec 2x+1)(cosec 2x cot 2x) dx  (ix) &int;3&#739; dx  '
      '(x) &int;e^(sin x+cos x+3)(cos x &minus; sin x) dx',
      '(i) &frac12;(ln x)&sup2; + C<br>(ii) ln|ln x| + C<br>(iii) &minus;ln|ln(cos x)| + C<br>'
      '(iv) ln|sec(ln x)| + C<br>(v) &radic;(1+e^(2x)) + C<br>(vi) e^(5 tan x) + C<br>'
      '(vii) e&#739; &minus; tan&#8315;&sup1;(e&#739;) + C<br>(viii) &minus;&frac12; e^(cosec 2x+1) + C<br>'
      '(ix) 3&#739;/ln 3 + C<br>(x) e^(sin x+cos x+3) + C',
      '(vii) write e&#739;+e^(&minus;x) = (e^(2x)+1)/e&#739; and substitute u = e&#739;: &int;u&sup2;/(u&sup2;+1) du.',
      163),
    q('u6_ex62_q3', 6, EX6_2, 'EX6.2', 3,
      'Evaluate by substitution: (i) &int;cos&#8309;2x sin 2x dx  (ii) &int;cot&radic;x/&radic;x dx  '
      '(iii) &int;(2+sin 3x)&#8310; cos 3x dx  (iv) &int;sin(ax+b) dx  (v) &int;(sin x+cos x)/(sin x&minus;cos x) dx  '
      '(vi) &int;e^(2x) sec&sup2;(e^(2x)) dx  (vii) &int;cosec 3x cot 3x/(a+b cosec 3x)&sup2; dx  '
      '(viii) &int;dx/((2 cot x+3) sin&sup2;x)  (ix) &int;sec x/(3 sin x+4 cos x) dx  (x) &int;cos(3x&minus;5) dx',
      '(i) &minus;(1/12)cos&#8310;2x + C<br>(ii) 2 ln|sin&radic;x| + C<br>(iii) (1/21)(2+sin 3x)&#8311; + C<br>'
      '(iv) &minus;(1/a)cos(ax+b) + C<br>(v) ln|sin x&minus;cos x| + C<br>(vi) &frac12; tan(e^(2x)) + C<br>'
      '(vii) 1/(3b(a+b cosec 3x)) + C<br>(viii) &minus;&frac12; ln|2 cot x+3| + C<br>'
      '(ix) (1/3) ln|3 tan x+4| + C<br>(x) (1/3) sin(3x&minus;5) + C',
      '(viii) 1/sin&sup2;x = cosec&sup2;x is &minus;&frac12; d/dx(2 cot x+3). (ix) divide numerator and denominator '
      'by cos&sup2;x to get &int;sec&sup2;x/(3 tan x+4) dx.',
      164),
    q('u6_ex62_q4', 6, EX6_2, 'EX6.2', 4,
      'Evaluate: (i) &int;cos&sup2;2y dy  (ii) &int;sin&sup3;(3x+5) dx  (iii) &int;cos&sup3;x &radic;(sin x) dx  '
      '(iv) &int;sin&#8308;x cos&#8309;x dx  (v) &int;sin&sup3;x/&radic;(cos x) dx  (vi) &int;cos&#8309;x sin&#8311;x dx  '
      '(vii) &int;sin&sup3;x cos&sup3;x dx  (viii) &int;sin 2x cos 4x dx  (ix) &int;cos 3x cos 5x dx  '
      '(x) &int;sin 3x cos 7x dx  (xi) &int;tan&sup2;x dx  (xii) &int;cot&#8308;x dx  (xiii) &int;tan&#8311;x dx  '
      '(xiv) &int;sec&#8308;2x dx  (xv) &int;tan&#8309;3x sec&sup3;3x dx  (xvi) &int;cosec&#8308;3x dx  '
      '(xvii) &int;sec&#8308;x &radic;(tan x) dx  (xviii) &int;cot 2x cosec&#8308;2x dx  (xix) &int;cosec&#8308;x/&radic;(cot x) dx  '
      '(xx) &int;&radic;(1+cos x) dx',
      '(i) y/2 + (1/8) sin 4y + C<br>(ii) &minus;(1/3)cos(3x+5) + (1/9)cos&sup3;(3x+5) + C<br>'
      '(iii) (2/3)sin^(3/2)x &minus; (2/7)sin^(7/2)x + C<br>(iv) sin&#8309;x/5 &minus; 2sin&#8311;x/7 + sin&#8313;x/9 + C<br>'
      '(v) &minus;2&radic;(cos x) + (2/5)cos^(5/2)x + C<br>(vi) sin&#8308;x/8 &minus; sin&sup1;&#8304;x/5 + sin&sup1;&sup2;x/12 + C<br>'
      '(vii) sin&#8308;x/4 &minus; sin&#8310;x/6 + C<br>(viii) &minus;(1/12)cos 6x + (1/4)cos 2x + C<br>'
      '(ix) (1/16)sin 8x + (1/4)sin 2x + C<br>(x) &minus;(1/20)cos 10x + (1/8)cos 4x + C<br>'
      '(xi) tan x &minus; x + C<br>(xii) &minus;(1/3)cot&sup3;x + cot x + x + C<br>'
      '(xiii) tan&#8310;x/6 &minus; tan&#8308;x/4 + tan&sup2;x/2 + ln|cos x| + C<br>(xiv) &frac12; tan 2x + (1/6)tan&sup3;2x + C<br>'
      '(xv) (1/21)sec&#8311;3x &minus; (2/15)sec&#8309;3x + (1/9)sec&sup3;3x + C<br>'
      '(xvi) &minus;(1/3)cot 3x &minus; (1/9)cot&sup3;3x + C<br>(xvii) (2/3)tan^(3/2)x + (2/7)tan^(7/2)x + C<br>'
      '(xviii) &minus;(1/4)cot&sup2;2x &minus; (1/8)cot&#8308;2x + C<br>(xix) &minus;2&radic;(cot x) &minus; (2/5)cot^(5/2)x + C<br>'
      '(xx) 2&radic;2 sin(x/2) + C',
      'Odd powers of sin/cos are split off for substitution; product-to-sum formulae in (viii)&ndash;(x); '
      'tan&sup2; = sec&sup2;&minus;1 and cot&sup2; = cosec&sup2;&minus;1 reductions in (xi)&ndash;(xvi), (xviii); '
      '(xx) uses 1+cos x = 2cos&sup2;(x/2).',
      164),
]

EX6_3 = 'Exercise 6.3'
SOLVED += [
    q('u6_ex63_q1', 6, EX6_3, 'EX6.3', 1, 'Evaluate &int;x&sup3;dx/&radic;(9&minus;x&sup2;).',
      '(1/3)(9&minus;x&sup2;)^(3/2) &minus; 9&radic;(9&minus;x&sup2;) + C',
      'u = 9&minus;x&sup2;, x&sup3;dx = (9&minus;u)(&minus;du/2).', 169),
    q('u6_ex63_q2', 6, EX6_3, 'EX6.3', 2, 'Evaluate &int;6dx/(9&minus;x&sup2;).',
      'ln|(3+x)/(3&minus;x)| + C', '6 &middot; (1/6) ln|(3+x)/(3&minus;x)|.', 169),
    q('u6_ex63_q3', 6, EX6_3, 'EX6.3', 3, 'Evaluate &int;x&sup2;&radic;(9&minus;x&sup2;) dx.',
      '(81/8) sin&#8315;&sup1;(x/3) &minus; (9/8)x&radic;(9&minus;x&sup2;) + (1/4)x&sup3;&radic;(9&minus;x&sup2;) + C',
      'x = 3 sin &theta; gives 81&int;sin&sup2;&theta; cos&sup2;&theta; d&theta; = (81/8)(&theta; &minus; sin 4&theta;/4).', 169),
    q('u6_ex63_q4', 6, EX6_3, 'EX6.3', 4, 'Evaluate &int;5dx/(25x&sup2;+9).',
      '(1/3) tan&#8315;&sup1;(5x/3) + C', '(5/25)&int;dx/(x&sup2;+9/25).', 169),
    q('u6_ex63_q5', 6, EX6_3, 'EX6.3', 5, 'Evaluate &int;dx/(4+x&sup2;)^(3/2).',
      'x/(4&radic;(4+x&sup2;)) + C', 'x = 2 tan &theta; reduces it to (1/4)&int;cos &theta; d&theta;.', 169),
    q('u6_ex63_q6', 6, EX6_3, 'EX6.3', 6, 'Evaluate &int;dx/&radic;(16+4x&sup2;).',
      '(1/2) ln|x+&radic;(x&sup2;+4)| + C', '&radic;(16+4x&sup2;) = 2&radic;(4+x&sup2;).', 169),
    q('u6_ex63_q7', 6, EX6_3, 'EX6.3', 7, 'Evaluate &int;x&sup3;&radic;(9x&sup2;&minus;36) dx.',
      '(3/5)(x&sup2;&minus;4)^(5/2) + 4(x&sup2;&minus;4)^(3/2) + C',
      '3&int;x&sup3;&radic;(x&sup2;&minus;4) dx with u = x&sup2;&minus;4.', 169),
    q('u6_ex63_q8', 6, EX6_3, 'EX6.3', 8, 'Evaluate &int;dx/&radic;(a&sup2;+x&sup2;).',
      'ln|x+&radic;(a&sup2;+x&sup2;)| + C', 'x = a tan &theta;.', 169),
    q('u6_ex63_q9', 6, EX6_3, 'EX6.3', 9, 'Evaluate &int;dx/(16&minus;x&sup2;)^(5/2).',
      '(1/256)[x/&radic;(16&minus;x&sup2;) + x&sup3;/(3(16&minus;x&sup2;)^(3/2))] + C',
      'x = 4 sin &theta; gives (1/256)&int;sec&#8308;&theta; d&theta; = (1/256)(tan &theta; + tan&sup3;&theta;/3). '
      'The key&#39;s second numerator &quot;x&quot; is a misprint for x&sup3;.', 169),
    q('u6_ex63_q10', 6, EX6_3, 'EX6.3', 10, 'Evaluate &int;x&#8309;dx/&radic;(x&sup2;&minus;9).',
      '(1/5)(x&sup2;&minus;9)^(5/2) + 6(x&sup2;&minus;9)^(3/2) + 81&radic;(x&sup2;&minus;9) + C',
      'u = x&sup2;&minus;9, x&#8309;dx = (u+9)&sup2; du/2.', 169),
    q('u6_ex63_q11', 6, EX6_3, 'EX6.3', 11, 'Evaluate &int;dx/(x&sup2;+4x+5).',
      'tan&#8315;&sup1;(x+2) + C', 'x&sup2;+4x+5 = (x+2)&sup2;+1.', 169),
    q('u6_ex63_q12', 6, EX6_3, 'EX6.3', 12, 'Evaluate &int;dx/&radic;(5+4x&minus;x&sup2;).',
      'sin&#8315;&sup1;((x&minus;2)/3) + C', '5+4x&minus;x&sup2; = 9&minus;(x&minus;2)&sup2;.', 169),
    q('u6_ex63_q13', 6, EX6_3, 'EX6.3', 13, 'Evaluate &int;dx/&radic;(9x&minus;x&sup2;).',
      'sin&#8315;&sup1;((2x&minus;9)/9) + C', '9x&minus;x&sup2; = 81/4 &minus; (x&minus;9/2)&sup2;.', 169),
    q('u6_ex63_q14', 6, EX6_3, 'EX6.3', 14, 'Evaluate &int;dx/((x+1)&radic;(x&sup2;+2x&minus;15)).',
      '(1/4) sec&#8315;&sup1;((x+1)/4) + C', 'x&sup2;+2x&minus;15 = (x+1)&sup2;&minus;16; u = x+1.', 169),
    q('u6_ex63_q15', 6, EX6_3, 'EX6.3', 15, 'Evaluate &int;dx/((x&minus;4)&radic;(x&sup2;&minus;8x&minus;9)).',
      '(1/5) sec&#8315;&sup1;((x&minus;4)/5) + C', 'x&sup2;&minus;8x&minus;9 = (x&minus;4)&sup2;&minus;25; u = x&minus;4.', 169),
    q('u6_ex63_q16', 6, EX6_3, 'EX6.3', 16, 'Evaluate &int;(2x&minus;5)dx/&radic;(8x&minus;x&sup2;).',
      '&minus;2&radic;(8x&minus;x&sup2;) + 3 sin&#8315;&sup1;((x&minus;4)/4) + C',
      'Split 2x&minus;5 = &minus;(8&minus;2x) + 3; the remainder uses 8x&minus;x&sup2; = 16&minus;(x&minus;4)&sup2;.', 169),
    q('u6_ex63_q17', 6, EX6_3, 'EX6.3', 17, 'Evaluate &int;(x+3)dx/(x&sup2;+2x+5).',
      'ln&radic;(x&sup2;+2x+5) + tan&#8315;&sup1;((x+1)/2) + C',
      'x+3 = &frac12;(2x+2) + 2; the remainder uses (x+1)&sup2;+4.', 169),
    q('u6_ex63_q18', 6, EX6_3, 'EX6.3', 18, 'Evaluate &int;(3x+9)dx/(x&sup2;+4x+4).',
      '3 ln|x+2| &minus; 3/(x+2) + C', 'u = x+2 turns it into &int;(3/u + 3/u&sup2;) du.', 169),
    q('u6_ex63_q19', 6, EX6_3, 'EX6.3', 19, 'Evaluate &int;(4x+9)dx/&radic;(2x&sup2;+8x&minus;10).',
      '2&radic;(2(x&sup2;+4x&minus;5)) + (&radic;2/2) ln|x+2+&radic;(x&sup2;+4x&minus;5)| + C',
      '4x+9 = (4x+8)+1; the remainder uses 2x&sup2;+8x&minus;10 = 2((x+2)&sup2;&minus;9).', 169),
    q('u6_ex63_q20', 6, EX6_3, 'EX6.3', 20, 'Evaluate &int;(2x&minus;5)dx/&radic;(5+4x&minus;x&sup2;).',
      '&minus;2&radic;(5+4x&minus;x&sup2;) &minus; sin&#8315;&sup1;((x&minus;2)/3) + C',
      '2x&minus;5 = &minus;(4&minus;2x) &minus; 1; the remainder uses 5+4x&minus;x&sup2; = 9&minus;(x&minus;2)&sup2;.', 169),
]

EX6_4 = 'Exercise 6.4'
SOLVED += [
    q('u6_ex64_q1', 6, EX6_4, 'EX6.4', 1,
      'Integrate by parts: (i) &int;x&sup2;e&#739; dx (ii) &int;x&sup3;e&#739; dx (iii) &int;x cos x dx '
      '(iv) &int;ln x dx (v) &int;x&sup2; sin x dx (vi) &int;x cosec&sup2;x dx (vii) &int;x sec&sup2;x dx '
      '(viii) &int;(ln x)&sup2; dx.',
      '(i) (x&sup2;&minus;2x+2)e&#739;+C (ii) (x&sup3;&minus;3x&sup2;+6x&minus;6)e&#739;+C (iii) x sin x+cos x+C '
      '(iv) x(ln x&minus;1)+C (v) 2(x sin x+cos x)&minus;x&sup2; cos x+C (vi) ln|sin x|&minus;x cot x+C '
      '(vii) x tan x+ln|cos x|+C (viii) x(ln x)&sup2;+2x(1&minus;ln x)+C',
      'u = the algebraic or logarithmic factor, dv = the rest; (i)&ndash;(ii) reduce &int;x&#8319;e&#739;dx repeatedly; '
      '(viii) &int;(ln x)&sup2;dx = x(ln x)&sup2; &minus; 2&int;ln x dx.', 174),
    q('u6_ex64_q2', 6, EX6_4, 'EX6.4', 2,
      'Integrate by parts: (i) &int;(x+1) ln(x+1) dx (ii) &int;x ln x dx (iii) &int;x&#8315;&sup3; ln x dx '
      '(iv) &int;x&#8315;&#8308; ln x&sup2; dx (v) &int;sin x cos x ln(sin x) dx (vi) &int;(tan x/cos&sup2;x) ln(tan x) dx '
      '(vii) &int;cot x cosec&sup2;x ln(cot x) dx (viii) &int;sec&sup3;x tan x ln(sec x) dx '
      '(ix) &int;cosec x cot x ln(cosec x) dx (x) &int;(ln x&sup2;)/x&sup2; dx (xi) &int;sec&sup3;x dx '
      '(xii) &int;cosec&sup3;x dx.',
      '(i) (1/4)(x+1)&sup2;(ln(x+1)&sup2;&minus;1)+C (ii) (1/4)x&sup2;(ln x&sup2;&minus;1)+C '
      '(iii) &minus;(1/(4x&sup2;))(1+ln x&sup2;)+C (iv) &minus;(1/(9x&sup3;))(ln x&#8310;+2)+C '
      '(v) (1/4)sin&sup2;x{ln(sin x)&sup2;&minus;1}+C (vi) (1/4)tan&sup2;x{ln(tan x)&sup2;&minus;1}+C '
      '(vii) &minus;(1/4)cot&sup2;x{ln(cot x)&sup2;&minus;1}+C (viii) (1/9)sec&sup3;x{ln(sec x)&sup3;&minus;1}+C '
      '(ix) cosec x(1&minus;ln|cosec x|)+C (x) &minus;(2/x)(1+ln x)+C '
      '(xi) (1/2)sec x tan x+ln&radic;(sec x+tan x)+C (xii) &minus;(1/2)cosec x cot x+ln&radic;(cosec x&minus;cot x)+C',
      'u = the logarithmic factor throughout, e.g. (iv) 2&int;x&#8315;&#8308; ln x dx = 2[&minus;(ln x)/(3x&sup3;) &minus; 1/(9x&sup3;)]; '
      '(xi)&ndash;(xii) reduction: 2I = sec x tan x + ln|sec x+tan x|, and the cosec analogue.', 174),
    q('u6_ex64_q3', 6, EX6_4, 'EX6.4', 3,
      'Integrate by parts: (i) &int;3x cos 3x dx (ii) &int;x&sup2; sin x dx (iii) &int;(x/cot&sup2;x) dx '
      '(iv) &int;x sec&sup2;x dx (v) &int;(5x/sin&sup2;2x) dx (vi) &int;cos &radic;x dx (vii) &int;e&sup2;&#739; sin 2x dx '
      '(viii) &int;e&#8315;&#739; cos 2x dx (ix) &int;cos(ln x) dx (x) &int;e&#688;&#739; sin bx dx.',
      '(i) x sin 3x+(1/3)cos 3x+C (ii) (2&minus;x&sup2;)cos x+2x sin x+C (iii) x tan x&minus;ln|sec x|&minus;x&sup2;/2+C '
      '(iv) x tan x+ln|cos x|+C (v) (5/4)[&minus;2x cot 2x+ln|sin 2x|]+C (vi) 2&radic;x sin&radic;x+2 cos&radic;x+C '
      '(vii) (1/4)e&sup2;&#739;(sin 2x&minus;cos 2x)+C (viii) (1/5)e&#8315;&#739;(2 sin 2x&minus;cos 2x)+C '
      '(ix) (1/2)x[sin(ln x)+cos(ln x)]+C (x) e&#688;&#739;(a sin bx&minus;b cos bx)/(a&sup2;+b&sup2;)+C',
      '(iii) x/cot&sup2;x = x tan&sup2;x = x(sec&sup2;x&minus;1); (v) 5&int;x cosec&sup2;2x dx; (vi) t = &radic;x gives 2&int;t cos t dt; '
      '(vii)&ndash;(x) &int;e&#688;&#739; sin bx dx = e&#688;&#739;(a sin bx &minus; b cos bx)/(a&sup2;+b&sup2;) and the cosine analogue; '
      '(ix) pair I with &int;sin(ln x)dx.', 174),
    q('u6_ex64_q4', 6, EX6_4, 'EX6.4', 4,
      'Integrate by parts: (i) &int;sin&#8315;&sup1;3x dx (ii) &int;x&#8308; tan&#8315;&sup1;x dx (iii) &int;tan&#8315;&sup1;(2x) dx '
      '(iv) &int;x cos&#8315;&sup1;x dx (v) &int;3x&sup2; sin&#8315;&sup1;(3x) dx (vi) &int;2x sec&#8315;&sup1;x dx '
      '(vii) &int;6x cosec&#8315;&sup1;(2x) dx (viii) &int;x&sup2; cot&#8315;&sup1;x dx.',
      '(i) x sin&#8315;&sup1;3x+(1/3)&radic;(1&minus;9x&sup2;)+C (ii) (1/5)(x&#8309; tan&#8315;&sup1;x&minus;x&#8308;/4+x&sup2;/2&minus;ln&radic;(1+x&sup2;))+C '
      '(iii) x tan&#8315;&sup1;2x&minus;(1/4)ln(1+4x&sup2;)+C (iv) (1/2)x&sup2; cos&#8315;&sup1;x&minus;(1/4)x&radic;(1&minus;x&sup2;)+(1/4)sin&#8315;&sup1;x+C '
      '(v) x&sup3; sin&#8315;&sup1;3x+(1/27)&radic;(1&minus;9x&sup2;)&minus;(1/81)(1&minus;9x&sup2;)^(3/2)+C '
      '(vi) x&sup2; sec&#8315;&sup1;x&minus;&radic;(x&sup2;&minus;1)+C (vii) 3x&sup2; cosec&#8315;&sup1;2x+(3/4)&radic;(4x&sup2;&minus;1)+C '
      '(viii) (1/6){2x&sup3; cot&#8315;&sup1;x+x&sup2;&minus;ln|1+x&sup2;|}+C',
      'u = the inverse-trigonometric factor; the leftover integrals use x&#8309;/(1+x&sup2;) = x&sup3;&minus;x+x/(1+x&sup2;), '
      'x&sup2;/&radic;(1&minus;x&sup2;), x/&radic;(x&sup2;&minus;1), x/&radic;(4x&sup2;&minus;1) and x&sup3;/(1+x&sup2;) = x&minus;x/(1+x&sup2;).', 174),
    q('u6_ex64_q5', 6, EX6_4, 'EX6.4', 5,
      'Integrate by parts: (i) &int;&radic;(9&minus;x&sup2;) dx (ii) &int;&radic;(16+4x&sup2;) dx (iii) &int;&radic;(x&sup2;&minus;25) dx.',
      '(i) (1/2){x&radic;(9&minus;x&sup2;)+9 sin&#8315;&sup1;(x/3)}+C (ii) x&radic;(4+x&sup2;)+4 ln|x+&radic;(4+x&sup2;)|+C '
      '(iii) (1/2)[x&radic;(x&sup2;&minus;25)&minus;25 ln|x+&radic;(x&sup2;&minus;25)|]+C',
      'Standard radical results obtained by one integration by parts; (ii) &radic;(16+4x&sup2;) = 2&radic;(4+x&sup2;).', 175),
]

EX6_5 = 'Exercise 6.5'
SOLVED += [
    q('u6_ex65_q1', 6, EX6_5, 'EX6.5', 1, 'Evaluate by partial fractions &int;(5x&minus;2)dx/((x&minus;3)(x+7)).',
      '(1/10)ln|(x&minus;3)&#8305;&sup3;(x+7)&sup3;&#8311;| + C',
      'A = 13/10 at x = 3, B = 37/10 at x = &minus;7.', 177),
    q('u6_ex65_q2', 6, EX6_5, 'EX6.5', 2, 'Evaluate by partial fractions &int;(7x&minus;25)dx/((x&minus;3)(x&minus;4)).',
      'ln|(x&minus;3)&#8308;(x&minus;4)&sup3;| + C', 'A = 4 at x = 3, B = 3 at x = 4.', 177),
    q('u6_ex65_q3', 6, EX6_5, 'EX6.5', 3, 'Evaluate by partial fractions &int;dx/(a&sup2;&minus;x&sup2;).',
      '(1/(2a))ln|(a+x)/(a&minus;x)| + C', '1/(a&sup2;&minus;x&sup2;) = (1/(2a))[1/(a&minus;x) + 1/(a+x)].', 178),
    q('u6_ex65_q4', 6, EX6_5, 'EX6.5', 4, 'Evaluate by partial fractions &int;dx/(x&sup2;&minus;a&sup2;).',
      '(1/(2a))ln|(x&minus;a)/(x+a)| + C', '1/(x&sup2;&minus;a&sup2;) = (1/(2a))[1/(x&minus;a) &minus; 1/(x+a)].', 178),
    q('u6_ex65_q5', 6, EX6_5, 'EX6.5', 5, 'Evaluate by partial fractions &int;(x&sup2;+2x+3)dx/(x&sup3;&minus;x).',
      'ln|((x&minus;1)&sup3;(x+1))/x&sup3;| + C',
      'x&sup3;&minus;x = x(x&minus;1)(x+1); A = &minus;3, B = 3, C = 1.', 178),
    q('u6_ex65_q6', 6, EX6_5, 'EX6.5', 6, 'Evaluate by partial fractions &int;5dx/(x&sup2;&minus;2x&minus;15).',
      '(5/8)ln|(x&minus;5)/(x+3)| + C', 'x&sup2;&minus;2x&minus;15 = (x&minus;5)(x+3); A = 5/8, B = &minus;5/8.', 178),
    q('u6_ex65_q7', 6, EX6_5, 'EX6.5', 7,
      'Evaluate by partial fractions &int;(2x+7)dx/((x&minus;1)(x&minus;5)(x+3)).',
      '&minus;(9/16)ln|x&minus;1| + (1/32)[17 ln|x&minus;5| + ln|x+3|] + C',
      'Cover-up: A = &minus;9/16, B = 17/32, C = 1/32. The key&#39;s &minus;19/16 on ln(x&minus;1) is a misprint: '
      'only &minus;9/16 makes the residues sum to zero.', 178),
    q('u6_ex65_q8', 6, EX6_5, 'EX6.5', 8, 'Evaluate by partial fractions &int;(5x+6)dx/((x+3)(x&minus;2)&sup2;).',
      '(9/25)ln|(x&minus;2)/(x+3)| &minus; 16/(5(x&minus;2)) + C',
      'A = &minus;9/25, B = 9/25, C = 16/5; &int;C/(x&minus;2)&sup2;dx = &minus;C/(x&minus;2).', 178),
    q('u6_ex65_q9', 6, EX6_5, 'EX6.5', 9,
      'Evaluate by partial fractions &int;(7x&sup2;&minus;2x+5)dx/((x&minus;6)(x&minus;3)&sup3;).',
      '(245/27)ln|(x&minus;6)/(x&minus;3)| + 182/(9(x&minus;3)) + 31/(3(x&minus;3)&sup2;) + C',
      'u = x&minus;3: numerator 7u&sup2;+40u+62 over u&sup3;(u&minus;3); expand 1/(u&minus;3) to read off the coefficients.', 178),
    q('u6_ex65_q10', 6, EX6_5, 'EX6.5', 10, 'Evaluate by partial fractions &int;(2x+1)dx/((x&minus;3)(x&sup2;+1)).',
      '(1/20)[14 ln|x&minus;3| &minus; 7 ln|x&sup2;+1| &minus; 2 tan&#8315;&sup1;x] + C',
      'A = 7/10, Bx+C = &minus;(7/10)x &minus; 1/10; the linear part gives &minus;(7/20)ln(x&sup2;+1) &minus; (1/10)tan&#8315;&sup1;x.', 178),
    q('u6_ex65_q11', 6, EX6_5, 'EX6.5', 11,
      'Evaluate by partial fractions &int;sec&sup2;x dx/((1+tan x)(2+tan x)).',
      'ln|(1+tan x)/(2+tan x)| + C', 't = tan x, dt = sec&sup2;x dx; 1/((1+t)(2+t)) = 1/(1+t) &minus; 1/(2+t).', 178),
    q('u6_ex65_q12', 6, EX6_5, 'EX6.5', 12,
      'Evaluate by partial fractions &int;cosec&sup2;x dx/(cot x(2+cot x)).',
      'ln|&radic;(1+2 tan x)| + C',
      'u = cot x, du = &minus;cosec&sup2;x dx; (1/2)ln|(2+cot x)/cot x| = (1/2)ln|1+2 tan x|.', 178),
    q('u6_ex65_q13', 6, EX6_5, 'EX6.5', 13, 'Evaluate by partial fractions &int;(3x+7)dx/((2x&minus;1)(x&minus;4)&sup2;).',
      '(17/49)ln|(2x&minus;1)/(x&minus;4)| &minus; 19/(7(x&minus;4)) + C',
      'A = 34/49 (gives (17/49)ln|2x&minus;1|), B = &minus;17/49, C = 19/7.', 178),
    q('u6_ex65_q14', 6, EX6_5, 'EX6.5', 14, 'Evaluate by partial fractions &int;(7x&minus;4)dx/((x&minus;3)(x&sup2;+2)).',
      '(17/11)ln((x&minus;3)/&radic;(x&sup2;+2)) + (13&radic;2/11)tan&#8315;&sup1;(x/&radic;2) + C',
      'A = 17/11, Bx+C = &minus;(17/11)x + 26/11; (26/11)&int;dx/(x&sup2;+2) = (26/(11&radic;2))tan&#8315;&sup1;(x/&radic;2).', 178),
    q('u6_ex65_q15', 6, EX6_5, 'EX6.5', 15, 'Evaluate by partial fractions &int;(2x&sup2;+5x+1)dx/(x&sup2;+5x+6).',
      '2x &minus; ln|(x+2)(x+3)&#8308;| + C',
      'Improper: integrand = 2 &minus; (5x+11)/((x+2)(x+3)); (5x+11)/((x+2)(x+3)) = 1/(x+2) + 4/(x+3).', 178),
    q('u6_ex65_q16', 6, EX6_5, 'EX6.5', 16, 'Evaluate by partial fractions &int;(x&sup3;+3x+1)dx/(x&sup2;+5x&minus;14).',
      '(1/2)x&sup2; &minus; 5x + (1/3)[5 ln|x&minus;2| + 121 ln|x+7|] + C',
      'Division gives x &minus; 5 + (42x&minus;69)/((x&minus;2)(x+7)); A = 5/3, B = 121/3.', 178),
]

EX6_6 = 'Exercise 6.6'
SOLVED += [
    q('u6_ex66_q1', 6, EX6_6, 'EX6.6', 1,
      'Evaluate the definite integrals: (i) &int;&#8320;&sup2;(4x&sup3;+3x&sup2;+5)dx (ii) &int;&#8315;&#8321;&sup2;(x&sup2;+1)&sup2;dx '
      '(iii) &int;&#8321;&sup2;(&theta;+&radic;&theta;)&sup3;d&theta; (iv) &int;&#8321;&sup3;(y+1/&radic;y)&sup2;dy '
      '(v) &int;&#8320;&#8308;dx/(&radic;(2+x)+&radic;x).',
      '(i) 34 (ii) 78/5 (iii) (1184&radic;2+1329)/140 (iv) 4&radic;3+ln 3+22/3 (v) (2/3)(3&radic;6&minus;&radic;2&minus;4)',
      'Direct antiderivatives; (v) rationalize: (1/2)&int;(&radic;(2+x)&minus;&radic;x)dx.', 187),
    q('u6_ex66_q2', 6, EX6_6, 'EX6.6', 2,
      'Evaluate the definite integrals: (i) &int;&#8321;&#8308;x(x&sup2;+9)^(3/2)dx (ii) &int;&#8322;&#8309;x dx/(7x&sup2;+2) '
      '(iii) &int;&#8320;&sup3;(2x+3)dx/&radic;(2x&sup2;+6x+5) (iv) &int;&#8321;&sup2;(x&sup3;+2x)^(&minus;1/2)(3x&sup2;+2)dx '
      '(v) &int;&#8320;^(&pi;/2)cos&sup3;x dx (vi) &int;_(&pi;&sup2;/4)^(&pi;&sup2;/36) sin&radic;x/&radic;x dx '
      '(vii) &int;&#8320;^(&pi;/4)&radic;(tan x)sec&sup2;x dx (viii) &int;&#8320;&sup2;e&#8309;&#739;&#8315;&sup2;dx '
      '(ix) &int;&#8320;^(&pi;/3)cos&sup3;3x sin&sup2;3x dx (x) &int;&#8320;^(&pi;/3)tan&sup2;x sec&#8308;x dx.',
      '(i) 5(125&minus;4&radic;10) (ii) (1/14)ln(59/10) (iii) &radic;41&minus;&radic;5 (iv) 2&radic;3 (v) 2/3 (vi) &minus;&radic;3 '
      '(vii) 2/3 (viii) (e&#8305;&#8304;&minus;1)/(5e&sup2;) (ix) 0 (x) 42&radic;3/15',
      'Substitutions u = x&sup2;+9, 7x&sup2;+2, 2x&sup2;+6x+5, x&sup3;+2x, t = tan x, t = &radic;x; (ix) the integrand is odd '
      'about t = &pi;/2 after t = 3x. The key&#39;s e&#8305;&#8310; in (viii) is a misprint for e&#8305;&#8304;.', 187),
    q('u6_ex66_q3', 6, EX6_6, 'EX6.6', 3,
      'Compute by basic properties: (i) &int;&#8322;&sup2;(x&#8308;+2x+3)^(5/2)(2x&sup3;+1)dx '
      '(ii) &int;&#8315;&#8325;&#8320;^&#8309;&#8304;(10x&#8313;&minus;8x&#8311;+6x&#8309;&minus;4x&sup3;+2x)dx '
      '(iii) &int;_(&minus;&pi;/2)^(&pi;/2)sin&#8313;x cos&#8310;x dx (iv) &int;_&minus;&pi;^&pi;sec&#8312;x tan x dx '
      '(v) &int;_(&minus;&pi;/2)^(&pi;/2)sin&sup2;x cos&sup2;x dx (vi) &int;_(&minus;&pi;/4)^(&pi;/4)tan&sup2;x dx '
      '(vii) &int;&#8315;&#8322;&#8322;(x&#8308;+2x&sup2;)dx.',
      '(i) 0 (ii) 0 (iii) 0 (iv) 0 (v) &pi;/8 (vi) 2&minus;&pi;/2 (vii) 352/15',
      '(i) equal limits; (ii)&ndash;(iv) odd integrands on symmetric intervals; (v)&ndash;(vii) even, double the half integral.', 187),
    q('u6_ex66_q4', 6, EX6_6, 'EX6.6', 4,
      'Given that d/dx(x/&radic;(1+x&sup2;)) = 1/(1+x&sup2;)^(3/2), evaluate &int;&#8320;&sup3;dx/(1+x&sup2;)^(3/2).',
      '3/&radic;10', 'The given derivative is the antiderivative: [x/&radic;(1+x&sup2;)]&#8320;&sup3;.', 187),
    q('u6_ex66_q5', 6, EX6_6, 'EX6.6', 5,
      'Given that d/dx[F(x)] = (2+x&sup2;)/(1+x&sup2;), evaluate F(&radic;3)&minus;F(1); if F(1) = &pi;, find F(x).',
      'F(&radic;3)&minus;F(1) = (&radic;3&minus;1)+&pi;/12; F(x) = x+tan&#8315;&sup1;x+(3&pi;&minus;4)/4',
      '(2+x&sup2;)/(1+x&sup2;) = 1+1/(1+x&sup2;), so F(x) = x+tan&#8315;&sup1;x+C; F(1) = &pi; fixes C = (3&pi;&minus;4)/4.', 188),
    q('u6_ex66_q6', 6, EX6_6, 'EX6.6', 6,
      'Given &int;&#8315;&#8322;&sup3;f(x)dx = 4 and &int;&#8325;&sup3;f(x)dx = 7, evaluate: (i) &int;&#8323;&#8315;&sup2;f(x)dx '
      '(ii) &int;&#8315;&#8322;&sup3;f(y)dy (iii) &int;&#8323;&#8309;f(y)dy (iv) &int;&#8322;&sup2;f(x)dx (v) &int;&#8315;&#8322;&#8309;f(x)dx '
      '(vi) &int;&#8325;&#8315;&sup2;f(y)dy.',
      '(i) &minus;4 (ii) 4 (iii) &minus;7 (iv) 0 (v) &minus;3 (vi) 3',
      'Reversing limits changes sign; the dummy variable is irrelevant; &int;&#8315;&#8322;&#8309; = &int;&#8315;&#8322;&sup3; + &int;&#8323;&#8309;.', 188),
    q('u6_ex66_q7', 6, EX6_6, 'EX6.6', 7,
      'Evaluate by trigonometric substitution: (i) &int;&#8320;&sup2;dx/&radic;(16&minus;x&sup2;) (ii) &int;&#8315;&#8321;&sup1;dx/(4&minus;x&sup2;) '
      '(iii) &int;&#8323;^(2&radic;3)x&sup3;dx/&radic;(x&sup2;+4) (iv) &int;&#8320;^&radic;3x&sup2;&radic;(3&minus;x&sup2;)dx.',
      '(i) &pi;/6 (ii) (ln 3)/2 (iii) (16&minus;&radic;13)/3 (iv) 9&pi;/16',
      '(i) x = 4 sin &theta;; (ii) partial fractions or x = 2 sin &theta;; (iii) u = x&sup2;+4 gives '
      '[( &radic;(x&sup2;+4)/3)(x&sup2;&minus;8)]&#8323;^(2&radic;3) &mdash; the key&#39;s 10 2/3 is the value with lower limit 0; '
      '(iv) x = &radic;3 sin &theta; gives 9&int;&#8320;^(&pi;/2)sin&sup2;&theta;cos&sup2;&theta;d&theta;.', 188),
    q('u6_ex66_q8', 6, EX6_6, 'EX6.6', 8,
      'Compute by integration by parts: (i) &int;&#8325;&#8313;xe&#8308;&#739;dx (ii) &int;&#8321;&#8308;x&sup2;ln x dx '
      '(iii) &int;_(&pi;/6)^(&pi;/2)x sin 2x dx (iv) &int;&#8320;&sup1;tan&#8315;&sup1;x dx.',
      '(i) (1/16)(35e&sup3;&#8310;&minus;19e&sup2;&#8304;) (ii) (128 ln 2)/3&minus;7 (iii) (7&pi;&minus;3&radic;3)/24 (iv) (&pi;&minus;ln 4)/4',
      '(i) uv with u = x; (ii) u = ln x; (iii) u = x, dv = sin 2x dx; (iv) u = tan&#8315;&sup1;x leaves &int;x/(1+x&sup2;)dx.', 188),
]

EX6_7 = 'Exercise 6.7'
SOLVED += [
    q('u6_ex67_q1', 6, EX6_7, 'EX6.7', 1, 'Find the area above the x-axis under y = 3x&sup2;+2 between x = 1 and x = 2.',
      '9', '&int;&#8321;&sup2;(3x&sup2;+2)dx = [x&sup3;+2x]&#8321;&sup2; = 12&minus;3.', 191),
    q('u6_ex67_q2', 6, EX6_7, 'EX6.7', 2, 'Find the area above the x-axis under y = 1/&radic;(4&minus;x&sup2;) between x = 1/2 and x = &radic;3/2.',
      '&asymp; 0.195', '[sin&#8315;&sup1;(x/2)] = sin&#8315;&sup1;(&radic;3/4) &minus; sin&#8315;&sup1;(1/4).', 191),
    q('u6_ex67_q3', 6, EX6_7, 'EX6.7', 3, 'Find the area above the x-axis under y = ln x between x = 1 and x = 3.',
      '3 ln 3&minus;2 &asymp; 1.2958', '[x ln x &minus; x]&#8321;&sup3;.', 191),
    q('u6_ex67_q4', 6, EX6_7, 'EX6.7', 4, 'Find the area above the x-axis under y = x sin x between x = &pi;/3 and x = &pi;/2.',
      '&asymp; 0.6575', '[sin x &minus; x cos x] = 1 &minus; (&radic;3/2 &minus; &pi;/6).', 191),
    q('u6_ex67_q5', 6, EX6_7, 'EX6.7', 5, 'Find the area above the x-axis under y = 1/(9+x&sup2;) between x = &minus;&radic;3 and x = &radic;3.',
      '&pi;/9', '(1/3)[tan&#8315;&sup1;(x/3)]; even integrand gives (2/3)tan&#8315;&sup1;(1/&radic;3).', 191),
    q('u6_ex67_q6', 6, EX6_7, 'EX6.7', 6, 'Find the area above the x-axis under y = 4x&sup3;+3x&sup2;+2x+1 between x = 0 and x = 2.',
      '30', '[x&#8308;+x&sup3;+x&sup2;+x]&#8320;&sup2; = 16+8+4+2.', 191),
    q('u6_ex67_q7', 6, EX6_7, 'EX6.7', 7, 'Find the area above the x-axis under y = 3 sec&sup2;x between x = &pi;/6 and x = &pi;/3.',
      '2&radic;3', '3[tan x] = 3(&radic;3 &minus; 1/&radic;3).', 191),
    q('u6_ex67_q8', 6, EX6_7, 'EX6.7', 8, 'Find the area above the x-axis under y = 6 sin&sup2;x between x = 0 and x = &pi;/3.',
      '(4&pi;&minus;3&radic;3)/4', '6 sin&sup2;x = 3(1&minus;cos 2x); 3[x &minus; (sin 2x)/2]&#8320;^(&pi;/3).', 191),
    q('u6_ex67_q9', 6, EX6_7, 'EX6.7', 9, 'Find the area above the x-axis under y = 5e&#8309;&#739; between x = &minus;2 and x = 3.',
      'e&#8305;&#8309;&minus;e&#8315;&#8305;&#8304; &asymp; 3269017.372', '[e&#8309;&#739;]&#8315;&#8322;&sup3;.', 191),
    q('u6_ex67_q10', 6, EX6_7, 'EX6.7', 10, 'Find the area above the x-axis under y = cos&#8308;x between x = 0 and x = &pi;/2.',
      '3&pi;/16', 'Wallis: &int;&#8320;^(&pi;/2)cos&#8308;x dx = (3/4)(1/2)(&pi;/2).', 191),
    q('u6_ex67_q11', 6, EX6_7, 'EX6.7', 11, 'Find the area above the x-axis under y = 4/sin&sup2;x between x = &pi;/6 and x = &pi;/4.',
      '4(&radic;3&minus;1)', '4&int;cosec&sup2;x dx = 4[&minus;cot x].', 191),
    q('u6_ex67_q12', 6, EX6_7, 'EX6.7', 12, 'Find the area above the x-axis under x&sup2;+y&sup2; = 36 between x = &minus;1 and x = 1.',
      '&radic;35+36 sin&#8315;&sup1;(1/6) &asymp; 11.9442',
      'y = &radic;(36&minus;x&sup2;); [(x/2)&radic;(36&minus;x&sup2;)+18 sin&#8315;&sup1;(x/6)]&#8315;&#8321;&sup1;.', 192),
    q('u6_ex67_q13', 6, EX6_7, 'EX6.7', 13, 'Find the area above the x-axis under x&sup2;/4+y&sup2;/9 = 1 between x = &minus;1 and x = 1.',
      '(3&radic;3)/2+&pi; &asymp; 5.7396', 'y = (3/2)&radic;(4&minus;x&sup2;); 3[(x/2)&radic;(4&minus;x&sup2;)+2 sin&#8315;&sup1;(x/2)]&#8320;&sup1; doubled by symmetry.', 192),
    q('u6_ex67_q14', 6, EX6_7, 'EX6.7', 14, 'Find the area above the x-axis under y&sup2; = 2x+5 between x = 1 and x = 2.',
      '(27&minus;7&radic;7)/3 &asymp; 2.82658', 'y = &radic;(2x+5); [(1/3)(2x+5)^(3/2)]&#8321;&sup2;.', 192),
    q('u6_ex67_q15', 6, EX6_7, 'EX6.7', 15, 'Find the area above the x-axis under y&sup2; = tan&#8308;x between x = &pi;/6 and x = &pi;/4.',
      '(12&minus;4&radic;3&minus;&pi;)/12', 'y = tan&sup2;x = sec&sup2;x&minus;1; [tan x &minus; x].', 192),
    q('u6_ex67_q16', 6, EX6_7, 'EX6.7', 16,
      'Write MAPLE commands to find the integration of: (i) f(x) = e&sup2;&#739; (ii) f(x) = sin x '
      '(iii) f(x) = cos 2x (iv) f(x) = ln(1+x) (v) f(x) = 1/x.',
      '(i) &gt; int(e&sup2;&#739;, x = 1..5) (ii) &gt; int(sin(x), x = 0..4&pi;) (iii) &gt; int(cos(2x), x = 0..&pi;/2) '
      '(iv) &gt; int(ln(1+x), x = 0..3) (v) &gt; int(1/x, x = 2..5)',
      'MAPLE&#39;s int command with the ranges as printed in the key.', 192),
]

REV6 = 'Review Exercise 6'
SOLVED += [
    q('u6_rev6_q1', 6, REV6, 'REV6', 1,
      'Choose the correct option: (i) &int;f&#8319;(x)f&prime;(x)dx, n &ne; &minus;1 (ii) same with n = &minus;1 '
      '(iii) &int;x&#8319;dx, n = &minus;1 (iv) &int;sin x cos x dx (v) &int;x&sup2;ln e^(x&sup2;)dx '
      '(vi) &int;e^(ln x&sup3;)dx (vii) &int;(1+tan&sup2;x)dx (viii) &int;2e&#739;/(1+e&#739;)dx '
      '(ix) &int;e^(x+3 ln x)/x&sup3;dx (x) &int;ln(e&#739;&middot;e^(sin x))dx '
      '(xi) &int;[1/(x&radic;(x&sup2;&minus;1))]/cosec&#8315;&sup1;x dx (xii) F antiderivative of f: &int;&#8320;&#690;f(x)dx '
      '(xiii) &int;&#8315;&#8325;&#8320;^&#8309;&#8304;(x&sup3;+x)dx (xiv) &int;_(&minus;&pi;/2)^(&pi;/2)sin&#8313;x cos&#8305;&#8305;x dx '
      '(xv) &int;_(&minus;&pi;/2)^(&pi;/2)sin&#8305;&#8304;x cos&#8305;&#8305;x dx (xvi) area under y = ln e^(x&sup2;) from &minus;1 to 1 '
      '(xvii) &int;&#8320;&#690;f(x)dx equals (xviii) &int;&#8322;&sup2;(x&sup3;+3x&sup2;&minus;5x^(&minus;1/2))dx '
      '(xix) &int;&#8315;&sup2;&sup2;(x&#8309;&minus;x&sup3;+x)&#8309;(5x&#8308;&minus;3x&sup2;+1)dx (xx) &int;dx/(a&sup2;+x&sup2;).',
      '(i) (d) f^(n+1)(x)/(n+1)+c<br>(ii) (c) ln|f(x)|+c<br>(iii) (d) ln x+c<br>(iv) (d) &minus;(1/4)cos 2x+c<br>'
      '(v) (b) x&#8309;/5+c<br>(vi) (c) x&#8308;/4+c<br>(vii) (a) tan x+c<br>(viii) (b) ln(1+e&#739;)&sup2;+c<br>'
      '(ix) (b) e&#739;+c<br>(x) (c) x&sup2;/2&minus;cos x+c<br>(xi) (a) ln(cosec&#8315;&sup1;x)&#8315;&sup1;+c<br>'
      '(xii) (b) F(b)&minus;F(a)<br>(xiii) (a) 0<br>(xiv) (c) 0<br>(xv) (d) 2&int;&#8320;^(&pi;/2)sin&#8305;&#8304;x cos&#8305;&#8305;x dx<br>'
      '(xvi) (a) 2/3<br>(xvii) (c) &minus;&int;&#690;&#8320;f(x)dx<br>(xviii) (a) 0<br>(xix) (b) 0<br>'
      '(xx) (c) (1/a)tan&#8315;&sup1;(x/a)+c',
      '(viii) the key prints (a) but d/dx ln(1+e&#739;) = e&#739;/(1+e&#739;), half the integrand, so (b) is correct; '
      '(xix) u = x&#8309;&minus;x&sup3;+x is odd with u(&plusmn;2) = &plusmn;26, so [u&#8310;/6] vanishes. '
      'All others match the key letters.', 192),
    q('u6_rev6_q2', 6, REV6, 'REV6', 2,
      'Evaluate: (i) &int;(5x&sup2;&minus;3x+1)/(x&sup2;(x+1))dx (ii) &int;dx/(sin x cos x) (iii) &int;e&sup3;&#739;/(1+e&#8310;&#739;)dx '
      '(iv) &int;(ln x)&#8311;/x dx (v) &int;5cos x dx/(6+sin x&minus;sin&sup2;x) (vi) &int;x sec&sup2;x dx '
      '(vii) &int;d&theta;/(cot &theta;&minus;tan &theta;) (viii) &int;x/(1+&radic;x)dx (ix) &int;(3+3tan&sup2;x)/(1+9tan&sup2;x)dx '
      '(x) &int;cot&#8315;&sup1;2x dx (xi) &int;(1&minus;&radic;x)/(1+&radic;x)dx (xii) &int;sin&#8309;x&radic;(cos x)dx.',
      '(i) ln|(x+1)&#8313;/x&#8308;|&minus;1/x+c<br>(ii) ln|tan x|+c<br>(iii) (1/3)tan&#8315;&sup1;(e&sup3;&#739;)+c<br>'
      '(iv) (ln x)&#8312;/8+c<br>(v) ln|(sin x+2)/(sin x&minus;3)|+c<br>(vi) x tan x+ln|cos x|+c<br>'
      '(vii) (1/4)ln|sec 2&theta;|+c<br>(viii) (2/3)x^(3/2)&minus;x+2&radic;x&minus;2 ln(&radic;x+1)+c<br>'
      '(ix) tan&#8315;&sup1;(3 tan x)+c<br>(x) x cot&#8315;&sup1;2x+(1/2)ln(1+4x&sup2;)+c<br>'
      '(xi) 4&radic;x&minus;x&minus;ln(&radic;x+1)&#8308;+c<br>(xii) &minus;(2/3)cos^(3/2)x+(4/7)cos^(7/2)x&minus;(2/11)cos^(11/2)x+C',
      'Flags vs key: (i) the key&#39;s ln|x&#8315;&sup3;(x&sup2;+1)^(3/2)|&minus;1/x+4tan&#8315;&sup1;x is the antiderivative of the '
      '(x&sup2;+1) variant, not the printed x&sup2;(x+1); (vii) cot &theta;&minus;tan &theta; = 2cot 2&theta; so the argument is 2&theta;, '
      'the key omits it; (viii) the log term is &minus;2ln(&radic;x+1), the key doubles it; (x) the log term is '
      '(1/2)ln(1+4x&sup2;), the key&#39;s exponent 1/4 halves it. (ii)&ndash;(vi), (ix), (xi), (xii) match the key.', 195),
]

EX7_1 = 'Exercise 7.1'
SOLVED += [
    q('u7_ex71_q1', 7, EX7_1, 'EX7.1', 1,
      'Find the distance between the following pairs of points: (i) A(&minus;1, 3) and B(5, &minus;5)  '
      '(ii) C(&minus;1, 0) and D(0, &minus;1)  (iii) E(1, &minus;1) and F(2, 7)  (iv) G(&minus;1, &minus;4) and H(5, &minus;4)',
      '(i) 10 units<br>(ii) &radic;2 units<br>(iii) &radic;65 units<br>(iv) 6 units',
      'Distance formula on each pair: (i) &radic;(36+64)=10; (ii) &radic;(1+1)=&radic;2; (iii) &radic;(1+64)=&radic;65; '
      '(iv) &radic;(36+0)=6. All match the key.',
      203),
    q('u7_ex71_q2', 7, EX7_1, 'EX7.1', 2,
      'Find the point on the y-axis which is 5&radic;2 units away from (5, 2).',
      '(0, 7) and (0, &minus;3)',
      'P(0, y): 25+(y&minus;2)&sup2;=50 &rarr; (y&minus;2)&sup2;=25 &rarr; y=7 or &minus;3. Matches the key.',
      203),
    q('u7_ex71_q3', 7, EX7_1, 'EX7.1', 3,
      'Find the point on the x-axis which is &radic;41 units away from (&minus;7, 5).',
      '(&minus;3, 0) and (&minus;11, 0)',
      'P(x, 0): (x+7)&sup2;+25=41 &rarr; (x+7)&sup2;=16 &rarr; x=&minus;3 or &minus;11. Matches the key.',
      203),
    q('u7_ex71_q4', 7, EX7_1, 'EX7.1', 4,
      'If ABC is a triangle whose vertices are A(&minus;3, 3), B(2, 6) and C(3, 0), give the most specific name for triangle ABC.',
      'Scalene triangle',
      '|AB|=&radic;34, |BC|=&radic;37, |CA|=&radic;45; all three sides differ. Matches the key.',
      203),
    q('u7_ex71_q5', 7, EX7_1, 'EX7.1', 5,
      'If the point P(2, 1) lies on the line segment joining the points A(4, 2) and B(8, 4), then show that '
      '|AP| = &frac12;|AB|.',
      '|AP| = &radic;5 = &frac12;|AB|, shown',
      '|AP|=&radic;(4+1)=&radic;5; |AB|=&radic;(16+4)=2&radic;5; &frac12;|AB|=&radic;5=|AP|.',
      204),
    q('u7_ex71_q6', 7, EX7_1, 'EX7.1', 6,
      'Find the coordinates of the midpoint of following points: (i) M(&minus;4, 2) and N(&minus;4, &minus;2)  '
      '(ii) P(&minus;1, &minus;4) and Q(5, &minus;4)  (iii) S(1, &minus;2) and T(2, &minus;4)  (iv) X(6, 2) and Y(&minus;2, &minus;7)',
      '(i) (&minus;4, 0)<br>(ii) (2, &minus;4)<br>(iii) (3/2, &minus;3)<br>(iv) (2, &minus;5/2)',
      'Average the two endpoints. Flag: the key prints (ii) as (2, 0), but the midpoint of (&minus;1,&minus;4) and '
      '(5,&minus;4) is (2,&minus;4) &mdash; key misprint; (i), (iii), (iv) match the key.',
      204),
    q('u7_ex71_q7', 7, EX7_1, 'EX7.1', 7,
      'Find the point which divides the line segment joining (4, &minus;1) and (4, 3) in the ratio 3:1 internally.',
      '(4, 2)',
      'x=(3&middot;4+1&middot;4)/4=4; y=(3&middot;3+1&middot;(&minus;1))/4=2. Matches the key.',
      204),
    q('u7_ex71_q8', 7, EX7_1, 'EX7.1', 8,
      'The points P(&minus;2, 2), Q(2, &minus;1) and R(&minus;1, 4) are the mid-points of the sides of the triangle. '
      'Find the vertices.',
      '(1, &minus;3), (&minus;5, 7), (3, 1)',
      'Each vertex = sum of two midpoints minus the third: P+Q&minus;R=(1,&minus;3), P+R&minus;Q=(&minus;5,7), '
      'Q+R&minus;P=(3,1). Matches the key.',
      204),
    q('u7_ex71_q9', 7, EX7_1, 'EX7.1', 9,
      'Z(4, 5) and X(7, &minus;1) are two given points and the point Y divides the line-segment ZX externally in the '
      'ratio 4:3. Find the coordinates of Y.',
      'Y(16, &minus;19)',
      'External section: ((4&middot;7&minus;3&middot;4)/(4&minus;3), (4&middot;(&minus;1)&minus;3&middot;5)/(4&minus;3))='
      '(16, &minus;19). Matches the key.',
      204),
    q('u7_ex71_q10', 7, EX7_1, 'EX7.1', 10,
      'If a point P(k, 7) divides the line segment joining A(8, 9) and B(1, 2) in a ratio k&#8321;:k&#8322;, then find '
      'ratio k&#8321;:k&#8322;. Also find the value of k.',
      'k&#8321;:k&#8322; = 2:5, k = 6',
      'y: 7=(2k&#8321;+9k&#8322;)/(k&#8321;+k&#8322;) &rarr; 5k&#8321;=2k&#8322; &rarr; 2:5; then '
      'k=(k&#8321;&middot;1+k&#8322;&middot;8)/7=(2+40)/7=6. Matches the key.',
      204),
    q('u7_ex71_q11', 7, EX7_1, 'EX7.1', 11,
      'A(2, 7) and B(&minus;4, &minus;8) are coordinates of the line segment AB. There are two points that trisect the '
      'segment AB. Find the points of trisection.',
      '(0, 2) and (&minus;2, &minus;3)',
      'Section formula in ratios 1:2 and 2:1: ((&minus;4+4)/3, (&minus;8+14)/3)=(0,2); ((&minus;8+2)/3, (&minus;16+7)/3)'
      '=(&minus;2,&minus;3). Matches the key.',
      204),
    q('u7_ex71_q12', 7, EX7_1, 'EX7.1', 12,
      'The vertices P, Q and R of a triangle are (2, 1), (5, 2) and (3, 4) respectively. Find the coordinates of the '
      'circum-centre and also the radius of the circum-circle of the triangle.',
      'Circumcentre (13/4, 9/4); radius 5&radic;2/4',
      '|CP|=|CQ| gives 3h+k=12; |CQ|=|CR| gives k=h&minus;1; solving h=13/4, k=9/4; radius=|CP|='
      '&radic;(25/16+25/16)=5&radic;2/4. Matches the key.',
      204),
    q('u7_ex71_q13', 7, EX7_1, 'EX7.1', 13,
      'AB is divided into 20 equal parts by P&#8321;, P&#8322;, P&#8323;, ..., P&#8321;&#8329;. If A and B are (2, 3) and '
      '(10, 11) respectively, find the coordinates of P&#8321;&#8323;.',
      '(36/5, 41/5)',
      'P&#8321;&#8323; divides AB in ratio 13:7: ((13&middot;10+7&middot;2)/20, (13&middot;11+7&middot;3)/20)'
      '=(144/20, 164/20). Matches the key.',
      204),
    q('u7_ex71_q14', 7, EX7_1, 'EX7.1', 14,
      'If A, B and C are three collinear points and the coordinates of A and B are (3, 4) and (7, 7) respectively, '
      'find the coordinates of C if |AC| = 10 units.',
      '(11, 10)',
      'Unit vector along AB = (4/5, 3/5); C = A + 10(4/5, 3/5) = (11, 10). The key lists only this point; '
      '(&minus;5, &minus;2) on the opposite ray also satisfies |AC|=10.',
      204),
    q('u7_ex71_q15', 7, EX7_1, 'EX7.1', 15,
      'Find the coordinates of the incentre of triangle whose angular points are respectively: '
      '(i) L(2, 8), M(8, 2) and N(9, 9)  (ii) P(&minus;36, 7), Q(20, 7) and R(0, &minus;8)',
      '(i) (13/2, 13/2)<br>(ii) (&minus;1, 0)',
      'Incentre = side-weighted average of vertices. (i) sides 5&radic;2, 5&radic;2, 6&radic;2 &rarr; (104/16, 104/16); '
      '(ii) sides 25, 39, 56 &rarr; (&minus;120/120, 0/120). Matches the key.',
      204),
    q('u7_ex71_q16', 7, EX7_1, 'EX7.1', 16,
      'The line segment joining P(&minus;8, 10) and Q(6, &minus;4) is cut by x and y axes at A and B respectively. '
      'Find the ratios in which A and B divide PQ.',
      'A (x-axis): 5:2; B (y-axis): 4:3',
      'x-axis: y=0 &rarr; 4m=10n &rarr; m:n=5:2; y-axis: x=0 &rarr; 6m=8n &rarr; m:n=4:3. Matches the key.',
      204),
    q('u7_ex71_q17', 7, EX7_1, 'EX7.1', 17,
      'Find the coordinates of the centroid of a triangle whose angular points are: '
      '(i) A(1, 3), (2, 7) and (5, 6)  (ii) P(&minus;2, 5), Q(&minus;7, 1) and R(&minus;8, &minus;4)',
      '(i) (8/3, 16/3)<br>(ii) (&minus;17/3, 2/3)',
      'Centroid = average of the three vertices. Matches the key.',
      204),
    q('u7_ex71_q18', 7, EX7_1, 'EX7.1', 18,
      'A straight line passes through the points (7, 9) and (&minus;1, 1). Find a point in the line whose ordinate is 4.',
      '(2, 4)',
      'Slope = 8/8 = 1; line y = x+2; ordinate 4 &rarr; x = 2. Matches the key.',
      204),
]

EX7_2 = 'Exercise 7.2'
SOLVED += [
    q('u7_ex72_q1', 7, EX7_2, 'EX7.2', 1,
      'Find the slope of the line passing through given pair of points: (i) A(3, 7) and B(2, 9)  '
      '(ii) C(5, &minus;2) and D(3, 6)  (iii) E(5, 3) and F(&minus;2, 3)  (iv) G(0, 0) and H(a, b)',
      '(i) &minus;2<br>(ii) &minus;4<br>(iii) 0<br>(iv) b/a',
      'm=(y&#8322;&minus;y&#8321;)/(x&#8322;&minus;x&#8321;): (i) 2/(&minus;1); (ii) 8/(&minus;2); (iii) 0/(&minus;7); '
      '(iv) b/a. All match the key.',
      207),
    q('u7_ex72_q2', 7, EX7_2, 'EX7.2', 2,
      'Find the slope of the perpendicular line when the given line passes through the following pair of points: '
      '(i) A(2, 1) and B(4, 5)  (ii) C(&minus;1, 0) and D(3, 5)  (iii) E(2, 1) and F(&minus;3, 1)  '
      '(iv) G(&minus;1, 2) and H(&minus;1, &minus;5)',
      '(i) &minus;1/2<br>(ii) &minus;4/5<br>(iii) undefined<br>(iv) 0',
      'Perpendicular slope = &minus;1/m. (i) m=2; (ii) m=5/4; (iii) m=0 so perpendicular is vertical (undefined); '
      '(iv) m undefined (vertical) so perpendicular slope 0. All match the key.',
      208),
    q('u7_ex72_q3', 7, EX7_2, 'EX7.2', 3,
      'In each of the following the slope of the line is given. What is the slope of a line (a) parallel '
      '(b) perpendicular, to it?  (i) 2/3  (ii) &minus;7/2  (iii) &minus;1  (iv) 4',
      '(i) (a) 2/3, (b) &minus;3/2<br>(ii) (a) &minus;7/2, (b) 2/7<br>(iii) (a) &minus;1, (b) 1<br>'
      '(iv) (a) 4, (b) &minus;1/4',
      'Parallel keeps m; perpendicular takes &minus;1/m. All match the key.',
      208),
    q('u7_ex72_q4', 7, EX7_2, 'EX7.2', 4,
      'Are the lines l&#8321; and l&#8322; passing through the given pairs of points parallel, perpendicular or neither? '
      '(i) l&#8321;: (1, 2), (3, 1) and l&#8322;: (0, &minus;1), (2, 0)  (ii) l&#8321;: (0, 3), (3, 1) and '
      'l&#8322;: (&minus;1, 4), (&minus;7, &minus;5)  (iii) l&#8321;: (2, &minus;1), (5, &minus;7) and '
      'l&#8322;: (0, 0), (&minus;1, 2)  (iv) l&#8321;: (1, 0), (2, 0) and l&#8322;: (5, &minus;5), (&minus;10, &minus;5)',
      '(i) neither<br>(ii) perpendicular<br>(iii) parallel<br>(iv) parallel',
      '(i) m&#8321;=&minus;1/2, m&#8322;=1/2: neither equal nor m&#8321;m&#8322;=&minus;1; (ii) m&#8321;=&minus;2/3, '
      'm&#8322;=3/2: product &minus;1; (iii) both &minus;2; (iv) both 0. All match the key.',
      208),
    q('u7_ex72_q5', 7, EX7_2, 'EX7.2', 5,
      'The line through (6, &minus;4) and (&minus;3, 2) is parallel to the line through (2, 1) and (0, y). Find y.',
      'y = 7/3',
      'm&#8321;=6/(&minus;9)=&minus;2/3; (y&minus;1)/(&minus;2)=&minus;2/3 &rarr; y&minus;1=4/3. Matches the key.',
      208),
    q('u7_ex72_q6', 7, EX7_2, 'EX7.2', 6,
      'The line through (2, 5) and (&minus;3, &minus;2) is perpendicular to the line through (4, &minus;1) and (x, 3). '
      'Find x.',
      'x = &minus;8/5',
      'm&#8321;=7/5; m&#8322;=4/(x&minus;4); (7/5)(4/(x&minus;4))=&minus;1 &rarr; x&minus;4=&minus;28/5. Matches the key.',
      208),
    q('u7_ex72_q7', 7, EX7_2, 'EX7.2', 7,
      'Using slopes prove that (&minus;1, 4), (&minus;3, &minus;6) and (3, &minus;2) are the vertices of right triangle.',
      'm(BC)&middot;m(CA) = &minus;1, right angle at C &mdash; proved',
      'm(AB)=5, m(BC)=2/3, m(CA)=&minus;3/2; (2/3)(&minus;3/2)=&minus;1 so BC &perp; CA. Proof question, no key entry.',
      208),
    q('u7_ex72_q8', 7, EX7_2, 'EX7.2', 8,
      'Using slopes, find the fourth vertex of a parallelogram if (0, &minus;1), (4, &minus;3) and (12, 3) are its '
      'three consecutive vertices.',
      '(8, 5)',
      'Diagonals bisect: D = A+C&minus;B = (8, 5); slope check m(AB)=m(DC)=&minus;1/2, m(BC)=m(AD)=3/4. Matches the key.',
      208),
]

EX7_3 = 'Exercise 7.3'
SOLVED += [
    q('u7_ex73_q1', 7, EX7_3, 'EX7.3', 1,
      'Find the equations of the straight lines parallel to the coordinate axes and passing through the point '
      '(3, &minus;4).',
      'y = &minus;4 (parallel to x-axis); x = 3 (parallel to y-axis)',
      'A horizontal line keeps the y-coordinate, a vertical line keeps the x-coordinate. Matches the key.',
      217),
    q('u7_ex73_q2', 7, EX7_3, 'EX7.3', 2,
      'Find the equations of the straight lines parallel to the coordinate axes and passing through the point (5, 2).',
      'y &minus; 2 = 0 and x &minus; 5 = 0',
      'Horizontal line y = 2; vertical line x = 5. Matches the key.',
      217),
    q('u7_ex73_q3', 7, EX7_3, 'EX7.3', 3,
      'Write the equation of the straight lines parallel to x-axis which is at a distance of 5 units from above the '
      'x-axis.',
      'y = 5',
      'Horizontal line 5 units above the x-axis. Matches the key.',
      217),
    q('u7_ex73_q4', 7, EX7_3, 'EX7.3', 4,
      'Find the equation of a line parallel to y-axis which is at a distance of 6 units on its left.',
      'x = &minus;6',
      'Vertical line 6 units left of the y-axis. Flag: the key prints x = &minus;5, which matches a distance of '
      '5 units, not the printed 6 &mdash; key misprint.',
      217),
    q('u7_ex73_q5', 7, EX7_3, 'EX7.3', 5,
      'Find the equations of the straight line determined by each of the following set of conditions: '
      '(i) through (5, &minus;2) with slope 4  (ii) through (&minus;1, &minus;4) with slope &minus;2/3  '
      '(iii) through (&minus;1/4, 3/4) with slope 2/5  (iv) through (0, b) with slope m  '
      '(v) through (7, &minus;3) and (&minus;4, 1)  (vi) through (5, &minus;5) and (&minus;3, 1)  '
      '(vii) through (at&#8321;&sup2;, 2at&#8321;) and (at&#8322;&sup2;, 2at&#8322;)  '
      '(viii) y-intercept 3, slope 2  (ix) y-intercept &minus;2, slope &minus;2/3  (x) y-intercept &minus;5, slope 1/2  '
      '(xi) y-intercept 0, slope 0  (xii) x-intercept 4, y-intercept 3  (xiii) x-intercept &minus;2, y-intercept 5  '
      '(xiv) x-intercept &minus;5, y-intercept &minus;1  (xv) perpendicular from origin p = 3 making angle '
      '&alpha; = 60&deg; with x-axis  (xvi) p = 3/2, &alpha; = 150&deg;',
      '(i) 4x&minus;y&minus;22=0<br>(ii) 2x+3y+14=0<br>(iii) 8x&minus;20y+17=0<br>(iv) mx&minus;y+b=0<br>'
      '(v) 4x+11y+5=0<br>(vi) 3x+4y+5=0<br>(vii) 2x&minus;(t&#8321;+t&#8322;)y+2at&#8321;t&#8322;=0<br>'
      '(viii) y=2x+3<br>(ix) y=(&minus;2/3)x&minus;2<br>(x) y=(1/2)x&minus;5<br>(xi) y=0<br>(xii) 3x+4y=12<br>'
      '(xiii) 5x&minus;2y=&minus;10<br>(xiv) x+5y=&minus;5<br>(xv) x+&radic;3y=6<br>(xvi) &radic;3x&minus;y=&minus;3',
      'Point-slope for (i)&ndash;(vii) [(vii) slope = 2/(t&#8321;+t&#8322;)]; slope-intercept for (viii)&ndash;(xi); '
      'two-intercept for (xii)&ndash;(xiv); normal form xcos&alpha;+ysin&alpha;=p for (xv)&ndash;(xvi). '
      'All sixteen match the key.',
      217),
    q('u7_ex73_q6', 7, EX7_3, 'EX7.3', 6,
      'Reduce the equation 3x + 4y &minus; 12 = 0 to the (i) slope-intercept form (ii) two-intercept form '
      '(iii) normal or perpendicular form.',
      '(i) y = (&minus;3/4)x + 3<br>(ii) x/4 + y/3 = 1<br>(iii) (3/5)x + (4/5)y = 12/5',
      '(i) solve for y; (ii) divide by 12; (iii) divide by &radic;(9+16)=5. All match the key.',
      218),
    q('u7_ex73_q7', 7, EX7_3, 'EX7.3', 7,
      'Find the equations of the sides of the triangle whose vertices are (1, 4), (2, &minus;3) and (&minus;1, &minus;2).',
      '7x+y&minus;11=0; x+3y+7=0; 3x&minus;y+1=0',
      'Two-point form on each pair; slopes &minus;7, &minus;1/3, 3. All match the key.',
      218),
    q('u7_ex73_q8', 7, EX7_3, 'EX7.3', 8,
      'Find the equation of the perpendicular bisector of the segment joining (&minus;1, 2) and (9, 12).',
      'x + y &minus; 11 = 0',
      'Midpoint (4, 7); segment slope 1 so bisector slope &minus;1. Matches the key.',
      218),
    q('u7_ex73_q9', 7, EX7_3, 'EX7.3', 9,
      'The x-intercept of a line is the reciprocal of its y-intercept and line passes through (2, &minus;1). '
      'Find its equation.',
      'x + 4y + 2 = 0 and x + y &minus; 1 = 0',
      'With y-intercept c: cx + y/c = 1; through (2,&minus;1): 2c&sup2;&minus;c&minus;1=0 &rarr; c=1 or &minus;1/2. '
      'Both match the key.',
      218),
    q('u7_ex73_q10', 7, EX7_3, 'EX7.3', 10,
      'Find the equation of the line which passes through (&minus;2, &minus;4) and the sum of its intercepts equal to 3.',
      '4x &minus; y + 4 = 0 and x &minus; 2y &minus; 6 = 0',
      'a+b=3 with &minus;2/a&minus;4/b=1 &rarr; a&sup2;&minus;5a&minus;6=0 &rarr; a=&minus;1 or 6. Both match the key.',
      218),
    q('u7_ex73_q11', 7, EX7_3, 'EX7.3', 11,
      'Find the equation of the line which passes through (5, 6) and the y-intercept is twice that of the x-intercept.',
      '2x + y &minus; 16 = 0',
      'x/a + y/(2a) = 1 &rarr; 2x+y=2a; through (5,6): a=8. Matches the key.',
      218),
    q('u7_ex73_q12', 7, EX7_3, 'EX7.3', 12,
      'Find an equation of the line through (11, &minus;5) and parallel to a line having slope 3/2.',
      '3x &minus; 2y &minus; 43 = 0',
      'y+5 = (3/2)(x&minus;11). Matches the key.',
      218),
    q('u7_ex73_q13', 7, EX7_3, 'EX7.3', 13,
      'Find an equation of the line through (&minus;4, &minus;6) and perpendicular to the line having slope &minus;3/2.',
      '2x &minus; 3y &minus; 10 = 0',
      'Perpendicular slope 2/3: y+6 = (2/3)(x+4). Matches the key.',
      218),
]

EX7_4 = 'Exercise 7.4'
SOLVED += [
    q('u7_ex74_q1', 7, EX7_4, 'EX7.4', 1,
      'Determine whether each of the specified points is above or below the given straight line: '
      '(i) 3x + 11y &minus; 44 = 0, (10, 1), (&minus;4, 6) and (5, 3)  '
      '(ii) 10x &minus; 12y + 17 = 0, (&minus;20, &minus;15), (5, 5) and (100, 84)  '
      '(iii) 29x &minus; 17y + 31 = 0, (0, 2), (&minus;3, &minus;3) and (20, 30)',
      '(i) (10, 1) below; (&minus;4, 6) above; (5, 3) above<br>'
      '(ii) (&minus;20, &minus;15) above; (5, 5) below; (100, 84) below<br>'
      '(iii) (0, 2) above; (&minus;3, &minus;3) above; (20, 30) below',
      'Compare y of the point with y on the line at the same x, e.g. (i) line y=4&minus;(3/11)x gives 14/11 at x=10, '
      'so (10,1) is below. All nine match the key.',
      222),
    q('u7_ex74_q2', 7, EX7_4, 'EX7.4', 2,
      'In each of the following, find the perpendicular distance from the point to the line: '
      '(i) 15x &minus; 8y &minus; 5 = 0, (2, 1)  (ii) 3x &minus; 4y + 5 = 0, (4, &minus;3)  '
      '(iii) 3x + 4y + 10 = 0, (3, &minus;2)  (iv) 2x &minus; 7y + 1 = 0, (7, 4)  '
      '(v) 5x + 12y &minus; 16 = 0, (3, &minus;1)',
      '(i) 1 unit<br>(ii) 29/5 = 5.8 units<br>(iii) 11/5 = 2.2 units<br>(iv) 13/&radic;53 units<br>(v) 1 unit',
      'd = |ax&#8321;+by&#8321;+c|/&radic;(a&sup2;+b&sup2;). All five match the key.',
      222),
    q('u7_ex74_q3', 7, EX7_4, 'EX7.4', 3,
      'Find the distance between the parallel lines: (i) 5x &minus; 12y + 10 = 0, 5x &minus; 12y &minus; 16 = 0  '
      '(ii) x + y &minus; 2 = 0, 2x + 2y &minus; 1 = 0  (iii) 4x &minus; 3y + 12 = 0, 4x &minus; 3y &minus; 12 = 0',
      '(i) 2 units<br>(ii) 3&radic;2/4 units<br>(iii) 24/5 = 4.8 units',
      'd = |c&#8321;&minus;c&#8322;|/&radic;(a&sup2;+b&sup2;) after equalising coefficients; (ii) halve the second '
      'equation first. All three match the key.',
      223),
]

EX7_5 = 'Exercise 7.5'
SOLVED += [
    q('u7_ex75_q1', 7, EX7_5, 'EX7.5', 1,
      'What is the angle between two lines when they intersect at origin and one of the line passes through (2, 3) '
      'and the other line passes through (&minus;3, 6)?',
      '&theta; = tan&#8315;&sup1;(7/4)',
      'm&#8321;=3/2, m&#8322;=&minus;2; tan&theta;=|(&minus;7/2)/(&minus;2)|=7/4. Matches the key.',
      227),
    q('u7_ex75_q2', 7, EX7_5, 'EX7.5', 2,
      'Find the angle between the following two lines. l&#8321;: 4x &minus; 3y = 8 and l&#8322;: 2x + 5y = 4.',
      '&theta; = tan&#8315;&sup1;(26/7) &asymp; tan&#8315;&sup1;(3.71)',
      'm&#8321;=4/3, m&#8322;=&minus;2/5; tan&theta;=(26/15)/(7/15)=26/7. Flag: the key prints 3.69, but the exact '
      'ratio is 26/7&asymp;3.7143 (the key rounded the slopes first).',
      227),
    q('u7_ex75_q3', 7, EX7_5, 'EX7.5', 3,
      'Find the acute angle between l&#8321;: y = 3x + 1 and l&#8322;: y = &minus;4x + 3.',
      '&theta; = tan&#8315;&sup1;(7/11) &asymp; tan&#8315;&sup1;(0.636)',
      'tan&theta;=|(3+4)/(1&minus;12)|=7/11. Matches the key.',
      227),
    q('u7_ex75_q4', 7, EX7_5, 'EX7.5', 4,
      'Find the angle between two lines, one of which is the x-axis and the other line is x &minus; y + 4 = 0.',
      '45&deg;',
      'Slopes 0 and 1 give tan&theta;=1. Matches the key.',
      227),
    q('u7_ex75_q5', 7, EX7_5, 'EX7.5', 5,
      'Find the angle between the lines 2x &minus; 3y + 7 = 0 and 7x + 4y &minus; 9 = 0.',
      '&theta; = tan&#8315;&sup1;(29/2)',
      'm&#8321;=2/3, m&#8322;=&minus;7/4; tan&theta;=(29/12)/(2/12)=29/2. Matches the key.',
      227),
    q('u7_ex75_q6', 7, EX7_5, 'EX7.5', 6,
      'Find the equation of line through point (3, 2) and making angle 45&deg; with the line x &minus; 2y = 3.',
      '3x &minus; y &minus; 7 = 0 and x + 3y &minus; 9 = 0',
      'Given slope 1/2; |(m&minus;1/2)/(1+m/2)|=1 gives m=3 or &minus;1/3. Both match the key.',
      227),
    q('u7_ex75_q7', 7, EX7_5, 'EX7.5', 7,
      'Determine the measure of the acute angle between the straight-line x &minus; y + 4 = 0 and the straight line '
      'passing through the points (3, &minus;2) and (&minus;2, 4).',
      '&theta; = tan&#8315;&sup1;(11) &asymp; 84.8055&deg;',
      'm&#8321;=1, m&#8322;=&minus;6/5; tan&theta;=(11/5)/(1/5)=11. Matches the key.',
      227),
    q('u7_ex75_q8', 7, EX7_5, 'EX7.5', 8,
      'Find the equation of family of lines that pass through the point of intersection of 2x + 3y &minus; 8 = 0 and '
      'x &minus; y + 1 = 0. Also find the point of intersection.',
      'a(2x + 3y &minus; 8) + b(x &minus; y + 1) = 0; point of intersection (1, 2)',
      'Family through the common point; solving the pair gives x=1, y=2. The key prints the family only.',
      227),
    q('u7_ex75_q9', 7, EX7_5, 'EX7.5', 9,
      'Find the equation of a line through the intersection of the lines: (i) 2x + 3y + 1 = 0, 3x &minus; 4y = 5 and '
      'passing through (2, 1)  (ii) x &minus; 4y = 3, x + 2y = 9 and passing through the origin  '
      '(iii) 3x + 2y = 8, 5x &minus; 11y + 1 = 0 and parallel to 6x + 13y = 25  (iv) 2x &minus; 3y + 4 = 0, '
      '3x + 3y &minus; 5 = 0 and parallel to y-axis  (v) 5x &minus; 6y = 1, 3x + 2y + 5 = 0 and perpendicular to '
      '5y &minus; 3x = 11  (vi) 3x &minus; 4y + 1 = 0, 5x + y &minus; 1 = 0 and cutting off equal intercepts from the '
      'axes  (vii) 43x + 29y + 43 = 0, 23x + 8y + 6 = 0 and having y-intercept &minus;2  (viii) 2x + 7y &minus; 8 = 0, '
      '3x + 2y + 5 = 0 and making an angle of 45&deg; with the line 2x + 3y &minus; 7 = 0',
      '(i) 30x&minus;23y&minus;37=0<br>(ii) x&minus;7y=0<br>(iii) 6x+13y&minus;25=0<br>(iv) 5x&minus;1=0<br>'
      '(v) 5x+3y+8=0<br>(vi) 23x+23y=11<br>(vii) x+2y+4=0<br>(viii) x&minus;5y+13=0',
      'Family L&#8321;+kL&#8322;=0 with k from the condition: (i) k=8/3; (ii) k=&minus;1/3; (iii) k=&minus;27/131; '
      '(iv) k=1; (v) k=45; (vi) k=&minus;7/4; (vii) k=&minus;3/2; (viii) k=&minus;1. Flag: (viii) the second 45&deg; '
      'case (k=&minus;33/7) gives 5x+y+13=0, also valid but not in the key. The eight key answers match.',
      227),
    q('u7_ex75_q10', 7, EX7_5, 'EX7.5', 10,
      'Find the angles of the triangle with the given vertices (1, 2), (3, 4) and (2, 5).',
      '26.5650&deg;, 63.4349&deg;, 90&deg;',
      'Side slopes 1, &minus;1, 3: slopes 1 and &minus;1 are perpendicular (90&deg;); tan of the others 1/2 and 2. '
      'Matches the key.',
      228),
    q('u7_ex75_q11', 7, EX7_5, 'EX7.5', 11,
      'What are the angles of the triangle with vertices A(3, 2), B(4, 5) and C(&minus;1, &minus;1)?',
      'A = 145.3&deg;, B = 21.37&deg;, C = 13.33&deg;',
      'Side slopes AB=3, BC=6/5, CA=3/4; at B tan=9/23, at C tan=9/38; at A the interior angle is obtuse, '
      '180&deg;&minus;34.70&deg;. Matches the key.',
      228),
    q('u7_ex75_q12', 7, EX7_5, 'EX7.5', 12,
      'Find the angles of triangle where the slopes of its sides are 3, 1/2, &minus;2.',
      '90&deg;, 45&deg;, 45&deg;',
      '(1/2)(&minus;2)=&minus;1 gives the right angle; the other two pairs give tan&theta;=1. Matches the key.',
      228),
]

EX7_6 = 'Exercise 7.6'
SOLVED += [
    q('u7_ex76_q1', 7, EX7_6, 'EX7.6', 1,
      'If A(2, 5), B(3, 7) and C(0, 8) are the vertices of a triangle then find the (i) equation of median through A '
      '(ii) equation of altitude through B (iii) equation of right bisector of side AC.',
      '(i) 5x+y&minus;15=0<br>(ii) 2x&minus;3y+15=0<br>(iii) 4x&minus;6y+35=0',
      '(i) midpoint of BC (3/2, 15/2), slope &minus;5; (ii) slope AC=&minus;3/2 so altitude slope 2/3 through B; '
      '(iii) midpoint of AC (1, 13/2), slope 2/3. All match the key.',
      236),
    q('u7_ex76_q2', 7, EX7_6, 'EX7.6', 2,
      'Show that the following lines are concurrent. Also find their point of concurrency: '
      '(i) x &minus; y = 6, 4y + 22 = 3x and 6x + 5y + 8 = 0  (ii) x/a + y/b = 1, x/b + y/a = 1 and y = x  '
      '(iii) 5x + y + 11 = 0, x + 7y + 9 = 0 and 2x + y + 5 = 0',
      '(i) (2, &minus;4)<br>(ii) (ab/(a+b), ab/(a+b))<br>(iii) (&minus;2, &minus;1)',
      'Intersect the first two lines and verify the third passes through the point; in (ii) subtracting the first '
      'two gives x=y, the third line. All match the key.',
      236),
    q('u7_ex76_q3', 7, EX7_6, 'EX7.6', 3,
      'If A(&minus;1, 5), B(2, 3) and C(7, 6) are the vertices of triangle, then show right bisectors, medians and '
      'altitudes of the triangle are concurrent.',
      'Medians at centroid (8/3, 14/3); right bisectors at circumcentre (105/38, 281/38); altitudes at orthocentre '
      '(47/19, &minus;15/19) &mdash; each family concurrent, shown',
      'Each family&#39;s third line is verified to pass through the intersection of the first two. Proof question, '
      'no key entry.',
      236),
]

EX7_7 = 'Exercise 7.7'
SOLVED += [
    q('u7_ex77_q1', 7, EX7_7, 'EX7.7', 1,
      'Find the area of the triangle whose vertices are: (i) (11, &minus;12), (6, 2) and (&minus;5, 10)  '
      '(ii) (3, 1), (&minus;2, 5) and (&minus;4, &minus;5)  (iii) (&minus;5, &minus;2), (4, &minus;6) and (1, 7)  '
      '(iv) (&minus;a, b + c), (a, b &minus; c) and (a, &minus;c)  (v) (a cos &theta;&#8321;, b sin &theta;&#8321;), '
      '(a cos &theta;&#8322;, b sin &theta;&#8322;) and (a cos &theta;&#8323;, b sin &theta;&#8323;)',
      '(i) 57 square units<br>(ii) 29 square units<br>(iii) 52.5 square units<br>(iv) ab square units<br>'
      '(v) &frac12;ab{sin(&theta;&#8321;&minus;&theta;&#8322;) + sin(&theta;&#8322;&minus;&theta;&#8323;) + '
      'sin(&theta;&#8323;&minus;&theta;&#8321;)}',
      'Area = &frac12;|x&#8321;(y&#8322;&minus;y&#8323;)+x&#8322;(y&#8323;&minus;y&#8321;)+x&#8323;(y&#8321;&minus;y&#8322;)|; '
      '(v) the bracket telescopes into the sine differences. Flag: the key mislabels the (iv) answer as (vi). '
      'All match the key.',
      238),
    q('u7_ex77_q2', 7, EX7_7, 'EX7.7', 2,
      'Find the area of a quadrilateral whose consecutive vertices are: (i) (3, &minus;3), (7, 5), (1, 2) and '
      '(&minus;3, 4)  (ii) (2, 3), (&minus;1, 2), (&minus;3, 2) and (3, &minus;3)',
      '(i) 26 square units<br>(ii) 14.5 square units',
      'Shoelace formula: (i) sum 52; (ii) sum 29; halve each. Both match the key.',
      238),
    q('u7_ex77_q3', 7, EX7_7, 'EX7.7', 3,
      'Prove, by the method of the area of a triangle, that the following points are collinear: '
      '(i) (2, 3), (5, 0) and (4, 1)  (ii) (2, 1), (4, &minus;1) and (1, 2)  (iii) (&minus;1, &minus;1), (5, 7) '
      'and (8, 11)',
      'Each triangle area = 0, so each triple is collinear &mdash; proved',
      '(i) &frac12;|&minus;2&minus;10+12|=0; (ii) &frac12;|&minus;6+4+2|=0; (iii) &frac12;|4+60&minus;64|=0. '
      'Proof question, no key entries.',
      238),
    q('u7_ex77_q4', 7, EX7_7, 'EX7.7', 4,
      'Find the area of triangle formed by the lines: (i) y = 0, y = 2x and y = 6x + 5  (ii) y &minus; x = 0, '
      'y + x = 0 and x &minus; c = 0  (iii) y = 2x + 3, 2y + 3x = 3 and x + y + 2 = 0',
      '(i) 25/24 square units<br>(ii) c&sup2; square units<br>(iii) 338/21 square units',
      'Vertices from pairwise intersections: (i) (0,0), (&minus;5/6,0), (&minus;5/4,&minus;5/2); (ii) (0,0), (c,c), '
      '(c,&minus;c); (iii) (&minus;3/7,15/7), (&minus;5/3,&minus;1/3), (7,&minus;9). All match the key.',
      238),
]

EX7_8 = 'Exercise 7.8'
SOLVED += [
    q('u7_ex78_q1', 7, EX7_8, 'EX7.8', 1,
      'Separate the pair of lines represented by the given equations and state their nature: '
      '(i) x&sup2; &minus; 5xy + 6y&sup2; = 0  (ii) 4x&sup2; &minus; xy &minus; 5y&sup2; = 0  '
      '(iii) 9x&sup2; &minus; 6xy + y&sup2; = 0  (iv) 10x&sup2; &minus; 3xy &minus; y&sup2; = 0  '
      '(v) 7x&sup2; &minus; 3xy + 5y&sup2; = 0',
      '(i) x &minus; 3y = 0, x &minus; 2y = 0; two real distinct lines<br>'
      '(ii) 4x &minus; 5y = 0, x + y = 0; two real distinct lines<br>'
      '(iii) 3x &minus; y = 0 twice; coincident real lines<br>'
      '(iv) 2x &minus; y = 0, 5x + y = 0; two real distinct lines<br>'
      '(v) h&sup2; &minus; ab = 9/4 &minus; 35 &lt; 0; two imaginary lines (only the origin is real)',
      'Factor each quadratic in y/x. (v) does not factor over the reals: y = [(3 &plusmn; &radic;(&minus;131))/10]x. '
      'Matches the key (the book misnumbers the parts (i),(ii),(ii),(iii),(v); they are renumbered (i)&ndash;(v) '
      'here in printed order, and the key follows the book\u2019s misnumbering).',
      242),
    q('u7_ex78_q2', 7, EX7_8, 'EX7.8', 2,
      'Find the combined equation of the pair of lines through the origin perpendicular to the given pair: '
      '(i) 2x&sup2; &minus; 5xy + y&sup2; = 0  (ii) 6x&sup2; &minus; 13xy + 6y&sup2; = 0',
      '(i) x&sup2; + 5xy + 2y&sup2; = 0<br>(ii) 6x&sup2; + 13xy + 6y&sup2; = 0',
      'The pair perpendicular to ax&sup2; + 2hxy + by&sup2; = 0 is bx&sup2; &minus; 2hxy + ay&sup2; = 0. '
      'Both match the key.',
      242),
    q('u7_ex78_q3', 7, EX7_8, 'EX7.8', 3,
      'Trace (separate) the pair of lines represented by: (i) x&sup2; &minus; 3xy + 2y&sup2; = 0  '
      '(ii) x&sup2; &minus; 6xy + 9y&sup2; = 0  (iii) 6x&sup2; &minus; xy &minus; y&sup2; = 0  '
      '(iv) 8x&sup2; &minus; 3xy &minus; y&sup2; = 0',
      '(i) y = x and y = x/2<br>(ii) coincident line y = x/3<br>(iii) y = 2x and y = &minus;3x<br>'
      '(iv) y = [(&minus;3 + &radic;41)/2]x and y = [(&minus;3 &minus; &radic;41)/2]x',
      '(i)&ndash;(iii) factor directly; (iv) needs the quadratic t&sup2; + 3t &minus; 8 = 0 for t = y/x, '
      'giving real distinct lines through the origin. Trace question, no key entries.',
      242),
    q('u7_ex78_q4', 7, EX7_8, 'EX7.8', 4,
      'Find the angle between the pair of lines represented by: (i) x&sup2; &minus; 5xy + 6y&sup2; = 0  '
      '(ii) 3x&sup2; + 7xy + 2y&sup2; = 0  (iii) x&sup2; + 2xy &minus; 3y&sup2; = 0  '
      '(iv) x&sup2; + xy &minus; 2y&sup2; = 0',
      '(i) tan&#8315;&sup1;(1/7)<br>(ii) 45&deg;<br>(iii) 116&deg;34&#8242; (tan &theta; = &minus;2)<br>'
      '(iv) 108&deg;26&#8242; (tan &theta; = &minus;3)',
      'tan &theta; = 2&radic;(h&sup2; &minus; ab)/(a + b). (i) a=1, h=&minus;5/2, b=6 &rarr; tan &theta; = 1/7; '
      '(ii) &rarr; 1; (iii) &rarr; &minus;2 (obtuse); (iv) &rarr; &minus;3 (obtuse). All match the key.',
      242),
    q('u7_ex78_q5', 7, EX7_8, 'EX7.8', 5,
      'If one of the gradients of the lines represented by ax&sup2; + 2hxy + by&sup2; = 0 is twice the other, '
      'show that 8h&sup2; = 9ab.',
      'Proof: let the gradients be m and 2m. Then m + 2m = &minus;2h/b &rarr; m = &minus;2h/(3b), and '
      'm&middot;2m = a/b &rarr; 2m&sup2; = a/b. Substituting: 2&middot;4h&sup2;/(9b&sup2;) = a/b &rarr; '
      '8h&sup2; = 9ab. (Shown)',
      'Uses sum and product of roots of bt&sup2; + 2ht + a = 0 where t is the gradient. '
      'Proof question, no key entry.',
      242),
]

REV7 = 'Review Exercise 7'
SOLVED += [
    q('u7_rev7_q1', 7, REV7, 'REV7', 1,
      'Select the correct option: (i) The slope of the line that passes through (&minus;3, &minus;4) and (7, 6) is '
      '(a) 0  (b) undefined  (c) &minus;1  (d) 1.  (ii) A line with a slope of 1/2 and a y-intercept 7 is '
      '(a) 2y = x &minus; 7  (b) y = (1/2)x + 7  (c) y = (1/2)x &minus; 7  (d) x &minus; 2y = 14.  '
      '(iii) Two lines are said to be parallel if and only if their slopes are  (a) equal  (b) unequal  '
      '(c) does not exist  (d) negative reciprocals of each other.  (iv) Two lines l&#8321; and l&#8322; are said '
      'to be perpendicular if and only if  (a) m&#8321;m&#8322; = &minus;1  (b) m&#8321;m&#8322; = 1  '
      '(c) m&#8321; = &minus;m&#8322;  (d) m&#8321; = 1/m&#8322;.  (v) The slope of a line that is perpendicular '
      'to a vertical line is  (a) 0  (b) 1  (c) 90&deg;  (d) undefined.  (vi) The slope of the line which makes '
      'an angle 45&deg; with the line 3x &minus; y = &minus;5 is  (a) 2  (b) 1/2  (c) 1/2, &minus;2  (d) &minus;2.  '
      '(vii) The point on the line 2x &minus; 3y = 5 which is equidistant from (1, 2) and (3, 4) is  '
      '(a) (&minus;2, 2)  (b) (4, 1)  (c) (1, &minus;1)  (d) (4, 6).  (viii) In a plane three or more points are '
      'said to be collinear if  (a) they lie on a circle  (b) they form a closed loop together  (c) they lie on a '
      'straight line  (d) they do not make any defined shape.  (ix) If the line coincides with the x-axis then its '
      'equation is  (a) y = b  (b) &minus;b  (c) y = 0  (d) &infin;.  (x) The general equation of line also known '
      'as standard equation of line is  (a) ax + by + c = 0  (b) y = ax + c  (c) y &minus; y&#8321; = m(x &minus; '
      'x&#8321;)  (d) x/a + y/b = 1',
      '(i) (d)<br>(ii) (b)<br>(iii) (a)<br>(iv) (a)<br>(v) (a)<br>(vi) (c)<br>(vii) (b)<br>(viii) (c)<br>'
      '(ix) (c)<br>(x) (a)',
      '(i) (6+4)/(7+3) = 1. (ii) y = (1/2)x + 7 is option (b) itself. (vi) |(m&minus;3)/(1+3m)| = 1 '
      '&rarr; m = 1/2 or &minus;2; the key misprints this as (b), but the complete option is (c). '
      '(vii) intersection of 2x &minus; 3y = 5 with the bisector x + y = 5 gives (4, 1).',
      242),
    q('u7_rev7_q2', 7, REV7, 'REV7', 2,
      'Find the value(s) of a if the distance between the points (5, &minus;2) and (1, a) is 5 units.',
      'a = 1 or a = &minus;5',
      '16 + (a + 2)&sup2; = 25 &rarr; (a + 2)&sup2; = 9 &rarr; a + 2 = &plusmn;3. Matches the key.',
      243),
    q('u7_rev7_q3', 7, REV7, 'REV7', 3,
      'M(3, 8) is the midpoint of AB where A is (&minus;2, 3). Find B.',
      'B = (8, 13)',
      'B = (2&middot;3 &minus; (&minus;2), 2&middot;8 &minus; 3) = (8, 13). Matches the key.',
      243),
    q('u7_rev7_q4', 7, REV7, 'REV7', 4,
      'Find the centre of the circle whose diameter has endpoints (2, &minus;3) and (&minus;6, 5).',
      '(&minus;2, 1)',
      'The centre is the midpoint of a diameter: ((2&minus;6)/2, (&minus;3+5)/2) = (&minus;2, 1). Matches the key.',
      243),
    q('u7_rev7_q5', 7, REV7, 'REV7', 5,
      'Find the point that divides the segment joining P(&minus;1, 7) and Q(4, &minus;3) in the ratio 2:3.',
      '(1, 3)',
      'Section formula: ((2&middot;4 + 3&middot;(&minus;1))/5, (2&middot;(&minus;3) + 3&middot;7)/5) = (1, 3). '
      'Matches the key.',
      243),
    q('u7_rev7_q6', 7, REV7, 'REV7', 6,
      'Find the points of trisection of the segment joining A(&minus;6, 11) and B(10, &minus;3).',
      '(&minus;2/3, 19/3) and (14/3, 5/3)',
      'P = A + (1/3)(B &minus; A) = (&minus;2/3, 19/3); Q = A + (2/3)(B &minus; A) = (14/3, 5/3). Matches the key.',
      243),
    q('u7_rev7_q7', 7, REV7, 'REV7', 7,
      'Two vertices of a triangle are (1, 4) and (3, 1) and its centroid is the origin. Find the third vertex.',
      '(&minus;4, &minus;5)',
      '(1 + 3 + x)/3 = 0 and (4 + 1 + y)/3 = 0 &rarr; x = &minus;4, y = &minus;5. Matches the key.',
      243),
    q('u7_rev7_q8', 7, REV7, 'REV7', 8,
      'Find the slope of a line perpendicular to the line &minus;2y = &minus;8x + 9.',
      '&minus;1/4',
      'The given line is y = 4x &minus; 9/2, slope 4; the perpendicular slope is &minus;1/4. Matches the key.',
      243),
    q('u7_rev7_q9', 7, REV7, 'REV7', 9,
      'Write the equation of the line in two-intercept form having x-intercept (6, 0) and y-intercept (0, 5).',
      'x/6 + y/5 = 1',
      'Two-intercept form x/a + y/b = 1 with a = 6, b = 5. Matches the key.',
      243),
    q('u7_rev7_q10', 7, REV7, 'REV7', 10,
      'Find the slope and y-intercept of each line: (a) y = 12x &minus; 6  (b) y = 5 &minus; 2x  '
      '(c) 4x &minus; y + 13 = 0  (d) y = 4x',
      '(a) slope 12, y-intercept &minus;6<br>(b) slope &minus;2, y-intercept 5<br>'
      '(c) slope 4, y-intercept 13<br>(d) slope 4, y-intercept 0',
      'Read off the slope-intercept form y = mx + c; (c) rewrites as y = 4x + 13. All match the key.',
      244),
    q('u7_rev7_q11', 7, REV7, 'REV7', 11,
      'Find the x- and y-intercepts of the line 4x + 8y + 2 = 0.',
      'x-intercept &minus;1/2; y-intercept &minus;1/4',
      'Set y = 0: x = &minus;2/4 = &minus;1/2. Set x = 0: y = &minus;2/8 = &minus;1/4. Matches the key.',
      244),
    q('u7_rev7_q12', 7, REV7, 'REV7', 12,
      'Find k so that the line through (3, k) and (2, 7) is parallel to the line through (&minus;1, 4) and (0, 6).',
      'k = 9',
      'Second slope = (6&minus;4)/(0&minus;(&minus;1)) = 2; parallel lines have equal slopes, so '
      '(k &minus; 7)/(3 &minus; 2) = 2 &rarr; k = 9. Matches the key.',
      244),
    q('u7_rev7_q13', 7, REV7, 'REV7', 13,
      'Determine whether each pair of lines is parallel, perpendicular, or neither: (a) y = 2x + 7, y = 7x &minus; 2  '
      '(b) x = 1, x = 5  (c) x = &minus;3, y = &minus;3',
      '(a) neither<br>(b) parallel<br>(c) perpendicular',
      '(a) slopes 2 and 7: neither equal nor negative reciprocals. (b) both vertical. (c) one vertical, one '
      'horizontal. All match the key.',
      244),
    q('u7_rev7_q14', 7, REV7, 'REV7', 14,
      'Find k so that the lines y = 3x &minus; 1, 2y = x + 3 and 3y = kx + 4 are concurrent.',
      'k = 2',
      'The first two meet at (1, 2); substituting in the third: 6 = k + 4 &rarr; k = 2. Matches the key.',
      244),
    q('u7_rev7_q15', 7, REV7, 'REV7', 15,
      'For the lines ax &minus; 2y &minus; 1 = 0 and 6x &minus; 4y &minus; b = 0, find the values of a and b when '
      'the lines are (i) parallel  (ii) perpendicular  (iii) coincident  (iv) have no common point.',
      '(i) a = 3, b &ne; 2<br>(ii) a = &minus;4/3, any b<br>(iii) a = 3, b = 2<br>(iv) a = 3, b &ne; 2',
      'Slopes a/2 and 3/2; intercepts &minus;1/2 and &minus;b/4. Perpendicular: (a/2)(3/2) = &minus;1 &rarr; '
      'a = &minus;4/3. Coincident: a = 3 and b/4 = 1/2 &rarr; b = 2. Flag: the key interchanges the labels of '
      '(ii) and (iii) relative to the question; the mapping above is the correct one.',
      244),
    q('u7_rev7_q16', 7, REV7, 'REV7', 16,
      'Find the equation of the line through the intersection of x + 2y &minus; 5 = 0 and 3x &minus; 2y + 1 = 0 '
      'that is (i) parallel to 4x + 3y &minus; 5 = 0  (ii) perpendicular to 2x &minus; 3y + 7 = 0.',
      '(i) 4x + 3y &minus; 10 = 0<br>(ii) 3x + 2y &minus; 7 = 0',
      'Intersection point: adding the equations gives 4x = 4, x = 1, y = 2, i.e. (1, 2). (i) slope &minus;4/3: '
      'y &minus; 2 = &minus;4/3(x &minus; 1). (ii) perpendicular slope &minus;3/2: y &minus; 2 = &minus;3/2(x &minus; 1). '
      'Both match the key.',
      244),
    q('u7_rev7_q17', 7, REV7, 'REV7', 17,
      'Find the distance of the point from the line: (i) (2, 1) from 15x &minus; 8y &minus; 5 = 0  '
      '(ii) (7, 4) from 2x &minus; 7y + 1 = 0',
      '(i) 1 unit (point below the line)<br>(ii) 13/&radic;53 units',
      'd = |ax&#8321; + by&#8321; + c|/&radic;(a&sup2; + b&sup2;). (i) |30 &minus; 8 &minus; 5|/17 = 1; the key '
      'prints the signed value &minus;1 with \u201cpoint below the line\u201d. (ii) |14 &minus; 28 + 1|/&radic;53 = '
      '13/&radic;53. Matches the key otherwise.',
      244),
]

EX8_1 = 'Exercise 8.1'
SOLVED += [
    q('u8_ex81_q1', 8, EX8_1, 'EX8.1', 1,
      'Describe the condition under which a plane cuts a right circular cone to produce: (i) circle  '
      '(ii) parabola  (iii) ellipse  (iv) hyperbola  (v) a degenerate conic',
      '(i) plane perpendicular to the axis<br>(ii) plane parallel to exactly one generator<br>'
      '(iii) plane cuts all generators of one nappe but is not perpendicular to the axis<br>'
      '(iv) plane parallel to the axis (cuts both nappes)<br>(v) plane passes through the vertex',
      'With semi-vertical angle &alpha; and plane-axis angle &beta;: circle &beta; = 90&deg;; parabola '
      '&beta; = &alpha;; ellipse &alpha; &lt; &beta; &lt; 90&deg;; hyperbola 0 &le; &beta; &lt; &alpha;; '
      'through the vertex the section degenerates to a point, a line, or a pair of lines. Descriptive question, '
      'no key entry.',
      249),
    q('u8_ex81_q2', 8, EX8_1, 'EX8.1', 2,
      'Find the equation of the circle if: (i) centre is at origin and radius 5&radic;2 units  (ii) centre is '
      '(&minus;5, 7) and radius 6 units  (iii) (2, &minus;3) and (&minus;4, 7) are the ends of its diameter  '
      '(iv) centre is at origin and contains a point (5, 6)  (v) centre is at (2, 3) and contains the point '
      '(5, 7)  (vi) centre is at (p, q) and radius of &radic;(p&sup2; + q&sup2;) units',
      '(i) x&sup2; + y&sup2; = 50<br>(ii) x&sup2; + y&sup2; + 10x &minus; 14y + 38 = 0<br>'
      '(iii) x&sup2; + y&sup2; + 2x &minus; 4y &minus; 29 = 0<br>(iv) x&sup2; + y&sup2; = 61<br>'
      '(v) x&sup2; + y&sup2; &minus; 4x &minus; 6y &minus; 12 = 0<br>(vi) x&sup2; + y&sup2; &minus; 2px &minus; '
      '2qy = 0',
      'Use (x &minus; h)&sup2; + (y &minus; k)&sup2; = r&sup2;. (iii) centre = midpoint (&minus;1, 2), '
      'r = &frac12;&radic;136 = &radic;34. (iv) r&sup2; = 25 + 36 = 61. (v) r&sup2; = 9 + 16 = 25. '
      'All match the key.',
      249),
    q('u8_ex81_q3', 8, EX8_1, 'EX8.1', 3,
      'Find the centre and radius of each of the following circles and draw them: (i) x&sup2; + y&sup2; &minus; '
      '25 = 0  (ii) (x + 3)&sup2; + (y &minus; 5)&sup2; = 49  (iii) x&sup2; + y&sup2; &minus; 6x + 8y + 10 = 0  '
      '(iv) x&sup2; + y&sup2; &minus; 8x + 9 = 0  (v) 5x&sup2; + 5y&sup2; + 20x &minus; 15y + 10 = 0',
      '(i) centre (0, 0), radius 5<br>(ii) centre (&minus;3, 5), radius 7<br>(iii) centre (3, &minus;4), radius '
      '&radic;15<br>(iv) centre (4, 0), radius &radic;7<br>(v) centre (&minus;2, 3/2), radius &radic;17/2',
      'Centre (&minus;g, &minus;f), r = &radic;(g&sup2; + f&sup2; &minus; c) after making the squared coefficients '
      '1; (v) divide by 5 first: x&sup2; + y&sup2; + 4x &minus; 3y + 2 = 0. Sketch: a circle at each centre with '
      'the stated radius. All match the key.',
      250),
    q('u8_ex81_q4', 8, EX8_1, 'EX8.1', 4,
      'Find the value of k if the radius of the circle 2x&sup2; + 2y&sup2; &minus; 8x + 4y + 3k = 0 is 10 units.',
      'k = &minus;190/3',
      'Divide by 2: x&sup2; + y&sup2; &minus; 4x + 2y + 3k/2 = 0; r&sup2; = 4 + 1 &minus; 3k/2 = 100 &rarr; '
      '3k/2 = &minus;95. Matches the key.',
      250),
    q('u8_ex81_q5', 8, EX8_1, 'EX8.1', 5,
      'Find the equation of the circle passing through (&minus;3, &minus;4) and concentric with the circle '
      'x&sup2; + y&sup2; &minus; 6x + 8y &minus; 24 = 0. Also identify the outer circle.',
      'x&sup2; + y&sup2; &minus; 6x + 8y &minus; 11 = 0; the given circle is the outer circle',
      'Both circles share centre (3, &minus;4). Required radius&sup2; = (&minus;3 &minus; 3)&sup2; + '
      '(&minus;4 + 4)&sup2; = 36 (r = 6); the given circle has r = &radic;49 = 7 &gt; 6, so it is the outer one. '
      'Matches the key.',
      250),
    q('u8_ex81_q6', 8, EX8_1, 'EX8.1', 6,
      'Show that the equations x = a cos &theta; and y = a sin &theta; represent a circle with centre at the '
      'origin and radius equal to a.',
      'x&sup2; + y&sup2; = a&sup2;cos&sup2;&theta; + a&sup2;sin&sup2;&theta; = a&sup2;, the circle centred at '
      '(0, 0) with radius a. (Shown)',
      'Squaring and adding eliminates &theta; via cos&sup2; + sin&sup2; = 1. Proof question, no key entry.',
      250),
    q('u8_ex81_q7', 8, EX8_1, 'EX8.1', 7,
      'Prove that the equation of a circle (i) through the origin has no constant term  (ii) with centre on the '
      'x-axis has no term in y  (iii) with centre on the y-axis has no term in x  (iv) with centre at the origin '
      'has no term in x and y both.',
      '(i) substituting (0, 0) in x&sup2; + y&sup2; + 2gx + 2fy + c = 0 gives c = 0<br>(ii) centre on x-axis '
      '&rarr; f = 0, so the 2fy term vanishes<br>(iii) centre on y-axis &rarr; g = 0, so the 2gx term vanishes<br>'
      '(iv) centre at origin &rarr; g = f = 0, both linear terms vanish. (Proved)',
      'Centre is (&minus;g, &minus;f); each geometric condition forces the matching coefficient to zero. '
      'Proof question, no key entry.',
      250),
]

EX8_2 = 'Exercise 8.2'
SOLVED += [
    q('u8_ex82_q1', 8, EX8_2, 'EX8.2', 1,
      'Find the equation of the circle through the given points: (i) (0, 0), (0, 3), (&minus;4, 0)  '
      '(ii) (0, 10), (&minus;10, 0), (8, 6)  (iii) (0, 3), (2, &minus;1), (1, 0)  (iv) (7, &minus;3), '
      '(&minus;7, 5), (11, 5)  (v) (1, 1), (2, &minus;1), (3, &minus;2)',
      '(i) x&sup2; + y&sup2; + 4x &minus; 3y = 0<br>(ii) x&sup2; + y&sup2; = 100<br>'
      '(iii) x&sup2; + y&sup2; &minus; 10x &minus; 6y + 9 = 0<br>(iv) x&sup2; + y&sup2; &minus; 4x &minus; 9y '
      '&minus; 57 = 0<br>(v) x&sup2; + y&sup2; &minus; 13x &minus; 5y + 16 = 0',
      'Substitute each point into x&sup2; + y&sup2; + 2gx + 2fy + c = 0 and solve the three linear equations; '
      'e.g. (iv) gives g = &minus;2, f = &minus;9/2, c = &minus;57 and (v) gives g = &minus;13/2, f = &minus;5/2, '
      'c = 16. All match the key.',
      254),
    q('u8_ex82_q2', 8, EX8_2, 'EX8.2', 2,
      'Find the equation of the circle through the points (1, 2), (2, 3) and having centre on (i) the x-axis  '
      '(ii) the y-axis.',
      '(i) x&sup2; + y&sup2; &minus; 8x + 3 = 0<br>(ii) x&sup2; + y&sup2; &minus; 8y + 11 = 0',
      '(i) centre on x-axis &rarr; f = 0; the two points give g = &minus;4, c = 3. (ii) g = 0 gives f = &minus;4, '
      'c = 11. Both match the key.',
      255),
    q('u8_ex82_q3', 8, EX8_2, 'EX8.2', 3,
      'Find the equation of the circle through the points (3, 1), (2, 2) and having centre on the line '
      'x + y &minus; 3 = 0.',
      'x&sup2; + y&sup2; &minus; 4x &minus; 2y + 4 = 0',
      'Centre (&minus;g, &minus;f) on the line &rarr; g + f = &minus;3; the points give g &minus; f = &minus;1, '
      'so g = &minus;2, f = &minus;1, c = 4. Matches the key.',
      255),
    q('u8_ex82_q4', 8, EX8_2, 'EX8.2', 4,
      'Find the equation of the circle through the points (0, &minus;1) and (3, 0) when the line '
      '3x + y &minus; 9 = 0 is tangent to it at (3, 0).',
      'x&sup2; + y&sup2; &minus; 3x + y = 0',
      'The centre lies on the normal at (3, 0), i.e. x &minus; 3y &minus; 3 = 0 (slope 1/3), giving g = 3f &minus; 3; '
      'with the two point equations f = 1/2, g = &minus;3/2, c = 0. Matches the key.',
      255),
    q('u8_ex82_q5', 8, EX8_2, 'EX8.2', 5,
      'Find the equation of the circle through the origin with x-intercept 2 which is tangent to the line '
      'y &minus; 1 = 0.',
      'x&sup2; + y&sup2; &minus; 2x = 0',
      'Origin &rarr; c = 0; point (2, 0) &rarr; g = &minus;1; tangency to y = 1: |&minus;f &minus; 1| = '
      '&radic;(1 + f&sup2;) &rarr; f = 0. Centre (1, 0), radius 1. Matches the key.',
      255),
    q('u8_ex82_q6', 8, EX8_2, 'EX8.2', 6,
      'Find the equation of a circle containing the points (1, 2), (2, 3) and having centre on '
      'x &minus; y + 1 = 0.',
      'x&sup2; + y&sup2; &minus; 3x &minus; 5y + 8 = 0',
      'Centre condition &minus;g + f + 1 = 0 &rarr; g = f + 1; the points give g + f = &minus;4, so f = &minus;5/2, '
      'g = &minus;3/2, c = 8. Matches the key.',
      255),
    q('u8_ex82_q7', 8, EX8_2, 'EX8.2', 7,
      'Find the equation of the circumcircle of the triangle with vertices (1, &minus;2), (&minus;5, 2) and '
      '(3, 4).',
      '11x&sup2; + 11y&sup2; + 16x &minus; 42y &minus; 155 = 0',
      'The three point equations give g = 8/11, f = &minus;21/11, c = &minus;155/11; multiplying by 11 clears '
      'fractions. Matches the key.',
      255),
    q('u8_ex82_q8', 8, EX8_2, 'EX8.2', 8,
      'Find the equation of the circle containing the points (1, &minus;2) and (3, &minus;4) and touching the '
      'x-axis.',
      'x&sup2; + y&sup2; + 10x + 20y + 25 = 0 and x&sup2; + y&sup2; &minus; 6x + 4y + 9 = 0',
      'Touching the x-axis &rarr; c = g&sup2;; the two points then give g&sup2; &minus; 2g &minus; 15 = 0, so '
      'g = 5 (f = 10, c = 25) or g = &minus;3 (f = 2, c = 9). Both match the key.',
      255),
    q('u8_ex82_q9', 8, EX8_2, 'EX8.2', 9,
      'Find the equation of the circle containing the point (6, 0) and touching the line x = y at (4, 4).',
      '3(x&sup2; + y&sup2;) &minus; 34x &minus; 14y + 96 = 0',
      'Centre on the normal x + y = 8 at (4, 4); (4, 4) on the circle gives c = 32; (6, 0) gives g = &minus;17/3, '
      'f = &minus;7/3. Matches the key.',
      255),
    q('u8_ex82_q10', 8, EX8_2, 'EX8.2', 10,
      'Show that the equation of a circle with centre (&minus;g, &minus;f) and (i) touching the x-axis is of the '
      'form x&sup2; + y&sup2; + 2gx + 2fy + g&sup2; = 0  (ii) touching the y-axis is of the form '
      'x&sup2; + y&sup2; + 2gx + 2fy + f&sup2; = 0',
      '(i) touching x-axis &rarr; r = |f| &rarr; g&sup2; + f&sup2; &minus; c = f&sup2; &rarr; c = g&sup2;, giving '
      'the stated form<br>(ii) touching y-axis &rarr; r = |g| &rarr; c = f&sup2;, giving the stated form. (Shown)',
      'The radius equals the modulus of the ordinate (resp. abscissa) of the centre when the circle touches the '
      'x-axis (resp. y-axis). Proof question, no key entry.',
      255),
    q('u8_ex82_q11', 8, EX8_2, 'EX8.2', 11,
      'Find the equation of the circle passing through the origin and having intercepts 6 and 8.',
      'x&sup2; + y&sup2; &minus; 6x &minus; 8y = 0',
      'c = 0; x-intercept 2&radic;(g&sup2; &minus; c) = 6 &rarr; |g| = 3; y-intercept 2&radic;(f&sup2; &minus; c) = 8 '
      '&rarr; |f| = 4; the key takes g = &minus;3, f = &minus;4 (other sign choices give the congruent circles '
      'x&sup2; + y&sup2; &plusmn; 6x &plusmn; 8y = 0). Matches the key.',
      255),
    q('u8_ex82_q12', 8, EX8_2, 'EX8.2', 12,
      'Find the equation of the circle which passes through the two points (b, 0) and (&minus;b, 0) and whose '
      'radius is a units.',
      'x&sup2; + y&sup2; &plusmn; 2&radic;(a&sup2; &minus; b&sup2;)&middot;y &minus; b&sup2; = 0 (exists when '
      'a &ge; b)',
      'The centre lies on the perpendicular bisector of the two points, the y-axis, so g = 0; (b, 0) gives '
      'c = &minus;b&sup2;; radius &radic;(f&sup2; + b&sup2;) = a gives f = &plusmn;&radic;(a&sup2; &minus; b&sup2;). '
      'No key entry.',
      255),
    q('u8_ex82_q13', 8, EX8_2, 'EX8.2', 13,
      'Find the equation of the circle which passes through the points (5, 0) and (0, &minus;5) and whose radius '
      'is 5 units.',
      'x&sup2; + y&sup2; = 25 or x&sup2; + y&sup2; &minus; 10x + 10y + 25 = 0',
      'The points give f = &minus;g and c = &minus;25 &minus; 10g; radius&sup2; = 2g&sup2; &minus; c = 25 leads to '
      '2g&sup2; + 10g = 0, so g = 0 (centre (0, 0)) or g = &minus;5 (centre (5, &minus;5)). No key entry.',
      255),
]

EX8_3 = 'Exercise 8.3'
SOLVED += [
    q('u8_ex83_q1', 8, EX8_3, 'EX8.3', 1,
      'Check whether the following lines are tangent, secant or neither to the circle x&sup2; + y&sup2; = 25: '
      '(i) y = x + 3  (ii) y = &radic;3x + 10  (iii) y = 2x + 15',
      '(i) secant<br>(ii) tangent<br>(iii) neither',
      'Compare the distance from the centre (0, 0) with r = 5: (i) 3/&radic;2 &asymp; 2.12 &lt; 5; '
      '(ii) 10/2 = 5; (iii) 15/&radic;5 = 3&radic;5 &asymp; 6.71 &gt; 5. All match the key.',
      265),
    q('u8_ex83_q2', 8, EX8_3, 'EX8.3', 2,
      'Find the condition of tangency and secancy of the line y = 2x + k with the circle '
      'x&sup2; + y&sup2; + 10x + 20y + c = 0.',
      'Tangent: k&sup2; = 625 &minus; 5c; secant: k&sup2; &lt; 625 &minus; 5c',
      'Centre (&minus;5, &minus;10), r = &radic;(125 &minus; c); d = |k|/&radic;5; set d = r (tangent) or '
      'd &lt; r (secant). Matches the key.',
      265),
    q('u8_ex83_q3', 8, EX8_3, 'EX8.3', 3,
      'Find the equation of the tangent to x&sup2; + y&sup2; = 36 with the slope &radic;3.',
      'y = &radic;3x &plusmn; 12',
      'y = mx &plusmn; r&radic;(1 + m&sup2;) with m = &radic;3, r = 6 gives &plusmn;6&radic;4 = &plusmn;12. '
      'Matches the key.',
      265),
    q('u8_ex83_q4', 8, EX8_3, 'EX8.3', 4,
      'Find the equation of tangent and normal: (i) at (1, &minus;4) to the circle x&sup2; + y&sup2; = 17  '
      '(ii) at (4, 1) to the circle x&sup2; + y&sup2; &minus; 4x + 2y = 3',
      '(i) tangent: x &minus; 4y = 17; normal: 4x + y = 0<br>(ii) tangent: x + y = 5; normal: x &minus; y = 3',
      'Tangent at (x&#8321;, y&#8321;) via xx&#8321; + yy&#8321; + g(x + x&#8321;) + f(y + y&#8321;) + c = 0; the normal '
      'is the line through the centre and the point of contact. Both match the key.',
      266),
    q('u8_ex83_q5', 8, EX8_3, 'EX8.3', 5,
      'Find the length of the tangent: (i) from (6, 1) to the circle x&sup2; + y&sup2; = 4  (ii) from (2, 5) to '
      'the circle x&sup2; + y&sup2; + 8x &minus; 5y = 7',
      '(i) &radic;33<br>(ii) &radic;13',
      'Length = &radic;S&#8321;: (i) &radic;(36 + 1 &minus; 4); (ii) &radic;(4 + 25 + 16 &minus; 25 &minus; 7). '
      'Both match the key.',
      266),
    q('u8_ex83_q6', 8, EX8_3, 'EX8.3', 6,
      'Find the condition that the line y = mx + c may be tangent to the circle (x &minus; h)&sup2; + '
      '(y &minus; k)&sup2; = r&sup2;.',
      '(mh &minus; k + c)&sup2; = r&sup2;(1 + m&sup2;)',
      'Distance from (h, k) to mx &minus; y + c = 0 equals r: |mh &minus; k + c|/&radic;(1 + m&sup2;) = r. '
      'Matches the key.',
      266),
    q('u8_ex83_q7', 8, EX8_3, 'EX8.3', 7,
      'Show that the circles x&sup2; + y&sup2; &minus; 6x &minus; 6y + 10 = 0 and x&sup2; + y&sup2; = 2 touch each '
      'other and find the point of contact.',
      'They touch externally; point of contact (1, 1)',
      'C&#8321; = (3, 3), r&#8321; = 2&radic;2; C&#8322; = (0, 0), r&#8322; = &radic;2; C&#8321;C&#8322; = 3&radic;2 = '
      'r&#8321; + r&#8322;. The contact point lies on C&#8322;C&#8321; at distance r&#8322; from C&#8322;. '
      'Matches the key.',
      266),
    q('u8_ex83_q8', 8, EX8_3, 'EX8.3', 8,
      'Find the equation(s) of the tangent(s) to the circle x&sup2; + y&sup2; = 25: (i) at the point whose '
      'abscissa is 3  (ii) at the point whose ordinate is &minus;4  (iii) parallel to 3x + 4y + 1 = 0  '
      '(iv) perpendicular to 3x + 4y + 1 = 0',
      '(i) 3x + 4y = 25 and 3x &minus; 4y = 25<br>(ii) 3x &minus; 4y = 25 and 3x + 4y + 25 = 0<br>'
      '(iii) 3x + 4y + 25 = 0 and 3x + 4y &minus; 25 = 0<br>(iv) 4x &minus; 3y + 25 = 0 and '
      '4x &minus; 3y &minus; 25 = 0',
      '(i) points (3, &plusmn;4); (ii) points (&plusmn;3, &minus;4); (iii) tangents 3x + 4y = &plusmn;25; '
      '(iv) slope 4/3 through distance 5 from the centre. All match the key.',
      266),
    q('u8_ex83_q9', 8, EX8_3, 'EX8.3', 9,
      'Find the equations of the tangents to x&sup2; + y&sup2; &minus; 6x &minus; 2y + 9 = 0 through the origin '
      'and their respective points of contact.',
      'Tangents: y = 0 and 3x &minus; 4y = 0; points of contact: (3, 0) and (12/5, 9/5)',
      'Centre (3, 1), r = 1; y = mx tangent when |3m &minus; 1|/&radic;(m&sup2; + 1) = 1 &rarr; 8m&sup2; '
      '&minus; 6m = 0. Contact points are the feet of perpendiculars from the centre. Matches the key.',
      266),
    q('u8_ex83_q10', 8, EX8_3, 'EX8.3', 10,
      'Show that the line ax + by + al + bm = 0 is normal to the circle x&sup2; + y&sup2; + 2lx + 2my + c = 0 for '
      'all values of a and b.',
      'The centre (&minus;l, &minus;m) satisfies a(&minus;l) + b(&minus;m) + al + bm = 0 identically, so the line '
      'always passes through the centre and is therefore a normal. (Shown)',
      'Every line through the centre of a circle is a normal to it. Proof question, no key entry.',
      266),
    q('u8_ex83_q11', 8, EX8_3, 'EX8.3', 11,
      'Find (i) the product of abscissae and (ii) the product of ordinates of the points where the line y = mx '
      'meets the circle x&sup2; + y&sup2; + 2gx + 2fy + c = 0.',
      '(i) c/(1 + m&sup2;)<br>(ii) cm&sup2;/(1 + m&sup2;)',
      'Substitute y = mx: (1 + m&sup2;)x&sup2; + 2(g + fm)x + c = 0, product of roots c/(1 + m&sup2;); '
      'substitute x = y/m for the ordinates. Both match the key.',
      266),
    q('u8_ex83_q12', 8, EX8_3, 'EX8.3', 12,
      'Prove that the line y = x + k&radic;2 touches the circle x&sup2; + y&sup2; = k&sup2; and find its point of '
      'contact.',
      'Distance from (0, 0) to x &minus; y + k&radic;2 = 0 is |k&radic;2|/&radic;2 = |k| = radius, so it touches; '
      'point of contact (&minus;k&radic;2/2, k&radic;2/2)',
      'The contact point is the foot of the perpendicular from the centre onto the line. Matches the key.',
      266),
    q('u8_ex83_q13', 8, EX8_3, 'EX8.3', 13,
      'Find the condition that the line 3x + 4y = c may touch the circle x&sup2; + y&sup2; = 8x.',
      'c = 32 or c = &minus;8',
      'Centre (4, 0), r = 4; |12 &minus; c|/5 = 4 &rarr; |12 &minus; c| = 20. Matches the key.',
      266),
    q('u8_ex83_q14', 8, EX8_3, 'EX8.3', 14,
      'Find whether the line x + y = 2 + &radic;2 touches the circle x&sup2; + y&sup2; &minus; 2x &minus; 2y '
      '&minus; 1 = 0.',
      'No &mdash; the given line is not a tangent (d = 1 &lt; &radic;3 = r, so it is a secant)',
      'Centre (1, 1), r = &radic;3; d = |1 + 1 &minus; 2 &minus; &radic;2|/&radic;2 = 1 &ne; &radic;3. '
      'Matches the key.',
      266),
    q('u8_ex83_q15', 8, EX8_3, 'EX8.3', 15,
      'Prove that the two circles x&sup2; + y&sup2; + 2gx + c = 0 and x&sup2; + y&sup2; + 2fy + c = 0 touch each '
      'other if 1/f&sup2; + 1/g&sup2; = 1/c.',
      'C&#8321; = (&minus;g, 0), r&#8321; = &radic;(g&sup2; &minus; c); C&#8322; = (0, &minus;f), r&#8322; = '
      '&radic;(f&sup2; &minus; c). Touching: g&sup2; + f&sup2; = (g&sup2; &minus; c) + (f&sup2; &minus; c) '
      '&plusmn; 2&radic;((g&sup2; &minus; c)(f&sup2; &minus; c)) &rarr; (g&sup2; &minus; c)(f&sup2; &minus; c) = '
      'c&sup2; &rarr; g&sup2;f&sup2; = c(g&sup2; + f&sup2;) &rarr; 1/f&sup2; + 1/g&sup2; = 1/c. (Proved)',
      'Squaring removes the &plusmn; so the same condition covers internal and external contact. '
      'Proof question, no key entry.',
      266),
]

EX8_4 = 'Exercise 8.4'
SOLVED += [
    q('u8_ex84_q1', 8, EX8_4, 'EX8.4', 1,
      'Prove analytically: the tangents drawn at the ends of a diameter of a circle are parallel.',
      'For x&sup2; + y&sup2; = r&sup2; with diameter ends P(r cos &theta;, r sin &theta;) and Q(&minus;r cos '
      '&theta;, &minus;r sin &theta;): tangent at P is x cos &theta; + y sin &theta; = r and at Q is '
      'x cos &theta; + y sin &theta; = &minus;r &mdash; same normal direction, different constants, hence '
      'distinct parallel lines. (Proved)',
      'Equal normal direction with unequal constants is exactly the condition for parallel distinct lines. '
      'Proof question, no key entry.',
      276),
    q('u8_ex84_q2', 8, EX8_4, 'EX8.4', 2,
      'Prove analytically: a normal to a circle passes through the centre of the circle.',
      'The normal at (x&#8321;, y&#8321;) to x&sup2; + y&sup2; + 2gx + 2fy + c = 0 is (x &minus; x&#8321;)'
      '(y&#8321; + f) &minus; (y &minus; y&#8321;)(x&#8321; + g) = 0; substituting the centre (&minus;g, &minus;f) '
      'gives &minus;(x&#8321; + g)(y&#8321; + f) + (y&#8321; + f)(x&#8321; + g) = 0, so the centre lies on every '
      'normal. (Proved)',
      'The normal is the line through the point of contact perpendicular to the tangent there. '
      'Proof question, no key entry.',
      276),
    q('u8_ex84_q3', 8, EX8_4, 'EX8.4', 3,
      'Prove analytically: the midpoint of the hypotenuse of a right triangle is the centre of the circle '
      'circumscribing the triangle.',
      'With the right angle at the origin and legs on the axes, A(a, 0), B(0, b); midpoint M(a/2, b/2) satisfies '
      'MA = MB = MC = &radic;(a&sup2;/4 + b&sup2;/4), so M is equidistant from all three vertices and is the '
      'circumcentre. (Proved)',
      'Equidistance from the three vertices is the defining property of the circumcentre. '
      'Proof question, no key entry.',
      276),
    q('u8_ex84_q4', 8, EX8_4, 'EX8.4', 4,
      'Prove analytically: the measure of the central angle of a major arc is double the measure of the '
      'inscribed angle of the corresponding minor arc.',
      'On x&sup2; + y&sup2; = r&sup2; take minor arc AB of central measure &theta; = |b &minus; a| and Q on that '
      'minor arc. Sum-to-product gives A &minus; Q &prop; (&minus;sin s, cos s), B &minus; Q &prop; '
      '(&minus;sin t, cos t) with s = (a+q)/2, t = (b+q)/2 and opposite proportionality signs, so '
      '&ang;AQB = &pi; &minus; |t &minus; s| = &pi; &minus; &theta;/2, while the central angle of the major arc is '
      '2&pi; &minus; &theta; = 2&ang;AQB. (Proved)',
      'The inscribed-angle theorem in coordinate form: an angle at the circumference is half the central angle '
      'standing on the same arc. Proof question, no key entry.',
      276),
    q('u8_ex84_q5', 8, EX8_4, 'EX8.4', 5,
      'Prove analytically: the parallelogram circumscribing a circle is a rhombus.',
      'Every side is tangent, so the distance from the centre to each side is r; opposite sides are parallel at '
      'distance 2r. Area = AB&middot;2r = BC&middot;2r &rarr; AB = BC, and a parallelogram with equal adjacent '
      'sides is a rhombus. (Proved)',
      'Computing the same area against the two pairs of parallel sides forces the adjacent sides equal. '
      'Proof question, no key entry.',
      276),
]

REV8 = 'Review Exercise 8'
SOLVED += [
    q('u8_rev8_q1', 8, REV8, 'REV8', 1,
      'Tick the correct option: (i) If a plane cuts one nappe of a right circular cone perpendicularly the conic '
      'is  (a) parabola  (b) circle  (c) ellipse  (d) hyperbola.  (ii) The centre of (x + 3)&sup2; + '
      '(y &minus; 5)&sup2; = 36 is  (a) (3, &minus;5)  (b) (&minus;3, &minus;5)  (c) (&minus;3, 5)  (d) (3, 5).  '
      '(iii) The centre of x&sup2; + y&sup2; + 10x &minus; 8y + 1 = 0 is  (a) (&minus;5, 8)  (b) (&minus;10, 8)  '
      '(c) (5, &minus;4)  (d) (&minus;5, 4).  (iv) The radius of x&sup2; + y&sup2; + 4x + 6y + 1 = 0 is  '
      '(a) &radic;13  (b) &radic;12  (c) &radic;10  (d) &radic;71.  (v) Which is a degenerate conic  (a) circle  '
      '(b) ellipse  (c) line  (d) parabola.  (vi) The circle with centre at origin and diameter 10 units is  '
      '(a) x&sup2; + y&sup2; = 100  (b) x&sup2; + y&sup2; + 100 = 0  (c) x&sup2; + y&sup2; = 50  '
      '(d) x&sup2; + y&sup2; = 25.  (vii) For what k is the radius of x&sup2; + y&sup2; + 6x &minus; 4y + k = 0 '
      'equal to 5  (a) 11  (b) &minus;12  (c) 10  (d) 12.  (viii) The centre of x&sup2; + y&sup2; + 6x + 8 = 0 is '
      ' (a) on x-axis  (b) on y-axis  (c) in 1st quadrant  (d) at origin.  (ix) The circle x&sup2; + y&sup2; + '
      '6x + 10y + 9 = 0  (a) touches x-axis  (b) touches y-axis  (c) passes through origin  (d) cuts x-axis.  '
      '(x) The circle x&sup2; + y&sup2; + 20x &minus; 8y + 16 = 0  (a) touches x-axis  (b) touches y-axis  '
      '(c) passes through origin  (d) cuts y-axis.  (xi) y = 2x + c is tangent to x&sup2; + y&sup2; = 25 if  '
      '(a) c&sup2; = 25  (b) c&sup2; = 625  (c) c&sup2; = 50  (d) c&sup2; = 125.  (xii) For what k is y = 2x + 3 '
      'tangent to x&sup2; + y&sup2; = k&sup2;  (a) &plusmn;5/&radic;3  (b) &plusmn;3/&radic;5  '
      '(c) &plusmn;&radic;(3/5)  (d) &plusmn;&radic;5/3.  (xiii) For what k is 2x + 3y + k = 0 normal to '
      'x&sup2; + y&sup2; + 2x + 9 = 0  (a) &minus;2  (b) 2  (c) 3  (d) &minus;3.  (xiv) The tangent to '
      'x&sup2; + y&sup2; = 25 at (3, 4) is  (a) 3x + 4y = 0  (b) 4x + 3y = 25  (c) 3x + 4y = 25  (d) 3x + 4y = 5.  '
      '(xv) The normal to x&sup2; + y&sup2; = 36 at (2, 4&radic;2) is  (a) 2x + 4&radic;2y = 0  (b) 4&radic;2x + '
      '2y = 0  (c) 2x &minus; 4&radic;2y = 0  (d) 4&radic;2x &minus; 2y = 0.  (xvi) The tangent to x&sup2; + '
      'y&sup2; = 100 with slope &radic;15 is  (a) y = &radic;15x &plusmn; 40  (b) y = &minus;&radic;15x &plusmn; 40  '
      '(c) y = &radic;15x &plusmn; 40y  (d) y = &minus;&radic;15x &plusmn; 40y.  (xvii) The length of the tangent '
      'to x&sup2; + y&sup2; + 2y &minus; 1 = 0 from (5, 2) is  (a) &radic;24  (b) &radic;33  (c) &radic;32  '
      '(d) &radic;31 units.  (xviii) Congruent chords of a circle are equidistant from its  (a) diameter  '
      '(b) centre  (c) arc  (d) segment.  (xix) Angle in a semi-circle is  (a) acute  (b) obtuse  (c) right  '
      '(d) straight angle.  (xx) The point (3, 3) is ______ the circle x&sup2; + y&sup2; = 64  (a) outside  '
      '(b) inside  (c) on  (d) cannot be determined',
      '(i) (b)<br>(ii) (c)<br>(iii) (d)<br>(iv) (b)<br>(v) (c)<br>(vi) (d)<br>(vii) (b)<br>(viii) (a)<br>'
      '(ix) (a)<br>(x) (b)<br>(xi) (d)<br>(xii) (b)<br>(xiii) (b)<br>(xiv) (c)<br>(xv) (d)<br>(xvi) (a)<br>'
      '(xvii) (c)<br>(xviii) (b)<br>(xix) (c)<br>(xx) (b)',
      '(iv) &radic;(4 + 9 &minus; 1) = &radic;12. (vii) 13 &minus; k = 25. (ix) r = 5 = |y-coordinate of centre|. '
      '(x) r = 10 = |x-coordinate of centre|. (xi) c&sup2; = r&sup2;(1 + m&sup2;) = 125. (xii) |k| = 3/&radic;5. '
      '(xvii) &radic;S&#8321; = &radic;32. (xx) 18 &lt; 64. All match the key.',
      276),
    q('u8_rev8_q2', 8, REV8, 'REV8', 2,
      'Find the equation of the circle passing through (2, 3), (4, 6) and having (i) centre on the x-axis  '
      '(ii) centre on the y-axis.',
      '(i) 2x&sup2; + 2y&sup2; &minus; 39x + 52 = 0<br>(ii) x&sup2; + y&sup2; &minus; 13y + 26 = 0',
      '(i) f = 0 gives 13 + 4g + c = 0 and 52 + 8g + c = 0 &rarr; g = &minus;39/4, c = 26 (doubled to clear '
      'fractions). (ii) g = 0 gives f = &minus;13/2, c = 26. Both match the key.',
      277),
    q('u8_rev8_q3', 8, REV8, 'REV8', 3,
      'y = &radic;3x + 10 is the equation of a tangent to the circle with centre at the origin. Find the equation '
      'of the normal to the circle at the point of tangency.',
      'x + &radic;3y = 0',
      'Radius = distance from the origin to the line = 10/2 = 5, so the circle is x&sup2; + y&sup2; = 25; the '
      'point of contact is the foot of the perpendicular (&minus;5&radic;3/2, 5/2); the normal joins it to the '
      'centre, slope &minus;1/&radic;3. Matches the key.',
      277),
    q('u8_rev8_q4', 8, REV8, 'REV8', 4,
      'Find the condition of tangency, secancy and normality of the line x + y + k = 0 to the circle '
      'x&sup2; + y&sup2; + 2x &minus; 3 = 0.',
      'Tangent: k = 1 &plusmn; 2&radic;2<br>Secant: k&sup2; &minus; 2k &minus; 7 &lt; 0<br>Normal: k = 1',
      'Centre (&minus;1, 0), r = 2, d = |k &minus; 1|/&radic;2. Tangent: (k &minus; 1)&sup2; = 8; secant: '
      '(k &minus; 1)&sup2; &lt; 8; normal: the line passes through the centre. Flag: the key prints the secant '
      'condition as k&sup2; &minus; 2k &minus; 7 = 0 (the boundary equation); the secant region is the strict '
      'inequality.',
      277),
]

EX9_1 = 'Exercise 9.1'
SOLVED += [
    q('u9_ex91_q1', 9, EX9_1, 'EX9.1', 1,
      'Draw the following parabolas: (i) y&sup2; = 10x  (ii) x&sup2; = &minus;12y  (iii) y&sup2; &minus; x '
      '&minus; 2y &minus; 1 = 0  (iv) x&sup2; &minus; 6x &minus; 2y + 5 = 0',
      '(i) opens right, vertex (0, 0), focus (5/2, 0)<br>(ii) opens down, vertex (0, 0), focus (0, &minus;3)<br>'
      '(iii) (y &minus; 1)&sup2; = x + 2: opens right, vertex (&minus;2, 1), focus (&minus;7/4, 1)<br>'
      '(iv) (x &minus; 3)&sup2; = 2(y + 2): opens up, vertex (3, &minus;2), focus (3, &minus;3/2)',
      'Complete the square to put each equation in a shifted standard form, then sketch the usual parabola '
      'shape at that vertex opening in that direction. Sketch task, no key entry.',
      289),
    q('u9_ex91_q2', 9, EX9_1, 'EX9.1', 2,
      'Determine the vertex, focus, latus rectum and equation of the directrix of the following, and find the '
      'equation of the axis of symmetry: (i) y&sup2; = &minus;8x  (ii) x&sup2; = &minus;16y  (iii) (y + 3)&sup2; '
      '= 12(x &minus; 2)  (iv) (x + 5)&sup2; = 8(y &minus; 3)  (v) x&sup2; + 4x &minus; y + 5 = 0  '
      '(vi) y&sup2; &minus; 6y + 8x &minus; 23 = 0',
      '(i) vertex (0, 0); focus (&minus;2, 0); LR 8; directrix x &minus; 2 = 0; axis y = 0<br>'
      '(ii) vertex (0, 0); focus (0, &minus;4); LR 16; directrix y &minus; 4 = 0; axis x = 0<br>'
      '(iii) vertex (2, &minus;3); focus (5, &minus;3); LR 12; directrix x + 1 = 0; axis y + 3 = 0<br>'
      '(iv) vertex (&minus;5, 3); focus (&minus;5, 5); LR 8; directrix y &minus; 1 = 0; axis x + 5 = 0<br>'
      '(v) vertex (&minus;2, 1); focus (&minus;2, 5/4); LR 1; directrix 4y &minus; 3 = 0; axis x + 2 = 0<br>'
      '(vi) vertex (4, 3); focus (2, 3); LR 8; directrix x &minus; 6 = 0; axis y &minus; 3 = 0',
      'Read 4a from the standard (or completed-square) form; the focus lies a units from the vertex along the '
      'axis, the directrix a units behind it. (v) is (x + 2)&sup2; = y &minus; 1 and (vi) is (y &minus; 3)&sup2; '
      '= &minus;8(x &minus; 4). All match the key.',
      289),
    q('u9_ex91_q3', 9, EX9_1, 'EX9.1', 3,
      'Find the equation of the parabola whose focus is F(1, &minus;2) and directrix is 3x &minus; 5 = 0.',
      '9y&sup2; + 12x + 36y + 20 = 0',
      'Locus condition (x &minus; 1)&sup2; + (y + 2)&sup2; = (x &minus; 5/3)&sup2; simplifies to '
      '(y + 2)&sup2; = &minus;(4/3)(x &minus; 4/3). Matches the key.',
      289),
    q('u9_ex91_q4', 9, EX9_1, 'EX9.1', 4,
      'Find the equation of the parabola whose focus is (3, 4) and the directrix is the line x + y &minus; 1 = 0.',
      'x&sup2; + y&sup2; &minus; 2xy &minus; 10x &minus; 14y + 49 = 0',
      '2[(x &minus; 3)&sup2; + (y &minus; 4)&sup2;] = (x + y &minus; 1)&sup2; since the distance to the oblique '
      'directrix carries a factor 1/&radic;2. Matches the key.',
      289),
    q('u9_ex91_q5', 9, EX9_1, 'EX9.1', 5,
      'Find the equation of the parabolas whose focus and vertex are as under: (i) vertex (0, 0), focus (5, 0)  '
      '(ii) vertex (0, 0), focus (0, &minus;2)  (iii) vertex (1, &minus;3), focus (1, 2)  (iv) vertex (2, 4), '
      'focus (3, 4)',
      '(i) y&sup2; = 20x<br>(ii) x&sup2; = &minus;8y<br>(iii) (x &minus; 1)&sup2; = 20(y + 3)<br>'
      '(iv) (y &minus; 4)&sup2; = 4(x &minus; 2)',
      'a = distance vertex-to-focus; the opening direction follows from focus minus vertex. Matches the key '
      '(the key\u2019s (ii) \u201cx&sup2; = &minus;8x\u201d is a misprint for x&sup2; = &minus;8y).',
      289),
    q('u9_ex91_q6', 9, EX9_1, 'EX9.1', 6,
      'Find the equation of the parabola whose focus and directrix are given: (i) focus (3, 0), directrix '
      'x &minus; 5 = 0  (ii) focus (0, 4), directrix y + 6 = 0  (iii) focus (&minus;4, 3), directrix y = 6',
      '(i) y&sup2; + 4x &minus; 16 = 0<br>(ii) x&sup2; &minus; 20y &minus; 20 = 0<br>'
      '(iii) x&sup2; + 8x + 6y &minus; 11 = 0',
      'The vertex is the midpoint of focus and foot of directrix on the axis; a = half the focus-directrix '
      'distance; opening is away from the directrix. All match the key.',
      290),
    q('u9_ex91_q7', 9, EX9_1, 'EX9.1', 7,
      'Find the equation of the parabola whose vertex and directrix are as under: (i) vertex (0, 0), directrix '
      'x = &minus;6  (ii) vertex (0, 0), directrix y = 5  (iii) vertex (3, 4), directrix x = 5',
      '(i) y&sup2; = 24x<br>(ii) x&sup2; = &minus;20y<br>(iii) (y &minus; 4)&sup2; = &minus;8(x &minus; 3)',
      'a = distance from vertex to directrix; the parabola opens away from the directrix. All match the key.',
      290),
    q('u9_ex91_q8', 9, EX9_1, 'EX9.1', 8,
      'Find the equation of the parabola whose vertex and point are given: (i) vertex (0, 0), point (3, 4)  '
      '(ii) vertex (5, 0), point (4, 6)',
      '(i) 3y&sup2; = 16x or 4x&sup2; = 9y<br>(ii) y&sup2; = &minus;36(x &minus; 5) or 6(x &minus; 5)&sup2; = y',
      'Two orientations fit each point: substitute into y&sup2; = 4ax and into x&sup2; = 4by (shifted forms in '
      '(ii)) and solve for the parameter. Both match the key.',
      290),
    q('u9_ex91_q9', 9, EX9_1, 'EX9.1', 9,
      'Find the standard equation of the parabola whose latus rectum and vertex are the diameter and centre of '
      'the circle x&sup2; + y&sup2; &minus; 4x &minus; 8y &minus; 5 = 0 respectively.',
      '(x &minus; 2)&sup2; = 10(y &minus; 4) or (y &minus; 4)&sup2; = 10(x &minus; 2)',
      'Circle centre (2, 4), radius &radic;25 = 5, so diameter 10 = latus rectum (4a = 10) and the vertex is '
      '(2, 4); either axis orientation is admitted. Matches the key.',
      290),
    q('u9_ex91_q10', 9, EX9_1, 'EX9.1', 10,
      'Find the equation of the circle whose centre is at the focus and whose diameter is the latus rectum of '
      'the parabola x&sup2; = 12y.',
      'x&sup2; + y&sup2; &minus; 6y &minus; 27 = 0',
      '4a = 12 gives focus (0, 3) and latus rectum 12, so radius 6: x&sup2; + (y &minus; 3)&sup2; = 36. Matches '
      'the key (the key\u2019s \u201c&minus; 6y&sup2;\u201d is a misprint for &minus; 6y).',
      290),
    q('u9_ex91_q11', 9, EX9_1, 'EX9.1', 11,
      'For what point of the parabola y&sup2; = 10x is the abscissa equal to three times its ordinate?',
      '(0, 0) and (90, 30)',
      'x = 3y substituted gives y&sup2; = 30y, so y = 0 or 30. Matches the key.',
      290),
]

EX9_2 = 'Exercise 9.2'
SOLVED += [
    q('u9_ex92_q1', 9, EX9_2, 'EX9.2', 1,
      'Find the condition when the line y = mx + c is tangent to the parabola x&sup2; = 4ay. Also find the point '
      'of contact and the equation of the tangent.',
      'Condition: c = &minus;am&sup2;; point of contact (2am, am&sup2;); tangent y = mx &minus; am&sup2;',
      'Substituting gives x&sup2; &minus; 4amx &minus; 4ac = 0; equal roots require 16a&sup2;m&sup2; + 16ac = 0. '
      'Matches the key.',
      298),
    q('u9_ex92_q2', 9, EX9_2, 'EX9.2', 2,
      'Find the condition of tangency and the point of tangency for the following lines and parabolas, and the '
      'equation of the tangent in each case: (i) 2x + y = c with y&sup2; = 10x  (ii) 3x + 4y = p with '
      'x&sup2; = 12y  (iii) y = cx with y&sup2; = 8(x &minus; 1)',
      '(i) c = &minus;5/4; contact (5/8, &minus;5/2); tangent y = &minus;2x &minus; 5/4<br>'
      '(ii) p = &minus;27/4; contact (&minus;9/2, 27/16); tangent y = &minus;(3/4)x &minus; 27/16<br>'
      '(iii) c = &plusmn;&radic;2; contact (2, &plusmn;2&radic;2); tangent y = &plusmn;&radic;2&middot;x',
      '(i) c = a/m with a = 5/2, m = &minus;2. (ii) p/4 = &minus;am&sup2; with a = 3, m = &minus;3/4. '
      '(iii) c&sup2;x&sup2; &minus; 8x + 8 = 0 has equal roots when 64 &minus; 32c&sup2; = 0. Flag: the key '
      'misprints (iii)\u2019s contact as (2, &plusmn;&radic;2) and its tangents as 4x &plusmn; &radic;2y &minus; 6 '
      '= 0; those lines miss both the origin and the contact point.',
      298),
    q('u9_ex92_q3', 9, EX9_2, 'EX9.2', 3,
      'Find the equation of tangent and normal to the following parabolas at the given points: (i) y&sup2; = 8x '
      'at (2, 4)  (ii) x&sup2; = 4y at (&minus;6, 9)  (iii) (y &minus; 1)&sup2; = 9(x &minus; 2) at (3, 4)',
      '(i) tangent x &minus; y + 2 = 0; normal x + y &minus; 6 = 0<br>(ii) tangent 3x + y + 9 = 0; normal '
      'x &minus; 3y + 33 = 0<br>(iii) tangent 3x &minus; 2y &minus; 1 = 0; normal 2x + 3y &minus; 18 = 0',
      'Tangent by yy&#8321; = 4a(x + x&#8321;) (or the shifted form); normal perpendicular at the same point. '
      'All match the key.',
      298),
    q('u9_ex92_q4', 9, EX9_2, 'EX9.2', 4,
      'Find the equation of tangent and normal at P(x&#8321;, y&#8321;) to the parabola x&sup2; = 4ay.',
      'Tangent: y &minus; y&#8321; = (x&#8321;/(2a))(x &minus; x&#8321;); normal: y &minus; y&#8321; = '
      '(2a/x&#8321;)(x&#8321; &minus; x)',
      'Differentiating x&sup2; = 4ay gives slope x/(2a) at P; the normal slope is its negative reciprocal. '
      'Matches the key.',
      298),
    q('u9_ex92_q5', 9, EX9_2, 'EX9.2', 5,
      'A light house uses a parabolic reflector that is 1 m in diameter. How deep should the reflector be if the '
      'light source is placed halfway between the vertex and the plane of the rim to produce a parallel beam of '
      'light along the axis of the parabola?',
      'Depth = 1/(2&radic;2) m (&asymp; 0.354 m)',
      'The source must be at the focus a, and a = d/2 with depth d; the rim point (1/2, d) gives 1/4 = 4a&middot;d '
      '= 2d&sup2;. Matches the key.',
      298),
    q('u9_ex92_q6', 9, EX9_2, 'EX9.2', 6,
      'A parabolic reflector of 12 cm in diameter is used in a vehicle and is 8 cm deep. Where should the light '
      'source be placed to produce a parallel beam of light?',
      'At the focus, 9/8 cm (1.125 cm) from the vertex on the axis',
      'Rim point (6, 8): 36 = 4a&middot;8 &rarr; a = 9/8; a parallel beam needs the source at the focus. Matches '
      'the key (the key\u2019s unit \u201cm\u201d is a misprint for cm).',
      298),
    q('u9_ex92_q7', 9, EX9_2, 'EX9.2', 7,
      'The main cable of a suspension bridge hangs as a parabola between two towers 100 m apart and 30 m high '
      'from the roadway. The cable is 5 m above the roadway at the centre. Find the equation of the parabola and '
      'the distance from the centre of a 10 m high suspended cable.',
      'x&sup2; = 100(y &minus; 5); distance 10&radic;5 m',
      'Vertex (0, 5); tower top (50, 30) gives 4a = 100; at y = 10, x&sup2; = 500. Matches the key.',
      298),
    q('u9_ex92_q8', 9, EX9_2, 'EX9.2', 8,
      'The main cable of a suspension bridge is a parabola; the towers are 600 feet apart and 60 feet high from '
      'the roadway, and the cable touches the roadway midway between the towers. What is the height of the '
      'suspender cable 150 feet from the centre of the bridge?',
      '15 feet',
      'Vertex (0, 0); (300, 60) gives 4a = 1500; at x = 150, y = 22500/1500 = 15. Matches the key.',
      298),
]

EX9_3 = 'Exercise 9.3'
SOLVED += [
    q('u9_ex93_q1', 9, EX9_3, 'EX9.3', 1,
      'Find the semi-axes, eccentricity, foci, vertices, covertices, latus rectum and equations of the '
      'directrices of the following ellipses, and draw their graphs: (i) x&sup2;/9 + y&sup2;/25 = 1  '
      '(ii) x&sup2;/16 + y&sup2;/10 = 1  (iii) (x &minus; 3)&sup2;/25 + (y + 4)&sup2;/16 = 1  '
      '(iv) (x + 1)&sup2;/9 + (y &minus; 2)&sup2;/16 = 1  (v) 9x&sup2; + 25y&sup2; = 225  '
      '(vi) 4x&sup2; &minus; 16x + 25y&sup2; + 200y &minus; 316 = 0',
      '(i) a = 5, b = 3, e = 4/5; foci (0, &plusmn;4); vertices (0, &plusmn;5); covertices (&plusmn;3, 0); '
      'LR 18/5; directrices y = &plusmn;25/4<br>'
      '(ii) a = 4, b = &radic;10, e = &radic;6/4; foci (&plusmn;&radic;6, 0); vertices (&plusmn;4, 0); covertices '
      '(0, &plusmn;&radic;10); LR 5; directrices x = &plusmn;16/&radic;6<br>'
      '(iii) a = 5, b = 4, e = 3/5; foci (6, &minus;4), (0, &minus;4); vertices (8, &minus;4), (&minus;2, '
      '&minus;4); covertices (3, 0), (3, &minus;8); LR 32/5; directrices 3x &minus; 34 = 0, 3x + 16 = 0<br>'
      '(iv) a = 4, b = 3, e = &radic;7/4; foci (&minus;1, 2 &plusmn; &radic;7); vertices (&minus;1, 6), '
      '(&minus;1, &minus;2); covertices (2, 2), (&minus;4, 2); LR 9/2; directrices y &minus; 2 = '
      '&plusmn;16/&radic;7<br>'
      '(v) a = 5, b = 3, e = 4/5; foci (&plusmn;4, 0); vertices (&plusmn;5, 0); covertices (0, &plusmn;3); '
      'LR 18/5; directrices x = &plusmn;25/4<br>'
      '(vi) a = 5, b = 2, e = &radic;21/5; foci (2 &plusmn; &radic;21, &minus;4); vertices (&minus;3, &minus;4), '
      '(7, &minus;4); covertices (2, &minus;6), (2, &minus;2); LR 8/5; directrices x &minus; 2 = '
      '&plusmn;25/&radic;21',
      'c&sup2; = a&sup2; &minus; b&sup2; with a the semi-major axis; LR = 2b&sup2;/a; directrices &plusmn;a/e '
      'along the major axis. Flag: in (vi) the printed constant &minus;316 is a book misprint (it would give '
      '4(x &minus; 2)&sup2; + 25(y + 4)&sup2; = 732); with +316 the ellipse is (x &minus; 2)&sup2;/25 + '
      '(y + 4)&sup2;/4 = 1 and all key entries follow. All match the key.',
      315),
    q('u9_ex93_q2', 9, EX9_3, 'EX9.3', 2,
      'Find the equations of ellipses centred at the origin with axes along the coordinate axes satisfying: '
      '(i) major and minor axes 12 and 8, minor axis along y-axis  (ii) major axis along y-axis, passing through '
      '(1, &radic;(3/2)) and (2/&radic;3, 1)  (iii) foci (&plusmn;3, 0), vertices (&plusmn;5, 0)  (iv) foci '
      '(0, &plusmn;4) and latus rectum 18/5  (v) foci (&plusmn;5, 0) and minor axis 12 along y-axis  '
      '(vi) minor axis along x-axis of length 8 and latus rectum 6 along y-axis  (vii) covertices (0, &plusmn;3) '
      'and distance between foci 10  (viii) directrix y = 25/3 and latus rectum 32/5',
      '(i) x&sup2;/36 + y&sup2;/16 = 1<br>(ii) x&sup2;/2 + y&sup2;/3 = 1<br>(iii) x&sup2;/25 + y&sup2;/16 = 1<br>'
      '(iv) x&sup2;/9 + y&sup2;/25 = 1<br>(v) x&sup2;/61 + y&sup2;/36 = 1<br>(vi) 9x&sup2;/256 + y&sup2;/16 = 1<br>'
      '(vii) x&sup2;/34 + y&sup2;/9 = 1<br>(viii) x&sup2;/16 + y&sup2;/25 = 1',
      '(ii) solve 1/b&sup2; + (3/2)/a&sup2; = 1 with (4/3)/b&sup2; + 1/a&sup2; = 1 &rarr; b&sup2; = 2, '
      'a&sup2; = 3. (iv) 2b&sup2;/a = 18/5 with a&sup2; &minus; b&sup2; = 16 &rarr; a = 5. (vi) 2b&sup2;/a = 6 '
      'with b = 4 &rarr; a = 16/3. (viii) a/e = 25/3 with 2b&sup2;/a = 32/5 &rarr; a = 5, e = 3/5. '
      'All match the key.',
      315),
    q('u9_ex93_q3', 9, EX9_3, 'EX9.3', 3,
      'Find the equation of the auxiliary circle to 5x&sup2; + 7y&sup2; = 11.',
      'x&sup2; + y&sup2; = 11/5',
      'The auxiliary circle has the major axis as diameter; here a&sup2; = 11/5. Matches the key.',
      316),
    q('u9_ex93_q4', 9, EX9_3, 'EX9.3', 4,
      'Is the point (4, 5) inside, on, or outside the ellipse 2x&sup2; + 3y&sup2; = 6?',
      'Outside',
      '2&middot;16 + 3&middot;25 = 107 &gt; 6. Matches the key.',
      316),
    q('u9_ex93_q5', 9, EX9_3, 'EX9.3', 5,
      'Find the equation of the ellipse with centre at (5, &minus;3), one vertex at (10, &minus;3) and one focus '
      'at (9, &minus;3).',
      '(x &minus; 5)&sup2;/25 + (y + 3)&sup2;/9 = 1',
      'Horizontal major axis with a = 5, c = 4, so b&sup2; = 9. Matches the key.',
      316),
    q('u9_ex93_q6', 9, EX9_3, 'EX9.3', 6,
      'For the ellipse 9x&sup2; + 13y&sup2; = 117 find: (i) the distance between foci  (ii) the distance between '
      'vertices  (iii) the distance between covertices.',
      '(i) 4<br>(ii) 2&radic;13<br>(iii) 6',
      'x&sup2;/13 + y&sup2;/9 = 1 gives a = &radic;13, b = 3, c = 2. All match the key.',
      316),
    q('u9_ex93_q7', 9, EX9_3, 'EX9.3', 7,
      'Find the eccentricity of an ellipse if: (i) its axes are 32 and 24  (ii) its latus rectum is equal to half '
      'of its major axis.',
      '(i) e = &radic;7/4<br>(ii) e = 1/&radic;2',
      '(i) a = 16, b = 12, c = 4&radic;7. (ii) 2b&sup2;/a = a &rarr; c&sup2; = a&sup2;/2. Both match the key.',
      316),
    q('u9_ex93_q8', 9, EX9_3, 'EX9.3', 8,
      'Find the equation of the circle passing through the focus of the parabola y&sup2; + 8x = 0 and the foci of '
      'the ellipse 25x&sup2; + 16y&sup2; = 400.',
      '2x&sup2; + 2y&sup2; &minus; 5x &minus; 18 = 0',
      'The three points are (&minus;2, 0) and (0, &plusmn;3); symmetry puts the centre at (5/4, 0) with '
      'r&sup2; = 169/16. Matches the key.',
      316),
    q('u9_ex93_q9', 9, EX9_3, 'EX9.3', 9,
      'Find the length of, and the equations of, the focal radii drawn to the point (4&radic;3, 5) of the ellipse '
      '25x&sup2; + 16y&sup2; = 1600.',
      'Lengths 7 and 13; lines x + 4&radic;3y &minus; 24&radic;3 = 0 and 11x &minus; 4&radic;3y &minus; '
      '24&radic;3 = 0',
      'x&sup2;/64 + y&sup2;/100 = 1 has a = 10, e = 3/5, foci (0, &plusmn;6); focal radii a &plusmn; e&middot;y'
      '&#8321; = 10 &plusmn; 3; the lines join each focus to the point. Matches the key.',
      316),
    q('u9_ex93_q10', 9, EX9_3, 'EX9.3', 10,
      'Find the equation of the ellipse with centre at (0, 1) and major axis parallel to the y-axis, passing '
      'through (2, 1) and (0, 4).',
      'x&sup2;/4 + (y &minus; 1)&sup2;/9 = 1',
      'x&sup2;/b&sup2; + (y &minus; 1)&sup2;/a&sup2; = 1 with (2, 1) giving b&sup2; = 4 and (0, 4) giving '
      'a&sup2; = 9. Matches the key.',
      316),
]

EX9_4 = 'Exercise 9.4'
SOLVED += [
    q('u9_ex94_q1', 9, EX9_4, 'EX9.4', 1,
      'Find the values of c for which the line y = &radic;5&#8202;x + c is a tangent to the ellipse '
      '4x&sup2; + 9y&sup2; = 36.',
      'c = &plusmn;7',
      'Divide by 36: x&sup2;/9 + y&sup2;/4 = 1, so a&sup2; = 9, b&sup2; = 4, m = &radic;5. '
      'Tangency c&sup2; = a&sup2;m&sup2; + b&sup2; = 45 + 4 = 49, so c = &plusmn;7. Matches the key.',
      320),
    q('u9_ex94_q2', 9, EX9_4, 'EX9.4', 2,
      'Show that the line x = 2y + 4 touches the ellipse x&sup2;/4 + y&sup2;/3 = 1, and find the point of contact.',
      'Touches at (1, &minus;3/2)',
      'Substituting x = 2y + 4 gives (2y+4)&sup2;/4 + y&sup2;/3 = 1 &rArr; 4y&sup2; + 12y + 9 = 0 '
      '&rArr; (2y + 3)&sup2; = 0, a double root, so the line touches. Then y = &minus;3/2 and '
      'x = 2(&minus;3/2) + 4 = 1. Point of contact (1, &minus;3/2). Matches the key.',
      320),
    q('u9_ex94_q3', 9, EX9_4, 'EX9.4', 3,
      'Find the condition that the line y = mx + c may be a tangent to the ellipse '
      'x&sup2;/b&sup2; + y&sup2;/a&sup2; = 1.',
      'c&sup2; = a&sup2; + b&sup2;m&sup2;',
      'For the vertical-major ellipse, substituting y = mx + c and setting the discriminant to zero '
      'gives c&sup2; = a&sup2; + b&sup2;m&sup2;. Matches the key.',
      321),
    q('u9_ex94_q4', 9, EX9_4, 'EX9.4', 4,
      'Find the condition that the following lines may touch the ellipse x&sup2;/a&sup2; + y&sup2;/b&sup2; = 1: '
      '(i) x/p + y/q = 1 &nbsp; (ii) x cos &alpha; + y sin &alpha; = p &nbsp; (iii) lx + my + n = 0',
      '(i) a&sup2;/p&sup2; + b&sup2;/q&sup2; = 1 &nbsp; (ii) p&sup2; = a&sup2;cos&sup2;&alpha; + b&sup2;sin&sup2;&alpha; '
      '&nbsp; (iii) a&sup2;l&sup2; + b&sup2;m&sup2; = n&sup2;',
      'Write each line in slope form y = m&#8202;x + c and impose c&sup2; = a&sup2;m&sup2; + b&sup2;. '
      '(i) m = &minus;q/p, c = q &rArr; q&sup2; = a&sup2;q&sup2;/p&sup2; + b&sup2; &rArr; a&sup2;/p&sup2; + b&sup2;/q&sup2; = 1. '
      '(ii) m = &minus;cot &alpha;, c = p/sin &alpha; &rArr; p&sup2; = a&sup2;cos&sup2;&alpha; + b&sup2;sin&sup2;&alpha;. '
      '(iii) m = &minus;l/m, c = &minus;n/m &rArr; a&sup2;l&sup2; + b&sup2;m&sup2; = n&sup2;. All match the key.',
      321),
    q('u9_ex94_q5', 9, EX9_4, 'EX9.4', 5,
      'Find the equation of the tangent to the ellipse x&sup2;/5 + y&sup2;/4 = 1 which has slope 3.',
      'y = 3x &plusmn; 7',
      'a&sup2; = 5, b&sup2; = 4, m = 3, so c = &plusmn;&radic;(a&sup2;m&sup2; + b&sup2;) = &plusmn;&radic;49 = &plusmn;7. '
      'Tangents y = 3x + 7 and y = 3x &minus; 7. The key prints only y = 3x + 7, but both values of c '
      'satisfy the tangency condition.',
      321),
    q('u9_ex94_q6', 9, EX9_4, 'EX9.4', 6,
      'Find the equations of the tangent and the normal to the ellipse at the given point: '
      '(i) 9x&sup2; + 25y&sup2; = 225 at (3, 12/5) &nbsp; (ii) 49x&sup2; + 64y&sup2; = 64&middot;49 '
      'at (8 cos &alpha;, 7 sin &alpha;)',
      '(i) tangent 9x + 20y &minus; 75 = 0, normal 100x &minus; 45y &minus; 192 = 0 &nbsp; '
      '(ii) tangent 7x cos &alpha; + 8y sin &alpha; = 56, normal 8x sin &alpha; &minus; 7y cos &alpha; '
      '&minus; 15 sin &alpha; cos &alpha; = 0',
      '(i) x&sup2;/25 + y&sup2;/9 = 1; tangent 3x/25 + 4y/15 = 1 (&equiv; 9x + 20y &minus; 75 = 0); '
      'normal 25x/3 &minus; 9y/(12/5) = 16 &rArr; 100x &minus; 45y &minus; 192 = 0. Matches the key. '
      '(ii) x&sup2;/64 + y&sup2;/49 = 1; tangent x cos &alpha;/8 + y sin &alpha;/7 = 1 (&equiv; 7x cos &alpha; '
      '+ 8y sin &alpha; = 56, matches key); normal 8x/cos &alpha; &minus; 7y/sin &alpha; = 15 &rArr; '
      '8x sin &alpha; &minus; 7y cos &alpha; = 15 sin &alpha; cos &alpha;. The key&#39;s normal '
      '"16x sin &alpha; &minus; 14y cos &alpha; = 15 sin &alpha;" does not pass through the contact point '
      '&mdash; key misprint (RHS should be 30 sin &alpha; cos &alpha;).',
      321),
    q('u9_ex94_q7', 9, EX9_4, 'EX9.4', 7,
      'Find the equations of the tangents and normals to the ellipse x&sup2;/3 + y&sup2;/2 = 1 at the ends '
      'of the latus rectum whose abscissa is positive.',
      'Tangents x + &radic;3&#8202;y &minus; 3 = 0 and x &minus; &radic;3&#8202;y &minus; 3 = 0; '
      'normals 3x &minus; &radic;3&#8202;y &minus; 1 = 0 and 3x + &radic;3&#8202;y &minus; 1 = 0',
      'a&sup2; = 3, b&sup2; = 2, c&sup2; = 1, e = 1/&radic;3; LR abscissa x = ae = 1 gives '
      'y&sup2; = 2(1 &minus; 1/3) = 4/3, so ends (1, &plusmn;2/&radic;3). Tangent x/3 &plusmn; y/&radic;3 = 1 '
      '&rArr; x &plusmn; &radic;3&#8202;y &minus; 3 = 0. Normal 3x &minus; 2y/(&plusmn;2/&radic;3) = 1 &rArr; '
      '3x &minus;/+ &radic;3&#8202;y &minus; 1 = 0. Matches the key.',
      321),
    q('u9_ex94_q8', 9, EX9_4, 'EX9.4', 8,
      'Find the equations of the tangents to the ellipse x&sup2;/5 + 9y&sup2;/20 = 1 at the points '
      'whose abscissa is 1.',
      'x + 3y &minus; 5 = 0 and x &minus; 3y &minus; 5 = 0',
      'x = 1 gives 9y&sup2;/20 = 4/5 &rArr; y = &plusmn;4/3. Tangent xx&#8321;/5 + 9yy&#8321;/20 = 1: '
      'at (1, 4/3) &rArr; x/5 + 3y/5 = 1 &rArr; x + 3y &minus; 5 = 0; at (1, &minus;4/3) &rArr; '
      'x &minus; 3y &minus; 5 = 0. The key&#39;s second tangent "x &minus; 3y + 3 = 0" is a misprint '
      '&mdash; it does not pass through (1, &minus;4/3).',
      321),
]

EX9_5 = 'Exercise 9.5'
SOLVED += [
    q('u9_ex95_q1', 9, EX9_5, 'EX9.5', 1,
      'Find the equation of the hyperbola with centre at the origin satisfying: (i) transverse and '
      'conjugate axes 16 and 12, transverse axis along y-axis; (ii) passes through (3&radic;17/4, 1) and '
      '(3, 0), transverse axis along x-axis; (iii) transverse axis of length 8 along y-axis with '
      'eccentricity &radic;5; (iv) transverse axis along x-axis with latus rectum 10 and eccentricity 3/2; '
      '(v) focus (5, 0), directrix x = 2; (vi) eccentricity 3 and focus (8, 0); (vii) eccentricity 2 and '
      'vertex (0, 4).',
      '(i) y&sup2;/64 &minus; x&sup2;/36 = 1 &nbsp; (ii) 16x&sup2; &minus; 9y&sup2; = 144 &nbsp; '
      '(iii) y&sup2;/16 &minus; x&sup2;/64 = 1 &nbsp; (iv) x&sup2;/16 &minus; y&sup2;/20 = 1 &nbsp; '
      '(v) x&sup2;/10 &minus; y&sup2;/15 = 1 &nbsp; (vi) 9x&sup2;/64 &minus; 9y&sup2;/512 = 1 &nbsp; '
      '(vii) y&sup2;/16 &minus; x&sup2;/48 = 1',
      '(i) a = 8, b = 6 along y. (ii) (3,0) gives a&sup2; = 9; (3&radic;17/4, 1) gives 17/16 &minus; 1 = 1/b&sup2; '
      '&rArr; b&sup2; = 16. (iii) a = 4, c = ae = 4&radic;5 &rArr; b&sup2; = 80 &minus; 16 = 64. '
      '(iv) 2b&sup2;/a = 10 and c&sup2; = 9a&sup2;/4 = a&sup2; + b&sup2; &rArr; a = 4, b&sup2; = 20. '
      '(v) ae = 5, a/e = 2 &rArr; a&sup2; = 10, b&sup2; = 15. (vi) a = 8/3, b&sup2; = 64 &minus; 64/9 = 512/9. '
      '(vii) a = 4, c = 8, b&sup2; = 48 with transverse axis along y. All match the key.',
      339),
    q('u9_ex95_q2', 9, EX9_5, 'EX9.5', 2,
      'Find equation of the hyperbola with centre (1, 3) satisfying: (i) focus (2, 3), eccentricity '
      '&radic;3, transverse axis parallel to x-axis; (ii) focus (4, 5), directrix y = 1, transverse axis '
      'parallel to y-axis.',
      '(i) 6(x&minus;1)&sup2; &minus; 3(y&minus;3)&sup2; = 2 &nbsp; (ii) (y&minus;3)&sup2;/2 &minus; '
      '(x&minus;1)&sup2;/2 = 1',
      '(i) c = 1, a = c/e = 1/&radic;3 &rArr; a&sup2; = 1/3, b&sup2; = 2/3 &rArr; 3(x&minus;1)&sup2; &minus; '
      '(3/2)(y&minus;3)&sup2; = 1 &equiv; 6(x&minus;1)&sup2; &minus; 3(y&minus;3)&sup2; = 2. '
      '(ii) As printed the data is impossible (the focus must lie on x = 1); using the key&#39;s intended '
      'focus (1, 5) and directrix y = 2: c = 2, a/e = a&sup2;/c = 1 &rArr; a&sup2; = 2, b&sup2; = 2, giving '
      '(y&minus;3)&sup2;/2 &minus; (x&minus;1)&sup2;/2 = 1. Matches the key; book misprint flagged.',
      340),
    q('u9_ex95_q3', 9, EX9_5, 'EX9.5', 3,
      'Find eccentricity, foci, vertices and latus rectum of each (and sketch the graph): '
      '(i) x&sup2;/9 &minus; y&sup2;/16 = 1 &nbsp; (ii) y&sup2;/5 &minus; x&sup2;/4 = 1 &nbsp; '
      '(iii) 9x&sup2; &minus; y&sup2; + 1 = 0 &nbsp; (iv) x&sup2;/4 &minus; y&sup2;/9 = 1',
      '(i) e = 5/3, foci (&plusmn;5, 0), vertices (&plusmn;3, 0), LR 32/3 &nbsp; (ii) e = 3/&radic;5, '
      'foci (0, &plusmn;3), vertices (0, &plusmn;&radic;5), LR 8/&radic;5 &nbsp; (iii) e = &radic;10/3, '
      'foci (0, &plusmn;&radic;10/3), vertices (0, &plusmn;1), LR 2/9 &nbsp; (iv) e = &radic;13/2, '
      'foci (&plusmn;&radic;13, 0), vertices (&plusmn;2, 0), LR 9',
      '(i) a = 3, b = 4, c = 5. (ii) a&sup2; = 5, b&sup2; = 4, c = 3 (transverse along y). '
      '(iii) Rewrite as y&sup2;/1 &minus; x&sup2;/(1/9) = 1: c&sup2; = 10/9. (iv) a = 2, b = 3, c = &radic;13. '
      'Graphs: branches through the vertices inside the semi-axis rectangle with asymptotes y = &plusmn;(b/a)x '
      '(or &plusmn;(a/b)x when the transverse axis is vertical). All match the key.',
      340),
    q('u9_ex95_q4', 9, EX9_5, 'EX9.5', 4,
      'Find centre, foci, eccentricity, vertices and equations of directrices (and sketch the graph): '
      '(i) (x&minus;5)&sup2;/9 &minus; (y+3)&sup2;/16 = 1 &nbsp; (ii) (y&minus;4)&sup2;/36 &minus; '
      '(x+5)&sup2;/64 = 1 &nbsp; (iii) 9x&sup2; &minus; 4y&sup2; + 36x + 8y &minus; 4 = 0 &nbsp; '
      '(iv) 25x&sup2; &minus; 150x &minus; 9y&sup2; + 72y + 306 = 0',
      '(i) centre (5, &minus;3), foci (10, &minus;3), (0, &minus;3), e = 5/3, vertices (8, &minus;3), '
      '(2, &minus;3), directrices x = 16/5, 34/5 &nbsp; (ii) centre (&minus;5, 4), foci (&minus;5, 14), '
      '(&minus;5, &minus;6), e = 5/3, vertices (&minus;5, 10), (&minus;5, &minus;2), directrices y = 38/5, 2/5 '
      '&nbsp; (iii) centre (&minus;2, 1), foci (&minus;2 &plusmn; &radic;13, 1), e = &radic;13/2, '
      'vertices (0, 1), (&minus;4, 1), directrices x = &minus;2 &plusmn; 4/&radic;13 &nbsp; '
      '(iv) centre (3, 4), foci (3, 4 &plusmn; &radic;34), e = &radic;34/5, vertices (3, 9), (3, &minus;1), '
      'directrices y = 4 &plusmn; 25/&radic;34',
      '(i) a = 3, b = 4, c = 5. (ii) a = 6, b = 8, c = 10 (transverse vertical). '
      '(iii) Completing squares: 9(x+2)&sup2; &minus; 4(y&minus;1)&sup2; = 36 &rArr; (x+2)&sup2;/4 &minus; '
      '(y&minus;1)&sup2;/9 = 1, so a = 2, b = 3, c = &radic;13 (the key&#39;s foci "( &minus;2, &plusmn;&radic;13, 1)" '
      'is a typeslip for (&minus;2 &plusmn; &radic;13, 1)). (iv) 25(x&minus;3)&sup2; &minus; 9(y&minus;4)&sup2; = '
      '&minus;225 &rArr; (y&minus;4)&sup2;/25 &minus; (x&minus;3)&sup2;/9 = 1, so a = 5, b = 3, c = &radic;34; '
      'the key omits the vertices and directrices given here.',
      340),
    q('u9_ex95_q5', 9, EX9_5, 'EX9.5', 5,
      'Find equation of rectangular hyperbola with centre at origin whose vertices are (&plusmn;4, 0) and '
      'find equation of its conjugate hyperbola. Also, find equations of asymptotes of the rectangular '
      'hyperbola.',
      'x&sup2; &minus; y&sup2; = 16; conjugate y&sup2; &minus; x&sup2; = 16; asymptotes y = &plusmn;x',
      'Rectangular hyperbola with vertices (&plusmn;4, 0) has a = b = 4: x&sup2;/16 &minus; y&sup2;/16 = 1 '
      '&rArr; x&sup2; &minus; y&sup2; = 16. Its conjugate is x&sup2;/16 &minus; y&sup2;/16 = &minus;1, i.e. '
      'y&sup2; &minus; x&sup2; = 16. Asymptotes of x&sup2; &minus; y&sup2; = 16 are y = &plusmn;x.',
      340),
    q('u9_ex95_q6', 9, EX9_5, 'EX9.5', 6,
      'Find the eccentricity of a hyperbola whose latus rectum is double the transverse axis.',
      'e = &radic;3',
      '2b&sup2;/a = 2(2a) &rArr; b&sup2; = 2a&sup2; &rArr; c&sup2; = a&sup2; + b&sup2; = 3a&sup2; '
      '&rArr; e = c/a = &radic;3.',
      340),
    q('u9_ex95_q7', 9, EX9_5, 'EX9.5', 7,
      'Show that the eccentricities e&#8321; and e&#8322; of the two conjugate hyperbolas satisfy the '
      'relation e&#8321;&sup2; + e&#8322;&sup2; = e&#8321;&sup2;&#8202;e&#8322;&sup2;.',
      '1/e&#8321;&sup2; + 1/e&#8322;&sup2; = 1 &rArr; e&#8321;&sup2; + e&#8322;&sup2; = e&#8321;&sup2;&#8202;e&#8322;&sup2;',
      'For x&sup2;/a&sup2; &minus; y&sup2;/b&sup2; = 1, e&#8321;&sup2; = (a&sup2;+b&sup2;)/a&sup2;; for its '
      'conjugate y&sup2;/b&sup2; &minus; x&sup2;/a&sup2; = 1, e&#8322;&sup2; = (a&sup2;+b&sup2;)/b&sup2;. '
      'Hence 1/e&#8321;&sup2; + 1/e&#8322;&sup2; = a&sup2;/(a&sup2;+b&sup2;) + b&sup2;/(a&sup2;+b&sup2;) = 1; '
      'multiplying by e&#8321;&sup2;&#8202;e&#8322;&sup2; gives e&#8321;&sup2; + e&#8322;&sup2; = '
      'e&#8321;&sup2;&#8202;e&#8322;&sup2;.',
      340),
]

EX9_6 = 'Exercise 9.6'
SOLVED += [
    q('u9_ex96_q1', 9, EX9_6, 'EX9.6', 1,
      'For what value of k, the line y = 2kx will be tangent to 2x&sup2; &minus; 5y&sup2; = 10.',
      'k = &plusmn;1/&radic;10',
      'x&sup2;/5 &minus; y&sup2;/2 = 1 with m = 2k, c = 0; tangency c&sup2; = a&sup2;m&sup2; &minus; b&sup2; '
      'gives 20k&sup2; = 2, so k = &plusmn;1/&radic;10. Matches the key.',
      351),
    q('u9_ex96_q2', 9, EX9_6, 'EX9.6', 2,
      'Find the condition when the line y = mx + c is tangent to y&sup2;/a&sup2; &minus; x&sup2;/b&sup2; = 1.',
      'c&sup2; = a&sup2; &minus; b&sup2;m&sup2;',
      'Substituting gives (b&sup2;m&sup2; &minus; a&sup2;)x&sup2; + 2b&sup2;mcx + b&sup2;c&sup2; &minus; '
      'a&sup2;b&sup2; = 0; zero discriminant reduces to a&sup2;(b&sup2;m&sup2; + c&sup2; &minus; a&sup2;) = 0, '
      'i.e. c&sup2; = a&sup2; &minus; b&sup2;m&sup2;. The key prints the sign-reversed c&sup2; = b&sup2;m&sup2; '
      '&minus; a&sup2;, which even fails for the horizontal tangents y = &plusmn;a &mdash; key misprint.',
      351),
    q('u9_ex96_q3', 9, EX9_6, 'EX9.6', 3,
      'Find the equation of tangent to the hyperbola 3x&sup2; &minus; 4y&sup2; = 12 when slope is 3.',
      'y = 3x &plusmn; &radic;33',
      'x&sup2;/4 &minus; y&sup2;/3 = 1; c&sup2; = a&sup2;m&sup2; &minus; b&sup2; = 36 &minus; 3 = 33. '
      'Matches the key.',
      352),
    q('u9_ex96_q4', 9, EX9_6, 'EX9.6', 4,
      'Find the equation of tangent and normal to y&sup2;/a&sup2; &minus; x&sup2;/b&sup2; = 1 at '
      '(x&#8321;, y&#8321;).',
      'Tangent: y &minus; y&#8321; = (a&sup2;x&#8321;/(b&sup2;y&#8321;))(x &minus; x&#8321;); '
      'normal: y &minus; y&#8321; = (b&sup2;y&#8321;/(a&sup2;x&#8321;))(x&#8321; &minus; x)',
      'Differentiating: y&prime; = a&sup2;x/(b&sup2;y), giving the tangent slope at the point; the normal is '
      'perpendicular. Equivalently tangent yy&#8321;/a&sup2; &minus; xx&#8321;/b&sup2; = 1 and normal '
      'b&sup2;x/x&#8321; + a&sup2;y/y&#8321; = a&sup2; + b&sup2;. Matches the key.',
      352),
    q('u9_ex96_q5', 9, EX9_6, 'EX9.6', 5,
      'Find the equation of tangent and normal to x&sup2;/5 &minus; y&sup2;/7 = 1 at (2&radic;5, &radic;7).',
      'Tangent: 14&radic;5&#8202;x &minus; 5&radic;7&#8202;y &minus; 105 = 0; normal: y &minus; &radic;7 = '
      '(5&radic;7/(14&radic;5))(2&radic;5 &minus; x)',
      'The printed point is not on the curve (S&#8321; = 4 &minus; 1 = 3), so the key&#39;s line is the polar '
      'T = S&#8321;: xx&#8321;/5 &minus; yy&#8321;/7 = 3 &rArr; 14&radic;5&#8202;x &minus; 5&radic;7&#8202;y '
      '&minus; 105 = 0, with the normal perpendicular to it through the point. Reproduced as keyed; '
      'book/key defect flagged.',
      352),
    q('u9_ex96_q6', 9, EX9_6, 'EX9.6', 6,
      'Find the transformed equation of (x&minus;6)&sup2;/25 + (y+7)&sup2;/16 = 1 when axes are translated '
      'with new origin (6, &minus;7).',
      'X&sup2;/25 + Y&sup2;/16 = 1',
      'With x = X + 6 and y = Y &minus; 7 the equation becomes X&sup2;/25 + Y&sup2;/16 = 1. Matches the key.',
      352),
    q('u9_ex96_q7', 9, EX9_6, 'EX9.6', 7,
      'If xy-axes are rotated through angle &theta;, find the new coordinates of P: (i) (2, 3), '
      '&theta; = 60&deg; &nbsp; (ii) (6, 7), &theta; = 45&deg; &nbsp; (iii) (&minus;4, 6), &theta; = 30&deg;',
      '(i) ((3&radic;3+2)/2, (3&minus;2&radic;3)/2) &nbsp; (ii) (13/&radic;2, 1/&radic;2) &nbsp; '
      '(iii) (3 &minus; 2&radic;3, 2 + 3&radic;3)',
      'Use X = x cos &theta; + y sin &theta;, Y = &minus;x sin &theta; + y cos &theta;. '
      '(i) X = 1 + 3&radic;3/2, Y = &minus;&radic;3 + 3/2. (ii) X = 13/&radic;2, Y = 1/&radic;2. '
      '(iii) X = &minus;2&radic;3 + 3, Y = 2 + 3&radic;3. All match the key.',
      352),
    q('u9_ex96_q8', 9, EX9_6, 'EX9.6', 8,
      'Find new origin O&prime; and new XY-axes with respect to the xy-system if it is translated 6 units '
      'to the left, 5 units up and rotated &pi;/6 radians anticlockwise.',
      'Origin (&minus;6, 5); X-axis: x &minus; &radic;3&#8202;y + 6 + 5&radic;3 = 0; Y-axis: '
      '&radic;3&#8202;x + y + 6&radic;3 &minus; 5 = 0',
      'Translation gives O&prime; = (&minus;6, 5). The X-axis through O&prime; with direction '
      '(cos 30&deg;, sin 30&deg;) is x &minus; &radic;3&#8202;y + 6 + 5&radic;3 = 0; the Y-axis with direction '
      '(&minus;sin 30&deg;, cos 30&deg;) is &radic;3&#8202;x + y + 6&radic;3 &minus; 5 = 0. Matches the key.',
      352),
    q('u9_ex96_q9', 9, EX9_6, 'EX9.6', 9,
      'Find new coordinates of P(4, 5) if new origin is (1, 2) and the XY-system is rotated &pi;/6 radians '
      'anticlockwise from the xy-system.',
      '((3&radic;3+3)/2, (3&radic;3&minus;3)/2)',
      'Relative coordinates (3, 3); X = 3cos30&deg; + 3sin30&deg; = (3&radic;3+3)/2 and '
      'Y = &minus;3sin30&deg; + 3cos30&deg; = (3&radic;3&minus;3)/2. The key&#39;s '
      '((2&radic;3+3)/2, (5&radic;3&minus;8)/2) is internally inconsistent (its components imply different '
      'pre-images) &mdash; key misprint.',
      352),
    q('u9_ex96_q10', 9, EX9_6, 'EX9.6', 10,
      'Identify and sketch the curve xy = 9.',
      'X&sup2; &minus; Y&sup2; = 18 &mdash; rectangular hyperbola, centre at origin, axes rotated 45&deg;',
      'Rotating by 45&deg; (x = (X&minus;Y)/&radic;2, y = (X+Y)/&radic;2) gives (X&sup2;&minus;Y&sup2;)/2 = 9, '
      'i.e. X&sup2; &minus; Y&sup2; = 18 with a&sup2; = b&sup2; = 18: rectangular hyperbola whose vertices are '
      '(&plusmn;3&radic;2, 0) in XY and whose asymptotes are the original axes. Matches the key.',
      352),
    q('u9_ex96_q11', 9, EX9_6, 'EX9.6', 11,
      'Through which angle should the axes be rotated about the origin so that the transformed equation of '
      '9x&sup2; + 12xy + 4y&sup2; &minus; x &minus; y = 0 does not contain the XY term.',
      '&theta; = &frac12; tan&#8315;&sup1;(12/5)',
      'cot 2&theta; = (A &minus; B)/H = (9 &minus; 4)/12 = 5/12, so tan 2&theta; = 12/5 and '
      '&theta; = &frac12; tan&#8315;&sup1;(12/5). Matches the key.',
      352),
]

REV9 = 'Review Exercise 9'
SOLVED += [
    q('u9_rev9_q1', 9, REV9, 'REV9', 1,
      'Tick the correct option: (i) eccentricity zero &rarr; conic; (ii) focus of x&sup2; = &minus;16y; '
      '(iii) latus rectum and vertex of (y&minus;3)&sup2; = &minus;8(x+4); (iv) tangent at (4, 6) to '
      'y&sup2; = 9x; (v) latus rectum of x&sup2;/25 + y&sup2;/16 = 1; (vi) eccentricity of x&sup2;/5 + '
      'y&sup2;/4 = 1; (vii) centre of (x+5)&sup2;/10 + (y&minus;3)&sup2;/20 = 1; (viii) directrices of '
      'x&sup2;/4 + y&sup2;/2 = 1; (ix) ax&sup2; + by&sup2; + gx + fy + c = 0 is a hyperbola if; '
      '(x) auxiliary circle of x&sup2;/6 + y&sup2;/5 = 1; (xi) directrices of (x&minus;h)&sup2;/p&sup2; + '
      '(y&minus;k)&sup2;/q&sup2; = 1 (q &gt; p); (xii) vertices of x&sup2;/9 + y&sup2;/16 = 1 (hyperbola); '
      '(xiii) conjugate hyperbola of x&sup2;/5 &minus; y&sup2;/6 = 1; (xiv) eccentricity of rectangular '
      'hyperbola; (xv) tangent to x&sup2;/6 + y&sup2;/5 = 1 at (&radic;6, 0); (xvi) y = k tangent to '
      'x&sup2;/25 + y&sup2;/9 = 1; (xvii) tangent to x&sup2;/16 &minus; y&sup2;/9 = 1 with slope 2; '
      '(xviii) xy = c&sup2; represents; (xix) origin shifted to (2, 3), coordinates of (5, 6); '
      '(xx) abscissa transformation for rotation by &pi;/4.',
      '(i) c &nbsp; (ii) d &nbsp; (iii) d &nbsp; (iv) d &nbsp; (v) b &nbsp; (vi) b &nbsp; (vii) c &nbsp; '
      '(viii) a &nbsp; (ix) b &nbsp; (x) d &nbsp; (xi) c &nbsp; (xii) c &nbsp; (xiii) b &nbsp; (xiv) d &nbsp; '
      '(xv) b &nbsp; (xvi) a &nbsp; (xvii) d &nbsp; (xviii) c &nbsp; (xix) b &nbsp; (xx) b',
      '(i) e = 0 is a circle. (ii) 4a = 16 opening down: (0, &minus;4). (iii) 4a = 8, vertex (&minus;4, 3). '
      '(iv) 6y = (9/2)(x+4) &equiv; 3x &minus; 4y + 12 = 0 (options a and d coincide; key ticks d). '
      '(v) 2b&sup2;/a = 32/5. (vi) c&sup2; = 1, e = 1/&radic;5. (vii) (&minus;5, 3). (viii) x = &plusmn;a/e = '
      '&plusmn;4/&radic;2 (options a and d coincide; key ticks a). (ix) a, b of different sign. '
      '(x) x&sup2; + y&sup2; = 6. (xi) major axis vertical: y &minus; k = &plusmn;q/e. (xii) (0, &plusmn;4). '
      '(xiii) y&sup2;/6 &minus; x&sup2;/5 = 1. (xiv) &radic;2. (xv) x = &radic;6. (xvi) k = &plusmn;3. '
      '(xvii) c&sup2; = 16&middot;4 &minus; 9 = 55. (xviii) hyperbola. (xix) (3, 3). '
      '(xx) x = x&prime;/&radic;2 &minus; y&prime;/&radic;2. All match the key.',
      352),
    q('u9_rev9_q2', 9, REV9, 'REV9', 2,
      'Find the foci, vertices and directrices for the conic: (a) (x&minus;5)&sup2;/25 + (y+3)&sup2;/16 = 1 '
      '&nbsp; (b) (x+4)&sup2;/9 &minus; (y+7)&sup2;/16 = 1',
      '(a) foci (8, &minus;3), (2, &minus;3); vertices (10, &minus;3), (0, &minus;3); x &minus; 5 = &plusmn;25/3 '
      '&nbsp; (b) foci (1, &minus;7), (&minus;9, &minus;7); vertices (&minus;1, &minus;7), (&minus;7, &minus;7); '
      'x + 4 = &plusmn;9/5',
      '(a) Ellipse with a = 5, b = 4, c = 3, e = 3/5; directrices x = 5 &plusmn; a/e = 5 &plusmn; 25/3. '
      '(b) Hyperbola with a = 3, b = 4, c = 5, e = 5/3; directrices x = &minus;4 &plusmn; a/e = '
      '&minus;4 &plusmn; 9/5. Both match the key.',
      354),
    q('u9_rev9_q3', 9, REV9, 'REV9', 3,
      'Find the condition of tangency when the line y = x + c is tangent to the conic: (i) y&sup2; = 10x '
      '&nbsp; (ii) 2x&sup2; + 3y&sup2; = 6 &nbsp; (iii) 5x&sup2; &minus; 7y&sup2; = 35',
      '(i) c = 5/2 &nbsp; (ii) c = &plusmn;&radic;5 &nbsp; (iii) c = &plusmn;&radic;2',
      '(i) Parabola 4a = 10: c = a/m = 5/2. (ii) x&sup2;/3 + y&sup2;/2 = 1: c&sup2; = a&sup2;m&sup2; + '
      'b&sup2; = 5. (iii) x&sup2;/7 &minus; y&sup2;/5 = 1: c&sup2; = a&sup2;m&sup2; &minus; b&sup2; = 2. '
      'All match the key.',
      354),
    q('u9_rev9_q4', 9, REV9, 'REV9', 4,
      'Find transformed equation of (x+5)&sup2;/7 &minus; (y&minus;3)&sup2;/5 = 1 when new origin is '
      '(&minus;5, 3).',
      'X&sup2;/7 &minus; Y&sup2;/5 = 1',
      'With x = X &minus; 5 and y = Y + 3 the equation becomes X&sup2;/7 &minus; Y&sup2;/5 = 1. The key prints '
      'X&sup2;/7 + Y&sup2;/5 = 1, losing the hyperbola&#39;s minus sign &mdash; key misprint.',
      354),
    q('u9_rev9_q5', 9, REV9, 'REV9', 5,
      'If xy-axes are rotated through angle &theta;, find coordinates of P if new coordinates are '
      '(&minus;2, 7), &theta; = 45&deg;.',
      'P = (&minus;9/&radic;2, 5/&radic;2)',
      'Old coordinates from new: x = X cos &theta; &minus; Y sin &theta; = (&minus;2 &minus; 7)/&radic;2 = '
      '&minus;9/&radic;2 and y = X sin &theta; + Y cos &theta; = (&minus;2 + 7)/&radic;2 = 5/&radic;2. '
      'Matches the key.',
      354),
]

EX10_1 = 'Exercise 10.1'
SOLVED += [
    q('u10_ex101_q1', 10, EX10_1, 'EX10.1', 1,
      'Find the order and degree of each of the following differential equations: (i) d&sup2;y/dx&sup2; + '
      '(dy/dx)&sup3; + xy = 0 &nbsp; (ii) x&sup3;dx + y&sup3;dy = 0 &nbsp; (iii) dy/dx = &radic;&#8323;'
      '((d&sup2;y/dx&sup2; + 1)&sup2;) &nbsp; (iv) d&sup3;y/dx&sup3; &minus; 5(d&sup2;y/dx&sup2;)&sup3; + '
      '7(dy/dx)&sup8; = 0 &nbsp; (v) d&#8308;y/dx&#8308; &minus; (dy/dx)^(1/2) = 0',
      '(i) order 2, degree 1 &nbsp; (ii) order 1, degree 1 &nbsp; (iii) order 2, degree 2 &nbsp; '
      '(iv) order 3, degree 1 &nbsp; (v) order 4, degree 2',
      '(ii) dy/dx = &minus;x&sup3;/y&sup3;. (iii) Cubing: (y&prime;)&sup3; = (y&Prime; + 1)&sup2;, so the '
      'highest derivative y&Prime; appears with power 2. (v) Squaring: (y&#8308;)&sup2; = y&prime;. '
      'All match the key.',
      360),
    q('u10_ex101_q2', 10, EX10_1, 'EX10.1', 2,
      'Show that y = x &minus; x ln x is the solution of the differential equation x&#8202;dy/dx + x &minus; y = 0.',
      'x&#8202;y&prime; + x &minus; y = 0 holds identically',
      'y&prime; = 1 &minus; (ln x + 1) = &minus;ln x, so x(&minus;ln x) + x &minus; (x &minus; x ln x) = '
      '&minus;x ln x + x ln x = 0.',
      360),
    q('u10_ex101_q3', 10, EX10_1, 'EX10.1', 3,
      'Show that y = Ae^(2x) + Be^(3x) is the general solution of d&sup2;y/dx&sup2; &minus; 5&#8202;dy/dx + 6y = 0.',
      'y&Prime; &minus; 5y&prime; + 6y = 0 with two arbitrary constants',
      'y&prime; = 2Ae^(2x) + 3Be^(3x), y&Prime; = 4Ae^(2x) + 9Be^(3x); then '
      '(4 &minus; 10 + 6)Ae^(2x) + (9 &minus; 15 + 6)Be^(3x) = 0. The two constants match the order 2, '
      'so it is the general solution.',
      360),
    q('u10_ex101_q4', 10, EX10_1, 'EX10.1', 4,
      'Obtain the differential equation by eliminating arbitrary constants from: (i) y = A cos x + B sin x '
      '&nbsp; (ii) y = A sin(x + 1) &nbsp; (iii) y = ax&sup2; + bx &nbsp; (iv) y = C&#8321;e^x + '
      'C&#8322;e^(&minus;2x)',
      '(i) y&Prime; + y = 0 &nbsp; (ii) dy/dx = y cot(x + 1) &nbsp; (iii) x&sup2;y&Prime; &minus; '
      '2xy&prime; + 2y = 0 &nbsp; (iv) y&Prime; + y&prime; &minus; 2y = 0',
      '(i) y&Prime; = &minus;A cos x &minus; B sin x = &minus;y. (ii) y&prime; = A cos(x+1), so '
      'y&prime;/y = cot(x+1). (iii) y&prime; = 2ax + b, y&Prime; = 2a give a = y&Prime;/2, b = y&prime; &minus; '
      'xy&Prime;; substituting back yields x&sup2;y&Prime; &minus; 2xy&prime; + 2y = 0. (iv) The exponents 1 and '
      '&minus;2 are roots of r&sup2; + r &minus; 2 = 0. All match the key.',
      360),
    q('u10_ex101_q5', 10, EX10_1, 'EX10.1', 5,
      'Find the particular solution of: (i) dy/dx = &radic;(1+cos y)/sin y, y(3) = &pi;/2, given that '
      'x + 2&radic;(1+cos y) + c = 0 is the general solution; (ii) d&sup2;y/dx&sup2; &minus; dy/dx + 2y = 0, '
      'y(0) = 1, y&prime;(0) = 3, given that y = Ae^(2x) + Be^(&minus;x) is the general solution.',
      '(i) x + 2&radic;(1+cos y) &minus; 5 = 0 &nbsp; (ii) 3y = 4e^(2x) &minus; e^(&minus;x)',
      '(i) 3 + 2&radic;(1+cos &pi;/2) + c = 0 &rArr; 3 + 2 + c = 0 &rArr; c = &minus;5. '
      '(ii) A + B = 1 and 2A &minus; B = 3 give A = 4/3, B = &minus;1/3. Note the printed equation of (ii) '
      'should read y&Prime; &minus; y&prime; &minus; 2y = 0 for the stated general solution (roots 2, &minus;1) '
      '&mdash; book misprint; answers match the key.',
      360),
]

EX10_2 = 'Exercise 10.2'
SOLVED += [
    q('u10_ex102_q1', 10, EX10_2, 'EX10.2', 1,
      'Solve by separating the variables: (i) x tan y dy = dx &nbsp; (ii) x sin y dx + (x&sup2;+1) cos y dy = 0 '
      '&nbsp; (iii) y(1+x)dx + x(1+y)dy = 0 &nbsp; (iv) (1+x&sup3;)dy &minus; x&sup2;dx = 0 &nbsp; '
      '(v) xy dy = (y+1)(1&minus;x)dx &nbsp; (vi) dy/dx = 3y&sup2; &minus; y&sup2; sin x &nbsp; '
      '(vii) (y&sup2;&minus;1) dy/dx = 4xy&sup2; &nbsp; (viii) x cos&sup2;y dx + tan y dy = 0',
      '(i) sec y = Cx &nbsp; (ii) sin y&middot;&radic;(x&sup2;+1) = C &nbsp; (iii) (x+y) + ln(xy) = C &nbsp; '
      '(iv) y = (1/3)ln(1+x&sup3;) + C &nbsp; (v) (x+y) &minus; ln(x+xy) = C &nbsp; (vi) &minus;1/y = 3x + cos x + C '
      '&nbsp; (vii) y + 1/y = 2x&sup2; + C &nbsp; (viii) tan&sup2;y = &minus;x&sup2; + C',
      '(i) &int;tan y dy = &int;dx/x. (ii) &int;x/(x&sup2;+1)dx + &int;cot y dy = 0 gives '
      '&frac12;ln(x&sup2;+1) + ln sin y = c, i.e. sin y = C/&radic;(x&sup2;+1); the key prints '
      'C&radic;(x&sup2;+1) with the wrong power of (x&sup2;+1). (iii) Divide by xy. (iv) dy = x&sup2;/(1+x&sup3;)dx. '
      '(v) y/(y+1)dy = (1&minus;x)/x dx. (vi) dy/y&sup2; = (3 &minus; sin x)dx. (vii) (1 &minus; 1/y&sup2;)dy = '
      '4x dx. (viii) x dx + tan y sec&sup2;y dy = 0.',
      370),
    q('u10_ex102_q2', 10, EX10_2, 'EX10.2', 2,
      'Solve the homogeneous equations: (i) (x+y)dy &minus; (x&minus;y)dx = 0 &nbsp; (ii) (6x&sup2;+2y&sup2;)dx '
      '&minus; (x&sup2;+4xy)dy = 0 &nbsp; (iii) (x&sup2;+3y&sup2;)dx &minus; 2xy dy = 0 &nbsp; '
      '(iv) (x&sup2;+y&sup2;)dx &minus; 2xy dy = 0 &nbsp; (v) dy/dx = y/x + sin(y/x)',
      '(i) &radic;(x&sup2;&minus;2xy&minus;y&sup2;) = C &nbsp; (ii) (3x&minus;2y)(2x+y) = Cx &nbsp; '
      '(iii) x&sup2; + y&sup2; = Cx&sup3; &nbsp; (iv) x&sup2; &minus; y&sup2; = Cx &nbsp; '
      '(v) cosec(y/x) &minus; cot(y/x) = Cx',
      'Substitute y = vx throughout. (i) (1+v)/(1&minus;2v&minus;v&sup2;)dv = dx/x gives '
      'x&sup2;&minus;2xy&minus;y&sup2; = C. (ii) (1+4v)/(6&minus;v&minus;2v&sup2;)dv = dx/x gives '
      'x(6&minus;v&minus;2v&sup2;) = C, i.e. 6x&sup2;&minus;xy&minus;2y&sup2; = Cx; the key&#39;s '
      '(y+2x)(2y&minus;3x) = C drops the factor x and does not differentiate back to the ODE. '
      '(iii) 2v/(1+v&sup2;)dv = dx/x. (iv) 2v/(1&minus;v&sup2;)dv = dx/x. (v) csc v dv = dx/x with '
      'tan(v/2) = csc v &minus; cot v.',
      370),
    q('u10_ex102_q3', 10, EX10_2, 'EX10.2', 3,
      'Solve: (i) dy/dx = (x+y+1)/(x&minus;y) &nbsp; (ii) (2x+y+1)dx + (2x+y&minus;1)dy = 0 &nbsp; '
      '(iii) dy/dx = (x+2y&minus;3)/(2x+y&minus;3) &nbsp; (iv) dy/dx = (2x+y&minus;2)/(2x+y+3)',
      '(i) tan&#8315;&sup1;((2y+1)/(2x+1)) &minus; ln&radic;(x&sup2;+y&sup2;+x+y+&frac12;) = C &nbsp; '
      '(ii) (x+y) + 2ln|2x+y&minus;3| = C &nbsp; (iii) (x+y&minus;2) = C(x&minus;y)&sup3; &nbsp; '
      '(iv) (1/3)(2x+y) + (5/9)ln|6x+3y+4| = x + C',
      '(i) Shift to X = x+&frac12;, Y = y+&frac12; then Y&prime; = (X+Y)/(X&minus;Y): '
      'tan&#8315;&sup1;(Y/X) &minus; &frac12;ln(X&sup2;+Y&sup2;) = C. (ii) u = 2x+y gives dx = '
      '(u&minus;1)/(u&minus;3)du, so x = u + 2ln|u&minus;3| + C; the key&#39;s single-ln form fails d/dx '
      'verification. (iii) Shift to X = x&minus;1, Y = y&minus;1 then (2+v)/(1&minus;v&sup2;)dv = dX/X gives '
      '(1+v)/(1&minus;v)&sup3; = CX&sup2;. (iv) u = 2x+y gives (u+3)/(3u+4)du = dx.',
      370),
    q('u10_ex102_q4', 10, EX10_2, 'EX10.2', 4,
      'A body moves in a straight line so that its velocity exceeds by 2 its distance from a fixed point of '
      'the line. If V = 5 m/s when t = 0, find the equation of the motion.',
      's = 5e^t &minus; 2',
      'ds/dt = s + 2 &rArr; ln(s+2) = t + c &rArr; s + 2 = Ce^t. At t = 0, s = V &minus; 2 = 3 so C = 5. '
      'The key omits this question; solution supplied here.',
      370),
    q('u10_ex102_q5', 10, EX10_2, 'EX10.2', 5,
      'When the temperature of the air is 290 K a certain substance cools from 400 K to 350 K in 20 minutes. '
      'Find (i) the temperature after 40 minutes; (ii) after how much time the temperature is 300 K.',
      '(i) &asymp; 322 K &nbsp; (ii) &asymp; 79 minutes',
      'Newton&#39;s cooling: T &minus; 290 = Ce^(&minus;kt) with C = 110 and e^(&minus;20k) = 60/110 = 6/11. '
      '(i) T(40) &minus; 290 = 110(6/11)&sup2; = 360/11 &asymp; 32.7 &rArr; T &asymp; 322 K. '
      '(ii) 10 = 110e^(&minus;kt) &rArr; t = 20 ln 11/ln(11/6) &asymp; 79 minutes. Matches the key.',
      371),
    q('u10_ex102_q6', 10, EX10_2, 'EX10.2', 6,
      'A resistor of 5 ohms and a capacitor of 0.02 farads are connected with a 10 volts battery. Assume that '
      'initially the charge on the capacitor is 5 coulombs. Find the charge and current in the circuit at any '
      'time.',
      'Q = 1/5 + (24/5)e^(&minus;10t); I = &minus;48e^(&minus;10t)',
      'R dQ/dt + Q/C = V &rArr; 5 dQ/dt + 50Q = 10 &rArr; dQ/dt + 10Q = 2, so Q = 1/5 + Ce^(&minus;10t); '
      'Q(0) = 5 gives C = 24/5. I = dQ/dt = &minus;48e^(&minus;10t). Matches the key.',
      371),
    q('u10_ex102_q7', 10, EX10_2, 'EX10.2', 7,
      'The population of a certain town is directly proportional to the square root of the present population '
      'at any time. If the population initially is 20000: (i) how much the population after 10 years? '
      '(ii) after how much time the population be doubled?',
      '(i) &asymp; 66860 &nbsp; (ii) 5 years (the key&#39;s 14.92 years is the five-fold time)',
      'dP/dt = k&radic;P &rArr; 2&radic;P = kt + 2&radic;20000. As printed no second datum fixes k; the '
      'key&#39;s numbers imply doubling in 5 years (k &asymp; 23.43), giving P(10) = 20000(2&radic;2 &minus; 1)&sup2; '
      '&asymp; 66860. With that datum the doubling time is 5 years, while 14.92 years corresponds to '
      'P = 100000 (five-fold) &mdash; key discrepancy flagged.',
      371),
]

EX10_3 = 'Exercise 10.3'
SOLVED += [
    q('u10_ex103_q1', 10, EX10_3, 'EX10.3', 1,
      'Find the orthogonal trajectory of the curves y = ax&sup2;.',
      'y&sup2; = &minus;x&sup2;/2 + C (&equiv; x&sup2; + 2y&sup2; = C)',
      'Family ODE: y&prime; = 2y/x; orthogonal: y&prime; = &minus;x/(2y) &rArr; 2y dy = &minus;x dx. '
      'Matches the key.',
      376),
    q('u10_ex103_q2', 10, EX10_3, 'EX10.3', 2,
      'Find the orthogonal trajectories of the hyperbola xy = c.',
      'y&sup2; &minus; x&sup2; = C',
      'Family ODE: y&prime; = &minus;y/x; orthogonal: y&prime; = x/y &rArr; y dy = x dx. Matches the key.',
      376),
    q('u10_ex103_q3', 10, EX10_3, 'EX10.3', 3,
      'Find the orthogonal trajectories of the family of parabolas y&sup2; = 4ax.',
      'y&sup2; + 2x&sup2; = C',
      '2yy&prime; = 4a = y&sup2;/x gives y&prime; = y/(2x); orthogonal: y&prime; = &minus;2x/y &rArr; '
      'y dy = &minus;2x dx. Matches the key.',
      376),
    q('u10_ex103_q4', 10, EX10_3, 'EX10.3', 4,
      'Find the orthogonal trajectories of the family of curves y = x/(1 + c&#8321;x).',
      'x&sup3; + y&sup3; = C',
      '1/y = 1/x + c&#8321; gives y&prime; = y&sup2;/x&sup2;; orthogonal: y&prime; = &minus;x&sup2;/y&sup2; '
      '&rArr; y&sup2;dy = &minus;x&sup2;dx &rArr; x&sup3; + y&sup3; = C. The key&#39;s &minus;1/y = &minus;1/x + C '
      'is the original family itself &mdash; key misprint.',
      376),
    q('u10_ex103_q5', 10, EX10_3, 'EX10.3', 5,
      'Find the general equation of family of curves perpendicular to y = c&#8321; sin x.',
      'e^(y&sup2;) = C cos&sup2;x',
      'Family ODE: y&prime; = y cot x; orthogonal: y&prime; = &minus;tan x/y &rArr; y dy = &minus;tan x dx '
      '&rArr; y&sup2;/2 = ln cos x + c &rArr; e^(y&sup2;) = C cos&sup2;x. Matches the key.',
      376),
    q('u10_ex103_q6', 10, EX10_3, 'EX10.3', 6,
      'Find the general equation of family of curves perpendicular to x^(1/3) + y^(1/3) = c.',
      'y^(5/3) &minus; x^(5/3) = C',
      'Family ODE: y&prime; = &minus;y^(2/3)/x^(2/3); orthogonal: y&prime; = x^(2/3)/y^(2/3) &rArr; '
      'y^(2/3)dy = x^(2/3)dx &rArr; y^(5/3) &minus; x^(5/3) = C. Matches the key.',
      376),
]

REV10 = 'Review Exercise 10'
SOLVED += [
    q('u10_rev10_q1', 10, REV10, 'REV10', 1,
      'Tick the correct answer: (i) order and degree of 1 + y&Prime; = xy&prime;; (ii) degree of '
      '(y&prime;)&#8308; + 3y&Prime;&Prime;; (iii) order and degree of (y&Prime;&Prime;&Prime;)&sup2; = '
      '&radic;(y&prime;); (iv) degree of y = x(y&prime;)&sup2; + y&prime;; (v) order and degree of '
      'y&Prime; = &radic;(1 + (y&prime;)&sup3;); (vi) value of y(&minus;1) if xdy &minus; ydx = 0, y(1) = 2; '
      '(vii) general solution of y&prime; + y&sup2; = 0; (viii) general solution of 9yy&prime; + 4x = 0.',
      '(i) b &nbsp; (ii) c &nbsp; (iii) a &nbsp; (iv) b &nbsp; (v) a &nbsp; (vi) b &nbsp; (vii) b &nbsp; '
      '(viii) a',
      '(i) order 2, degree 1. (ii) highest derivative y&Prime; appears to power 1, so degree 1. '
      '(iii) squaring twice: (y&Prime;&Prime;&Prime;)&#8308; = y&prime; &rArr; order 3, degree 4. '
      '(iv) y&prime; appears squared &rArr; degree 2. (v) (y&Prime;)&sup2; = 1 + (y&prime;)&sup3; &rArr; '
      'order 2, degree 2. (vi) y = cx with y(1) = 2 gives y = 2x, y(&minus;1) = &minus;2. '
      '(vii) &minus;1/y = &minus;x + c &rArr; y = 1/(x + c). (viii) 9y dy = &minus;4x dx &rArr; '
      '4x&sup2; + 9y&sup2; = c. All match the key.',
      376),
    q('u10_rev10_q2', 10, REV10, 'REV10', 2,
      'Show that y = Ae^(3x) + Be^(4x) is the general solution of d&sup2;y/dx&sup2; &minus; 7dy/dx + 12y = 0.',
      'Verified (identity holds for all A, B)',
      'y&prime; = 3Ae^(3x) + 4Be^(4x) and y&Prime; = 9Ae^(3x) + 16Be^(4x), so '
      'y&Prime; &minus; 7y&prime; + 12y = (9 &minus; 21 + 12)Ae^(3x) + (16 &minus; 28 + 12)Be^(4x) = 0. '
      'The solution contains two independent arbitrary constants, matching the order 2 of the equation, '
      'so it is the general solution.',
      377),
    q('u10_rev10_q3', 10, REV10, 'REV10', 3,
      'Solve: (i) cos(x+y)dy = dx &nbsp; (ii) x&sup2;y&prime; = x&sup2; + xy + y&sup2; &nbsp; '
      '(iii) (xy + y&sup2;)dx = (x&sup2; &minus; xy)dy &nbsp; (iv) xy&prime; = y + x tan(y/x) &nbsp; '
      '(v) (2x + 3y &minus; 5)dy + (3x + 2y + 1)dx = 0 &nbsp; (vi) (2x + y + 1)dx + (4x + 2y &minus; 1)dy = 0 '
      '&nbsp; (vii) y&prime; = y/x + cos(y/x) &nbsp; (viii) y&prime; = e^(x+y)',
      '(i) tan((x+y)/2) = y + C &nbsp; (ii) tan&#8315;&sup1;(y/x) = ln x + C &nbsp; (iii) x/y + ln(xy) = C '
      '&nbsp; (iv) sin(y/x) = Cx &nbsp; (v) 3x&sup2; + 4xy + 3y&sup2; + 2x &minus; 10y = C &nbsp; '
      '(vi) ln|2x + y &minus; 1| + (x + 2y) = C &nbsp; (vii) sec(y/x) + tan(y/x) = Cx &nbsp; '
      '(viii) &minus;e^(&minus;y) = e^x + C',
      '(i) Put u = x + y: dx = cos u/(1 + cos u) du = (1 &minus; &frac12;sec&sup2;(u/2))du, so '
      'x = u &minus; tan(u/2) + C. (ii) Homogeneous: v = y/x gives dv/(1 + v&sup2;) = dx/x. '
      '(iii) v = y/x gives (1 &minus; v)/(2v&sup2;) dv = dx/x, integrating to x/y + ln(xy) = C; the key&#39;s '
      'x/y = ln(Cy) does not differentiate back to the equation &mdash; key misprint. (iv) v = y/x gives '
      'cot v dv = dx/x, so ln sin v = ln x + c, i.e. sin(y/x) = Cx; the key&#39;s y = x cos&#8315;&sup1;(Cx) '
      'corresponds to y&prime; = y/x &minus; cot(y/x) &mdash; key misprint. (v) Exact after shifting the origin '
      'to (&minus;13/5, 17/5); the key&#39;s shifted form is the same first integral. (vi) u = 2x + y gives '
      '3(1 &minus; u)dx + (2u &minus; 1)du = 0. (vii) v = y/x gives sec v dv = dx/x. (viii) Separate: '
      'e^(&minus;y)dy = e^x dx.',
      377),
    q('u10_rev10_q4', 10, REV10, 'REV10', 4,
      'If y = (A + Bx)e^(&minus;2x) is the general solution of d&sup2;y/dx&sup2; + 4dy/dx + 4y = 0, find its '
      'particular solution when y(0) = 2 and y&prime;(0) = 5.',
      'y = (2 + 9x)e^(&minus;2x)',
      'y(0) = A = 2. y&prime; = Be^(&minus;2x) &minus; 2(A + Bx)e^(&minus;2x), so y&prime;(0) = B &minus; 2A = 5 '
      'gives B = 9. Matches the key.',
      378),
    q('u10_rev10_q5', 10, REV10, 'REV10', 5,
      'Form the differential equation by eliminating the arbitrary constants: (i) y = 9/x + b &nbsp; '
      '(ii) y = e^x(a cos x + b sin x) &nbsp; (iii) y = ln cos(x &minus; a) + b &nbsp; '
      '(iv) y = A cos(ln x) + B sin(ln x)',
      '(i) y&prime; = &minus;9/x&sup2; &nbsp; (ii) y&Prime; &minus; 2y&prime; + 2y = 0 &nbsp; '
      '(iii) y&Prime; = &minus;(1 + (y&prime;)&sup2;) &nbsp; (iv) x&sup2;y&Prime; + xy&prime; + y = 0',
      '(i) Differentiate once: y&prime; = &minus;9/x&sup2; (b disappears). (ii) Roots of the auxiliary equation '
      'are 1 &plusmn; i, so the ODE is y&Prime; &minus; 2y&prime; + 2y = 0. (iii) y&prime; = &minus;tan(x &minus; a) '
      'and y&Prime; = &minus;sec&sup2;(x &minus; a) = &minus;(1 + tan&sup2;(x &minus; a)), giving '
      'y&Prime; = &minus;(1 + (y&prime;)&sup2;); the key prints the positive sign &mdash; key misprint. '
      '(iv) With t = ln x the equation becomes d&sup2;y/dt&sup2; + y = 0, i.e. x&sup2;y&Prime; + '
      'xy&prime; + y = 0.',
      378),
    q('u10_rev10_q6', 10, REV10, 'REV10', 6,
      'A particle moving in a straight line has acceleration dv/dt = 1/&radic;t. If V = 25 m/s when t = 9 s, '
      'find the velocity after 20 s.',
      'v = 2&radic;t + 19; v(20) = 4&radic;5 + 19 m/s &asymp; 27.94 m/s',
      'v = &int;t^(&minus;1/2)dt = 2&radic;t + C; 25 = 2(3) + C gives C = 19. Hence v(20) = 2&radic;20 + 19 = '
      '4&radic;5 + 19 m/s. Matches the key.',
      378),
    q('u10_rev10_q7', 10, REV10, 'REV10', 7,
      'Find the orthogonal trajectories of the family of curves 3x + 4y = c.',
      '3y = 4x + C',
      'Differentiating, 3 + 4y&prime; = 0, so the family slope is &minus;3/4. Orthogonal trajectories have slope '
      '4/3: dy/dx = 4/3 &rArr; 3y = 4x + C (another family of parallel lines). Matches the key.',
      378),
    q('u10_rev10_q8', 10, REV10, 'REV10', 8,
      'Find the equation of the family of curves perpendicular to y = ln(tan x + c&#8321;).',
      'e^(&minus;y) = &frac12;(x + (sin 2x)/2) + C',
      'From e^y = tan x + c&#8321;, the family ODE is e^y y&prime; = sec&sup2;x. Perpendicular curves satisfy '
      'y&prime; = &minus;e^y cos&sup2;x, i.e. e^(&minus;y)dy = &minus;cos&sup2;x dx = &minus;(1 + cos 2x)/2 dx. '
      'Integrating: &minus;e^(&minus;y) = &minus;&frac12;(x + (sin 2x)/2) + C&#8321;. Matches the key.',
      378),
]

EX11 = 'Exercise 11'
SOLVED += [
    q('u11_ex11_q1', 11, EX11, 'EX11', 1,
      'Find &part;f/&part;x and &part;f/&part;y when f(x, y) is given by: (i) 3x&sup3; + y&sup2; &minus; 6x + '
      '2y &minus; 7 &nbsp; (ii) x&sup2; + xy &minus; y&sup2; &minus; 2x &minus; 2y &minus; 8 &nbsp; '
      '(iii) sin(x + y) &nbsp; (iv) e^x cos y &nbsp; (v) &frac12;ln(x&sup2; + y&sup2;)',
      '(i) 9x&sup2; &minus; 6, 2y + 2 &nbsp; (ii) 2x + y &minus; 2, x &minus; 2y &minus; 2 &nbsp; '
      '(iii) cos(x + y), cos(x + y) &nbsp; (iv) e^x cos y, &minus;e^x sin y &nbsp; '
      '(v) x/(x&sup2; + y&sup2;), y/(x&sup2; + y&sup2;)',
      'Differentiate treating the other variable as constant. (i) &part;/&part;x kills y-terms and vice versa. '
      '(iii) Chain rule on x + y gives cos(x + y) for both. (iv) e^x is constant in y, cos y is constant in x. '
      '(v) &frac12; &middot; 2x/(x&sup2; + y&sup2;) and the symmetric y form. All match the key.',
      389),
    q('u11_ex11_q2', 11, EX11, 'EX11', 2,
      'The volume of the cone is given by V = (1/3)&pi;r&sup2;h. Differentiate V with respect to its '
      'independent variables.',
      '&part;V/&part;r = (2/3)&pi;rh &nbsp; &part;V/&part;h = (1/3)&pi;r&sup2;',
      'Holding h constant: &part;V/&part;r = (1/3)&pi;h &middot; 2r = (2/3)&pi;rh. Holding r constant: '
      '&part;V/&part;h = (1/3)&pi;r&sup2;. Matches the key.',
      389),
    q('u11_ex11_q3', 11, EX11, 'EX11', 3,
      'Check whether the following functions are homogeneous or not; find the degree if homogeneous: '
      '(i) (x&sup3; &minus; 5x&sup2;y + 7xy&sup2; + y&sup3;)/(xy&sup2;) &nbsp; (ii) tan((x+y)/y&sup2;) &nbsp; '
      '(iii) x&sup3; + 3x&sup2;y + 2y&sup2;x + y&sup3; &nbsp; (iv) cos&#8315;&sup1;((x&sup2; &minus; '
      'y&sup2;)/(xy)) &nbsp; (v) (x&sup2; &minus; xy + y&sup2;)/(x + y&sup2;) &nbsp; '
      '(vi) &radic;(x&#8312; &minus; 3x&sup2;y&#8310;) &nbsp; (vii) x&sup3; sin(y&sup2;/x) &nbsp; '
      '(viii) ln((x&sup2; + y&sup2;)/(x + y))',
      '(i) homogeneous, degree 0 &nbsp; (ii) not homogeneous &nbsp; (iii) homogeneous, degree 3 &nbsp; '
      '(iv) homogeneous, degree 0 &nbsp; (v) not homogeneous &nbsp; (vi) homogeneous, degree 4 &nbsp; '
      '(vii) not homogeneous &nbsp; (viii) not homogeneous',
      'Test f(tx, ty) = t&#8319;f(x, y). (i) degree 3 over degree 3 &rArr; n = 0. (ii) argument mixes degree 1 '
      'over degree 2. (iii) every term degree 3. (iv) argument degree 0. (v) denominator mixes degrees 1 and 2. '
      '(vi) radicand degree 8, square root halves it &rArr; n = 4. (vii) sin(t&middot;y&sup2;/x) does not scale '
      'as a power of t. (viii) ln t + ln((x&sup2;+y&sup2;)/(x+y)) &ne; t&#8319;f. All match the key.',
      389),
    q('u11_ex11_q4', 11, EX11, 'EX11', 4,
      'Verify Euler&#39;s theorem x &part;f/&part;x + y &part;f/&part;y = nf for: (i) xy + y&sup2; &nbsp; '
      '(ii) cos(x/y) &nbsp; (iii) &radic;(xy) &minus; x &nbsp; (iv) ln((x + y)/y)',
      '(i) = 2f (n = 2) &nbsp; (ii) = 0 (n = 0) &nbsp; (iii) = f (n = 1) &nbsp; (iv) = 0 (n = 0)',
      '(i) f&#8339; = y, f&#7527; = x + 2y &rArr; xy + xy + 2y&sup2; = 2f. (ii) f&#8339; = &minus;sin(x/y)/y, '
      'f&#7527; = x sin(x/y)/y&sup2; &rArr; the two terms cancel. (iii) f&#8339; = &frac12;&radic;(y/x) &minus; 1, '
      'f&#7527; = &frac12;&radic;(x/y) &rArr; &frac12;&radic;(xy) &minus; x + &frac12;&radic;(xy) = f. '
      '(iv) f&#8339; = 1/(x+y), f&#7527; = 1/(x+y) &minus; 1/y &rArr; 1 &minus; 1 = 0. All match the key.',
      390),
    q('u11_ex11_q5', 11, EX11, 'EX11', 5,
      'If u = x&sup2;(y &minus; x) + y&sup2;(x &minus; y), show that &part;u/&part;x + &part;u/&part;y = '
      '&minus;2(x &minus; y)&sup2;.',
      'Shown: sum = &minus;2x&sup2; + 4xy &minus; 2y&sup2; = &minus;2(x &minus; y)&sup2;',
      'Expand u = x&sup2;y &minus; x&sup3; + xy&sup2; &minus; y&sup3;. Then u&#8339; = 2xy &minus; 3x&sup2; + '
      'y&sup2; and u&#7527; = x&sup2; + 2xy &minus; 3y&sup2;; adding gives &minus;2x&sup2; + 4xy &minus; '
      '2y&sup2; = &minus;2(x &minus; y)&sup2;.',
      390),
    q('u11_ex11_q6', 11, EX11, 'EX11', 6,
      'If u = tan&#8315;&sup1;((x&sup3; + y&sup3;)/(x &minus; y)), prove that x &part;u/&part;x + '
      'y &part;u/&part;y = sin 2u.',
      'Shown: x u&#8339; + y u&#7527; = 2 tan u/sec&sup2;u = sin 2u',
      'w = (x&sup3; + y&sup3;)/(x &minus; y) is homogeneous of degree 2, so Euler gives x w&#8339; + '
      'y w&#7527; = 2w. With w = tan u, w&#8339; = sec&sup2;u &middot; u&#8339; (and likewise in y), hence '
      'sec&sup2;u (x u&#8339; + y u&#7527;) = 2 tan u, i.e. x u&#8339; + y u&#7527; = 2 sin u cos u = sin 2u.',
      390),
    q('u11_ex11_q7', 11, EX11, 'EX11', 7,
      'Use the MAPLE command &gt;diff to partial differentiate with respect to x and y: '
      '(i) x&sup2;y + xy + xy&sup2; &nbsp; (ii) y + x cos(y) &nbsp; (iii) (x + &radic;x)/(y + &radic;y)',
      '(i) &part;/&part;x = 2xy + y + y&sup2;, &part;/&part;y = x&sup2; + x + 2xy &nbsp; (ii) cos y, '
      '1 &minus; x sin y &nbsp; (iii) (1 + 1/(2&radic;x))/(y + &radic;y), &minus;(x + &radic;x)(1 + '
      '1/(2&radic;y))/(y + &radic;y)&sup2;',
      'MAPLE session: &gt; f := x^2*y + x*y + x*y^2; then &gt; diff(f, x); and &gt; diff(f, y); give the pair in '
      '(i). For (ii) &gt; f := y + x*cos(y); gives cos(y) and 1 &minus; x*sin(y). For (iii) '
      '&gt; f := (x + sqrt(x))/(y + sqrt(y)); gives (2&radic;x + 1)/(2&radic;x(y + &radic;y)) in x and '
      '&minus;(x + &radic;x)(2&radic;y + 1)/(2&radic;y(y + &radic;y)&sup2;) in y. Matches the key&#39;s commands.',
      390),
]

REV11 = 'Review Exercise 11'
SOLVED += [
    q('u11_rev11_q1', 11, REV11, 'REV11', 1,
      'Tick the correct answer: (i) f = e^(xy): f&#8339;/f&#7527; = ? &nbsp; (ii) surface area of a cube is a '
      'function of how many variables? &nbsp; (iii) g = cos(x/y): g&#7527;/g&#8339; = ? &nbsp; (iv) degree of '
      'homogeneity of tan(2x/(3y))? &nbsp; (v) P = 2(x + y): sum of the partial derivatives = ? &nbsp; '
      '(vi) z homogeneous of degree 0: x z&#8339; + y z&#7527; = ? &nbsp; (vii) area of a trapezium is a function '
      'of how many variables? &nbsp; (viii) w homogeneous of degree 2/3: u w&#7524; + v w&#7525; = ? &nbsp; '
      '(ix) z = f(u/v) of degree 0: v &part;z/&part;v = ? &nbsp; (x) f, g homogeneous of degrees 2 and 3: degree '
      'of f/g = ?',
      '(i) c &nbsp; (ii) a &nbsp; (iii) a &nbsp; (iv) d &nbsp; (v) d &nbsp; (vi) c &nbsp; (vii) c &nbsp; '
      '(viii) d &nbsp; (ix) c &nbsp; (x) d',
      '(i) y e^(xy)/(x e^(xy)) = y/x. (ii) S = 6s&sup2; uses the single edge s. (iii) (x sin(x/y)/y&sup2;)/'
      '(&minus;sin(x/y)/y) = &minus;x/y. (iv) argument degree 0. (v) 2 + 2 = 4. (vi) Euler with n = 0. '
      '(vii) A = &frac12;(a + b)h uses three lengths. (viii) Euler with n = 2/3 gives (2/3)w. (ix) u z&#7524; + '
      'v z&#7525; = 0 with z&#7524; = f&#8242;/v, z&#7525; = &minus;u f&#8242;/v&sup2; &rArr; v z&#7525; = '
      '&minus;u z&#7524;. (x) t&sup2;/t&sup3; = t&#8315;&sup1;. All match the key.',
      390),
    q('u11_rev11_q2', 11, REV11, 'REV11', 2,
      'Let f(x, y) = xy and g(x, y) = &frac12;xy be the homogeneous functions for the areas of rectangle and '
      'triangle. Are f + g, f &minus; g, fg and f/g homogeneous? If yes, what are their degrees?',
      'All homogeneous: f + g degree 2, f &minus; g degree 2, fg degree 4, f/g degree 0',
      'f + g = (3/2)xy and f &minus; g = &frac12;xy scale as t&sup2;; fg = &frac12;x&sup2;y&sup2; scales as '
      't&#8308;; f/g = 2 is constant, i.e. t&#8304;. Sums, products and quotients of homogeneous functions of '
      'equal degree (for + and &minus;) combine degrees additively.',
      391),
    q('u11_rev11_q3', 11, REV11, 'REV11', 3,
      'Verify Euler&#39;s theorem for the function z = &radic;(x&sup2; + y&sup2;).',
      'x z&#8339; + y z&#7527; = z (degree 1)',
      'z is homogeneous of degree 1. z&#8339; = x/&radic;(x&sup2; + y&sup2;) and z&#7527; = '
      'y/&radic;(x&sup2; + y&sup2;), so x z&#8339; + y z&#7527; = (x&sup2; + y&sup2;)/&radic;(x&sup2; + y&sup2;) '
      '= &radic;(x&sup2; + y&sup2;) = z = 1&middot;z.',
      391),
    q('u11_rev11_q4', 11, REV11, 'REV11', 4,
      'Given that z = g(x, y) is a homogeneous function of degree 3, show that x &part;z/&part;x + '
      'y &part;z/&part;y = 3z.',
      'Shown by differentiating g(tx, ty) = t&sup3;g(x, y) in t at t = 1',
      'Homogeneity gives g(tx, ty) = t&sup3;g(x, y). Differentiating with respect to t: '
      'x g&#8339;(tx, ty) + y g&#7527;(tx, ty) = 3t&sup2;g(x, y). Putting t = 1 yields x z&#8339; + y z&#7527; = 3z.',
      391),
    q('u11_rev11_q5', 11, REV11, 'REV11', 5,
      'Given that y = f(u, v) is a homogeneous function of degree &minus;3/2, show that u &part;y/&part;u + '
      'v &part;y/&part;v = &minus;(3/2)y.',
      'Shown by differentiating f(tu, tv) = t^(&minus;3/2)f(u, v) in t at t = 1',
      'f(tu, tv) = t^(&minus;3/2)f(u, v). Differentiating in t: u f&#7524;(tu, tv) + v f&#7525;(tu, tv) = '
      '&minus;(3/2)t^(&minus;5/2)f(u, v). At t = 1 this is u y&#7524; + v y&#7525; = &minus;(3/2)y.',
      391),
    q('u11_rev11_q6', 11, REV11, 'REV11', 6,
      'Given that u = sin&#8315;&sup1;((&radic;x &minus; &radic;y)/(&radic;x + &radic;y)), show that '
      'x &part;u/&part;x + y &part;u/&part;y = 0.',
      'Shown: cos u (x u&#8339; + y u&#7527;) = 0 &rArr; x u&#8339; + y u&#7527; = 0',
      'w = (&radic;x &minus; &radic;y)/(&radic;x + &radic;y) is homogeneous of degree 0, so Euler gives '
      'x w&#8339; + y w&#7527; = 0. Since sin u = w, w&#8339; = cos u &middot; u&#8339; and w&#7527; = '
      'cos u &middot; u&#7527;, hence cos u (x u&#8339; + y u&#7527;) = 0 and (cos u &ne; 0) the bracket '
      'vanishes.',
      391),
    q('u11_rev11_q7', 11, REV11, 'REV11', 7,
      'Given that u = sec&#8315;&sup1;((x&sup3; &minus; y&sup3;)/(x + y)), show that x &part;u/&part;x + '
      'y &part;u/&part;y = 2 cot u.',
      'Shown: sec u tan u (x u&#8339; + y u&#7527;) = 2 sec u &rArr; x u&#8339; + y u&#7527; = 2 cot u',
      'w = (x&sup3; &minus; y&sup3;)/(x + y) is homogeneous of degree 2, so x w&#8339; + y w&#7527; = 2w. With '
      'sec u = w, w&#8339; = sec u tan u &middot; u&#8339; (and likewise in y), giving sec u tan u '
      '(x u&#8339; + y u&#7527;) = 2 sec u, i.e. x u&#8339; + y u&#7527; = 2/tan u = 2 cot u.',
      391),
]

EX12_1 = 'Exercise 12.1'
SOLVED += [
    q('u12_ex121_q1', 12, EX12_1, 'EX12.1', 1,
      'Use the bisection method to find a real root of: (i) 2x&sup3; &minus; 2x &minus; 5, [1, 2], three '
      'iterations &nbsp; (ii) x&sup3; &minus; 2x &minus; 5, [1.5, 2.5], four iterations &nbsp; (iii) '
      'x&sup3; &minus; x + 1, [&minus;2, &minus;1], five iterations &nbsp; (iv) cos x, [1, 2], one decimal '
      'place (five iterations) &nbsp; (v) 3x &minus; e^x, [0, 1], three decimal places (eleven iterations) '
      '&nbsp; (vi) 3x &minus; &radic;(1 + sin x), [0, 1], three decimal places (thirteen iterations)',
      '(i) 1.6250 &nbsp; (ii) 2.0625 &nbsp; (iii) &minus;1.34375 &nbsp; (iv) 1.59375 (&asymp; 1.6) &nbsp; '
      '(v) 0.61865 (&asymp; 0.619) &nbsp; (vi) 0.39197 (&asymp; 0.392)',
      'Halve the bracketing interval each step, keeping the half where f changes sign. (i) f(1) = &minus;5, '
      'f(2) = 7: midpoints 1.5 (&minus;), 1.75 (+), 1.625 (+). (ii) f(1.5) = &minus;4.625, f(2.5) = 5.625: '
      '2 (&minus;), 2.25 (+), 2.125 (+), 2.0625 (&minus;). (iii) f(&minus;2) = &minus;5, f(&minus;1) = 1: '
      '&minus;1.5 (&minus;), &minus;1.25 (+), &minus;1.375 (&minus;), &minus;1.3125 (+), &minus;1.34375 '
      '(&minus;). (iv) cos 1 &gt; 0, cos 2 &lt; 0: 1.5 (+), 1.75 (&minus;), 1.625 (&minus;), 1.5625 (+), '
      '1.59375 (&minus;). (v) f(0) = &minus;1, f(1) = +0.281718: signs &minus;,+,&plus;,&minus;,&minus;,'
      '&minus;,&minus;,&plus;,&plus;,&minus; at 0.5, 0.75, 0.625, 0.5625, 0.59375, 0.609375, 0.6171875, '
      '0.62109375, 0.619140625, 0.6181640625, giving x&#8321;&#8321; = 0.6186523. (vi) f(0) = &minus;1, '
      'f(1) = +1.642992: thirteen halvings end at x&#8321;&#8323; = 0.3919678. All match the key.',
      397),
    q('u12_ex121_q2', 12, EX12_1, 'EX12.1', 2,
      'Write the MAPLE command fsolve to find numerical solutions of: (i) 3x&#8308;y&sup2; = 17, '
      'x&sup2;y &minus; 5xy&sup2; &minus; 2y = 1 &nbsp; (ii) 3x&sup3; &minus; 27x + 3 &nbsp; (iii) '
      '3x&sup3; + 9x + 3 &nbsp; (iv) 2x&sup3; + 4x + 2',
      '(i) x = 3.155009739, y = 0.2391456167 &nbsp; (ii) &minus;3.054084215, 0.1112641576, 2.942820058 &nbsp; '
      '(iii) &minus;0.3221853546 &nbsp; (iv) &minus;0.4533976515',
      'MAPLE session: &gt; fsolve({3*x^4*y^2 = 17, x^2*y - 5*x*y^2 - 2*y = 1}, {x, y}); returns the pair in (i). '
      '&gt; fsolve(3*x^3 - 27*x + 3, x); lists the three real roots in (ii); &gt; fsolve(3*x^3 + 9*x + 3, x); '
      'and &gt; fsolve(2*x^3 + 4*x + 2, x); give the single real roots in (iii) and (iv). Matches the key.',
      397),
]

EX12_2 = 'Exercise 12.2'
SOLVED += [
    q('u12_ex122_q1', 12, EX12_2, 'EX12.2', 1,
      'Use the regula falsi method to find a root of x&sup3; &minus; 2x &minus; 5 = 0 on [2, 3] up to three '
      'iterations.',
      '2.0896',
      'f(2) = &minus;1, f(3) = 16. x&#8321; = (2&middot;16 + 3&middot;1)/17 = 2.058824, f = &minus;0.390793; '
      'x&#8322; = 2.081264, f = &minus;0.147206; x&#8323; = 2.089638. Matches the key.',
      400),
    q('u12_ex122_q2', 12, EX12_2, 'EX12.2', 2,
      'Use the regula falsi method to find a root of sin(2x) &minus; e^(x&minus;1) = 0 on [&minus;2, &minus;1] '
      'up to four iterations.',
      '&minus;1.6077',
      'f(&minus;2) = 0.707015, f(&minus;1) = &minus;1.044633. x&#8321; = &minus;1.596366 (f = &minus;0.023428), '
      'x&#8322; = &minus;1.609313 (f = +0.003371), x&#8323; = &minus;1.607672 (f = &minus;0.000022), '
      'x&#8324; = &minus;1.607693. Matches the key.',
      400),
    q('u12_ex122_q3', 12, EX12_2, 'EX12.2', 3,
      'Use the regula falsi method to find a root of x&#8308; &minus; x &minus; 10 = 0 on [1, 2] up to two '
      'decimal places.',
      '1.8554 (1.86 to two decimal places)',
      'f(1) = &minus;10, f(2) = 4. x&#8321; = 1.714286 (f = &minus;3.077885), x&#8322; = 1.838532 '
      '(f = &minus;0.412780), x&#8323; = 1.853635 (f = &minus;0.047800), x&#8324; = 1.855363. Matches the key.',
      400),
    q('u12_ex122_q4', 12, EX12_2, 'EX12.2', 4,
      'Use the regula falsi method to find a root of 3x + sin(x) &minus; e^x = 0 on [0, 1] up to three decimal '
      'places.',
      '0.36047 &asymp; 0.360 (key 0.3604)',
      'f(0) = &minus;1, f(1) = 1.123189. x&#8321; = 0.470989 (f = +0.264974), x&#8322; = 0.372331 '
      '(f = +0.029658), x&#8323; = 0.361607 (f = +0.002922), x&#8324; = 0.360553 (f = +0.000242), '
      'x&#8325; = 0.360466 (f &asymp; 0). Matches the key.',
      400),
    q('u12_ex122_q5', 12, EX12_2, 'EX12.2', 5,
      'Use the regula falsi method to find a root of 2 cos x &minus; x = 0 on [1, 2] up to five decimal places.',
      '1.02987 (key prints 1.02986, truncated)',
      'f(1) = 0.080605, f(2) = &minus;2.832294. x&#8321; = 1.027672 (f = +0.005949), x&#8322; = 1.029709 '
      '(f = +0.000421), x&#8323; = 1.029854, x&#8324; = 1.029864, x&#8325; = 1.029866. The exact root is '
      '1.0298665, which rounds to 1.02987 at five decimals; the key truncates to 1.02986.',
      400),
]

EX12_3 = 'Exercise 12.3'
SOLVED += [
    q('u12_ex123_q1', 12, EX12_3, 'EX12.3', 1,
      'Use Newton&#39;s Raphson method for f(x) = 2x&sup3; &minus; 2x &minus; 5 up to three iterations with '
      'initial guess x&#8320; = 2.',
      '1.600612',
      'f&prime; = 6x&sup2; &minus; 2. x&#8321; = 2 &minus; 7/22 = 1.681818; x&#8322; = 1.681818 &minus; '
      '1.150458/14.971074 = 1.604973; x&#8323; = 1.604973 &minus; 0.058675/13.455626 = 1.600612. Matches the key.',
      402),
    q('u12_ex123_q2', 12, EX12_3, 'EX12.3', 2,
      'Use Newton&#39;s Raphson method for f(x) = x&sup3; &minus; x &minus; 1 up to three iterations with '
      'initial guess x&#8320; = 1.',
      '1.325200',
      'f&prime; = 3x&sup2; &minus; 1. x&#8321; = 1 + 1/2 = 1.5; x&#8322; = 1.5 &minus; 0.875/5.75 = 1.347826; '
      'x&#8323; = 1.347826 &minus; 0.100682/4.449906 = 1.325200. Matches the key.',
      402),
    q('u12_ex123_q3', 12, EX12_3, 'EX12.3', 3,
      'Use Newton&#39;s Raphson method for f(x) = x&sup3; &minus; 2x &minus; 5 up to two iterations with '
      'initial guess x&#8320; = 1.',
      '4.765517',
      'f(1) = &minus;6 and f&prime;(1) = 1 give x&#8321; = 7; then f(7) = 324, f&prime;(7) = 145 give '
      'x&#8322; = 7 &minus; 324/145 = 4.765517. The guess x&#8320; = 1 is far from the root 2.0946, so two '
      'iterations land at 4.765517 &mdash; exactly the key&#39;s value.',
      402),
    q('u12_ex123_q4', 12, EX12_3, 'EX12.3', 4,
      'Use Newton&#39;s Raphson method for f(x) = 2 cos x &minus; x with x&#8320; = 0.',
      '1.0298665 (4 iterations)',
      'f&prime; = &minus;2 sin x &minus; 1. x&#8321; = 0 &minus; 2/(&minus;1) = 2; x&#8322; = 2 &minus; '
      '(&minus;2.832294)/(&minus;2.818595) = 0.995140; x&#8323; = 0.995140 + 0.034967 = 1.030107; '
      'x&#8324; = 1.030107 &minus; 0.000244 = 1.0298665. Matches the key.',
      402),
    q('u12_ex123_q5', 12, EX12_3, 'EX12.3', 5,
      'Use Newton&#39;s Raphson method for f(x) = 2^x &minus; x &minus; 1.7 with x&#8320; = 1.5.',
      '1.812497 (4 iterations)',
      'f&prime; = 2^x ln 2 &minus; 1. x&#8321; = 1.5 + 0.371573/0.960138 = 1.887000; x&#8322; = 1.887000 &minus; '
      '0.112020/1.563967 = 1.815375; x&#8323; = 1.815375 &minus; 0.004132/1.439536 = 1.812504; '
      'x&#8324; = 1.812497. Matches the key.',
      402),
    q('u12_ex123_q6', 12, EX12_3, 'EX12.3', 6,
      'Use Newton&#39;s Raphson method for f(x) = 3x &minus; e^x with x&#8320; = 0.',
      '0.619061 (4 iterations)',
      'f&prime; = 3 &minus; e^x. x&#8321; = 0 + 1/2 = 0.5; x&#8322; = 0.5 + 0.148721/1.351279 = 0.610060; '
      'x&#8323; = 0.610060 + 0.010362/1.159459 = 0.618997; x&#8324; = 0.619061. Matches the key.',
      402),
    q('u12_ex123_q7', 12, EX12_3, 'EX12.3', 7,
      'Use Newton&#39;s Raphson method for f(x) = 3x &minus; &radic;(1 + sin x) with x&#8320; = 1.',
      '0.391847 (4 iterations)',
      'f&prime; = 3 &minus; cos x/(2&radic;(1 + sin x)). x&#8321; = 1 &minus; 1.642992/2.800921 = 0.413410; '
      'x&#8322; = 0.413410 &minus; 0.056287/2.613255 = 0.391871; x&#8323; = 0.391871 &minus; 0.000063/2.606907 = '
      '0.391847; x&#8324; = 0.391847. Matches the key.',
      402),
]

EX12_4 = 'Exercise 12.4'
SOLVED += [
    q('u12_ex124_q1', 12, EX12_4, 'EX12.4', 1,
      'Evaluate by the trapezoidal rule: (i) &int;&#8320;&sup2; e^x dx, 6 intervals &nbsp; (ii) '
      '&int;&#8321;&sup3; dx/&radic;x, 5 intervals &nbsp; (iii) &int;&#8320;^(&pi;/2) sin x dx, 7 intervals '
      '&nbsp; (iv) &int;&#8320;^1.4 e^(&minus;x&sup2;) dx, 5 intervals',
      '(i) 6.448105 &nbsp; (ii) 1.469424 &nbsp; (iii) 0.995800 &nbsp; (iv) 0.841370',
      'T = (h/2)[y&#8320; + 2(interior ordinates) + y&#8345;. (i) h = 1/3, ordinates '
      '1, 1.3956124, 1.9477340, 2.7182818, 3.7936679, 5.2944901, 7.3890561. (ii) h = 0.4, ordinates 1, '
      '0.8451543, 0.7453560, 0.6741999, 0.6201737, 0.5773503. (iii) h = &pi;/14, ordinates 0, 0.2225209, '
      '0.4338837, 0.6234900, 0.7818315, 0.9009689, 0.9749279, 1. (iv) h = 0.28, ordinates 1, 0.9245892, '
      '0.7308073, 0.4938058, 0.2852549, 0.1408584. All match the key.',
      411),
    q('u12_ex124_q2', 12, EX12_4, 'EX12.4', 2,
      'Evaluate by Simpson&#39;s 1/3 rule: (i) &int;&#8322;&sup3; (4x&sup2; + 6)dx, 4 intervals &nbsp; '
      '(ii) &int;&#8320;&sup2; e^(&minus;x) dx, 6 intervals &nbsp; (iii) &int;&#8320;^(&pi;/3) &radic;(sin x) dx, '
      '6 intervals &nbsp; (iv) &int;&#8320;&sup1; 2/(1 + x&sup2;) dx, 8 intervals',
      '(i) 31.3333 &nbsp; (ii) 0.864723 &nbsp; (iii) 0.680676 &nbsp; (iv) 1.570796',
      'S = (h/3)[y&#8320; + 4(odds) + 2(evens) + y&#8345;. (i) The rule is exact for a quadratic: '
      '(4x&sup3;/3 + 6x) from 2 to 3 = 54 &minus; 22.666667 (the printed upper limit &minus;3 is a misprint for 3). '
      '(ii) h = 1/3, ordinates 1, 0.7165313, 0.5134171, 0.3678794, 0.2635971, 0.1888756, 0.1353353. '
      '(iii) h = &pi;/18, ordinates 0, 0.4167112, 0.5848249, 0.7071068, 0.8017403, 0.8752396, 0.9306049. '
      '(iv) h = 0.125, ordinates 2, 1.9692308, 1.8823529, 1.7534247, 1.6, 1.4382022, 1.28, 1.1327434, 1 '
      '(the value is &pi;/2). All match the key.',
      411),
    q('u12_ex124_q3', 12, EX12_4, 'EX12.4', 3,
      'Evaluate by Simpson&#39;s 3/8 rule: (i) &int;&#8321;&sup3; &radic;x dx, 6 intervals &nbsp; (ii) '
      '&int;&#8321;&#8310; (ln x)/x dx, 3 sub-intervals &nbsp; (iii) &int;&#8320;&sup2; e^(2x)/(1 + x&sup2;) dx, '
      '9 sub-intervals &nbsp; (iv) &int;&#8320;^(&pi;/4) sin x dx, 6 sub-intervals',
      '(i) 2.797389759 &nbsp; (ii) 1.51075995 &nbsp; (iii) 8.777054 &nbsp; (iv) 0.292894',
      'S = (3h/8)[y&#8320; + 3y&#8321; + 3y&#8322; + 2y&#8323; + 3y&#8324; + 3y&#8325; + 2y&#8326; + &hellip; + '
      'y&#8345;. (i) h = 1/3, ordinates 1, 1.1547005, 1.2909944, 1.4142136, 1.5275252, 1.6329932, 1.7320508. '
      '(ii) h = 5/3, ordinates 0, 0.3678110, 0.3383855, 0.2986266. (iii) h = 2/9, ordinates 1, 1.4862292, '
      '2.0310506, 2.6264533, 3.3051020, 4.1294093, 5.1810798, 6.5639993, 8.4136973, 10.9196300. '
      '(iv) h = &pi;/24, ordinates 0, 0.1305262, 0.2588190, 0.3826834, 0.5, 0.6087614, 0.7071068. All match the key.',
      411),
    q('u12_ex124_q4', 12, EX12_4, 'EX12.4', 4,
      'Write the MAPLE command Trapezoid / Simpson (ApproximateInt) for: (i) (x&sup2; &minus; 2)/2, x = 0..1, '
      'n = 10, trapezoidal &nbsp; (ii) &radic;(9 + x&sup2;), x = 0..4, n = 10, trapezoidal &nbsp; (iii) '
      '1/(x&sup2; + 4x + 3), x = 0..2, n = 10, Simpson &nbsp; (iv) e^(&minus;x&sup2;), x = 0..2, n = 10, Simpson',
      '(i) &minus;333/400 &nbsp; (ii) 14.9544232 &nbsp; (iii) 0.2938949 (key) &nbsp; (iv) 0.88208098',
      'Commands: &gt; ApproximateInt((x^2-2)/2, x = 0..1, method = trapezoid, partition = 10); etc. (i) h = 0.1 '
      'gives &minus;0.8325 = &minus;333/400. (ii) h = 0.4, ordinates 3, 3.0265492, 3.1048349, 3.2310989, 3.4, '
      '3.6055513, 3.8418745, 4.1036569, 4.3863424, 4.6861498, 5. (iii) composite Simpson with h = 0.2 gives '
      '0.2939172 while the key&#39;s 0.2938949 is the exact &frac12;ln(9/5) = 0.2938933 to 6 dp (adaptive '
      'evaluation) &mdash; difference 2&times;10&#8315;&#8309;. (iv) h = 0.2, ordinates 1, 0.9607894, 0.8521438, '
      '0.6976763, 0.5272924, 0.3678794, 0.2369278, 0.1408584, 0.0773047, 0.0391639, 0.0183156.',
      411),
]

REV12 = 'Review Exercise 12'
SOLVED += [
    q('u12_rev12_q1', 12, REV12, 'REV12', 1,
      'Select the correct option: (i) sign of f(a)f(b) when a root lies in [a, b]; (ii) the bisection '
      'approximation is which mean of the endpoints; (iii) false-position iteration formula; (iv) fastest '
      'method for a nonlinear equation; (v) Newton&#39;s method fails when f&prime; becomes; (vi) '
      'Newton&#39;s iteration formula; (vii) numerical integration evaluates a; (viii) trapezoidal sub-interval '
      'count is a multiple of; (ix) Simpson 1/3 sub-interval count is a multiple of; (x) fastest quadrature of '
      'the list.',
      '(i) b &nbsp; (ii) a &nbsp; (iii) d &nbsp; (iv) c &nbsp; (v) c &nbsp; (vi) d &nbsp; (vii) a &nbsp; '
      '(viii) b &nbsp; (ix) c &nbsp; (x) b',
      '(i) A sign change is required: f(a)f(b) &lt; 0. (ii) The midpoint is the arithmetic mean. (iii) '
      'x = (a f(b) &minus; b f(a))/(f(b) &minus; f(a)). (iv) Newton&#39;s quadratic convergence makes it fastest. '
      '(v) Division by f&prime; fails at f&prime; = 0. (vi) x&#8345;&#8330;&#8321; = x&#8345; &minus; '
      'f(x&#8345;)/f&prime;(x&#8345;). (vii) A definite integral. (viii) The trapezoidal rule accepts any n, i.e. '
      'a multiple of 1 &mdash; the key&#39;s c (= 2) is Simpson&#39;s requirement, key misprint. (ix) Simpson 1/3 '
      'needs an even number of sub-intervals. (x) Simpson 1/3 is the most accurate of the three. Key agrees '
      'except (viii).',
      411),
    q('u12_rev12_q2', 12, REV12, 'REV12', 2,
      'Using the bisection method find the root of cos x &minus; xe^x with a = 0 and b = 1, taking 5 iterations.',
      '0.53125',
      'f(0) = 1 &gt; 0, f(1) = &minus;2.177980 &lt; 0. Midpoints: 0.5 (f = +0.053222), 0.75 (&minus;0.856061), '
      '0.625 (&minus;0.356691), 0.5625 (&minus;0.141294), 0.53125. Matches the key.',
      412),
    q('u12_rev12_q3', 12, REV12, 'REV12', 3,
      'Find a root of 2e^x sin x = 1 by the false position method, correct to three decimal places with three '
      'iterations, taking [1, 2] as the interval.',
      '0.38156 &asymp; 0.382 (as the key; see explanation)',
      'f(x) = 2e^x sin x &minus; 1 has f(1) = 3.574710 and f(2) = 12.437699, both positive, so [1, 2] contains '
      'no root; applying the false-position formula mechanically as the book does gives x&#8321; = 0.596670 '
      '(f = 1.040861), x&#8322; = 0.430989 (f = 0.285709), x&#8323; = 0.381561 &mdash; the key&#39;s 0.38156. The '
      'genuine root of 2e^x sin x = 1 is &asymp; 0.3573 in [0, 1]; flagged in the solution file.',
      412),
    q('u12_rev12_q4', 12, REV12, 'REV12', 4,
      'Find the cube root of 12 using the Newton Raphson method assuming x&#8320; = 2.5.',
      '2.289',
      'f = x&sup3; &minus; 12, f&prime; = 3x&sup2;. x&#8321; = 2.5 &minus; 3.625/18.75 = 2.306667; '
      'x&#8322; = 2.306667 &minus; 0.273107/15.962133 = 2.289557; x&#8323; = 2.289557 &minus; 0.002021/15.726214 = '
      '2.289428 &asymp; 2.289. Matches the key.',
      412),
    q('u12_rev12_q5', 12, REV12, 'REV12', 5,
      'Solve &int;&#8320;&sup1; cos(x&sup2;) dx using the trapezoidal rule for n = 5.',
      '0.898911 &asymp; 0.898914 (key)',
      'h = 0.2 with ordinates cos(x&sup2;) = 1, 0.999200, 0.987213, 0.935897, 0.802095, 0.540302. '
      'T = 0.1[1 + 2(3.724405) + 0.540302] = 0.898911. Matches the key to the printed digits.',
      412),
    q('u12_rev12_q6', 12, REV12, 'REV12', 6,
      'Solve &int;_(&minus;2)^4 e^(x&sup2;) dx using Simpson&#39;s one-third as well as Simpson&#39;s '
      'three-eighth rule for n = 6.',
      'Simpson 1/3: 2972903.47 &nbsp; Simpson 3/8: 3341495.53 (key prints the 3/8 value)',
      'h = 1 with ordinates e^(x&sup2;) = 54.598150, 2.718282, 1, 2.718282, 54.598150, 8103.083928, '
      '8886110.520508. Simpson 1/3: (1/3)[y&#8320; + 4(y&#8321; + y&#8323; + y&#8325;) + 2(y&#8322; + y&#8324;) + '
      'y&#8326;] = 2972903.47. Simpson 3/8: (3/8)[y&#8320; + 3y&#8321; + 3y&#8322; + 2y&#8323; + 3y&#8324; + '
      '3y&#8325; + y&#8326;] = 3341495.53, the key&#39;s value.',
      412),
]


def build():
    solved_by_unit = {}
    for item in SOLVED:
        solved_by_unit.setdefault(item['chapter'], []).append(item)

    chapters = []
    for num, title, ps, pe, bs, be in UNITS:
        qs = solved_by_unit.get(num, [])
        chapters.append({
            'number': num, 'title': title, 'startPage': ps, 'endPage': pe,
            'bookStart': bs, 'bookEnd': be, 'totalQuestions': len(qs), 'questions': qs,
        })

    solved_pages = {}
    for item in SOLVED:
        solved_pages.setdefault(item['pdfPage'], []).append(item)

    pages_map = {}
    for p in range(1, TOTAL_PAGES + 1):
        chapter_number = None
        for num, _t, ps, pe, _bs, _be in UNITS:
            if ps <= p <= pe:
                chapter_number = num
                break
        pages_map[str(p)] = {
            'pdfPage': p,
            'bookPage': p - 4 if p >= 5 else None,
            'chapterNumber': chapter_number,
            'isFrontMatter': p <= 4,
            'hasExercise': p in solved_pages,
            'questions': solved_pages.get(p, []),
        }

    data = {
        'subjectId': 'math_xii',
        'subjectName': 'Mathematics',
        'gradeId': 'class_xii',
        'gradeName': 'Class XII (HSC Part II)',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': TOTAL_PAGES,
        'totalQuestionsSolved': len(SOLVED),
        'chapters': chapters,
        'pagesMap': pages_map,
    }
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    print('wrote', os.path.abspath(OUT), '| solved items:', len(SOLVED))


if __name__ == '__main__':
    build()
