"""Computer Science XI — Unit 1: Computer Systems (book pages 1-70)."""
from .common import bq, mcq

ITEMS = []

# ---------------------------------------------------------------------------
# A. Encircle the correct answer — PDF 74 (book 69)
# ---------------------------------------------------------------------------
ITEMS += [
    mcq(1, 'A', 'i', 'A digital signal has:',
        [('a', 'Infinite values'), ('b', 'Only two values'),
         ('c', 'Three values'), ('d', 'Ten values')], 'b',
        'A digital signal is discrete: it carries only two levels, 0 (low) and 1 (high). '
        'Any continuous range of values belongs to an analog signal.', 74),
    mcq(1, 'A', 'ii', 'Which gate gives output 1 only when all inputs are 1?',
        [('a', 'OR gate'), ('b', 'AND gate'),
         ('c', 'NOT gate'), ('d', 'NOR gate')], 'b',
        'The AND gate is defined by Y = A\u00b7B. Its output is 1 only when every input is 1; '
        'a single 0 input forces the output to 0.', 74),
    mcq(1, 'A', 'iii', 'XOR gate gives output 1 when inputs are:',
        [('a', 'Same'), ('b', 'Different'),
         ('c', 'Both 0'), ('d', 'Both 1')], 'b',
        'XOR (exclusive-OR) gives Y = A\u2295B = A\u2032B + AB\u2032, which is 1 only when the inputs differ. '
        'Equal inputs (both 0 or both 1) give 0.', 74),
    mcq(1, 'A', 'iv', 'Which phase comes first in SDLC?',
        [('a', 'Testing'), ('b', 'Requirement Analysis'),
         ('c', 'Coding'), ('d', 'Design')], 'b',
        'The Software Development Life Cycle starts with requirement gathering and analysis: '
        'what the system must do is established before planning, design, coding or testing.', 74),
    mcq(1, 'A', 'v', 'In Agile, a short development cycle is called:',
        [('a', 'Phase'), ('b', 'Sprint'),
         ('c', 'Module'), ('d', 'Release')], 'b',
        'Agile divides work into time-boxed iterations called sprints (commonly 1-4 weeks), '
        'each ending with a potentially shippable increment.', 74),
    mcq(1, 'A', 'vi', 'Which testing type does NOT require knowledge of code?',
        [('a', 'White box testing'), ('b', 'Black box testing'),
         ('c', 'Unit testing'), ('d', 'Code review')], 'b',
        'Black-box testing checks inputs and outputs against the specification without looking at '
        'the internal code; white-box testing and code review require the source.', 74),
    mcq(1, 'A', 'vii', 'What device operates at the Network layer (Layer 3) of the OSI model?',
        [('a', 'Hub'), ('b', 'Switch'),
         ('c', 'Router'), ('d', 'Repeater')], 'c',
        'A router makes forwarding decisions from logical (IP) addresses, which are handled by '
        'Layer 3. Hubs and repeaters work at Layer 1; switches normally work at Layer 2.', 74),
    mcq(1, 'A', 'viii', 'How many layers does the TCP/IP model have?',
        [('a', '3'), ('b', '4'),
         ('c', '5'), ('d', '7')], 'b',
        'The TCP/IP model has four layers: Network Access (Link), Internet, Transport and Application.', 74),
    mcq(1, 'A', 'ix', 'UDP is preferred over TCP for video streaming because:',
        [('a', 'UDP is more reliable'), ('b', 'UDP is slower but more accurate'),
         ('c', 'UDP is faster and has lower delay'), ('d', 'UDP guarantees delivery')], 'c',
        'Streaming tolerates an occasional lost frame but not delay. UDP has no handshake, '
        'acknowledgements or retransmissions, so it is faster with lower latency than TCP.', 74),
    mcq(1, 'A', 'x', 'Which OSI layer is responsible for routing packets between networks?',
        [('a', 'Physical'), ('b', 'Data Link'),
         ('c', 'Network'), ('d', 'Transport')], 'c',
        'The Network layer (Layer 3) performs logical addressing and routing, choosing the path '
        'a packet takes across interconnected networks.', 74),
]

# ---------------------------------------------------------------------------
# B. Fill in the Blanks — PDF 74-75 (book 69-70)
# ---------------------------------------------------------------------------
ITEMS += [
    bq(1, 'B', 'i', 'An ____________ gate gives output 1 only when both the inputs are same.',
       'XNOR (Exclusive-NOR) gate',
       'The XNOR gate is the complement of XOR: Y = AB + A\u2032B\u2032. Its output is 1 for equal inputs '
       '(0,0 or 1,1) and 0 for different inputs.', 74),
    bq(1, 'B', 'ii', 'The ____________ gate is also called an inverter.',
       'NOT gate',
       'The NOT gate has one input and one output, Y = A\u2032. It inverts (complements) the input, '
       'which is why it is called an inverter.', 74),
    bq(1, 'B', 'iii', 'In Agile, a short development cycle is called a ____________.',
       'sprint',
       'An Agile sprint is a fixed-length iteration in which a small, prioritized set of features '
       'is designed, built and tested.', 74),
    bq(1, 'B', 'iv', 'SRS stands for ____________.',
       'Software Requirements Specification',
       'The SRS is the document that records the functional and non-functional requirements of a '
       'system and acts as the basis for design, coding and acceptance testing.', 75),
    bq(1, 'B', 'v', 'UDP stands for ____________.',
       'User Datagram Protocol',
       'UDP is a connectionless transport-layer protocol. It sends datagrams without a handshake, '
       'acknowledgements or retransmission, trading reliability for speed.', 75),
]

# ---------------------------------------------------------------------------
# C. Short descriptive answers — PDF 75 (book 70)
# ---------------------------------------------------------------------------
ITEMS += [
    bq(1, 'C', 'i', 'Define digital logic and give two examples of digital devices.',
       'Digital logic is the branch of electronics that processes information represented by '
       'discrete binary values (0 and 1) using logic gates and Boolean algebra.\n'
       'Examples of digital devices: a computer (laptop/desktop) and a smartphone. '
       'Other valid examples: digital watch, calculator, digital camera, smart TV.',
       'Digital logic circuits implement Boolean operations with gates such as AND, OR and NOT. '
       'Because the signals take only two levels, the circuits are less sensitive to noise and '
       'can be manufactured reliably on a large scale.', 75),
    bq(1, 'C', 'ii', 'What is the difference between analog and digital signals?',
       'An analog signal varies continuously over time and can take any value in a range, so it is '
       'represented by a smooth wave (e.g. the output of a microphone or a mercury thermometer).\n'
       'A digital signal is discrete: it takes only fixed values, normally two voltage levels '
       'representing 0 and 1, and is represented by square pulses.\n'
       'Analog signals are more affected by noise and are harder to store and process; digital '
       'signals are noise-resistant, easy to compress, store and transmit without loss.',
       'The key distinction is continuity. Analog values change smoothly; digital values jump '
       'between two allowed levels.', 75),
    bq(1, 'C', 'iii', 'Compare Waterfall and Agile models. When would we use each?',
       'Waterfall: linear and sequential. Each phase (requirements, design, coding, testing, '
       'deployment) must be completed before the next begins; requirements are frozen early; '
       'customer feedback arrives mainly at the end.\n'
       'Agile: iterative and incremental. Work is divided into short sprints, each producing a '
       'working increment; requirements may change between sprints and the customer is involved '
       'continuously.\n'
       'Use Waterfall when requirements are stable, well understood and regulatory/contractual '
       'documentation is required (e.g. a banking or safety-critical system with a fixed scope). '
       'Use Agile when requirements are uncertain or evolving and early feedback matters '
       '(e.g. a new mobile app or a web start-up product).',
       'Waterfall optimizes predictability and documentation; Agile optimizes flexibility and '
       'early delivery of value. The right choice depends on requirement stability and how often '
       'the customer can give feedback.', 75),
    bq(1, 'C', 'iv', 'What is the difference between an IP address and a MAC address?',
       'A MAC address is a 48-bit physical/hardware address burned into a network interface card '
       '(e.g. 00:1A:2B:3C:4D:5E). It is used inside a local network by the Data Link layer and is '
       'normally permanent.\n'
       'An IP address is a logical address assigned to a device on a network (IPv4: 32-bit, '
       'e.g. 192.168.1.10; IPv6: 128-bit). It is used by the Network layer to route packets '
       'between networks and can change when the device joins a different network.\n'
       'In short: MAC addresses identify a hardware interface locally; IP addresses identify a '
       "device's location logically across networks.",
       'MAC = flat, physical, local; IP = hierarchical, logical, routable. ARP is the protocol '
       'that maps a known IP address to a MAC address on a LAN.', 75),
    bq(1, 'C', 'v', 'Explain the difference between TCP and UDP. Give one real-life example of each.',
       'TCP is connection-oriented and reliable. It establishes a connection with a three-way '
       'handshake, numbers the segments, acknowledges received data and retransmits lost packets, '
       'and preserves order. It has more overhead.\n'
       'UDP is connectionless and unreliable. It sends independent datagrams with no handshake, '
       'acknowledgement or retransmission, so packets may be lost or arrive out of order, but it '
       'is faster and has lower delay.\n'
       'Examples: TCP \u2014 loading a web page over HTTPS or downloading a file, where every byte must '
       'arrive correctly. UDP \u2014 live video streaming or an online game, where low latency matters '
       'more than recovering an occasional lost packet.',
       'TCP trades speed for guaranteed, ordered delivery; UDP trades reliability for speed and '
       'low latency. The application requirement decides which is appropriate.', 75),
]

# ---------------------------------------------------------------------------
# D. Detailed answers — PDF 75 (book 70)
# ---------------------------------------------------------------------------
ITEMS += [
    bq(1, 'D', 'i', 'Explain all seven logic gates with their symbols, Boolean expressions, and truth tables.',
       '1. AND gate \u2014 Boolean expression Y = A\u00b7B. Output is 1 only when both inputs are 1. '
       'Truth table (inputs A B \u2192 Y): 00\u21920, 01\u21920, 10\u21920, 11\u21921. Symbol: a D-shaped body with two inputs.\n'
       '2. OR gate \u2014 Y = A + B. Output is 1 when at least one input is 1. '
       'Truth table: 00\u21920, 01\u21921, 10\u21921, 11\u21921. Symbol: a curved shield with two inputs.\n'
       '3. NOT gate (inverter) \u2014 Y = A\u2032. Output is the complement of the input. '
       'Truth table: 0\u21921, 1\u21920. Symbol: a triangle with a small circle (bubble) at the output.\n'
       '4. NAND gate \u2014 Y = (A\u00b7B)\u2032. It is an AND gate followed by a NOT. '
       'Truth table: 00\u21921, 01\u21921, 10\u21921, 11\u21920. Symbol: D-shape with an output bubble.\n'
       '5. NOR gate \u2014 Y = (A + B)\u2032. It is an OR gate followed by a NOT. '
       'Truth table: 00\u21921, 01\u21920, 10\u21920, 11\u21920. Symbol: curved shield with an output bubble.\n'
       '6. XOR gate \u2014 Y = A\u2295B = A\u2032B + AB\u2032. Output is 1 when the inputs differ. '
       'Truth table: 00\u21920, 01\u21921, 10\u21921, 11\u21920. Symbol: OR-shaped gate with an extra curved input line.\n'
       '7. XNOR gate \u2014 Y = AB + A\u2032B\u2032. Output is 1 when the inputs are equal. '
       'Truth table: 00\u21921, 01\u21920, 10\u21920, 11\u21921. Symbol: XOR gate with an output bubble.',
       'Each gate is defined by its Boolean expression, and the truth table lists the output for '
       'every possible input combination. NAND and NOR are called universal gates because any '
       'other gate can be built using them alone.', 75),
    bq(1, 'D', 'ii', 'Draw the truth table for the expression: Y = A\u2032 \u00b7 B + C',
       'There are three variables, so the table has 2\u00b3 = 8 rows. First invert A to get A\u2032, '
       'then AND it with B, then OR the result with C.\n'
       'A  B  C  |  A\u2032  |  A\u2032B  |  Y = A\u2032B + C\n'
       '0  0  0  |  1   |  0    |  0\n'
       '0  0  1  |  1   |  0    |  1\n'
       '0  1  0  |  1   |  1    |  1\n'
       '0  1  1  |  1   |  1    |  1\n'
       '1  0  0  |  0   |  0    |  0\n'
       '1  0  1  |  0   |  0    |  1\n'
       '1  1  0  |  0   |  0    |  0\n'
       '1  1  1  |  0   |  0    |  1',
       'Y is 1 whenever C = 1, or when A = 0 and B = 1. The only rows giving 0 are 000, 100 and 110, '
       'where C = 0 and A\u2032B = 0.', 75),
    bq(1, 'D', 'iii', 'Explain all phases of SDLC in detail with activities and deliverables.',
       '1. Requirement Gathering and Analysis \u2014 Activities: interview users, study existing '
       'systems, collect functional and non-functional requirements. Deliverable: Software '
       'Requirements Specification (SRS).\n'
       '2. Planning and Feasibility \u2014 Activities: estimate cost, schedule and resources; check '
       'technical, economic and operational feasibility; assess risks. Deliverable: project plan '
       'and feasibility report.\n'
       '3. System Design \u2014 Activities: define architecture, modules, database schema, interfaces '
       'and data flow. Deliverable: design document (architecture, ER diagrams, UI design).\n'
       '4. Implementation / Coding \u2014 Activities: write source code module by module, follow coding '
       'standards and version control. Deliverable: working source code and build.\n'
       '5. Testing \u2014 Activities: unit testing, integration testing, system testing, acceptance '
       'testing; log and fix defects. Deliverable: test plan, test cases and test report.\n'
       '6. Deployment \u2014 Activities: install the system in the production environment, migrate '
       'data, train users. Deliverable: released system and user documentation.\n'
       '7. Maintenance \u2014 Activities: fix defects, adapt to new environments, improve performance '
       'and add requested changes. Deliverable: updated releases and maintenance records.',
       'The phases are sequential in Waterfall but overlap in Agile. Each phase produces a '
       'deliverable that becomes the input to the next phase.', 75),
    bq(1, 'D', 'iv', 'Explain each layer of the OSI model in detail. For each layer, state its main '
       'function, one real-life analogy, and two protocols used.',
       '7. Application layer \u2014 provides network services directly to user applications. Analogy: '
       'a person writing a letter and deciding what to say. Protocols: HTTP/HTTPS, SMTP.\n'
       '6. Presentation layer \u2014 translates, encrypts/decrypts and compresses data. Analogy: a '
       'translator who also seals the letter in an envelope. Protocols: SSL/TLS, MIME.\n'
       '5. Session layer \u2014 establishes, manages and terminates sessions between applications. '
       'Analogy: a telephone operator who sets up and ends a call. Protocols: NetBIOS, RPC.\n'
       '4. Transport layer \u2014 provides end-to-end delivery, segmentation, flow control and error '
       'recovery. Analogy: a courier service that numbers parcels and replaces lost ones. '
       'Protocols: TCP, UDP.\n'
       '3. Network layer \u2014 logical addressing and routing of packets between networks. Analogy: '
       'the postal system choosing the route between cities. Protocols: IP, ICMP.\n'
       '2. Data Link layer \u2014 frames data, performs physical (MAC) addressing and error detection '
       'on a local link. Analogy: a local mail sorter who puts letters into the right street box. '
       'Protocols: Ethernet, PPP.\n'
       '1. Physical layer \u2014 transmits raw bits over a medium and defines voltages, cables and '
       'connectors. Analogy: the roads and vehicles that physically carry the mail. Protocols: '
       'Ethernet physical layer, RS-232.',
       'The layers are usually remembered from 7 down to 1 with "Please Do Not Throw Sausage Pizza '
       'Away". Each layer adds or removes its own header, which is encapsulation/decapsulation.', 75),
    bq(1, 'D', 'v', 'Describe the four types of software maintenance with examples.',
       '1. Corrective maintenance \u2014 fixing defects discovered after delivery. Example: patching a '
       'login bug that rejects valid passwords.\n'
       '2. Adaptive maintenance \u2014 changing software so it keeps working in a new environment '
       '(new OS, database or hardware). Example: updating an app to run on Windows 11 or a new '
       'Android version.\n'
       '3. Perfective maintenance \u2014 improving performance, maintainability or adding requested '
       'enhancements. Example: optimizing a report query so it runs in 2 seconds instead of 20.\n'
       '4. Preventive maintenance \u2014 restructuring code and updating components to prevent future '
       'failures. Example: refactoring old modules and applying security updates before a problem '
       'appears.',
       'Corrective = fix faults; adaptive = fit a changed environment; perfective = improve; '
       'preventive = avoid future faults.', 75),
]

# ---------------------------------------------------------------------------
# E. Activities — PDF 75 (book 70)
# ---------------------------------------------------------------------------
ITEMS += [
    bq(1, 'E', 1, 'Create a truth table for Y = A \u00b7 B \u00b7 C + A\u2032 \u00b7 B',
       'A  B  C  |  ABC  |  A\u2032B  |  Y\n'
       '0  0  0  |  0    |  0    |  0\n'
       '0  0  1  |  0    |  0    |  0\n'
       '0  1  0  |  0    |  1    |  1\n'
       '0  1  1  |  0    |  1    |  1\n'
       '1  0  0  |  0    |  0    |  0\n'
       '1  0  1  |  0    |  0    |  0\n'
       '1  1  0  |  0    |  0    |  0\n'
       '1  1  1  |  1    |  0    |  1\n'
       'Simplification: Y = B(A\u2032 + AC) = B(A\u2032 + C) = A\u2032B + BC.',
       'The first term ABC is 1 only in the last row. The second term A\u2032B is 1 in rows 010 and '
       '011. OR-ing them gives 1 in rows 010, 011 and 111.', 75),
    bq(1, 'E', 2, 'Design a logic circuit for a simple burglar alarm that sounds when EITHER the '
       'door OR window is opened.',
       'Let D = 1 when the door is open and W = 1 when the window is open. The alarm output is '
       'Alarm = D + W, so a two-input OR gate is used.\n'
       'Circuit: door sensor and window sensor feed the two inputs of the OR gate; the OR output '
       'drives the buzzer through a transistor/relay.\n'
       'Truth table: 00\u21920 (silent), 01\u21921, 10\u21921, 11\u21921 (alarm).',
       'EITHER/OR is exactly the OR operation. If the alarm must also sound when both are open, '
       'OR already covers that case (11 gives 1).', 75),
    bq(1, 'E', 3, 'Use an online LogiSim to verify your truth tables.',
       'Procedure: (1) open the Logisim-Evolution web/desktop simulator; (2) place the required '
       'gates (AND, OR, NOT, NAND, NOR, XOR, XNOR) and input pins; (3) connect the inputs to the '
       'gate and the output to an output pin/LED; (4) toggle every input combination and record '
       'the output; (5) compare the observed outputs with the truth table.\n'
       'Sample check for Y = A\u2032B + C: inputs 000 give 0; 001 give 1; 010 give 1; 011 give 1; '
       '100 give 0; 101 give 1; 110 give 0; 111 give 1 \u2014 the simulation matches the table.',
       'The simulator is a verification tool: matching every row confirms that the Boolean '
       'expression and the gate circuit are equivalent.', 75),
    bq(1, 'E', 4, 'Create an SRS document for a simple calculator app.',
       'A model SRS for a calculator app:\n'
       '1. Introduction \u2014 purpose: a four-function calculator for students; scope: desktop/mobile '
       'app with a numeric keypad and display.\n'
       '2. Functional requirements \u2014 FR1 accept two operands; FR2 support +, \u2212, \u00d7, \u00f7; '
       'FR3 display the result immediately; FR4 clear (C) resets the display; FR5 division by zero '
       'shows an error message instead of crashing; FR6 support decimal numbers.\n'
       '3. Non-functional requirements \u2014 NFR1 result shown within 0.2 s; NFR2 usable by a '
       'first-time user without help; NFR3 correct to at least 10 significant digits; NFR4 '
       'available on Windows and Android.\n'
       '4. Assumptions and constraints \u2014 single user, no network access, no history feature in '
       'version 1.\n'
       '5. Acceptance criteria \u2014 all FRs pass the test cases, including 5 \u00f7 0 = "Error".',
       'An SRS states WHAT the system must do (functional) and HOW WELL (non-functional), '
       'without prescribing the implementation.', 75),
    bq(1, 'E', 5, 'Draw a flowchart for a program that checks if a number is even or odd.',
       'Flowchart steps:\n'
       '(1) Start (oval).\n'
       '(2) Input N (parallelogram).\n'
       '(3) Decision (diamond): is N MOD 2 = 0?\n'
       '(4) If Yes \u2192 print "Even" (parallelogram) \u2192 Stop (oval).\n'
       '(5) If No \u2192 print "Odd" (parallelogram) \u2192 Stop (oval).\n'
       'Equivalent pseudocode: INPUT N; IF N MOD 2 = 0 THEN PRINT "Even" ELSE PRINT "Odd".',
       'MOD 2 gives the remainder after division by 2. A remainder of 0 means the number is even; '
       'otherwise it is odd.', 75),
    bq(1, 'E', 6, 'Open the command prompt (Windows) or terminal (Mac/Linux) and type: ping '
       'www.google.com. Record the results. Which OSI layer and protocol is being used? What does '
       'the output tell you about network connectivity?',
       'Model output: four replies of the form "Reply from 142.250.x.x: bytes=32 time=25ms TTL=115", '
       'followed by a summary such as "Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)" and '
       'approximate round-trip times.\n'
       'Layer/protocol: ping uses ICMP Echo Request/Reply, which operates at the Network layer '
       '(Layer 3) of the OSI model (it is carried inside IP packets).\n'
       'What it shows: successful replies prove that the local host has a working link, an IP '
       'address and route, that DNS resolved the name, and that the destination is reachable. '
       'Round-trip time measures latency; packet loss shows reliability. "Destination host '
       'unreachable" or 100% loss would indicate a connectivity problem.',
       'The exact IP addresses and times depend on the reader\'s network; the structure of the '
       'output and its interpretation are what matter.', 75),
    bq(1, 'E', 7, 'Draw a diagram showing the seven layers of the OSI model. For each layer, write '
       'its name, main function, and at least one protocol. Use the mnemonic "Please Do Not Throw '
       'Sausage Pizza Away" to help you remember the order.',
       'Layer 7 Application \u2014 user services; HTTP/HTTPS, SMTP.\n'
       'Layer 6 Presentation \u2014 translation, encryption, compression; SSL/TLS, MIME.\n'
       'Layer 5 Session \u2014 start/manage/end sessions; NetBIOS, RPC.\n'
       'Layer 4 Transport \u2014 end-to-end delivery and flow control; TCP, UDP.\n'
       'Layer 3 Network \u2014 logical addressing and routing; IP, ICMP.\n'
       'Layer 2 Data Link \u2014 framing, MAC addressing, error detection; Ethernet, PPP.\n'
       'Layer 1 Physical \u2014 transmission of raw bits; RS-232, Ethernet physical layer.\n'
       'Mnemonic: "Please Do Not Throw Sausage Pizza Away" lists the layers from 1 to 7: '
       'Physical, Data Link, Network, Transport, Session, Presentation, Application.',
       'The mnemonic lists the layers from 1 (Physical) to 7 (Application), which is the order in '
       'which data is sent and received at the two ends.', 75),
    bq(1, 'E', 8, 'Create a comparison table of TCP and UDP, listing at least five differences. For '
       'each protocol, give two examples of applications that use it and explain why.',
       'TCP vs UDP:\n'
       '1. Connection: TCP is connection-oriented (three-way handshake); UDP is connectionless.\n'
       '2. Reliability: TCP acknowledges and retransmits lost data; UDP does not guarantee delivery.\n'
       '3. Ordering: TCP delivers segments in order; UDP datagrams may arrive out of order.\n'
       '4. Speed/latency: TCP is slower with more overhead; UDP is faster with lower latency.\n'
       '5. Header size: TCP header is 20+ bytes; UDP header is 8 bytes.\n'
       '6. Flow/congestion control: TCP has both; UDP has neither.\n'
       'TCP examples: web browsing (HTTPS) needs every byte of the page correctly; email (SMTP) '
       'must not lose or reorder the message.\n'
       'UDP examples: live video/audio streaming tolerates a lost frame but not delay; online '
       'gaming needs the newest position quickly rather than an old packet retransmitted.',
       'Choose TCP when correctness and completeness matter; choose UDP when timeliness matters '
       'more than perfect delivery.', 75),
]
