"""Unit 11 - Application of Trigonometry (book pp. 317-336, PDF pp. 321-340)."""
from .common import bq, mcq

U = 11
EX1 = 'Exercise 11.1'
EX2 = 'Exercise 11.2'
EX3 = 'Exercise 11.3'
EX4 = 'Exercise 11.4'
RE11 = 'Review Exercise 11'

ITEMS = []

# ============================================================== Exercise 11.1 (pdf 323)
ITEMS += [
    bq(U, EX1, 'EX11.1', '1(i)', 'Solve the right angled triangle ABC in which γ = 90°, given a = 4 m, b = 3 m.',
       'c = 5 m, α ≈ 53°8′, β ≈ 36°52′.',
       'γ = 90°, so c is the hypotenuse and a, b are the legs. By Pythagoras: c = √(a<sup>2</sup> + b<sup>2</sup>) = √(4<sup>2</sup> + 3<sup>2</sup>) = √25 = 5 m. '
       'tan α = a/b = 4/3 = 1.3333 ⇒ α = tan<sup>−1</sup>(1.3333) = 53.13° = 53°8′. '
       'β = 90° − α = 90° − 53.13° = 36.87° = 36°52′. (Printed key: α = 53°7′, β = 36°53′.)', 323,
       'Right-angled triangle ABC with the right angle at C (γ = 90°); a = BC = 4 m, b = CA = 3 m, c = AB = 5 m.'),
    bq(U, EX1, 'EX11.1', '1(ii)', 'Solve the right angled triangle ABC in which γ = 90°, given a = 12 m, b = 5 m.',
       'c = 13 m, α ≈ 67°23′, β ≈ 22°37′.',
       'c = √(a<sup>2</sup> + b<sup>2</sup>) = √(12<sup>2</sup> + 5<sup>2</sup>) = √169 = 13 m. '
       'tan α = 12/5 = 2.4 ⇒ α = tan<sup>−1</sup>(2.4) = 67.38° = 67°23′. β = 90° − 67.38° = 22.62° = 22°37′. '
       '(Printed key: α = 67°22′, β = 22°38′.)', 323,
       'Right-angled triangle ABC, right angle at C; a = BC = 12 m, b = CA = 5 m, c = AB = 13 m.'),
    bq(U, EX1, 'EX11.1', '1(iii)', 'Solve the right angled triangle ABC in which γ = 90°, given a = 8 m, b = 6 m.',
       'c = 10 m, α ≈ 53°8′, β ≈ 36°52′.',
       'c = √(8<sup>2</sup> + 6<sup>2</sup>) = √100 = 10 m. tan α = 8/6 = 1.3333 ⇒ α = 53.13° = 53°8′; '
       'β = 90° − 53.13° = 36.87° = 36°52′. (Printed key: α = 53°7′, β = 36°53′.)', 323,
       'Right-angled triangle ABC, right angle at C; a = BC = 8 m, b = CA = 6 m, c = AB = 10 m.'),
    bq(U, EX1, 'EX11.1', '1(iv)', 'Solve the right angled triangle ABC in which γ = 90°, given c = 8 m, β = 42°30′.',
       'α = 47°30′, a ≈ 5.9 m, b ≈ 5.4 m.',
       'α = 180° − γ − β = 180° − 90° − 42°30′ = 47°30′. '
       'a = c sin α = 8 sin 47°30′ = 8(0.73728) = 5.898 ≈ 5.9 m. '
       'b = c cos α = 8 cos 47°30′ = 8(0.67559) = 5.405 ≈ 5.4 m. '
       'Check: a<sup>2</sup> + b<sup>2</sup> = 34.8 + 29.2 = 64 = c<sup>2</sup>.', 323,
       'Right-angled triangle ABC, right angle at C; c = AB = 8 m, β = 42°30′ at B, α = 47°30′ at A.'),
    bq(U, EX1, 'EX11.1', '1(v)', 'Solve the right angled triangle ABC in which γ = 90°, given a = 140 m, α = 38°20′.',
       'β = 51°40′, b ≈ 177 m, c ≈ 225.7 m.',
       'β = 90° − α = 90° − 38°20′ = 51°40′. '
       'tan α = a/b ⇒ b = a/tan α = 140/tan 38°20′ = 140/0.79089 = 177.0 m. '
       'sin α = a/c ⇒ c = a/sin α = 140/sin 38°20′ = 140/0.62024 = 225.7 m.', 323,
       'Right-angled triangle ABC, right angle at C; a = BC = 140 m, α = 38°20′ at A.'),
    bq(U, EX1, 'EX11.1', '1(vi)', 'Solve the right angled triangle ABC in which γ = 90°, given b = 30.8 m, α = 41°50′.',
       'β = 48°10′, a ≈ 27.57 m, c ≈ 41.34 m.',
       'β = 90° − α = 90° − 41°50′ = 48°10′. '
       'tan α = a/b ⇒ a = b tan α = 30.8 tan 41°50′ = 30.8(0.89569) = 27.57 m. '
       'cos α = b/c ⇒ c = b/cos α = 30.8/cos 41°50′ = 30.8/0.74547 = 41.34 m.', 323,
       'Right-angled triangle ABC, right angle at C; b = CA = 30.8 m, α = 41°50′ at A.'),

    bq(U, EX1, 'EX11.1', '2', 'A vertical stick 16 m long casts a 12 cm long shadow. Find the angle of elevation of the sun.',
       'θ ≈ 53°8′ (taking the shadow as 12 m, as the printed key does).',
       'Let θ be the angle of elevation. In the right triangle formed by the stick and its shadow, '
       'tan θ = height/shadow = 16/12 = 1.3333 ⇒ θ = tan<sup>−1</sup>(1.3333) = 53.13° = 53°8′. '
       'Note: the shadow is printed as 12 cm, which is a misprint for 12 m — the printed key (53°7′) comes from 16/12. '
       'With a 12 cm shadow the angle would be tan<sup>−1</sup>(16/0.12) = tan<sup>−1</sup>(133.3) ≈ 89.57°.', 323,
       'Right triangle: vertical stick 16 m, horizontal shadow 12 m, angle of elevation θ of the sun at the shadow tip.'),

    bq(U, EX1, 'EX11.1', '3', 'Find the distance of a man from the foot of a tower 169 m high, if the angle of depression of the man from its top is 48°30′.',
       'x ≈ 149.5 m.',
       'The angle of depression from the top equals the angle of elevation of the top from the man (alternate angles), so in the right triangle '
       'tan 48°30′ = 169/x ⇒ x = 169/tan 48°30′ = 169/1.13029 = 149.5 m.', 323,
       'Right triangle: vertical tower 169 m, horizontal distance x from its foot to the man, angle 48°30′ at the man.'),

    bq(U, EX1, 'EX11.1', '4', 'A string of a flying kite is 200 metres long and its angle of elevation is 58°30′. Find the height of the kite when the string is fully stretched.',
       'h ≈ 170.53 m.',
       'In the right triangle, the string is the hypotenuse and the height h is opposite the angle of elevation: '
       'sin 58°30′ = h/200 ⇒ h = 200 sin 58°30′ = 200(0.85264) = 170.53 m.', 323,
       'Right triangle: string 200 m as hypotenuse, vertical height h of the kite, angle 58°30′ at the ground.'),

    bq(U, EX1, 'EX11.1', '5', 'A man 1.8 m tall observes that the angle of elevation of the top of a tree at a distance of 12 m from him is 31°45′. What is the height of the tree?',
       'Height of the tree ≈ 9.23 m (key: 9.22 m).',
       'Height of the tree above the man\u2019s eye level = 12 tan 31°45′ = 12(0.61882) = 7.43 m. '
       'Adding the height of the man: height of tree = 7.43 + 1.8 = 9.23 m.', 323,
       'Right triangle: horizontal distance 12 m from the man\u2019s eye to the tree, height above eye level h, angle 31°45′.'),

    bq(U, EX1, 'EX11.1', '6', 'From the top of a cliff 80 m high, the angle of depression of a boat is 12°30′. How far is the boat from the cliff?',
       'x ≈ 361 m.',
       'The angle of depression equals the angle of elevation of the cliff top from the boat, so '
       'tan 12°30′ = 80/x ⇒ x = 80/tan 12°30′ = 80/0.22169 = 360.86 ≈ 361 m.', 323,
       'Right triangle: vertical cliff 80 m, horizontal distance x of the boat from the foot of the cliff, angle 12°30′ at the boat.'),

    bq(U, EX1, 'EX11.1', '7', 'Two masts are 20 m and 12 m high. If the line joining their tops makes an angle of 35° with the horizontal, find the distance between them.',
       'd ≈ 11.4 m.',
       'Difference in heights = 20 − 12 = 8 m. The line joining the tops, the horizontal through the shorter mast\u2019s top and the vertical drop form a right triangle: '
       'tan 35° = 8/d ⇒ d = 8/tan 35° = 8/0.70021 = 11.43 ≈ 11.4 m.', 323,
       'Two vertical masts 20 m and 12 m high standing on the same horizontal ground, horizontal distance d apart; the segment joining their tops makes 35° with the horizontal.'),

    bq(U, EX1, 'EX11.1', '8', 'A window washer is working in a hotel building. An observer at a distance of 20 m from the building finds the angle of elevation of the worker to be 30°. The worker climbs up 12 m and the observer moves 4 m further away from the building. Find the new angle of elevation of the worker.',
       'θ ≈ 44°27′.',
       'First position: height of the worker above the observer\u2019s eye = 20 tan 30° = 20(0.57735) = 11.547 m. '
       'After climbing 12 m the height becomes 11.547 + 12 = 23.547 m, and the observer is now 20 + 4 = 24 m away. '
       'tan θ = 23.547/24 = 0.98113 ⇒ θ = tan<sup>−1</sup>(0.98113) = 44.45° = 44°27′.', 323,
       'Two right triangles with a common vertical wall: observer 20 m then 24 m from the building, worker 11.547 m then 23.547 m above eye level.'),
]

# ============================================================== Exercise 11.2 (pdf 330-331)
ITEMS += [
    bq(U, EX2, 'EX11.2', '1(i)', 'Solve the triangle by using the law of sines: a = 70, b = 34, α = 79°.',
       'β ≈ 28°29′, γ ≈ 72°31′, c ≈ 68.02.',
       'Law of sines: a/sin α = b/sin β ⇒ sin β = b sin α/a = 34 sin 79°/70 = 34(0.98163)/70 = 0.47679 ⇒ β = 28.48° ≈ 28°29′. '
       'γ = 180° − α − β = 180° − 79° − 28.48° = 72.52° ≈ 72°31′. '
       'c = a sin γ/sin α = 70(0.95379)/0.98163 = 68.02. (Printed key: β = 28°28′, γ = 72°32′.)', 330),
    bq(U, EX2, 'EX11.2', '1(ii)', 'Solve the triangle by using the law of sines: b = 136, γ = 104.2°, α = 43.1°.',
       'β = 32.7°, a ≈ 172, c ≈ 244.',
       'β = 180° − α − γ = 180° − 43.1° − 104.2° = 32.7°. '
       'Law of sines: a = b sin α/sin β = 136 sin 43.1°/sin 32.7° = 136(0.68327)/0.54024 = 172.0. '
       'c = b sin γ/sin β = 136 sin 104.2°/sin 32.7° = 136(0.96945)/0.54024 = 244.0.', 330),
    bq(U, EX2, 'EX11.2', '1(iii)', 'Solve the triangle by using the law of sines: α = 48°45′, β = 69°15′, c = 40.5.',
       'γ = 62°, a ≈ 34.5, b ≈ 42.9.',
       'γ = 180° − 48°45′ − 69°15′ = 62°. '
       'a = c sin α/sin γ = 40.5 sin 48°45′/sin 62° = 40.5(0.75184)/0.88295 = 34.49. '
       'b = c sin β/sin γ = 40.5 sin 69°15′/sin 62° = 40.5(0.93544)/0.88295 = 42.89.', 330),

    bq(U, EX2, 'EX11.2', '2(i)', 'Solve the triangle by using the law of cosines: α = 78.2°, b = 62.4, c = 150.',
       'a ≈ 150.2, β ≈ 24°, γ ≈ 77.8°.',
       'Law of cosines: a<sup>2</sup> = b<sup>2</sup> + c<sup>2</sup> − 2bc cos α = 62.4<sup>2</sup> + 150<sup>2</sup> − 2(62.4)(150)cos 78.2° '
       '= 3893.76 + 22500 − 3828.2 = 22565.6 ⇒ a = 150.2. '
       'Then sin β = b sin α/a = 62.4(0.97887)/150.2 = 0.40661 ⇒ β = 24.0°. '
       'γ = 180° − 78.2° − 24.0° = 77.8°.', 330),
    bq(U, EX2, 'EX11.2', '2(ii)', 'Solve the triangle by using the law of cosines: a = 48, b = 33.3, γ = 41°30′.',
       'c ≈ 31.92, α ≈ 94.8°, β ≈ 43.7°.',
       'c<sup>2</sup> = a<sup>2</sup> + b<sup>2</sup> − 2ab cos γ = 48<sup>2</sup> + 33.3<sup>2</sup> − 2(48)(33.3)cos 41°30′ '
       '= 2304 + 1108.89 − 2394.16 = 1018.73 ⇒ c = 31.92. '
       'cos α = (b<sup>2</sup> + c<sup>2</sup> − a<sup>2</sup>)/(2bc) = (1108.89 + 1018.73 − 2304)/(2 × 33.3 × 31.92) = −176.38/2125.9 = −0.08297 '
       '⇒ α = 94.76°. β = 180° − 41.5° − 94.76° = 43.74°. (Printed key: α = 94.9°, β = 43.6°.)', 330),
    bq(U, EX2, 'EX11.2', '2(iii)', 'Solve the triangle by using the law of cosines: a = 73, c = 40, β = 76°45′.',
       'b ≈ 74.77, α ≈ 71°52′, γ ≈ 31°23′.',
       'b<sup>2</sup> = a<sup>2</sup> + c<sup>2</sup> − 2ac cos β = 73<sup>2</sup> + 40<sup>2</sup> − 2(73)(40)cos 76°45′ '
       '= 5329 + 1600 − 1338.5 = 5590.5 ⇒ b = 74.77. '
       'cos α = (b<sup>2</sup> + c<sup>2</sup> − a<sup>2</sup>)/(2bc) = (5590.5 + 1600 − 5329)/(2 × 74.77 × 40) = 1861.5/5981.6 = 0.31121 '
       '⇒ α = 71.87°. γ = 180° − 76°45′ − 71.87° = 31.38°.', 330),

    bq(U, EX2, 'EX11.2', '3(i)', 'Solve by using the laws of tangents: a = 432, c = 325, β = 42°.',
       'α ≈ 89.21°, γ ≈ 48.79°, b ≈ 289.1.',
       'Law of tangents: tan((α − γ)/2)/tan((α + γ)/2) = (a − c)/(a + c) = (432 − 325)/(432 + 325) = 107/757 = 0.14135. '
       '(α + γ)/2 = (180° − 42°)/2 = 69°, so tan((α − γ)/2) = 0.14135 tan 69° = 0.14135(2.60509) = 0.36823 ⇒ (α − γ)/2 = 20.22°, α − γ = 40.43°. '
       'With α + γ = 138°: α = 89.21°, γ = 48.79°. By the law of sines b = a sin β/sin α = 432 sin 42°/sin 89.21° = 289.1. '
       '(Printed key gives b = 289.31, a transposition typo; the law-of-sines value is 289.09.)', 330),
    bq(U, EX2, 'EX11.2', '3(ii)', 'Solve by using the laws of tangents: b = 39, c = 35, α = 75°.',
       'β ≈ 56.53°, γ ≈ 48.47°, a ≈ 45.16.',
       'Law of tangents: tan((β − γ)/2)/tan((β + γ)/2) = (b − c)/(b + c) = 4/74 = 0.054054. '
       '(β + γ)/2 = (180° − 75°)/2 = 52.5°, so tan((β − γ)/2) = 0.054054 tan 52.5° = 0.054054(1.30323) = 0.070446 ⇒ (β − γ)/2 = 4.03°, β − γ = 8.06°. '
       'With β + γ = 105°: β = 56.53°, γ = 48.47°. By the law of sines a = b sin α/sin β = 39 sin 75°/sin 56.53° = 45.16.', 330),
    bq(U, EX2, 'EX11.2', '3(iii)', 'Solve by using the laws of tangents: a = 39.14, b = 34.21, γ = 78°10′.',
       'α ≈ 55.65°, β ≈ 46.19°, c ≈ 46.40.',
       'Law of tangents: tan((α − β)/2)/tan((α + β)/2) = (a − b)/(a + b) = 4.93/73.35 = 0.067212. '
       '(α + β)/2 = (180° − 78°10′)/2 = 50°55′, so tan((α − β)/2) = 0.067212 tan 50.9167° = 0.067212(1.23155) = 0.08278 ⇒ (α − β)/2 = 4.73°, α − β = 9.46°. '
       'With α + β = 101.83°: α = 55.65°, β = 46.19°. By the law of sines c = a sin γ/sin α = 39.14 sin 78°10′/sin 55.65° = 46.40. '
       '(Printed key: α = 55.38°, β = 46.43°, c = 46.5 — a rounding slip; the values above satisfy the law of cosines.)', 330),

    bq(U, EX2, 'EX11.2', '4(i)', 'Solve the triangle by using suitable laws: a = 9, b = 7, c = 5.',
       'α ≈ 95.7°, β ≈ 50.7°, γ ≈ 33.6°.',
       'Three sides are known, so use the law of cosines. '
       'cos α = (b<sup>2</sup> + c<sup>2</sup> − a<sup>2</sup>)/(2bc) = (49 + 25 − 81)/(2 × 7 × 5) = −7/70 = −0.1 ⇒ α = 95.74°. '
       'cos β = (a<sup>2</sup> + c<sup>2</sup> − b<sup>2</sup>)/(2ac) = (81 + 25 − 49)/(2 × 9 × 5) = 57/90 = 0.63333 ⇒ β = 50.70°. '
       'γ = 180° − 95.74° − 50.70° = 33.56°.', 330),
    bq(U, EX2, 'EX11.2', '4(ii)', 'Solve the triangle by using suitable laws: b = 35, a = 37, α = 23°25′.',
       'β ≈ 22°4′, γ ≈ 134°31′, c ≈ 66.4  (for the data as printed).',
       'Two sides and a non-included angle: use the law of sines. '
       'sin β = b sin α/a = 35 sin 23°25′/37 = 35(0.39737)/37 = 0.37587 ⇒ β = 22.07° (the obtuse value 157.93° is impossible since α + β &lt; 180°). '
       'γ = 180° − 23.42° − 22.07° = 134.51°. c = a sin γ/sin α = 37 sin 134.51°/0.39737 = 37(0.71344)/0.39737 = 66.43. '
       'Printed key gives a = 14.74, β = 70°39′, γ = 85°56′: those are the answers for b = 35, c = 37 (not a = 37), i.e. the printed “a = 37” is a misprint for c = 37.', 330),

    bq(U, EX2, 'EX11.2', '5(i)', 'Solve the triangle by using the half angle formula of sines: a = 55, c = 65, b = 85.',
       'α ≈ 40°19′, β ≈ 89°48′, γ ≈ 49°53′.',
       's = ½(a + b + c) = ½(55 + 85 + 65) = 102.5; s − a = 47.5, s − b = 17.5, s − c = 37.5. '
       'sin(α/2) = √((s − b)(s − c)/(bc)) = √(17.5 × 37.5/(85 × 65)) = √(656.25/5525) = 0.34464 ⇒ α/2 = 20.16°, α = 40.32°. '
       'sin(β/2) = √((s − a)(s − c)/(ac)) = √(47.5 × 37.5/(55 × 65)) = √(1781.25/3575) = 0.70588 ⇒ β/2 = 44.90°, β = 89.80°. '
       'γ = 180° − 40.32° − 89.80° = 49.88°.', 330),
    bq(U, EX2, 'EX11.2', '5(ii)', 'Solve the triangle by using the half angle formula of sines: b = 15, a = 20, c = 14.',
       'α ≈ 87°8′, β ≈ 48°31′, γ ≈ 44°21′.',
       's = ½(20 + 15 + 14) = 24.5; s − a = 4.5, s − b = 9.5, s − c = 10.5. '
       'sin(α/2) = √((s − b)(s − c)/(bc)) = √(9.5 × 10.5/(15 × 14)) = √(99.75/210) = 0.68920 ⇒ α/2 = 43.57°, α = 87.13°. '
       'sin(β/2) = √((s − a)(s − c)/(ac)) = √(4.5 × 10.5/(20 × 14)) = √(47.25/280) = 0.41079 ⇒ β/2 = 24.25°, β = 48.51°. '
       'γ = 180° − 87.13° − 48.51° = 44.36°.', 330),
    bq(U, EX2, 'EX11.2', '5(iii)', 'Solve the triangle by using the half angle formula of sines: c = 1.3, b = 2.3, a = 2.7.',
       'α ≈ 92°58′, β ≈ 58°17′, γ ≈ 28°44′.',
       's = ½(2.7 + 2.3 + 1.3) = 3.15; s − a = 0.45, s − b = 0.85, s − c = 1.85. '
       'sin(α/2) = √((s − b)(s − c)/(bc)) = √(0.85 × 1.85/(2.3 × 1.3)) = √(1.5725/2.99) = 0.72520 ⇒ α/2 = 46.49°, α = 92.97°. '
       'sin(β/2) = √((s − a)(s − c)/(ac)) = √(0.45 × 1.85/(2.7 × 1.3)) = √(0.8325/3.51) = 0.48701 ⇒ β/2 = 29.14°, β = 58.29°. '
       'γ = 180° − 92.97° − 58.29° = 28.74°.', 330),

    bq(U, EX2, 'EX11.2', '6(i)', 'Solve the triangle by using the half angle formula of cosines: a = 95, b = 76, c = 85.',
       'α ≈ 72°5′, β ≈ 49°34′, γ ≈ 58°21′.',
       's = ½(95 + 76 + 85) = 128; s − a = 33, s − b = 52, s − c = 43. '
       'cos(α/2) = √(s(s − a)/(bc)) = √(128 × 33/(76 × 85)) = √(4224/6460) = 0.80862 ⇒ α/2 = 36.04°, α = 72.08°. '
       'cos(β/2) = √(s(s − b)/(ac)) = √(128 × 52/(95 × 85)) = √(6656/8075) = 0.90789 ⇒ β/2 = 24.78°, β = 49.57°. '
       'γ = 180° − 72.08° − 49.57° = 58.35°. '
       '(Printed key: 72°8′, 49°32′, 58°20′ — the key rounds loosely; exact recomputation gives 72°5′, 49°34′, 58°21′.)', 330),
    bq(U, EX2, 'EX11.2', '6(ii)', 'Solve the triangle by using the half angle formula of cosines: a = 10, b = 7, c = 5.',
       'α ≈ 111°48′, β ≈ 40°32′, γ ≈ 27°40′.',
       's = ½(10 + 7 + 5) = 11; s − a = 1, s − b = 4, s − c = 6. '
       'cos(α/2) = √(s(s − a)/(bc)) = √(11 × 1/(7 × 5)) = √(11/35) = 0.56061 ⇒ α/2 = 55.90°, α = 111.80°. '
       'cos(β/2) = √(s(s − b)/(ac)) = √(11 × 4/(10 × 5)) = √(44/50) = 0.93808 ⇒ β/2 = 20.27°, β = 40.54°. '
       'γ = 180° − 111.80° − 40.54° = 27.66°. '
       '(Printed key: 111°52′, 40°30′, 27°38′ — small rounding slips; exact recomputation gives 111°48′, 40°32′, 27°40′.)', 330),
    bq(U, EX2, 'EX11.2', '6(iii)', 'Solve the triangle by using the half angle formula of cosines: c = 10, a = 15, b = 7.',
       'γ ≈ 34°3′, β ≈ 23°4′, α ≈ 122°53′.',
       's = ½(15 + 7 + 10) = 16; s − a = 1, s − b = 9, s − c = 6. '
       'cos(γ/2) = √(s(s − c)/(ab)) = √(16 × 6/(15 × 7)) = √(96/105) = 0.95618 ⇒ γ/2 = 17.02°, γ = 34.05°. '
       'cos(β/2) = √(s(s − b)/(ac)) = √(16 × 9/(15 × 10)) = √(144/150) = 0.97980 ⇒ β/2 = 11.54°, β = 23.07°. '
       'α = 180° − 34.05° − 23.07° = 122.88°.', 330),

    bq(U, EX2, 'EX11.2', '7(i)', 'Solve by using the half angle formula of tangent: c = 23, a = 13, b = 16.',
       'α ≈ 33°11′, β ≈ 42°22′, γ ≈ 104°28′.',
       's = ½(13 + 16 + 23) = 26; s − a = 13, s − b = 10, s − c = 3. '
       'r = √((s − a)(s − b)(s − c)/s) = √(13 × 10 × 3/26) = √15 = 3.8730. '
       'tan(α/2) = r/(s − a) = 3.8730/13 = 0.29792 ⇒ α/2 = 16.59°, α = 33.18°. '
       'tan(β/2) = r/(s − b) = 3.8730/10 = 0.38730 ⇒ β/2 = 21.18°, β = 42.36°. '
       'γ = 180° − 33.18° − 42.36° = 104.46°.', 330),
    bq(U, EX2, 'EX11.2', '7(ii)', 'Solve by using the half angle formula of tangent: a = 25, b = 20, c = 18.',
       'α ≈ 82°6′, β ≈ 52°25′, γ ≈ 45°29′.',
       's = ½(25 + 20 + 18) = 31.5; s − a = 6.5, s − b = 11.5, s − c = 13.5. '
       'r = √((s − a)(s − b)(s − c)/s) = √(6.5 × 11.5 × 13.5/31.5) = √32.0357 = 5.6600. '
       'tan(α/2) = r/(s − a) = 5.6600/6.5 = 0.87077 ⇒ α/2 = 41.05°, α = 82.10°. '
       'tan(β/2) = r/(s − b) = 5.6600/11.5 = 0.49217 ⇒ β/2 = 26.21°, β = 52.41°. '
       'γ = 180° − 82.10° − 52.41° = 45.49°.', 330),
    bq(U, EX2, 'EX11.2', '7(iii)', 'Solve by using the half angle formula of tangent: a = 16, b = 11, c = 13.',
       'α ≈ 83°10′, β ≈ 43°3′, γ ≈ 53°47′.',
       's = ½(16 + 11 + 13) = 20; s − a = 4, s − b = 9, s − c = 7. '
       'r = √((s − a)(s − b)(s − c)/s) = √(4 × 9 × 7/20) = √12.6 = 3.5496. '
       'tan(α/2) = r/(s − a) = 3.5496/4 = 0.88741 ⇒ α/2 = 41.59°, α = 83.17°. '
       'tan(β/2) = r/(s − b) = 3.5496/9 = 0.39441 ⇒ β/2 = 21.53°, β = 43.05°. '
       'γ = 180° − 83.17° − 43.05° = 53.78°. '
       '(Printed key gives α = 83°18′; the correct value is 83°10′, so the key has an 8′ slip.)', 330),

    bq(U, EX2, 'EX11.2', '8', 'Find the largest angle of ΔABC when a = 6 cm, b = 8 cm and c = 9.4 cm.',
       'γ ≈ 83.03°.',
       'The largest angle lies opposite the largest side, so it is γ (opposite c = 9.4 cm). '
       'cos γ = (a<sup>2</sup> + b<sup>2</sup> − c<sup>2</sup>)/(2ab) = (36 + 64 − 88.36)/(2 × 6 × 8) = 11.64/96 = 0.12125 ⇒ γ = 83.03°.', 330),
    bq(U, EX2, 'EX11.2', '9', 'Find the smallest angle in ΔABC when a = 25 cm, b = 18 cm and c = 21 cm.',
       'β = 45°.',
       'The smallest angle is opposite the smallest side, so it is β (opposite b = 18 cm). '
       'cos β = (a<sup>2</sup> + c<sup>2</sup> − b<sup>2</sup>)/(2ac) = (625 + 441 − 324)/(2 × 25 × 21) = 742/1050 = 0.70667 ⇒ β = 45.0°.', 330),
    bq(U, EX2, 'EX11.2', '10', 'Find the length of the third side of a triangular building that faces 13.6 metres along one street and 13 metres along another street. The angle of intersection between the streets measures 72°.',
       'Third side ≈ 15.64 m.',
       'The two given sides enclose 72°, so by the law of cosines '
       'x<sup>2</sup> = 13.6<sup>2</sup> + 13<sup>2</sup> − 2(13.6)(13)cos 72° = 184.96 + 169 − 353.6(0.30902) = 353.96 − 109.27 = 244.69 '
       '⇒ x = 15.64 m.', 330),
    bq(U, EX2, 'EX11.2', '11', 'If one side of a triangle is y units long, another side is 3 times as long and the angle between the two sides measures 35°, find the measures of the other two angles and the third side.',
       'Third side ≈ 2.25y; the other angles are ≈ 15° and ≈ 130°.',
       'Third side: x<sup>2</sup> = y<sup>2</sup> + (3y)<sup>2</sup> − 2(y)(3y)cos 35° = y<sup>2</sup>(10 − 6(0.81915)) = 5.0851y<sup>2</sup> ⇒ x = 2.255y ≈ 2.25y. '
       'By the law of sines, the angle A opposite the side y satisfies sin A = y sin 35°/x = 0.57358/2.255 = 0.25437 ⇒ A = 14.74° ≈ 15°. '
       'The remaining angle = 180° − 35° − 14.74° = 130.26° ≈ 130°.', 330),
    bq(U, EX2, 'EX11.2', '12', 'If the length of larger side of a parallelogram is 55 cm and one diagonal of the parallelogram makes angles of measure 30° and 50° with a pair of adjacent sides, find the length of the diagonal.',
       'Diagonal ≈ 70.7 cm.',
       'The diagonal cuts the parallelogram into a triangle whose angles at the two ends of the diagonal are 30° and 50°, so the third angle is 180° − 30° − 50° = 100°. '
       'The 55 cm side lies opposite the larger of 30° and 50°, i.e. opposite 50°. '
       'By the law of sines: d/sin 100° = 55/sin 50° ⇒ d = 55 sin 100°/sin 50° = 55(0.98481)/0.76604 = 70.71 cm.', 330,
       'Parallelogram with larger side 55 cm; the diagonal makes 30° with one adjacent side and 50° with the other, forming a triangle with angles 30°, 50°, 100°.'),
    bq(U, EX2, 'EX11.2', '13', 'The sides of a parallelogram are 25 cm and 35 cm long and one of its angles is 36°. Find the lengths of its diagonals.',
       'Diagonals ≈ 57.15 cm and ≈ 20.84 cm.',
       'For a parallelogram with sides p, q and included angle θ the diagonals are '
       'd<sub>1</sub> = √(p<sup>2</sup> + q<sup>2</sup> + 2pq cos θ) and d<sub>2</sub> = √(p<sup>2</sup> + q<sup>2</sup> − 2pq cos θ). '
       'd<sub>1</sub><sup>2</sup> = 625 + 1225 + 2(25)(35)(0.80902) = 1850 + 1415.8 = 3265.8 ⇒ d<sub>1</sub> = 57.15 cm. '
       'd<sub>2</sub><sup>2</sup> = 1850 − 1415.8 = 434.2 ⇒ d<sub>2</sub> = 20.84 cm.', 331),
    bq(U, EX2, 'EX11.2', '14', 'Two hikers start from the same point; one walks 9 km heading east, the other one 10 km heading 55° north east. How far apart are they at the end of their walks?',
       '≈ 8.82 km apart.',
       'The two paths enclose 55°, so the distance d between the hikers is the third side of a triangle with sides 9 and 10: '
       'd<sup>2</sup> = 9<sup>2</sup> + 10<sup>2</sup> − 2(9)(10)cos 55° = 81 + 100 − 180(0.57358) = 181 − 103.24 = 77.76 ⇒ d = 8.818 km.', 331),
    bq(U, EX2, 'EX11.2', '15', 'Two planes start from Karachi International Airport at the same time and fly in directions that make an angle of 127° with each other. Their speeds are 525 km/h. How far apart are they at the end of 2 hours of flying time?',
       '≈ 1879.4 km apart.',
       'Distance flown by each plane = 525 × 2 = 1050 km. By the law of cosines '
       'd<sup>2</sup> = 1050<sup>2</sup> + 1050<sup>2</sup> − 2(1050)(1050)cos 127° = 2(1050<sup>2</sup>)(1 − cos 127°) = 2205000(1.60182) = 3532013 '
       '⇒ d = 1879.4 km.', 331),
]

# ============================================================== Exercise 11.3 (pdf 333)
ITEMS += [
    bq(U, EX3, 'EX11.3', '1(i)', 'Find the area of triangle ABC when a = 8.6, b = 11.4, γ = 90°.',
       '▲ = 49.02 square units.',
       'Two sides and the included angle: ▲ = ½ab sin γ = ½(8.6)(11.4) sin 90° = ½(98.04)(1) = 49.02 square units.', 333),
    bq(U, EX3, 'EX11.3', '1(ii)', 'Find the area of triangle ABC when b = 63, c = 17, α = 120°.',
       '▲ ≈ 463.76 square units.',
       'The included angle between b and c is α: ▲ = ½bc sin α = ½(63)(17) sin 120° = 535.5(0.86603) = 463.76 square units. '
       '(Printed key: 463.74.)', 333),
    bq(U, EX3, 'EX11.3', '1(iii)', 'Find the area of triangle ABC when c = 5.34, a = 9.30, β = 53°34′.',
       '▲ ≈ 19.98 square units.',
       'The included angle between a and c is β: ▲ = ½ac sin β = ½(9.30)(5.34) sin 53°34′ = 24.831(0.80489) = 19.98 square units.', 333),
    bq(U, EX3, 'EX11.3', '1(iv)', 'Find the area of triangle ABC when c = 36, α = 46°, β = 66°.',
       '▲ ≈ 459.28 square units.',
       'One side and two angles: γ = 180° − 46° − 66° = 68°, and ▲ = ½c<sup>2</sup> sin α sin β/sin γ '
       '= ½(36)<sup>2</sup>(sin 46°)(sin 66°)/sin 68° = 648(0.71934)(0.91355)/0.92718 = 459.28 square units. '
       '(Printed key: 459.22.)', 333),
    bq(U, EX3, 'EX11.3', '1(v)', 'Find the area of triangle ABC when a = 54, β = 37°, γ = 54°.',
       '▲ ≈ 709.98 square units.',
       'α = 180° − 37° − 54° = 89°, and ▲ = ½a<sup>2</sup> sin β sin γ/sin α '
       '= ½(54)<sup>2</sup>(sin 37°)(sin 54°)/sin 89° = 1458(0.60182)(0.80902)/0.99985 = 709.98 square units.', 333),
    bq(U, EX3, 'EX11.3', '1(vi)', 'Find the area of triangle ABC when b = 4.8, α = 35°9′, γ = 85°31′.',
       '▲ ≈ 7.69 square units (key: 7.66).',
       'β = 180° − 35°9′ − 85°31′ = 59°20′, and ▲ = ½b<sup>2</sup> sin α sin γ/sin β '
       '= ½(4.8)<sup>2</sup>(sin 35°9′)(sin 85°31′)/sin 59°20′ = 11.52(0.57574)(0.99694)/0.86015 = 7.69 square units.', 333),
    bq(U, EX3, 'EX11.3', '1(vii)', 'Find the area of triangle ABC when a = 37, b = 41, c = 37.',
       '▲ ≈ 631.43 square units.',
       'Three sides — Hero\u2019s formula. s = ½(37 + 41 + 37) = 57.5; s − a = 20.5, s − b = 16.5, s − c = 20.5. '
       '▲ = √(s(s − a)(s − b)(s − c)) = √(57.5 × 20.5 × 16.5 × 20.5) = √398,712 = 631.43 square units.', 333),
    bq(U, EX3, 'EX11.3', '1(viii)', 'Find the area of triangle ABC when a = 41.34, b = 35.65, c = 56.81.',
       '▲ ≈ 734.28 square units.',
       's = ½(41.34 + 35.65 + 56.81) = 66.9; s − a = 25.56, s − b = 31.25, s − c = 10.09. '
       '▲ = √(66.9 × 25.56 × 31.25 × 10.09) = √539,152 = 734.28 square units.', 333),
    bq(U, EX3, 'EX11.3', '1(ix)', 'Find the area of triangle ABC when a = 98, b = 120, c = 200.',
       '▲ ≈ 4310.73 square units.',
       's = ½(98 + 120 + 200) = 209; s − a = 111, s − b = 89, s − c = 9. '
       '▲ = √(209 × 111 × 89 × 9) = √18,582,399 = 4310.73 square units.', 333),

    bq(U, EX3, 'EX11.3', '2', 'The area of a triangle is 3.346 square units. If β = 20.9° and γ = 117.2°, find a and angle α.',
       'α = 41.9°, a ≈ 3.75 units.',
       'α = 180° − 20.9° − 117.2° = 41.9°. Using ▲ = ½a<sup>2</sup> sin β sin γ/sin α: '
       'a<sup>2</sup> = 2▲ sin α/(sin β sin γ) = 2(3.346)(0.66795)/((0.35674)(0.88936)) = 4.4699/0.31727 = 14.088 '
       '⇒ a = 3.75 units.', 333),
    bq(U, EX3, 'EX11.3', '3', 'The measures of the two sides of a triangle are 4 and 5 units. Find the third side so that the area of the triangle is 6 square units.',
       'Third side = 3 units (or √73 ≈ 8.54 units if the included angle is obtuse).',
       '▲ = ½(4)(5) sin θ = 10 sin θ = 6 ⇒ sin θ = 0.6 ⇒ θ = 36.87°. Then '
       'x<sup>2</sup> = 4<sup>2</sup> + 5<sup>2</sup> − 2(4)(5)cos 36.87° = 41 − 40(0.8) = 9 ⇒ x = 3 units. '
       'The obtuse possibility θ = 143.13° gives x<sup>2</sup> = 41 + 32 = 73, x = √73 ≈ 8.54 units. (Printed key: 3.)', 333),
    bq(U, EX3, 'EX11.3', '4', 'Find the area of the equilateral triangle whose each side is x units long.',
       '▲ = (√3/4)x<sup>2</sup> square units.',
       'For an equilateral triangle the included angle between two sides is 60°, so '
       '▲ = ½(x)(x) sin 60° = ½x<sup>2</sup>(√3/2) = (√3/4)x<sup>2</sup> square units. '
       '(Hero\u2019s formula with s = 3x/2 gives the same result.)', 333),
]

# ============================================================== Exercise 11.4 (pdf 337-338)
ITEMS += [
    bq(U, EX4, 'EX11.4', '1(i)', 'Find the values of R and r of ΔABC when a = 5 cm, b = 10 cm, c = 12 cm.',
       'R ≈ 6.11 cm, r ≈ 1.82 cm.',
       's = ½(5 + 10 + 12) = 13.5; s − a = 8.5, s − b = 3.5, s − c = 1.5. '
       '▲ = √(13.5 × 8.5 × 3.5 × 1.5) = √602.4375 = 24.55 cm<sup>2</sup>. '
       'R = abc/(4▲) = (5)(10)(12)/(4 × 24.55) = 600/98.18 = 6.11 cm; '
       'r = ▲/s = 24.55/13.5 = 1.82 cm. (Printed key: R = 6.12 cm, r = 1.81 cm.)', 337),
    bq(U, EX4, 'EX11.4', '1(ii)', 'Find the values of R and r of ΔABC when a = 10.5 cm, b = 11.5 cm, c = 20.5 cm.',
       'R ≈ 15.14 cm, r ≈ 1.92 cm.',
       's = ½(10.5 + 11.5 + 20.5) = 21.25; s − a = 10.75, s − b = 9.75, s − c = 0.75. '
       '▲ = √(21.25 × 10.75 × 9.75 × 0.75) = √1670.45 = 40.87 cm<sup>2</sup>. '
       'R = abc/(4▲) = (10.5)(11.5)(20.5)/(4 × 40.87) = 2475.375/163.48 = 15.14 cm; '
       'r = ▲/s = 40.87/21.25 = 1.92 cm.', 337),
    bq(U, EX4, 'EX11.4', '1(iii)', 'Find the values of R and r of ΔABC when a = 40 cm, b = 12 cm, c = 38 cm.',
       'R = 20 cm, r ≈ 5.07 cm.',
       's = ½(40 + 12 + 38) = 45; s − a = 5, s − b = 33, s − c = 7. '
       '▲ = √(45 × 5 × 33 × 7) = √51,975 = 227.98 cm<sup>2</sup>. '
       'R = abc/(4▲) = (40)(12)(38)/(4 × 227.98) = 18,240/911.9 = 20 cm; '
       'r = ▲/s = 227.98/45 = 5.07 cm. (Printed key rounds r to 5 cm.)', 337),
    bq(U, EX4, 'EX11.4', '2(i)', 'Find r<sub>1</sub>, r<sub>2</sub> and r<sub>3</sub>, if the measures of the sides of triangle ABC are a = 23 cm, b = 24 cm, c = 28 cm.',
       'r<sub>1</sub> ≈ 18.21 cm, r<sub>2</sub> ≈ 19.56 cm, r<sub>3</sub> ≈ 27.80 cm.',
       's = ½(23 + 24 + 28) = 37.5; s − a = 14.5, s − b = 13.5, s − c = 9.5. '
       '▲ = √(37.5 × 14.5 × 13.5 × 9.5) = √69,736 = 264.08 cm<sup>2</sup>. '
       'r<sub>1</sub> = ▲/(s − a) = 264.08/14.5 = 18.21 cm; r<sub>2</sub> = ▲/(s − b) = 264.08/13.5 = 19.56 cm; '
       'r<sub>3</sub> = ▲/(s − c) = 264.08/9.5 = 27.80 cm.', 338),
    bq(U, EX4, 'EX11.4', '2(ii)', 'Find r<sub>1</sub>, r<sub>2</sub> and r<sub>3</sub>, if the measures of the sides of triangle ABC are a = 24.4 cm, b = 34.8 cm, c = 42.5 cm.',
       'r<sub>1</sub> ≈ 16.05 cm, r<sub>2</sub> ≈ 26.45 cm, r<sub>3</sub> ≈ 50.85 cm.',
       's = ½(24.4 + 34.8 + 42.5) = 50.85; s − a = 26.45, s − b = 16.05, s − c = 8.35. '
       '▲ = √(50.85 × 26.45 × 16.05 × 8.35) = √180,251 = 424.56 cm<sup>2</sup>. '
       'r<sub>1</sub> = 424.56/26.45 = 16.05 cm; r<sub>2</sub> = 424.56/16.05 = 26.45 cm; r<sub>3</sub> = 424.56/8.35 = 50.85 cm.', 338),
    bq(U, EX4, 'EX11.4', '2(iii)', 'Find r<sub>1</sub>, r<sub>2</sub> and r<sub>3</sub>, if the measures of the sides of triangle ABC are a = 75 cm, b = 62 cm, c = 53 cm.',
       'r<sub>1</sub> ≈ 81.14 cm, r<sub>2</sub> ≈ 49.18 cm, r<sub>3</sub> ≈ 38.64 cm.',
       's = ½(75 + 62 + 53) = 95; s − a = 20, s − b = 33, s − c = 42. '
       '▲ = √(95 × 20 × 33 × 42) = √2,633,400 = 1622.78 cm<sup>2</sup>. '
       'r<sub>1</sub> = 1622.78/20 = 81.14 cm; r<sub>2</sub> = 1622.78/33 = 49.18 cm; r<sub>3</sub> = 1622.78/42 = 38.64 cm.', 338),

    bq(U, EX4, 'EX11.4', '3', 'If a = b = c, then prove that r<sub>1</sub> : R : r = 3 : 2 : 1.',
       'Proof: for an equilateral triangle R = 2r and r<sub>1</sub> = 3r, hence r<sub>1</sub> : R : r = 3 : 2 : 1.',
       'Let a = b = c = x. Then s = 3x/2 and ▲ = (√3/4)x<sup>2</sup>. '
       'r = ▲/s = [(√3/4)x<sup>2</sup>]/(3x/2) = (√3/6)x. '
       'R = abc/(4▲) = x<sup>3</sup>/(4(√3/4)x<sup>2</sup>) = x/√3 = (√3/3)x = 2r. '
       'r<sub>1</sub> = ▲/(s − a) = [(√3/4)x<sup>2</sup>]/(x/2) = (√3/2)x = 3r. '
       'Therefore r<sub>1</sub> : R : r = 3r : 2r : r = 3 : 2 : 1.', 338),
    bq(U, EX4, 'EX11.4', '4(i)', 'Show that r<sub>1</sub>r<sub>2</sub>r<sub>3</sub> = rs<sup>2</sup>.',
       'Proof: r<sub>1</sub>r<sub>2</sub>r<sub>3</sub> = ▲<sup>3</sup>/[(s − a)(s − b)(s − c)] = s▲ = rs<sup>2</sup>.',
       'r<sub>1</sub> = ▲/(s − a), r<sub>2</sub> = ▲/(s − b), r<sub>3</sub> = ▲/(s − c), so '
       'r<sub>1</sub>r<sub>2</sub>r<sub>3</sub> = ▲<sup>3</sup>/[(s − a)(s − b)(s − c)]. '
       'Since ▲<sup>2</sup> = s(s − a)(s − b)(s − c), we get (s − a)(s − b)(s − c) = ▲<sup>2</sup>/s, hence '
       'r<sub>1</sub>r<sub>2</sub>r<sub>3</sub> = ▲<sup>3</sup> ÷ (▲<sup>2</sup>/s) = s▲. But ▲ = rs, so r<sub>1</sub>r<sub>2</sub>r<sub>3</sub> = rs·s = rs<sup>2</sup>.', 338),
    bq(U, EX4, 'EX11.4', '4(ii)', 'Show that r = 4R sin(α/2) sin(β/2) sin(γ/2).',
       'Proof: the product of the three half-angle sines equals (s − a)(s − b)(s − c)/(abc), and abc = 4R▲.',
       'sin(α/2) = √((s − b)(s − c)/(bc)), sin(β/2) = √((s − a)(s − c)/(ac)), sin(γ/2) = √((s − a)(s − b)/(ab)). '
       'Multiplying: sin(α/2)sin(β/2)sin(γ/2) = (s − a)(s − b)(s − c)/(abc). '
       'Now (s − a)(s − b)(s − c) = ▲<sup>2</sup>/s and abc = 4R▲, so the product = ▲<sup>2</sup>/(s·4R▲) = ▲/(4Rs) = r/(4R). '
       'Hence r = 4R sin(α/2) sin(β/2) sin(γ/2).', 338),
    bq(U, EX4, 'EX11.4', '4(iii)', 'Show that r<sub>1</sub> = a cos(β/2) cos(γ/2)/cos(α/2).',
       'Proof: the right-hand side simplifies to √(s(s − b)(s − c)/(s − a)) = ▲/(s − a) = r<sub>1</sub>.',
       'r<sub>1</sub> = ▲/(s − a) = √(s(s − a)(s − b)(s − c))/(s − a) = √(s(s − b)(s − c)/(s − a)) … (1). '
       'Using cos(β/2) = √(s(s − b)/(ac)), cos(γ/2) = √(s(s − c)/(ab)) and cos(α/2) = √(s(s − a)/(bc)): '
       'a cos(β/2)cos(γ/2)/cos(α/2) = a·[s√((s − b)(s − c))/(a√(bc))]·[√(bc)/√(s(s − a))] '
       '= s√((s − b)(s − c))/√(s(s − a)) = √(s(s − b)(s − c)/(s − a)), which is (1). Hence the identity holds.', 338),
    bq(U, EX4, 'EX11.4', '5', 'Prove that 1/r<sup>2</sup> + 1/r<sub>1</sub><sup>2</sup> + 1/r<sub>2</sub><sup>2</sup> + 1/r<sub>3</sub><sup>2</sup> = (a<sup>2</sup> + b<sup>2</sup> + c<sup>2</sup>)/▲<sup>2</sup>.',
       'Proof: 1/r = s/▲ and 1/r<sub>1</sub> = (s − a)/▲, so the sum is [s<sup>2</sup> + (s − a)<sup>2</sup> + (s − b)<sup>2</sup> + (s − c)<sup>2</sup>]/▲<sup>2</sup> = (a<sup>2</sup> + b<sup>2</sup> + c<sup>2</sup>)/▲<sup>2</sup>.',
       '1/r = s/▲, 1/r<sub>1</sub> = (s − a)/▲, 1/r<sub>2</sub> = (s − b)/▲, 1/r<sub>3</sub> = (s − c)/▲. '
       'Put x = s − a, y = s − b, z = s − c; then s = x + y + z, a = y + z, b = z + x, c = x + y. '
       'Numerator = s<sup>2</sup> + x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup> '
       '= (x + y + z)<sup>2</sup> + x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup> = 2(x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup>) + 2xy + 2yz + 2zx, '
       'while a<sup>2</sup> + b<sup>2</sup> + c<sup>2</sup> = (y + z)<sup>2</sup> + (z + x)<sup>2</sup> + (x + y)<sup>2</sup> = 2(x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup>) + 2xy + 2yz + 2zx. '
       'The numerators are equal, so the sum equals (a<sup>2</sup> + b<sup>2</sup> + c<sup>2</sup>)/▲<sup>2</sup>.', 338),
    bq(U, EX4, 'EX11.4', '6', 'Show that 1/(2rR) = 1/(ab) + 1/(bc) + 1/(ca).',
       'Proof: both sides reduce to 2s/(abc).',
       'r = ▲/s and R = abc/(4▲) ⇒ rR = abc/(4s), so 1/(2rR) = 2s/(abc). '
       'On the other hand 1/(ab) + 1/(bc) + 1/(ca) = (c + a + b)/(abc) = 2s/(abc). '
       'The two sides are therefore equal.', 338),
]

# ============================================================== Review Exercise 11 (pdf 338-340)
ITEMS += [
    mcq(U, RE11, 'REV11', 'i', 'From the top of a cliff 80 m high the angle of depression of a boat is α. If the distance between the boat and the foot of the cliff is 80√3 m, then angle α is:',
        ['π/4', 'π/6', 'π/3', '3π/4'], 'b',
        'The angle of depression from the cliff top equals the angle of elevation of the top from the boat, so '
        'tan α = 80/(80√3) = 1/√3 ⇒ α = 30° = π/6.', 338),
    mcq(U, RE11, 'REV11', 'ii', 'To solve an oblique triangle, we use:',
        ['law of sines', 'Laws of cosines', 'Laws of tangents', 'All of these'], 'd',
        'Every oblique triangle can be solved by the law of sines, the law of cosines or the law of tangents, depending on which three elements are given; hence all of these are used.', 338),
    mcq(U, RE11, 'REV11', 'iii', 'A circle which touches all the sides of a triangle is called ______.',
        ['circum-circle', 'in-circle', 'ex-circle', 'tri-circle'], 'b',
        'The circle inscribed inside a triangle, touching all three sides, is the in-circle (its centre is the in-centre and its radius the in-radius).', 338),
    mcq(U, RE11, 'REV11', 'iv', 'In a triangle ABC, if β = 90°, then b<sup>2</sup> = c<sup>2</sup> + a<sup>2</sup> − 2ac cos β becomes:',
        ['Law of sines', 'Law of tangents', 'Pythagoras theorem', 'None of these'], 'c',
        'Put cos 90° = 0 in the law of cosines: b<sup>2</sup> = c<sup>2</sup> + a<sup>2</sup> − 2ac(0) = a<sup>2</sup> + c<sup>2</sup>, '
        'which is the Pythagoras theorem for the right angle at B.', 338),
    mcq(U, RE11, 'REV11', 'v', 'In any triangle ABC, √((s − a)(s − c)/(ac)) is equal to:',
        ['sin α/2', 'cos α/2', 'sin β/2', 'sin γ/2'], 'c',
        'The half-angle sine formula gives sin(β/2) = √((s − a)(s − c)/(ac)), because β lies opposite b and the two adjacent sides are a and c.', 338),
    mcq(U, RE11, 'REV11', 'vi', 'In any triangle ABC, cos(γ/2) is equal to:',
        ['√(s(s − a)/ab)', '√(s(s − b)/ac)', '√(s(s − a)/bc)', '√(s(s − c)/ab)'], 'd',
        'Half-angle cosine formula: cos(γ/2) = √(s(s − c)/(ab)), since γ is opposite c and the adjacent sides are a and b.', 338),
    mcq(U, RE11, 'REV11', 'vii', 'In any triangle ABC, with usual notations, s is equal to:',
        ['a + b + c', '(a + b + c)/2', '(a + b + c)/3', 'abc/2'], 'b',
        's denotes the semi-perimeter, i.e. half the sum of the sides: s = ½(a + b + c) = (a + b + c)/2.', 338),
    mcq(U, RE11, 'REV11', 'viii', '√(s(s − b)/((s − a)(s − c))) = …',
        ['sin β/2', 'cos β/2', 'tan β/2', 'cot β/2'], 'd',
        'tan(β/2) = √((s − a)(s − c)/(s(s − b))), so its reciprocal is cot(β/2) = √(s(s − b)/((s − a)(s − c))).', 338),
    mcq(U, RE11, 'REV11', 'ix', 'In any triangle ABC, √((s − a)(s − b)/(s(s − c))) is equal to:',
        ['sin γ/2', 'cos γ/2', 'tan γ/2', 'cot γ/2'], 'c',
        'Half-angle tangent formula: tan(γ/2) = √((s − a)(s − b)/(s(s − c))) = r/(s − c).', 339),
    mcq(U, RE11, 'REV11', 'x', 'We can solve an oblique triangle, if:',
        ['One side and two angles are known', 'Three sides are known', 'Two sides and their included angles are known', 'All of these'], 'd',
        'One side with two angles (law of sines), three sides (law of cosines) or two sides with the included angle (law of cosines) each determine the triangle completely, so all of these cases can be solved.', 339),
    mcq(U, RE11, 'REV11', 'xi', 'In ΔABC, inradius = ---------',
        ['▲/(s − a)', '▲/(s − b)', '▲/(s − c)', '▲/s'], 'd',
        'The in-radius is r = ▲/s, because ▲ = rs (the area equals the in-radius times the semi-perimeter). '
        'Printed key gives (b) ▲/s — the letter is a misprint, since ▲/s is option (d).', 339),
    mcq(U, RE11, 'REV11', 'xii', 'In any triangle ABC, Area of triangle is:',
        ['bc sin α', '½ca sin α', '½ab sin γ', '½ab sin β'], 'c',
        'The area is half the product of two sides times the sine of the included angle. Sides a and b enclose the angle γ, so ▲ = ½ab sin γ. '
        '(The angle between b and c is α and between c and a is β, so options (a) and (b) are not of the correct form.)', 339),
    mcq(U, RE11, 'REV11', 'xiii', "Hero's formula is:",
        ['▲ = s(s − a)(s − b)(s − c)', '▲ = √((s − a)(s − b)(s − c))', '▲ = √(s(s − a)(s − b)(s − c))', '▲ = (a + b + c)/2'], 'c',
        'Hero\u2019s formula: ▲ = √(s(s − a)(s − b)(s − c)) with s = (a + b + c)/2. Option (a) omits the square root and option (d) is just s.', 339),
    mcq(U, RE11, 'REV11', 'xiv', 'The circle passing through the three vertices of a triangle is called:',
        ['Circum-circle', 'In-circle', 'Ex-centre', 'Escribed circle'], 'a',
        'The circle through the three vertices is the circum-circle; its centre is the circum-centre and its radius the circum-radius.', 339),
    mcq(U, RE11, 'REV11', 'xv', 'The point of intersection of the right bisectors of the sides of a triangle is called:',
        ['Circum-centre', 'In-centre', 'Escribed centre', 'Ortho-centre'], 'a',
        'The right bisectors (perpendicular bisectors) of the sides meet at the circum-centre, the centre of the circum-circle.', 339),
    mcq(U, RE11, 'REV11', 'xvi', 'Radius of the circle which passes through all the vertices of a triangle is:',
        ['Circum-radius', 'In-radius', 'e-Radius', 'Diameter'], 'a',
        'The radius of the circum-circle, which passes through all three vertices, is the circum-radius R = abc/(4▲).', 339),
    mcq(U, RE11, 'REV11', 'xvii', 'In any triangle ABC, with usual notations, abc =',
        ['R', 'Rs', '4R▲', '▲/s'], 'c',
        'From R = abc/(4▲) we get abc = 4R▲.', 339),
    mcq(U, RE11, 'REV11', 'xviii', 'The point of intersection of the internal bisectors of angles of a triangle is:',
        ['In-centre', 'e-centre', 'Circum-centre', 'Ex-centre'], 'a',
        'The internal bisectors of the angles of a triangle are concurrent at the in-centre, the centre of the in-circle.', 339),
    mcq(U, RE11, 'REV11', 'xix', 'In any equilateral triangle ABC, with usual notations, r : R : r<sub>1</sub> =',
        ['1 : 2 : 3', '3 : 2 : 1', '1 : 3 : 2', '1 : 1 : 1'], 'a',
        'For an equilateral triangle R = 2r and r<sub>1</sub> = 3r, so r : R : r<sub>1</sub> = r : 2r : 3r = 1 : 2 : 3.', 339),
    mcq(U, RE11, 'REV11', 'xx', 'Circum radius of ΔABC is:',
        ['▲/s', '▲/(s − b)', '▲/(s − a)', 'abc/(4▲)'], 'd',
        'The circum-radius is R = abc/(4▲); the options ▲/s, ▲/(s − a) and ▲/(s − b) are the in-radius and the ex-radii r<sub>1</sub>, r<sub>2</sub>.', 339),

    bq(U, RE11, 'REV11', '2(i)', 'Prove that r<sub>2</sub> = b cos(α/2) cos(γ/2)/cos(β/2).',
       'Proof: both sides equal √(s(s − a)(s − c)/(s − b)) = ▲/(s − b).',
       'r<sub>2</sub> = ▲/(s − b). Since ▲<sup>2</sup> = s(s − a)(s − b)(s − c), ▲ = √(s(s − a)(s − b)(s − c)), so '
       'r<sub>2</sub> = √(s(s − a)(s − c)/(s − b)) … (1). '
       'Now cos(α/2) = √(s(s − a)/(bc)), cos(γ/2) = √(s(s − c)/(ab)) and cos(β/2) = √(s(s − b)/(ac)). '
       'Therefore b cos(α/2)cos(γ/2)/cos(β/2) = b·[s√((s − a)(s − c))/(b√(ac))]·[√(ac)/√(s(s − b))] '
       '= s√((s − a)(s − c))/√(s(s − b)) = √(s(s − a)(s − c)/(s − b)), which is (1). Hence the result.', 339),
    bq(U, RE11, 'REV11', '2(ii)', 'Prove that r<sub>1</sub>r<sub>2</sub> + r<sub>2</sub>r<sub>3</sub> + r<sub>3</sub>r<sub>1</sub> = s<sup>2</sup>.',
       'Proof: the sum equals ▲<sup>2</sup>·s/[(s − a)(s − b)(s − c)] = s<sup>2</sup>.',
       'r<sub>1</sub> = ▲/(s − a), r<sub>2</sub> = ▲/(s − b), r<sub>3</sub> = ▲/(s − c), so '
       'r<sub>1</sub>r<sub>2</sub> = ▲<sup>2</sup>/[(s − a)(s − b)], r<sub>2</sub>r<sub>3</sub> = ▲<sup>2</sup>/[(s − b)(s − c)], r<sub>3</sub>r<sub>1</sub> = ▲<sup>2</sup>/[(s − c)(s − a)]. '
       'Sum = ▲<sup>2</sup>[(s − c) + (s − a) + (s − b)]/[(s − a)(s − b)(s − c)] = ▲<sup>2</sup>(3s − 2s)/[(s − a)(s − b)(s − c)] '
       '= ▲<sup>2</sup>s/[(s − a)(s − b)(s − c)]. Since ▲<sup>2</sup> = s(s − a)(s − b)(s − c), this equals s·s = s<sup>2</sup>.', 339),

    bq(U, RE11, 'REV11', '3(i)', 'Find the area of triangle ABC when a = 5.2 cm, β = 30°, γ = 40°.',
       '▲ ≈ 4.62 square units (key: 4.6).',
       'α = 180° − 30° − 40° = 110°. Using one side and two angles: '
       '▲ = ½a<sup>2</sup> sin β sin γ/sin α = ½(5.2)<sup>2</sup>(sin 30°)(sin 40°)/sin 110° '
       '= 13.52(0.5)(0.64279)/0.93969 = 4.62 square units.', 340),
    bq(U, RE11, 'REV11', '3(ii)', 'Find the area of triangle ABC when a = 125 cm, b = 120 cm, γ = 150°.',
       '▲ = 3750 square units.',
       'The included angle between a and b is γ, so ▲ = ½ab sin γ = ½(125)(120) sin 150° = 7500(0.5) = 3750 square units.', 340),

    bq(U, RE11, 'REV11', '4(i)', 'Find R and r of ΔABC when a = 18.8 cm, b = 24.5 cm, c = 30.2 cm.',
       'R ≈ 15.12 cm, r ≈ 6.26 cm.',
       's = ½(18.8 + 24.5 + 30.2) = 36.75; s − a = 17.95, s − b = 12.25, s − c = 6.55. '
       '▲ = √(36.75 × 17.95 × 12.25 × 6.55) = √52,929 = 230.06 cm<sup>2</sup>. '
       'R = abc/(4▲) = (18.8)(24.5)(30.2)/(4 × 230.06) = 13,909.7/920.24 = 15.12 cm; '
       'r = ▲/s = 230.06/36.75 = 6.26 cm. (Printed key: R = 15.1 cm, r = 6.3 cm.)', 340),
    bq(U, RE11, 'REV11', '4(ii)', 'Find R and r of ΔABC when a = 13.8 cm, b = 13.8 cm, c = 10.4 cm.',
       'R ≈ 7.45 cm, r ≈ 3.50 cm.',
       's = ½(13.8 + 13.8 + 10.4) = 19; s − a = 5.2, s − b = 5.2, s − c = 8.6. '
       '▲ = √(19 × 5.2 × 5.2 × 8.6) = √4418.3 = 66.47 cm<sup>2</sup>. '
       'R = abc/(4▲) = (13.8)(13.8)(10.4)/(4 × 66.47) = 1980.58/265.88 = 7.45 cm; '
       'r = ▲/s = 66.47/19 = 3.50 cm.', 340),

    bq(U, RE11, 'REV11', '5', 'Find r<sub>1</sub>, r<sub>2</sub> and r<sub>3</sub> of the escribed circles, if the measures of the sides of triangle ABC are a = 3 cm, b = 4 cm and c = 5 cm.',
       'r<sub>1</sub> = 2 cm, r<sub>2</sub> = 3 cm, r<sub>3</sub> = 6 cm.',
       'a = 3, b = 4, c = 5 is right-angled at C, so s = ½(3 + 4 + 5) = 6 and ▲ = ½(3)(4) = 6 cm<sup>2</sup> '
       '(Hero\u2019s formula: √(6 × 3 × 2 × 1) = 6). '
       'r<sub>1</sub> = ▲/(s − a) = 6/3 = 2 cm; r<sub>2</sub> = ▲/(s − b) = 6/2 = 3 cm; r<sub>3</sub> = ▲/(s − c) = 6/1 = 6 cm.', 340),

    bq(U, RE11, 'REV11', '6', 'A hiker walks due east at 4 km per hour and a second hiker, starting at the same point, walks 55° north-east at the rate of 5 km per hour. How far apart will they be after 3 hours?',
       '≈ 8.61 km apart (≈ 8.6 km).',
       'After 3 hours the first hiker has walked 4 × 3 = 12 km due east and the second 5 × 3 = 15 km in the direction 55° east of north (bearing N55°E). '
       'The angle between due east and N55°E is 90° − 55° = 35°, so by the law of cosines '
       'd<sup>2</sup> = 12<sup>2</sup> + 15<sup>2</sup> − 2(12)(15)cos 35° = 144 + 225 − 360(0.81915) = 369 − 294.89 = 74.11 ⇒ d = 8.61 km. '
       'Reading 55° from the east axis instead would give 12.75 km; the printed key 8.6 km confirms the bearing interpretation used here.', 340),
    bq(U, RE11, 'REV11', '7', 'Three points A, B, C form a triangle such that the ratio of the measures of their angles is 1 : 2 : 3. Find the ratio of the lengths of the sides.',
       'a : b : c = 1 : √3 : 2.',
       'Let the angles be x, 2x, 3x. Then x + 2x + 3x = 180° ⇒ x = 30°, so the angles are 30°, 60°, 90°. '
       'By the law of sines the sides are proportional to the sines of the opposite angles: '
       'sin 30° : sin 60° : sin 90° = ½ : √3/2 : 1 = 1 : √3 : 2.', 340),
    bq(U, RE11, 'REV11', '8', 'A piece of plastic strip 1 metre long is bent to form an isosceles triangle with 95° as measure of its largest angle. Find the length of the sides.',
       'Equal sides ≈ 28.78 cm each; base ≈ 42.44 cm.',
       'Let each equal side be x metres; the largest angle 95° is the vertex angle between them, so the base is '
       'b = 2x sin 47.5°. Perimeter: 2x + 2x sin 47.5° = 1 ⇒ 2x(1 + 0.73728) = 1 ⇒ x = 1/3.47456 = 0.28780 m = 28.78 cm. '
       'Base = 1 − 2(0.28780) = 0.42440 m = 42.44 cm.', 340,
       'Isosceles triangle: vertex angle 95°, base angles 42.5° each, equal sides x, base 2x sin 47.5°, perimeter 1 m.'),
    bq(U, RE11, 'REV11', '9', 'Two airplanes leave a field at the same time. One flies 30° East of North at 250 km/h, the other 45° East of South at 300 km/h. How far apart are they at the end of 2 hours?',
       '≈ 874.8 km apart.',
       'Distances flown: 250 × 2 = 500 km and 300 × 2 = 600 km. The first course is 30° east of north and the second 45° east of south, '
       'so the angle between the two courses is 180° − 30° − 45° = 105°. '
       'd<sup>2</sup> = 500<sup>2</sup> + 600<sup>2</sup> − 2(500)(600)cos 105° = 250,000 + 360,000 + 155,291 = 765,291 ⇒ d = 874.8 km.', 340),
    bq(U, RE11, 'REV11', '10', 'Two men are on the opposite sides of a 100 m high tower. If the measures of the angles of elevation of the top of the tower are 18° and 22° respectively, find the distance between them.',
       '≈ 555.3 m.',
       'Distances from the foot of the tower: x<sub>1</sub> = 100/tan 18° = 100/0.32492 = 307.77 m and '
       'x<sub>2</sub> = 100/tan 22° = 100/0.40403 = 247.51 m. Since the men are on opposite sides, '
       'distance = 307.77 + 247.51 = 555.28 ≈ 555 m.', 340),
    bq(U, RE11, 'REV11', '11', 'A man standing 60 m away from a tower notices that the angles of elevation of the top and the bottom of a flagstaff on the top of the tower are 64° and 62° respectively. Find the length of the flagstaff.',
       '≈ 10.17 m.',
       'Height of the top of the flagstaff = 60 tan 64° = 60(2.05030) = 123.02 m; '
       'height of the top of the tower = 60 tan 62° = 60(1.88073) = 112.84 m. '
       'Length of the flagstaff = 123.02 − 112.84 = 10.17 ≈ 10.2 m.', 340),
    bq(U, RE11, 'REV11', '12', 'The angle of elevation of the top of a 60 m high tower from a point A, on the same level as the foot of the tower, is 25°. Find the angle of elevation of the top of the tower from a point B, 20 m nearer to A from the foot of the tower.',
       'θ ≈ 28°54′.',
       'Distance of A from the foot = 60/tan 25° = 60/0.46631 = 128.67 m. '
       'B is 20 m nearer, so its distance is 128.67 − 20 = 108.67 m. '
       'tan θ = 60/108.67 = 0.55213 ⇒ θ = tan<sup>−1</sup>(0.55213) = 28.90° = 28°54′.', 340),
    bq(U, RE11, 'REV11', '13', 'Two buildings A and B are 100 m apart. The angle of elevation from the top of the building A to the top of the building B is 20°. The angle of elevation from the base of the building B to the top of the building A is 50°. Find the height of the building B.',
       'Height of building B ≈ 155.6 m (key: 155.5 m).',
       'Height of building A = 100 tan 50° = 100(1.19175) = 119.18 m (angle of elevation from the base of B, 100 m away). '
       'The top of B is 100 tan 20° = 100(0.36397) = 36.40 m above the top of A. '
       'Height of B = 119.18 + 36.40 = 155.58 ≈ 155.6 m.', 340,
       'Two vertical buildings A and B, 100 m apart on level ground; height of A is 100 tan 50°, and the top of B is 100 tan 20° above the top of A.'),
]
