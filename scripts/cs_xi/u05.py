"""Computer Science XI — Unit 5: Applications and Impacts of Computing (book 174-198)."""
from .common import bq, mcq

ITEMS = []

# A. MCQs — PDF 201-202 (book 196-197)
ITEMS += [
    mcq(5, 'A', 'i', 'A smartwatch records heart rate and sends it to a mobile phone. Which technology '
        'is mainly used here?',
        [('a', 'Word Processing'), ('b', 'Internet of Things'),
         ('c', 'Printing Technology'), ('d', 'Analog Technology')], 'b',
        'The watch contains a sensor, a processor and a wireless connection; it gathers data and '
        'sends it to another device over a network. That network of physical devices with sensors '
        'and connectivity is the Internet of Things (IoT).', 201),
    mcq(5, 'A', 'ii', 'In a smart irrigation system, which device checks whether the soil is dry or wet?',
        [('a', 'Actuator'), ('b', 'Sensor'),
         ('c', 'Monitor'), ('d', 'Smart hearing aid')], 'b',
        'A soil-moisture sensor measures the water content of the soil and sends the reading to the '
        'controller. An actuator (e.g. a valve) would take the action after the decision is made.', 201),
    mcq(5, 'A', 'iii', 'A school removes duplicate student records while preparing examination results. '
        'Which step of Data Analytics is this?',
        [('a', 'Data collection'), ('b', 'Data visualization'),
         ('c', 'Data cleaning'), ('d', 'Data storage')], 'c',
        'Removing duplicates, missing values and incorrect entries is data cleaning (data wrangling), '
        'which happens before analysis so the results are trustworthy.', 202),
    mcq(5, 'A', 'iv', 'Which of the following is a primary source of information?',
        [('a', 'Textbook'), ('b', 'Interview'),
         ('c', 'Dictionary'), ('d', 'Summary website')], 'b',
        'A primary source is original, first-hand evidence: an interview, survey, experiment or '
        'observation. Textbooks, dictionaries and summary websites compile or interpret other '
        'sources, so they are secondary or tertiary.', 202),
    mcq(5, 'A', 'v', 'A student uses an unknown website without an author name or references. This '
        'source is likely to be:',
        [('a', 'Reliable'), ('b', 'Primary'),
         ('c', 'Unreliable'), ('d', 'Official')], 'c',
        'Missing authorship, missing references and an unknown publisher make it impossible to '
        'verify the information, so the source should be treated as unreliable until corroborated '
        'by a trustworthy source.', 202),
    mcq(5, 'A', 'vi', 'Which technology supports people with hearing, vision, learning, or movement '
        'difficulties?',
        [('a', 'Gaming technology'), ('b', 'Manufacturing technology'),
         ('c', 'Assistive technology'), ('d', 'Antivirus technology')], 'c',
        'Assistive technology is designed to remove barriers for people with disabilities: screen '
        'readers, hearing aids, speech-to-text tools, screen magnifiers and specialised input '
        'devices.', 202),
    mcq(5, 'A', 'vii', 'Which of the following is an actuator in a smart water system?',
        [('a', 'Soil moisture sensor'), ('b', 'Water valve'),
         ('c', 'Temperature sensor'), ('d', 'Camera sensor')], 'b',
        'A valve performs a physical action (opening or closing the water flow), which is the role '
        'of an actuator. The other three are sensors that measure conditions.', 202),
    mcq(5, 'A', 'viii', 'Which type of source usually provides summarized information for quick reference?',
        [('a', 'Primary source'), ('b', 'Secondary source'),
         ('c', 'Tertiary source'), ('d', 'Unverified source')], 'c',
        'Tertiary sources compile and summarize primary and secondary material for quick reference: '
        'encyclopedias, dictionaries, handbooks, indexes and databases.', 202),
    mcq(5, 'A', 'ix', 'Which method is used to present data through charts and graphs?',
        [('a', 'Data collection'), ('b', 'Data storage'),
         ('c', 'Data cleaning'), ('d', 'Data visualization')], 'd',
        'Data visualization presents data graphically (bar, line and pie charts, dashboards) so '
        'patterns and comparisons are easier to understand.', 202),
    mcq(5, 'A', 'x', 'Which assistive technology converts on-screen text into speech?',
        [('a', 'Screen reader'), ('b', 'Smart meter'),
         ('c', 'Motion sensor'), ('d', 'Water pump')], 'a',
        'A screen reader reads the text and interface of the screen aloud with a synthesized voice, '
        'helping users with visual impairments.', 202),
]

# B. Fill in the Blanks — PDF 202 (book 197)
ITEMS += [
    bq(5, 'B', 'i', 'A ____________ detects changes such as temperature, movement, light, or soil moisture.',
       'sensor',
       'A sensor converts a physical condition (temperature, motion, light, moisture) into an '
       'electrical signal that a controller can process.', 202),
    bq(5, 'B', 'ii', 'An ____________ performs a physical action, such as opening a valve or switching '
       'on a fan.',
       'actuator',
       'An actuator converts an electrical command into physical movement or action \u2014 a motor, '
       'valve, relay, fan or pump.', 202),
    bq(5, 'B', 'iii', 'Correcting duplicate, missing, or incorrect records is called data ____________.',
       'cleaning (cleansing / wrangling)',
       'Data cleaning removes or corrects duplicates, missing values, inconsistent formats and '
       'outliers before analysis.', 202),
    bq(5, 'B', 'iv', 'An interview is an example of a ____________ source of information.',
       'primary',
       'An interview collects original, first-hand information directly from a person who '
       'experienced or knows the situation.', 202),
    bq(5, 'B', 'v', 'Screen readers and hearing aids are examples of ____________ technologies.',
       'assistive',
       'Assistive technologies help people with disabilities perform tasks and access information '
       'independently.', 202),
]

# C. Short answers — PDF 203 (book 198)
ITEMS += [
    bq(5, 'C', 'i', 'How does Artificial Intelligence help a mobile phone recognize a user\'s face?',
       'The phone\'s camera captures the face, and an AI model trained on many face images converts '
       'the image into a mathematical pattern (facial features/embeddings). It compares that '
       'pattern with the stored pattern of the authorized user and accepts the match above a '
       'confidence threshold.\n'
       'The model also adapts to changes such as glasses or a beard. Liveness checks (blink, depth) '
       'help prevent a photograph from unlocking the phone.',
       'Face recognition is a machine-learning/computer-vision application: it learns features from '
       'examples rather than following hand-written rules for every face.', 203),
    bq(5, 'C', 'ii', 'What is the difference between a sensor and an actuator?',
       'A sensor is an input device: it measures a physical condition (temperature, light, motion, '
       'moisture) and converts it into a signal for the controller.\n'
       'An actuator is an output device: it converts a control signal into a physical action, such '
       'as opening a valve, starting a motor or switching a fan.\n'
       'Example in smart irrigation: the soil-moisture sensor measures how dry the soil is; the '
       'water valve (actuator) opens to let water flow when the reading is below the threshold.',
       'Sensor = sense/measure (input); actuator = act/move (output).', 203),
    bq(5, 'C', 'iii', 'How does cloud computing support students and teachers in Pakistan?',
       'Cloud computing provides storage and software over the internet instead of on local '
       'machines. For students it enables access to notes, videos and assignments from any device, '
       'online classes, and collaboration on shared documents; work is not lost if a device breaks.\n'
       'For teachers it supports uploading learning material, online quizzes and automatic marking, '
       'sharing results with parents, and teaching remotely, which is especially valuable where '
       'schools are far apart or during disruptions.\n'
       'In Pakistan, services such as Google Classroom, MS Teams and cloud drives are widely used; '
       'the main requirements are affordable internet and electricity.',
       'The benefits are access anywhere, low upfront cost, easy collaboration and backup; the '
       'challenges are connectivity, data cost and power outages.', 203),
    bq(5, 'C', 'iv', 'What problems can occur if people become over-dependent on technology?',
       'Over-dependence can cause:\n'
       '\u2022 loss of basic skills \u2014 inability to calculate, navigate or write without a device;\n'
       '\u2022 health problems \u2014 eye strain, poor posture, reduced physical activity and sleep loss;\n'
       '\u2022 social isolation \u2014 less face-to-face interaction and weaker communication skills;\n'
       '\u2022 reduced attention and increased distraction from notifications and short videos;\n'
       '\u2022 privacy and security risks from sharing too much data;\n'
       '\u2022 vulnerability when systems fail \u2014 no power, no internet or a cyberattack stops work;\n'
       '\u2022 job displacement and economic dependence on a few platforms.\n'
       'Responsible use means balancing technology with offline activity, verifying information and '
       'keeping essential skills.',
       'Technology is a tool; over-dependence turns it into a single point of failure and can harm '
       'health, skills and privacy.', 203),
    bq(5, 'C', 'v', 'Why are communication and problem-solving skills important for future computing '
       'careers?',
       'Computing work is collaborative and client-facing. Communication skills are needed to '
       'gather requirements, explain technical choices to non-technical users, write documentation '
       'and work in a team; unclear communication causes costly misunderstandings.\n'
       'Problem-solving skills are needed because programs fail, requirements change and new '
       'problems appear. A developer must analyse the problem, break it into parts, compare '
       'solutions, test them and debug under pressure.\n'
       'Together they turn technical knowledge into working solutions that people can actually use.',
       'Technical skill alone is not enough: careers progress fastest for people who can understand '
       'a problem, communicate a solution and work with others.', 203),
]

# D. Detailed answers — PDF 203 (book 198)
ITEMS += [
    bq(5, 'D', 'i', 'Explain how IoT components work together in a smart irrigation system for a '
       'farmer in Sindh. Include sensors, actuators, connectivity, data processing, and user '
       'interface in your answer.',
       'A smart irrigation system decides when and how much to water based on measurements rather '
       'than a fixed timetable.\n'
       '1. Sensors \u2014 soil-moisture sensors placed in the field measure water content; temperature '
       'and humidity sensors measure evaporation conditions. They send readings continuously.\n'
       '2. Connectivity \u2014 the controller sends the readings over a mobile network (GSM/4G) or '
       'Wi-Fi/LoRa to a cloud service. This lets the farmer monitor fields that are far from home.\n'
       '3. Data processing \u2014 the cloud/controller compares moisture with the crop\'s threshold, '
       'checks the weather forecast and decides whether irrigation is needed. It can log history and '
       'detect a faulty sensor.\n'
       '4. Actuators \u2014 if the soil is too dry, the controller opens the water valve or starts the '
       'pump for a calculated time, then closes it. This saves water and fuel/electricity.\n'
       '5. User interface \u2014 a mobile app or SMS dashboard shows moisture levels, valve status and '
       'alerts; the farmer can start or stop irrigation manually from anywhere.\n'
       'Benefits in Sindh: water saving in a water-scarce province, less labour, healthier crops and '
       'early warning of dry conditions or leaks. Challenges: connectivity, power and maintenance.',
       'The loop is: sense \u2192 transmit \u2192 decide \u2192 act \u2192 report. Each component has one role, and the '
       'farmer remains in control through the interface.', 203),
    bq(5, 'D', 'ii', 'A college wants to improve its examination result system. Explain how Data '
       'Analytics can help from data collection to data visualization.',
       '1. Define the question \u2014 e.g. which subjects/classes need attention, and what factors '
       'affect results.\n'
       '2. Data collection \u2014 gather marks from teachers, attendance records, internal assessment '
       'and student details, in a consistent format (spreadsheet/database).\n'
       '3. Data cleaning \u2014 remove duplicate students, correct missing or out-of-range marks and '
       'standardize names/classes so the analysis is reliable.\n'
       '4. Data storage \u2014 keep the cleaned data in a database or spreadsheet with backups and '
       'access control.\n'
       '5. Analysis \u2014 calculate pass rates, averages, subject-wise and class-wise comparisons, and '
       'correlations (e.g. attendance vs marks); identify weak subjects and at-risk students.\n'
       '6. Visualization \u2014 present the results as bar charts of pass rate by subject, line charts of '
       'performance over terms, and pie charts of grade distribution.\n'
       '7. Action \u2014 the college uses the findings to arrange remedial classes, train teachers and '
       'counsel students, then repeats the cycle next term.',
       'Analytics converts raw marks into decisions: collect \u2192 clean \u2192 store \u2192 analyse \u2192 visualize \u2192 '
       'act.', 203),
    bq(5, 'D', 'iii', 'A student finds information from a social media post and an official government '
       'website. Explain how the student should decide which source is more reliable.',
       'The student should evaluate both sources using standard criteria:\n'
       '1. Authorship \u2014 who created it? An official government website names the department and '
       'publisher; a social media post may be anonymous or a personal opinion.\n'
       '2. Authority \u2014 is the publisher responsible for this information? A government department '
       'is authoritative for official statistics; a random account is not.\n'
       '3. Accuracy and evidence \u2014 are references, data and dates provided? Official sites usually '
       'publish reports and methodology; posts often lack sources.\n'
       '4. Currency \u2014 is the information up to date? Check the publication/update date.\n'
       '5. Objectivity \u2014 is it factual or persuasive/emotional? Social posts may be designed to '
       'spread quickly rather than to be accurate.\n'
       '6. Verification \u2014 can the claim be confirmed by an independent trustworthy source '
       '(another government site, a reputable news organisation, a textbook)?\n'
       '7. Purpose and audience \u2014 was it written to inform or to attract likes?\n'
       'Conclusion: the official government website is more reliable, but the student should still '
       'check the date and confirm key figures with a second official source. The social post can '
       'be used only as a lead to investigate.',
       'Reliability is judged by authority, evidence, currency, objectivity and independent '
       'verification \u2014 not by how many people shared the post.', 203),
    bq(5, 'D', 'iv', 'Analyze the positive and negative impacts of computing.',
       'Positive impacts:\n'
       '\u2022 Communication \u2014 instant messaging, video calls and email connect people across distances.\n'
       '\u2022 Education \u2014 online resources, simulations and remote classes widen access.\n'
       '\u2022 Healthcare \u2014 digital records, diagnostic imaging and telemedicine improve care.\n'
       '\u2022 Business and employment \u2014 e-commerce, banking and remote work create opportunities.\n'
       '\u2022 Efficiency and accuracy \u2014 automation performs repetitive work faster and with fewer errors.\n'
       '\u2022 Agriculture and industry \u2014 IoT and data analytics improve yields and reduce waste.\n'
       'Negative impacts:\n'
       '\u2022 Privacy \u2014 personal data can be collected, leaked or misused.\n'
       '\u2022 Security \u2014 hacking, malware, fraud and identity theft.\n'
       '\u2022 Screen time and health \u2014 eye strain, poor posture, less exercise and sleep problems.\n'
       '\u2022 Social isolation and misinformation \u2014 shallow online interaction and rapid spread of fake news.\n'
       '\u2022 Job displacement \u2014 automation removes some roles and demands new skills.\n'
       '\u2022 Digital divide \u2014 unequal access to devices, internet and electricity.\n'
       '\u2022 Environmental cost \u2014 energy use of data centres and electronic waste.\n'
       'Balanced conclusion: computing brings large benefits, but responsible use requires privacy '
       'protection, security awareness, digital skills and regulation.',
       'The same technology can help or harm depending on how it is used and who controls it; the '
       'task is to maximize benefits while managing the risks.', 203),
    bq(5, 'D', 'v', 'Discuss the career opportunities related to AI, IoT, Data Analytics, and '
       'Assistive Technologies in Pakistan. What skills should students develop for these careers?',
       'AI careers \u2014 machine-learning engineer, data scientist, computer-vision engineer, NLP '
       'engineer, AI product manager. In Pakistan, AI is used in fintech (fraud detection), '
       'telecom (customer support chatbots), agriculture (crop diagnosis) and healthcare imaging.\n'
       'IoT careers \u2014 embedded-systems engineer, IoT solutions architect, firmware developer, '
       'network/automation engineer. Opportunities exist in smart agriculture, smart metering, '
       'industrial automation and home security.\n'
       'Data Analytics careers \u2014 data analyst, business-intelligence analyst, database '
       'administrator, data engineer. Banks, telecoms, retailers, hospitals and government '
       'departments need analysts to turn data into decisions.\n'
       'Assistive Technology careers \u2014 accessibility specialist, assistive-technology developer, '
       'rehabilitation engineer, UX designer for accessibility. There is growing demand in schools, '
       'hospitals and NGOs serving people with disabilities.\n'
       'Skills to develop:\n'
       '\u2022 programming (Python, JavaScript/C++), data structures and algorithms;\n'
       '\u2022 mathematics and statistics for AI/analytics;\n'
       '\u2022 databases and SQL, spreadsheets and data visualization;\n'
       '\u2022 electronics and networking basics for IoT;\n'
       '\u2022 cloud platforms, version control (Git) and cybersecurity awareness;\n'
       '\u2022 communication, teamwork, problem-solving and English writing;\n'
       '\u2022 domain knowledge (agriculture, health, education) and a portfolio of real projects.',
       'The careers overlap: all four need programming, data literacy and problem-solving; the '
       'differences are in the domain and the tools.', 203),
]

# E. Activities — PDF 203 (book 198)
ITEMS += [
    bq(5, 'E', 1, 'Think of one smart device used in your home, school, or community. Does it use AI, '
       'IoT, or Data Analytics? Explain your answer in two or three sentences.',
       'Model answer (smart LED bulb / smart TV / smart meter): A smart bulb uses IoT. The phone app '
       'sends commands over Wi-Fi to a small controller in the bulb, which switches the LED and '
       'reports its status back to the app. It may also use simple automation rules (turn on at '
       'sunset), but it does not learn from data, so it is mainly IoT rather than AI or analytics.',
       'Name the device, identify the sensing/connectivity/control parts, and justify which of AI, '
       'IoT or analytics is the main technology.', 203),
    bq(5, 'E', 2, 'Which smart city application is most needed in your city or town? Write one '
       'reason for your answer.',
       'Model answer: A smart traffic-management system is most needed in Karachi. Sensors and '
       'cameras at intersections would measure traffic density and adjust signal timing, reducing '
       'congestion and fuel waste during peak hours, while an app could tell drivers which routes '
       'are blocked.\n'
       'Other acceptable answers: smart water metering (reduce losses), smart waste collection '
       '(full-bin sensors), smart street lighting (save electricity), air-quality monitoring.',
       'Any application is acceptable if it names the city problem and gives a concrete reason why '
       'the technology helps.', 203),
    bq(5, 'E', 3, 'Think about a farming problem in Pakistan. How can IoT help solve it?',
       'Problem: water scarcity and uneven irrigation in Sindh/Punjab.\n'
       'IoT solution: soil-moisture sensors in each field send readings to a controller. When the '
       'soil is dry, the controller opens the valve for a measured time; when it is wet enough, the '
       'valve stays closed. A weather feed can skip irrigation before rain. The farmer sees the '
       'status and alerts on a mobile app and can control the pump remotely.\n'
       'Result: less water and fuel used, healthier crops, and evidence of how much water each field '
       'received.',
       'A good answer names a specific problem, lists the sensor \u2192 decision \u2192 actuator \u2192 app chain, '
       'and states the benefit.', 203),
    bq(5, 'E', 4, 'Choose one career from IoT or AI. Write two reasons why this career interests you '
       'and list three skills required for it.',
       'Model answer \u2014 IoT engineer:\n'
       'Reasons: (1) I enjoy building things that interact with the real world, such as sensors and '
       'automated machines; (2) IoT can solve practical problems in agriculture and energy in '
       'Pakistan, so the work has visible impact.\n'
       'Three skills: (1) programming in C/C++ or Python for microcontrollers; (2) basic electronics '
       'and networking (sensors, Wi-Fi, MQTT); (3) problem-solving and debugging of hardware-software '
       'systems.',
       'The reasons should be personal and specific; the skills should match the chosen career.', 203),
    bq(5, 'E', 5, 'Do you enjoy reading, writing, checking facts, or organizing information? Choose '
       'one career from this section and explain why it may be suitable for you.',
       'Model answer \u2014 data analyst (for a student who enjoys organizing information and checking '
       'facts): A data analyst collects and cleans data, looks for patterns and explains them with '
       'charts and reports. The work suits someone who likes accuracy, enjoys finding the story in '
       'numbers and can explain results clearly to others. The habit of checking facts is directly '
       'useful because unreliable data leads to wrong decisions.',
       'There is no single correct career; the answer should connect the student\'s interests to the '
       'daily tasks of the chosen role.', 203),
    bq(5, 'E', 6, 'Write one positive and one negative impact of computing that you have observed in '
       'your daily life.',
       'Model answer: Positive \u2014 online classes and shared class notes let me study even when '
       'school is closed, and I can ask a teacher a question instantly. Negative \u2014 notifications '
       'and short videos break my concentration while studying, and I sometimes spend much longer on '
       'the phone than I intended.',
       'Both impacts must be specific and observed, not general statements copied from the text.', 203),
    bq(5, 'E', 7, 'Identify one assistive technology used in schools or hospitals. Write how it helps '
       'people and which career is related to it.',
       'Model answer: A screen reader used in a school computer lab. It converts on-screen text into '
       'speech so a student with a visual impairment can read lessons, browse the web and write '
       'documents independently.\n'
       'Related careers: accessibility specialist / assistive-technology developer, who tests '
       'software with screen readers, adds labels and keyboard navigation, and designs interfaces '
       'that work for everyone.',
       'The answer should name a real assistive device, state the barrier it removes and link it to '
       'a career that builds or supports it.', 203),
]
