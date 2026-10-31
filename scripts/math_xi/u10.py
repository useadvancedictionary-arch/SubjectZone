"""Unit 10 - Trigonometric Identities of Sum and Difference of Angles.

Book pp. 292-316, PDF pp. 296-320.  Exercise 10.1 PDF 303-304, Exercise 10.2
PDF 308, Exercise 10.3 PDF 314-315, Exercise 10.4 PDF 318, Review Exercise 10
PDF 319.  (PDF p. 320, book p. 316, is blank in the supplied PDF.)
"""
from .common import bq, mcq

U = 10
EX1 = 'Exercise 10.1'
EX2 = 'Exercise 10.2'
EX3 = 'Exercise 10.3'
EX4 = 'Exercise 10.4'
RE = 'Review Exercise 10'

ITEMS = []

# ============================================================ Exercise 10.1 (pdf 303-304)
ITEMS += [
    bq(U, EX1, 'EX10.1', '1(i)', 'Prove that: cos(360° + θ) = cos θ.',
       'cos(360° + θ) = cos θ.',
       'Use cos(A + B) = cos A cos B − sin A sin B with A = 360°, B = θ:<br>'
       'cos(360° + θ) = cos 360° cos θ − sin 360° sin θ = (1)cos θ − (0)sin θ = cos θ = R.H.S.', 303),
    bq(U, EX1, 'EX10.1', '1(ii)', 'Prove that: sin(180° + θ) = −sin θ.',
       'sin(180° + θ) = −sin θ.',
       'Use sin(A + B) = sin A cos B + cos A sin B with A = 180°, B = θ:<br>'
       'sin(180° + θ) = sin 180° cos θ + cos 180° sin θ = (0)cos θ + (−1)sin θ = −sin θ = R.H.S.', 303),
    bq(U, EX1, 'EX10.1', '1(iii)', 'Prove that: tan(180° − θ) = −tan θ.',
       'tan(180° − θ) = −tan θ.',
       'Use tan(A − B) = (tan A − tan B)/(1 + tan A tan B) with A = 180°, B = θ:<br>'
       'tan(180° − θ) = (tan 180° − tan θ)/(1 + tan 180° tan θ) = (0 − tan θ)/(1 + 0) = −tan θ = R.H.S.', 303),
    bq(U, EX1, 'EX10.1', '1(iv)', 'Prove that: sin(270° − θ) = −cos θ.',
       'sin(270° − θ) = −cos θ.',
       'Use sin(A − B) = sin A cos B − cos A sin B with A = 270°, B = θ:<br>'
       'sin(270° − θ) = sin 270° cos θ − cos 270° sin θ = (−1)cos θ − (0)sin θ = −cos θ = R.H.S.', 303),

    bq(U, EX1, 'EX10.1', '1(v)', 'Prove that: cot(270° + θ) = −tan θ.',
       'cot(270° + θ) = −tan θ.',
       'Write cot as cos/sin and expand both:<br>'
       'cos(270° + θ) = cos 270° cos θ − sin 270° sin θ = 0 − (−1)sin θ = sin θ,<br>'
       'sin(270° + θ) = sin 270° cos θ + cos 270° sin θ = −cos θ + 0 = −cos θ.<br>'
       'Hence cot(270° + θ) = sin θ/(−cos θ) = −tan θ = R.H.S.', 304),
    bq(U, EX1, 'EX10.1', '1(vi)', 'Prove that: cot(270° − θ) = tan θ.',
       'cot(270° − θ) = tan θ.',
       'cos(270° − θ) = cos 270° cos θ + sin 270° sin θ = 0 + (−1)sin θ = −sin θ,<br>'
       'sin(270° − θ) = sin 270° cos θ − cos 270° sin θ = −cos θ − 0 = −cos θ.<br>'
       'Hence cot(270° − θ) = (−sin θ)/(−cos θ) = tan θ = R.H.S.', 304),
    bq(U, EX1, 'EX10.1', '1(vii)', 'Prove that: cosec(360° − θ) = −cosec θ.',
       'cosec(360° − θ) = −cosec θ.',
       'sin(360° − θ) = sin 360° cos θ − cos 360° sin θ = 0 − (1)sin θ = −sin θ.<br>'
       'Therefore cosec(360° − θ) = 1/sin(360° − θ) = 1/(−sin θ) = −cosec θ = R.H.S.', 304),
    bq(U, EX1, 'EX10.1', '1(viii)', 'Prove that: sec(360° − θ) = sec θ.',
       'sec(360° − θ) = sec θ.',
       'cos(360° − θ) = cos 360° cos θ + sin 360° sin θ = (1)cos θ + 0 = cos θ.<br>'
       'Therefore sec(360° − θ) = 1/cos(360° − θ) = 1/cos θ = sec θ = R.H.S.', 304),

    bq(U, EX1, 'EX10.1', '2(i)', 'Evaluate: sin 150° cos 300° + sin 300° cos 150°.',
       '1', 'This is the expansion of sin(A + B) with A = 150°, B = 300°:<br>'
       'sin 150° cos 300° + sin 300° cos 150° = sin(150° + 300°) = sin 450° = sin(450° − 360°) = sin 90° = 1.', 304),
    bq(U, EX1, 'EX10.1', '2(ii)', 'Evaluate: cos 19° cos 11° − sin 19° sin 11°.',
       '√3/2', 'This is the expansion of cos(A + B) with A = 19°, B = 11°:<br>'
       'cos 19° cos 11° − sin 19° sin 11° = cos(19° + 11°) = cos 30° = √3/2.', 304),

    bq(U, EX1, 'EX10.1', '3(i)', 'Verify that: cos 75° = (√3 − 1)/(2√2).',
       'Verified; both sides equal (√6 − √2)/4 = (√3 − 1)/(2√2).',
       'cos 75° = cos(45° + 30°) = cos 45° cos 30° − sin 45° sin 30°<br>'
       '= (1/√2)(√3/2) − (1/√2)(1/2) = (√3 − 1)/(2√2). Hence the statement is true.', 304),
    bq(U, EX1, 'EX10.1', '3(ii)', 'Verify that: cos(180° + 45°) cos(180° − 45°) = 1/2.',
       'Verified; the product is 1/2.',
       'cos(180° + 45°) = −cos 45° = −1/√2 and cos(180° − 45°) = −cos 45° = −1/√2.<br>'
       'Product = (−1/√2)(−1/√2) = 1/2. (Directly: cos 225° cos 135° = (−√2/2)(−√2/2) = 1/2.)', 304),

    bq(U, EX1, 'EX10.1', '4(i)', 'Without using tables or calculator, find the value of sin 75°.',
       '(1 + √3)/(2√2) = (√6 + √2)/4',
       'sin 75° = sin(45° + 30°) = sin 45° cos 30° + cos 45° sin 30°<br>'
       '= (1/√2)(√3/2) + (1/√2)(1/2) = (√3 + 1)/(2√2) = (√6 + √2)/4.', 304),
    bq(U, EX1, 'EX10.1', '4(ii)', 'Without using tables or calculator, find the value of tan 105°.',
       '−2 − √3',
       'tan 105° = tan(60° + 45°) = (tan 60° + tan 45°)/(1 − tan 60° tan 45°)<br>'
       '= (√3 + 1)/(1 − √3) = −(√3 + 1)/(√3 − 1) = −(√3 + 1)²/2 = −(4 + 2√3)/2 = −2 − √3.', 304),
    bq(U, EX1, 'EX10.1', '4(iii)', 'Without using tables or calculator, find the value of cos 165°.',
       '(−1 − √3)/(2√2) = −(√6 + √2)/4',
       'cos 165° = cos(120° + 45°) = cos 120° cos 45° − sin 120° sin 45°<br>'
       '= (−1/2)(1/√2) − (√3/2)(1/√2) = (−1 − √3)/(2√2) = −(√6 + √2)/4.', 304),
    bq(U, EX1, 'EX10.1', '4(iv)', 'Without using tables or calculator, find the value of sin 255°.',
       '(−1 − √3)/(2√2) = −(√6 + √2)/4',
       'sin 255° = sin(180° + 75°) = −sin 75°<br>'
       '= −(√6 + √2)/4 = (−1 − √3)/(2√2). (Using sin 75° = sin(45° + 30°).)', 304),
    bq(U, EX1, 'EX10.1', '4(v)', 'Without using tables or calculator, find the value of tan(5π/12).',
       '2 + √3',
       '5π/12 = 75°. tan 75° = tan(45° + 30°) = (1 + 1/√3)/(1 − 1/√3)<br>'
       '= (√3 + 1)/(√3 − 1) = (√3 + 1)²/2 = (4 + 2√3)/2 = 2 + √3.', 304),
    bq(U, EX1, 'EX10.1', '4(vi)', 'Without using tables or calculator, find the value of cos(13π/12).',
       '(−1 − √3)/(2√2) = −(√6 + √2)/4',
       '13π/12 = 195° = 180° + 15°, so cos(13π/12) = −cos 15°.<br>'
       'cos 15° = cos(45° − 30°) = (1/√2)(√3/2) + (1/√2)(1/2) = (√3 + 1)/(2√2).<br>'
       'Hence cos(13π/12) = −(√3 + 1)/(2√2) = (−1 − √3)/(2√2).', 304),
    bq(U, EX1, 'EX10.1', '4(vii)', 'Without using tables or calculator, find the value of sin(23π/12).',
       '(1 − √3)/(2√2) = (√2 − √6)/4',
       '23π/12 = 345° = 360° − 15°, so sin(23π/12) = −sin 15°.<br>'
       'sin 15° = sin(45° − 30°) = (1/√2)(√3/2) − (1/√2)(1/2) = (√3 − 1)/(2√2).<br>'
       'Hence sin(23π/12) = −(√3 − 1)/(2√2) = (1 − √3)/(2√2).', 304),
    bq(U, EX1, 'EX10.1', '4(viii)', 'Without using tables or calculator, find the value of cos(25π/12).',
       '(1 + √3)/(2√2) = (√6 + √2)/4',
       '25π/12 = 375° = 360° + 15°, so cos(25π/12) = cos 15°.<br>'
       'cos 15° = cos(45° − 30°) = cos 45° cos 30° + sin 45° sin 30°<br>'
       '= (1/√2)(√3/2) + (1/√2)(1/2) = (√3 + 1)/(2√2).', 304),

    bq(U, EX1, 'EX10.1', '5(i)', 'Prove that: [sin(α + β) + sin(α − β)]/[cos(α + β) + cos(α − β)] = tan α.',
       'The identity is true.',
       'Expand both sums:<br>'
       'sin(α + β) + sin(α − β) = (sin α cos β + cos α sin β) + (sin α cos β − cos α sin β) = 2 sin α cos β,<br>'
       'cos(α + β) + cos(α − β) = (cos α cos β − sin α sin β) + (cos α cos β + sin α sin β) = 2 cos α cos β.<br>'
       'Therefore L.H.S. = (2 sin α cos β)/(2 cos α cos β) = sin α/cos α = tan α = R.H.S.', 304),
    bq(U, EX1, 'EX10.1', '5(ii)', 'Prove that: [cos(α + β) + cos(α − β)]/[sin(α + β) + sin(α − β)] = cot α.',
       'The identity is true.',
       'From the expansions, the numerator is 2 cos α cos β and the denominator is 2 sin α cos β:<br>'
       'cos(α + β) + cos(α − β) = 2 cos α cos β,<br>'
       'sin(α + β) + sin(α − β) = 2 sin α cos β.<br>'
       'Hence L.H.S. = (2 cos α cos β)/(2 sin α cos β) = cos α/sin α = cot α = R.H.S.', 304),

    bq(U, EX1, 'EX10.1', '6(i)', 'Prove that: sin(α + β) sin(α − β) = sin²α − sin²β.',
       'The identity is true.',
       'L.H.S. = (sin α cos β + cos α sin β)(sin α cos β − cos α sin β)<br>'
       '= sin²α cos²β − cos²α sin²β<br>'
       '= sin²α(1 − sin²β) − (1 − sin²α)sin²β<br>'
       '= sin²α − sin²α sin²β − sin²β + sin²α sin²β = sin²α − sin²β = R.H.S.', 304),
    bq(U, EX1, 'EX10.1', '6(ii)', 'Prove that: cos(α + β) cos(α − β) = cos²α − sin²β.',
       'The identity is true.',
       'L.H.S. = (cos α cos β − sin α sin β)(cos α cos β + sin α sin β)<br>'
       '= cos²α cos²β − sin²α sin²β<br>'
       '= cos²α(1 − sin²β) − (1 − cos²α)sin²β<br>'
       '= cos²α − cos²α sin²β − sin²β + cos²α sin²β = cos²α − sin²β = R.H.S.', 304),

    bq(U, EX1, 'EX10.1', '7(i)', 'Prove that: cos(α + β) + cos(α − β) = 2 cos α cos β.',
       'The identity is true.',
       'cos(α + β) = cos α cos β − sin α sin β and cos(α − β) = cos α cos β + sin α sin β.<br>'
       'Adding the two equations gives cos(α + β) + cos(α − β) = 2 cos α cos β = R.H.S.', 304),
    bq(U, EX1, 'EX10.1', '7(ii)', 'Prove that: cos α cos(β − α) − sin α sin(β − α) = cos β.',
       'The identity is true.',
       'The left side is the expansion of cos(α + (β − α)):<br>'
       'cos α cos(β − α) − sin α sin(β − α) = cos(α + β − α) = cos β = R.H.S.<br>'
       'Equivalently, expand cos(β − α) and sin(β − α): cos²α cos β + cos α sin α sin β − sin α sin β cos α + sin²α cos β = (cos²α + sin²α)cos β = cos β.', 304),

    bq(U, EX1, 'EX10.1', '8(i)',
       'If sin α = 12/13 and sin β = 3/5, where 0 < α < π/2 and 0 < β < π/2, then find cos(α + β).',
       '−16/65',
       'Because α and β are acute, cos α = √(1 − 144/169) = 5/13 and cos β = √(1 − 9/25) = 4/5.<br>'
       'cos(α + β) = cos α cos β − sin α sin β = (5/13)(4/5) − (12/13)(3/5) = 20/65 − 36/65 = −16/65.', 304),
    bq(U, EX1, 'EX10.1', '8(ii)',
       'If sin α = 12/13 and sin β = 3/5, where 0 < α < π/2 and 0 < β < π/2, then find tan(α + β).',
       '−63/16',
       'cos α = 5/13, cos β = 4/5. First sin(α + β) = sin α cos β + cos α sin β = 48/65 + 15/65 = 63/65, and from 8(i) cos(α + β) = −16/65.<br>'
       'tan(α + β) = sin(α + β)/cos(α + β) = (63/65)/(−16/65) = −63/16.', 304),
    bq(U, EX1, 'EX10.1', '8(iii)',
       'If sin α = 12/13 and sin β = 3/5, where 0 < α < π/2 and 0 < β < π/2, then find cot(α − β).',
       '56/33',
       'cos(α − β) = cos α cos β + sin α sin β = 20/65 + 36/65 = 56/65 and sin(α − β) = sin α cos β − cos α sin β = 48/65 − 15/65 = 33/65.<br>'
       'cot(α − β) = cos(α − β)/sin(α − β) = (56/65)/(33/65) = 56/33.', 304),
    bq(U, EX1, 'EX10.1', '8(iv)',
       'If sin α = 12/13 and sin β = 3/5, where 0 < α < π/2 and 0 < β < π/2, then find cos(α − β).',
       '56/65',
       'cos α = 5/13 and cos β = 4/5. cos(α − β) = cos α cos β + sin α sin β = (5/13)(4/5) + (12/13)(3/5) = 20/65 + 36/65 = 56/65.', 304),
    bq(U, EX1, 'EX10.1', '8(v)',
       'If sin α = 12/13 and sin β = 3/5, where 0 < α < π/2 and 0 < β < π/2, then find sin(α + β).',
       '63/65',
       'sin(α + β) = sin α cos β + cos α sin β, with cos α = 5/13 and cos β = 4/5:<br>'
       '= (12/13)(4/5) + (5/13)(3/5) = 48/65 + 15/65 = 63/65.', 304),
    bq(U, EX1, 'EX10.1', '8(vi)',
       'If sin α = 12/13 and sin β = 3/5, where 0 < α < π/2 and 0 < β < π/2, then find sin(α − β).',
       '33/65',
       'sin(α − β) = sin α cos β − cos α sin β = (12/13)(4/5) − (5/13)(3/5) = 48/65 − 15/65 = 33/65.', 304),
    bq(U, EX1, 'EX10.1', '8(vii)',
       'If sin α = 12/13 and sin β = 3/5, where 0 < α < π/2 and 0 < β < π/2, then find cot(α + β).',
       '−16/63',
       'From 8(i) and 8(v), cos(α + β) = −16/65 and sin(α + β) = 63/65.<br>'
       'cot(α + β) = cos(α + β)/sin(α + β) = (−16/65)/(63/65) = −16/63.', 304),
    bq(U, EX1, 'EX10.1', '8(viii)',
       'If sin α = 12/13 and sin β = 3/5, where 0 < α < π/2 and 0 < β < π/2, then find tan(α − β).',
       '33/56',
       'From 8(iii) and 8(iv), sin(α − β) = 33/65 and cos(α − β) = 56/65.<br>'
       'tan(α − β) = sin(α − β)/cos(α − β) = (33/65)/(56/65) = 33/56.', 304),
    bq(U, EX1, 'EX10.1', '8(ix)',
       'If sin α = 12/13 and sin β = 3/5, where 0 < α < π/2 and 0 < β < π/2, also find the quadrants in which the angles (α + β) and (α − β) lie.',
       'α + β lies in the 2nd quadrant; α − β lies in the 1st quadrant.',
       'sin(α + β) = 63/65 > 0 while cos(α + β) = −16/65 < 0, so α + β is in the 2nd quadrant.<br>'
       'sin(α − β) = 33/65 > 0 and cos(α − β) = 56/65 > 0, so α − β is in the 1st quadrant.', 304),
]

# ============================================================ Exercise 10.2 (pdf 308)
ITEMS += [
    bq(U, EX2, 'EX10.2', '1(i)', 'Generate all allied angles if θ = 60°.',
       'All angles of the form 90°n ± 60° (n ∈ ℤ): ±30°, ±60°, ±120°, ±150°, ±210°, ±240°, …',
       'Allied angles are n(90°) ± θ, n ∈ ℤ. For θ = 60°:<br>'
       'n = 0: ±60°; n = 1: 90° ± 60° = 30°, 150°; n = 2: 180° ± 60° = 120°, 240°;<br>'
       'n = 3: 270° ± 60° = 210°, 330°; n = −1: −30°, −150°; n = −2: −120°, −240°; and so on.<br>'
       'Hence the allied angles are ±30°, ±60°, ±120°, ±150°, ±210°, ±240°, ±300°, ±330°, …<br>'
       '(The printed key lists the first few only: ±30°, ±60°, ±120°, ±150°, ±240°, ….)', 308),
    bq(U, EX2, 'EX10.2', '1(ii)', 'Generate all allied angles if θ = 50°.',
       'All angles of the form 90°n ± 50° (n ∈ ℤ): ±40°, ±50°, ±130°, ±140°, ±220°, ±230°, …',
       'For θ = 50°:<br>'
       'n = 0: ±50°; n = 1: 90° ± 50° = 40°, 140°; n = 2: 180° ± 50° = 130°, 230°;<br>'
       'n = 3: 270° ± 50° = 220°, 320°; n = −1: −40°, −140°; n = −2: −130°, −230°; and so on.<br>'
       'Hence the allied angles are ±40°, ±50°, ±130°, ±140°, ±220°, ±230°, ±310°, ±320°, …<br>'
       '(The printed key lists the first few only: ±40°, ±50°, ±130°, ±140°, ±230°, ….)', 308),

    bq(U, EX2, 'EX10.2', '2(i)',
       'Show that: sin(90° − θ)/cosec(90° − θ) + cos(90° − θ)/sec(90° − θ) = 1.',
       'The identity is true.',
       'Using co-ratios: sin(90° − θ) = cos θ, cosec(90° − θ) = sec θ, cos(90° − θ) = sin θ, sec(90° − θ) = cosec θ.<br>'
       'L.H.S. = cos θ/sec θ + sin θ/cosec θ = cos θ · cos θ + sin θ · sin θ = cos²θ + sin²θ = 1 = R.H.S.', 308),
    bq(U, EX2, 'EX10.2', '2(ii)',
       'Show that: sin²2° + sin²3° + sin²87° + sin²88° = 2.',
       'The identity is true.',
       'Since sin(90° − θ) = cos θ, sin 87° = cos 3° and sin 88° = cos 2°.<br>'
       'L.H.S. = (sin²2° + cos²2°) + (sin²3° + cos²3°) = 1 + 1 = 2 = R.H.S.', 308),

    bq(U, EX2, 'EX10.2', '3(i)', 'Evaluate without using calculator: sin 675°.',
       '−1/√2',
       'Reduce the angle modulo 360°: 675° − 360° = 315°, so sin 675° = sin 315°.<br>'
       '315° = 360° − 45°, hence sin 315° = −sin 45° = −1/√2.', 308),
    bq(U, EX2, 'EX10.2', '3(ii)', 'Evaluate without using calculator: tan(25π/6).',
       '1/√3',
       '25π/6 = 4π + π/6, and tangent has period π:<br>'
       'tan(25π/6) = tan(4π + π/6) = tan(π/6) = 1/√3.', 308),
    bq(U, EX2, 'EX10.2', '3(iii)', 'Evaluate without using calculator: cosec(2130°).',
       '−2',
       '2130° − 5(360°) = 2130° − 1800° = 330°, so sin 2130° = sin 330° = −sin 30° = −1/2.<br>'
       'Hence cosec 2130° = 1/sin 2130° = 1/(−1/2) = −2.', 308),
    bq(U, EX2, 'EX10.2', '3(iv)', 'Evaluate without using calculator: sec 55°/cosec 35° + sin 48°/cos 42°.',
       '2',
       'sec 55° = cosec(90° − 55°) = cosec 35°, so sec 55°/cosec 35° = 1.<br>'
       'sin 48° = cos(90° − 48°) = cos 42°, so sin 48°/cos 42° = 1.<br>'
       'Therefore the expression equals 1 + 1 = 2.', 308),
    bq(U, EX2, 'EX10.2', '3(v)',
       'Evaluate without using calculator: 2 sin 56°/cos 34° − cot 37°/tan 53° − √2 sin 45°.',
       '0',
       'sin 56° = cos 34°, so 2 sin 56°/cos 34° = 2.<br>'
       'cot 37° = tan(90° − 37°) = tan 53°, so cot 37°/tan 53° = 1.<br>'
       '√2 sin 45° = √2 · (1/√2) = 1.<br>'
       'Hence the expression = 2 − 1 − 1 = 0.', 308),
    bq(U, EX2, 'EX10.2', '3(vi)',
       'Evaluate without using calculator: cos 1° + cos 2° + cos 3° + … + cos 180°.',
       '−1',
       'Pair each term with its supplement: cos θ + cos(180° − θ) = cos θ − cos θ = 0.<br>'
       'The pairs (1°, 179°), (2°, 178°), …, (89°, 91°) all cancel, leaving cos 90° + cos 180° = 0 + (−1) = −1.<br>'
       'Printed key gives (vi) 1; the correct value is −1 (the key has interchanged the answers of (vi) and (vii)).', 308),
    bq(U, EX2, 'EX10.2', '3(vii)',
       'Evaluate without using calculator: tan 1° · tan 2° · tan 3° · … · tan 89°.',
       '1',
       'For each θ, tan(90° − θ) = cot θ, so tan θ · tan(90° − θ) = tan θ · cot θ = 1.<br>'
       'Pairing 1° with 89°, 2° with 88°, …, 44° with 46° gives 44 factors equal to 1, and the middle factor is tan 45° = 1.<br>'
       'Hence the product is 1. Printed key gives (vii) −1; the correct value is 1 (the key has interchanged the answers of (vi) and (vii)).', 308),

    bq(U, EX2, 'EX10.2', '4(i)', 'Show that: cos(45° − θ) = (1/√2)(cos θ + sin θ).',
       'The identity is true.',
       'cos(45° − θ) = cos 45° cos θ + sin 45° sin θ<br>'
       '= (1/√2)cos θ + (1/√2)sin θ = (1/√2)(cos θ + sin θ) = R.H.S.', 308),
    bq(U, EX2, 'EX10.2', '4(ii)', 'Show that: tan(45° + θ) tan(45° − θ) = 1.',
       'The identity is true.',
       'tan(45° + θ) = (1 + tan θ)/(1 − tan θ) and tan(45° − θ) = (1 − tan θ)/(1 + tan θ).<br>'
       'Their product is [(1 + tan θ)(1 − tan θ)]/[(1 − tan θ)(1 + tan θ)] = 1 = R.H.S.', 308),

    bq(U, EX2, 'EX10.2', '5(i)', 'Express 15 sin θ + 8 cos θ in the form r sin(θ + φ), where θ and φ are in the first quadrant.',
       '17 sin(θ + φ), where cos φ = 15/17 and sin φ = 8/17.',
       'Write 15 = r cos φ and 8 = r sin φ. Squaring and adding: r² = 15² + 8² = 225 + 64 = 289, so r = 17.<br>'
       'Then cos φ = 15/17 and sin φ = 8/17 (φ acute).<br>'
       '15 sin θ + 8 cos θ = r sin θ cos φ + r cos θ sin φ = r sin(θ + φ) = 17 sin(θ + φ).', 308),
    bq(U, EX2, 'EX10.2', '5(ii)',
       'Express (√3/2) sin θ + (1/2) cos θ in the form r sin(θ + φ), where θ and φ are in the first quadrant.',
       'sin(θ + φ), where cos φ = √3/2 and sin φ = 1/2 (φ = 30°).',
       'Here a = √3/2 and b = 1/2, so r = √(3/4 + 1/4) = 1.<br>'
       'cos φ = √3/2 and sin φ = 1/2, hence φ = 30°.<br>'
       '(√3/2) sin θ + (1/2) cos θ = sin θ cos 30° + cos θ sin 30° = sin(θ + 30°) = sin(θ + φ).', 308),
    bq(U, EX2, 'EX10.2', '5(iii)',
       'Express sin θ + cos θ in the form r sin(θ + φ), where θ and φ are in the first quadrant.',
       '√2 sin(θ + φ), where cos φ = 1/√2 and sin φ = 1/√2 (φ = 45°).',
       'a = 1, b = 1, so r = √(1² + 1²) = √2; cos φ = 1/√2 and sin φ = 1/√2, giving φ = 45°.<br>'
       'sin θ + cos θ = √2[(1/√2)sin θ + (1/√2)cos θ] = √2 sin(θ + 45°) = √2 sin(θ + φ).', 308),

    bq(U, EX2, 'EX10.2', '6', 'Prove that: tan α/cot(90° − α) + cos(90° − α)/sin α = 2.',
       'The identity is true.',
       'cot(90° − α) = tan α and cos(90° − α) = sin α.<br>'
       'L.H.S. = tan α/tan α + sin α/sin α = 1 + 1 = 2 = R.H.S.', 308),

    bq(U, EX2, 'EX10.2', '7(i)',
       'If A + B + C = 180°, prove that: tan A + tan B + tan C = tan A tan B tan C.',
       'The identity is true.',
       'Since A + B = 180° − C, tan(A + B) = tan(180° − C) = −tan C.<br>'
       'But tan(A + B) = (tan A + tan B)/(1 − tan A tan B). Hence<br>'
       '(tan A + tan B)/(1 − tan A tan B) = −tan C<br>'
       '⇒ tan A + tan B = −tan C + tan A tan B tan C<br>'
       '⇒ tan A + tan B + tan C = tan A tan B tan C = R.H.S.', 308),
    bq(U, EX2, 'EX10.2', '7(ii)',
       'If A + B + C = 180°, prove that: cos((B + C)/2) = sin(A/2).',
       'The identity is true.',
       'From A + B + C = 180°, B + C = 180° − A, so (B + C)/2 = 90° − A/2.<br>'
       'cos(90° − A/2) = sin(A/2) = R.H.S.', 308),
    bq(U, EX2, 'EX10.2', '7(iii)',
       'If A + B + C = 180°, prove that: tan(A/2) tan(B/2) + tan(B/2) tan(C/2) + tan(C/2) tan(A/2) = 1.',
       'The identity is true.',
       'A/2 + B/2 = 90° − C/2, so tan(A/2 + B/2) = tan(90° − C/2) = cot(C/2) = 1/tan(C/2).<br>'
       'Using the tangent addition formula:<br>'
       '[tan(A/2) + tan(B/2)]/[1 − tan(A/2)tan(B/2)] = 1/tan(C/2).<br>'
       'Cross-multiplying:<br>'
       'tan(C/2)[tan(A/2) + tan(B/2)] = 1 − tan(A/2)tan(B/2)<br>'
       '⇒ tan(A/2)tan(C/2) + tan(B/2)tan(C/2) + tan(A/2)tan(B/2) = 1 = R.H.S.', 308),
]

# ============================================================ Exercise 10.3 (pdf 314-315)
ITEMS += [
    bq(U, EX3, 'EX10.3', '1', 'Prove the identity: sin 2θ/sin θ − cos 2θ/cos θ = sec θ.',
       'The identity is true.',
       'L.H.S. = (2 sin θ cos θ)/sin θ − (2 cos²θ − 1)/cos θ<br>'
       '= 2 cos θ − 2 cos θ + 1/cos θ = 1/cos θ = sec θ = R.H.S.', 314),
    bq(U, EX3, 'EX10.3', '2', 'Prove the identity: sin 3α/sin α − cos 3α/cos α = 2.',
       'The identity is true.',
       'Use sin 3α = 3 sin α − 4 sin³α and cos 3α = 4 cos³α − 3 cos α:<br>'
       'L.H.S. = (3 − 4 sin²α) − (4 cos²α − 3) = 6 − 4(sin²α + cos²α) = 6 − 4 = 2 = R.H.S.', 314),
    bq(U, EX3, 'EX10.3', '3', 'Prove the identity: sin 4θ/sin 2θ − cos 4θ/cos 2θ = sec 2θ.',
       'The identity is true.',
       'sin 4θ = 2 sin 2θ cos 2θ and cos 4θ = 2 cos²2θ − 1.<br>'
       'L.H.S. = 2 cos 2θ − (2 cos²2θ − 1)/cos 2θ = 2 cos 2θ − 2 cos 2θ + 1/cos 2θ = sec 2θ = R.H.S.', 314),
    bq(U, EX3, 'EX10.3', '4', 'Prove the identity: cos 2α = (1 − tan²α)/(1 + tan²α).',
       'The identity is true.',
       'Write tan α = sin α/cos α and multiply numerator and denominator by cos²α:<br>'
       'R.H.S. = (cos²α − sin²α)/(cos²α + sin²α) = cos 2α/1 = cos 2α = L.H.S.', 314),
    bq(U, EX3, 'EX10.3', '5', 'Prove the identity: (cos(θ/2) − sin(θ/2))² = 1 − sin θ.',
       'The identity is true.',
       'L.H.S. = cos²(θ/2) + sin²(θ/2) − 2 sin(θ/2)cos(θ/2)<br>'
       '= 1 − sin θ = R.H.S. (using 2 sin x cos x = sin 2x with x = θ/2).', 314),
    bq(U, EX3, 'EX10.3', '6', 'Prove the identity: sin 2α = 2 tan α/(1 + tan²α).',
       'The identity is true.',
       'R.H.S. = [2(sin α/cos α)]/[1 + sin²α/cos²α]<br>'
       '= (2 sin α cos α)/(cos²α + sin²α) = 2 sin α cos α = sin 2α = L.H.S.', 314),
    bq(U, EX3, 'EX10.3', '7', 'Prove the identity: cos 2θ = (cot²θ − 1)/(cot²θ + 1).',
       'The identity is true.',
       'R.H.S. = (cos²θ/sin²θ − 1)/(cos²θ/sin²θ + 1)<br>'
       '= (cos²θ − sin²θ)/(cos²θ + sin²θ) = cos 2θ = L.H.S.', 314),
    bq(U, EX3, 'EX10.3', '8', 'Prove the identity: sin 4θ = 4 sin θ cos θ cos 2θ.',
       'The identity is true.',
       'R.H.S. = 2(2 sin θ cos θ)cos 2θ = 2 sin 2θ cos 2θ = sin 4θ = L.H.S.', 314),
    bq(U, EX3, 'EX10.3', '9', 'Prove the identity: cos 4θ = 8 cos⁴θ − 8 cos²θ + 1.',
       'The identity is true.',
       'cos 4θ = 2 cos²2θ − 1 = 2(2 cos²θ − 1)² − 1<br>'
       '= 2(4 cos⁴θ − 4 cos²θ + 1) − 1 = 8 cos⁴θ − 8 cos²θ + 1 = R.H.S.', 314),
    bq(U, EX3, 'EX10.3', '10', 'Prove the identity: tan(α/2) = cosec α − cot α.',
       'The identity is true.',
       'R.H.S. = 1/sin α − cos α/sin α = (1 − cos α)/sin α.<br>'
       'Now tan(α/2) = sin α/(1 + cos α); multiplying numerator and denominator by (1 − cos α) gives<br>'
       'sin α(1 − cos α)/(1 − cos²α) = (1 − cos α)/sin α.<br>'
       'Hence tan(α/2) = cosec α − cot α = R.H.S.', 314),
    bq(U, EX3, 'EX10.3', '11', 'Prove the identity: cosec²(θ/2) = 2 sec θ/(sec θ − 1).',
       'The identity is true.',
       'L.H.S. = 1/sin²(θ/2) = 2/(1 − cos θ).<br>'
       'Multiply numerator and denominator by sec θ:<br>'
       '2/(1 − cos θ) = 2 sec θ/(sec θ − 1) = R.H.S.', 314),
    bq(U, EX3, 'EX10.3', '12', 'Prove the identity: (sin θ + sin 2θ)/(1 + cos θ + cos 2θ) = tan θ.',
       'The identity is true.',
       'Numerator = sin θ + 2 sin θ cos θ = sin θ(1 + 2 cos θ).<br>'
       'Denominator = 1 + cos θ + (2 cos²θ − 1) = cos θ(1 + 2 cos θ).<br>'
       'L.H.S. = sin θ(1 + 2 cos θ)/[cos θ(1 + 2 cos θ)] = sin θ/cos θ = tan θ = R.H.S.', 314),
    bq(U, EX3, 'EX10.3', '13', 'Prove the identity: tan 4θ = 4 tan θ(1 − tan²θ)/(tan⁴θ − 6 tan²θ + 1).',
       'The identity is true.',
       'Let t = tan θ. tan 2θ = 2t/(1 − t²), so<br>'
       'tan 4θ = 2 tan 2θ/(1 − tan²2θ) = [2(2t/(1 − t²))]/[1 − 4t²/(1 − t²)²]<br>'
       '= [4t/(1 − t²)] · [(1 − t²)²/((1 − t²)² − 4t²)]<br>'
       '= 4t(1 − t²)/(1 − 2t² + t⁴ − 4t²) = 4 tan θ(1 − tan²θ)/(tan⁴θ − 6 tan²θ + 1) = R.H.S.', 314),
    bq(U, EX3, 'EX10.3', '14', 'Prove the identity: sec θ = (tan(θ/2) + cot(θ/2))/(cot(θ/2) − tan(θ/2)).',
       'The identity is true.',
       'Let x = tan(θ/2). Then<br>'
       'R.H.S. = (x + 1/x)/(1/x − x) = (x² + 1)/(1 − x²).<br>'
       'But cos θ = (1 − x²)/(1 + x²), so R.H.S. = 1/cos θ = sec θ = L.H.S.', 314),
    bq(U, EX3, 'EX10.3', '15', 'Prove the identity: cot 2θ = (cot θ − tan θ)/2.',
       'The identity is true.',
       'R.H.S. = [(cos θ/sin θ) − (sin θ/cos θ)]/2<br>'
       '= [(cos²θ − sin²θ)/(sin θ cos θ)]/2 = cos 2θ/(2 sin θ cos θ)<br>'
       '= cos 2θ/sin 2θ = cot 2θ = L.H.S.', 315),
    bq(U, EX3, 'EX10.3', '16', 'Prove the identity: tan²(θ/2) = (tan θ − sin θ)/(tan θ + sin θ).',
       'The identity is true.',
       'R.H.S. = [sin θ(1/cos θ − 1)]/[sin θ(1/cos θ + 1)]<br>'
       '= [(1 − cos θ)/cos θ]/[(1 + cos θ)/cos θ] = (1 − cos θ)/(1 + cos θ)<br>'
       '= tan²(θ/2) = L.H.S.', 315),

    bq(U, EX3, 'EX10.3', '17(i)', 'Evaluate: tan 22.5°.',
       '√2 − 1',
       'tan 22.5° = tan(45°/2) = (1 − cos 45°)/sin 45°<br>'
       '= (1 − 1/√2)/(1/√2) = (√2 − 1)/1 = √2 − 1.', 315),
    bq(U, EX3, 'EX10.3', '17(ii)', 'Evaluate: cos 15°.',
       '(√3 + 1)/(2√2) = (√6 + √2)/4',
       'cos 15° = cos(45° − 30°) = cos 45° cos 30° + sin 45° sin 30°<br>'
       '= (1/√2)(√3/2) + (1/√2)(1/2) = (√3 + 1)/(2√2).', 315),

    bq(U, EX3, 'EX10.3', '18(i)',
       'If cos θ = −4/5 and π/2 < θ < π, find sin(θ/2).',
       '3/√10',
       'θ is in the second quadrant, so sin θ = +3/5. Since π/2 < θ < π, we have π/4 < θ/2 < π/2, so sin(θ/2) > 0.<br>'
       'sin(θ/2) = √((1 − cos θ)/2) = √((1 + 4/5)/2) = √(9/10) = 3/√10.', 315),
    bq(U, EX3, 'EX10.3', '18(ii)',
       'If cos θ = −4/5 and π/2 < θ < π, find cos(θ/2).',
       '1/√10',
       'cos(θ/2) = √((1 + cos θ)/2) = √((1 − 4/5)/2) = √(1/10) = 1/√10 (positive because θ/2 is in the first quadrant).', 315),
    bq(U, EX3, 'EX10.3', '18(iii)',
       'If cos θ = −4/5 and π/2 < θ < π, find tan(θ/2).',
       '3',
       'sin θ = 3/5. tan(θ/2) = sin θ/(1 + cos θ) = (3/5)/(1 − 4/5) = (3/5)/(1/5) = 3.', 315),
    bq(U, EX3, 'EX10.3', '18(iv)',
       'If cos θ = −4/5 and π/2 < θ < π, find sin 2θ.',
       '−24/25',
       'sin 2θ = 2 sin θ cos θ = 2(3/5)(−4/5) = −24/25.', 315),
    bq(U, EX3, 'EX10.3', '18(v)',
       'If cos θ = −4/5 and π/2 < θ < π, find cos 2θ.',
       '7/25',
       'cos 2θ = 2 cos²θ − 1 = 2(16/25) − 1 = 32/25 − 25/25 = 7/25.', 315),
    bq(U, EX3, 'EX10.3', '18(vi)',
       'If cos θ = −4/5 and π/2 < θ < π, find tan 2θ.',
       '−24/7',
       'tan 2θ = sin 2θ/cos 2θ = (−24/25)/(7/25) = −24/7.', 315),

    bq(U, EX3, 'EX10.3', '19(i)',
       'If sin θ = 12/13, where 0 < θ < π/2, find sin(θ/2).',
       '2/√13',
       'θ is acute, so cos θ = √(1 − 144/169) = 5/13 and θ/2 is acute.<br>'
       'sin(θ/2) = √((1 − cos θ)/2) = √((1 − 5/13)/2) = √(4/13) = 2/√13.', 315),
    bq(U, EX3, 'EX10.3', '19(ii)',
       'If sin θ = 12/13, where 0 < θ < π/2, find cos(θ/2).',
       '3/√13',
       'cos θ = 5/13. cos(θ/2) = √((1 + cos θ)/2) = √((1 + 5/13)/2) = √(9/13) = 3/√13.', 315),
    bq(U, EX3, 'EX10.3', '19(iii)',
       'If sin θ = 12/13, where 0 < θ < π/2, find tan(θ/2).',
       '2/3',
       'tan(θ/2) = (1 − cos θ)/sin θ = (1 − 5/13)/(12/13) = (8/13)/(12/13) = 2/3.', 315),
    bq(U, EX3, 'EX10.3', '19(iv)',
       'If sin θ = 12/13, where 0 < θ < π/2, find sin 2θ.',
       '120/169',
       'sin 2θ = 2 sin θ cos θ = 2(12/13)(5/13) = 120/169.', 315),
    bq(U, EX3, 'EX10.3', '19(v)',
       'If sin θ = 12/13, where 0 < θ < π/2, find cos 2θ.',
       '−119/169',
       'cos 2θ = 1 − 2 sin²θ = 1 − 2(144/169) = 1 − 288/169 = −119/169.', 315),
    bq(U, EX3, 'EX10.3', '19(vi)',
       'If sin θ = 12/13, where 0 < θ < π/2, find tan 2θ.',
       '−120/119',
       'tan 2θ = sin 2θ/cos 2θ = (120/169)/(−119/169) = −120/119.', 315),

    bq(U, EX3, 'EX10.3', '20(i)',
       'If cos θ = 3/5, where 0 < θ < π/2, find sin 3θ.',
       '44/125',
       'sin θ = 4/5. sin 3θ = 3 sin θ − 4 sin³θ = 3(4/5) − 4(64/125)<br>'
       '= 12/5 − 256/125 = 300/125 − 256/125 = 44/125.', 315),
    bq(U, EX3, 'EX10.3', '20(ii)',
       'If cos θ = 3/5, where 0 < θ < π/2, find cos 3θ.',
       '−117/125',
       'cos 3θ = 4 cos³θ − 3 cos θ = 4(27/125) − 3(3/5)<br>'
       '= 108/125 − 9/5 = 108/125 − 225/125 = −117/125.', 315),
    bq(U, EX3, 'EX10.3', '20(iii)',
       'If cos θ = 3/5, where 0 < θ < π/2, find tan 3θ.',
       '−44/117',
       'tan 3θ = sin 3θ/cos 3θ = (44/125)/(−117/125) = −44/117.<br>'
       'Printed key gives −44/125, which is incorrect: it repeats the denominator 125 of sin 3θ instead of using cos 3θ = −117/125.', 315),
]

# ============================================================ Exercise 10.4 (pdf 318)
ITEMS += [
    bq(U, EX4, 'EX10.4', '1(i)', 'Express the following product as a sum or difference: 2 sin 6θ cos 3θ.',
       'sin 9θ + sin 3θ',
       'Use 2 sin A cos B = sin(A + B) + sin(A − B) with A = 6θ, B = 3θ:<br>'
       '2 sin 6θ cos 3θ = sin(6θ + 3θ) + sin(6θ − 3θ) = sin 9θ + sin 3θ.', 318),
    bq(U, EX4, 'EX10.4', '1(ii)', 'Express the following product as a sum or difference: cos 3θ sin 6θ.',
       '½(sin 9θ + sin 3θ)',
       'Use 2 cos A sin B = sin(A + B) − sin(A − B) with A = 3θ, B = 6θ:<br>'
       'cos 3θ sin 6θ = ½[sin(3θ + 6θ) − sin(3θ − 6θ)] = ½[sin 9θ − sin(−3θ)] = ½(sin 9θ + sin 3θ).', 318),
    bq(U, EX4, 'EX10.4', '1(iii)', 'Express the following product as a sum or difference: 2 sin(α − β) cos(α + β).',
       'sin 2α − sin 2β',
       'Use 2 sin A cos B = sin(A + B) + sin(A − B) with A = α − β, B = α + β:<br>'
       '2 sin(α − β)cos(α + β) = sin(2α) + sin(−2β) = sin 2α − sin 2β.', 318),
    bq(U, EX4, 'EX10.4', '1(iv)', 'Express the following product as a sum or difference: −2 sin((α + β)/2) sin((α − β)/2).',
       'cos α − cos β',
       'Use −2 sin A sin B = cos(A + B) − cos(A − B) with A = (α + β)/2, B = (α − β)/2:<br>'
       '−2 sin((α + β)/2)sin((α − β)/2) = cos α − cos β.', 318),
    bq(U, EX4, 'EX10.4', '1(v)', 'Express the following product as a sum or difference: sin(θ + 45°) sin(θ − 45°).',
       '−½ cos 2θ',
       'Use sin A sin B = ½[cos(A − B) − cos(A + B)] with A = θ + 45°, B = θ − 45°:<br>'
       'sin(θ + 45°)sin(θ − 45°) = ½[cos 90° − cos 2θ] = ½[0 − cos 2θ] = −½ cos 2θ.', 318),
    bq(U, EX4, 'EX10.4', '1(vi)',
       'Express the following product as a sum or difference: 2 cos(2θ + 60°) cos(2θ − 60°).',
       'cos 4θ − ½',
       'Use 2 cos A cos B = cos(A + B) + cos(A − B) with A = 2θ + 60°, B = 2θ − 60°:<br>'
       '2 cos(2θ + 60°)cos(2θ − 60°) = cos 4θ + cos 120° = cos 4θ − ½.', 318),

    bq(U, EX4, 'EX10.4', '2(i)', 'Express the following sum or difference as a product: sin 2α − sin 2β.',
       '2 cos(α + β) sin(α − β)',
       'Use sin u − sin v = 2 cos((u + v)/2) sin((u − v)/2) with u = 2α, v = 2β:<br>'
       'sin 2α − sin 2β = 2 cos(α + β) sin(α − β).', 318),
    bq(U, EX4, 'EX10.4', '2(ii)', 'Express the following sum or difference as a product: cos(5θ/2) + cos(3θ/2).',
       '2 cos 2θ cos(θ/2)',
       'Use cos u + cos v = 2 cos((u + v)/2) cos((u − v)/2) with u = 5θ/2, v = 3θ/2:<br>'
       'cos(5θ/2) + cos(3θ/2) = 2 cos(2θ) cos(θ/2).', 318),
    bq(U, EX4, 'EX10.4', '2(iii)', 'Express the following sum or difference as a product: cos 25° + cos 65°.',
       '2 cos 45° cos 20°',
       'cos 25° + cos 65° = 2 cos((25° + 65°)/2) cos((25° − 65°)/2) = 2 cos 45° cos(−20°) = 2 cos 45° cos 20°.', 318),
    bq(U, EX4, 'EX10.4', '2(iv)', 'Express the following sum or difference as a product: cos(θ + 30°) − cos(θ − 30°).',
       '−sin θ',
       'Use cos u − cos v = −2 sin((u + v)/2) sin((u − v)/2) with u = θ + 30°, v = θ − 30°:<br>'
       '= −2 sin θ sin 30° = −2 sin θ (1/2) = −sin θ.', 318),
    bq(U, EX4, 'EX10.4', '2(v)', 'Express the following sum or difference as a product: sin(π/2) − sin(π/4).',
       '2 cos(3π/8) sin(π/8)',
       'sin(π/2) − sin(π/4) = 2 cos((π/2 + π/4)/2) sin((π/2 − π/4)/2)<br>'
       '= 2 cos(3π/8) sin(π/8).', 318),
    bq(U, EX4, 'EX10.4', '2(vi)', 'Express the following sum or difference as a product: sin 2(θ + 40°) + sin 2(θ − 40°).',
       '2 sin 2θ cos 80°',
       'Use sin u + sin v = 2 sin((u + v)/2) cos((u − v)/2) with u = 2(θ + 40°), v = 2(θ − 40°):<br>'
       '= 2 sin(2θ) cos 80° = 2 sin 2θ cos 80°.', 318),

    bq(U, EX4, 'EX10.4', '3(i)', 'Prove the identity: (sin α − sin β)/(cos α + cos β) = tan((α − β)/2).',
       'The identity is true.',
       'sin α − sin β = 2 cos((α + β)/2) sin((α − β)/2) and cos α + cos β = 2 cos((α + β)/2) cos((α − β)/2).<br>'
       'L.H.S. = [2 cos((α + β)/2) sin((α − β)/2)]/[2 cos((α + β)/2) cos((α − β)/2)]<br>'
       '= sin((α − β)/2)/cos((α − β)/2) = tan((α − β)/2) = R.H.S.', 318),
    bq(U, EX4, 'EX10.4', '3(ii)',
       'Prove the identity: (sin α + sin β)/(sin α − sin β) = tan((α + β)/2) cot((α − β)/2).',
       'The identity is true.',
       'sin α + sin β = 2 sin((α + β)/2) cos((α − β)/2) and sin α − sin β = 2 cos((α + β)/2) sin((α − β)/2).<br>'
       'L.H.S. = [2 sin((α + β)/2) cos((α − β)/2)]/[2 cos((α + β)/2) sin((α − β)/2)]<br>'
       '= tan((α + β)/2) cot((α − β)/2) = R.H.S.', 318),
    bq(U, EX4, 'EX10.4', '3(iii)', 'Prove the identity: (sin 6θ + sin 4θ)/(cos 6θ + cos 4θ) = tan 5θ.',
       'The identity is true.',
       'sin 6θ + sin 4θ = 2 sin 5θ cos θ and cos 6θ + cos 4θ = 2 cos 5θ cos θ.<br>'
       'L.H.S. = (2 sin 5θ cos θ)/(2 cos 5θ cos θ) = tan 5θ = R.H.S.', 318),
    bq(U, EX4, 'EX10.4', '3(iv)',
       'Prove the identity: (sin 2θ + sin 4θ + sin 6θ + sin 8θ)/(cos 2θ + cos 4θ + cos 6θ + cos 8θ) = tan 5θ.',
       'The identity is true.',
       'Numerator = (sin 2θ + sin 8θ) + (sin 4θ + sin 6θ) = 2 sin 5θ cos 3θ + 2 sin 5θ cos θ<br>'
       '= 2 sin 5θ(cos 3θ + cos θ) = 2 sin 5θ (2 cos 2θ cos θ) = 4 sin 5θ cos 2θ cos θ.<br>'
       'Denominator = (cos 2θ + cos 8θ) + (cos 4θ + cos 6θ) = 2 cos 5θ cos 3θ + 2 cos 5θ cos θ<br>'
       '= 2 cos 5θ(cos 3θ + cos θ) = 4 cos 5θ cos 2θ cos θ.<br>'
       'Hence L.H.S. = (4 sin 5θ cos 2θ cos θ)/(4 cos 5θ cos 2θ cos θ) = tan 5θ = R.H.S.', 318),
    bq(U, EX4, 'EX10.4', '3(v)', 'Prove the identity: (sin α + sin 2α)/(cos α − cos 2α) = cot(α/2).',
       'The identity is true.',
       'Numerator = 2 sin(3α/2) cos(α/2).<br>'
       'Denominator = cos α − cos 2α = −2 sin(3α/2) sin(−α/2) = 2 sin(3α/2) sin(α/2).<br>'
       'L.H.S. = [2 sin(3α/2) cos(α/2)]/[2 sin(3α/2) sin(α/2)] = cos(α/2)/sin(α/2) = cot(α/2) = R.H.S.', 318),
    bq(U, EX4, 'EX10.4', '3(vi)',
       'Prove the identity: [sin(θ + φ) − 2 sin θ + sin(θ − φ)]/[cos(θ + φ) − 2 cos θ + cos(θ − φ)] = tan θ.',
       'The identity is true.',
       'Numerator = sin(θ + φ) + sin(θ − φ) − 2 sin θ = 2 sin θ cos φ − 2 sin θ = 2 sin θ(cos φ − 1).<br>'
       'Denominator = cos(θ + φ) + cos(θ − φ) − 2 cos θ = 2 cos θ cos φ − 2 cos θ = 2 cos θ(cos φ − 1).<br>'
       'L.H.S. = [2 sin θ(cos φ − 1)]/[2 cos θ(cos φ − 1)] = tan θ = R.H.S.', 318),

    bq(U, EX4, 'EX10.4', '4(i)', 'Evaluate: sin 20° sin 40° sin 60° sin 80°.',
       '3/16',
       'sin 60° = √3/2, so the product is (√3/2) sin 20° sin 40° sin 80°.<br>'
       'sin 20° sin 40° = ½[cos 20° − cos 60°] = ½[cos 20° − ½].<br>'
       'Hence sin 20° sin 40° sin 80° = ½ cos 20° sin 80° − ¼ sin 80°<br>'
       '= ¼[sin 100° + sin 60°] − ¼ sin 80° = ¼[sin 80° + √3/2] − ¼ sin 80° = √3/8.<br>'
       'Therefore the required product = (√3/2)(√3/8) = 3/16.', 318),
    bq(U, EX4, 'EX10.4', '4(ii)', 'Evaluate: cos 20° cos 40° cos 60° cos 80°.',
       '1/16',
       'cos 60° = ½, so the product is ½ cos 20° cos 40° cos 80°.<br>'
       'cos 20° cos 40° = ½[cos 60° + cos 20°] = ½[½ + cos 20°].<br>'
       'Hence cos 20° cos 40° cos 80° = ¼ cos 80° + ½ cos 20° cos 80°<br>'
       '= ¼ cos 80° + ¼[cos 100° + cos 60°] = ¼ cos 80° + ¼[−cos 80° + ½] = 1/8.<br>'
       'Therefore the required product = ½ · 1/8 = 1/16.', 318),

    bq(U, EX4, 'EX10.4', '5(i)', 'Show that: (cos 8° − sin 8°)/(cos 8° + sin 8°) = tan 37°.',
       'The identity is true.',
       'Divide numerator and denominator by cos 8°:<br>'
       'L.H.S. = (1 − tan 8°)/(1 + tan 8°) = tan(45° − 8°) = tan 37° = R.H.S.', 318),
    bq(U, EX4, 'EX10.4', '5(ii)', 'Show that: (cos 11° + sin 11°)/(cos 11° − sin 11°) = tan 56°.',
       'The identity is true.',
       'Divide numerator and denominator by cos 11°:<br>'
       'L.H.S. = (1 + tan 11°)/(1 − tan 11°) = tan(45° + 11°) = tan 56° = R.H.S.', 318),
    bq(U, EX4, 'EX10.4', '5(iii)', 'Show that: sin 50° − sin 70° + sin 10° = 0.',
       'The identity is true.',
       'sin 50° − sin 70° = 2 cos(60°) sin(−10°) = 2(1/2)(−sin 10°) = −sin 10°.<br>'
       'Therefore sin 50° − sin 70° + sin 10° = −sin 10° + sin 10° = 0 = R.H.S.', 318),
]

# ============================================================ Review Exercise 10 (pdf 319)
# PDF 319 (book p. 315) prints the review MCQs (i)-(xiii).  PDF 320 (book p. 316)
# is an empty page in the supplied PDF, yet the printed key on PDF 418 lists
# answers for (xiv)-(xvii); those four question stems and options are not
# present anywhere in this copy, so they cannot be transcribed.  For the record,
# the key gives: (xiv) (a) cos 5θ − cos 9θ; (xv) (a) 270° + θ;
# (xvi) (c) cos α; (xvii) (a) 0.
ITEMS += [
    mcq(U, RE, 'REV10', 'i', 'cos(α − β) is equal to:',
        ['cos α cos β + sin α sin β', 'cos α cos β − sin α sin β',
         'sin α cos β + cos α sin β', 'sin α cos β − cos α sin β'], 'a',
        'The cosine of a difference is cos(α − β) = cos α cos β + sin α sin β. The minus sign belongs to cos(α + β).', 319),
    mcq(U, RE, 'REV10', 'ii',
        'Angles associated with basic angles of measure θ to a right angle or its multiple are called:',
        ['Coterminal angles', 'Angles in standard positions', 'Allied angles', 'Obtuse angles'], 'c',
        'Allied angles are the angles of the form n(90°) ± θ (or nπ/2 ± θ); they differ from θ by a multiple of a right angle, which is exactly the definition given.', 319),
    mcq(U, RE, 'REV10', 'iii', 'sin(π/2 + θ) is equal to:',
        ['cos θ', 'sin θ', '−cos θ', '−sin θ'], 'a',
        'sin(π/2 + θ) = sin 90° cos θ + cos 90° sin θ = (1)cos θ + (0)sin θ = cos θ.', 319),
    mcq(U, RE, 'REV10', 'iv', 'cos(π − θ) is equal to:',
        ['sin θ', 'cos θ', '- sin θ', '- cos θ'], 'd',
        'cos(π − θ) = cos 180° cos θ + sin 180° sin θ = (−1)cos θ + 0 = −cos θ.', 319),
    mcq(U, RE, 'REV10', 'v', 'tan(π + θ) is equal to:',
        ['tan θ', '−cot θ', '- tan θ', 'cot θ'], 'a',
        'Tangent has period π, so tan(π + θ) = tan θ. (Expansion: (0 + tan θ)/(1 − 0·tan θ) = tan θ.)', 319),
    mcq(U, RE, 'REV10', 'vi', 'cos(2π + θ) is equal to:',
        ['sin θ', 'cos θ', '- sin θ', '- cos θ'], 'b',
        'Cosine has period 2π, so cos(2π + θ) = cos θ. (Expansion: cos 2π cos θ − sin 2π sin θ = cos θ.)', 319),
    mcq(U, RE, 'REV10', 'vii', 'sin 540° is equal to:',
        ['1', '0', '1/√2', '√3/2'], 'b',
        'sin 540° = sin(540° − 360°) = sin 180° = 0.', 319),
    mcq(U, RE, 'REV10', 'viii', 'sin(−300°) is equal to:',
        ['1', '√3/2', '0', '−1'], 'b',
        'sin(−300°) = −sin 300° = −sin(360° − 60°) = −(−sin 60°) = sin 60° = √3/2.', 319),
    mcq(U, RE, 'REV10', 'ix',
        'If α, β and γ are the angles of ΔABC, then sin(α + β) is equal to:',
        ['sin γ', '−sin γ', 'cos γ', '−cos γ'], 'a',
        'In ΔABC, α + β + γ = 180°, so α + β = 180° − γ. Hence sin(α + β) = sin(180° − γ) = sin γ.', 319),
    mcq(U, RE, 'REV10', 'x', 'cos 2α is equal to:',
        ['cos²α − sin²α', '2cos²α − 1', '1 − 2 sin²α', 'all of these'], 'd',
        'All three forms are valid: cos 2α = cos²α − sin²α = 2cos²α − 1 = 1 − 2sin²α, using sin²α + cos²α = 1.', 319),
    mcq(U, RE, 'REV10', 'xi', 'sin(α/2) is equal to:',
        ['±√((1 + sin α)/2)', '±√((1 − cos α)/2)', '±√((1 + cos α)/2)', '±√((1 − sin α)/2)'], 'b',
        'From cos α = 1 − 2sin²(α/2), we get sin²(α/2) = (1 − cos α)/2, so sin(α/2) = ±√((1 − cos α)/2). The sign is fixed by the quadrant of α/2.', 319),
    mcq(U, RE, 'REV10', 'xii', 'cos 3α is equal to:',
        ['3 cos α − 4 cos α', '3 cos³α + 4 cos α', '4 cos³α − 3 cos α', '4 cos³α + 4 cos α'], 'c',
        'cos 3α = 4cos³α − 3cos α, so option (c) is correct. The printed option (a) is misprinted as "3 cos α − 4 cos α" (the cube on the first cosine is missing); even read as 3cos α − 4cos³α it would be the formula for sin 3α with cos in place of sin, not cos 3α.', 319),
    mcq(U, RE, 'REV10', 'xiii', 'cos α − cos β =',
        ['2 sin((α + β)/2) cos((α − β)/2)', '2 cos((α + β)/2) sin((α − β)/2)',
         '2 cos((α + β)/2) cos((α − β)/2)', '−2 sin((α + β)/2) sin((α − β)/2)'], 'd',
        'Using cos u − cos v = −2 sin((u + v)/2) sin((u − v)/2) with u = α, v = β gives cos α − cos β = −2 sin((α + β)/2) sin((α − β)/2).', 319),
]
