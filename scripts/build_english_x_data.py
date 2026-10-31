#!/usr/bin/env python3
"""Builds public/data/class_x_english.json for the SubjectZone app.

Secondary Stage English Book Two for Class X (Sindh Textbook Board, Jamshoro):
6 units covering Reading Comprehension, Oral Communication, Language Practice,
Writing, Study Skills, and Fun activities.
Scanned PDF — no extractable text; solutions written from rendered page images.
Book page = PDF page - 4 (4 pages of cover/TOC before content starts at PDF page 5).
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'public', 'data', 'class_x_english.json')

# (unit_number, title, pdf_start, pdf_end)
# Book page 1 = PDF page 5, so bookPage = pdfPage - 4
UNITS = [
    (1, 'Contributions of Notable Leaders',    5,   46),
    (2, 'Labour and People\'s Rights',         27,  68),
    (3, 'Practicing Positive Work Ethics',     50,  97),
    (4, 'Media for Information and Reflection', 72, 116),
    (5, 'Respecting Self and Others',          101, 132),
    (6, 'Character Building',                  120, 152),
]

TOTAL_PAGES = 194

SEC_LABEL = {
    '1': 'Reading Comprehension',
    '2': 'Oral Communication',
    '3': 'Language Practice',
    '4': 'Writing',
    '5': 'Study Skills',
    '6': 'Fun',
}


def sec(unit, letter):
    return f'Unit {unit} {SEC_LABEL.get(letter, letter)}'


def q(qid, unit, letter, number, qtype, question, answer, explanation, pdf_page):
    d = {
        'id': qid,
        'unit': unit,
        'section': sec(unit, letter),
        'sectionCode': f'U{unit}{letter}',
        'type': qtype,
        'number': number,
        'question': question,
        'answer': answer,
        'explanation': explanation,
        'pdfPage': pdf_page,
        'bookPage': pdf_page - 4,
        'figure': None,
    }
    return d


SOLVED = []

# ============================================================================
# UNIT 1: Contributions of Notable Leaders
# ============================================================================

# Unit 1, Section 1.1: Reading Comprehension - The Voice of God (PDF 6, book 2)
U, S = 1, '1'
SOLVED += [
    q('u1_s1_ex1_q1', U, S, 1, 'comprehension',
      'Why did the author climb the topmost steeple?',
      'The author climbed the topmost steeple to hear the voice of God. He thought God would be found in high, sacred places like church steeples.',
      'The poem shows the author\'s initial belief that God resides in lofty, religious structures. This represents a common misconception that divinity is found only in formal religious settings.',
      6),
    q('u1_s1_ex1_q2', U, S, 2, 'comprehension',
      'Why did God tell him to go down again?',
      'God told him to go down because God dwells among the people, not in high steeples. God is found in the community and in human connections, not isolated in tall buildings.',
      'The poem\'s central message is that God is not confined to religious buildings but lives among ordinary people. True spirituality is found in human service and community.',
      6),
    q('u1_s1_ex1_q3', U, S, 3, 'comprehension',
      'Say in your own words what you think is the message of this poem?',
      'The message of the poem is that God is not found in high places or religious buildings alone. God lives among the people, in our communities, and in our service to others. True spirituality is about connecting with humanity, not seeking isolation in sacred spaces.',
      'The poem challenges the notion that divinity requires physical elevation or separation. It emphasizes that God is accessible in everyday life and human relationships.',
      6),
]

# Unit 1, Section 1.1: Reading Comprehension - The Wise Caliph (PDF 11, book 7)
SOLVED += [
    q('u1_s1_ex2_q1', U, S, 1, 'comprehension',
      'How many main characters are there in the story?',
      'There are four main characters in the story: Caliph Haroon-ur-Rashid, the Qazi (judge), the well-dressed rich man, and the beggar in rags.',
      'The story revolves around these four characters. The Caliph is the wise judge, the Qazi brings the case, and the two men are disputing ownership of the horse.',
      11),
    q('u1_s1_ex2_q2', U, S, 2, 'comprehension',
      'Who are they?',
      'The four main characters are: (1) Caliph Haroon-ur-Rashid - the wise ruler, (2) The Qazi - the judge who brought the case, (3) The well-dressed rich man - the true owner of the horse, (4) The beggar in rags - who tried to steal the horse.',
      'Each character plays a specific role in demonstrating wisdom and justice. The Caliph shows clever judgment, while the other characters represent different aspects of society.',
      11),
    q('u1_s1_ex2_q3', U, S, 3, 'comprehension',
      'Who got the horse?',
      'The well-dressed rich man got the horse. The Caliph determined the true owner by observing the horse\'s reaction - it snorted and neighed with pleasure when the rich man touched it, but winced when the beggar touched it.',
      'The Caliph used a clever test based on the animal\'s natural response to its true master. This shows that animals recognize and respond to their owners.',
      11),
    q('u1_s1_ex2_q4', U, S, 4, 'comprehension',
      'Was the person who wrongly claimed the horse punished?',
      'No, the beggar was not punished. The Caliph showed mercy and forgave him, saying "I shall be merciful and forgive you this time, if you beg forgiveness from this gentleman here." The rich man also forgave the beggar and even gave him gold coins.',
      'The story emphasizes mercy and forgiveness over punishment. Both the Caliph and the rich man showed compassion, teaching a lesson about kindness and second chances.',
      11),
]

# Unit 1, Section 1.1: Vocabulary Exercise (PDF 14, book 10)
SOLVED += [
    q('u1_s1_ex3_q1', U, S, 1, 'vocabulary',
      'What does "disguise" mean?',
      'Disguise means "change appearance". It refers to altering one\'s look to avoid recognition.',
      'In the story, the Caliph disguised himself as a common man to walk among his people without being recognized.',
      14),
    q('u1_s1_ex3_q2', U, S, 2, 'vocabulary',
      'What does "concerned" mean?',
      'Concerned means "worried about". It shows care and anxiety about someone or something.',
      'The Caliph was concerned about his people\'s problems and welfare, showing his care as a ruler.',
      14),
    q('u1_s1_ex3_q3', U, S, 3, 'vocabulary',
      'What does "welfare" mean?',
      'Welfare means "general well-being". It refers to the health, happiness, and prosperity of people.',
      'The Caliph cared about the welfare of his people, meaning their overall well-being and quality of life.',
      14),
    q('u1_s1_ex3_q4', U, S, 4, 'vocabulary',
      'What does "mingle" mean?',
      'Mingle means "mix with people". It refers to joining and interacting with others in a social setting.',
      'The Caliph would mingle with common people to understand their difficulties firsthand.',
      14),
    q('u1_s1_ex3_q5', U, S, 5, 'vocabulary',
      'What does "rags" mean?',
      'Rags means "old, torn clothes". It refers to worn-out, poor-quality clothing.',
      'The beggar was dressed in rags, indicating his poverty and low social status.',
      14),
    q('u1_s1_ex3_q6', U, S, 6, 'vocabulary',
      'What does "dispute" mean?',
      'Dispute means "disagreement about something". It refers to a conflict or argument over something.',
      'The two men had a dispute over the ownership of the horse.',
      14),
    q('u1_s1_ex3_q7', U, S, 7, 'vocabulary',
      'What does "resolve" mean?',
      'Resolve means "find a solution". It refers to settling or solving a problem or conflict.',
      'The Qazi hoped the Caliph would resolve the difficult case.',
      14),
    q('u1_s1_ex3_q8', U, S, 8, 'vocabulary',
      'What does "certain" mean?',
      'Certain means "know for sure". It refers to being confident or sure about something.',
      'The Qazi was certain that the Caliph would resolve the case justly.',
      14),
    q('u1_s1_ex3_q9', U, S, 9, 'vocabulary',
      'What does "claims" mean?',
      'Claims means "officially said". It refers to stating that something belongs to you or is true.',
      'Each man claimed that the horse belonged to him.',
      14),
    q('u1_s1_ex3_q10', U, S, 10, 'vocabulary',
      'What does "motioned" mean?',
      'Motioned means "signalled". It refers to making a gesture to direct or communicate.',
      'The Caliph motioned for the men to step forward.',
      14),
    q('u1_s1_ex3_q11', U, S, 11, 'vocabulary',
      'What does "dismount" mean?',
      'Dismount means "get off something". It refers to getting down from a horse or vehicle.',
      'The men had to dismount from their horses.',
      14),
    q('u1_s1_ex3_q12', U, S, 12, 'vocabulary',
      'What does "puzzled" mean?',
      'Puzzled means "unable to understand". It refers to being confused or perplexed.',
      'The Qazi was puzzled by the difficult case.',
      14),
    q('u1_s1_ex3_q13', U, S, 13, 'vocabulary',
      'What does "winced" mean?',
      'Winced means "showed dislike". It refers to making a slight movement showing pain or discomfort.',
      'The horse winced when the beggar touched it, showing discomfort.',
      14),
    q('u1_s1_ex3_q14', U, S, 14, 'vocabulary',
      'What does "neighed" mean?',
      'Neighed means "sound made by a horse". It refers to the characteristic sound horses make.',
      'The horse neighed with pleasure when its true owner touched it.',
      14),
    q('u1_s1_ex3_q15', U, S, 15, 'vocabulary',
      'What does "pronounced" mean?',
      'Pronounced means "officially said". It refers to declaring or stating something formally.',
      'The Caliph pronounced his judgment about the horse\'s ownership.',
      14),
]

# Unit 1, Section 1.2: Oral Communication (PDF 19, book 15)
U, S = 1, '2'
SOLVED += [
    q('u1_s2_ex1_q1', U, S, 1, 'oral',
      'Organize the mixed-up points about diseases and health.',
      'The correct order is: (a) I believe that medicines from parents/grandparents are better than doctors. (b) Health is most important, we should protect it. (c) Some illnesses go away on their own. (d) This doesn\'t make sense, but I\'ll go with your idea. (e) I don\'t agree, doctors give us lead to other problems. (f) Yes, that makes sense. (g) We should see a doctor for health problems lasting more than 2-3 days. (h) Not treating diseases properly can lead to bigger problems.',
      'This exercise teaches students to organize jumbled points into a coherent discussion about health and medical treatment.',
      19),
    q('u1_s2_ex2_q1', U, S, 1, 'oral',
      'Prepare a role play about giving advice on problems young people face.',
      'Students work in groups of four. One plays a councillor, three play citizens. Each citizen presents a problem, others give advice using expressions like "I suggest", "I think", "You should". Topics include education, health, environment, and social issues.',
      'This exercise develops oral communication skills through role-playing real-life scenarios about seeking and giving advice.',
      20),
    q('u1_s2_ex3_q1', U, S, 1, 'oral',
      'Prepare a brief dialogue on one of the given topics expressing agreement and disagreement.',
      'Topics include: (1) All students should study up to Masters level. (2) All of us should grow our own vegetables. (3) All of us should stop eating meat. (4) All people in offices should wear uniforms. (5) No animals should be allowed on roads. Students express both agreement and disagreement using given expressions.',
      'This exercise practices expressing different viewpoints respectfully, an important communication skill.',
      20),
]

# Unit 1, Section 1.3: Language Practice (PDF 22, book 18)
U, S = 1, '3'
SOLVED += [
    q('u1_s3_ex1_q1', U, S, 1, 'grammar',
      'Add capital letters and punctuation: "moreover i have seen his picture in magazines on television and in movies"',
      'Moreover, I have seen his picture in magazines, on television, and in movies.',
      'Capitalize first word "Moreover" and pronoun "I". Add comma after "Moreover" and before "and" in a list.',
      22),
    q('u1_s3_ex1_q2', U, S, 2, 'grammar',
      'Add capital letters and punctuation: "chuck chuck chuck the train began moving out of the station therefore the people started running"',
      'Chuck, chuck, chuck! The train began moving out of the station; therefore, the people started running.',
      'Capitalize first word. Add exclamation after sound words. Use semicolon before "therefore" and comma after it.',
      22),
    q('u1_s3_ex1_q3', U, S, 3, 'grammar',
      'Add capital letters and punctuation: "wow this is a pleasant surprise why didn\'t you tell me you were coming"',
      'Wow! This is a pleasant surprise. Why didn\'t you tell me you were coming?',
      'Capitalize "Wow" and "This". Add exclamation after "Wow". End with question mark.',
      22),
    q('u1_s3_ex1_q4', U, S, 4, 'grammar',
      'Add capital letters and punctuation: "your book has been lying on this table for ten days said mr jawad when will you read it"',
      '"Your book has been lying on this table for ten days," said Mr. Jawad. "When will you read it?"',
      'Use quotation marks for direct speech. Capitalize "Mr. Jawad". Add comma inside quotes before "said".',
      22),
]

# Unit 1, Section 1.3: Apostrophes and Quotation Marks (PDF 22, book 18)
SOLVED += [
    q('u1_s3_ex2_q1', U, S, 1, 'grammar',
      'Insert apostrophes: "This book isn\'t mine, said Abdul Karim. I dont know who put it here."',
      '"This book isn\'t mine," said Abdul Karim. "I don\'t know who put it here."',
      'Add apostrophe in "don\'t" (do not). Use quotation marks for direct speech.',
      22),
    q('u1_s3_ex2_q2', U, S, 2, 'grammar',
      'Insert apostrophes: "Can we go to the seaside, father? the children asked. Its such a lovely day."',
      '"Can we go to the seaside, father?" the children asked. "It\'s such a lovely day."',
      'Add apostrophe in "It\'s" (It is). Use quotation marks and question mark correctly.',
      22),
    q('u1_s3_ex2_q3', U, S, 3, 'grammar',
      'Insert apostrophes: "The girls father said, Ill take you to school today. Its still early and well reach in time."',
      'The girl\'s father said, "I\'ll take you to school today. It\'s still early and we\'ll reach in time."',
      'Add apostrophe in "girl\'s" (possessive), "I\'ll" (I will), "It\'s" (It is), "we\'ll" (we will).',
      22),
    q('u1_s3_ex2_q4', U, S, 4, 'grammar',
      'Insert apostrophes: "Mother said, Wholl help me clean the house? I cant said Laila Ive got to write an essay."',
      'Mother said, "Who\'ll help me clean the house?" "I can\'t," said Laila. "I\'ve got to write an essay."',
      'Add apostrophes in "Who\'ll" (Who will), "can\'t" (cannot), "I\'ve" (I have). Use proper quotation marks.',
      22),
]

# Unit 1, Section 1.4: Writing (PDF 28, book 24)
U, S = 1, '4'
SOLVED += [
    q('u1_s4_ex1_q1', U, S, 1, 'writing',
      'Write a paragraph about "The Voice of God" poem using pre-writing strategy.',
      'The poem "The Voice of God" by Louis I. Newman teaches us that God is not found in high places like steeples or mountains. The poet climbed to the topmost steeple to hear God\'s voice, but God told him to go down among the people. The message is clear: God lives in our communities, in our service to others, and in human connections. True spirituality is not about isolation in sacred spaces but about engaging with humanity. We should look for God in the faces of the poor, the needy, and our fellow human beings.',
      'This paragraph uses the pre-writing strategy: brainstorming ideas, organizing them logically, and writing a coherent paragraph with a clear topic sentence and supporting details.',
      28),
]

# Unit 1, Section 1.5: Study Skills (PDF 30, book 26)
U, S = 1, '5'
SOLVED += [
    q('u1_s5_ex1_q1', U, S, 1, 'activity',
      'Collect points for written and oral work about notable leaders.',
      'Points to collect: (1) Research about the leader\'s life and achievements. (2) Note their contributions to society. (3) Identify their qualities and values. (4) Find examples of their wisdom or kindness. (5) Prepare both written notes and oral presentation points. (6) Practice speaking clearly and confidently.',
      'Study skills involve organizing information effectively for both written and oral presentations. This exercise teaches research and presentation preparation.',
      30),
]

# Unit 1, Section 1.6: Fun (PDF 32, book 28)
U, S = 1, '6'
SOLVED += [
    q('u1_s6_ex1_q1', U, S, 1, 'activity',
      'Complete the story about a wise ruler.',
      'Story completion exercise: Students read an incomplete story about a wise ruler and complete it using their imagination. The story should include elements of wisdom, justice, and kindness, similar to the Caliph story in the unit.',
      'This fun activity encourages creativity while reinforcing the unit\'s themes of wisdom and leadership.',
      32),
]

# ============================================================================
# UNIT 2: Labour and People's Rights
# ============================================================================

# Unit 2, Section 2.1: Reading Comprehension - Dignity of Work (PDF 35, book 31)
U, S = 2, '1'
SOLVED += [
    q('u2_s1_ex1_q1', U, S, 1, 'comprehension',
      'What is the main message of "Dignity of Work"?',
      'The main message is that all work is dignified and should be respected. The dialogue between Akhtar and his uncle shows that even simple jobs like sweeping are honorable. The Holy Prophet (PBUH) and his companions did their own work, showing that no work is beneath anyone\'s dignity.',
      'The story teaches that work itself has dignity, regardless of its nature. Islam emphasizes self-reliance and doing one\'s own work.',
      35),
    q('u2_s1_ex1_q2', U, S, 2, 'comprehension',
      'Why did the Holy Prophet (PBUH) do his own work?',
      'The Holy Prophet (PBUH) did his own work because he believed in self-reliance and dignity of labor. He repaired his own shoes, mended his clothes, swept his room, and helped build the mosque in Medina. He never asked anyone to do what he wouldn\'t do himself.',
      'The Prophet\'s example shows that true leadership involves serving others and doing one\'s own work, not expecting others to serve you.',
      35),
    q('u2_s1_ex1_q3', U, S, 3, 'comprehension',
      'Give examples of how the companions of the Prophet did their own work.',
      'Examples include: (1) Hazrat Abu Bakr (RA) fetched water for widows and neighbors. (2) Hazrat Omar (RA) carried a sack of flour for a needy family. (3) Hazrat Ali (RA) labored in a Jew\'s garden and gave away his wages. (4) Hazrat Fatima (RA) fetched water, ground corn, and swept the house. (5) Caliph Omar bin Abdul Aziz refused to hire a servant. (6) Sultan Nasir-ud-din earned his living by making caps. (7) Emperor Aurangzeb transcribed the Holy Quran.',
      'These examples show that even the most powerful and respected people in Islamic history did their own work and helped others.',
      35),
]

# Unit 2, Section 2.2: Oral Communication (PDF 41, book 37)
U, S = 2, '2'
SOLVED += [
    q('u2_s2_ex1_q1', U, S, 1, 'oral',
      'Seek and offer advice about problems young people face.',
      'Students work in groups. One plays a councillor, others play citizens. Citizens present problems like unemployment, education costs, health issues. Councillor and others offer advice using expressions: "I suggest", "I think you should", "Why don\'t you", "It would be better if".',
      'This exercise develops skills in seeking and giving advice, an important life skill for young people.',
      41),
]

# Unit 2, Section 2.3: Language Practice (PDF 43, book 39)
U, S = 2, '3'
SOLVED += [
    q('u2_s3_ex1_q1', U, S, 1, 'grammar',
      'Fill in blanks with Present Simple: "Birds usually ______ their nests in summer." (build)',
      'Birds usually build their nests in summer.',
      'Use base form "build" for plural subject "Birds" in Present Simple tense.',
      43),
    q('u2_s3_ex1_q2', U, S, 2, 'grammar',
      'Fill in blanks with Present Simple: "He ______ up late and ______ quickly for school." (get, dress)',
      'He gets up late and dresses quickly for school.',
      'Add "s" to verbs for third person singular: "gets" and "dresses".',
      43),
    q('u2_s3_ex2_q1', U, S, 1, 'grammar',
      'Fill in blanks with Present Continuous: "Look! It ______ so hard." (rain)',
      'Look! It is raining so hard.',
      'Use "is raining" for Present Continuous with singular subject "It". Add "ing" to verb.',
      43),
    q('u2_s3_ex2_q2', U, S, 2, 'grammar',
      'Fill in blanks with Present Continuous: "We ______ English these days." (learn)',
      'We are learning English these days.',
      'Use "are learning" for Present Continuous with plural subject "We".',
      43),
]

# Unit 2, Section 2.4: Writing (PDF 50, book 46)
U, S = 2, '4'
SOLVED += [
    q('u2_s4_ex1_q1', U, S, 1, 'writing',
      'Write a formal email to a company manager about a job application.',
      'Subject: Application for the Position of Sales Representative\n\nDear Sir/Madam,\n\nI am writing to apply for the position of Sales Representative advertised in the Daily Dawn on 15th March. I have completed my Bachelor\'s degree in Business Administration and have two years of experience in sales.\n\nI am a hardworking and honest person with good communication skills. I can speak English, Urdu, and Sindhi fluently. I am confident that I can contribute effectively to your company\'s growth.\n\nI have attached my CV and certificates for your reference. I would be grateful for an opportunity to discuss my application in an interview.\n\nThank you for considering my application.\n\nYours faithfully,\n[Name]',
      'A formal email should include: clear subject line, proper salutation, introduction stating purpose, body with qualifications, polite closing, and signature.',
      50),
]

# Unit 2, Section 2.5: Study Skills (PDF 53, book 49)
U, S = 2, '5'
SOLVED += [
    q('u2_s5_ex1_q1', U, S, 1, 'activity',
      'Fill in a job application form.',
      'Students practice filling a job application form with: personal details (name, address, phone), educational qualifications, work experience, skills, references. This teaches practical life skills for job seeking.',
      'Filling forms correctly is an important study and life skill. Attention to detail and accuracy are essential.',
      53),
]

# Unit 2, Section 2.6: Fun (PDF 55, book 51)
U, S = 2, '6'
SOLVED += [
    q('u2_s6_ex1_q1', U, S, 1, 'activity',
      'Play a word game related to jobs and professions.',
      'Word game: Students form teams and take turns naming jobs/professions. Each word must start with the last letter of the previous word. For example: Teacher → Runner → Nurse → Engineer. Teams earn points for correct answers.',
      'This fun activity builds vocabulary related to occupations while developing quick thinking.',
      55),
]

# ============================================================================
# UNIT 3: Practicing Positive Work Ethics
# ============================================================================

# Unit 3, Section 3.1: Reading Comprehension - King Bruce and the Spider (PDF 57, book 53)
U, S = 3, '1'
SOLVED += [
    q('u3_s1_ex1_q1', U, S, 1, 'comprehension',
      'Why was King Bruce sad and defeated?',
      'King Bruce was sad and defeated because he had lost six battles against his enemies. He had tried hard to defeat them but failed every time. He felt hopeless and thought he could never win.',
      'The story shows that even great leaders face defeats. What matters is how they respond to failure.',
      57),
    q('u3_s1_ex1_q2', U, S, 2, 'comprehension',
      'What did the spider teach King Bruce?',
      'The spider taught King Bruce the lesson of perseverance and never giving up. The spider tried six times to reach the ceiling and fell each time, but on the seventh attempt, it succeeded. This inspired Bruce to try again and eventually win the seventh battle.',
      'The spider\'s persistence shows that success comes to those who keep trying despite failures.',
      57),
    q('u3_s1_ex1_q3', U, S, 3, 'comprehension',
      'What is the moral of the story?',
      'The moral is: "Never give up. Try and try again until you succeed." Failure is not the end but a step toward success. Persistence and determination lead to victory.',
      'This moral applies to all areas of life - studies, sports, career, and personal goals.',
      57),
]

# Unit 3, Section 3.2: Oral Communication (PDF 64, book 60)
U, S = 3, '2'
SOLVED += [
    q('u3_s2_ex1_q1', U, S, 1, 'oral',
      'Express needs with reasons in different situations.',
      'Students practice expressing needs with reasons. Examples: (1) "I need a new book because mine is torn." (2) "We need more trees because they clean the air." (3) "I need help with homework because it\'s difficult." (4) "The school needs a library because students love reading."',
      'This exercise teaches students to justify their needs with logical reasons, an important communication skill.',
      64),
]

# Unit 3, Section 3.3: Language Practice (PDF 66, book 62)
U, S = 3, '3'
SOLVED += [
    q('u3_s3_ex1_q1', U, S, 1, 'grammar',
      'Fill in blanks with Past Simple: "Yesterday, I ______ to the market." (go)',
      'Yesterday, I went to the market.',
      'Use past form "went" for irregular verb "go" in Past Simple tense.',
      66),
    q('u3_s3_ex1_q2', U, S, 2, 'grammar',
      'Fill in blanks with Past Simple: "She ______ her homework last night." (complete)',
      'She completed her homework last night.',
      'Add "d" to regular verb "complete" to form past tense "completed".',
      66),
    q('u3_s3_ex2_q1', U, S, 1, 'grammar',
      'Fill in blanks with articles (a, an, the): "I saw ______ elephant at the zoo."',
      'I saw an elephant at the zoo.',
      'Use "an" before vowel sounds. "Elephant" starts with vowel sound "e".',
      66),
    q('u3_s3_ex2_q2', U, S, 2, 'grammar',
      'Fill in blanks with articles: "______ sun rises in the east."',
      'The sun rises in the east.',
      'Use "the" for unique things. There is only one sun.',
      66),
]

# Unit 3, Section 3.4: Writing (PDF 73, book 69)
U, S = 3, '4'
SOLVED += [
    q('u3_s4_ex1_q1', U, S, 1, 'writing',
      'Write a summary of the poem "The Voice of God".',
      'Summary: The poem "The Voice of God" by Louis I. Newman is about a man who searches for God in high places. He climbs a steeple but God tells him to go down among the people. The poem teaches that God is found in human service and community, not in isolation. The main theme is that true spirituality lies in helping others.',
      'A summary should capture the main points briefly without personal opinions. It should be shorter than the original.',
      73),
]

# Unit 3, Section 3.5: Study Skills (PDF 75, book 71)
U, S = 3, '5'
SOLVED += [
    q('u3_s5_ex1_q1', U, S, 1, 'activity',
      'Practice free writing about your daily routine.',
      'Free writing exercise: Write continuously for 10 minutes about your daily routine without worrying about grammar or spelling. Just let your thoughts flow. Topics can include: morning activities, school, homework, play time, family time, bedtime.',
      'Free writing helps overcome writer\'s block and develops fluency in expressing thoughts.',
      75),
]

# Unit 3, Section 3.6: Fun (PDF 77, book 73)
U, S = 3, '6'
SOLVED += [
    q('u3_s6_ex1_q1', U, S, 1, 'activity',
      'Learn cool collocations (word partnerships).',
      'Collocations are words that go together naturally. Examples: (1) make a decision (not do a decision), (2) do homework (not make homework), (3) take a photo (not make a photo), (4) have a party (not make a party), (5) catch a cold (not take a cold). Students match verbs with correct nouns.',
      'Learning collocations improves natural English usage and fluency.',
      77),
]

# ============================================================================
# UNIT 4: Media for Information and Reflection
# ============================================================================

# Unit 4, Section 4.1: Reading Comprehension - Social Media (PDF 79, book 75)
U, S = 4, '1'
SOLVED += [
    q('u4_s1_ex1_q1', U, S, 1, 'comprehension',
      'What are the advantages of social media?',
      'Advantages of social media include: (1) Connecting with friends and family worldwide. (2) Sharing information quickly. (3) Learning about current events. (4) Educational content and online courses. (5) Business opportunities and marketing. (6) Entertainment and creativity.',
      'Social media has transformed communication and information sharing in the modern world.',
      79),
    q('u4_s1_ex1_q2', U, S, 2, 'comprehension',
      'What are the disadvantages of social media?',
      'Disadvantages include: (1) Addiction and time wastage. (2) Cyberbullying and online harassment. (3) Spread of false information. (4) Privacy concerns and data theft. (5) Reduced face-to-face interaction. (6) Mental health issues like depression and anxiety.',
      'While social media has benefits, excessive or irresponsible use can harm individuals and society.',
      79),
    q('u4_s1_ex1_q3', U, S, 3, 'comprehension',
      'How can we use social media responsibly?',
      'We can use social media responsibly by: (1) Limiting screen time. (2) Verifying information before sharing. (3) Being kind and respectful online. (4) Protecting personal information. (5) Balancing online and offline activities. (6) Using it for learning and positive purposes.',
      'Responsible use maximizes benefits while minimizing harms.',
      79),
]

# Unit 4, Section 4.2: Oral Communication (PDF 90, book 86)
U, S = 4, '2'
SOLVED += [
    q('u4_s2_ex1_q1', U, S, 1, 'oral',
      'Give an individual presentation on a topic of your choice.',
      'Students prepare a 3-5 minute presentation on topics like: (1) My favorite book, (2) Environmental protection, (3) Importance of education, (4) My role model, (5) Technology in daily life. Presentation should have introduction, body with 3 points, and conclusion.',
      'Individual presentations develop confidence, organization skills, and public speaking ability.',
      90),
]

# Unit 4, Section 4.3: Language Practice (PDF 92, book 88)
U, S = 4, '3'
SOLVED += [
    q('u4_s3_ex1_q1', U, S, 1, 'grammar',
      'Fill in blanks with Future tense: "Tomorrow, I ______ to the library." (go)',
      'Tomorrow, I will go to the library.',
      'Use "will + base verb" for Future Simple tense.',
      92),
    q('u4_s3_ex1_q2', U, S, 2, 'grammar',
      'Change to passive voice: "The teacher teaches the students."',
      'The students are taught by the teacher.',
      'In passive voice, object becomes subject. Use "is/are + past participle". "Teach" becomes "taught".',
      92),
    q('u4_s3_ex1_q3', U, S, 3, 'grammar',
      'Change to passive voice: "She writes a letter."',
      'A letter is written by her.',
      'Object "a letter" becomes subject. Use "is written" (present passive). "She" becomes "by her".',
      92),
]

# Unit 4, Section 4.4: Writing (PDF 100, book 96)
U, S = 4, '4'
SOLVED += [
    q('u4_s4_ex1_q1', U, S, 1, 'writing',
      'Write a cause and effect essay about pollution.',
      'Title: Causes and Effects of Pollution\n\nPollution is a major problem in our cities. There are several causes and effects of pollution.\n\nCauses: First, vehicles release harmful gases into the air. Second, factories dump waste into rivers. Third, people throw garbage on streets.\n\nEffects: Pollution causes health problems like asthma and cancer. It harms animals and plants. It makes our cities dirty and unpleasant.\n\nSolutions: We should use public transport, plant trees, and recycle waste. Government should make strict laws against pollution.\n\nIn conclusion, pollution is serious but we can solve it together.',
      'A cause and effect essay identifies reasons (causes) and results (effects) of a problem, then suggests solutions.',
      100),
]

# Unit 4, Section 4.5: Study Skills (PDF 103, book 99)
U, S = 4, '5'
SOLVED += [
    q('u4_s5_ex1_q1', U, S, 1, 'activity',
      'Practice critical thinking and problem solving.',
      'Critical thinking exercise: Analyze a problem (e.g., traffic congestion). Identify causes (too many cars, poor roads). Brainstorm solutions (public transport, carpooling, better roads). Evaluate each solution. Choose the best one and explain why.',
      'Critical thinking involves analyzing problems systematically and finding logical solutions.',
      103),
]

# Unit 4, Section 4.6: Fun (PDF 105, book 101)
U, S = 4, '6'
SOLVED += [
    q('u4_s6_ex1_q1', U, S, 1, 'activity',
      'Write about "Me after 10 years".',
      'Creative writing: Students imagine and write about their life 10 years in the future. Topics include: career, family, achievements, lifestyle, contributions to society. Example: "After 10 years, I will be a doctor helping poor people. I will have a small clinic in my village..."',
      'This activity encourages goal-setting and creative thinking about the future.',
      105),
]

# ============================================================================
# UNIT 5: Respecting Self and Others
# ============================================================================

# Unit 5, Section 5.1: Reading Comprehension - A Bad Dream (PDF 108, book 104)
U, S = 5, '1'
SOLVED += [
    q('u5_s1_ex1_q1', U, S, 1, 'comprehension',
      'What was the bad dream about?',
      'The bad dream was about a world where people didn\'t respect each other. In the dream, the dreamer saw people fighting, being rude, and not caring about others\' feelings. Everyone was unhappy and lonely.',
      'The dream shows the importance of respect in creating a happy society.',
      108),
    q('u5_s1_ex1_q2', U, S, 2, 'comprehension',
      'What lesson did the dreamer learn?',
      'The dreamer learned that respect is essential for happiness and peace. When we respect others, we create a positive environment. Disrespect leads to conflict and unhappiness.',
      'The story teaches that respect is a two-way street - we must give respect to receive it.',
      108),
]

# Unit 5, Section 5.2: Oral Communication (PDF 116, book 112)
U, S = 5, '2'
SOLVED += [
    q('u5_s2_ex1_q1', U, S, 1, 'oral',
      'Evaluate a presentation using given criteria.',
      'Presentation evaluation criteria: (1) Content - was it informative? (2) Organization - was it logical? (3) Delivery - was it clear and confident? (4) Language - was it correct? (5) Engagement - did it hold attention? Students give feedback using these criteria.',
      'Evaluation skills help students become better presenters and critical listeners.',
      116),
]

# Unit 5, Section 5.3: Language Practice (PDF 117, book 113)
U, S = 5, '3'
SOLVED += [
    q('u5_s3_ex1_q1', U, S, 1, 'grammar',
      'Identify singular and plural nouns: "The children play in the garden."',
      '"Children" is plural (more than one child). "Garden" is singular (one garden).',
      'Singular nouns refer to one person/thing. Plural nouns refer to more than one.',
      117),
    q('u5_s3_ex1_q2', U, S, 2, 'grammar',
      'Use modal verbs: "You ______ respect your elders." (should/must)',
      'You should respect your elders.',
      '"Should" expresses advice or duty. "Must" expresses strong obligation.',
      117),
]

# Unit 5, Section 5.4: Writing (PDF 123, book 119)
U, S = 5, '4'
SOLVED += [
    q('u5_s4_ex1_q1', U, S, 1, 'writing',
      'Write a letter to the editor about cleanliness in your city.',
      'The Editor,\nDaily Dawn,\nKarachi.\n\nSubject: Cleanliness in Our City\n\nDear Sir,\n\nI want to draw attention to the poor cleanliness in our city. Streets are full of garbage. Drains are blocked. This causes diseases and bad smell.\n\nI suggest: (1) More dustbins on streets. (2) Regular garbage collection. (3) Fines for littering. (4) Awareness campaigns.\n\nPlease publish this to awaken authorities.\n\nYours,\n[Name]',
      'A letter to the editor should be concise, state the problem clearly, and suggest solutions.',
      123),
]

# Unit 5, Section 5.5: Study Skills (PDF 124, book 120)
U, S = 5, '5'
SOLVED += [
    q('u5_s5_ex1_q1', U, S, 1, 'activity',
      'Maintain a daily schedule.',
      'Create a daily schedule: (1) Wake up time: 6:00 AM. (2) Morning routine: 6:00-7:00. (3) School: 8:00-2:00. (4) Homework: 3:00-5:00. (5) Play time: 5:00-6:00. (6) Family time: 6:00-8:00. (7) Study: 8:00-9:00. (8) Sleep: 9:30 PM.',
      'Time management is a crucial study skill. A schedule helps balance all activities.',
      124),
]

# Unit 5, Section 5.6: Fun (PDF 125, book 121)
U, S = 5, '6'
SOLVED += [
    q('u5_s6_ex1_q1', U, S, 1, 'activity',
      'Play a game with name, place, animal, thing.',
      'Game: Choose a letter (e.g., "B"). Students write: Name (Bilal), Place (Balochistan), Animal (Bear), Thing (Book). First to complete correctly wins. This builds vocabulary and quick thinking.',
      'This classic game develops vocabulary across categories while being fun and competitive.',
      125),
]

# ============================================================================
# UNIT 6: Character Building
# ============================================================================

# Unit 6, Section 6.1: Reading Comprehension - Speak Gently (PDF 127, book 123)
U, S = 6, '1'
SOLVED += [
    q('u6_s1_ex1_q1', U, S, 1, 'comprehension',
      'What is the message of "Speak Gently"?',
      'The message is to speak kindly and gently to others. Harsh words hurt people\'s feelings and damage relationships. Gentle words heal, comfort, and build strong bonds. We should always choose kindness in our speech.',
      'The poem emphasizes the power of words to either hurt or heal.',
      127),
    q('u6_s1_ex1_q2', U, S, 2, 'comprehension',
      'Why should we speak gently?',
      'We should speak gently because: (1) It shows respect for others. (2) It avoids hurting feelings. (3) It builds trust and friendship. (4) It reflects good character. (5) It creates peace and harmony.',
      'Gentle speech is a sign of maturity and good upbringing.',
      127),
]

# Unit 6, Section 6.2: Oral Communication (PDF 131, book 127)
U, S = 6, '2'
SOLVED += [
    q('u6_s2_ex1_q1', U, S, 1, 'oral',
      'Practice public speaking on a given topic.',
      'Students prepare a 2-minute speech on topics like: (1) Importance of honesty. (2) My favorite teacher. (3) How to be a good friend. (4) Respect for parents. Practice speaking clearly, confidently, and with proper body language.',
      'Public speaking builds confidence and communication skills essential for life.',
      131),
]

# Unit 6, Section 6.3: Language Practice (PDF 132, book 128)
U, S = 6, '3'
SOLVED += [
    q('u6_s3_ex1_q1', U, S, 1, 'grammar',
      'Use transitional devices: "First, ______. Second, ______. Finally, ______."',
      'First, we should respect our parents. Second, we should help our teachers. Finally, we should be kind to friends.',
      'Transitional devices like "first, second, finally" organize ideas logically.',
      132),
    q('u6_s3_ex1_q2', U, S, 2, 'grammar',
      'Change direct to indirect: He said, "I am happy."',
      'He said that he was happy.',
      'In indirect speech: remove quotes, change pronouns, adjust tense (present → past).',
      132),
]

# Unit 6, Section 6.4: Writing (PDF 138, book 134)
U, S = 6, '4'
SOLVED += [
    q('u6_s4_ex1_q1', U, S, 1, 'writing',
      'Write an expository essay on "The Importance of Education".',
      'Education is the foundation of success. It opens doors to opportunities. First, education gives us knowledge and skills. Second, it helps us get good jobs. Third, it makes us better citizens.\n\nEducation also builds character. We learn values like honesty, respect, and responsibility. Educated people can solve problems and contribute to society.\n\nIn conclusion, education is essential for personal and national progress. Every child should have access to quality education.',
      'An expository essay explains or informs about a topic with facts and examples.',
      138),
]

# Unit 6, Section 6.5: Study Skills (PDF 141, book 137)
U, S = 6, '5'
SOLVED += [
    q('u6_s5_ex1_q1', U, S, 1, 'activity',
      'Do a SWOC analysis (Strengths, Weaknesses, Opportunities, Challenges).',
      'SWOC analysis of a student: Strengths - hardworking, good at math. Weaknesses - weak in English, shy. Opportunities - scholarships, online courses. Challenges - time management, competition. This helps self-awareness and planning.',
      'SWOC analysis is a tool for self-assessment and strategic planning.',
      141),
]

# Unit 6, Section 6.6: Fun (PDF 142, book 138)
U, S = 6, '6'
SOLVED += [
    q('u6_s6_ex1_q1', U, S, 1, 'activity',
      'Play an adventure game involving problem-solving.',
      'Adventure game: Students work in teams to solve puzzles and complete challenges. Each challenge requires teamwork, creativity, and critical thinking. Example: Decode a message, build a bridge with limited materials, solve a riddle.',
      'Adventure games develop teamwork, problem-solving, and leadership skills.',
      142),
]

# ============================================================================
# Build the JSON
# ============================================================================

def build():
    chapters = []
    all_items = []

    for unit_num, unit_title, pdf_start, pdf_end in UNITS:
        unit_items = [q for q in SOLVED if q['unit'] == unit_num]
        chapters.append({
            'number': unit_num,
            'title': unit_title,
            'startPage': pdf_start,
            'endPage': pdf_end,
            'bookStart': pdf_start - 4,
            'bookEnd': pdf_end - 4,
            'totalQuestions': len(unit_items),
            'questions': unit_items,
        })
        all_items.extend(unit_items)

    pages_map = {f'page_{i:03d}': f'/books/class_x/english/pages/page_{i:03d}.webp'
                 for i in range(1, TOTAL_PAGES + 1)}

    out = {
        'subject': 'Secondary Stage English',
        'grade': 'X',
        'board': 'Sindh Textbook Board, Jamshoro',
        'totalPages': TOTAL_PAGES,
        'totalChapters': len(UNITS),
        'totalQuestionsSolved': len(all_items),
        'chapters': chapters,
        'pages': pages_map,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f'Built {OUT}: {len(all_items)} solved items across {len(UNITS)} units.')


if __name__ == '__main__':
    build()
