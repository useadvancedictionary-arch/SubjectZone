"""Computer Science XI — Unit 3: Programming Fundamentals (book 91-138)."""
from .common import bq, mcq

ITEMS = []

# A. MCQs — PDF 141 (book 136)
ITEMS += [
    mcq(3, 'A', 'i', 'Which is the correct statement to insert Comments in Python code?',
        [('a', '// This is comment'), ('b', '/* This is comment*/'),
         ('c', '# This is comment'), ('d', '-- This is comment')], 'c',
        'Python comments start with # and run to the end of the line. //, /* */ and -- are comment '
        'or decrement syntax from other languages and are invalid for comments in Python.', 141),
    mcq(3, 'A', 'ii', 'Which one is not a legal variable name?',
        [('a', '_myvar'), ('b', 'my_var'),
         ('c', 'Myvar'), ('d', 'my-var')], 'd',
        'A Python identifier may contain letters, digits and underscores, and may not begin with a '
        'digit. The hyphen is not allowed: Python reads my-var as the subtraction my - var.', 141),
    mcq(3, 'A', 'iii', 'Which one is the correct way to write if statement in Python?',
        [('a', 'if (condition):'), ('b', 'if(condition );'),
         ('c', 'if (1):'), ('d', 'none of these')], 'a',
        'The general form of a Python if statement is "if condition:" with a colon at the end; '
        'parentheses are optional, so (a) is the expected syntax. (b) is invalid because of the '
        'semicolon inside the condition. Note: (c) "if (1):" is also syntactically valid (1 is '
        'truthy), but it is a constant test rather than the general form asked for, so (a) is the '
        'intended answer.', 141),
    mcq(3, 'A', 'iv', '__ is the operator can be used to compare two values?',
        [('a', '<>'), ('b', '=='),
         ('c', '><'), ('d', '=')], 'b',
        'The equality comparison operator is ==, which returns True or False. A single = is '
        'assignment, and <> / >< are not valid Python operators.', 141),
    mcq(3, 'A', 'v', '__ loop is used when the number of iterations is known in advance',
        [('a', 'While'), ('b', 'Do while'),
         ('c', 'For'), ('d', 'For each')], 'c',
        'A for loop iterates over a known sequence or a range with a known count. A while loop '
        'repeats as long as a condition is true, so its count may be unknown in advance. Python has '
        'no do-while loop.', 141),
    mcq(3, 'A', 'vi', 'Which programming language is closest to binary (0s and 1s)?',
        [('a', 'High Level language'), ('b', 'Mid-Level Language'),
         ('c', 'Low Level language'), ('d', 'Script Language')], 'c',
        'Low-level languages (machine language and assembly) are closest to the hardware; machine '
        'language is written directly in binary, and assembly maps closely to machine instructions.', 141),
    mcq(3, 'A', 'vii', 'Standard indentation in Python?',
        [('a', '2 spaces'), ('b', '4 spaces'),
         ('c', '6 spaces'), ('d', '8 spaces')], 'b',
        'PEP 8, the official Python style guide, recommends 4 spaces per indentation level. '
        'Indentation is significant in Python because it defines blocks.', 141),
    mcq(3, 'A', 'viii', '__ data type does the input() function always return.',
        [('a', 'Int'), ('b', 'Float'),
         ('c', 'String'), ('d', 'Bool')], 'c',
        'input() reads the user\'s text and always returns a string. To use a number, it must be '
        'converted explicitly, e.g. age = int(input("Age: ")).', 141),
    mcq(3, 'A', 'ix', '__ statement exits a loop immediately',
        [('a', 'Pass'), ('b', 'Continue'),
         ('c', 'Break'), ('d', 'Exit')], 'c',
        'break terminates the innermost loop at once. continue skips the rest of the current '
        'iteration; pass does nothing.', 141),
    mcq(3, 'A', 'x', '__ bitwise operator returns 1 only when BOTH bits are 1?',
        [('a', 'AND'), ('b', 'OR'),
         ('c', 'NOT'), ('d', 'XOR')], 'a',
        'The bitwise AND operator & gives 1 only where both corresponding bits are 1. OR gives 1 '
        'if either bit is 1, NOT inverts, and XOR gives 1 when the bits differ.', 141),
]

# B. Fill in the Blanks — PDF 142 (book 137)
ITEMS += [
    bq(3, 'B', 'i', 'Remarks or notes added for the developer in the source code are called ____________.',
       'comments',
       'Comments document the code for human readers. They begin with # in Python and are ignored '
       'by the interpreter.', 142),
    bq(3, 'B', 'ii', 'An identifier whose value can change during program execution is called a '
       '____________.',
       'variable',
       'A variable is a named reference to a memory location. Its value can be reassigned while the '
       'program runs, unlike a constant.', 142),
    bq(3, 'B', 'iii', 'A ____________ cannot be used as a variable name in Python.',
       'keyword (reserved word)',
       'Keywords such as if, for, while, def and class are reserved by the language for its own '
       'syntax, so they cannot be used as identifiers.', 142),
    bq(3, 'B', 'iv', 'The extension of Python source code files is ____________.',
       '.py',
       'Python source files are saved with the .py extension, e.g. calculator.py.', 142),
    bq(3, 'B', 'v', 'The statement used to execute different blocks of code based on a condition in '
       'Python is called the ____________ statement.',
       'if (conditional / selection) statement',
       'The if statement evaluates a condition and runs one block when it is true, optionally an '
       'else block when it is false; elif adds further alternatives.', 142),
]

# C. Short answers — PDF 142 (book 137)
ITEMS += [
    bq(3, 'C', 'i', 'What is a selection statement? Differentiate between if, elif, and else with an '
       'example.',
       'A selection statement chooses which block of code to execute based on a condition. Python\'s '
       'selection statements are if, if-else and if-elif-else.\n'
       'if runs its block only when the condition is true.\n'
       'elif is checked only when all previous conditions were false; any number of elif branches '
       'may follow.\n'
       'else runs when none of the above conditions is true; it has no condition of its own.\n'
       'Example:\n'
       'marks = int(input("Marks: "))\n'
       'if marks >= 80:\n'
       '    print("A")\n'
       'elif marks >= 60:\n'
       '    print("B")\n'
       'else:\n'
       '    print("C")',
       'Only one branch executes. Conditions are tested from top to bottom, and else is the '
       'fallback.', 142),
    bq(3, 'C', 'ii', 'What is the difference between a for loop and a while loop?',
       'A for loop iterates over a sequence (list, string, range) and runs once for each item. The '
       'number of iterations is known from the sequence, and the loop variable is updated '
       'automatically.\n'
       'A while loop repeats while a condition remains true. The number of iterations may be '
       'unknown in advance, and the programmer must update the control variable to avoid an '
       'infinite loop.\n'
       'Example: for i in range(5): print(i) prints 0-4. '
       'i = 0; while i < 5: print(i); i += 1 does the same, but the update must be written explicitly.',
       'Use for when iterating over a known collection or count; use while when repetition depends '
       'on a condition (e.g. reading until the user enters "quit").', 142),
    bq(3, 'C', 'iii', 'What are the three types of errors in Python? Define each in one line.',
       '1. Syntax error \u2014 the code violates Python\'s grammar and cannot be parsed, so the program '
       'does not start (e.g. missing colon).\n'
       '2. Runtime error (exception) \u2014 the code is syntactically valid but fails while running, '
       'e.g. division by zero or an index out of range.\n'
       '3. Logical error \u2014 the program runs without crashing but produces a wrong result because '
       'the logic is incorrect, e.g. using + instead of * in an average.',
       'Syntax errors are caught before execution, runtime errors during execution, and logical '
       'errors only by testing expected outputs.', 142),
    bq(3, 'C', 'iv', 'What is debugging? Explain the techniques used for debugging.',
       'Debugging is the process of finding, understanding and fixing errors in a program.\n'
       'Techniques:\n'
       '\u2022 Reading the traceback carefully \u2014 it names the error type and the line where it occurred.\n'
       '\u2022 Using print() statements to display variables at key points and compare with expected values.\n'
       '\u2022 Using a debugger with breakpoints and single-step execution to inspect the program state.\n'
       '\u2022 Code review / rubber-duck explanation \u2014 reading the code aloud or with a partner to spot mistakes.\n'
       '\u2022 Testing with edge cases (zero, empty input, negative numbers, large values) and comparing '
       'actual with expected output.\n'
       '\u2022 Isolating the faulty part by commenting out sections or reducing the program to a minimal '
       'reproducible case.',
       'Debugging is iterative: reproduce the bug, locate it, fix it, then re-test to confirm the '
       'fix and check that nothing else broke.', 142),
    bq(3, 'C', 'v', 'Define following terms: (a) Sequence (b) Datatype (c) Repetition (d) Variable '
       '(e) Arithmetic Operator',
       '(a) Sequence: execution of statements one after another in the order written; it is the '
       'default control flow.\n'
       '(b) Datatype: the kind of value a variable can hold, which determines the operations allowed '
       'and the memory used (int, float, str, bool, list, tuple, dict, set).\n'
       '(c) Repetition: executing a block of code more than once, using a for or while loop.\n'
       '(d) Variable: a named memory location whose value can change during execution, e.g. count = 5.\n'
       '(e) Arithmetic Operator: a symbol that performs a mathematical operation on operands: +, -, '
       '*, /, //, %, **.',
       'Sequence, selection and repetition are the three control structures; datatype, variable and '
       'operator are the basic building blocks of expressions.', 142),
]

# D. Detailed answers — PDF 142 (book 137)
ITEMS += [
    bq(3, 'D', 'i', 'What are control structures in Python? Explain Sequence, Selection (if, if-else, '
       'if-elif-else, Nested if), and Repetition (for loop, while loop, Nested loop) with syntax and '
       'code examples for each.',
       'Control structures determine the order in which statements execute. Python has three: '
       'sequence, selection and repetition.\n'
       '1. Sequence \u2014 statements run top to bottom.\n'
       '   a = 5\n'
       '   b = 3\n'
       '   print(a + b)      # 8\n'
       '2. Selection \u2014 choose a block by condition.\n'
       '   if condition:\n'
       '       block\n'
       '   if-else:\n'
       '   if marks >= 40:\n'
       '       print("Pass")\n'
       '   else:\n'
       '       print("Fail")\n'
       '   if-elif-else:\n'
       '   if marks >= 80:\n'
       '       print("A")\n'
       '   elif marks >= 60:\n'
       '       print("B")\n'
       '   else:\n'
       '       print("C")\n'
       '   Nested if:\n'
       '   if age >= 18:\n'
       '       if citizen:\n'
       '           print("Eligible to vote")\n'
       '3. Repetition \u2014 repeat a block.\n'
       '   for loop (known count):\n'
       '   for i in range(1, 6):\n'
       '       print(i)          # 1 2 3 4 5\n'
       '   while loop (condition-controlled):\n'
       '   n = 5\n'
       '   while n > 0:\n'
       '       print(n)\n'
       '       n -= 1\n'
       '   Nested loop:\n'
       '   for i in range(1, 4):\n'
       '       for j in range(1, 4):\n'
       '           print(i, j)\n'
       'Indentation (4 spaces) defines each block in Python.',
       'Any program can be built from these three structures. Selection chooses among alternatives; '
       'repetition repeats work; nesting combines them.', 142),
    bq(3, 'D', 'ii', 'Explain variables and data types in Python. List all built-in data types with '
       'their names, type keywords, descriptions, and examples in the form of a table.',
       'A variable is a name that refers to a value stored in memory. In Python a variable is '
       'created by assignment (x = 10) and its type is inferred from the value; no explicit '
       'declaration is needed. Names follow the identifier rules and should be descriptive.\n'
       'Built-in data types:\n'
       'Name | Type keyword | Description | Example\n'
       'Integer | int | whole numbers | 42\n'
       'Float | float | decimal numbers | 3.14\n'
       'String | str | text in quotes | "Salam"\n'
       'Boolean | bool | True or False | True\n'
       'List | list | ordered, mutable collection | [1, 2, 3]\n'
       'Tuple | tuple | ordered, immutable collection | (1, 2, 3)\n'
       'Dictionary | dict | key-value pairs | {"name": "Ali"}\n'
       'Set | set | unordered collection of unique items | {1, 2, 3}\n'
       'Complex | complex | real + imaginary part | 2 + 3j\n'
       'NoneType | None | the type of the single value None, meaning "no value" | None\n'
       'The type of a value can be checked with type(x), and converted with int(), float(), str(), '
       'bool(), list() etc.',
       'Python is dynamically typed: the same variable can later refer to a value of a different '
       'type. Lists and dictionaries are mutable; tuples and strings are immutable.', 142),
    bq(3, 'D', 'iii', 'Describe input and output handling in Python. Explain the print() and input() '
       'functions with their syntax, purpose, and at least two code examples each.',
       'Output: print() displays values on the screen.\n'
       'Syntax: print(value1, value2, ..., sep=" ", end="\\n")\n'
       'Purpose: write text, numbers or expressions to standard output; sep sets the separator '
       'between values and end sets what is printed after the last value.\n'
       'Examples:\n'
       'print("Hello, World!")\n'
       'name = "Ali"\n'
       'print("Name:", name, sep=" -> ")     # Name: -> Ali\n'
       'print("A", "B", sep="-", end="!")    # A-B!\n'
       'Input: input() reads a line of text typed by the user.\n'
       'Syntax: input(prompt)\n'
       'Purpose: pause the program, show an optional prompt and return the entered text as a '
       'string.\n'
       'Examples:\n'
       'name = input("Enter your name: ")\n'
       'print("Welcome,", name)\n'
       'age = int(input("Enter your age: "))   # convert string to int\n'
       'print("Next year you will be", age + 1)\n'
       'Because input() always returns str, numeric input must be converted with int() or float().',
       'print() is for output; input() is for input. The prompt written inside input() is displayed '
       'to the user but is not part of the returned value.', 142),
    bq(3, 'D', 'iv', 'Explain all Arithmetic and Assignment Operators in Python with their symbols, '
       'purpose, examples, and results in tabular form. Also write a code example for each.',
       'Arithmetic operators (a = 10, b = 3):\n'
       'Operator | Purpose | Example | Result\n'
       '+ | addition | a + b | 13\n'
       '- | subtraction | a - b | 7\n'
       '* | multiplication | a * b | 30\n'
       '/ | true division | a / b | 3.3333\n'
       '// | floor division | a // b | 3\n'
       '% | modulus (remainder) | a % b | 1\n'
       '** | exponentiation | a ** b | 1000\n'
       'Assignment operators:\n'
       'Operator | Purpose | Example | Result (starting a = 10)\n'
       '= | assign | a = 5 | a becomes 5\n'
       '+= | add and assign | a += 3 | a becomes 13\n'
       '-= | subtract and assign | a -= 3 | a becomes 7\n'
       '*= | multiply and assign | a *= 3 | a becomes 30\n'
       '/= | divide and assign | a /= 2 | a becomes 5.0\n'
       '//= | floor-divide and assign | a //= 3 | a becomes 3\n'
       '%= | modulus and assign | a %= 3 | a becomes 1\n'
       '**= | exponentiate and assign | a **= 2 | a becomes 100\n'
       'Code example:\n'
       'a = 10\n'
       'b = 3\n'
       'print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)\n'
       'a += 5      # 15\n'
       'a *= 2      # 30\n'
       'print(a)',
       'Arithmetic operators produce a value; assignment operators store a value back into a '
       'variable. The compound form x += y is shorthand for x = x + y.', 142),
    bq(3, 'D', 'v', 'What are the different types of error in Python? Explain each type in detail '
       'with code examples for each type. Also describe the technique of reading error messages '
       '(Tracebacks).',
       '1. Syntax error \u2014 the parser cannot understand the code, so nothing runs.\n'
       '   Example: if x > 5 print(x)   (missing colon)\n'
       '   Python reports "SyntaxError: expected \':\'" and points to the line.\n'
       '2. Runtime error (exception) \u2014 the syntax is valid but an operation fails during execution.\n'
       '   Example: print(10 / 0)  \u2192 ZeroDivisionError: division by zero\n'
       '   Example: print(names[5])  \u2192 IndexError: list index out of range\n'
       '   Example: print(int("abc"))  \u2192 ValueError: invalid literal for int()\n'
       '3. Logical error \u2014 the program runs and produces output, but the output is wrong because '
       'the logic is wrong.\n'
       '   Example: average = a + b / 2  should be (a + b) / 2; the program prints a wrong average '
       'without any error message.\n'
       'Reading a traceback: read the LAST line first (it names the exception), then the line above '
       'it (the exact statement and line number), then follow the "File ... line ..." frames upward '
       'to see which function called which. The caret (^) shows where Python detected the problem. '
       'Fix the cause, not just the symptom, and re-run to confirm.',
       'Syntax and runtime errors announce themselves; logical errors must be found by testing. The '
       'traceback is read bottom-up: exception type, message, then the failing line.', 142),
]

# E. Activities — PDF 143 (book 138)
ITEMS += [
    bq(3, 'E', 1, 'Write a program of arithmetic calculator that takes two integer input from user '
       'also take a choice for arithmetic calculation. Display proper messages for user.',
       'a = int(input("Enter first number: "))\n'
       'b = int(input("Enter second number: "))\n'
       'print("1. Add  2. Subtract  3. Multiply  4. Divide")\n'
       'choice = input("Enter your choice (1-4): ")\n'
       'if choice == "1":\n'
       '    print("Result =", a + b)\n'
       'elif choice == "2":\n'
       '    print("Result =", a - b)\n'
       'elif choice == "3":\n'
       '    print("Result =", a * b)\n'
       'elif choice == "4":\n'
       '    if b != 0:\n'
       '        print("Result =", a / b)\n'
       '    else:\n'
       '        print("Error: division by zero is not allowed")\n'
       'else:\n'
       '    print("Invalid choice")',
       'The choice is compared as a string, so the user input is not converted to int. Division is '
       'guarded against zero, and every branch prints a clear message.', 143),
    bq(3, 'E', 2, 'Create a "guess the number" game where the player has only one chance to guess '
       'the correct number. Use Python\'s random module to generate a random number and compare it '
       'with the user\'s input. If the guess matches the number, print "You win"; otherwise, print '
       '"You lose".',
       'import random\n'
       'secret = random.randint(1, 10)\n'
       'guess = int(input("Guess a number between 1 and 10: "))\n'
       'if guess == secret:\n'
       '    print("You win")\n'
       'else:\n'
       '    print("You lose")\n'
       '    print("The number was", secret)',
       'random.randint(1, 10) returns an integer from 1 to 10 inclusive. Comparing the converted '
       'input with the secret using == gives the win/lose branch.', 143),
    bq(3, 'E', 3, 'Write a Python program that simulates a basic ATM Machine using simple data types '
       '(int, float, str, bool). The program should combine Selection (if/elif/else) and Repetition '
       '(while loop) statements to perform real-world banking operations such as PIN verification, '
       'balance inquiry, cash deposit, and cash withdrawal. The output of the program should look '
       'like the following.',
       'balance = 10000.00\n'
       'pin = "1234"\n'
       'attempts = 0\n'
       'logged_in = False\n'
       'print("========== WELCOME TO ATM ==========")\n'
       'while attempts < 3 and not logged_in:\n'
       '    entered = input("Enter PIN: ")\n'
       '    if entered == pin:\n'
       '        logged_in = True\n'
       '    else:\n'
       '        attempts += 1\n'
       '        print("Wrong PIN!", 3 - attempts, "attempt(s) left.")\n'
       'if not logged_in:\n'
       '    print("Card blocked. Please contact your bank.")\n'
       'else:\n'
       '    print("Login Successful!")\n'
       '    while True:\n'
       '        print("-------- ATM MENU --------")\n'
       '        print("1. Check Balance")\n'
       '        print("2. Deposit")\n'
       '        print("3. Withdraw")\n'
       '        print("4. Exit")\n'
       '        choice = input("Choose (1-4): ")\n'
       '        if choice == "1":\n'
       '            print(f"Your Balance: Rs. {balance:.2f}")\n'
       '        elif choice == "2":\n'
       '            amount = float(input("Enter deposit amount: Rs. "))\n'
       '            balance += amount\n'
       '            print(f"Deposited Rs. {amount:.2f}")\n'
       '            print(f"New Balance: Rs. {balance:.2f}")\n'
       '        elif choice == "3":\n'
       '            amount = float(input("Enter withdrawal amount: Rs. "))\n'
       '            if amount <= balance:\n'
       '                balance -= amount\n'
       '                print(f"Withdrawn Rs. {amount:.2f}")\n'
       '                print(f"Remaining Balance: Rs. {balance:.2f}")\n'
       '            else:\n'
       '                print("Insufficient balance")\n'
       '        elif choice == "4":\n'
       '            print("Thank you! Goodbye.")\n'
       '            break\n'
       '        else:\n'
       '            print("Invalid choice")',
       'The outer while loop allows up to three PIN attempts; the inner while loop repeats the menu '
       'until the user chooses Exit. balance is a float, pin and choice are strings, and logged_in '
       'is a bool. Withdrawal is checked against the balance before subtracting.', 143),
]
