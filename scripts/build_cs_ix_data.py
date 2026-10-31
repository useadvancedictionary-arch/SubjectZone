#!/usr/bin/env python3
"""Builds public/data/class_ix_cs.json for the SubjectZone app.

Computer Science IX (Sindh Textbook Board, Jamshoro): 7 units covering
Fundamentals of Computer, Fundamentals of Operating System, Office Automation,
Data Communication and Computer Networks, Computer Security and Ethics,
Web Development, and Introduction to Database System.

The CS IX PDF has extractable text, so the exercises were captured from the
extracted text (scripts/cs_ix_text/all.txt) plus the rendered page images for
the "Match the columns" tables.

Book page = PDF page - 6 (6 pages of cover/contents before Unit 1 starts).
Each unit exercise has: A = Choose the right answer (MCQs),
B = Respond the following (short questions),
C = Match the columns, and a separate ACTIVITIES list.
The book contains NO printed answer key, so answers are derived from the
content and standard computer-science knowledge.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'public', 'data', 'class_ix_cs.json')

# (unit_number, title, pdf_start, pdf_end)
# Book page 1 = PDF page 7, so bookPage = pdfPage - 6
CHAPTERS = [
    (1, 'Fundamentals of Computer',               7,   35),
    (2, 'Fundamentals of Operating System',       36,  51),
    (3, 'Office Automation',                      52,  70),
    (4, 'Data Communication and Computer Networks', 71,  100),
    (5, 'Computer Security and Ethics',           101, 122),
    (6, 'Web Development',                        123, 147),
    (7, 'Introduction to Database System',        148, 168),
]

TOTAL_PAGES = 168
FRONT_MATTER_PAGES = 6

SEC_LABEL = {
    'A': 'MCQs',
    'B': 'Short Questions',
    'C': 'Match the Columns',
    'D': 'Activities',
}


def sec(chapter, letter):
    return f'Exercise {chapter} {SEC_LABEL.get(letter, letter)}'


def q(qid, chapter, letter, number, qtype, question, answer, explanation, pdf_page,
      options=None, correct=None):
    d = {
        'id': qid,
        'chapter': chapter,
        'section': sec(chapter, letter),
        'sectionCode': f'EX{chapter}{letter}',
        'type': qtype,
        'number': number,
        'question': question,
        'answer': answer,
        'explanation': explanation,
        'pdfPage': pdf_page,
        'bookPage': pdf_page - 6,
        'figure': None,
    }
    if qtype == 'mcq':
        d['options'] = [{'key': k, 'text': t} for k, t in options]
        d['optionsRaw'] = '  '.join(f'({k}) {t}' for k, t in options)
        d['correctAnswer'] = correct
    return d


SOLVED = []

# ============================================================================
# UNIT 1 — Fundamentals of Computer   PDF pages 7-35
# A = MCQs (PDF 32-33), B = Short Qs (PDF 33), C = Match (PDF 34), D = Activities (PDF 35)
# ============================================================================

C, S = 1, 'A'
SOLVED += [
    q('u1_exA_q1', C, S, 1, 'mcq',
      'The device that converts hard copy into soft copy is:',
      '(c) scanner',
      'A scanner reads a physical document (hard copy) and converts it into a digital image/file (soft copy). A printer and a plotter do the opposite (soft copy to hard copy); a barcode reader only reads barcode data.',
      32,
      [('a', 'printer'), ('b', 'plotter'), ('c', 'scanner'), ('d', 'barcode reader')], '(c)'),
    q('u1_exA_q2', C, S, 2, 'mcq',
      'The volatile memory:',
      '(b) loses contents as the power is disconnected',
      'Volatile memory (RAM) keeps its data only while the computer is powered on; as soon as the power is switched off, its contents are lost. ROM is non-volatile and retains its contents permanently.',
      32,
      [('a', 'is permanent'), ('b', 'loses contents as the power is disconnected'),
       ('c', 'possesses large storage'), ('d', 'manages hardware resources')], '(b)'),
    q('u1_exA_q3', C, S, 3, 'mcq',
      'Media players are:',
      '(c) entertainment software',
      'Media players (e.g., VLC, Windows Media Player) are application software used to play music and video for enjoyment, so they belong to the entertainment software category.',
      32,
      [('a', 'business software'), ('b', 'education software'),
       ('c', 'entertainment software'), ('d', 'productivity software')], '(c)'),
    q('u1_exA_q4', C, S, 4, 'mcq',
      'The programs that are generally installed to manage and maintain overall computer resources is:',
      '(a) operating system',
      'The operating system (Windows, Linux, etc.) is the system software that manages all hardware and software resources of the computer — processor, memory, files and input/output devices.',
      32,
      [('a', 'operating system'), ('b', 'utility program'),
       ('c', 'language translator'), ('d', 'device driver')], '(a)'),
    q('u1_exA_q5', C, S, 5, 'mcq',
      'Modern languages use:',
      '(a) compiler',
      'Modern high-level languages (C, C++, Java) are translated into machine code by a compiler, which reads the whole program and produces an object/executable file. An assembler is used for low-level assembly language, not for modern high-level languages.',
      32,
      [('a', 'compiler'), ('b', 'interpreter'), ('c', 'convertor'), ('d', 'assembler')], '(a)'),
    q('u1_exA_q6', C, S, 6, 'mcq',
      'A collection of wires connecting the CPU with main memory that is used to identify particular locations is:',
      '(c) address bus',
      'The address bus carries memory addresses from the CPU to main memory so that a particular location can be identified. The data bus carries the actual data, and the control bus carries control/timing signals.',
      32,
      [('a', 'control bus'), ('b', 'data bus'), ('c', 'address bus'), ('d', 'memory bus')], '(c)'),
    q('u1_exA_q7', C, S, 7, 'mcq',
      'The inexpensive and most commonly used computers are:',
      '(d) microcomputer',
      'Microcomputers (personal computers, laptops) are the smallest and least expensive class of digital computers and are the most commonly used in homes, schools and offices. Supercomputers, mainframes and minicomputers are larger and costlier.',
      32,
      [('a', 'super computer'), ('b', 'mainframe computer'),
       ('c', 'minicomputer'), ('d', 'microcomputer')], '(d)'),
    q('u1_exA_q8', C, S, 8, 'mcq',
      'Computer cannot start without:',
      '(a) operating system',
      'A computer cannot be used until the operating system is loaded, because the OS manages the hardware and software and provides the environment in which all other programs run.',
      32,
      [('a', 'operating system'), ('b', 'utility program'),
       ('c', 'device drivers'), ('d', 'business software')], '(a)'),
    q('u1_exA_q9', C, S, 9, 'mcq',
      'Graphical User Interface (GUI) was developed in:',
      '(b) fourth generation',
      'The fourth generation of computers (1971 onwards) used microprocessors and saw the development of Graphical User Interfaces (GUIs), which let users work with windows, icons and a mouse instead of typing commands.',
      33,
      [('a', 'second generation'), ('b', 'fourth generation'),
       ('c', 'mechanical era'), ('d', 'electro-mechanical era')], '(b)'),
    q('u1_exA_q10', C, S, 10, 'mcq',
      'A person who uses different programming languages to develop programs is:',
      '(c) software engineer',
      'A software engineer/programmer writes, tests and maintains computer programs using programming languages. A database administrator manages databases, a web designer designs web pages and a graphic designer creates visual content.',
      33,
      [('a', 'database administrator'), ('b', 'web designer'),
       ('c', 'software engineer'), ('d', 'graphic designer')], '(c)'),

    q('u1_exB_q1', C, 'B', 1, 'sq',
      'Discuss the use of computer in any two fields of life.',
      'Computers are used in almost every field of life. Two important fields are:\n\n'
      '• Education: computers help in teaching and learning through e-learning software, multimedia presentations, online classes, research, and preparing assignments and reports.\n'
      '• Business: computers are used for accounting, payroll, inventory, billing, e-commerce, email communication and maintaining records of customers and employees.\n\n'
      'Other fields include health, banking, engineering, transport and entertainment.',
      'Computers increase speed, accuracy and efficiency and can store and process huge amounts of data, which is why they are widely used in every profession.',
      33),
    q('u1_exB_q2', C, 'B', 2, 'sq',
      'Differentiate Compiler and Assembler.',
      '• Compiler: a language translator that converts a complete high-level language program (e.g., C, C++, Java) into machine code in one go and produces an object/executable file. It reads the whole program and reports all errors together.\n'
      '• Assembler: a translator that converts a program written in assembly language (low-level language using mnemonics such as MOV, ADD) into machine code.\n\n'
      'Key difference: a compiler translates high-level language, while an assembler translates assembly (low-level) language.',
      'Both are language translators (system software), but they work on different levels of language.',
      33),
    q('u1_exB_q3', C, 'B', 3, 'sq',
      'Differentiate System and Application software.',
      '• System software: controls and manages the computer hardware and provides a platform on which other programs run. Examples: operating system (Windows, Linux), device drivers, utilities and language translators.\n'
      '• Application software: designed to help the user perform a specific task. Examples: MS Word, MS Excel, media players, web browsers and games.\n\n'
      'Difference: system software runs the computer itself and is usually written in low-level languages; application software is used by the end user for a particular job.',
      'System software is the base on which application software runs — for example, MS Word (application) needs Windows (system software) to run.',
      33),
    q('u1_exB_q4', C, 'B', 4, 'sq',
      'Describe artificial intelligence with examples.',
      'Artificial intelligence (AI) is the branch of computer science in which computers/machines are made to simulate human intelligence — they can learn, reason, understand language and make decisions like humans.\n\n'
      'Examples: voice assistants (Siri, Alexa), chatbots, self-driving cars, face-recognition systems, recommendation engines (YouTube/Netflix suggestions) and chess-playing programs.',
      'AI uses large amounts of data and algorithms to learn from experience and improve its performance, which is known as machine learning.',
      33),
    q('u1_exB_q5', C, 'B', 5, 'sq',
      'Discuss Impact and Non-Impact Printers with examples.',
      '• Impact printers: strike a print head or ribbon against the paper to form characters (like a typewriter). They are noisy but cheap for large-volume printing. Examples: dot-matrix printer, daisy-wheel printer, line printer.\n'
      '• Non-impact printers: form the image without touching the paper. They are quieter, faster and give better print quality. Examples: inkjet printer, laser printer, thermal printer.',
      'Impact printers are still used for multi-copy carbon forms; non-impact printers are preferred for high-quality colour printing.',
      33),
    q('u1_exB_q6', C, 'B', 6, 'sq',
      'Write the use of these storage devices: Hard Disk, USB Flash Disk, SD Card.',
      '• Hard Disk: a secondary storage device fitted inside the system unit; stores large amounts of data permanently (operating system, software, files) and gives fast access.\n'
      '• USB Flash Disk: a small, portable, rewritable solid-state device used to carry and transfer data between computers.\n'
      '• SD Card: a small flash memory card used in portable devices such as digital cameras, mobile phones and tablets to store photos, videos and other files.',
      'All three are secondary (auxiliary) storage devices; the USB flash disk and SD card are removable while the hard disk is usually fixed inside the computer.',
      33),
    q('u1_exB_q7', C, 'B', 7, 'sq',
      'Which monitor will you prefer in your school; CRT or FPD? Why?',
      'I would prefer a FPD (Flat Panel Display, e.g., LCD/LED) monitor for the school.\n\n'
      'Reasons:\n'
      '• It is thin and light and occupies less desk space.\n'
      '• It consumes less power and produces less heat.\n'
      '• It gives a sharper, flicker-free picture that is easier on the eyes.\n'
      '• It is safer because it has no high-voltage CRT tube.',
      'A CRT (Cathode Ray Tube) monitor is bulky, heavy and consumes more power, so FPD is the modern and preferred choice.',
      33),
    q('u1_exB_q8', C, 'B', 8, 'sq',
      'List any five components present on motherboard.',
      'Five components found on a motherboard:\n'
      '1. Microprocessor (CPU) and its socket.\n'
      '2. RAM slots (main memory).\n'
      '3. ROM/BIOS chip.\n'
      '4. Buses (data bus, address bus, control bus).\n'
      '5. Expansion slots (PCI/PCIe) and ports (USB, VGA, etc.).\n\n'
      'Other parts include capacitors, resistors, diodes, transistors, jumpers and the chipset.',
      'The motherboard is the main circuit board that connects and allows communication between all the parts of the computer.',
      33),
    q('u1_exB_q9', C, 'B', 9, 'sq',
      'Prepare a table of generations.',
      '| Generation | Period | Technology | Example of Machines |\n'
      '|---|---|---|---|\n'
      '| First | 1940–1956 | Vacuum Tubes | ENIAC, UNIVAC |\n'
      '| Second | 1956–1963 | Transistors | IBM 1401, IBM 7094 |\n'
      '| Third | 1964–1971 | Integrated Circuits (ICs) | IBM 360, IBM 370 |\n'
      '| Fourth | 1971–Present | Microprocessors | IBM PC, Apple II |\n'
      '| Fifth | Present and Beyond | Artificial Intelligence | IBM Watson, smart devices |',
      'Each generation is named after the core technology used to build the computers, and each step made computers smaller, faster, cheaper and more powerful.',
      33),
    q('u1_exB_q10', C, 'B', 10, 'sq',
      'Give examples of business, education, entertainment and productivity software.',
      '• Business software: accounting/payroll software, inventory and billing software, MS Excel for bookkeeping.\n'
      '• Education software: MS PowerPoint, e-learning/LMS software, typing tutor, digital encyclopedias.\n'
      '• Entertainment software: media players (VLC), computer games, video editing software.\n'
      '• Productivity software: MS Word, MS Excel, MS PowerPoint and MS Access.',
      'Productivity software helps individuals to create documents, spreadsheets and presentations, while business/education/entertainment software serves specific industries or purposes.',
      34),

    q('u1_exC_q1', C, 'C', 1, 'sq',
      'Match the columns: (i) ALU',
      '(d) Perform arithmetic and logical operations',
      'The Arithmetic Logic Unit (ALU) is the part of the CPU that carries out all arithmetic (+, −, ×, ÷) and logical (comparison) operations.',
      34),
    q('u1_exC_q2', C, 'C', 2, 'sq',
      'Match the columns: (ii) Input Devices',
      '(g) Hardware device that sends data into a computer',
      'Input devices (keyboard, mouse, scanner, etc.) are hardware devices that feed data and instructions into the computer.',
      34),
    q('u1_exC_q3', C, 'C', 3, 'sq',
      'Match the columns: (iii) Secondary Storage Devices',
      '(f) Large storage capacity, store data permanently',
      'Secondary storage devices (hard disk, USB flash disk, optical discs) have large capacity and keep data permanently even when the power is off.',
      34),
    q('u1_exC_q4', C, 'C', 4, 'sq',
      'Match the columns: (iv) Productivity Software',
      '(e) Helps to produce spreadsheets, database etc.',
      'Productivity software such as MS Excel and MS Access helps users produce spreadsheets, databases, documents and presentations.',
      34),
    q('u1_exC_q5', C, 'C', 5, 'sq',
      'Match the columns: (v) Mechanical Era',
      '(a) Period of manually operated machines',
      'In the mechanical era (before electronics) devices such as the abacus and Babbage\'s Analytical Engine were operated manually.',
      34),
    q('u1_exC_q6', C, 'C', 6, 'sq',
      'Match the columns: (vi) Digital Computers',
      '(c) Process information using binary number system',
      'Digital computers work only with discrete data and process all information in the binary number system (0 and 1).',
      34),
    q('u1_exC_q7', C, 'C', 7, 'sq',
      'Match the columns: (vii) Microcomputer',
      '(b) PC',
      'A microcomputer is a small, inexpensive computer that uses a single microprocessor; the Personal Computer (PC) is the common example.',
      34),

    q('u1_exD_q1', C, 'D', 1, 'sq',
      'Develop a timeline for major innovations in computer evolution.',
      'Timeline of major innovations:\n'
      '• c. 3000 BC — Abacus (first calculating device).\n'
      '• 1617 — Napier\'s bones (logarithms).\n'
      '• 1642 — Pascaline (Pascal\'s adding machine).\n'
      '• 1837 — Analytical Engine (Charles Babbage; "Father of the Computer").\n'
      '• 1890 — Hollerith punched-card tabulating machine.\n'
      '• 1946 — ENIAC, the first general-purpose electronic computer (vacuum tubes).\n'
      '• 1956 — Transistor computers (second generation).\n'
      '• 1964 — Integrated Circuit (IC) computers (third generation).\n'
      '• 1971 — Intel 4004 microprocessor; start of personal computers.\n'
      '• 1981 — IBM PC; 1990s — Internet and World Wide Web.\n'
      '• 2000s–present — Smartphones, cloud computing and Artificial Intelligence.',
      'The timeline shows the progress from mechanical calculating aids to modern electronic and AI-based computers.',
      35),
    q('u1_exD_q2', C, 'D', 2, 'sq',
      'Prepare a list of input and output devices and write their uses.',
      'Input devices and uses:\n'
      '• Keyboard — typing text and commands.\n'
      '• Mouse — pointing, clicking and selecting.\n'
      '• Scanner — converting printed documents into digital files.\n'
      '• Microphone — entering sound/voice.\n'
      '• Webcam — capturing images and video.\n\n'
      'Output devices and uses:\n'
      '• Monitor — displaying soft copy output.\n'
      '• Printer — producing hard copy on paper.\n'
      '• Plotter — printing large engineering drawings.\n'
      '• Speaker — producing sound output.\n'
      '• Projector — displaying output on a large screen.',
      'Input devices bring data into the computer; output devices present the processed result to the user.',
      35),
    q('u1_exD_q3', C, 'D', 3, 'sq',
      'Make a list of specifications that you should know before buying a computer.',
      'Specifications to check before buying a computer:\n'
      '1. Processor (CPU) model and speed (e.g., Intel Core i5, 2.5 GHz).\n'
      '2. RAM size (e.g., 8 GB).\n'
      '3. Hard disk/SSD capacity (e.g., 512 GB SSD).\n'
      '4. Monitor size and resolution.\n'
      '5. Graphics card (dedicated/integrated).\n'
      '6. Ports (USB, HDMI) and connectivity (Wi-Fi, Bluetooth).\n'
      '7. Operating system and warranty.',
      'Knowing these specifications helps you buy a computer that matches your needs and budget.',
      35),
    q('u1_exD_q4', C, 'D', 4, 'sq',
      'List analog, digital and hybrid devices from your surroundings (any five).',
      '• Analog devices: mercury thermometer, analog clock/wristwatch, analog bathroom scale, speedometer of an old car, mercury barometer.\n'
      '• Digital devices: digital watch, calculator, mobile phone, digital camera, digital weighing scale.\n'
      '• Hybrid devices: laptop computer, smartphone, digital thermostat, modern car dashboard, UPS (uninterruptible power supply with digital display).',
      'Analog devices work with continuous values, digital devices with discrete (0/1) values, and hybrid devices use both.',
      35),
    q('u1_exD_q5', C, 'D', 5, 'sq',
      'Label the following block diagram of computer system.',
      'The block diagram of a computer system has five main blocks:\n'
      '• Input Unit — accepts data and instructions (keyboard, mouse).\n'
      '• CPU (Central Processing Unit) — contains the ALU, Control Unit and registers; processes the data.\n'
      '• Memory Unit — stores data and instructions (primary memory: RAM/ROM).\n'
      '• Output Unit — presents the result (monitor, printer).\n'
      '• Arrows between the blocks show the flow of data and control signals.',
      'The CPU, memory, input and output unit together form the basic computer system.',
      35),
]


# ============================================================================
# UNIT 2 — Fundamentals of Operating System   PDF pages 36-51
# A = MCQs (PDF 49-50), B = Short Qs (PDF 50), C = Match (PDF 51), D = Activities (PDF 51)
# ============================================================================

C = 2
SOLVED += [
    q('u2_exA_q1', C, S, 1, 'mcq',
      'The software which performs all basic tasks is:',
      '(c) operating system',
      'The operating system performs all the basic tasks of the computer such as managing the processor, memory, files and input/output devices and providing a user interface.',
      49,
      [('a', 'antivirus'), ('b', 'start menu'), ('c', 'operating system'), ('d', 'office automation')], '(c)'),
    q('u2_exA_q2', C, S, 2, 'mcq',
      'A program that enables user to interact with computer is called:',
      '(d) interface',
      'The user interface (CLI or GUI) is the part of the operating system that allows the user to communicate with and control the computer.',
      49,
      [('a', 'my document'), ('b', 'start menu'), ('c', 'desktop'), ('d', 'interface')], '(d)'),
    q('u2_exA_q3', C, S, 3, 'mcq',
      'The process of checking computer, starting operating system and making it ready to work is referred to as:',
      '(b) booting',
      'Booting is the process in which the computer checks its hardware, loads the operating system into memory and becomes ready for the user to work.',
      49,
      [('a', 'resource management'), ('b', 'booting'),
       ('c', 'error checking'), ('d', 'file management')], '(b)'),
    q('u2_exA_q4', C, S, 4, 'mcq',
      'The number of user(s) that can access the resources simultaneously on a Multi-user OS is/are:',
      '(c) many',
      'A multi-user operating system allows many users to access the computer and its resources at the same time (e.g., over a network/server).',
      49,
      [('a', 'one'), ('b', 'two'), ('c', 'many'), ('d', 'only administrators')], '(c)'),
    q('u2_exA_q5', C, S, 5, 'mcq',
      'Which management controls the dynamic allocation and de-allocation of processor, memory, etc?',
      '(a) Resource',
      'Resource Management dynamically allocates and de-allocates the computer\'s resources (processor time, memory, devices) among the running programs.',
      49,
      [('a', 'Resource'), ('b', 'File'), ('c', 'I/O'), ('d', 'User')], '(a)'),
    q('u2_exA_q6', C, S, 6, 'mcq',
      'In which operating system jobs are executed in groups?',
      '(a) Batch Processing',
      'In a batch processing operating system, similar jobs are collected into groups (batches) and executed one after another without user interaction.',
      49,
      [('a', 'Batch Processing'), ('b', 'Time Sharing'),
       ('c', 'Single User'), ('d', 'Real Time')], '(a)'),
    q('u2_exA_q7', C, S, 7, 'mcq',
      'The system that guarantees that critical tasks should be completed without shortest delay is:',
      '(b) Hard Real Time',
      'A hard real time system guarantees that critical tasks are completed within a strict deadline; missing the deadline could cause serious damage (e.g., airbag or pacemaker systems).',
      50,
      [('a', 'Batch Processing'), ('b', 'Hard Real Time'),
       ('c', 'Soft Real Time'), ('d', 'Time Sharing')], '(b)'),
    q('u2_exA_q8', C, S, 8, 'mcq',
      'DOS is an example of:',
      '(c) Single User OS',
      'MS-DOS is a single-user, single-tasking operating system — only one user can work on the computer at a time.',
      50,
      [('a', 'Real Time Processing OS'), ('b', 'Multi Processing OS'),
       ('c', 'Single User OS'), ('d', 'Multi User OS')], '(c)'),
    q('u2_exA_q9', C, S, 9, 'mcq',
      'The group of programs that helps office workers to do a number of routine tasks easily and efficiently is called:',
      '(d) office automation',
      'Office automation software (MS Word, Excel, PowerPoint, Outlook) helps office workers perform routine tasks such as typing, calculating, presenting and communicating easily and efficiently.',
      50,
      [('a', 'operating system'), ('b', 'e-mail'), ('c', 'anti-virus'), ('d', 'office automation')], '(d)'),
    q('u2_exA_q10', C, S, 10, 'mcq',
      'The operating system that allows frequent switching from one task to another is:',
      '(d) Time Sharing',
      'A time-sharing operating system gives each user/program a small slice of CPU time in turn, so it can switch frequently from one task to another.',
      50,
      [('a', 'Batch Processing'), ('b', 'Real Time Processing'),
       ('c', 'Single User'), ('d', 'Time Sharing')], '(d)'),

    q('u2_exB_q1', C, 'B', 1, 'sq',
      'Define Operating System. Give three examples of operating systems.',
      'An operating system (OS) is system software that manages all the hardware and software resources of a computer and provides an interface between the user and the computer. It controls the processor, memory, files and input/output devices.\n\n'
      'Examples: Microsoft Windows, Linux, macOS (also Android and iOS for mobile devices).',
      'Without an operating system a computer cannot be started or used.',
      50),
    q('u2_exB_q2', C, 'B', 2, 'sq',
      'List the functions of an OS? Write briefly about any two.',
      'Functions of an OS: process/task management, memory management, file management, input/output management, resource management, providing a user interface, and security/error handling.\n\n'
      '• File Management: the OS organizes data into files and folders, keeps track of where each file is stored, and controls creating, reading, writing, renaming and deleting of files.\n'
      '• Memory Management: the OS keeps track of which parts of main memory are in use, allocates memory to programs when needed and frees it when no longer required.',
      'These functions make sure that all programs get the resources they need and that the system runs smoothly.',
      50),
    q('u2_exB_q3', C, 'B', 3, 'sq',
      'Differentiate between CLI and GUI. Write any two benefits of each.',
      '• CLI (Command Line Interface): the user types text commands to give instructions (e.g., MS-DOS, Linux terminal).\n'
      '  Benefits: (1) very fast for expert users; (2) uses very few system resources.\n'
      '• GUI (Graphical User Interface): the user interacts using windows, icons, menus and a pointer (e.g., Windows).\n'
      '  Benefits: (1) easy to learn and use — no need to memorise commands; (2) visually intuitive with icons and menus, which reduces errors.',
      'Modern operating systems use a GUI for everyday users but still provide a CLI for advanced tasks.',
      50),
    q('u2_exB_q4', C, 'B', 4, 'sq',
      'Which resources are managed by Resource Management function of OS?',
      'Resource Management of an OS manages the main resources of the computer:\n'
      '• Processor (CPU time),\n'
      '• Main memory (RAM),\n'
      '• Input/output devices, and\n'
      '• Storage / secondary memory devices.\n\n'
      'It performs the dynamic allocation and de-allocation of these resources so that every running program gets a fair share and the system works efficiently.',
      'Resource management prevents conflicts between programs that need the same device or memory at the same time.',
      50),
    q('u2_exB_q5', C, 'B', 5, 'sq',
      'What is the difference between single user and multi user OS? If you are a manager of a large organization which type of OS will you prefer? Justify your answer with any two reasons.',
      '• Single-user OS: designed for one user at a time (e.g., MS-DOS).\n'
      '• Multi-user OS: allows many users to access the computer and its resources simultaneously (e.g., Linux, UNIX, Windows Server).\n\n'
      'As a manager of a large organisation I would prefer a Multi-user OS because:\n'
      '1. Many employees can work on the same system/server at the same time, which saves cost and hardware.\n'
      '2. It provides better resource sharing, security and centralised management of users and data.',
      'Multi-user systems keep data and applications on one server, making administration and backups easier.',
      50),
    q('u2_exB_q6', C, 'B', 6, 'sq',
      'What is the purpose of office automation software? With examples, explain how can office automation help employees to be productive and efficient?',
      'Office automation software is a group of computer programs that help office workers perform their routine tasks easily, quickly and efficiently.\n\n'
      'Examples: MS Word (documents), MS Excel (spreadsheets), MS PowerPoint (presentations) and MS Outlook (email).\n\n'
      'How it helps: it lets employees produce professional documents, calculate and analyse data accurately, prepare presentations and communicate by email — reducing manual effort, time and errors, which increases productivity and efficiency.',
      'Office automation removes repetitive manual paperwork and speeds up everyday office work.',
      50),
    q('u2_exB_q7', C, 'B', 7, 'sq',
      'List the programs available in MS Office and write why each program is used?',
      '• MS Word — word processing: used for typing, formatting, editing and printing documents.\n'
      '• MS Excel — spreadsheet: used for calculations, formulas, charts and data analysis.\n'
      '• MS PowerPoint — presentation: used for making slide shows for lectures and meetings.\n'
      '• MS Access — database: used for storing and managing large amounts of structured data.\n'
      '• MS Outlook — email/personal information manager: used for sending mail and managing calendar and contacts.',
      'MS Office is a suite of office automation programs in which each program handles a particular type of office task.',
      50),
    q('u2_exB_q8', C, 'B', 8, 'sq',
      'What is the major difference between Soft Real Time and Hard Real Time systems?',
      'The major difference is the consequence of missing a deadline.\n'
      '• Hard Real Time system: a critical task must be completed within a strict deadline; missing it can cause severe damage or total failure (e.g., airbag, anti-lock brakes, pacemaker).\n'
      '• Soft Real Time system: occasional missed deadlines are tolerated, causing only degraded performance but no serious harm (e.g., video streaming, online ticket booking).',
      'Hard real time is used where timing is safety-critical; soft real time is used where a slight delay is acceptable.',
      50),
    q('u2_exB_q9', C, 'B', 9, 'sq',
      'Why it is important to install an antivirus?',
      'An antivirus is important because it:\n'
      '• detects, blocks and removes viruses, worms, Trojans and other malware;\n'
      '• prevents data loss and damage to the system;\n'
      '• scans files, emails and downloads before threats enter the computer;\n'
      '• protects personal and financial information from theft; and\n'
      '• keeps the computer running safely and efficiently.\n\n'
      'It must be updated regularly so that it can fight the latest threats.',
      'An antivirus is a utility program that acts as a security guard for the computer.',
      50),

    q('u2_exC_q1', C, 'C', 1, 'sq',
      'Match the columns: (i) CLI',
      '(f) Interface',
      'The Command Line Interface (CLI) is one type of user interface, through which the user interacts with the computer by typing commands.',
      51),
    q('u2_exC_q2', C, 'C', 2, 'sq',
      'Match the columns: (ii) Windows',
      '(d) Operating system',
      'Windows is a graphical multi-tasking operating system developed by Microsoft.',
      51),
    q('u2_exC_q3', C, 'C', 3, 'sq',
      'Match the columns: (iii) Process',
      '(e) A job to be performed by the system',
      'A process is a program (job) that is being executed by the system; process management controls these jobs.',
      51),
    q('u2_exC_q4', C, 'C', 4, 'sq',
      'Match the columns: (iv) Ms Excel',
      '(b) Office automation',
      'MS Excel is part of the office automation suite; it is used to prepare spreadsheets and perform calculations.',
      51),
    q('u2_exC_q5', C, 'C', 5, 'sq',
      'Match the columns: (v) Real time processing operating system',
      '(a) Time bound operating system',
      'A real time processing OS works within strict time limits (deadlines), so it is called a time-bound operating system.',
      51),
    q('u2_exC_q6', C, 'C', 6, 'sq',
      'Match the columns: (vi) Input / Output Management',
      '(c) Function of operating system',
      'Input/output management — controlling the flow of data to and from devices — is one of the main functions of the operating system.',
      51),

    q('u2_exD_q1', C, 'D', 1, 'sq',
      'Teacher should demonstrate installation process of: Windows Operating System, Microsoft Office and any free antivirus software.',
      'General installation steps (same for all three programs):\n'
      '1. Insert the installation DVD or run the downloaded setup/ISO file.\n'
      '2. If a licence/key is required, enter the product key.\n'
      '3. Accept the licence agreement.\n'
      '4. Choose the installation type (e.g., "Custom" for Windows) and select the drive/partition.\n'
      '5. Follow the on-screen instructions and wait while files are copied.\n'
      '6. Restart the computer if asked, then activate the product and install updates.',
      'Installing an OS replaces/loads the system software; Office and antivirus are application/utility programs installed on top of the OS.',
      51),
    q('u2_exD_q2', C, 'D', 2, 'sq',
      'Students should be given task to make use of antivirus software.',
      'Steps to use an antivirus:\n'
      '1. Open the antivirus program from the desktop or Start Menu.\n'
      '2. Update it (download the latest virus definitions) so it recognises new threats.\n'
      '3. Select a scan type — Quick scan (common areas) or Full scan (entire computer).\n'
      '4. Start the scan and wait for it to finish.\n'
      '5. If any threat is found, choose "Quarantine" or "Remove/Delete" as suggested.\n'
      '6. Review the scan report and enable real-time (automatic) protection.',
      'Regular scanning and updating keep the computer protected from the latest malware.',
      51),
    q('u2_exD_q3', C, 'D', 3, 'sq',
      'Student should observe and work with different icons on Windows Desktop, Start Menu and Utility Programs available.',
      'Task: explore the Windows environment.\n'
      '• Desktop icons: Recycle Bin, This PC, folders/shortcuts. Practise opening, selecting and arranging them.\n'
      '• Start Menu: click the Start button and note the program list, search box and power options.\n'
      '• Utility programs: open and practise with Disk Cleanup, Disk Defragmenter, Calculator, Notepad, Paint and the Control Panel settings.',
      'Utility programs are small system programs that help maintain and manage the computer.',
      51),
    q('u2_exD_q4', C, 'D', 4, 'sq',
      'Student should also practice creating, copying, moving and deleting files and folders.',
      'Steps:\n'
      '• Creating: right-click on the desktop/a folder → New → Folder (or New → Text Document) and give it a name.\n'
      '• Copying: select the file/folder → Ctrl+C, open the destination → Ctrl+V (the original remains).\n'
      '• Moving: select → Ctrl+X, open the destination → Ctrl+V (the original is removed).\n'
      '• Deleting: select → Delete key (moves to Recycle Bin) or Shift+Delete (permanent).\n'
      '• Renaming: select → F2 and type the new name.',
      'Practising these operations teaches file management, a key function of the operating system.',
      51),
    q('u2_exD_q5', C, 'D', 5, 'sq',
      'Teacher should also demonstrate the Task Manager for explaining Task Management concept.',
      'Demonstration: press Ctrl+Shift+Esc (or Ctrl+Alt+Delete → Task Manager) to open it.\n'
      '• Processes tab: shows all running programs/processes with their CPU, memory and disk usage.\n'
      '• Performance tab: shows overall CPU, memory, disk and network usage.\n'
      '• Applications tab: lists open applications; a program can be ended with "End task".\n'
      'This shows how the OS manages (starts, schedules and stops) many tasks at the same time.',
      'Task Manager is a utility that lets you see and control the processes running on the computer.',
      51),
    q('u2_exD_q6', C, 'D', 6, 'sq',
      'Teacher should also demonstrate the BIOS screen.',
      'Demonstration: restart the computer and press the setup key (usually Del, F2 or F10) during start-up to enter the BIOS/UEFI screen.\n'
      'In BIOS you can:\n'
      '• view system information (processor, memory);\n'
      '• set the date and time;\n'
      '• change the boot order (which device to start from);\n'
      '• enable/disable hardware devices and set passwords.\n'
      'Save the changes with F10 and exit.',
      'BIOS (Basic Input Output System) is firmware that starts the hardware and loads the operating system during booting.',
      51),
]


# ============================================================================
# UNIT 3 — Office Automation   PDF pages 52-70
# A = MCQs (PDF 65-66), B = Short Qs (PDF 66-67), C = Match (PDF 67), D = Activities (PDF 67-70)
# ============================================================================

C = 3
SOLVED += [
    q('u3_exA_q1', C, S, 1, 'mcq',
      'Which chart will be suitable to show the share of three partners in a business?',
      '(d) pie chart',
      'A pie chart shows each part as a slice of a whole circle, so it is ideal for showing the share (percentage) of each partner in a business.',
      65,
      [('a', 'line chart'), ('b', 'bar chart'), ('c', 'area chart'), ('d', 'pie chart')], '(d)'),
    q('u3_exA_q2', C, S, 2, 'mcq',
      'The software that is used for accounting purpose is:',
      '(b) MS Excel',
      'MS Excel is spreadsheet software with formulas and functions, which makes it suitable for accounting, calculations and financial records.',
      65,
      [('a', 'MS Word'), ('b', 'MS Excel'), ('c', 'MS Power point'), ('d', 'MS Access')], '(b)'),
    q('u3_exA_q3', C, S, 3, 'mcq',
      'The software that is used to format a document is:',
      '(a) MS Word',
      'MS Word is a word processor used to create and format text documents (fonts, alignment, styles, margins, headers, etc.).',
      65,
      [('a', 'MS Word'), ('b', 'MS Excel'), ('c', 'MS Power point'), ('d', 'MS Access')], '(a)'),
    q('u3_exA_q4', C, S, 4, 'mcq',
      'The special character that initiates the formula mode in a cell is:',
      '(b) =',
      'In MS Excel, typing the equals sign (=) at the start of a cell entry tells Excel that a formula follows (e.g., =A1+B1).',
      65,
      [('a', '/'), ('b', '='), ('c', '-'), ('d', '*')], '(b)'),
    q('u3_exA_q5', C, S, 5, 'mcq',
      'The function which is used to re-arrange data according to specific criteria is called:',
      '(b) Sorting',
      'Sorting arranges data in ascending or descending order according to a chosen criterion (e.g., names alphabetically or marks from high to low). Filtering only displays the rows that meet a condition.',
      65,
      [('a', 'Filtering'), ('b', 'Sorting'), ('c', 'Organizing'), ('d', 'Grouping')], '(b)'),
    q('u3_exA_q6', C, S, 6, 'mcq',
      'If we want to change the overall design of a word document, we should use:',
      '(a) themes',
      'A theme is a set of unified colours, fonts and effects that changes the overall look/design of the whole document in one step.',
      65,
      [('a', 'themes'), ('b', 'page layout'), ('c', 'watermark'), ('d', 'margins')], '(a)'),
    q('u3_exA_q7', C, S, 7, 'mcq',
      'The correct formula to calculate the total in the given table is:',
      '(a) = B2 + C2 + D2 + E2',
      'To add the four values in a row, the cells B2, C2, D2 and E2 are added together with a plus sign. (=SUM(B2:E2) would also work, but none of the SUM options given uses the correct syntax.)',
      66,
      [('a', '= B2 + C2 + D2 + E2'), ('b', '= B2 + E2'),
       ('c', '= sum (B2 to E2)'), ('d', '= sum (B2 from E2)')], '(a)'),
    q('u3_exA_q8', C, S, 8, 'mcq',
      'The correct formula to calculate the percentage in the given table is:',
      '(c) =(B2 + C2 + D2 + E2) / 400 * 100',
      'The total marks are found by adding the four cells, then dividing by the maximum total (400) and multiplying by 100 to get the percentage. Brackets are needed so that the addition is done before the division.',
      66,
      [('a', '=B2 + C2 + D2 + E2 / 400 * 100'), ('b', '=B2 + C2 + D2 + E2 * 100'),
       ('c', '=(B2 + C2 + D2 + E2) / 400 * 100'), ('d', '=(B2 + C2 + D2 + E2) / 100 * 400')], '(c)'),
    q('u3_exA_q9', C, S, 9, 'mcq',
      'Charts are basically used to:',
      '(d) show the quantities and their relationships graphically',
      'A chart presents numerical data as bars, lines, slices or columns so that quantities and the relationships between them can be understood quickly and visually.',
      66,
      [('a', 'design tables'), ('b', 'organize data in tables'),
       ('c', 'Sort data in different columns'), ('d', 'show the quantities and their relationships graphically')], '(d)'),
    q('u3_exA_q10', C, S, 10, 'mcq',
      'To apply the table of contents automatically, the most important task is to properly define the:',
      '(a) levels of heading',
      'An automatic Table of Contents is built from the document\'s headings. If the heading levels (Heading 1, Heading 2, …) are applied correctly, Word can gather them and create the ToC automatically.',
      66,
      [('a', 'levels of heading'), ('b', 'page numbering'),
       ('c', 'page layout'), ('d', 'themes')], '(a)'),

    q('u3_exB_q1', C, 'B', 1, 'sq',
      'What is a word processor? Write any three applications of a word processor.',
      'A word processor is application software used to create, edit, format, save and print text documents.\n\n'
      'Three applications:\n'
      '1. Creating and formatting documents such as letters, reports and assignments.\n'
      '2. Inserting tables, pictures, charts and page decorations (watermarks, borders, page colour).\n'
      '3. Writing and printing mail-merge letters, résumés and newsletters.',
      'MS Word is the most widely used word processor.',
      66),
    q('u3_exB_q2', C, 'B', 2, 'sq',
      'Discuss the Margins and Paper Size options in the Page Setup group.',
      '• Margins: the blank space left between the text and the edges of the page (top, bottom, left, right). Margins make the document look neat and leave room for binding. Preset options are Normal, Narrow, Moderate, Wide and Custom Margins.\n'
      '• Paper Size: this option selects the size of the page/paper, e.g., A4, A3, A5, Letter and Legal. Choosing the correct size ensures that the document prints properly on the available paper.',
      'Both options are found in the Page Setup group of the Layout (Page Layout) tab and affect how the page looks when printed.',
      66),
    q('u3_exB_q3', C, 'B', 3, 'sq',
      'Name and describe two options in Orientation.',
      'The two orientation options are:\n'
      '• Portrait — the page is taller than it is wide (height > width); used for ordinary letters, reports and books.\n'
      '• Landscape — the page is wider than it is tall (width > height); used for wide tables, charts, certificates and posters.',
      'Orientation is set from the Page Setup group and can also be changed for a single section using a section break.',
      66),
    q('u3_exB_q4', C, 'B', 4, 'sq',
      'How can we apply Margins in a document?',
      'Steps:\n'
      '1. Open the document in MS Word.\n'
      '2. Go to the Layout (Page Layout) tab.\n'
      '3. In the Page Setup group, click Margins.\n'
      '4. Choose a preset margin (Normal, Narrow, Moderate, Wide) or click Custom Margins.\n'
      '5. In the dialog box, type the required Top, Bottom, Left and Right values and click OK.\n'
      'The new margins are applied to the document.',
      'Margins can be applied to the whole document or, after inserting a section break, only to a particular section.',
      66),
    q('u3_exB_q5', C, 'B', 5, 'sq',
      'Describe the different types of breaks in MS Word.',
      'MS Word provides two groups of breaks:\n\n'
      'Page Breaks:\n'
      '• Page — moves the text after the break to the next page.\n'
      '• Column — moves the text to the next column.\n'
      '• Text Wrapping — forces the surrounding text to wrap around an object.\n\n'
      'Section Breaks:\n'
      '• Next Page — starts a new section on the next page.\n'
      '• Continuous — starts a new section on the same page.\n'
      '• Even Page / Odd Page — starts the new section on the next even/odd page.\n\n'
      'Section breaks are used to change page layout, orientation, columns or headers/footers for part of a document.',
      'Breaks are inserted from the Layout tab → Breaks.',
      67),
    q('u3_exB_q6', C, 'B', 6, 'sq',
      'Differentiate "Bring Forward" and "Send Backward" options in the Arrange group with example.',
      'These options change the stacking order of overlapping objects:\n'
      '• Bring Forward — moves the selected object one step up (closer to the front) so that it comes in front of the object behind it.\n'
      '• Send Backward — moves the selected object one step down (behind) so that the other object comes in front.\n\n'
      'Example: if a picture and a shape overlap, selecting the picture and clicking Bring Forward puts the picture in front of the shape; clicking Send Backward puts the shape back in front.',
      'The Arrange group also contains "Bring to Front" and "Send to Back" to move an object all the way to the front or back.',
      67),
    q('u3_exB_q7', C, 'B', 7, 'sq',
      'Explain the "Columns" option in the Page Setup group.',
      'The Columns option divides the text of a page into more than one vertical column, like a newspaper.\n\n'
      'Steps: Layout → Page Setup → Columns → choose One, Two, Three, Left or Right, or click More Columns to set the number, width and spacing of the columns.\n\n'
      'It is useful for newsletters, brochures and leaflets where text flows from the bottom of one column to the top of the next.',
      'The number and spacing of columns can be changed for the whole document or only for a section.',
      67),
    q('u3_exB_q8', C, 'B', 8, 'sq',
      'List and define Position and Wrap Text option in Arrange Group.',
      '• Position: places a selected object (picture/shape) at a chosen location relative to the page, margin, paragraph or line. It offers preset positions (e.g., top-left with square wrapping, middle centre) and More Layout Options for exact coordinates.\n'
      '• Wrap Text: controls how the surrounding text flows around an object. Options are In Line with Text, Square, Tight, Through, Top and Bottom, Behind Text and In Front of Text.',
      'Both options are in the Arrange group of the Format tab and are used when working with pictures, shapes and text boxes.',
      67),
    q('u3_exB_q9', C, 'B', 9, 'sq',
      'In what way does a ToC help book reader?',
      'A Table of Contents (ToC) lists the headings/chapters of a document together with their page numbers. It helps the reader to:\n'
      '• quickly locate and jump to a particular section or chapter;\n'
      '• see the overall structure and organisation of the document at a glance;\n'
      '• navigate directly to the required page (when the ToC entries are hyperlinks) without scrolling through the whole document.',
      'An automatic ToC is created from the document\'s heading levels and can be updated with a single click.',
      67),
    q('u3_exB_q10', C, 'B', 10, 'sq',
      'Write steps that will multiply 37 by 15 using the formula bar in MS Excel.',
      'Steps:\n'
      '1. Click on a cell, say A1.\n'
      '2. Click in the formula bar and type the formula =37*15.\n'
      '3. Press Enter.\n'
      '4. Excel displays the result 555 in cell A1.\n\n'
      'Alternative: type 37 in cell A1 and 15 in cell B1, then in cell C1 type =A1*B1 and press Enter.',
      'The formula bar always begins with "=" and shows the formula of the active cell so it can be edited easily.',
      67),
    q('u3_exB_q11', C, 'B', 11, 'sq',
      'Why do we use Watermark in a document? Give some examples of Watermarks.',
      'A watermark is a faint, semi-transparent text or image that appears behind the main text of a document. It is used to:\n'
      '• identify or authenticate a document;\n'
      '• show its status or purpose;\n'
      '• display a company logo or name; and\n'
      '• discourage unauthorised copying.\n\n'
      'Examples: "CONFIDENTIAL", "DRAFT", "SAMPLE", "COPY", "BEST COPY", or a company logo.',
      'A watermark is inserted from Design → Watermark and can be a preset, custom text or a picture.',
      67),
    q('u3_exB_q12', C, 'B', 12, 'sq',
      'List four uses of spreadsheets in business.',
      'Spreadsheets are used in business for:\n'
      '1. Accounting and bookkeeping (ledgers, balance sheets, income statements).\n'
      '2. Preparing payroll and salary sheets.\n'
      '3. Budgeting, forecasting and financial planning.\n'
      '4. Inventory/stock management, invoicing and billing (and analysing sales data with charts).',
      'Formulas and functions in spreadsheets make calculations fast and let results update automatically when data changes.',
      67),

    q('u3_exC_q1', C, 'C', 1, 'sq',
      'Match the columns: (i) Wrap Text',
      '(b) allows to arrange text around an image',
      'The Wrap Text option makes the surrounding text flow around a picture or shape instead of overlapping it.',
      67),
    q('u3_exC_q2', C, 'C', 2, 'sq',
      'Match the columns: (ii) Automatic Table of Contents',
      '(d) is created based on heading',
      'An automatic ToC is generated by Word from the heading levels used in the document.',
      67),
    q('u3_exC_q3', C, 'C', 3, 'sq',
      'Match the columns: (iii) Page Setup Group sets',
      '(e) margins, orientation and size',
      'The Page Setup group contains the Margins, Orientation, Size and Columns options that control the page layout.',
      67),
    q('u3_exC_q4', C, 'C', 4, 'sq',
      'Match the columns: (iv) Excel is used to',
      '(f) organize, display, format and calculate data',
      'MS Excel is spreadsheet software used to organize, display, format and calculate numerical data using formulas and charts.',
      67),
    q('u3_exC_q5', C, 'C', 5, 'sq',
      'Match the columns: (v) Charts',
      '(c) Show data graphically',
      'Charts present data graphically (as bars, lines, pie slices, etc.) so that it is easy to compare and understand.',
      67),
    q('u3_exC_q6', C, 'C', 6, 'sq',
      'Match the columns: (vi) Ms Word is widely used for',
      '(a) documentation',
      'MS Word is the most widely used word processor for preparing all kinds of documents (documentation).',
      67),

    q('u3_exD_q1', C, 'D', 1, 'sq',
      'Compose a document in MS Word and apply Watermark, Page Color and Page Border.',
      'Steps:\n'
      '1. Open MS Word and type the text of the document.\n'
      '2. Watermark: Design → Watermark → choose a preset (e.g., DRAFT/CONFIDENTIAL) or Custom Watermark to add your own text/picture.\n'
      '3. Page Color: Design → Page Color → choose a colour from the palette.\n'
      '4. Page Border: Design → Page Borders → in the Borders and Shading dialog select the border style, colour, width and apply to the whole document → OK.',
      'These options are all on the Design tab and change the appearance of the whole page.',
      68),
    q('u3_exD_q2', C, 'D', 2, 'sq',
      'Apply different options of Margins, Orientation, Size and Columns in a document.',
      'Steps:\n'
      '• Margins: Layout → Page Setup → Margins → choose Normal/Narrow/Wide or Custom Margins.\n'
      '• Orientation: Layout → Page Setup → Orientation → choose Portrait or Landscape.\n'
      '• Size: Layout → Page Setup → Size → choose A4, A3, Letter, etc.\n'
      '• Columns: Layout → Page Setup → Columns → choose One, Two, Three or More Columns.',
      'Practising these options shows how the overall page layout of a document can be changed.',
      68),
    q('u3_exD_q3', C, 'D', 3, 'sq',
      'Add 15 Names and 15 Marks Obtained in two columns and apply different sorting options in MS Excel.',
      'Steps:\n'
      '1. In cell A1 type "Name" and in B1 type "Marks Obtained".\n'
      '2. Enter 15 names in A2:A16 and their marks in B2:B16.\n'
      '3. Select the data range (including the headings).\n'
      '4. Data tab → Sort → sort by "Marks Obtained" Largest to Smallest (or Smallest to Largest), or sort by "Name" A to Z / Z to A.\n'
      '5. Use Data → Sort → Add Level to sort by more than one column at a time.\n'
      'Observe how the rows rearrange according to the chosen criterion.',
      'Sorting arranges the data in order; always include the heading row so Excel keeps the headings with the data.',
      68),
    q('u3_exD_q4', C, 'D', 4, 'sq',
      'Type the given text in MS Word using Urdu or Sindhi language facility.',
      'Steps:\n'
      '1. Open MS Word and enable the Urdu/Sindhi keyboard from Windows: Settings → Time & Language → Language → Add a language → Urdu/Sindhi.\n'
      '2. Switch the keyboard layout to Urdu/Sindhi (using the language bar or Windows key + Space).\n'
      '3. In Word, choose an Urdu/Sindhi font (e.g., Jameel Noori Nastaleeq for Urdu) and set the text direction to Right-to-Left.\n'
      '4. Type the given passage following the correct right-to-left order.\n'
      '5. Save the document.',
      'For South-Asian scripts, using an appropriate font and RTL direction is important for correct display.',
      69),
    q('u3_exD_q5', C, 'D', 5, 'sq',
      'Using the given pie chart (a batsman\'s 149 runs), prepare an Excel sheet to calculate: (a) how many runs came from ones, twos, fours and sixes, (b) the strike rate of the player, and (c) prepare a pie chart of the shares.',
      'Data taken from the given chart: ones = 21 balls scoring 1 each, twos = 7 balls, fours = 14 balls, sixes = 9 balls; total runs = 149; balls faced (BF) = 64.\n\n'
      'Steps in Excel:\n'
      '1. Create columns: Type (1s/2s/4s/6s), Balls, Runs = Balls × value.\n'
      '  • 1s: 21 balls × 1 = 21 runs\n'
      '  • 2s: 7 balls × 2 = 14 runs\n'
      '  • 4s: 14 balls × 4 = 56 runs\n'
      '  • 6s: 9 balls × 6 = 54 runs\n'
      '  Total = 21 + 14 + 56 + 54 = 145 runs (the chart also mentions other scoring).\n'
      '2. Strike rate = (Total runs / Balls faced) × 100 = (149 / 64) × 100 ≈ 232.8.\n'
      '3. Select the Runs column → Insert → Pie Chart to show the share of each type of scoring.',
      'A spreadsheet makes it easy to calculate totals and percentages and to draw a pie chart from the results.',
      69),
    q('u3_exD_q6', C, 'D', 6, 'sq',
      'Create a newsletter in MS Word with a header, three columns and some graphics with text wrapped around them.',
      'Steps:\n'
      '1. Insert → Header → type the newsletter title/heading in the header area.\n'
      '2. Layout → Columns → Three to divide the page into three columns.\n'
      '3. Insert → Pictures/Shapes to add graphics.\n'
      '4. Select a graphic → Layout Options (or Format → Wrap Text) → choose Square/Tight wrapping so the text flows around it.\n'
      '5. Format the text with headings, bullets and borders to give a professional newsletter look.',
      'A newsletter combines a header, multiple columns and wrapped images to present information attractively.',
      69),
    q('u3_exD_q7', C, 'D', 7, 'sq',
      'Create a spreadsheet of employees\' payroll in MS Excel (Emp ID, Emp Name, Dept, Basic Pay, Medical Allowance, Conveyance Allowance, House Rent, Gross Salary, Income Tax, Net Salary).',
      'Calculation rules given in the book:\n'
      '• Medical Allowance (MA) = 15% of Basic Salary → =B2*15%\n'
      '• Conveyance Allowance (CA) = 22.5% of Basic Salary → =B2*22.5%\n'
      '• House Rent (HR) = 40% of Basic Salary → =B2*40%\n'
      '• Gross Salary = Basic Pay + MA + CA + HR → =B2+C2+D2+E2\n'
      '• Income Tax = 7.5% of Gross Salary → =F2*7.5%\n'
      '• Net Salary = Gross Salary − Income Tax → =F2−G2\n\n'
      'Steps: enter the headings in row 1, fill the Emp ID, Name, Dept and Basic Pay, then type the formulas in the first data row and copy them down using the fill handle so that all other rows are calculated automatically.',
      'Using cell references (instead of typed numbers) makes the whole sheet update automatically when the Basic Pay changes.',
      69),
]


# ============================================================================
# UNIT 4 — Data Communication and Computer Networks   PDF pages 71-100
# A = MCQs (PDF 98-99), B = Short Qs (PDF 99), C = Match (PDF 100), D = Activities (PDF 100)
# ============================================================================

C = 4
SOLVED += [
    q('u4_exA_q1', C, S, 1, 'mcq',
      'Wired Media is also called:',
      '(c) guided media',
      'Wired (guided) media, such as twisted pair, coaxial and fibre-optic cable, guides the signal along a physical path. Wireless media are called unguided media.',
      98,
      [('a', 'targeted media'), ('b', 'directed media'), ('c', 'guided media'), ('d', 'unguided media')], '(c)'),
    q('u4_exA_q2', C, S, 2, 'mcq',
      'Communication system is made up of:',
      '(c) five components',
      'A communication system has five components: message, sender, receiver, transmission medium and protocol.',
      98,
      [('a', 'three components'), ('b', 'four components'), ('c', 'five components'), ('d', 'six components')], '(c)'),
    q('u4_exA_q3', C, S, 3, 'mcq',
      'Both Physical and Logical addresses are:',
      '(b) unique',
      'A physical address (MAC address) and a logical address (IP address) are both unique — each device on a network has its own distinct addresses.',
      98,
      [('a', 'different'), ('b', 'unique'), ('c', 'permanent'), ('d', 'temporary')], '(b)'),
    q('u4_exA_q4', C, S, 4, 'mcq',
      'If you are an electrical or electronic engineer, you should join:',
      '(a) IEEE',
      'The IEEE (Institute of Electrical and Electronics Engineers) is the professional organisation and standards body for electrical and electronic/computer engineers.',
      98,
      [('a', 'IEEE'), ('b', 'IETF'), ('c', 'ITU'), ('d', 'ANSI')], '(a)'),
    q('u4_exA_q5', C, S, 5, 'mcq',
      'The topology in which all computers are connected to a central device called hub is:',
      '(b) Star',
      'In a star topology every computer is connected by its own cable to a central device (hub/switch), forming a star shape.',
      98,
      [('a', 'Bus'), ('b', 'Star'), ('c', 'Ring'), ('d', 'Tree')], '(b)'),
    q('u4_exA_q6', C, S, 6, 'mcq',
      'Change in the shape of signal between sender and receiver is called:',
      '(d) distortion',
      'Distortion is the change in the shape (waveform) of a signal as it travels through the medium, caused by different components of the signal travelling at different speeds.',
      98,
      [('a', 'attenuation'), ('b', 'interruption'), ('c', 'noise'), ('d', 'distortion')], '(d)'),
    q('u4_exA_q7', C, S, 7, 'mcq',
      'Router determines data path to transfer data packets which is the:',
      '(d) optimal',
      'A router chooses the best (optimal) path for data packets, considering factors such as the shortest and least-congested route to the destination.',
      98,
      [('a', 'shortest'), ('b', 'longest'), ('c', 'cheapest'), ('d', 'optimal')], '(d)'),
    q('u4_exA_q8', C, S, 8, 'mcq',
      'Converting digital signal to analog is called:',
      '(a) modulation',
      'Modulation converts a digital signal into an analog signal (and the reverse is demodulation); a modem performs both, which is why it is called MODEM (MOdulator-DEModulator).',
      99,
      [('a', 'modulation'), ('b', 'modification'), ('c', 'bandwidth'), ('d', 'multiplexing')], '(a)'),
    q('u4_exA_q9', C, S, 9, 'mcq',
      'The number of bits used in an IPV 4 address are:',
      '(b) 32',
      'An IPv4 address is a 32-bit address, usually written as four decimal numbers (octets) separated by dots, e.g., 192.168.1.1.',
      99,
      [('a', '16'), ('b', '32'), ('c', '64'), ('d', '128')], '(b)'),
    q('u4_exA_q10', C, S, 10, 'mcq',
      'The loss of energy in transmission signal refers to:',
      '(a) Attenuation',
      'Attenuation is the loss of signal energy (strength) as the signal travels, becoming weaker over distance; it is corrected using amplifiers or repeaters.',
      99,
      [('a', 'Attenuation'), ('b', 'Distortion'), ('c', 'Noise'), ('d', 'Jitter')], '(a)'),

    q('u4_exB_q1', C, 'B', 1, 'sq',
      'List the properties of a good communication system. Explain any one.',
      'Properties of a good communication system:\n'
      '1. Delivery — data must reach the correct destination and user.\n'
      '2. Accuracy — data must be delivered without errors.\n'
      '3. Reliability — the system must work consistently.\n'
      '4. Timeliness — data must arrive on time.\n'
      '5. Jitter control — variation in delay must be kept within limits.\n\n'
      '• Accuracy: the system must deliver the data exactly as it was sent. If the received data differs from the sent data (because of noise, distortion or attenuation), the communication is inaccurate and the information becomes useless or dangerous.',
      'These properties are the basic requirements of effective data communication.',
      99),
    q('u4_exB_q2', C, 'B', 2, 'sq',
      'Explain components of communication using single example.',
      'A communication system has five components: message, sender, receiver, transmission medium and protocol.\n\n'
      'Example — sending an email:\n'
      '• Message: the text of the email.\n'
      '• Sender: the person who writes and sends the email.\n'
      '• Receiver: the person who receives the email.\n'
      '• Transmission medium: the Internet (cables and network equipment).\n'
      '• Protocol: SMTP, the set of rules that governs how the email is sent.',
      'All five components must be present for any data communication to take place.',
      99),
    q('u4_exB_q3', C, 'B', 3, 'sq',
      'Write the function of following network devices: Amplifiers, Routers, Switch, Hub.',
      '• Amplifier: strengthens (amplifies) a weak signal so that it can travel a longer distance without losing strength.\n'
      '• Router: connects different networks and finds the best (optimal) path to forward data packets to their destination.\n'
      '• Switch: connects multiple devices in a LAN and sends data only to the intended device (it is intelligent and uses MAC addresses).\n'
      '• Hub: a simple device that connects several devices and broadcasts data to all of them (it is non-intelligent).',
      'A hub broadcasts to everyone while a switch sends data only to the correct device, which makes a switch more efficient.',
      99),
    q('u4_exB_q4', C, 'B', 4, 'sq',
      'List the causes of signal impairments. Explain any one.',
      'Causes of signal impairment:\n'
      '1. Attenuation — loss of signal strength.\n'
      '2. Distortion — change in the shape of the signal.\n'
      '3. Noise — unwanted energy added to the signal.\n\n'
      '• Attenuation: as a signal travels through the medium it gradually loses energy and becomes weak. This is why signals cannot travel unlimited distances and must be boosted using amplifiers or repeaters.',
      'Impairment reduces the quality and accuracy of the received signal.',
      99),
    q('u4_exB_q5', C, 'B', 5, 'sq',
      'What is the difference between radio wave and microwave?',
      '• Radio waves: lower-frequency electromagnetic waves; omni-directional (spread out in all directions); can pass through walls and buildings; used for AM/FM radio, TV and mobile communication.\n'
      '• Microwaves: higher-frequency electromagnetic waves; unidirectional (require a line-of-sight path); cannot penetrate solid obstacles; used for satellite links, Wi-Fi and radar.',
      'Because microwaves need a clear line of sight, microwave towers and satellite dishes must be placed high and aligned.',
      99),
    q('u4_exB_q6', C, 'B', 6, 'sq',
      'Why OSI model is broken up in layers?',
      'The OSI model is divided into layers so that a complex networking task is broken into smaller, manageable parts. Each layer performs a specific, well-defined function and communicates with the layers above and below through standard interfaces.\n\n'
      'Benefits: simpler design; easy troubleshooting and modification of one layer without affecting the others; interoperability between products from different manufacturers; and easier standardisation and learning.',
      'The seven OSI layers are Physical, Data Link, Network, Transport, Session, Presentation and Application.',
      99),
    q('u4_exB_q7', C, 'B', 7, 'sq',
      'Explain the purpose of Standard Organization.',
      'Standard organisations develop and publish common rules, formats and protocols for networking and communication so that hardware and software from different manufacturers can work together (interoperability).\n\n'
      'Examples: IEEE, IETF, ITU and ANSI. Their standards ensure compatibility, reliability and worldwide communication.',
      'Without standards, devices from different companies could not communicate with each other.',
      99),
    q('u4_exB_q8', C, 'B', 8, 'sq',
      'List one merit and one demerit of each topology.',
      '• Bus: merit — simple and cheap to install; demerit — if the main backbone cable breaks, the whole network fails.\n'
      '• Star: merit — easy to add/remove devices and one fault affects only one device; demerit — needs more cable and a central hub/switch, and if the hub fails the whole network stops.\n'
      '• Ring: merit — no collisions, data moves in an orderly way; demerit — failure of one node or cable can break the whole ring.\n'
      '• Tree: merit — easy to expand into hierarchical groups; demerit — complex, and failure of the backbone/root affects large parts of the network.',
      'The choice of topology depends on cost, size and reliability requirements of the network.',
      99),
    q('u4_exB_q9', C, 'B', 9, 'sq',
      'Give one example of LAN, WAN and MAN.',
      '• LAN (Local Area Network): a network within a school computer lab or an office building.\n'
      '• MAN (Metropolitan Area Network): a city-wide network, such as a cable-TV network or a network linking several offices across a city.\n'
      '• WAN (Wide Area Network): the Internet, or a bank\'s network connecting its branches all over the country (or across continents).',
      'LAN < MAN < WAN in terms of geographical area covered.',
      99),
    q('u4_exB_q10', C, 'B', 10, 'sq',
      'How can we measure bit rate and baud rate? Give an example of each.',
      '• Bit rate: the number of bits transmitted per second, measured in bits per second (bps).\n'
      '• Baud rate: the number of signal units (symbols) transmitted per second.\n'
      'Relationship: Bit rate = Baud rate × number of bits per signal unit.\n\n'
      'Example: if a line transmits 2400 symbols per second and each symbol carries 1 bit, both the baud rate and the bit rate are 2400. If each symbol carries 4 bits at 1000 symbols/second, the baud rate is 1000 baud and the bit rate is 4000 bps.',
      'Bit rate measures the actual data speed, while baud rate measures how fast the signal changes.',
      99),

    q('u4_exC_q1', C, 'C', 1, 'sq',
      'Match the columns: (i) Parts of an IPV4 address',
      '(b) Network and Host',
      'An IPv4 address has two parts: the network part (which identifies the network) and the host part (which identifies the device on that network).',
      100),
    q('u4_exC_q2', C, 'C', 2, 'sq',
      'Match the columns: (ii) Physical address',
      '(e) Cannot be changed',
      'The physical address (MAC address) is fixed by the manufacturer in the network card and cannot be changed, unlike a logical (IP) address.',
      100),
    q('u4_exC_q3', C, 'C', 3, 'sq',
      'Match the columns: (iii) Change in shape of signals',
      '(f) Distortion',
      'Distortion is the change in the shape (waveform) of a signal as it passes through the transmission medium.',
      100),
    q('u4_exC_q4', C, 'C', 4, 'sq',
      'Match the columns: (iv) A networking connecting two continents',
      '(a) WAN',
      'A Wide Area Network (WAN) spans a very large geographical area, even connecting different continents (e.g., the Internet).',
      100),
    q('u4_exC_q5', C, 'C', 5, 'sq',
      'Match the columns: (v) TCP and UDP are used at',
      '(c) Transport layer',
      'TCP and UDP are transport-layer protocols of the OSI model that provide end-to-end data delivery.',
      100),
    q('u4_exC_q6', C, 'C', 6, 'sq',
      'Match the columns: (vi) In OSI model the layer responsible to decide the format of data',
      '(d) Data link layer',
      'The data link layer organises the bits into frames and decides the format of the data being transferred (framing, physical addressing and error control).',
      100),

    q('u4_exD_q1', C, 'D', 1, 'sq',
      'APSTNDP are the first characters of OSI Model\'s Layers. Make a sentence of seven words where each word starts with each character.',
      'The seven OSI layers are: Application, Presentation, Session, Transport, Network, Data Link, Physical → A-P-S-T-N-D-P.\n\n'
      'A sample sentence (each word starting with A P S T N D P):\n'
      '"All People Seem To Need Data Processing."',
      'This mnemonic is a memory aid to remember the order of the OSI layers from top to bottom.',
      100),
    q('u4_exD_q2', C, 'D', 2, 'sq',
      'Compare Coaxial Cable, UTP, STP and Fiber Optic cable in terms of cost, data rate, installation, interference and maximum length of segment.',
      'Comparison:\n'
      '• Coaxial cable — Cost: moderate; Data rate: moderate; Installation: fairly easy; Interference: moderate (shielding helps); Max length: longer than twisted pair (hundreds of metres).\n'
      '• UTP (Unshielded Twisted Pair) — Cost: lowest; Data rate: low–moderate; Installation: easiest; Interference: high (no shielding); Max length: about 100 m.\n'
      '• STP (Shielded Twisted Pair) — Cost: higher than UTP; Data rate: moderate; Installation: harder (shielding); Interference: low (shielded); Max length: about 100 m.\n'
      '• Fiber Optic — Cost: highest; Data rate: very high; Installation: difficult (needs skilled work); Interference: none (immune to EMI); Max length: very long (kilometres).',
      'Fibre optic gives the best speed and immunity but costs the most; UTP is the cheapest but shortest in range.',
      100),
    q('u4_exD_q3', C, 'D', 3, 'sq',
      'Uncover the twisted pair cable, count number of wires and also make list of color scheme.',
      'Task: carefully strip the outer jacket of a twisted pair (UTP) cable.\n'
      '• Number of wires: an Ethernet UTP cable contains 8 wires arranged as 4 twisted pairs.\n'
      '• Colour scheme (T568B standard):\n'
      '  1. Orange/White  2. Orange  3. Green/White  4. Blue\n'
      '  5. Blue/White    6. Green   7. Brown/White  8. Brown',
      'Twisting the pairs reduces electromagnetic interference and cross-talk.',
      100),
    q('u4_exD_q4', C, 'D', 4, 'sq',
      'Identify different type of layers of coaxial cable.',
      'A coaxial cable has four layers (from inside to outside):\n'
      '1. Inner conductor — a copper wire that carries the signal.\n'
      '2. Insulation (dielectric) — separates the inner conductor from the shield.\n'
      '3. Metallic shield (braided mesh/foil) — protects the signal from interference and forms the outer conductor.\n'
      '4. Outer jacket — a plastic covering that protects the whole cable.',
      'The shielding of a coaxial cable makes it less prone to interference than twisted pair cable.',
      100),
    q('u4_exD_q5', C, 'D', 5, 'sq',
      'Identify and write names of different connectors used in telephone landline, coaxial cable and twisted pair cable.',
      '• Telephone landline — RJ-11 connector (has 6 positions, usually 2–4 wires).\n'
      '• Coaxial cable — BNC connector (also F-type/coaxial connectors) used with TV and network coaxial cables.\n'
      '• Twisted pair cable — RJ-45 connector (8 positions, used for Ethernet LAN cables).',
      'RJ stands for Registered Jack; RJ-11 and RJ-45 look similar but RJ-45 is wider.',
      100),
    q('u4_exD_q6', C, 'D', 6, 'sq',
      'Make a list of hardware equipment for each topology.',
      '• Bus topology: one main backbone cable (coaxial), terminators at both ends, network interface cards (NICs) and T-connectors.\n'
      '• Star topology: a central hub or switch, one cable per computer and NICs.\n'
      '• Ring topology: cables connecting each computer in a loop, NICs and (in some types) a token/Multistation Access Unit.\n'
      '• Tree topology: a backbone cable, hubs/switches at different levels, connectors and NICs.',
      'Each topology needs different connecting devices and cabling arrangements.',
      100),
    q('u4_exD_q7', C, 'D', 7, 'sq',
      'Draw a Hybrid Topology diagram in which bus, ring and star topologies are used.',
      'Task: on paper, draw a diagram combining three topologies:\n'
      '1. Draw a horizontal backbone line (Bus) with terminators at both ends.\n'
      '2. Connect a Ring (a circle of connected nodes) to the bus through one node.\n'
      '3. Connect a Star (a central hub/switch with several computers on separate cables) to another point on the bus.\n'
      '4. Label the bus, ring and star sections and show how they join to form one hybrid network.',
      'A hybrid topology is a combination of two or more basic topologies and is used in large networks for flexibility and reliability.',
      100),
]


# ============================================================================
# UNIT 5 — Computer Security and Ethics   PDF pages 101-122
# A = MCQs (PDF 119-120), B = Short Qs (PDF 120-121), C = Match (PDF 121), D = Activities (PDF 122)
# ============================================================================

C = 5
SOLVED += [
    q('u5_exA_q1', C, S, 1, 'mcq',
      'The broad term that encompasses different harmful software is:',
      '(b) Malware',
      'Malware (malicious software) is the broad term that includes viruses, worms, Trojans, spyware and adware. Virus, adware and spyware are only specific types of malware.',
      119,
      [('a', 'Virus'), ('b', 'Malware'), ('c', 'Adware'), ('d', 'Spyware')], '(b)'),
    q('u5_exA_q2', C, S, 2, 'mcq',
      'The authentication mechanism that only allows the real person to access data or device is:',
      '(c) Biometric',
      'Biometrics (fingerprint, face or iris recognition) uses a unique physical feature of a person, so it can allow only the real person to access the data or device.',
      119,
      [('a', 'Username and Password'), ('b', 'PIN'), ('c', 'Biometric'), ('d', 'Scan Code')], '(c)'),
    q('u5_exA_q3', C, S, 3, 'mcq',
      'Software are mostly protected under:',
      '(b) Copyrights',
      'Software is protected mainly by copyright, which gives the creator the exclusive right to copy, distribute and sell the work. Patents protect inventions and trademarks protect brand names/logos.',
      119,
      [('a', 'Patents'), ('b', 'Copyrights'), ('c', 'Trademarks'), ('d', 'Logos')], '(b)'),
    q('u5_exA_q4', C, S, 4, 'mcq',
      'The professional ethics in computer field is important because:',
      '(d) It creates healthy and positive work environment.',
      'Professional ethics guide professionals to behave honestly and responsibly, which creates a healthy, positive and trustworthy work environment and protects the interests of users and society.',
      119,
      [('a', 'It is necessary by law.'), ('b', 'Violation can cause serious penalties.'),
       ('c', 'It is useful for financial benefits.'), ('d', 'It creates healthy and positive work environment.')], '(d)'),
    q('u5_exA_q5', C, S, 5, 'mcq',
      'Free Antivirus Software often:',
      '(b) Offer only limited service',
      'Free antivirus programs usually provide only basic protection; advanced features such as full real-time protection, ransomware defence and technical support are offered only in the paid version.',
      119,
      [('a', 'Expire after sometimes'), ('b', 'Offer only limited service'),
       ('c', 'Cannot be updated'), ('d', 'Cannot be purchased')], '(b)'),
    q('u5_exA_q6', C, S, 6, 'mcq',
      'Copying and pasting some texts from internet without acknowledging the real author is an example of:',
      '(a) Plagiarism',
      'Plagiarism is presenting someone else\'s work or ideas as your own without giving credit to the original author.',
      120,
      [('a', 'Plagiarism'), ('b', 'Illegal use of patent'),
       ('c', 'Information Piracy'), ('d', 'Copyright Violation')], '(a)'),
    q('u5_exA_q7', C, S, 7, 'mcq',
      'Since it does not harm or steal data, the least harmful malware is:',
      '(b) Adware',
      'Adware only displays unwanted advertisements and pop-up windows; it does not destroy files or steal data, so it is the least harmful type of malware.',
      120,
      [('a', 'Virus'), ('b', 'Adware'), ('c', 'Spyware'), ('d', 'Trojan')], '(b)'),
    q('u5_exA_q8', C, S, 8, 'mcq',
      'The malware that replicates itself and doesn\'t need to attach with any files is:',
      '(d) Worm',
      'A worm can copy (replicate) itself and spread across a network on its own; it does not need to attach itself to a host file, unlike a virus.',
      120,
      [('a', 'Virus'), ('b', 'Adware'), ('c', 'Spyware'), ('d', 'Worm')], '(d)'),
    q('u5_exA_q9', C, S, 9, 'mcq',
      'Through which virus spreads?',
      '(d) All of them',
      'A virus can spread through email attachments, Internet downloads and removable media such as flash disks and CDs — i.e., all of the given ways.',
      120,
      [('a', 'Email Attachments'), ('b', 'Internet Downloads'),
       ('c', 'Flash Disks and Cds'), ('d', 'All of them')], '(d)'),
    q('u5_exA_q10', C, S, 10, 'mcq',
      '"Click this link and win a $5 voucher at McDonald\'s". This is an example of:',
      '(c) Clickjacking',
      'The book describes clickjacking as a fraud in which users are tricked into clicking a link/button to "claim a reward they never applied for". A fake offer like "click this link and win a voucher" is such a trap that leads to malware or data theft. (It is also scam-like: never click such offers.)',
      120,
      [('a', 'Scam'), ('b', 'Phishing'), ('c', 'Clickjacking'), ('d', 'Hacking')], '(c)'),

    q('u5_exB_q1', C, 'B', 1, 'sq',
      'Why is computer security important? Write any three reasons.',
      'Computer security is important because:\n'
      '1. It protects valuable data and information from theft, loss or damage.\n'
      '2. It prevents unauthorised access to our computer, accounts and network.\n'
      '3. It protects our privacy and financial information (passwords, banking details) and keeps the system free from viruses and malware so that work can continue safely.',
      'Without security, personal and business information can be stolen or destroyed.',
      120),
    q('u5_exB_q2', C, 'B', 2, 'sq',
      'Explain Cyber Bullying with an example.',
      'Cyber bullying (cyber harassment) is the use of electronic means such as computers, mobile phones or the Internet to threaten, insult, embarrass or harass a person.\n\n'
      'Example: a student repeatedly posts insulting comments and spreads rumours about a classmate on social media, or sends threatening messages to that person.',
      'Cyber bullying harms the victim\'s self-esteem and emotions and is a punishable cyber crime.',
      120),
    q('u5_exB_q3', C, 'B', 3, 'sq',
      'Why is information accuracy important?',
      'Information accuracy is important because decisions, reports, banking, medical treatment and business all depend on correct data. If information is inaccurate it can lead to wrong decisions, financial loss, health risks and loss of trust. In computing, errors can spread very quickly, so data must be verified and kept accurate.',
      'Accurate information is the basis of reliable decisions and trustworthy systems.',
      120),
    q('u5_exB_q4', C, 'B', 4, 'sq',
      'What is Ethical Hacking?',
      'Ethical hacking is the practice of testing a computer system or network with the owner\'s permission, using the same techniques as hackers, in order to find security weaknesses and fix them before criminals can exploit them. Ethical hackers (white-hat hackers) work legally to improve security and protect data.',
      'Ethical hacking is done with consent and for protection, whereas criminal hacking is done illegally and for harm or profit.',
      120),
    q('u5_exB_q5', C, 'B', 5, 'sq',
      'Your friend has become a victim of cyber harassment. What two advices will you give him or her?',
      'Two advices:\n'
      '1. Do not reply or react to the harasser, and do not delete the evidence — save copies/screenshots of the messages.\n'
      '2. Report the incident to a trusted adult (parents/teacher) and to the authorities/website — block the person, report the account, and in Pakistan contact the National Response Centre for Cyber Crimes helpline 9911.',
      'Staying calm, preserving evidence and reporting are the safest ways to deal with cyber harassment.',
      120),
    q('u5_exB_q6', C, 'B', 6, 'sq',
      'Write any two measures to avoid email account hacking.',
      'Two measures:\n'
      '1. Use a strong, unique password, keep it secret, change it regularly and enable two-step verification.\n'
      '2. Never open suspicious links or attachments or give your password on unknown websites, and always log out from public/shared computers.',
      'Most email hacking is caused by weak passwords and by giving away login details on fake (phishing) pages.',
      120),
    q('u5_exB_q7', C, 'B', 7, 'sq',
      'How is software piracy harmful for software developers?',
      'Software piracy (the illegal use, copying or distribution of software) harms developers because they lose the sales revenue and profit they should have earned. This reduces the money available for research, updates, customer support and employees\' salaries, discourages innovation, and can force companies to raise prices for honest customers.',
      'Piracy is both illegal and unethical as it violates the creator\'s copyright.',
      120),
    q('u5_exB_q8', C, 'B', 8, 'sq',
      'Give two examples of phishing.',
      'Two examples:\n'
      '1. A fake email pretending to be from a bank that asks you to click a link and confirm your account details.\n'
      '2. A fraudulent website or message posing as a trusted company that asks for your username, password or credit-card details.',
      'Phishing uses false emails/websites to trick people into giving sensitive information.',
      120),
    q('u5_exB_q9', C, 'B', 9, 'sq',
      'What is an Intellectual Property Right?',
      'Intellectual Property Right (IPR) is a legal right that protects the creations of the human intellect — such as inventions, literary and artistic works, software, designs, symbols and names. IPR prevents others from stealing or illegally using these creations and is enforced through copyrights, patents and trademarks.',
      'IPR encourages creativity and innovation by giving creators control over their work.',
      120),
    q('u5_exB_q10', C, 'B', 10, 'sq',
      'Differentiate the following on the given criteria: Virus, Worm, Adware, Spyware.',
      'Criteria: (1) How is it initiated? (2) Means to spread (3) Effect on computer speed (4) Damage to data/hardware (5) Level of danger.\n\n'
      '• Virus — initiated when an infected file/program is run; spreads through infected files, email attachments and USB devices; slows the computer; can corrupt or delete data and damage software; danger: high.\n'
      '• Worm — initiates and runs by itself (no host file needed); spreads automatically across networks/email; consumes network bandwidth and slows the computer; can delete files and overload networks; danger: high.\n'
      '• Adware — comes with free/downloaded software; spreads through downloads and pop-up ads; slows browsing/computer slightly; shows unwanted ads and redirects the browser; danger: low (least harmful).\n'
      '• Spyware — installed secretly along with other software; spreads with bundled downloads; may slow the computer; secretly steals personal data and passwords; danger: high.',
      'All four are types of malware, but they differ in how they start, spread and harm the system.',
      121),

    q('u5_exC_q1', C, 'C', 1, 'sq',
      'Match the columns: (i) Presenting someone\'s ideas as your own without acknowledging the author',
      '(f) Plagiarism',
      'Plagiarism is presenting someone else\'s work or ideas as your own without proper acknowledgement of the author.',
      121),
    q('u5_exC_q2', C, 'C', 2, 'sq',
      'Match the columns: (ii) An advertising software that presents ads and pop-up windows to spread virus',
      '(a) Adware',
      'Adware is advertising software that displays unwanted ads and pop-up windows and can also help spread viruses.',
      121),
    q('u5_exC_q3', C, 'C', 3, 'sq',
      'Match the columns: (iii) Crime that is committed through a computer system',
      '(e) Cybercrime',
      'A cybercrime is any crime committed using a computer or computer network (hacking, fraud, harassment, etc.).',
      121),
    q('u5_exC_q4', C, 'C', 4, 'sq',
      'Match the columns: (iv) A secretive security code that verifies user\'s identity',
      '(c) PIN',
      'A PIN (Personal Identification Number) is a secret code used to verify a user\'s identity, e.g., for an ATM card.',
      121),
    q('u5_exC_q5', C, 'C', 5, 'sq',
      'Match the columns: (v) A person that gains unauthorized access to other computers by bypassing passwords',
      '(b) Cracker',
      'A cracker breaks into computer systems by bypassing passwords or other security controls, usually for a harmful purpose.',
      121),
    q('u5_exC_q6', C, 'C', 6, 'sq',
      'Match the columns: (vi) A utility software that prevents threats and data loss from a computer',
      '(d) Antivirus',
      'An antivirus is a utility software that detects, blocks and removes threats (viruses/malware) and prevents data loss.',
      121),

    q('u5_exD_q1', C, 'D', 1, 'sq',
      'Organize a poster exhibition in which students suggest measures to use the computer and the internet safely. Topics: prevent viruses & malware; say no to cyber bullying and harassment; say no to piracy and plagiarism; how to cope with cyber crimes.',
      'Task guidance — each group prepares a poster on one topic:\n'
      '• Prevent viruses and malware: use antivirus, update software, avoid suspicious links/attachments.\n'
      '• Say no to cyber bullying and harassment: be respectful online; block and report abusers.\n'
      '• Say no to piracy and plagiarism: buy legal software; always acknowledge sources.\n'
      '• How to cope with cyber crimes: save evidence, report to a trusted adult and to the authorities (helpline 9911).',
      'A poster exhibition spreads awareness of safe and ethical computer use.',
      122),
    q('u5_exD_q2', C, 'D', 2, 'sq',
      'During classroom discussion, put the following situations before students and discuss what they will do and why: (a) a phone call claiming you won a prize but asking an advance payment; (b) a file from an unknown email asking your bank details or email ID and password; (c) a website demanding your Facebook/Gmail credentials to view content.',
      'Discussion points (all are scams/phishing attempts):\n'
      '• (a) Prize + advance payment is a classic scam — never pay; disconnect and report.\n'
      '• (b) Never give bank details, email ID or password to unknown senders; delete the file without opening it and report the email as spam.\n'
      '• (c) Never enter your social-media or email credentials on unknown websites; such sites steal your account.',
      'The rule is: never share personal or financial information with unknown persons, links or websites.',
      122),
    q('u5_exD_q3', C, 'D', 3, 'sq',
      'Make a list of the services that free antivirus software does not offer.',
      'Services usually not offered by free antivirus software:\n'
      '• Full real-time (always-on) protection.\n'
      '• Protection against advanced threats such as ransomware.\n'
      '• Firewall and safe-banking/safe-browsing tools.\n'
      '• Email and web protection.\n'
      '• Automatic updates and priority virus definitions.\n'
      '• Technical support and customer service.',
      'Free versions offer only limited basic protection; full features are available only in paid versions.',
      122),
    q('u5_exD_q4', C, 'D', 4, 'sq',
      'Search newspapers or the internet to find news about a cyber crime, especially one in which the criminal was caught and punished.',
      'Task guidance:\n'
      '1. Search newspapers or the internet for a reported cyber crime (e.g., online fraud, hacking, identity theft or cyber harassment).\n'
      '2. Note the type of crime, how it was committed, the loss caused, and how the criminal was traced and punished.\n'
      '3. Present a short report and the lesson learnt (e.g., the importance of strong passwords and reporting crimes).',
      'Real cases show how cyber crimes are committed and how digital evidence helps catch the criminals.',
      122),
    q('u5_exD_q5', C, 'D', 5, 'sq',
      'Write an essay on any topic, copy and paste some text from internet websites, then check plagiarism using tools such as duplichecker.com, quetext.com and plagscan.com.',
      'Task guidance:\n'
      '1. Write an original essay on any topic.\n'
      '2. Copy and paste some text from internet websites into it.\n'
      '3. Visit a plagiarism-checking site (www.duplichecker.com, www.quetext.com or www.plagscan.com) and upload/paste your essay.\n'
      '4. Observe the percentage of copied (plagiarised) text highlighted by the tool.\n'
      '5. Rewrite the copied parts in your own words and give references so that the essay becomes original.',
      'Plagiarism checkers help students understand and avoid copying others\' work.',
      122),
]


# ============================================================================
# UNIT 6 — Web Development   PDF pages 123-147
# A = MCQs (PDF 144-145), B = Short Qs (PDF 146), C = Match (PDF 146), D = Activities (PDF 147)
# ============================================================================

C = 6
SOLVED += [
    q('u6_exA_q1', C, S, 1, 'mcq',
      'The service that is responsible for making websites publicly accessible through the internet is called:',
      '(b) Web Hosting',
      'Web hosting is the service that stores a website on a server connected to the Internet so that it becomes publicly accessible. The web server is the machine/software; hosting is the service.',
      144,
      [('a', 'Web Server'), ('b', 'Web Hosting'), ('c', 'Web Site'), ('d', 'Web Browser')], '(b)'),
    q('u6_exA_q2', C, S, 2, 'mcq',
      'The type of special website where different users can ask questions and give answers or discuss on various topics is called:',
      '(c) Forums site',
      'A forum is an online discussion site where users post questions and answers and discuss various topics.',
      144,
      [('a', 'Social site'), ('b', 'Blogs site'), ('c', 'Forums site'), ('d', 'Informational site')], '(c)'),
    q('u6_exA_q3', C, S, 3, 'mcq',
      'Entertainment site specializes in delivering:',
      '(d) Content like videos, images and games for entertainment',
      'Entertainment websites provide content such as videos, images, music and games for enjoyment (e.g., YouTube, gaming sites).',
      144,
      [('a', 'News, weather and current affairs'),
       ('b', 'Information about products and services of a business'),
       ('c', 'Personal information of a particular person'),
       ('d', 'Content like videos, images and games for entertainment')], '(d)'),
    q('u6_exA_q4', C, S, 4, 'mcq',
      'A web browser will translate the codes in a web page if the extension of the document is:',
      '(a) .html',
      'A web browser can interpret (render) HTML code, so the file must have an .html (or .htm) extension. Files such as .txt, .doc and .pdf are not HTML pages.',
      145,
      [('a', '.html'), ('b', '.txt'), ('c', '.doc'), ('d', '.pdf')], '(a)'),
    q('u6_exA_q5', C, S, 5, 'mcq',
      'The tag used to automatically add line space before and after the containing text is:',
      '(c) <p>',
      'The <p> (paragraph) tag adds a blank line (space) above and below the text automatically, unlike <br> which only breaks the line.',
      145,
      [('a', '<br>'), ('b', '<hr>'), ('c', '<p>'), ('d', '<pre>')], '(c)'),
    q('u6_exA_q6', C, S, 6, 'mcq',
      'The type of list which shows its items in a numerically ordered sequence is:',
      '(c) Ordered List',
      'An ordered list (<ol>) displays items in a numbered sequence (1, 2, 3 …); an unordered list (<ul>) uses bullets.',
      145,
      [('a', 'Nested List'), ('b', 'Unordered List'), ('c', 'Ordered List'), ('d', 'Description List')], '(c)'),
    q('u6_exA_q7', C, S, 7, 'mcq',
      'To create a clickable text which navigates to another page or section, we use:',
      '(d) <a> tag',
      'The <a> (anchor) tag creates a hyperlink. Its href attribute gives the target page/section, and clicking the text navigates there.',
      145,
      [('a', '<input> tag'), ('b', '<li> tag'), ('c', '<b> tag'), ('d', '<a> tag')], '(d)'),
    q('u6_exA_q8', C, S, 8, 'mcq',
      'To differentiate the heading cells from rest of the data in a table, we use:',
      '(a) <th> tag',
      'The <th> tag defines a table heading cell; its text is shown bold and centred, which differentiates it from the ordinary <td> data cells.',
      145,
      [('a', '<th> tag'), ('b', '<tr> tag'), ('c', '<td> tag'), ('d', '<dt> tag')], '(a)'),
    q('u6_exA_q9', C, S, 9, 'mcq',
      'The tag used to define the title caption of the web browser is:',
      '(c) <title>',
      'The <title> tag, placed inside <head>, sets the caption that is shown on the browser\'s title bar or tab; the <h1> tag is a visible heading in the page body.',
      145,
      [('a', '<thead>'), ('b', '<head>'), ('c', '<title>'), ('d', '<h1>')], '(c)'),
    q('u6_exA_q10', C, S, 10, 'mcq',
      'The attribute used to define the URL for reference of image in <img> tag is:',
      '(c) src',
      'The src (source) attribute of the <img> tag specifies the path/URL of the image file to display. href is used with <a>, and alt gives alternate text.',
      145,
      [('a', 'target'), ('b', 'name'), ('c', 'src'), ('d', 'href')], '(c)'),

    q('u6_exB_q1', C, 'B', 1, 'sq',
      'Differentiate between web hosting and web server.',
      '• Web server: both the hardware (a powerful computer) and the software (e.g., Apache, IIS) that stores web pages and delivers them to users\' browsers on request.\n'
      '• Web hosting: a service (provided by a hosting company) that provides space on a web server connected to the Internet so that a website becomes publicly accessible.\n\n'
      'In short: a web server is the machine/software, while web hosting is the paid service of storing your website on such a server.',
      'You need both a web server and a hosting service (which may be your own or rented) to publish a website.',
      146),
    q('u6_exB_q2', C, 'B', 2, 'sq',
      'What are the steps involved in creating a complete website?',
      'Steps to create a complete website:\n'
      '1. Plan the purpose, audience and structure of the site.\n'
      '2. Register a domain name.\n'
      '3. Design the layout and gather content (text, images).\n'
      '4. Write the HTML/CSS code for the pages.\n'
      '5. Test the pages in different browsers and fix errors.\n'
      '6. Choose a web host and upload (publish) the files.\n'
      '7. Maintain the site and update content regularly.',
      'Planning and testing before publishing help avoid mistakes and give a professional result.',
      146),
    q('u6_exB_q3', C, 'B', 3, 'sq',
      'Differentiate between <head>, <title> and <h1> to <h6> tags.',
      '• <head>: a container element that holds information about the page (metadata) such as the title, styles and scripts; its content is not shown in the page body.\n'
      '• <title>: placed inside <head>; it sets the caption shown on the browser\'s title bar/tab.\n'
      '• <h1>–<h6>: heading tags used inside the body to display visible headings of different sizes; <h1> is the largest (main heading) and <h6> the smallest.',
      '<head> holds information about the page, while <h1>–<h6> display headings on the page.',
      146),
    q('u6_exB_q4', C, 'B', 4, 'sq',
      'Identify and explain some HTML tags used for formatting of the content.',
      'Formatting tags:\n'
      '• <b> / <strong> — bold text.\n'
      '• <i> / <em> — italic text.\n'
      '• <u> — underlined text.\n'
      '• <sub> — subscript (e.g., H<sub>2</sub>O).\n'
      '• <sup> — superscript (e.g., x<sup>2</sup>).\n'
      '• <br> — line break; <hr> — horizontal rule.\n'
      '• <p> — paragraph; <h1>–<h6> — headings; <mark> — highlighted text.',
      'These tags control how the text appears on the web page.',
      146),
    q('u6_exB_q5', C, 'B', 5, 'sq',
      'Differentiate between ordered and unordered lists.',
      '• Ordered list (<ol>): displays items in a numbered/ordered sequence (1, 2, 3 …); used when the order of items matters, e.g., steps in a procedure.\n'
      '• Unordered list (<ul>): displays items with bullet points; used when the order does not matter, e.g., a list of features.\n\n'
      'In both types each item is written inside <li> tags.',
      'The <li> (list item) tag is used for individual items in both ordered and unordered lists.',
      146),
    q('u6_exB_q6', C, 'B', 6, 'sq',
      'How are images displayed in an HTML page?',
      'Images are displayed with the <img> tag, which is an empty (self-closing) tag and does not need a closing tag.\n\n'
      'It uses the attributes:\n'
      '• src — the path/URL of the image file.\n'
      '• alt — alternate text shown if the image cannot load.\n'
      '• width and height — size of the image.\n\n'
      'Example: <img src="pic.jpg" alt="sample" width="200">',
      'The <img> tag places the image at that position in the page flow.',
      146),
    q('u6_exB_q7', C, 'B', 7, 'sq',
      'How can a user be redirected to another web page?',
      'By using a hyperlink created with the <a> (anchor) tag. The href attribute gives the address of the target page; clicking the link redirects the user.\n\n'
      'Example: <a href="page2.html">Go to Page 2</a>\n\n'
      'Hyperlinks can also jump to a section within the same page using a #id, or open an external website with a full URL.',
      'The <a> tag is the basic navigation element of the web.',
      146),
    q('u6_exB_q8', C, 'B', 8, 'sq',
      'What kind of HTML elements are used to display data in rows and columns? Discuss some of its formatting features.',
      'Tables are used to display data in rows and columns. Tags:\n'
      '• <table> — creates the table.\n'
      '• <tr> — creates a table row.\n'
      '• <th> — a heading cell; <td> — a data cell.\n'
      '• <caption> — table title; <thead>/<tbody> — header/body sections.\n\n'
      'Formatting features: border, cellpadding, cellspacing, width, height, align, bgcolor/background, and colspan/rowspan to merge cells.',
      'Tables organize content neatly into rows and columns and are useful for displaying structured data.',
      146),
    q('u6_exB_q9', C, 'B', 9, 'sq',
      'Is it possible to display the entire contents of another web page in our HTML page? How?',
      'Yes — by using the <iframe> (inline frame) tag. It embeds another web page inside the current page.\n\n'
      'Example: <iframe src="other.html" width="500" height="300"></iframe>\n\n'
      'Frames/framesets were also used earlier to divide a page into different frames, each showing a separate page.',
      'The iframe creates a small window inside the page that shows another page\'s content.',
      146),
    q('u6_exB_q10', C, 'B', 10, 'sq',
      'List some popular text editors and other tools which help in designing and development of websites.',
      'Popular text editors and tools:\n'
      '• Notepad, Notepad++\n'
      '• Sublime Text\n'
      '• Visual Studio Code\n'
      '• Atom, Brackets\n'
      '• Adobe Dreamweaver, Bluefish (with visual/WYSIWYG design support).',
      'These editors provide syntax highlighting and helpful features for writing HTML, CSS and JavaScript.',
      146),

    q('u6_exC_q1', C, 'C', 1, 'sq',
      'Match the columns: (i) E-Commerce',
      '(e) Business website',
      'An e-commerce site is a business website used for buying and selling goods or services online.',
      146),
    q('u6_exC_q2', C, 'C', 2, 'sq',
      'Match the columns: (ii) <head>',
      '(d) Contains additional information and styling features of the web page',
      'The <head> section contains metadata, the title, styles (CSS) and scripts — extra information and styling for the page that is not shown in the body.',
      146),
    q('u6_exC_q3', C, 'C', 3, 'sq',
      'Match the columns: (iii) <ul><ol><dl>',
      '(b) Organize information as list points',
      'The list tags <ul>, <ol> and <dl> organize information as list points (bulleted, numbered or description lists).',
      146),
    q('u6_exC_q4', C, 'C', 4, 'sq',
      'Match the columns: (iv) <tables>',
      '(c) Organize information in rows and columns',
      'HTML tables organize information in rows and columns.',
      146),
    q('u6_exC_q5', C, 'C', 5, 'sq',
      'Match the columns: (v) <img>',
      '(f) Add images and infographics to the web page',
      'The <img> tag is used to add images (and infographics) to a web page.',
      146),
    q('u6_exC_q6', C, 'C', 6, 'sq',
      'Match the columns: (vi) Hyperlinks',
      '(a) Add navigation support to web pages',
      'Hyperlinks (created with the <a> tag) provide navigation from one page or section to another.',
      146),

    q('u6_exD_q1', C, 'D', 1, 'sq',
      'Create three pages: home.html (title, heading "Input and Output Devices", unordered list with hyperlinks to inputs.html and outputs.html), inputs.html (title, table with names and 200-pixel images of input devices), outputs.html (same for output devices).',
      'home.html:\n'
      '<html><head><title>Unit 6 – Activity – Home</title></head>\n'
      '<body>\n'
      '  <h1>Input and Output Devices</h1>\n'
      '  <ul>\n'
      '    <li><a href="inputs.html">Input Devices</a></li>\n'
      '    <li><a href="outputs.html">Output Devices</a></li>\n'
      '  </ul>\n'
      '</body></html>\n\n'
      'inputs.html:\n'
      '<html><head><title>Unit 6 – Activity – Input Devices</title></head>\n'
      '<body>\n'
      '  <table border="1">\n'
      '    <tr><td>Keyboard</td><td><img src="keyboard.jpg" width="200"></td></tr>\n'
      '    <tr><td>Mouse</td><td><img src="mouse.jpg" width="200"></td></tr>\n'
      '  </table>\n'
      '</body></html>\n\n'
      'outputs.html: same structure with output device names (Monitor, Printer) and their images (width="200").',
      'This activity practises hyperlinks, tables and images — three important HTML features.',
      147),
]


# ============================================================================
# UNIT 7 — Introduction to Database System   PDF pages 148-168
# A = MCQs (PDF 163-164), B = Short Qs (PDF 164), C = Match (PDF 165), D = Activities (PDF 165)
# ============================================================================

C = 7
SOLVED += [
    q('u7_exA_q1', C, S, 1, 'mcq',
      'Which of the following Microsoft Office packages is a DBMS?',
      '(d) MS Access',
      'MS Access is a Database Management System (DBMS) used to create and manage databases. Word, Excel and PowerPoint are word-processing, spreadsheet and presentation programs.',
      163,
      [('a', 'MS-Word'), ('b', 'MS-Excel'), ('c', 'MS-Power Point'), ('d', 'MS-Access')], '(d)'),
    q('u7_exA_q2', C, S, 2, 'mcq',
      'The basic limitation of a flat file database is that:',
      '(b) It stores data in a single file',
      'A flat file database stores all data in a single file/table, which leads to duplication (redundancy), inconsistency and difficulty in managing large data. A DBMS solves these problems using related tables.',
      163,
      [('a', 'It is complicated'), ('b', 'It stores data in a single file'),
       ('c', 'It is very heavy'), ('d', 'It is not supported on internet')], '(b)'),
    q('u7_exA_q3', C, S, 3, 'mcq',
      'In a database table of "Students", the address of the student will be a:',
      '(b) Field',
      'A field is a single column of a table that stores one type of information, e.g., the "Address" column. A record is a complete row.',
      163,
      [('a', 'Record'), ('b', 'Field'), ('c', 'Entity'), ('d', 'Data type')], '(b)'),
    q('u7_exA_q4', C, S, 4, 'mcq',
      'In a database table of "Students", the particulars of a single student will be a:',
      '(a) Record',
      'A record is a complete row of a table that holds all the fields (particulars) of one entity — here, all the data of a single student.',
      163,
      [('a', 'Record'), ('b', 'Field'), ('c', 'Entity'), ('d', 'Data type')], '(a)'),
    q('u7_exA_q5', C, S, 5, 'mcq',
      'In a relational database, keys are used to create a:',
      '(d) Relationship',
      'Keys (primary and foreign) are used to link tables and create relationships between them in a relational database.',
      163,
      [('a', 'Table'), ('b', 'Fields'), ('c', 'Records'), ('d', 'Relationship')], '(d)'),
    q('u7_exA_q6', C, S, 6, 'mcq',
      'A field that stores the names of students should be defined as:',
      '(c) String',
      'A String (text) data type is used to store text such as names. Integer and Float store numbers, and Boolean stores True/False.',
      163,
      [('a', 'Integer'), ('b', 'Float'), ('c', 'String'), ('d', 'Boolean')], '(c)'),
    q('u7_exA_q7', C, S, 7, 'mcq',
      'A key that allows only unique entries in a field is called:',
      '(a) Primary Key',
      'A primary key uniquely identifies each record in a table, so it allows only unique values (no duplicates and no nulls).',
      163,
      [('a', 'Primary Key'), ('b', 'Secondary Key'), ('c', 'Foreign Key'), ('d', 'Super Key')], '(a)'),
    q('u7_exA_q8', C, S, 8, 'mcq',
      'Data Redundancy means:',
      '(a) Duplication of Data',
      'Data redundancy means the unnecessary duplication (repetition) of the same data in more than one place. A good database design reduces redundancy.',
      163,
      [('a', 'Duplication of Data'), ('b', 'Variety of Data'),
       ('c', 'Size of Data'), ('d', 'Data Type')], '(a)'),
    q('u7_exA_q9', C, S, 9, 'mcq',
      'The relationship that matches one record of an entity with only one record of another entity is called:',
      '(a) One-to-One relationship',
      'In a one-to-one relationship, one record of an entity is related to only one record of another entity (e.g., one person has one national ID card).',
      164,
      [('a', 'One-to-One relationship'), ('b', 'One-to-Many relationship'),
       ('c', 'Many-to-One relationship'), ('d', 'Many-to-Many relationship')], '(a)'),
    q('u7_exA_q10', C, S, 10, 'mcq',
      'The shape that is used to represent an attribute in an ERD is:',
      '(d) An ellipse',
      'In an Entity Relationship Diagram, an entity is drawn as a rectangle, an attribute as an ellipse (oval) and a relationship as a diamond.',
      164,
      [('a', 'A diamond'), ('b', 'An octagon'), ('c', 'A rectangle'), ('d', 'An ellipse')], '(d)'),

    q('u7_exB_q1', C, 'B', 1, 'sq',
      'Why Database Management System is preferred over Flat File System?',
      'A DBMS is preferred over a flat file system because it:\n'
      '1. reduces data redundancy (duplication) by storing data in related tables;\n'
      '2. avoids inconsistency, so the same data is not stored in many places;\n'
      '3. allows data sharing among many users;\n'
      '4. enforces data integrity, accuracy and security;\n'
      '5. supports queries, reports and different views of the data;\n'
      '6. makes updating and retrieving large data easy and reliable.',
      'A flat file stores everything in one file, causing duplication and difficulty in managing and updating data.',
      164),
    q('u7_exB_q2', C, 'B', 2, 'sq',
      'Discuss the use of databases in business with example.',
      'Databases are used in business to store and manage large amounts of related data such as customers, products, sales and employees.\n\n'
      'Example: a bank stores customer accounts, balances and transactions in a database; using it, the bank can quickly find a customer\'s balance, generate statements and detect fraud. Similarly, a school keeps student records, marks and attendance in a database.',
      'A database lets a business retrieve accurate information quickly and make better decisions.',
      164),
    q('u7_exB_q3', C, 'B', 3, 'sq',
      'What is the difference between Design View and Datasheet View?',
      '• Design View: used to define or change the structure of a table — the field names, data types, descriptions and the primary key.\n'
      '• Datasheet View: used to enter, view and edit the actual data (records) of the table in a row-and-column layout, similar to a spreadsheet.',
      'Design View defines the table\'s structure, while Datasheet View is used for the data itself.',
      164),
    q('u7_exB_q4', C, 'B', 4, 'sq',
      'Why is it important to carefully decide the data type for each field?',
      'The data type of a field decides what kind of values can be stored and how much space they take. Choosing the correct data type:\n'
      '• ensures data is stored correctly (numbers as numbers so they can be calculated, dates as dates);\n'
      '• prevents wrong entries;\n'
      '• saves storage space; and\n'
      '• improves the accuracy and speed of queries and calculations.',
      'For example, a phone number should be stored as text, but marks should be stored as numbers.',
      164),
    q('u7_exB_q5', C, 'B', 5, 'sq',
      'What is the difference between table and view?',
      '• Table: a stored object in the database that physically holds the data in rows (records) and columns (fields).\n'
      '• View: a virtual table — it does not store data itself; it shows data selected from one or more tables by a query.\n\n'
      'A view is used to display only the required data and to hide sensitive fields from certain users.',
      'A view acts like a window into the data of one or more tables.',
      164),
    q('u7_exB_q6', C, 'B', 6, 'sq',
      'Explain entities, attributes and relationships with one example of each.',
      '• Entity: a real-world object or person about which data is stored (e.g., Student, Teacher).\n'
      '• Attribute: a property or characteristic of an entity (e.g., Roll No, Name, Address of a Student).\n'
      '• Relationship: an association between two entities (e.g., a Student is enrolled in a Class).\n\n'
      'Example: Entity = Student; its attributes = Roll No, Name, Class; relationship = Student → enrolled in → Class.',
      'In an ERD, entities are rectangles, attributes are ellipses and relationships are diamonds.',
      164),
    q('u7_exB_q7', C, 'B', 7, 'sq',
      'List the major characteristics of primary and foreign keys.',
      '• Primary key: uniquely identifies each record in a table; it never contains duplicate values and cannot be null; a table has only one primary key.\n'
      '• Foreign key: a field in one table that refers to the primary key of another table; it may contain duplicate values and may be null; it is used to create a link (relationship) between two tables and to maintain referential integrity.',
      'Primary key = unique identifier of a table; foreign key = reference to another table\'s primary key.',
      164),
    q('u7_exB_q8', C, 'B', 8, 'sq',
      'Write three benefits of using relationships in the database.',
      'Three benefits:\n'
      '1. They avoid data redundancy, because data is not repeated in every table.\n'
      '2. They maintain data integrity and consistency, since related data is stored once and linked.\n'
      '3. They make it easy to combine and retrieve data from several tables through queries and reports.',
      'Relationships are the basis of a well-designed relational database.',
      164),
    q('u7_exB_q9', C, 'B', 9, 'sq',
      'Discuss the importance of ERD in business.',
      'An Entity Relationship Diagram (ERD) is a graphical plan of a database. In business it is important because it:\n'
      '• shows the entities, their attributes and the relationships before the database is built;\n'
      '• helps designers and managers understand the data structure;\n'
      '• avoids mistakes and redundancy;\n'
      '• communicates the design clearly to the team; and\n'
      '• ensures the database meets the business requirements.',
      'A good ERD saves time and cost by planning the database properly before implementation.',
      164),
    q('u7_exB_q10', C, 'B', 10, 'sq',
      'Write any two statements from the following ER Diagram (Company – Advertisement – Candidate – Interview).',
      'Two statements from the ER diagram:\n'
      '1. A Company releases an Advertisement (Company → releases → Advertisement).\n'
      '2. A Candidate applies for an Advertisement and faces an Interview (Candidate → applies for → Advertisement; Candidate → faces → Interview).\n\n'
      'Other statements: a Candidate takes/appears in an Interview; an Advertisement brings Candidates.',
      'An ER diagram can be read as simple sentences describing how the entities are related.',
      164),

    q('u7_exC_q1', C, 'C', 1, 'sq',
      'Match the columns: (i) Primary Key',
      '(b) Always unique value in field',
      'A primary key always holds a unique value in its field so that each record can be identified.',
      165),
    q('u7_exC_q2', C, 'C', 2, 'sq',
      'Match the columns: (ii) Integer data',
      '(d) Number without decimal point',
      'Integer data type stores whole numbers (numbers without a decimal point).',
      165),
    q('u7_exC_q3', C, 'C', 3, 'sq',
      'Match the columns: (iii) Relationship',
      '(e) Connection between two tables',
      'A relationship is a connection (link) between two tables created with keys.',
      165),
    q('u7_exC_q4', C, 'C', 4, 'sq',
      'Match the columns: (iv) Field',
      '(a) Attributes',
      'A field is a column of a table that stores one attribute of the entity.',
      165),
    q('u7_exC_q5', C, 'C', 5, 'sq',
      'Match the columns: (v) View',
      '(f) Shows virtual data',
      'A view is a virtual table that shows data selected from one or more tables without storing it.',
      165),
    q('u7_exC_q6', C, 'C', 6, 'sq',
      'Match the columns: (vi) Flat file system',
      '(c) Data in plain text form',
      'In a flat file system all data is kept in a single file (plain text/table form) without relationships.',
      165),
    q('u7_exC_q7', C, 'C', 7, 'sq',
      'Match the columns: (vii) Entity',
      '(g) Table with its own attributes',
      'An entity becomes a table that has its own attributes (fields).',
      165),

    q('u7_exD_q1', C, 'D', 1, 'sq',
      'Create few tables and practice adding, updating and deleting records in MS Access.',
      'Steps:\n'
      '1. Open MS Access and create a Blank Database.\n'
      '2. Create → Table Design; add fields (e.g., Roll No, Name, Marks) with their data types and set a primary key.\n'
      '3. Switch to Datasheet View.\n'
      '• Adding: type new data in the last empty row.\n'
      '• Updating: click in a cell and change its value.\n'
      '• Deleting: select the row (record) and press Delete (confirm the warning).\n'
      '4. Save the table with a suitable name.',
      'These operations practise data entry (CRUD) in a database table.',
      165),
    q('u7_exD_q2', C, 'D', 2, 'sq',
      'Create a table in MS Access by importing an Excel Sheet. Examine the data type of each field after importing and change where required.',
      'Steps:\n'
      '1. External Data → New Data Source → From File → Excel.\n'
      '2. Browse to the Excel file, choose "Import the source data into a new table" and select the sheet.\n'
      '3. Tick "First Row Contains Column Headings" and click Next/Finish.\n'
      '4. Open the new table in Design View.\n'
      '5. Check the data type of each field (text, number, date, etc.) and change any field whose type was detected wrongly, then save.',
      'Access guesses the data types from the data, so the types should always be checked after importing.',
      165),
    q('u7_exD_q3', C, 'D', 3, 'sq',
      'Create different views to show data from two tables.',
      'Steps:\n'
      '1. Make sure the two tables have a common field (related by a foreign key).\n'
      '2. Create → Query Design; add both tables to the query window.\n'
      '3. Join the common fields (Access shows a line between them).\n'
      '4. Select the fields you want to display from the two tables in the grid.\n'
      '5. Run the query to see the combined data, and save it as a view/query (e.g., "StudentMarks").',
      'A query (view) combines data from two tables without storing a duplicate copy.',
      165),
    q('u7_exD_q4', C, 'D', 4, 'sq',
      'Draw a simple ERD on paper and implement it in MS Access (at least three entities, attributes, data types, primary and foreign keys and simple relationships).',
      'Task guidance:\n'
      '1. Choose three entities, e.g., Student, Class and Teacher.\n'
      '2. List attributes for each (Student: RollNo, Name, ClassID; Class: ClassID, ClassName; Teacher: TeacherID, Name, ClassID).\n'
      '3. Draw rectangles for entities, ellipses for attributes and diamonds for relationships; mark primary keys (underlined).\n'
      '4. Implement in Access: create a table for each entity in Design View, set the correct data type for every field and set the primary key.\n'
      '5. Add foreign-key fields and create relationships using Database Tools → Relationships (drag the primary key of one table onto the matching field of another).',
      'This activity brings together all the database concepts: entities, attributes, data types, keys and relationships.',
      165),
]


# ============================================================================
# BUILD
# ============================================================================

def build():
    solved_by_chapter = {}
    for item in SOLVED:
        solved_by_chapter.setdefault(item['chapter'], []).append(item)

    chapters = []
    for num, title, ps, pe in CHAPTERS:
        qs = solved_by_chapter.get(num, [])
        chapters.append({
            'number': num, 'title': title,
            'startPage': ps, 'endPage': pe,
            'bookStart': ps - 6, 'bookEnd': pe - 6,
            'totalQuestions': len(qs), 'questions': qs,
        })

    solved_pages = {}
    for item in SOLVED:
        solved_pages.setdefault(item['pdfPage'], []).append(item)

    pages_map = {}
    for p in range(1, TOTAL_PAGES + 1):
        chapter_number = None
        for num, _t, ps, pe in CHAPTERS:
            if ps <= p <= pe:
                chapter_number = num
                break
        pages_map[str(p)] = {
            'pdfPage': p,
            'bookPage': p - 6 if p > FRONT_MATTER_PAGES else None,
            'chapterNumber': chapter_number,
            'isFrontMatter': p <= FRONT_MATTER_PAGES,
            'hasExercise': p in solved_pages,
            'questions': solved_pages.get(p, []),
        }

    data = {
        'subject': 'Computer Science',
        'grade': 'Class IX',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': TOTAL_PAGES,
        'totalChapters': len(CHAPTERS),
        'totalQuestionsSolved': len(SOLVED),
        'chapters': chapters,
        'pages': pages_map,
    }

    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Built {OUT}: {len(SOLVED)} solved items across {len(chapters)} units.")
    for ch in chapters:
        print(f"  Unit {ch['number']}: {ch['totalQuestions']} items "
              f"(book pp.{ch['bookStart']}-{ch['bookEnd']})")


if __name__ == '__main__':
    build()