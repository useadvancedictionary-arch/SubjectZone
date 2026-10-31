"""Computer Science XI — Unit 6: Digital Literacy (book 199-218)."""
from .common import bq, mcq

ITEMS = []

# A. MCQs — PDF 221-222 (book 216-217)
ITEMS += [
    mcq(6, 'A', 'i', 'Which of the following best describes digital literacy?',
        [('a', 'The ability to type quickly using a keyboard'),
         ('b', 'The ability to use digital tools to find, evaluate, create, and communicate '
               'information responsibly'),
         ('c', 'The ability to install software on a computer'),
         ('d', 'The ability to use social media for entertainment')], 'b',
        'Digital literacy is broader than typing or installing software: it includes finding and '
        'evaluating information, creating digital content, communicating responsibly and using '
        'technology safely and ethically.', 221),
    mcq(6, 'A', 'ii', 'A student asks classmates, "How does mobile phone use affect your concentration '
        'during study?" What type of data is mainly collected?',
        [('a', 'Quantitative data because it can be counted easily'),
         ('b', 'Secondary data because classmates already know the answer'),
         ('c', 'Qualitative data because it collects opinions and experiences'),
         ('d', 'Numerical data because mobile phone use is related to time')], 'c',
        'The question asks for descriptions of opinions and experiences, which are non-numerical '
        'qualitative data. Quantitative data would come from a question such as "How many minutes '
        'per day do you use your phone while studying?"', 221),
    mcq(6, 'A', 'iii', 'Which search query is most suitable for finding a reliable PDF report about '
        'internet usage in Pakistan?',
        [('a', 'internet usage Pakistan'),
         ('b', 'best internet use in Pakistan social media'),
         ('c', '"internet usage in Pakistan" filetype:pdf'),
         ('d', 'Pakistan internet all websites latest')], 'c',
        'Quotation marks force the exact phrase, and filetype:pdf restricts results to PDF '
        'documents. The other queries contain vague words that return unrelated pages.', 222),
    mcq(6, 'A', 'iv', 'Which option is the best example of primary data?',
        [('a', 'A government report downloaded from the internet'),
         ('b', 'A research article written by another author'),
         ('c', 'Survey responses collected directly from Class XI students'),
         ('d', 'Statistics copied from an online database')], 'c',
        'Primary data is collected first-hand by the researcher for the current study. Survey '
        'responses collected directly from students are original data; the other options are '
        'secondary sources compiled by someone else.', 222),
    mcq(6, 'A', 'v', 'Why are spreadsheets useful when presenting research data?',
        [('a', 'They automatically make the research question correct'),
         ('b', 'They help organize data, perform calculations, and create charts'),
         ('c', 'They replace the need for collecting original data'),
         ('d', 'They ensure all online information is reliable')], 'b',
        'A spreadsheet stores data in rows and columns, supports formulas and sorting, and can draw '
        'charts. It does not design the research or guarantee data quality by itself.', 222),
    mcq(6, 'A', 'vi', 'A digital artefact created after research should mainly:',
        [('a', 'repeat long paragraphs from websites'),
         ('b', 'communicate results and conclusions clearly'),
         ('c', 'include decoration only'),
         ('d', 'avoid any data visuals')], 'b',
        'The purpose of the artefact (slides, infographic or report) is to communicate the research '
        'question, method, findings and conclusion clearly to the intended audience.', 222),
    mcq(6, 'A', 'vii', 'Data collected directly by the researcher is called:',
        [('a', 'Secondary data'), ('b', 'Processed data'),
         ('c', 'Primary data'), ('d', 'Digital data')], 'c',
        'Primary data comes directly from the source through surveys, interviews, observations or '
        'experiments conducted by the researcher for the current purpose.', 222),
    mcq(6, 'A', 'viii', 'Which search operator helps search within a specific website or domain?',
        [('a', 'OR'), ('b', 'AND'),
         ('c', 'NOT'), ('d', 'site:')], 'd',
        'The site: operator restricts results to a domain, e.g. site:gov.pk or site:unesco.org. '
        'OR, AND and NOT combine or exclude search terms.', 222),
    mcq(6, 'A', 'ix', 'Copying someone else\'s work without giving credit is called:',
        [('a', 'Copyright'), ('b', 'Referencing'),
         ('c', 'Citation'), ('d', 'Plagiarism')], 'd',
        'Plagiarism is presenting another person\'s words, ideas or images as your own. Copyright '
        'is the legal right of the creator; citation and referencing are the correct ways to credit '
        'a source.', 222),
    mcq(6, 'A', 'x', 'Asking permission before collecting responses is part of research:',
        [('a', 'Analysis'), ('b', 'Sampling'),
         ('c', 'Presentation'), ('d', 'Ethics')], 'd',
        'Informed consent \u2014 explaining the purpose and asking permission before collecting data \u2014 '
        'is a core ethical requirement of research with human participants.', 222),
]

# B. Fill in the Blanks — PDF 222-223 (book 217-218)
ITEMS += [
    bq(6, 'B', 'i', 'A well-defined ____________ helps a student choose suitable data-collection '
       'methods and stay focused during research.',
       'research question',
       'A focused research question states exactly what is being investigated; it determines the '
       'sample, the method and the analysis.', 222),
    bq(6, 'B', 'ii', 'Data collected directly by the researcher through surveys, interviews or '
       'observation is called ____________ data.',
       'primary',
       'Primary data is original, first-hand data gathered for the current study.', 222),
    bq(6, 'B', 'iii', 'Data taken from reports, books, websites or databases prepared by others is '
       'called ____________ data.',
       'secondary',
       'Secondary data was collected by someone else and is reused for a new purpose; it must be '
       'checked for reliability and currency.', 223),
    bq(6, 'B', 'iv', 'Copying words, images or ideas without giving credit is called ____________.',
       'plagiarism',
       'Plagiarism is the use of another person\'s work without acknowledgement. It can be avoided '
       'by quoting and citing the source properly.', 223),
    bq(6, 'B', 'v', 'Asking permission before collecting responses is part of research ____________.',
       'ethics',
       'Research ethics requires informed consent, confidentiality, voluntary participation and '
       'honest reporting.', 223),
]

# C. Short answers — PDF 223 (book 218)
ITEMS += [
    bq(6, 'C', 'i', 'What is primary data? Give one example.',
       'Primary data is original, first-hand data collected by the researcher specifically for the '
       'current study, using methods such as surveys, interviews, observations or experiments.\n'
       'Example: a student prepares a questionnaire and collects answers from 30 classmates about '
       'their daily study hours. Those responses are primary data because the student collected '
       'them directly.',
       'Primary data is fresh and controlled by the researcher, but collecting it takes time and '
       'effort.', 223),
    bq(6, 'C', 'ii', 'What is secondary data? Give one example.',
       'Secondary data is information that was collected and published by someone else, then reused '
       'for a new purpose.\n'
       'Example: using the Pakistan Bureau of Statistics report on internet subscribers to study '
       'internet use in your city. The data was collected by the bureau, not by the student.\n'
       'Secondary data is quick and often large-scale, but the researcher must check its source, '
       'date and reliability.',
       'Primary = first-hand; secondary = someone else\'s published data.', 223),
    bq(6, 'C', 'iii', 'What is plagiarism and why should it be avoided?',
       'Plagiarism is presenting another person\'s words, ideas, data, images or code as your own '
       'without acknowledgement, whether copied directly or paraphrased closely.\n'
       'It should be avoided because:\n'
       '\u2022 it is dishonest and misrepresents who did the work;\n'
       '\u2022 it violates academic integrity rules and can lead to failing a subject or losing marks;\n'
       '\u2022 it is an academic and ethical offence; if the copied work is protected by copyright, '
       'copying it without permission may also amount to copyright infringement (the two concepts are '
       'related but not identical);\n'
       '\u2022 it stops the student from developing real understanding and skills;\n'
       '\u2022 it damages the trust of teachers and future employers.\n'
       'Avoid it by quoting and citing sources, keeping notes of where information came from, and '
       'writing in your own words.',
       'Plagiarism is an ethical and academic offence, not just a formatting mistake; citation is '
       'the correct way to use other people\'s work.', 223),
    bq(6, 'C', 'iv', 'What is meant by data privacy?',
       'Data privacy is the right and ability of a person to control how their personal information '
       '(name, address, phone number, health or financial data) is collected, used, shared and '
       'stored.\n'
       'Privacy requires that data is collected with consent, used only for the stated purpose, '
       'protected from unauthorized access and deleted when no longer needed. For example, a school '
       'should not publish students\' phone numbers or share their records with advertisers without '
       'permission.',
       'Privacy is about who can see and use personal data; security is about protecting it from '
       'unauthorized access.', 223),
    bq(6, 'C', 'v', 'Write any three ways to protect personal information while using digital '
       'technologies.',
       '1. Use strong, unique passwords for each account and enable two-factor authentication; '
       'never share passwords.\n'
       '2. Limit what you share on social media and check privacy settings so only trusted people '
       'can see your posts.\n'
       '3. Avoid clicking unknown links or downloading attachments from unknown senders, and install '
       'updates/antivirus to prevent phishing and malware.\n'
       'Other valid answers: use a passcode on the phone, log out on shared computers, avoid public '
       'Wi-Fi for banking, review app permissions.',
       'Three concrete habits are enough; each should reduce the chance of unauthorized access or '
       'oversharing.', 223),
]

# D. Detailed answers — PDF 223 (book 218)
ITEMS += [
    bq(6, 'D', 'i', 'Explain the concept of digital literacy. Why is it necessary for students in '
       'modern education?',
       'Digital literacy is the ability to use digital tools and networks to find, evaluate, create, '
       'manage and communicate information responsibly and safely. It combines technical skills '
       '(using devices and software) with critical thinking (judging the reliability of information) '
       'and ethical behaviour (privacy, consent, citation, respectful communication).\n'
       'It includes:\n'
       '\u2022 finding information with effective search strategies;\n'
       '\u2022 evaluating sources for authority, accuracy, currency and bias;\n'
       '\u2022 creating content with word processors, spreadsheets, presentations and media tools;\n'
       '\u2022 communicating and collaborating online;\n'
       '\u2022 protecting privacy and security;\n'
       '\u2022 using technology ethically and legally.\n'
       'Why students need it:\n'
       '1. Learning materials are increasingly online; students must find and judge them.\n'
       '2. Assignments require research, data handling and digital presentation.\n'
       '3. Misinformation spreads quickly; critical evaluation protects students from false claims.\n'
       '4. Online safety \u2014 students must protect their data and recognize phishing and scams.\n'
       '5. Future employment requires digital collaboration and productivity tools.\n'
       '6. Responsible citizenship includes respectful online communication and respect for '
       'copyright.',
       'Digital literacy is not just knowing which button to press; it is the ability to use '
       'digital information wisely, safely and ethically.', 223),
    bq(6, 'D', 'ii', 'Describe the difference between qualitative and quantitative data with suitable '
       'examples.',
       'Quantitative data is numerical and can be counted or measured; it answers "how many" or '
       '"how much" and can be analysed with statistics.\n'
       'Examples: the number of hours students study per day (2.5 hours), the marks obtained in a '
       'test (75/100), the number of students in a class (40), the percentage of households with '
       'internet (54%).\n'
       'Qualitative data is non-numerical and describes qualities, opinions, experiences or '
       'categories; it answers "why" or "how" and is analysed by grouping themes.\n'
       'Examples: a student\'s description of how phone notifications affect concentration, '
       'interview answers about study habits, the colour of a product, the reasons a student chose '
       'a subject.\n'
       'Comparison:\n'
       'Quantitative \u2014 numbers, measurable, objective, statistically analysable, often from closed '
       'questions.\n'
       'Qualitative \u2014 words/images, descriptive, subjective, rich in detail, often from open '
       'questions and interviews.\n'
       'Mixed methods combine both: a survey can ask "How many hours do you study?" (quantitative) '
       'and "How do you feel about your study routine?" (qualitative).',
       'The type of question determines the data type: closed/numeric questions produce '
       'quantitative data; open questions produce qualitative data.', 223),
    bq(6, 'D', 'iii', 'Explain any four data-collection strategies: interviews, surveys, prototypes, '
       'observations, and simulations.',
       '1. Interviews \u2014 a conversation with a person who has relevant knowledge, using prepared '
       'open questions. They give detailed explanations and allow follow-up questions. Example: '
       'interviewing the class teacher about why students lose concentration. Limitation: time-'
       'consuming and a small sample.\n'
       '2. Surveys \u2014 a set of written/online questions given to many respondents, often with '
       'closed options. They are efficient for large samples and easy to quantify. Example: a Google '
       'Form asking 100 students about daily phone use. Limitation: shallow answers and response '
       'bias.\n'
       '3. Prototypes \u2014 a simple working model of a product or interface tested with users. They '
       'reveal usability problems early. Example: a paper or Figma mock-up of a study-planner app '
       'tested by five students. Limitation: a prototype is not the final product.\n'
       '4. Observations \u2014 watching and recording behaviour in its natural setting without '
       'interfering. They capture what people actually do rather than what they say. Example: '
       'observing how often students check their phones during a study period. Limitation: an '
       'observer effect and subjective recording.\n'
       '5. Simulations \u2014 using a model (software or mathematical) to imitate a real system and '
       'test scenarios safely. Example: simulating traffic flow with different signal timings. '
       'Limitation: the results depend on the assumptions of the model.',
       'The choice depends on the research question, the sample size, the time available and whether '
       'the study needs numbers, explanations, usability evidence or controlled experiments.', 223),
    bq(6, 'D', 'iv', 'Describe the steps involved in designing a data-collection approach for a '
       'research question.',
       '1. Define the research question precisely \u2014 what exactly do you want to find out, and for '
       'whom? A focused question such as "How does phone use during study affect concentration among '
       'Class XI students?" is better than "phones are bad".\n'
       '2. Identify the variables and the data type \u2014 decide which factors to measure '
       '(quantitative) and which experiences to describe (qualitative).\n'
       '3. Choose the population and sample \u2014 who can answer the question, how many, and how they '
       'will be selected (random, stratified, convenience).\n'
       '4. Choose the method(s) \u2014 survey, interview, observation, prototype testing or simulation, '
       'and justify the choice.\n'
       '5. Design the instrument \u2014 write clear, unbiased questions; choose closed/open formats; '
       'pilot-test with a few people and revise confusing items.\n'
       '6. Plan ethics \u2014 explain the purpose, obtain informed consent, guarantee anonymity and '
       'confidentiality, and allow participants to withdraw.\n'
       '7. Plan the logistics \u2014 timeline, permissions, tools (Google Forms, spreadsheet), and how '
       'data will be stored securely.\n'
       '8. Plan the analysis and presentation in advance \u2014 decide which tables, averages or charts '
       'will answer the question, so the collected data is usable.\n'
       '9. Collect, clean and check the data \u2014 remove duplicates, handle missing values and record '
       'any limitations.',
       'Planning the analysis before collecting data prevents the common problem of collecting data '
       'that cannot answer the question.', 223),
    bq(6, 'D', 'v', 'Explain how spreadsheets, presentations, infographics, and reports can be used '
       'to communicate research findings.',
       '1. Spreadsheets \u2014 organize raw data in rows and columns, clean it, compute totals, '
       'averages and percentages with formulas, sort/filter it, and create charts. They are the '
       'working tool behind the findings and allow the reader to check the calculations. Example: a '
       'sheet of 30 survey responses with an AVERAGE formula and a bar chart of responses by class.\n'
       '2. Presentations \u2014 a sequence of slides for a live audience: title, research question, '
       'method, key findings, conclusion and recommendations. Slides should use short points and '
       'one clear visual per idea, not long paragraphs. Example: a 5-slide deck summarizing a study '
       'of phone use during study.\n'
       '3. Infographics \u2014 a single visual page combining charts, icons and short text to explain '
       'the main finding at a glance. They are effective for posters, social media and notice '
       'boards. Example: a poster showing "62% of students check their phone within 10 minutes of '
       'studying".\n'
       '4. Reports \u2014 a written document with introduction, methodology, results, discussion, '
       'conclusion and references. Reports provide the full detail and evidence for readers who need '
       'to verify or reuse the work. Example: a 4-page report with tables, charts and citations.\n'
       'Choosing the format: presentations for a live audience, infographics for quick public '
       'communication, reports for detailed academic records, and spreadsheets as the underlying '
       'data source.',
       'All four formats should present the same findings consistently; the difference is the '
       'audience and the level of detail.', 223),
]

# E. Activities — PDF 223 (book 218)
ITEMS += [
    bq(6, 'E', 1, 'In groups of 3-4 students, choose a topic such as smartphone use in college, '
       'online learning during examinations, or internet habits of students.',
       'Model plan: Topic \u2014 "Smartphone use during study time among Class XI students".\n'
       'Group roles: leader (coordinates), questionnaire designer, data collector, analyst/'
       'presenter.\n'
       'Scope: 30 students from the class, one week of data collection.\n'
       'Output: a short research plan stating the topic, the group members\' roles, the target '
       'participants and the timeline.',
       'Any of the suggested topics is acceptable; the group should state a narrow topic and divide '
       'the work.', 223),
    bq(6, 'E', 2, 'Form a clear research question, identify your target sample, and design a survey '
       'or interview with at least 8 questions. Make sure the wording is fair, clear, and ethical.',
       'Research question: "How does smartphone use during study affect the concentration of Class '
       'XI students?"\n'
       'Target sample: 30 Class XI students, mixed genders, selected randomly from two sections.\n'
       'Survey (8 questions):\n'
       '1. How many minutes per day do you use your phone while studying? (0-30 / 31-60 / 61-120 / more than 120)\n'
       '2. Do you keep notifications on while studying? (always / sometimes / never)\n'
       '3. How often do you check your phone during a 30-minute study session? (0 / 1-2 / 3-5 / more than 5)\n'
       '4. On a scale of 1-5, how much does phone use disturb your concentration?\n'
       '5. What do you usually do on the phone during study breaks? (open answer)\n'
       '6. Do you study better with the phone in another room? (yes / no / not sure)\n'
       '7. How many hours do you sleep on average? (less than 6 / 6-7 / 7-8 / more than 8)\n'
       '8. Is there anything else you would like to share about phone use and study? (open answer)\n'
       'Ethics: participation is voluntary and anonymous; no names are recorded; responses are used '
       'only for this class project; consent is asked at the start.',
       'Questions should be neutral (not leading), one idea per question, and include a consent '
       'statement.', 223),
    bq(6, 'E', 3, 'Collect responses from at least 20 students, enter the data into a spreadsheet, '
       'clean the data, and create at least one table and one chart or infographic.',
       'Procedure:\n'
       '1. Collect 20+ responses (paper or Google Form).\n'
       '2. Enter each response as one row; put question numbers as column headings.\n'
       '3. Clean: remove duplicate entries, correct out-of-range values (e.g. 300 minutes), decide '
       'how to handle blank answers.\n'
       '4. Table: response count and percentage for each option of Questions 1-3.\n'
       '5. Chart: a bar chart of minutes-per-day categories and a pie chart of notification use.\n'
       'Sample table:\n'
       'Daily phone use while studying | Students | Percentage\n'
       '0-30 min | 6 | 30%\n'
       '31-60 min | 9 | 45%\n'
       '61-120 min | 4 | 20%\n'
       'More than 120 min | 1 | 5%\n'
       'The chart is created with Insert > Chart in the spreadsheet and labelled with a title, axis '
       'labels and a data source note.',
       'The sample numbers are illustrative; the student\'s own collected data must be used in the '
       'actual project.', 223),
    bq(6, 'E', 4, 'Prepare a short digital artefact (3-5 slides, infographic, or brief report) that '
       'presents findings, conclusions, the reliability of any secondary sources used, and one '
       'recommendation for the intended audience.',
       'Model artefact outline (4 slides):\n'
       'Slide 1 \u2014 Title, research question and sample: "Smartphone use during study \u2014 survey of '
       '30 Class XI students".\n'
       'Slide 2 \u2014 Method and data: anonymous survey, 8 questions, 30 responses; one bar chart of '
       'daily phone use and one pie chart of notification habits.\n'
       'Slide 3 \u2014 Findings and conclusion: most students (45%) use the phone 31-60 minutes while '
       'studying; students who keep notifications on report more distraction; conclusion \u2014 phone '
       'use is associated with reduced concentration.\n'
       'Slide 4 \u2014 Reliability and recommendation: the survey is primary data but the sample is '
       'small and from one class, so results cannot be generalized; a government report (secondary '
       'source) was used only for background and was checked for date and publisher. Recommendation: '
       'students should keep phones in another room or turn on focus mode during study.',
       'The artefact must connect question \u2192 method \u2192 findings \u2192 conclusion \u2192 recommendation, and '
       'state the limitations of the data.', 223),
]
