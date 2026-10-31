import json, os

def q(chapter, section, sectionCode, type_, number, question, answer, explanation="", pdfPage=0, bookPage=0, figure=None, options=None, optionsRaw=None, correctAnswer=None):
    return {
        "id": f"physics_ix_{chapter.lower().replace(' ', '_')}_q{number}",
        "chapter": chapter,
        "section": section,
        "sectionCode": sectionCode,
        "type": type_,
        "number": number,
        "question": question,
        "answer": answer,
        "explanation": explanation,
        "pdfPage": pdfPage,
        "bookPage": bookPage,
        "figure": figure,
        "options": options,
        "optionsRaw": optionsRaw,
        "correctAnswer": correctAnswer
    }

data = []

# ============ UNIT 1: Physical Quantities and Measurement ============
chapter = "Physical Quantities and Measurement"

# Section A: MCQs (10 questions)
data.append(q(chapter, "Section A", "A", "mcq", 1,
    "The least count of a metre rule is:",
    "1 mm",
    "A metre rule has markings in millimetres, so its least count is 1 mm.",
    pdfPage=29, bookPage=26,
    options=["1 mm", "1 cm", "0.1 mm", "0.01 mm"],
    optionsRaw="a) 1 mm  b) 1 cm  c) 0.1 mm  d) 0.01 mm",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 2,
    "The least count of a Vernier calliper is:",
    "0.1 mm",
    "Vernier callipers can measure up to 0.1 mm precision.",
    pdfPage=29, bookPage=26,
    options=["0.1 mm", "0.01 mm", "1 mm", "0.001 mm"],
    optionsRaw="a) 0.1 mm  b) 0.01 mm  c) 1 mm  d) 0.001 mm",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 3,
    "The least count of a screw gauge is:",
    "0.01 mm",
    "Screw gauge has the smallest least count of 0.01 mm among common measuring instruments.",
    pdfPage=29, bookPage=26,
    options=["0.01 mm", "0.1 mm", "1 mm", "0.001 mm"],
    optionsRaw="a) 0.01 mm  b) 0.1 mm  c) 1 mm  d) 0.001 mm",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 4,
    "One light year is equal to:",
    "9.46 × 10¹⁵ m",
    "Light travels approximately 9.46 × 10¹⁵ metres in one year.",
    pdfPage=29, bookPage=26,
    options=["9.46 × 10¹⁵ m", "9.46 × 10¹² m", "9.46 × 10¹⁰ m", "9.46 × 10⁸ m"],
    optionsRaw="a) 9.46 × 10¹⁵ m  b) 9.46 × 10¹² m  c) 9.46 × 10¹ m  d) 9.46 × 10⁸ m",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 5,
    "The number of base units in SI is:",
    "7",
    "SI has 7 base units: metre, kilogram, second, ampere, kelvin, mole, and candela.",
    pdfPage=29, bookPage=26,
    options=["7", "6", "5", "4"],
    optionsRaw="a) 7  b) 6  c) 5  d) 4",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 6,
    "Which of the following is a derived unit?",
    "Newton",
    "Newton is derived from kg·m/s², making it a derived unit.",
    pdfPage=29, bookPage=26,
    options=["Newton", "Metre", "Kilogram", "Second"],
    optionsRaw="a) Newton  b) Metre  c) Kilogram  d) Second",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 7,
    "The unit of pressure is:",
    "Pascal",
    "Pressure = Force/Area, measured in N/m² = Pascal.",
    pdfPage=29, bookPage=26,
    options=["Pascal", "Newton", "Joule", "Watt"],
    optionsRaw="a) Pascal  b) Newton  c) Joule  d) Watt",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 8,
    "1 litre is equal to:",
    "1000 cm³",
    "1 litre = 1000 cm³ = 1 dm³.",
    pdfPage=29, bookPage=26,
    options=["1000 cm³", "100 cm³", "10 cm³", "1 cm³"],
    optionsRaw="a) 1000 cm³  b) 100 cm³  c) 10 cm³  d) 1 cm³",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 9,
    "The prefix 'mega' represents:",
    "10⁶",
    "Mega represents one million or 10.",
    pdfPage=29, bookPage=26,
    options=["10⁶", "10³", "10⁹", "10¹²"],
    optionsRaw="a) 10⁶  b) 10³  c) 10⁹  d) 10¹²",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 10,
    "The most precise measurement is:",
    "5.00 mm",
    "More decimal places indicate greater precision. 5.00 mm has 3 significant figures.",
    pdfPage=29, bookPage=26,
    options=["5.00 mm", "5.0 mm", "5 mm", "50 mm"],
    optionsRaw="a) 5.00 mm  b) 5.0 mm  c) 5 mm  d) 50 mm",
    correctAnswer="a"))

# Section B: Structured Questions
data.append(q(chapter, "Section B", "B", "structured", 1,
    "Define base quantities and derived quantities.",
    "Base quantities are fundamental physical quantities that cannot be defined in terms of other quantities (e.g., length, mass, time). Derived quantities are formed by combining base quantities through multiplication or division (e.g., speed = length/time, force = mass × acceleration).",
    pdfPage=30, bookPage=27))

data.append(q(chapter, "Section B", "B", "structured", 2,
    "What is the difference between a metre rule and a Vernier calliper?",
    "A metre rule measures length with a least count of 1 mm, while a Vernier calliper measures with greater precision, having a least count of 0.1 mm. Vernier callipers can also measure internal and external diameters.",
    pdfPage=30, bookPage=27))

data.append(q(chapter, "Section B", "B", "structured", 3,
    "Convert 2.5 km into metres.",
    "2.5 km = 2.5 × 1000 m = 2500 m",
    pdfPage=30, bookPage=27))

data.append(q(chapter, "Section B", "B", "structured", 4,
    "Express 0.00045 in scientific notation.",
    "0.00045 = 4.5 × 10⁻⁴",
    pdfPage=30, bookPage=27))

data.append(q(chapter, "Section B", "B", "structured", 5,
    "How many significant figures are in 0.00580?",
    "3 significant figures. Leading zeros are not significant, but the trailing zero after the decimal is significant.",
    pdfPage=30, bookPage=27))

data.append(q(chapter, "Section B", "B", "structured", 6,
    "Define the term 'least count'.",
    "Least count is the smallest measurement that can be accurately made with a measuring instrument. It determines the precision of the instrument.",
    pdfPage=30, bookPage=27))

data.append(q(chapter, "Section B", "B", "structured", 7,
    "What is the SI unit of mass? Define it.",
    "The SI unit of mass is the kilogram (kg). It is defined as the mass of the international prototype of the kilogram, a platinum-iridium cylinder kept at the International Bureau of Weights and Measures in France.",
    pdfPage=30, bookPage=27))

data.append(q(chapter, "Section B", "B", "structured", 8,
    "Differentiate between accuracy and precision.",
    "Accuracy refers to how close a measurement is to the true value. Precision refers to how close repeated measurements are to each other, indicating the reproducibility of results.",
    pdfPage=30, bookPage=27))

data.append(q(chapter, "Section B", "B", "structured", 9,
    "Calculate the area of a rectangle with length 5.2 cm and width 3.1 cm.",
    "Area = length × width = 5.2 cm × 3.1 cm = 16.12 cm² ≈ 16 cm² (to 2 significant figures)",
    pdfPage=30, bookPage=27))

data.append(q(chapter, "Section B", "B", "structured", 10,
    "Why is scientific notation useful in physics?",
    "Scientific notation is useful for expressing very large or very small numbers compactly, making calculations easier and reducing errors. It also clearly shows the number of significant figures.",
    pdfPage=30, bookPage=27))

# ============ UNIT 2: Kinematics ============
chapter = "Kinematics"

# Section A: MCQs (8 questions)
data.append(q(chapter, "Section A", "A", "mcq", 1,
    "A body is in motion if it:",
    "Changes its position with respect to surroundings",
    "Motion is defined as change in position relative to a reference point.",
    pdfPage=59, bookPage=56,
    options=["Changes its position with respect to surroundings", "Remains at rest", "Moves in a straight line", "Moves with constant speed"],
    optionsRaw="a) Changes its position with respect to surroundings  b) Remains at rest  c) Moves in a straight line  d) Moves with constant speed",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 2,
    "The shortest distance between two points is called:",
    "Displacement",
    "Displacement is the shortest straight-line distance between initial and final positions.",
    pdfPage=59, bookPage=56,
    options=["Displacement", "Distance", "Speed", "Velocity"],
    optionsRaw="a) Displacement  b) Distance  c) Speed  d) Velocity",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 3,
    "The rate of change of displacement is called:",
    "Velocity",
    "Velocity = change in displacement / time taken.",
    pdfPage=59, bookPage=56,
    options=["Velocity", "Speed", "Acceleration", "Momentum"],
    optionsRaw="a) Velocity  b) Speed  c) Acceleration  d) Momentum",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 4,
    "A body moving with uniform velocity has:",
    "Zero acceleration",
    "If velocity is constant (uniform), there is no change in velocity, hence acceleration is zero.",
    pdfPage=59, bookPage=56,
    options=["Zero acceleration", "Constant acceleration", "Variable acceleration", "Negative acceleration"],
    optionsRaw="a) Zero acceleration  b) Constant acceleration  c) Variable acceleration  d) Negative acceleration",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 5,
    "The area under a velocity-time graph gives:",
    "Displacement",
    "Area under velocity-time graph = velocity × time = displacement.",
    pdfPage=59, bookPage=56,
    options=["Displacement", "Velocity", "Acceleration", "Speed"],
    optionsRaw="a) Displacement  b) Velocity  c) Acceleration  d) Speed",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 6,
    "The slope of a distance-time graph gives:",
    "Speed",
    "Slope = change in distance / change in time = speed.",
    pdfPage=59, bookPage=56,
    options=["Speed", "Velocity", "Acceleration", "Displacement"],
    optionsRaw="a) Speed  b) Velocity  c) Acceleration  d) Displacement",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 7,
    "When a body is thrown vertically upward, its velocity at the highest point is:",
    "Zero",
    "At the highest point, the body momentarily stops before falling back, so velocity is zero.",
    pdfPage=59, bookPage=56,
    options=["Zero", "Maximum", "Minimum", "Equal to initial velocity"],
    optionsRaw="a) Zero  b) Maximum  c) Minimum  d) Equal to initial velocity",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 8,
    "The acceleration due to gravity on Earth's surface is approximately:",
    "9.8 m/s²",
    "Standard value of g on Earth's surface is approximately 9.8 m/s².",
    pdfPage=59, bookPage=56,
    options=["9.8 m/s²", "10 m/s²", "9.8 m/s", "10 m/s"],
    optionsRaw="a) 9.8 m/s²  b) 10 m/s²  c) 9.8 m/s  d) 10 m/s",
    correctAnswer="a"))

# Section B: Structured Questions
data.append(q(chapter, "Section B", "B", "structured", 1,
    "Differentiate between distance and displacement.",
    "Distance is the total path length covered by a body (scalar quantity, always positive). Displacement is the shortest straight-line distance from initial to final position with direction (vector quantity, can be positive, negative, or zero).",
    pdfPage=60, bookPage=57))

data.append(q(chapter, "Section B", "B", "structured", 2,
    "A car travels 100 m east and then 50 m west. Find the total distance and displacement.",
    "Total distance = 100 m + 50 m = 150 m. Displacement = 100 m - 50 m = 50 m east.",
    pdfPage=60, bookPage=57))

data.append(q(chapter, "Section B", "B", "structured", 3,
    "Define uniform and non-uniform velocity.",
    "Uniform velocity: A body covers equal displacements in equal intervals of time. Non-uniform velocity: A body covers unequal displacements in equal intervals of time.",
    pdfPage=60, bookPage=57))

data.append(q(chapter, "Section B", "B", "structured", 4,
    "A train starting from rest attains a velocity of 20 m/s in 10 seconds. Find its acceleration.",
    "Using v = u + at: 20 = 0 + a(10), so a = 2 m/s²",
    pdfPage=60, bookPage=57))

data.append(q(chapter, "Section B", "B", "structured", 5,
    "Derive the first equation of motion: v = u + at",
    "Acceleration a = (v - u)/t. Rearranging: at = v - u, therefore v = u + at.",
    pdfPage=60, bookPage=57))

data.append(q(chapter, "Section B", "B", "structured", 6,
    "A ball is thrown vertically upward with velocity 30 m/s. How high will it go? (g = 10 m/s²)",
    "Using v² = u² + 2as: 0 = 30² + 2(-10)s, so 0 = 900 - 20s, s = 45 m",
    pdfPage=60, bookPage=57))

data.append(q(chapter, "Section B", "B", "structured", 7,
    "Sketch a distance-time graph for a body at rest.",
    "The graph is a horizontal straight line parallel to the time axis, showing that distance does not change with time.",
    pdfPage=60, bookPage=57, figure="horizontal_line_graph"))

data.append(q(chapter, "Section B", "B", "structured", 8,
    "What information can be obtained from the slope of a velocity-time graph?",
    "The slope of a velocity-time graph gives the acceleration of the body. Positive slope indicates positive acceleration, negative slope indicates deceleration.",
    pdfPage=60, bookPage=57))

# ============ UNIT 3: Dynamics ============
chapter = "Dynamics"

# Section A: MCQs (6 questions)
data.append(q(chapter, "Section A", "A", "mcq", 1,
    "The rate of change of momentum is equal to:",
    "Force",
    "Newton's Second Law: F = dp/dt (force equals rate of change of momentum).",
    pdfPage=85, bookPage=82,
    options=["Force", "Acceleration", "Velocity", "Impulse"],
    optionsRaw="a) Force  b) Acceleration  c) Velocity  d) Impulse",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 2,
    "Newton's first law of motion is also known as:",
    "Law of inertia",
    "Newton's first law states that a body remains at rest or in uniform motion unless acted upon by a force - this is the law of inertia.",
    pdfPage=85, bookPage=82,
    options=["Law of inertia", "Law of momentum", "Law of acceleration", "Law of action-reaction"],
    optionsRaw="a) Law of inertia  b) Law of momentum  c) Law of acceleration  d) Law of action-reaction",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 3,
    "The mass of a body is a measure of its:",
    "Inertia",
    "Mass quantifies the inertia of a body - its resistance to change in motion.",
    pdfPage=85, bookPage=82,
    options=["Inertia", "Weight", "Volume", "Density"],
    optionsRaw="a) Inertia  b) Weight  c) Volume  d) Density",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 4,
    "Action and reaction forces act on:",
    "Different bodies",
    "Newton's third law: action and reaction forces act on two different bodies, not the same body.",
    pdfPage=85, bookPage=82,
    options=["Different bodies", "Same body", "Either same or different", "Neither"],
    optionsRaw="a) Different bodies  b) Same body  c) Either same or different  d) Neither",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 5,
    "The unit of momentum is:",
    "kg·m/s",
    "Momentum = mass × velocity, so unit is kg·m/s.",
    pdfPage=85, bookPage=82,
    options=["kg·m/s", "N·s", "Both a and b", "Neither"],
    optionsRaw="a) kg·m/s  b) N·s  c) Both a and b  d) Neither",
    correctAnswer="c"))

data.append(q(chapter, "Section A", "A", "mcq", 6,
    "Friction force always acts:",
    "Opposite to the direction of motion",
    "Friction opposes relative motion between surfaces in contact.",
    pdfPage=85, bookPage=82,
    options=["Opposite to the direction of motion", "In the direction of motion", "Perpendicular to motion", "At any angle"],
    optionsRaw="a) Opposite to the direction of motion  b) In the direction of motion  c) Perpendicular to motion  d) At any angle",
    correctAnswer="a"))

# Section B: Structured Questions
data.append(q(chapter, "Section B", "B", "structured", 1,
    "State Newton's second law of motion and derive F = ma.",
    "Newton's second law: The rate of change of momentum of a body is directly proportional to the applied force. F = dp/dt = d(mv)/dt = m(dv/dt) = ma (for constant mass).",
    pdfPage=86, bookPage=83))

data.append(q(chapter, "Section B", "B", "structured", 2,
    "A force of 20 N acts on a body of mass 5 kg. Find its acceleration.",
    "Using F = ma: 20 = 5a, so a = 4 m/s²",
    pdfPage=86, bookPage=83))

data.append(q(chapter, "Section B", "B", "structured", 3,
    "Explain the law of conservation of momentum with an example.",
    "In an isolated system, total momentum before collision equals total momentum after collision. Example: When a gun fires a bullet, the gun recoils backward. Momentum of bullet forward = momentum of gun backward.",
    pdfPage=86, bookPage=83))

data.append(q(chapter, "Section B", "B", "structured", 4,
    "Differentiate between mass and weight.",
    "Mass is the amount of matter in a body (scalar, constant everywhere, measured in kg). Weight is the gravitational force on a body (vector, varies with location, W = mg, measured in Newtons).",
    pdfPage=86, bookPage=83))

data.append(q(chapter, "Section B", "B", "structured", 5,
    "Why does a passenger fall forward when a bus stops suddenly?",
    "Due to inertia of motion. The passenger's body tends to continue moving forward when the bus stops suddenly, causing them to fall forward.",
    pdfPage=86, bookPage=83))

data.append(q(chapter, "Section B", "B", "structured", 6,
    "Calculate the force required to stop a 1000 kg car moving at 20 m/s in 5 seconds.",
    "Using F = ma = m(v-u)/t = 1000(0-20)/5 = -4000 N. The negative sign indicates opposing force. Magnitude = 4000 N.",
    pdfPage=86, bookPage=83))

data.append(q(chapter, "Section B", "B", "structured", 7,
    "State Newton's third law of motion with two examples.",
    "For every action, there is an equal and opposite reaction. Examples: (1) Walking - foot pushes ground backward, ground pushes foot forward. (2) Swimming - hands push water backward, water pushes swimmer forward.",
    pdfPage=86, bookPage=83))

data.append(q(chapter, "Section B", "B", "structured", 8,
    "What is the role of friction in our daily life? Give two advantages and two disadvantages.",
    "Advantages: (1) Enables walking without slipping. (2) Allows vehicles to brake. Disadvantages: (1) Causes wear and tear of machines. (2) Reduces efficiency by converting kinetic energy to heat.",
    pdfPage=86, bookPage=83))

# ============ UNIT 4: Turning Effect of Forces ============
chapter = "Turning Effect of Forces"

# Section A: MCQs (10 questions)
data.append(q(chapter, "Section A", "A", "mcq", 1,
    "A pair of unlike parallel forces having different lines of force produce:",
    "a couple",
    "Two unlike parallel forces with different lines of action form a couple, producing rotation.",
    pdfPage=113, bookPage=110,
    options=["equilibrium", "torque", "a couple", "unstable equilibrium"],
    optionsRaw="a) equilibrium  b) torque  c) a couple  d) unstable equilibrium",
    correctAnswer="c"))

data.append(q(chapter, "Section A", "A", "mcq", 2,
    "Head-to-tail rule can be used to add:",
    "any number of forces",
    "The head-to-tail rule can be used to add any number of vector forces.",
    pdfPage=113, bookPage=110,
    options=["two", "three", "five", "any number of"],
    optionsRaw="a) two  b) three  c) five  d) any number of",
    correctAnswer="d"))

data.append(q(chapter, "Section A", "A", "mcq", 3,
    "A force of 15 N makes an angle of 60° with horizontal. Its vertical component will be:",
    "13 N",
    "Vertical component = F sin θ = 15 × sin 60° = 15 × 0.866 ≈ 13 N",
    pdfPage=113, bookPage=110,
    options=["15 N", "10 N", "13 N", "7 N"],
    optionsRaw="a) 15 N  b) 10 N  c) 13 N  d) 7 N",
    correctAnswer="c"))

data.append(q(chapter, "Section A", "A", "mcq", 4,
    "A body is in equilibrium when it has:",
    "zero acceleration",
    "In equilibrium, net force is zero, so acceleration is zero (body is at rest or moving with uniform velocity).",
    pdfPage=113, bookPage=110,
    options=["uniform speed", "uniform acceleration", "both (a) and (b)", "zero acceleration"],
    optionsRaw="a) uniform speed  b) uniform acceleration  c) both (a) and (b)  d) zero acceleration",
    correctAnswer="d"))

data.append(q(chapter, "Section A", "A", "mcq", 5,
    "A body is in stable equilibrium after slight tilt if its Centre of gravity:",
    "is at lowest position",
    "In stable equilibrium, the centre of gravity rises when tilted and returns to lowest position when released.",
    pdfPage=113, bookPage=110,
    options=["remains above the point of contact", "remains on one side of point of contact", "passes over the point of contact", "is at lowest position"],
    optionsRaw="a) remains above the point of contact  b) remains on one side of point of contact  c) passes over the point of contact  d) is at lowest position",
    correctAnswer="d"))

data.append(q(chapter, "Section A", "A", "mcq", 6,
    "A body is in unstable equilibrium after slight tilt if its center of gravity:",
    "remains on one side of the point of contact",
    "In unstable equilibrium, the centre of gravity moves to one side and doesn't return to original position.",
    pdfPage=113, bookPage=110,
    options=["remains on one side of the point of contact", "remains above the point of contact", "passes over the point of contact", "is positioned at its bottom"],
    optionsRaw="a) remains on one side of the point of contact  b) remains above the point of contact  c) passes over the point of contact  d) is positioned at its bottom",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 7,
    "A body is in neutral equilibrium when its Centre of gravity:",
    "Remains at same height",
    "In neutral equilibrium, the centre of gravity remains at the same height when the body is displaced.",
    pdfPage=114, bookPage=111,
    options=["Is at the lowest position", "Remains at same height", "Is at highest position", "Is at its base"],
    optionsRaw="a) Is at the lowest position  b) Remains at same height  c) Is at highest position  d) Is at its base",
    correctAnswer="b"))

data.append(q(chapter, "Section A", "A", "mcq", 8,
    "Bunsen burner is made stable by:",
    "Increasing its base area",
    "Stability increases with larger base area and lower centre of gravity.",
    pdfPage=114, bookPage=111,
    options=["Increasing its length", "Increasing its mass", "Decreasing its base area", "Increasing its base area"],
    optionsRaw="a) Increasing its length  b) Increasing its mass  c) Decreasing its base area  d) Increasing its base area",
    correctAnswer="d"))

data.append(q(chapter, "Section A", "A", "mcq", 9,
    "A tight rope walker carries a long pole to:",
    "Lower his Centre of gravity",
    "The long pole lowers the combined centre of gravity, increasing stability.",
    pdfPage=114, bookPage=111,
    options=["Increase his weight", "Raise his Centre of gravity", "Lower his Centre of gravity", "Keep his Centre of gravity in fixed position"],
    optionsRaw="a) Increase his weight  b) Raise his Centre of gravity  c) Lower his Centre of gravity  d) Keep his Centre of gravity in fixed position",
    correctAnswer="c"))

data.append(q(chapter, "Section A", "A", "mcq", 10,
    "Stability of a racing car is increased by:",
    "Lowering its Centre of gravity",
    "Racing cars have low centres of gravity and wide bases for maximum stability during turns.",
    pdfPage=114, bookPage=111,
    options=["Increasing its height", "Raising its Centre of gravity", "Decreasing its width", "Lowering its Centre of gravity"],
    optionsRaw="a) Increasing its height  b) Raising its Centre of gravity  c) Decreasing its width  d) Lowering its Centre of gravity",
    correctAnswer="d"))

# Section B: Structured Questions
data.append(q(chapter, "Section B", "B", "structured", 1,
    "a) Define like and unlike forces. b) A pair of like parallel forces 15N each are acting on a body. Find their resultant. c) Two unlike parallel forces 10 N each acting along same line. Find their resultant.",
    "a) Like forces act in the same direction; unlike forces act in opposite directions. b) Resultant of like forces = 15 + 15 = 30 N. c) Resultant of unlike forces = 10 - 10 = 0 N.",
    pdfPage=112, bookPage=112))

data.append(q(chapter, "Section B", "B", "structured", 2,
    "a) Describe the head-to-tail rule of vector addition of forces. b) Three forces 12 N along x-axis, 8 N making an angle of 45° with x-axis and 8 N along y-axis. i) Find their resultant ii) Find the direction of resultant.",
    "a) Head-to-tail rule: Draw vectors head to tail; resultant is from tail of first to head of last. b) Fx = 12 + 8cos45° = 12 + 5.66 = 17.66 N; Fy = 8sin45° + 8 = 5.66 + 8 = 13.66 N. Resultant = √(17.66² + 13.66²) = √(311.88 + 186.60) = √498.48 ≈ 22.33 N. Direction: θ = tan⁻¹(13.66/17.66) ≈ 37.7°",
    pdfPage=112, bookPage=112))

data.append(q(chapter, "Section B", "B", "structured", 3,
    "a) How a force can be resolved into its perpendicular components? b) A gardener is driving a lawnmower with a force of 80 N that makes an angle of 40° with the ground. i) Find its horizontal component ii) Find its vertical component.",
    "a) A force F at angle θ can be resolved into Fx = F cos θ (horizontal) and Fy = F sin θ (vertical). b) Fx = 80 cos 40° = 80 × 0.766 = 61.28 N; Fy = 80 sin 40° = 80 × 0.643 = 51.44 N.",
    pdfPage=112, bookPage=112))

data.append(q(chapter, "Section B", "B", "structured", 4,
    "a) How can you determine a force from its rectangular components? b) Horizontal and vertical components of a force are 4 N and 3 N respectively. Find i) Resultant force ii) Direction of resultant.",
    "a) F = √(Fx² + Fy²) and θ = tan⁻¹(Fy/Fx). b) i) F = √(4² + 3²) = √(16+9) = √25 = 5 N. ii) θ = tan⁻¹(3/4) = tan⁻¹(0.75) ≈ 36.87°",
    pdfPage=112, bookPage=112))

data.append(q(chapter, "Section B", "B", "structured", 5,
    "a) What do you mean by moment of force? b) A spanner of 0.3 m length can produce a torque of 300 Nm. i) Determine the force applied on it. ii) What should be the length of the spanner if torque is to be increased to 500 Nm with same applied force?",
    "a) Moment of force (torque) = Force × perpendicular distance from pivot. b) i) τ = F × d, so 300 = F × 0.3, F = 1000 N. ii) 500 = 1000 × d, d = 0.5 m.",
    pdfPage=113, bookPage=113))

data.append(q(chapter, "Section B", "B", "structured", 6,
    "a) State the principle of moment. b) A uniform meter rule is supported at its center is balanced by two forces 12 N and 20 N. i) If 20 N force is placed at a distance of 3 m from pivot find the position of 12 N force on the other side of pivot. ii) If the 20 N force is moved to 4 cm from pivot then find force to replace 12 N force.",
    "a) Principle of moments: For a body in equilibrium, sum of clockwise moments = sum of anticlockwise moments. b) i) 20 × 3 = 12 × d, d = 60/12 = 5 m. ii) 20 × 4 = F × d, need more information about d to find F.",
    pdfPage=113, bookPage=113))

data.append(q(chapter, "Section B", "B", "structured", 7,
    "a) Define Center of mass and Center of gravity. b) How will you determine the Center of mass and Center of gravity?",
    "a) Center of mass: Point where entire mass of body is concentrated. Center of gravity: Point where entire weight of body acts. For uniform gravitational field, both coincide. b) Center of gravity can be found by suspension method or balancing method.",
    pdfPage=113, bookPage=113))

data.append(q(chapter, "Section B", "B", "structured", 8,
    "a) Define couple as a pair of forces tending to produce torque. b) A mechanic uses a double arm spanner to turn a nut. He applies a force of 15 N at each end of the spanner and produces a torque of 60 Nm. What is the length of the moment arm of the couple?",
    "a) A couple consists of two equal and opposite parallel forces not acting along the same line, producing pure rotation. b) Torque of couple = F × d (distance between forces). 60 = 15 × d, d = 4 m. Moment arm = d/2 = 2 m.",
    pdfPage=113, bookPage=113))

# ============ UNIT 5: Forces and Matter ============
chapter = "Forces and Matter"

# Section A: MCQs (7 questions)
data.append(q(chapter, "Section A", "A", "mcq", 1,
    "Springs are used in brakes and clutches because they:",
    "Can store elastic potential energy",
    "Springs store energy when compressed and release it, making them useful in brakes and clutches.",
    pdfPage=130, bookPage=127,
    options=["Can store elastic potential energy", "Are rigid", "Cannot deform", "Have high density"],
    optionsRaw="a) Can store elastic potential energy  b) Are rigid  c) Cannot deform  d) Have high density",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 2,
    "Elastic deformation is:",
    "Temporary deformation",
    "Elastic deformation is temporary; the body returns to original shape when force is removed.",
    pdfPage=130, bookPage=127,
    options=["Temporary deformation", "Permanent deformation", "No deformation", "Plastic deformation"],
    optionsRaw="a) Temporary deformation  b) Permanent deformation  c) No deformation  d) Plastic deformation",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 3,
    "Which of the following is an elastic material?",
    "Steel",
    "Steel is highly elastic and returns to original shape after deformation.",
    pdfPage=130, bookPage=127,
    options=["Steel", "Plasticine", "Putty", "Wax"],
    optionsRaw="a) Steel  b) Plasticine  c) Putty  d) Wax",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 4,
    "The spring constant depends on:",
    "Material and dimensions of spring",
    "Spring constant k depends on the material, length, and cross-sectional area of the spring.",
    pdfPage=130, bookPage=127,
    options=["Material and dimensions of spring", "Applied force only", "Extension only", "Temperature only"],
    optionsRaw="a) Material and dimensions of spring  b) Applied force only  c) Extension only  d) Temperature only",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 5,
    "The unit of spring constant is:",
    "N/m",
    "From Hooke's law F = kx, k = F/x, so unit is N/m.",
    pdfPage=130, bookPage=127,
    options=["N/m", "N·m", "N/m²", "N"],
    optionsRaw="a) N/m  b) N·m  c) N/m²  d) N",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 6,
    "Hooke's law graph between load and extension is:",
    "Straight line through origin",
    "Hooke's law states F  x, so the graph is a straight line passing through origin (within elastic limit).",
    pdfPage=130, bookPage=127,
    options=["Straight line through origin", "Curve", "Horizontal line", "Vertical line"],
    optionsRaw="a) Straight line through origin  b) Curve  c) Horizontal line  d) Vertical line",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 7,
    "The unit of pressure is:",
    "Pascal",
    "Pressure = Force/Area = N/m² = Pascal (Pa).",
    pdfPage=130, bookPage=127,
    options=["Pascal", "Newton", "Joule", "Watt"],
    optionsRaw="a) Pascal  b) Newton  c) Joule  d) Watt",
    correctAnswer="a"))

# Section B: Structured Questions
data.append(q(chapter, "Section B", "B", "structured", 1,
    "A student hangs different loads on a spring and measures the extension. Load (N): 0, 1, 2, 3, 4, 5. Extension (cm): 0, 2, 4, 6, 8, 10. Plot a graph and find the spring constant.",
    "The graph is a straight line through origin. Spring constant k = F/x = 1N/0.02m = 50 N/m. (Using any pair: 2/0.04 = 50, 3/0.06 = 50, etc.)",
    pdfPage=131, bookPage=128))

data.append(q(chapter, "Section B", "B", "structured", 2,
    "A spring extends 3.5 cm when a load of 14 N is applied. Find the spring constant.",
    "Using Hooke's law F = kx: k = F/x = 14/0.035 = 400 N/m",
    pdfPage=131, bookPage=128))

data.append(q(chapter, "Section B", "B", "structured", 3,
    "State Hooke's law and define elastic limit.",
    "Hooke's law: Within elastic limit, extension is directly proportional to applied force (F = kx). Elastic limit: Maximum force up to which a body returns to original shape when force is removed.",
    pdfPage=131, bookPage=128))

data.append(q(chapter, "Section B", "B", "structured", 4,
    "Define pressure and state its SI unit.",
    "Pressure is force acting per unit area: P = F/A. SI unit is Pascal (Pa) = N/m².",
    pdfPage=131, bookPage=128))

data.append(q(chapter, "Section B", "B", "structured", 5,
    "A metal block weighing 20 N rests on a surface of area 5 cm². Calculate the pressure exerted.",
    "P = F/A = 20 N / (5 × 10⁻⁴ m²) = 20/0.0005 = 40,000 Pa = 40 kPa",
    pdfPage=131, bookPage=128))

data.append(q(chapter, "Section B", "B", "structured", 6,
    "Explain why a container with three spouts at different heights shows water coming out with different speeds.",
    "Pressure increases with depth (P = ρgh). Water from lower spout experiences greater pressure, so it flows out faster. Upper spout has less pressure, so water flows slower.",
    pdfPage=132, bookPage=129))

data.append(q(chapter, "Section B", "B", "structured", 7,
    "Describe an experiment to verify Hooke's law.",
    "Hang a spring vertically, attach a pointer. Add weights incrementally and measure extension. Plot load vs extension graph. If graph is straight line through origin, Hooke's law is verified. The slope gives spring constant.",
    pdfPage=132, bookPage=129))

data.append(q(chapter, "Section B", "B", "structured", 8,
    "Differentiate between stress and strain.",
    "Stress = Force/Area (measured in Pa), the internal restoring force per unit area. Strain = Change in dimension/Original dimension (dimensionless), the deformation produced. Stress causes strain.",
    pdfPage=132, bookPage=129))

data.append(q(chapter, "Section B", "B", "structured", 9,
    "What is Young's modulus? Give its formula and unit.",
    "Young's modulus (Y) = Stress/Strain = (F/A)/(ΔL/L) = FL/(AΔL). Unit: N/m² or Pascal. It measures stiffness of a material.",
    pdfPage=132, bookPage=129))

# ============ UNIT 6: Gravitation ============
chapter = "Gravitation"

# Section A: MCQs (17 questions)
data.append(q(chapter, "Section A", "A", "mcq", 1,
    "When a ball is thrown upward, the force of gravity acts:",
    "Downward throughout the motion",
    "Gravity always acts downward toward the center of Earth, regardless of direction of motion.",
    pdfPage=152, bookPage=149,
    options=["Downward throughout the motion", "Upward throughout the motion", "Downward only when falling", "Zero at highest point"],
    optionsRaw="a) Downward throughout the motion  b) Upward throughout the motion  c) Downward only when falling  d) Zero at highest point",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 2,
    "Newton's law of gravitation applies to:",
    "All bodies in the universe",
    "Newton's law of gravitation is universal - it applies to all masses in the universe.",
    pdfPage=152, bookPage=149,
    options=["Only Earth and Moon", "Only planets", "All bodies in the universe", "Only small objects"],
    optionsRaw="a) Only Earth and Moon  b) Only planets  c) All bodies in the universe  d) Only small objects",
    correctAnswer="c"))

data.append(q(chapter, "Section A", "A", "mcq", 3,
    "The value of gravitational constant G is:",
    "6.673 × 10⁻¹¹ Nm²/kg²",
    "G = 6.673 × 10⁻¹¹ Nm²/kg² is the universal gravitational constant.",
    pdfPage=152, bookPage=149,
    options=["6.673 × 10⁻¹¹ Nm²/kg²", "9.8 m/s²", "6.673 × 10¹¹ Nm²/kg²", "9.8 N/kg"],
    optionsRaw="a) 6.673 × 10⁻¹¹ Nm²/kg²  b) 9.8 m/s²  c) 6.673 × 10¹¹ Nm²/kg²  d) 9.8 N/kg",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 4,
    "The direction of gravitational field is:",
    "Toward the center of Earth",
    "Gravitational field lines point toward the center of mass creating the field.",
    pdfPage=152, bookPage=149,
    options=["Away from Earth", "Toward the center of Earth", "Parallel to surface", "In all directions equally"],
    optionsRaw="a) Away from Earth  b) Toward the center of Earth  c) Parallel to surface  d) In all directions equally",
    correctAnswer="b"))

data.append(q(chapter, "Section A", "A", "mcq", 5,
    "Who was the first scientist to formulate the law of gravitation?",
    "Newton",
    "Sir Isaac Newton formulated the universal law of gravitation in 1687.",
    pdfPage=152, bookPage=149,
    options=["Newton", "Einstein", "Galileo", "Kepler"],
    optionsRaw="a) Newton  b) Einstein  c) Galileo  d) Kepler",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 6,
    "The gravitational force between two bodies is proportional to:",
    "m₁m₂/r²",
    "F = Gm₁m₂/r², so force is proportional to product of masses and inversely proportional to square of distance.",
    pdfPage=152, bookPage=149,
    options=["m₁m₂/r²", "m₁+m₂/r", "m₁m₂/r", "m₁+m₂/r²"],
    optionsRaw="a) m₁m₂/r²  b) m₁+m₂/r  c) m₁m₂/r  d) m₁+m₂/r²",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 7,
    "Gravitational force is always:",
    "Attractive",
    "Gravitational force is always attractive - masses always attract each other.",
    pdfPage=152, bookPage=149,
    options=["Attractive", "Repulsive", "Both attractive and repulsive", "Neither"],
    optionsRaw="a) Attractive  b) Repulsive  c) Both attractive and repulsive  d) Neither",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 8,
    "The value of G is:",
    "Constant everywhere in the universe",
    "G is a universal constant with the same value everywhere.",
    pdfPage=152, bookPage=149,
    options=["Constant everywhere in the universe", "Different on different planets", "Zero in space", "Infinite at Earth's surface"],
    optionsRaw="a) Constant everywhere in the universe  b) Different on different planets  c) Zero in space  d) Infinite at Earth's surface",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 9,
    "Gravitational force between two bodies is independent of:",
    "Medium between them",
    "Gravitational force depends only on masses and distance, not on the medium between them.",
    pdfPage=152, bookPage=149,
    options=["Medium between them", "Masses of bodies", "Distance between them", "Universal constant G"],
    optionsRaw="a) Medium between them  b) Masses of bodies  c) Distance between them  d) Universal constant G",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 10,
    "If g = 10 ms⁻², the weight of 1 kg mass is:",
    "10 N",
    "W = mg = 1 × 10 = 10 N",
    pdfPage=152, bookPage=149,
    options=["10 N", "1 N", "100 N", "0.1 N"],
    optionsRaw="a) 10 N  b) 1 N  c) 100 N  d) 0.1 N",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 11,
    "Newton's law of gravitation is consistent with:",
    "Newton's third law of motion",
    "Gravitational forces form action-reaction pairs, consistent with Newton's third law.",
    pdfPage=152, bookPage=149,
    options=["Newton's third law of motion", "Newton's first law only", "Newton's second law only", "None of Newton's laws"],
    optionsRaw="a) Newton's third law of motion  b) Newton's first law only  c) Newton's second law only  d) None of Newton's laws",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 12,
    "A spring balance measures:",
    "Weight",
    "Spring balance measures the gravitational force (weight) acting on a body.",
    pdfPage=153, bookPage=150,
    options=["Mass", "Weight", "Volume", "Density"],
    optionsRaw="a) Mass  b) Weight  c) Volume  d) Density",
    correctAnswer="b"))

data.append(q(chapter, "Section A", "A", "mcq", 13,
    "Weight of a body on the Moon is:",
    "Decreased",
    "Moon's gravity is about 1/6 of Earth's, so weight decreases on the Moon.",
    pdfPage=153, bookPage=150,
    options=["Increased", "Decreased", "Same as on Earth", "Zero"],
    optionsRaw="a) Increased  b) Decreased  c) Same as on Earth  d) Zero",
    correctAnswer="b"))

data.append(q(chapter, "Section A", "A", "mcq", 14,
    "The mass of Earth is approximately:",
    "6.0 × 10²⁴ kg",
    "Earth's mass is approximately 6.0 × 10²⁴ kg.",
    pdfPage=153, bookPage=150,
    options=["6.0 × 10²⁴ kg", "6.0 × 10²² kg", "6.0 × 10² kg", "6.0 × 10²⁰ kg"],
    optionsRaw="a) 6.0 × 10²⁴ kg  b) 6.0 × 10²² kg  c) 6.0 × 10²⁶ kg  d) 6.0 × 10²⁰ kg",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 15,
    "The Moon is a:",
    "Natural satellite",
    "The Moon is Earth's natural satellite, orbiting Earth naturally.",
    pdfPage=153, bookPage=150,
    options=["Artificial satellite", "Natural satellite", "Planet", "Star"],
    optionsRaw="a) Artificial satellite  b) Natural satellite  c) Planet  d) Star",
    correctAnswer="b"))

data.append(q(chapter, "Section A", "A", "mcq", 16,
    "A communication satellite completes one revolution around Earth in:",
    "24 hours",
    "Geostationary communication satellites have an orbital period of 24 hours, matching Earth's rotation.",
    pdfPage=153, bookPage=150,
    options=["12 hours", "24 hours", "48 hours", "1 hour"],
    optionsRaw="a) 12 hours  b) 24 hours  c) 48 hours  d) 1 hour",
    correctAnswer="b"))

data.append(q(chapter, "Section A", "A", "mcq", 17,
    "The orbital velocity of a satellite is independent of:",
    "Mass of satellite",
    "Orbital velocity v = √(GM/r), which depends on Earth's mass and orbital radius, not satellite's mass.",
    pdfPage=153, bookPage=150,
    options=["Mass of satellite", "Mass of Earth", "Orbital radius", "Gravitational constant"],
    optionsRaw="a) Mass of satellite  b) Mass of Earth  c) Orbital radius  d) Gravitational constant",
    correctAnswer="a"))

# Section B: Self Assessment Questions (Q10-Q12)
data.append(q(chapter, "Section B", "B", "structured", 10,
    "Write down any four uses of artificial satellites.",
    "1) Communication (TV, radio, telephone signals). 2) Weather forecasting and monitoring. 3) Navigation (GPS). 4) Scientific research and Earth observation. 5) Military surveillance.",
    pdfPage=150, bookPage=150))

data.append(q(chapter, "Section B", "B", "structured", 11,
    "What is Geostationary orbit?",
    "A geostationary orbit is a circular orbit above Earth's equator at approximately 35,786 km altitude where a satellite orbits with the same period as Earth's rotation (24 hours). The satellite appears stationary relative to Earth's surface.",
    pdfPage=150, bookPage=150))

data.append(q(chapter, "Section B", "B", "structured", 12,
    "Why the two satellites of different masses have same speed in the same orbit?",
    "Orbital velocity v = √(GM/r) depends only on Earth's mass M and orbital radius r, not on satellite's mass m. Therefore, all satellites in the same orbit have the same speed regardless of their masses.",
    pdfPage=150, bookPage=150))

# ============ UNIT 7: Properties of Matter ============
chapter = "Properties of Matter"

# Section A: MCQs (10 questions)
data.append(q(chapter, "Section A", "A", "mcq", 1,
    "In solids, particles are:",
    "Closely packed in fixed positions",
    "Solid particles are closely packed with strong intermolecular forces, vibrating about fixed positions.",
    pdfPage=172, bookPage=169,
    options=["Closely packed in fixed positions", "Far apart and moving freely", "Moderately close and sliding", "In random motion"],
    optionsRaw="a) Closely packed in fixed positions  b) Far apart and moving freely  c) Moderately close and sliding  d) In random motion",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 2,
    "A burning candle involves which states of matter?",
    "Solid, liquid and gas",
    "Wax (solid) melts to liquid, then vaporizes to gas which burns.",
    pdfPage=172, bookPage=169,
    options=["Solid only", "Liquid only", "Solid and liquid", "Solid, liquid and gas"],
    optionsRaw="a) Solid only  b) Liquid only  c) Solid and liquid  d) Solid, liquid and gas",
    correctAnswer="d"))

data.append(q(chapter, "Section A", "A", "mcq", 3,
    "The process of changing gas to liquid is called:",
    "Condensation",
    "Condensation is the phase change from gas to liquid.",
    pdfPage=172, bookPage=169,
    options=["Evaporation", "Condensation", "Sublimation", "Freezing"],
    optionsRaw="a) Evaporation  b) Condensation  c) Sublimation  d) Freezing",
    correctAnswer="b"))

data.append(q(chapter, "Section A", "A", "mcq", 4,
    "Which property is characteristic of solids?",
    "Definite shape and volume",
    "Solids have both definite shape and definite volume due to strong intermolecular forces.",
    pdfPage=172, bookPage=169,
    options=["Definite shape and volume", "Definite volume but no shape", "No definite shape or volume", "Takes shape of container"],
    optionsRaw="a) Definite shape and volume  b) Definite volume but no shape  c) No definite shape or volume  d) Takes shape of container",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 5,
    "According to kinetic molecular theory, pressure of gas is caused by:",
    "Collisions of molecules with container walls",
    "Gas pressure results from continuous collisions of gas molecules with the walls of the container.",
    pdfPage=172, bookPage=169,
    options=["Collisions of molecules with container walls", "Weight of gas molecules", "Attraction between molecules", "Temperature of gas"],
    optionsRaw="a) Collisions of molecules with container walls  b) Weight of gas molecules  c) Attraction between molecules  d) Temperature of gas",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 6,
    "When a sealed cylinder of gas is heated:",
    "Pressure increases",
    "In a sealed container (constant volume), heating increases kinetic energy and collision frequency, increasing pressure.",
    pdfPage=172, bookPage=169,
    options=["Pressure increases", "Volume increases", "Pressure decreases", "No change"],
    optionsRaw="a) Pressure increases  b) Volume increases  c) Pressure decreases  d) No change",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 7,
    "When gas molecules are heated, they:",
    "Move faster",
    "Heating increases kinetic energy, causing molecules to move faster.",
    pdfPage=172, bookPage=169,
    options=["Move faster", "Move slower", "Stop moving", "Move in straight lines only"],
    optionsRaw="a) Move faster  b) Move slower  c) Stop moving  d) Move in straight lines only",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 8,
    "Evaporation is the process of:",
    "Liquid changing to gas at surface",
    "Evaporation occurs at the surface of a liquid at any temperature below boiling point.",
    pdfPage=172, bookPage=169,
    options=["Liquid changing to gas at surface", "Liquid changing to gas throughout", "Solid changing to gas", "Gas changing to liquid"],
    optionsRaw="a) Liquid changing to gas at surface  b) Liquid changing to gas throughout  c) Solid changing to gas  d) Gas changing to liquid",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 9,
    "When a gas changes to liquid, molecules:",
    "Come closer together",
    "During condensation, gas molecules lose energy and come closer together to form liquid.",
    pdfPage=172, bookPage=169,
    options=["Come closer together", "Move further apart", "Stop moving", "Move faster"],
    optionsRaw="a) Come closer together  b) Move further apart  c) Stop moving  d) Move faster",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 10,
    "A substance has melting point -17°C and boiling point 117°C. At room temperature (25°C), it is:",
    "Liquid",
    "At 25°C, the substance is above its melting point (-17°C) and below its boiling point (117°C), so it exists as liquid.",
    pdfPage=172, bookPage=169,
    options=["Solid", "Liquid", "Gas", "Plasma"],
    optionsRaw="a) Solid  b) Liquid  c) Gas  d) Plasma",
    correctAnswer="b"))

# Unit 7 has no Section B structured questions - only Summary and worked examples

# ============ UNIT 8: Energy Sources and Transfer of Energy ============
chapter = "Energy Sources and Transfer of Energy"

# Section A: MCQs (10 questions)
data.append(q(chapter, "Section A", "A", "mcq", 1,
    "Work done is equal to:",
    "F × d",
    "Work = Force × displacement in the direction of force: W = Fd.",
    pdfPage=191, bookPage=188,
    options=["F × d", "F/d", "F + d", "F - d"],
    optionsRaw="a) F × d  b) F/d  c) F + d  d) F - d",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 2,
    "Kinetic energy is given by:",
    "½mv²",
    "KE = ½mv², where m is mass and v is velocity.",
    pdfPage=191, bookPage=188,
    options=["½mv²", "mv²", "mgh", "Fd"],
    optionsRaw="a) ½mv²  b) mv²  c) mgh  d) Fd",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 3,
    "Power is defined as:",
    "W/t",
    "Power = Work done / time taken: P = W/t.",
    pdfPage=191, bookPage=188,
    options=["W/t", "W × t", "F × d", "mgh"],
    optionsRaw="a) W/t  b) W × t  c) F × d  d) mgh",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 4,
    "Potential energy is given by:",
    "mgh",
    "Gravitational PE = mgh, where m is mass, g is acceleration due to gravity, h is height.",
    pdfPage=191, bookPage=188,
    options=["mgh", "½mv²", "Fd", "ma"],
    optionsRaw="a) mgh  b) ½mv²  c) Fd  d) ma",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 5,
    "Nuclear energy is obtained from:",
    "Nucleus of atoms",
    "Nuclear energy is released from the nucleus of atoms through fission or fusion.",
    pdfPage=191, bookPage=188,
    options=["Nucleus of atoms", "Chemical bonds", "Solar radiation", "Wind"],
    optionsRaw="a) Nucleus of atoms  b) Chemical bonds  c) Solar radiation  d) Wind",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 6,
    "Which is a renewable energy source?",
    "Solar energy",
    "Solar energy is renewable as it comes from the Sun and won't run out.",
    pdfPage=191, bookPage=188,
    options=["Solar energy", "Coal", "Petroleum", "Natural gas"],
    optionsRaw="a) Solar energy  b) Coal  c) Petroleum  d) Natural gas",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 7,
    "Efficiency is the ratio of:",
    "Useful energy output to total energy input",
    "Efficiency = (Useful energy output / Total energy input) × 100%",
    pdfPage=191, bookPage=188,
    options=["Useful energy output to total energy input", "Total energy input to useful output", "Work done to time taken", "Force to distance"],
    optionsRaw="a) Useful energy output to total energy input  b) Total energy input to useful output  c) Work done to time taken  d) Force to distance",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 8,
    "Power is defined as:",
    "Rate of doing work",
    "Power is the rate at which work is done or energy is transferred.",
    pdfPage=191, bookPage=188,
    options=["Rate of doing work", "Total work done", "Force applied", "Energy stored"],
    optionsRaw="a) Rate of doing work  b) Total work done  c) Force applied  d) Energy stored",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 9,
    "Fossil fuels include:",
    "Coal, oil and natural gas",
    "Fossil fuels are coal, petroleum (oil), and natural gas formed from ancient organic matter.",
    pdfPage=191, bookPage=188,
    options=["Coal, oil and natural gas", "Solar and wind", "Nuclear and geothermal", "Hydroelectric and tidal"],
    optionsRaw="a) Coal, oil and natural gas  b) Solar and wind  c) Nuclear and geothermal  d) Hydroelectric and tidal",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 10,
    "Which is a non-renewable energy source?",
    "Coal",
    "Coal is a fossil fuel that takes millions of years to form and is non-renewable.",
    pdfPage=191, bookPage=188,
    options=["Coal", "Solar", "Wind", "Hydroelectric"],
    optionsRaw="a) Coal  b) Solar  c) Wind  d) Hydroelectric",
    correctAnswer="a"))

# Section B: Structured Questions
data.append(q(chapter, "Section B", "B", "structured", 1,
    "Define work and state its SI unit.",
    "Work is done when a force moves a body through a distance in the direction of force. W = Fd. SI unit is Joule (J) = N·m.",
    pdfPage=192, bookPage=189))

data.append(q(chapter, "Section B", "B", "structured", 2,
    "A force of 50 N moves a body through 10 m. Calculate the work done.",
    "W = Fd = 50 × 10 = 500 J",
    pdfPage=192, bookPage=189))

data.append(q(chapter, "Section B", "B", "structured", 3,
    "Differentiate between work and energy.",
    "Work is the transfer of energy by a force acting through a distance. Energy is the capacity to do work. Both measured in Joules. Work is a process; energy is a property of a system.",
    pdfPage=192, bookPage=189))

data.append(q(chapter, "Section B", "B", "structured", 4,
    "When is work done said to be zero? Give two examples.",
    "Work is zero when: (1) Force is perpendicular to displacement (e.g., carrying a bag horizontally). (2) No displacement occurs (e.g., pushing a wall that doesn't move).",
    pdfPage=192, bookPage=189))

data.append(q(chapter, "Section B", "B", "structured", 5,
    "List different forms of energy.",
    "1) Kinetic energy (motion). 2) Potential energy (position). 3) Chemical energy (bonds). 4) Heat/Thermal energy. 5) Light energy. 6) Sound energy. 7) Electrical energy. 8) Nuclear energy.",
    pdfPage=192, bookPage=189))

data.append(q(chapter, "Section B", "B", "structured", 6,
    "Give two examples of potential energy and two examples of kinetic energy.",
    "Potential energy: (1) Water stored in a dam. (2) A stretched bow. Kinetic energy: (1) A moving car. (2) A flying bird.",
    pdfPage=192, bookPage=189))

data.append(q(chapter, "Section B", "B", "structured", 7,
    "State the law of conservation of energy.",
    "Energy cannot be created or destroyed, only transformed from one form to another. Total energy of an isolated system remains constant.",
    pdfPage=192, bookPage=189))

data.append(q(chapter, "Section B", "B", "structured", 8,
    "Describe the energy conversion in a hydroelectric power plant.",
    "Potential energy of stored water → Kinetic energy of falling water → Mechanical energy of turbine rotation → Electrical energy from generator.",
    pdfPage=192, bookPage=189))

data.append(q(chapter, "Section B", "B", "structured", 9,
    "What are renewable energy sources? Give four examples.",
    "Renewable energy sources are naturally replenished and won't run out. Examples: (1) Solar energy. (2) Wind energy. (3) Hydroelectric energy. (4) Geothermal energy. (5) Biomass energy.",
    pdfPage=193, bookPage=190))

data.append(q(chapter, "Section B", "B", "structured", 10,
    "What are non-renewable energy sources? Give three examples.",
    "Non-renewable sources are finite and will eventually run out. Examples: (1) Coal. (2) Petroleum/Oil. (3) Natural gas. (4) Nuclear fuel (uranium).",
    pdfPage=193, bookPage=190))

data.append(q(chapter, "Section B", "B", "structured", 11,
    "Why should we use renewable energy sources?",
    "1) They won't run out. 2) They produce less pollution. 3) They help combat climate change. 4) They are sustainable for future generations. 5) Reduces dependence on fossil fuels.",
    pdfPage=193, bookPage=190))

data.append(q(chapter, "Section B", "B", "structured", 12,
    "What are the disadvantages of fossil fuels?",
    "1) Non-renewable (will run out). 2) Cause air pollution. 3) Produce greenhouse gases (CO₂). 4) Contribute to global warming. 5) Cause acid rain. 6) Extraction damages environment.",
    pdfPage=193, bookPage=190))

data.append(q(chapter, "Section B", "B", "structured", 13,
    "How is solar energy converted to electrical energy?",
    "Solar panels (photovoltaic cells) convert sunlight directly to electricity using semiconductor materials. Solar thermal systems use sunlight to heat water, produce steam, and drive turbines.",
    pdfPage=193, bookPage=190))

data.append(q(chapter, "Section B", "B", "structured", 14,
    "Describe how wind energy is harnessed.",
    "Wind turbines have blades that rotate when wind blows. The rotation drives a generator that produces electricity. Wind farms have multiple turbines for large-scale power generation.",
    pdfPage=193, bookPage=190))

data.append(q(chapter, "Section B", "B", "structured", 15,
    "What is geothermal energy? How is it used?",
    "Geothermal energy is heat from Earth's interior. It's used by drilling wells to access hot water/steam, which drives turbines to generate electricity or directly heats buildings.",
    pdfPage=193, bookPage=190))

data.append(q(chapter, "Section B", "B", "structured", 16,
    "Compare renewable and non-renewable energy sources.",
    "Renewable: Naturally replenished, environmentally friendly, sustainable, but may have high initial costs. Non-renewable: Finite, cause pollution, cheaper currently, but will run out and damage environment.",
    pdfPage=193, bookPage=190))

data.append(q(chapter, "Section B", "B", "structured", 17,
    "Define efficiency of a system.",
    "Efficiency = (Useful energy output / Total energy input) × 100%. It measures how well a system converts input energy to useful output energy.",
    pdfPage=194, bookPage=191))

data.append(q(chapter, "Section B", "B", "structured", 18,
    "A machine takes 1000 J of energy and produces 800 J of useful work. Find its efficiency.",
    "Efficiency = (800/1000) × 100% = 80%",
    pdfPage=194, bookPage=191))

data.append(q(chapter, "Section B", "B", "structured", 19,
    "Why can no machine be 100% efficient?",
    "Some energy is always lost as heat due to friction, air resistance, sound, etc. No machine can convert all input energy to useful output.",
    pdfPage=194, bookPage=191))

data.append(q(chapter, "Section B", "B", "structured", 20,
    "How can we improve the efficiency of machines?",
    "1) Reduce friction using lubricants. 2) Use better materials. 3) Regular maintenance. 4) Improve design. 5) Reduce energy losses as heat and sound.",
    pdfPage=194, bookPage=191))

data.append(q(chapter, "Section B", "B", "structured", 21,
    "Define power and state its SI unit.",
    "Power is the rate of doing work or rate of energy transfer. P = W/t. SI unit is Watt (W) = J/s.",
    pdfPage=194, bookPage=191))

data.append(q(chapter, "Section B", "B", "structured", 22,
    "A motor does 5000 J of work in 10 seconds. Find its power.",
    "P = W/t = 5000/10 = 500 W",
    pdfPage=194, bookPage=191))

data.append(q(chapter, "Section B", "B", "structured", 23,
    "Differentiate between kilowatt and kilowatt-hour.",
    "Kilowatt (kW) is a unit of power (rate of energy transfer). Kilowatt-hour (kWh) is a unit of energy (power × time). 1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J.",
    pdfPage=194, bookPage=191))

data.append(q(chapter, "Section B", "B", "structured", 24,
    "An electric heater of 2 kW runs for 3 hours. Calculate the energy consumed in kWh.",
    "Energy = Power × time = 2 kW × 3 h = 6 kWh",
    pdfPage=194, bookPage=191))

# ============ UNIT 9: Thermal Properties of Matter ============
chapter = "Thermal Properties of Matter"

# Section A: MCQs (11 questions)
data.append(q(chapter, "Section A", "A", "mcq", 1,
    "Heat is a form of:",
    "Energy",
    "Heat is thermal energy transferred between bodies due to temperature difference.",
    pdfPage=216, bookPage=213,
    options=["Energy", "Force", "Power", "Pressure"],
    optionsRaw="a) Energy  b) Force  c) Power  d) Pressure",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 2,
    "Heat capacity equals:",
    "mass × specific heat",
    "Heat capacity C = mc, where m is mass and c is specific heat capacity.",
    pdfPage=216, bookPage=213,
    options=["mass × specific heat", "mass/specific heat", "specific heat/mass", "mass + specific heat"],
    optionsRaw="a) mass × specific heat  b) mass/specific heat  c) specific heat/mass  d) mass + specific heat",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 3,
    "Latent heat of vaporization is the heat required to:",
    "Change liquid to gas at boiling point",
    "Latent heat of vaporization is the heat needed to convert unit mass of liquid to gas at constant temperature (boiling point).",
    pdfPage=216, bookPage=213,
    options=["Change liquid to gas at boiling point", "Raise temperature by 1°C", "Change solid to liquid", "Change gas to liquid"],
    optionsRaw="a) Change liquid to gas at boiling point  b) Raise temperature by 1°C  c) Change solid to liquid  d) Change gas to liquid",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 4,
    "Specific heat capacity is defined as:",
    "Heat required to raise temperature of 1 kg by 1 K",
    "Specific heat capacity c = Q/(mΔT), the heat needed to raise 1 kg of substance by 1 Kelvin.",
    pdfPage=216, bookPage=213,
    options=["Heat required to raise temperature of 1 kg by 1 K", "Heat required to raise temperature of 1 g by 1°C", "Total heat content", "Heat lost by a body"],
    optionsRaw="a) Heat required to raise temperature of 1 kg by 1 K  b) Heat required to raise temperature of 1 g by 1°C  c) Total heat content  d) Heat lost by a body",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 5,
    "Boiling point of water is:",
    "100°C",
    "Water boils at 100°C (373 K) at standard atmospheric pressure.",
    pdfPage=216, bookPage=213,
    options=["100°C", "0°C", "50°C", "200°C"],
    optionsRaw="a) 100°C  b) 0°C  c) 50°C  d) 200°C",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 6,
    "Ice melts at:",
    "0°C",
    "Ice melts at 0°C (273 K) at standard atmospheric pressure.",
    pdfPage=216, bookPage=213,
    options=["0°C", "100°C", "-10°C", "10°C"],
    optionsRaw="a) 0°C  b) 100°C  c) -10°C  d) 10°C",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 7,
    "Latent heat of fusion is the heat required to:",
    "Change solid to liquid at melting point",
    "Latent heat of fusion is the heat needed to convert unit mass of solid to liquid at constant temperature (melting point).",
    pdfPage=216, bookPage=213,
    options=["Change solid to liquid at melting point", "Change liquid to gas", "Raise temperature", "Cool a substance"],
    optionsRaw="a) Change solid to liquid at melting point  b) Change liquid to gas  c) Raise temperature  d) Cool a substance",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 8,
    "Latent heat of vaporization of water is:",
    "2.26 × 10⁶ J/kg",
    "Latent heat of vaporization of water is approximately 2.26 × 10⁶ J/kg.",
    pdfPage=216, bookPage=213,
    options=["2.26 × 10⁶ J/kg", "3.36 × 10⁵ J/kg", "4.2 × 10³ J/kg·K", "1.0 × 10⁵ J/kg"],
    optionsRaw="a) 2.26 × 10⁶ J/kg  b) 3.36 × 10⁵ J/kg  c) 4.2 × 10³ J/kg·K  d) 1.0 × 10⁵ J/kg",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 9,
    "Vaporization can occur at:",
    "All temperatures",
    "Evaporation (surface vaporization) occurs at all temperatures below boiling point.",
    pdfPage=216, bookPage=213,
    options=["All temperatures", "Only at boiling point", "Only at 100°C", "Only at 0°C"],
    optionsRaw="a) All temperatures  b) Only at boiling point  c) Only at 100°C  d) Only at 0°C",
    correctAnswer="a"))

data.append(q(chapter, "Section A", "A", "mcq", 10,
    "Rate of evaporation depends on:",
    "All of these",
    "Evaporation rate depends on temperature, surface area, wind speed, and humidity.",
    pdfPage=216, bookPage=213,
    options=["Temperature", "Surface area", "Wind speed", "All of these"],
    optionsRaw="a) Temperature  b) Surface area  c) Wind speed  d) All of these",
    correctAnswer="d"))

data.append(q(chapter, "Section A", "A", "mcq", 11,
    "Linear thermal expansion depends on:",
    "Original length, temperature change, and material",
    "ΔL = αL₀ΔT, where α is coefficient of linear expansion (material property), L₀ is original length, ΔT is temperature change.",
    pdfPage=216, bookPage=213,
    options=["Original length only", "Temperature change only", "Material only", "Original length, temperature change, and material"],
    optionsRaw="a) Original length only  b) Temperature change only  c) Material only  d) Original length, temperature change, and material",
    correctAnswer="d"))

# Section B: Structured Questions
data.append(q(chapter, "Section B", "B", "structured", 1,
    "Differentiate between heat and temperature.",
    "Heat is thermal energy in transit between bodies due to temperature difference (measured in Joules). Temperature is the degree of hotness or coldness of a body (measured in Kelvin, Celsius, or Fahrenheit). Heat flows from higher to lower temperature.",
    pdfPage=217, bookPage=214))

data.append(q(chapter, "Section B", "B", "structured", 2,
    "Define thermal equilibrium.",
    "Two bodies are in thermal equilibrium when they are at the same temperature and there is no net flow of heat between them.",
    pdfPage=217, bookPage=214))

data.append(q(chapter, "Section B", "B", "structured", 3,
    "Define specific heat capacity and give its SI unit.",
    "Specific heat capacity is the amount of heat required to raise the temperature of 1 kg of a substance by 1 K (or 1°C). SI unit: J/(kg·K) or J/(kg·°C).",
    pdfPage=217, bookPage=214))

data.append(q(chapter, "Section B", "B", "structured", 4,
    "Calculate the heat required to raise the temperature of 2 kg of water from 20°C to 80°C. (Specific heat of water = 4200 J/kg·K)",
    "Q = mcΔT = 2 × 4200 × (80-20) = 2 × 4200 × 60 = 504,000 J = 504 kJ",
    pdfPage=217, bookPage=214))

data.append(q(chapter, "Section B", "B", "structured", 5,
    "Define latent heat of fusion.",
    "Latent heat of fusion is the amount of heat required to change 1 kg of a substance from solid to liquid state at its melting point without change in temperature. For ice: 3.36 × 10⁵ J/kg.",
    pdfPage=217, bookPage=214))

data.append(q(chapter, "Section B", "B", "structured", 6,
    "Define latent heat of vaporization.",
    "Latent heat of vaporization is the amount of heat required to change 1 kg of a substance from liquid to gas state at its boiling point without change in temperature. For water: 2.26 × 10⁶ J/kg.",
    pdfPage=217, bookPage=214))

data.append(q(chapter, "Section B", "B", "structured", 7,
    "Why does temperature remain constant during phase change?",
    "During phase change, the heat energy supplied is used to break intermolecular bonds rather than increase kinetic energy. Since temperature depends on average kinetic energy, it remains constant until the phase change is complete.",
    pdfPage=217, bookPage=214))

data.append(q(chapter, "Section B", "B", "structured", 8,
    "Define evaporation and list factors affecting its rate.",
    "Evaporation is the process of liquid changing to vapor at the surface at any temperature below boiling point. Factors: (1) Temperature - higher temp increases rate. (2) Surface area - larger area increases rate. (3) Wind speed - faster wind increases rate. (4) Humidity - lower humidity increases rate.",
    pdfPage=218, bookPage=215))

data.append(q(chapter, "Section B", "B", "structured", 9,
    "Why does evaporation cause cooling?",
    "During evaporation, high-energy molecules escape from the liquid surface, leaving behind lower-energy molecules. This reduces the average kinetic energy of remaining molecules, lowering the temperature and causing cooling.",
    pdfPage=218, bookPage=215))

data.append(q(chapter, "Section B", "B", "structured", 10,
    "Differentiate between evaporation and boiling.",
    "Evaporation: occurs at surface, at any temperature, slow process, causes cooling. Boiling: occurs throughout liquid, at fixed boiling point, rapid process, bubbles form throughout.",
    pdfPage=218, bookPage=215))

data.append(q(chapter, "Section B", "B", "structured", 11,
    "Define linear thermal expansion and give its formula.",
    "Linear thermal expansion is the increase in length of a solid when heated. Formula: ΔL = αL₀ΔT, where α is coefficient of linear expansion, L₀ is original length, ΔT is temperature change.",
    pdfPage=218, bookPage=215))

data.append(q(chapter, "Section B", "B", "structured", 12,
    "Give two practical applications of thermal expansion.",
    "1) Gaps left in railway tracks to allow for expansion in summer. 2) Bimetallic strips used in thermostats - two metals with different expansion rates bend when heated, breaking or making electrical contact.",
    pdfPage=218, bookPage=215))

data.append(q(chapter, "Section B", "B", "structured", 13,
    "Why are gaps left in bridges and railway tracks?",
    "Gaps are left to allow for thermal expansion. In summer, materials expand due to heat. Without gaps, the expansion would cause buckling, warping, or structural damage.",
    pdfPage=218, bookPage=215))

# Write output
output_path = "D:/SubjectZone/public/data/class_ix_physics.json"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Generated {len(data)} questions for Physics IX")

# Count by unit
from collections import Counter
unit_counts = Counter()
for item in data:
    unit_counts[item['chapter']] += 1

print("\nQuestions per unit:")
for unit, count in sorted(unit_counts.items()):
    print(f"  {unit}: {count}")

# Count by type
type_counts = Counter(item['type'] for item in data)
print(f"\nTotal MCQs: {type_counts.get('mcq', 0)}")
print(f"Total Structured: {type_counts.get('structured', 0)}")
print(f"Total: {len(data)}")
