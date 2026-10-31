"""Computer Science XI — Unit 2: Computational Thinking & Algorithm (book 71-90)."""
from .common import bq, mcq

ITEMS = []

# A. MCQs — PDF 94 (book 89)
ITEMS += [
    mcq(2, 'A', 'i', 'Which strategy involves ignoring the brand of a kettle when learning how to make tea?',
        [('a', 'Decomposition'), ('b', 'Pattern Recognition'),
         ('c', 'Abstraction'), ('d', 'Sorting')], 'c',
        'Abstraction removes details that do not matter for the task. The brand of the kettle is '
        'irrelevant to the procedure of making tea, so it is abstracted away.', 94),
    mcq(2, 'A', 'ii', 'Bubble Sort is also commonly known as:',
        [('a', 'Linear Sort'), ('b', 'Ripple Sort'),
         ('c', 'Selection Sort'), ('d', 'Binary Sort')], 'b',
        'Bubble Sort repeatedly swaps adjacent out-of-order elements; the exchange ripples through '
        'the list, hence the alternative name ripple sort.', 94),
    mcq(2, 'A', 'iii', 'Which searching algorithm requires the data to be sorted before it can be used?',
        [('a', 'Linear Search'), ('b', 'Sequential Search'),
         ('c', 'Binary Search'), ('d', 'Bubble Search')], 'c',
        'Binary Search halves the search range each step by comparing the middle element. That '
        'decision is only valid when the data is in sorted order.', 94),
    mcq(2, 'A', 'iv', 'What is the main disadvantage of Selection Sort?',
        [('a', 'It uses extra RAM'), ('b', 'It is difficult to code'),
         ('c', 'It must finish every loop even if the list is sorted'),
         ('d', 'It only works on alphabetical data')], 'c',
        'Selection Sort always scans the remaining list to find the minimum, even when the list is '
        'already sorted. Its running time is therefore O(n\u00b2) in the best, average and worst cases. '
        'It sorts numeric data too, so (d) is false.', 94),
    mcq(2, 'A', 'v', 'An algorithm is considered "correct" if:',
        [('a', 'It runs very fast'), ('b', 'Its output matches expected outcomes for given inputs'),
         ('c', 'It uses minimal memory'), ('d', 'It is written in a specific programming language')], 'b',
        'Correctness means the algorithm produces the expected output for every valid input. '
        'Speed and memory describe efficiency, not correctness; an algorithm is language-independent.', 94),
    mcq(2, 'A', 'vi', 'What does the abbreviation CT stand for?',
        [('a', 'Computer Technology'), ('b', 'Computational Thinking'),
         ('c', 'Central Terminal'), ('d', 'Coding Technique')], 'b',
        'In this unit CT means Computational Thinking: decomposition, pattern recognition, '
        'abstraction and algorithm design.', 94),
    mcq(2, 'A', 'vii', 'Which operation is represented by MOD?',
        [('a', 'Multiplication'), ('b', 'Division'),
         ('c', 'Subtraction'), ('d', 'Finding the remainder after division')], 'd',
        'MOD returns the remainder of an integer division, e.g. 17 MOD 5 = 2 because 17 = 3\u00d75 + 2.', 94),
    mcq(2, 'A', 'viii', 'In algorithms, what is the purpose of a PTR?',
        [('a', 'To store text data'), ('b', 'To perform calculations'),
         ('c', 'To track positions in an array'), ('d', 'To display output')], 'c',
        'PTR (pointer) stores the position/index currently being examined. In linear search it '
        'walks through the array; in binary search BEG, MID and END are such position markers.', 95),
    mcq(2, 'A', 'ix', 'What does INT represent in an algorithm?',
        [('a', 'Internet'), ('b', 'Integer'),
         ('c', 'Interval'), ('d', 'Input')], 'b',
        'INT is the standard abbreviation for Integer, a whole number such as 5 or \u22123, used to '
        'declare a variable that stores no fractional part.', 95),
    mcq(2, 'A', 'x', 'In the Binary Search algorithm, the abbreviations BEG, END, and MID represent:',
        [('a', 'Input, Process, and Output'), ('b', 'Beginning, End, and Middle positions'),
         ('c', 'First, Last, and Next values'), ('d', 'Start, Stop, and Result')], 'b',
        'Binary Search maintains the boundaries of the current search range: BEG (first index), '
        'END (last index) and MID = (BEG + END) / 2, the element tested next.', 95),
]

# B. Fill in the Blanks — PDF 95 (book 90)
ITEMS += [
    bq(2, 'B', 'i', '____________ is a step-by-step logical procedure to solve a problem.',
       'Algorithm',
       'An algorithm is a finite, ordered set of unambiguous steps that transforms inputs into '
       'the required output. It is independent of any programming language.', 95),
    bq(2, 'B', 'ii', 'Sorting may be Ascending or ____________.',
       'Descending',
       'Ascending order goes from the smallest to the largest (1, 2, 3); descending order goes '
       'from the largest to the smallest (3, 2, 1).', 95),
    bq(2, 'B', 'iii', 'Algorithm is ____________ and language-independent.',
       'conceptual (a logical procedure)',
       'An algorithm is a conceptual/logical solution: it describes WHAT to do, not which '
       'language or syntax to use. The same algorithm can be implemented in Python, C++ or Java.', 95),
    bq(2, 'B', 'iv', '____________ algorithm is designed to locate a specific element within list of data.',
       'Searching',
       'A searching algorithm examines a collection to find a target value (or report that it is '
       'absent). Linear search and binary search are the two algorithms covered in this unit.', 95),
    bq(2, 'B', 'v', 'We measure any algorithm efficiency through ____________ and ____________ as resources.',
       'time and space (memory)',
       'Efficiency has two dimensions: time complexity (how the number of operations grows with '
       'input size) and space complexity (how much extra memory the algorithm needs).', 95),
]

# C. Short answers — PDF 95 (book 90)
ITEMS += [
    bq(2, 'C', 'i', 'Define pattern recognition.',
       'Pattern recognition is the computational-thinking skill of identifying similarities, '
       'regularities or repeated structures in problems and data, so that a solution found for '
       'one case can be reused for the others.\n'
       'Example: noticing that every student record has the same fields (name, roll number, marks) '
       'lets one table structure serve for all records; recognizing that a series of numbers grows '
       'by a constant difference suggests a loop with a step.',
       'Spotting a pattern turns a new problem into a known problem, which is why it is one of the '
       'four pillars of computational thinking.', 95),
    bq(2, 'C', 'ii', 'Explain the concept of decomposition.',
       'Decomposition is breaking a complex problem or system into smaller, independent parts that '
       'are easier to understand, solve and test. Each part can then be handled separately and the '
       'parts combined into the full solution.\n'
       'Example: building a school management system is decomposed into student registration, '
       'attendance, fee collection and result preparation. Each module can be designed, coded and '
       'tested on its own.',
       'Smaller parts reduce complexity, allow parallel work and make errors easier to locate.', 95),
    bq(2, 'C', 'iii', 'What is meant by correctness in problem-solving?',
       'Correctness is the property that an algorithm produces the expected output for every valid '
       'input, including boundary cases. It is established by reasoning about the steps and by '
       'testing with valid, invalid and edge-case inputs.\n'
       'An algorithm that is fast but returns a wrong answer is not correct, and therefore useless.',
       'Correctness is about WHAT the algorithm returns, not how quickly it returns it; speed is '
       'covered by efficiency.', 95),
    bq(2, 'C', 'iv', 'Why is efficiency important in problem-solving?',
       'Efficiency measures the resources an algorithm consumes: time (number of operations) and '
       'space (memory). An efficient algorithm finishes quickly and uses little memory, which '
       'matters when data is large or the device is limited.\n'
       'Example: searching a sorted list of one million items takes about one million comparisons '
       'with linear search but only about 20 with binary search. On a phone or embedded device, an '
       'inefficient algorithm may drain the battery or run out of memory.',
       'Efficiency is usually expressed with Big-O notation, e.g. O(n) for linear search and '
       'O(log n) for binary search.', 95),
    bq(2, 'C', 'v', 'What do you understand by clarity in problem-solving?',
       'Clarity means an algorithm is easy to read, understand, explain and modify. It uses '
       'meaningful names, simple steps, consistent indentation and comments where needed, and it '
       'avoids unnecessary complexity.\n'
       'A clear algorithm can be checked by another person, converted to code with fewer mistakes, '
       'and maintained later. Obscure tricks may save a line but cost far more in debugging.',
       'Clarity is a quality of the solution, not of the computer: the machine will run a confusing '
       'algorithm, but humans must understand it to trust and maintain it.', 95),
]

# D. Detailed answers — PDF 95 (book 90)
ITEMS += [
    bq(2, 'D', 'i', 'What is the difference between an algorithm and pseudocode?',
       'An algorithm is the abstract, language-independent solution: a finite ordered list of '
       'unambiguous steps that solves a problem. It states the logic, e.g. "repeat for each '
       'element: if it equals the target, report its position".\n'
       'Pseudocode is a written representation of that algorithm using structured English and '
       'programming-like keywords (IF, WHILE, FOR, INPUT, OUTPUT). It is closer to code and easier '
       'to translate, but it still ignores the syntax of any particular language.\n'
       'Example algorithm for the maximum of a list: (1) set MAX to the first value; (2) compare '
       'each remaining value; (3) if a value is larger, replace MAX; (4) report MAX.\n'
       'Same idea in pseudocode:\n'
       'MAX \u2190 A[1]\n'
       'FOR i \u2190 2 TO n\n'
       '    IF A[i] > MAX THEN MAX \u2190 A[i]\n'
       'END FOR\n'
       'PRINT MAX',
       'The algorithm is the idea; pseudocode is one way of writing the idea down. Pseudocode is '
       'not executable, while a program adds the exact syntax of a language.', 95),
    bq(2, 'D', 'ii', 'What is abstraction in an algorithm, and why is it used?',
       'Abstraction is the process of removing irrelevant details and keeping only the features '
       'needed to solve the problem. It creates a simplified model of the real situation.\n'
       'Example: a route-finding algorithm models a city as a graph of intersections and roads. '
       'It ignores building colours, shop names and traffic-light timing, because those details do '
       'not affect the shortest path. Similarly, a student-record algorithm keeps name, roll number '
       'and marks but ignores height or favourite colour.\n'
       'Why it is used: (1) it reduces complexity so the logic is easier to design and understand; '
       '(2) it makes the solution general, so the same algorithm works for many cases; (3) it lets '
       'us work at a higher level and hide implementation details behind functions.',
       'Abstraction is not about losing information carelessly; it is about deliberately choosing '
       'the details that matter for the task.', 95),
    bq(2, 'D', 'iii', 'Write the steps of the Selection Sort algorithm.',
       'Selection Sort repeatedly selects the smallest element of the unsorted part and places it '
       'at the beginning of that part.\n'
       'Steps (ascending order, list A of n elements):\n'
       '1. Set i = 1 (first position of the unsorted part).\n'
       '2. Set MIN = i.\n'
       '3. For j = i + 1 to n: if A[j] < A[MIN], set MIN = j.\n'
       '4. If MIN \u2260 i, swap A[i] with A[MIN].\n'
       '5. Increase i by 1.\n'
       '6. Repeat steps 2-5 until i = n \u2212 1.\n'
       '7. The list is now sorted; stop.\n'
       'Example: [5, 3, 8, 1] \u2192 swap 5 and 1 \u2192 [1, 3, 8, 5] \u2192 minimum of the rest is 3, already in '
       'place \u2192 [1, 3, 8, 5] \u2192 swap 8 and 5 \u2192 [1, 3, 5, 8].',
       'The algorithm performs n \u2212 1 passes. Each pass does a linear scan, so the time complexity '
       'is O(n\u00b2) in all cases, while the extra space is O(1) because sorting is done in place.', 95),
    bq(2, 'D', 'iv', 'Write the steps of the Binary Search algorithm.',
       'Binary Search works only on a sorted list. It repeatedly halves the search range.\n'
       'Steps (list A sorted ascending, target T):\n'
       '1. Set BEG = 1 and END = n.\n'
       '2. If BEG > END, the target is not present; stop.\n'
       '3. Set MID = integer part of (BEG + END) / 2.\n'
       '4. If A[MID] = T, report MID and stop.\n'
       '5. If A[MID] < T, set BEG = MID + 1 (search the right half).\n'
       '6. If A[MID] > T, set END = MID \u2212 1 (search the left half).\n'
       '7. Repeat from step 2.\n'
       'Example: A = [2, 4, 7, 11, 15, 20, 25], T = 15. MID = 4 \u2192 A[4] = 11 < 15, so BEG = 5. '
       'MID = 6 \u2192 A[6] = 20 > 15, so END = 5. MID = 5 \u2192 A[5] = 15, found at position 5.',
       'Each comparison discards half of the remaining elements, so the number of comparisons is '
       'at most log\u2082 n + 1: about 20 comparisons for a million items.', 95),
    bq(2, 'D', 'v', 'Which searching algorithm is best for large datasets? Explain your answer.',
       'Binary Search is best for large datasets, provided the data is sorted (or can be kept '
       'sorted). Its time complexity is O(log n), because every comparison halves the search range. '
       'For one million items it needs about 20 comparisons; for one billion, about 30.\n'
       'Linear (sequential) search is O(n): it may need to examine every element, which is far too '
       'slow for large collections. It is still useful for small or unsorted data, or when the list '
       'changes so often that keeping it sorted is not worthwhile.\n'
       'The cost of sorting the data once (O(n log n)) is repaid when many searches are performed. '
       'For very large datasets stored on disk or in a database, the same principle underlies '
       'indexes and B-trees.',
       'The answer depends on the requirement: binary search for many searches on sorted data; '
       'linear search for a single search on small/unsorted data.', 95),
]

# E. Activities — PDF 95 (book 90)
ITEMS += [
    bq(2, 'E', 'i', 'Arrange the assembly queue according to students\' heights.',
       'Method: line up the students and apply a simple sorting procedure, e.g. Selection Sort.\n'
       '1. Find the shortest student in the line and bring that student to the front.\n'
       '2. From the remaining students, find the next shortest and place that student second.\n'
       '3. Repeat until everyone is placed.\n'
       'Alternative: compare adjacent students and swap them if the taller one is in front (Bubble '
       'Sort), repeating passes until no swaps are needed.\n'
       'Result: the queue is arranged in ascending order of height.',
       'Sorting a physical line is exactly the same algorithm as sorting an array; each student is '
       'an element and height is the comparison key.', 95),
    bq(2, 'E', 'ii', 'Arrange the names in the attendance register in descending alphabetical order.',
       'Method: Selection Sort on the name field.\n'
       '1. Compare all names and find the alphabetically last name; place it first.\n'
       '2. Find the last name among the remaining entries and place it second.\n'
       '3. Continue until all names are placed.\n'
       'For a register of 40 names this needs at most 40 \u00d7 39 / 2 = 780 comparisons. The result is '
       'descending alphabetical order, e.g. Zubair, Sana, Raheel, ... , Ayesha.',
       'Descending order uses the same selection procedure with the comparison reversed: choose '
       'the largest (last in the alphabet) instead of the smallest.', 95),
    bq(2, 'E', 'iii', 'Find the name of your class monitor in the attendance register using the binary '
       'search technique.',
       'Step 1: the register must be in alphabetical order, so sort it first if necessary.\n'
       'Step 2: set BEG to the first name and END to the last name.\n'
       'Step 3: open the register at the middle position MID = (BEG + END) / 2 and read the name.\n'
       'Step 4: if it is the monitor\'s name, stop. If the monitor\'s name comes later in the '
       'alphabet, set BEG = MID + 1; if it comes earlier, set END = MID \u2212 1.\n'
       'Step 5: repeat from step 3 until the name is found or BEG > END.\n'
       'Example: with 40 names, at most 6 comparisons are needed instead of up to 40.',
       'Binary search works because the register is sorted: comparing with the middle name tells '
       'you which half cannot contain the target.', 95),
]
