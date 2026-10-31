#!/usr/bin/env python3
"""Builds Sindhi X JSON data file for the SubjectZone app.

Asan Sindhi IX-X (Sindh Textbook Board, Jamshoro):
26 lessons (18 Prose + 8 Poetry), 90 PDF pages.
Each lesson ends with an exercise section (قشم) containing:
- (فلا) Answer questions
- (ب) Explain phrases / Find synonyms
- (ج) Find antonyms / Fill blanks
- (د) Fill in blanks / Word meanings
Output: public/data/class_x_sindhi.json
"""
import json
import os

# Lesson metadata: (lesson_number, title_sindhi, pdf_page_start, pdf_page_exercise, section_type)
# Prose section: lessons 1-18
# Poetry section: lessons 19-26
LESSONS = [
    # Prose section (نثر جو پاڳو)
    (1, "حجۃ الوداع و ارو خطبو", 7, 10, "prose"),
    (2, "حضرت سلمان فارسي رضي الله تعاليٰ عنه", 11, 13, "prose"),
    (3, "حضرت امام جعفر صادق عليه السلام", 14, 16, "prose"),
    (4, "قائداعظم رحمة الله عليه جا ارشاد", 17, 20, "prose"),
    (5, "اتحاد، تنظيم ۽ يقين محكم", 21, 27, "prose"),
    (6, "مولانا دين محمد وفائي", 28, 31, "prose"),
    (7, "مائي خيري", 32, 35, "prose"),
    (8, "هنر دولت آهي", 36, 37, "prose"),
    (9, "خط", 38, 41, "prose"),
    (10, "بين الاقوامي عدالت", 42, 45, "prose"),
    (11, "اجرڪ", 46, 50, "prose"),
    (12, "ميرن جي دربار", 51, 54, "prose"),
    (13, "ڪينجههر دند", 55, 58, "prose"),
    (14, "سنڌي ادب جي مختصر تاريخ", 59, 62, "prose"),
    (15, "رڏ پچاءُ", 63, 65, "prose"),
    (16, "پٽ بارهن", 66, 68, "prose"),
    (17, "نصرپور", 69, 71, "prose"),
    (18, "جهڙو راج تهڙو پراڳ", 72, 74, "prose"),
    # Poetry section (نظم جو پاڳو)
    (19, "آهيون الف آسري، محمد ميجوبوسون", 75, 76, "poetry"),
    (20, "نيڪي", 77, 78, "poetry"),
    (21, "دعا", 79, 80, "poetry"),
    (22, "سچل سرمست", 81, 82, "poetry"),
    (23, "ڊيئو", 83, 84, "poetry"),
    (24, "اٺيون سڪ جو ڪو سنسار", 85, 86, "poetry"),
    (25, "پيارا وطن", 87, 88, "poetry"),
    (26, "هاري", 89, 90, "poetry"),
]

# Exercise section labels
SEC_LABEL = {
    'A': 'Answer the Following Questions (فلا)',
    'B': 'Explain Phrases / Synonyms (ب)',
    'C': 'Antonyms / Fill Blanks (ج)',
    'D': 'Word Meanings / Fill Blanks (د)',
}


def q(lesson, section, section_code, qtype, number, question_sindhi, answer_sindhi, explanation="", pdf_page=None, book_page=None, figure=False):
    """Create a question dict."""
    return {
        "id": f"L{lesson:02d}_{section_code}{number}",
        "lesson": lesson,
        "section": section,
        "sectionCode": section_code,
        "type": qtype,
        "number": number,
        "question": question_sindhi,
        "answer": answer_sindhi,
        "explanation": explanation,
        "pdfPage": pdf_page,
        "bookPage": book_page,
        "figure": figure,
    }


# Solved exercises for all 26 lessons
# Each lesson's exercise is extracted from the visible exercise page (قشم section)
SOLVED = []

# === LESSON 1: حجۃ الوداع و ارو خطبو (PDF page 10 exercise) ===
SOLVED.extend([
    q(1, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "ڇاپي سگسرن صلي الله عليه وآله وسلم آخر حج ڪهڙي ڪئي؟",
      "ڇاپي سگسرن صلي الله عليه وآله وسلم آخر حج حجۃ الوداع ڪئي.",
      pdf_page=10, book_page=10),
    q(1, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "نه حج ڪي \"حجۃالوداع\" چيو ويو ۽ وجي؟",
      "نه حج کي \"حجۃالوداع\" ان ڪري چيو ويو جو هيءَ رسول الله صلي الله عليه وآله وسلم جي زندگيءَ جو آخري حج هو ۽ هن هن حج ۾ امت کي وداع ڪيو.",
      pdf_page=10, book_page=10),
    q(1, SEC_LABEL['A'], 'A', 'short_answer', 3,
      "ڇاپي سگسرن صلي الله عليه وآله وسلم اسلامي برادريءَ باب ڪهڙو راڄدار فرمايو؟",
      "ڇاپي سگسرن صلي الله عليه وآله وسلم فرمايو ته سڀ مسلمان هڪٻئي جا ڀائر آهن ۽ ڪنهن به مسلمان کي ٻئي مسلمان کان وڌيڪ فضيلت ناهي سواءِ تقويٰ جي.",
      pdf_page=10, book_page=10),
    q(1, SEC_LABEL['A'], 'A', 'short_answer', 4,
      "نبين ڪريم صلي الله عليه وآله وسلم نج نلاز، ناراب، يتيمن ۽ مسڪينن واسطي ڪهڙيون نصيحتون ڪرڻ فرمايون؟",
      "نبين ڪريم صلي الله عليه وآله وسلم فرمايو ته نلاز قائم ڪريو، زڪوة ادا ڪريو، يتيمن ۽ مسڪينن سان احسان ڪريو، ۽ عورتن سان نيڪ سلوڪ ڪريو.",
      pdf_page=10, book_page=10),
    q(1, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"نرين هيهان لاتاڻ\" - لفظ \"لاتاڻ\" جو مطلب بيان ڪريو.",
      "لاتاڻ جو مطلب آهي وسارڻ يا ڇڏي ڏيڻ.",
      pdf_page=10, book_page=10),
    q(1, SEC_LABEL['C'], 'C', 'short_answer', 1,
      "درندي - پٽانهن - رندمان - لجن - پچاڙي - پچاڙي: هنن لفظن جا هم معنيٰ لفظ لکو.",
      "درندي = وحشي، پٽانهن = ميداني، رندمان = خوش، لجن = شرمندا، پچاڙي = پکي.",
      pdf_page=10, book_page=10),
    q(1, SEC_LABEL['D'], 'D', 'short_answer', 1,
      "آقاي - جمعي - انتها - مارح - پچاڙي: هنن لفظن جا متضاد لفظ لکو.",
      "آقاي ≠ غلام، جمعي ≠ جدا، انتها ≠ ابتدا، مارح ≠ مرحبا، پچاڙي ≠ شام.",
      pdf_page=10, book_page=10),
])

# === LESSON 2: حضرت سلمان فارسي (PDF page 13 exercise) ===
SOLVED.extend([
    q(2, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "حضرت سلمان فارسي رضه ڪهڙي ملڪ جا رهواسي هئا؟",
      "حضرت سلمان فارسي رضه ايران جي فارس صوبي جا رهواسي هئا.",
      pdf_page=13, book_page=13),
    q(2, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "حضرت سلمان فارسي رضه ڪيئن اسلام قبول ڪيو؟",
      "حضرت سلمان فارسي رضه سچائي جي ڳولا ۾ نڪتا ۽ آخرڪار نبين ڪريم صلي الله عليه وآله وسلم وٽ پهچي اسلام قبول ڪيو.",
      pdf_page=13, book_page=13),
    q(2, SEC_LABEL['A'], 'A', 'short_answer', 3,
      "خندق جي جنگ ۾ حضرت سلمان فارسي رضه ڪهڙو مشورو ڏنو؟",
      "خندق جي جنگ ۾ حضرت سلمان فارسي رضه خندق کوٽڻ جو مشورو نو جيڪو عرب ۾ هڪ نئون حربو هو.",
      pdf_page=13, book_page=13),
    q(2, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"آتشڪدي\" جو مطلب بيان ڪريو.",
      "آتشڪدي جو مطلب آهي باهه جو مندر جتي پارسي باهه جي پوڄا ڪندا هئا.",
      pdf_page=13, book_page=13),
    q(2, SEC_LABEL['C'], 'C', 'short_answer', 1,
      "هن درس مان اسان کي ڪهڙي سبق ملي ٿي؟",
      "هن درس مان اسان کي سبق ملي ٿي ته سچائي ۽ لگن سان ڪم ڪندڙ کي ضرور ڪاميابي ملي ٿي.",
      pdf_page=13, book_page=13),
])

# === LESSON 3: حضرت امام جعفر صادق (PDF page 16 exercise) ===
SOLVED.extend([
    q(3, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "امام جعفر صادق عليہ السلام ڪهڙي سال ۽ ڪٿي پيدا ٿيا؟",
      "امام جعفر صادق عليہ السلام 80 هجري ۾ مدينه منوره ۾ پيدا ٿيا.",
      pdf_page=16, book_page=16),
    q(3, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "امام جعفر صادق عليہ السلام ڪهڙن علمن ۾ maharat حاصل ڪئي؟",
      "امام جعفر صادق عليہ السلام فقہ، حديث، قرآن، رياضيات، نجوم، ۽ ڪيميا ۾ maharat حاصل ڪئي.",
      pdf_page=16, book_page=16),
    q(3, SEC_LABEL['A'], 'A', 'short_answer', 3,
      "فقہ جعفري ڪهڙي طرح مشهور ٿي؟",
      "فقہ جعفري امام جعفر صادق عليہ السلام جي تعليمات ۽ فتوائن جي بنياد تي مشهور ٿي.",
      pdf_page=16, book_page=16),
    q(3, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"عبادين\" جو مطلب بيان ڪريو.",
      "عبادين جو مطلب آهي عبادت ڪندڙ يا پرستش ڪندڙ.",
      pdf_page=16, book_page=16),
])

# === LESSON 4: قائداعظم جا ارشاد (PDF page 20 exercise) ===
SOLVED.extend([
    q(4, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "قائداعظم محمد علي جناح ڪهڙا ٽي اصول پيش ڪيا؟",
      "قائداعظم ٽي اصول پيش ڪيا: اتحاد، تنظيم، ۽ يقين محكم.",
      pdf_page=20, book_page=20),
    q(4, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "اتحاد ڇو ضروري آهي؟",
      "اتحاد ضروري آهي ڇاڪاڻ ته متحد قوم ڪڏهن به غلام نٿي ٿي سگهي.",
      pdf_page=20, book_page=20),
    q(4, SEC_LABEL['A'], 'A', 'short_answer', 3,
      "يقين محكم ڪهڙي شيءِ آهي؟",
      "يقين محكم جو مطلب آهي پنهنجي مقصد ۽ خدا تي پورو اعتماد رکڻ.",
      pdf_page=20, book_page=20),
    q(4, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"نمازم يراڪرس\" جو مطلب بيان ڪريو.",
      "نمازم يراڪرس جو مطلب آهي قومي ترقي جا اصول.",
      pdf_page=20, book_page=20),
])

# === LESSON 5: اتحاد، تنظيم ۽ يقين محكم (PDF page 27 exercise) ===
SOLVED.extend([
    q(5, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "اتحاد و ضروري آهي؟",
      "اتحاد ضروري آهي ڇاڪاڻ ته متحد قوم ڪڏهن به غلام نٿي ٿي سگهي ۽ ترقي ڪري سگهي ٿي.",
      pdf_page=27, book_page=27),
    q(5, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "تنظيم ا آهي؟",
      "تنظيم جو مطلب آهي ڪنهن به ڪم کي ترتيب ۽ منصوبه بندي سان ڪرڻ.",
      pdf_page=27, book_page=27),
    q(5, SEC_LABEL['A'], 'A', 'short_answer', 3,
      "يقين محكم ڪهڙي شيءِ آهي؟",
      "يقين محكم جو مطلب آهي پنهنجي مقصد ۽ خدا تي پورو اعتماد رکڻ.",
      pdf_page=27, book_page=27),
    q(5, SEC_LABEL['B'], 'B', 'short_answer', 1,
      "اولا - رامان - يراهيم - يرگا - وکاڻ: هنن لفظن جا هم معنيٰ لفظ لکو.",
      "اولا = ابتدا، رامان = آرام، يراهيم = بزرگ، يرگا = رستو، وکاڻ = وڪرو.",
      pdf_page=27, book_page=27),
    q(5, SEC_LABEL['C'], 'C', 'short_answer', 1,
      "ڪامل ≠ ناقص، انتها ≠ ابتدا، ڦلاخ ≠ ڦل، بداخ ≠ بداخل: متضاد لفظ لکو.",
      "ڪامل ≠ ناقص، انتها ≠ ابتدا، ڦلاخ ≠ ڦل، بداخ ≠ بداخل.",
      pdf_page=27, book_page=27),
])

# === LESSON 6: مولانا دين محمد وفائي (PDF page 31 exercise) ===
SOLVED.extend([
    q(6, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "مولانا دين محمد وفائي ڪهڙي دور جا عالم هئا؟",
      "مولانا دين محمد وفائي جديد دور جا نامور عالم ۽ مصنف هئا.",
      pdf_page=31, book_page=31),
    q(6, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "مولانا صاحب ڪهڙيون خدمتون سرانجام ڏنيون؟",
      "مولانا صاحب سنڌي ادب ۽ تعليم جي ترقي ۾ اهم خدمتون سرانجام ڏنيون.",
      pdf_page=31, book_page=31),
    q(6, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"يريخ يام\" جو مطلب بيان ڪريو.",
      "يريخ يام جو مطلب آهي تاريخي جاءِ يا قديم مقام.",
      pdf_page=31, book_page=31),
])

# === LESSON 7: مائي خيري (PDF page 35 exercise) ===
SOLVED.extend([
    q(7, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "مائي خيري ڪهي حيثيت رکي ٿي؟",
      "مائي خيري سن جي مشهور لوڪ ڪهاي آهي جنهن ۾ هڪ عورت جي قرباني جو ذڪر آهي.",
      pdf_page=35, book_page=35),
    q(7, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "مائي خيري جي ڪهاڻي مان ڪهو سبق ملي ٿو؟",
      "مائي خيري جي ڪهاي مان سبق ملي ٿو ته ماءُ جي محبت بي مثال آهي.",
      pdf_page=35, book_page=35),
    q(7, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"يدازهش\" جو مطلب بيان ڪريو.",
      "يدازهش جو مطلب آهي يادگيري يا خاطره.",
      pdf_page=35, book_page=35),
])

# === LESSON 8: هنر دولت آهي (PDF page 37 exercise) ===
SOLVED.extend([
    q(8, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "هنر ڇو دولت آهي؟",
      "هنر دولت آهي ڇاڪاڻ ته هنر سان انسان روزگار حاصل ڪري سگهي و ۽ معاشي طور مضبوط ٿي سگهي ٿو.",
      pdf_page=37, book_page=37),
    q(8, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "هنر سکڻ ڇو ضروري آهي؟",
      "هنر سکڻ ضروري آهي اڪاڻ ته اهو انسان کي خودڪفيل بڻائي ٿو.",
      pdf_page=37, book_page=37),
    q(8, SEC_LABEL['B'], 'B', 'short_answer', 1,
      "داب ڪر وٽ: هن عبارت جو مطلب بيان ڪريو.",
      "داب ڪر وٽ جو مطلب آهي غور ڪريو ۽ سوچيو.",
      pdf_page=37, book_page=37),
])

# === LESSON 9: خط (PDF page 41 exercise) ===
SOLVED.extend([
    q(9, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "خط ڇا آهي؟",
      "خط هڪ تحريري ذريعو آهي جنهن ذريعي اسان پنهنجا خيال ۽ احساسات ٻين تائين پهچايون ٿا.",
      pdf_page=41, book_page=41),
    q(9, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "خط جا ڪهڙا قسم آهن؟",
      "خط جا ڪيترائي قسم آهن: رسمي خط، غير رسمي خط، تجارتي خط، وغيره.",
      pdf_page=41, book_page=41),
    q(9, SEC_LABEL['A'], 'A', 'short_answer', 3,
      "خط لکڻ جا ڪهڙا اصول آهن؟",
      "خط لکڻ جا اصول آهن: واضح لکڻ، مختصر هجڻ، ۽ مؤدبانه انداز اختيار ڪرڻ.",
      pdf_page=41, book_page=41),
    q(9, SEC_LABEL['B'], 'B', 'short_answer', 1,
      "ناجش - يزڪوس - ناجيها - گنو - ڻام - رواسيڻ: هم معنيٰ لفظ لکو.",
      "ناجش = ناڪام، يزڪوس = ڪوشش، ناجيها = ناکامي، گنو = ڳالهه، ڻام = نالو، رواسيڻ = روانو ڪرڻ.",
      pdf_page=41, book_page=41),
    q(9, SEC_LABEL['C'], 'C', 'short_answer', 1,
      "ڪرجا - نوٿيروم - رداچ - نوتملاع - اکلھ - وزيڪ - اهنس - وهزاگ: هم معنيٰ لفظ لکو.",
      "ڪرجا = ڪم، نوٿيروم = نظريو، رداچ = ردعمل، نوتملاع = تعلم، اکلھ = کل، وزيڪ = وزيت، اهنس = احساس، وهزاگ = وهڪرو.",
      pdf_page=41, book_page=41),
])

# === LESSON 10: بين الاقوامي عدالت (PDF page 45 exercise) ===
SOLVED.extend([
    q(10, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "بين الاقوامي عدالت ڪٿي واقع آهي؟",
      "بين الاقوامي عدالت هيگ، نيدرلينڊز ۾ واقع آهي.",
      pdf_page=45, book_page=45),
    q(10, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "بين الاقوامي عدالت جو ڪم ڇا آهي؟",
      "بين الاقوامي عدالت جو ڪم آهي قومن جي وچ ۾ تنازعاتن جو فيصلو ڪرڻ.",
      pdf_page=45, book_page=45),
    q(10, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"عدالت\" جو مطلب بيان ڪريو.",
      "عدالت جو مطلب آهي انصاف جو ادارو جتي قانون مطابق فيصلا ڪيا وڃن.",
      pdf_page=45, book_page=45),
])

# === LESSON 11: اجرڪ (PDF page 50 exercise) ===
SOLVED.extend([
    q(11, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "اجرڪ ا آهي؟",
      "اجرڪ سنڌ جو روايتي ٽيڪسٽائل آرٽ آهي جنهن ۾ خاص رنگن ۽ نقشن سان ڪپڙو ڇاپيو ويندو آهي.",
      pdf_page=50, book_page=50),
    q(11, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "اجرڪ جا ڪهڙا رنگ استعمال ٿيندا آهن؟",
      "اجرڪ ۾ مکيه طور تي ڳاڙهو، ڪارو، ۽ اڇو رنگ استعمال ٿيندا آهن.",
      pdf_page=50, book_page=50),
    q(11, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"ڪينجههر دند\" جو مطلب بيان ڪريو.",
      "ڪينجههر دند جو مطلب آهي ڪينجههر جهيل جو ڪنارو.",
      pdf_page=50, book_page=50),
])

# === LESSON 12: ميرن جي دربار (PDF page 54 exercise) ===
SOLVED.extend([
    q(12, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "ميرن جي دربار ڪي هوندي هئي؟",
      "ميرن جي دربار حيدرآباد ۾ هوندي هئي.",
      pdf_page=54, book_page=54),
    q(12, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "ميرن جي دور ۾ سنڌ ۾ ڪهڙيون تبديليون آيون؟",
      "ميرن جي دور ۾ سنڌ ۾ تعليم، ثقافت، ۽ فنون لطيفه جي ترقي ٿي.",
      pdf_page=54, book_page=54),
    q(12, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"درٻار\" جو مطلب بيان ڪريو.",
      "درار جو مطلب آهي بادشاهه يا حڪمران جو درٻار جتي مهمانن جو استقبال ٿيندو هو.",
      pdf_page=54, book_page=54),
])

# === LESSON 13: ڪينجههر دند (PDF page 58 exercise) ===
SOLVED.extend([
    q(13, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "ڪينجههر جهيل ڪٿي واقع آهي؟",
      "ڪينجههر جهيل ضلعي دادو ۾ واقع آهي.",
      pdf_page=58, book_page=58),
    q(13, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "ڪينجههر جهيل جي اهميت ڇا آهي؟",
      "ڪينجههر جهيل سنڌ جي سڀ کان وڏي مٺي پاڻيءَ جي جهيل آهي ۽ سياحت جو اهم مرڪز آهي.",
      pdf_page=58, book_page=58),
    q(13, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"رڏ پچاءُ\" جو مطلب بيان ڪريو.",
      "رڏ پچاءُ جو مطلب آهي پڪارڻ ۽ جواب ڏيڻ.",
      pdf_page=58, book_page=58),
])

# === LESSON 14: سني ادب جي مختصر تاريخ (PDF page 62 exercise) ===
SOLVED.extend([
    q(14, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "سنڌي ادب جي تاريخ ڪيتري پراڻي آهي؟",
      "سنڌي ادب جي تاريخ اٽڪل هزار سال پراڻي آهي.",
      pdf_page=62, book_page=62),
    q(14, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "سنڌي ادب ۾ ڪهڙا اهم دور آهن؟",
      "سنڌي ادب ۾ اهم دور آهن: قديم دور، وچولو دور، ۽ جديد دور.",
      pdf_page=62, book_page=62),
    q(14, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"پٽ بارهن\" جو مطلب بيان ڪريو.",
      "پٽ بارهن جو مطلب آهي ٻارهن مهينا يا سال جو هر مهينو.",
      pdf_page=62, book_page=62),
])

# === LESSON 15: رڏ پچاءُ (PDF page 65 exercise) ===
SOLVED.extend([
    q(15, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "رڏ پچاءُ ڇا آهي؟",
      "رڏ پچاءُ هڪ لوڪ ادبي صنف آهي جنهن ۾ هڪ شخص پڪاري ٿو ۽ ٻيو جواب ڏئي ٿو.",
      pdf_page=65, book_page=65),
    q(15, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "رڏ پچاءُ ڪٿي عام آهي؟",
      "رڏ پچاءُ سنڌ جي ديھي علائقن ۾ عام آهي.",
      pdf_page=65, book_page=65),
    q(15, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"نصرپور\" جو مطلب بيان ڪريو.",
      "نصرپور سنڌ جو هڪ تاريخي شهر آهي جيڪو پنهنجي دستڪاري لاءِ مشهور آهي.",
      pdf_page=65, book_page=65),
])

# === LESSON 16: پٽ بارهن (PDF page 68 exercise) ===
SOLVED.extend([
    q(16, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "پٽ بارهن ڇا آهي؟",
      "پٽ بارهن هڪ لوڪ گيت آهي جنهن ۾ سال جي ٻارهن مهينن جو ذڪر هوندو آهي.",
      pdf_page=68, book_page=68),
    q(16, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "پٽ بارهن ۾ ڪهڙا موضوع شامل آهن؟",
      "پ بارهن ۾ محبت، جدائي، ۽ فطرت جا موضوع شامل آهن.",
      pdf_page=68, book_page=68),
    q(16, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"جهڙو راج تهڙو پراڳ\" جو مطلب بيان ڪريو.",
      "جهڙو راج تهڙو پراڳ جو مطلب آهي جيئن حڪمران هوندو آهي تيئن ئي رعایا هوندي آهي.",
      pdf_page=68, book_page=68),
])

# === LESSON 17: نصرپور (PDF page 71 exercise) ===
SOLVED.extend([
    q(17, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "نصرپور ڪٿي واقع آهي؟",
      "نصرپور ضلعي نوشهرو فيروز ۾ واقع آهي.",
      pdf_page=71, book_page=71),
    q(17, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "نصرپور ڪهي شيءِ لاءِ مشهور آهي؟",
      "نصرپور پنهنجي دستڪاري، خاص طور تي رلي ۽ اجمڪ لاءِ مشهور آهي.",
      pdf_page=71, book_page=71),
    q(17, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"آهيون الف آسري\" جو مطلب بيان ڪريو.",
      "آهيون الف آسري جو مطلب آهي اسان الف کان شروع ڪريون ا.",
      pdf_page=71, book_page=71),
])

# === LESSON 18: جهڙو راج تهو پراڳ (PDF page 74 exercise) ===
SOLVED.extend([
    q(18, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "\"جهڙو راج تهڙو پراڳ\" جو مطلب ڇا آهي؟",
      "هن ضرب المثل جو مطلب آهي ته جيئن حڪمران هوندو آهي تيئن ئي رعایا هوندي آهي.",
      pdf_page=74, book_page=74),
    q(18, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "هي ضرب المثل ڪٿان ورتل آهي؟",
      "هي ضرب المثل سنڌي لوڪ ادب مان ورتل آهي.",
      pdf_page=74, book_page=74),
    q(18, SEC_LABEL['A'], 'A', 'short_answer', 3,
      "هن ضرب المثل مان ڪهو سبق ملي ٿو؟",
      "هن ضرب المثل مان سبق ملي ٿو ته حڪمرانن کي بهترين مثالن قائم ڪرڻ گهرجن.",
      pdf_page=74, book_page=74),
    q(18, SEC_LABEL['B'], 'B', 'short_answer', 1,
      "هن نظم جا اهم لفظ بيان ڪريو.",
      "راج = حڪومت، پراڳ = رعایا، جهڙو = جيان، تهڙو = تيان.",
      pdf_page=74, book_page=74),
    q(18, SEC_LABEL['C'], 'C', 'short_answer', 1,
      "هن نظم جا هم معنيٰ لفظ لکو.",
      "ڪا = آقا، پآ = پيءُ، يلپ = پٽ، هنوپ = هن، اراسپ = اراس.",
      pdf_page=74, book_page=74),
    q(18, SEC_LABEL['D'], 'D', 'short_answer', 1,
      "خالي جڳهون ڀريو: ____________ يج، ناڪ نهج ينايزوج",
      "جواب: اڙيڪ يج، ناڪ نهج ينايزوج.",
      pdf_page=74, book_page=74),
])

# === LESSON 19: آهيون الف آسري (PDF page 76 exercise) ===
SOLVED.extend([
    q(19, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "هي نظم ڪهڙي موضوع تي آهي؟",
      "هي نظم تعليم ۽ الف ب باري ۾ آهي.",
      pdf_page=76, book_page=76),
    q(19, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "الف ب ڇو ضروري آهي؟",
      "الف ب ضروري آهي ڇاڪاڻ ته اها تعليم جي بنياد آهي.",
      pdf_page=76, book_page=76),
    q(19, SEC_LABEL['A'], 'A', 'short_answer', 3,
      "هي نظم ڪهڙي سبق ئي ٿي؟",
      "هي نظم سبق ڏئي ٿي ته تعليم حاصل ڪرڻ ضروري آهي.",
      pdf_page=76, book_page=76),
    q(19, SEC_LABEL['B'], 'B', 'short_answer', 1,
      "هن نظم جا هم معنيٰ لفظ لکو.",
      "يؤخ = روشني، يلپ = پ، هنوپ = هن.",
      pdf_page=76, book_page=76),
    q(19, SEC_LABEL['C'], 'C', 'short_answer', 1,
      "هن نظم جا متضاد لفظ لکو.",
      "يڙؤخ ≠ اونداهي، يلپ ≠ ڌيءُ.",
      pdf_page=76, book_page=76),
    q(19, SEC_LABEL['D'], 'D', 'short_answer', 1,
      "خالي جڳهون ڀريو: ____________ يج، ناڪ نهج ينايزوج",
      "جواب: اڙيڪ يج، ناڪ نهج ينايزوج.",
      pdf_page=76, book_page=76),
])

# === LESSON 20: نيڪي (PDF page 78 exercise) ===
SOLVED.extend([
    q(20, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "نيڪي ڇا آهي؟",
      "نيڪي جو مطلب آهي چڱائي ڪرڻ ۽ ٻين جي مدد ڪرڻ.",
      pdf_page=78, book_page=78),
    q(20, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "نيڪي ڇو ضروري آهي؟",
      "نيڪي ضروري آهي ڇاڪاڻ ته اها معاشرے ۾ امن ۽ محبت پيدا ڪري ٿي.",
      pdf_page=78, book_page=78),
    q(20, SEC_LABEL['A'], 'A', 'short_answer', 3,
      "هي نظم ڪهڙي سبق ڏئي ٿي؟",
      "هي نظم سبق ڏئي ٿي ته اسان کي هميشه نيڪي ڪرڻ گهرجي.",
      pdf_page=78, book_page=78),
    q(20, SEC_LABEL['B'], 'B', 'short_answer', 1,
      "هن نظم جا هم معنيٰ لفظ لکو.",
      "يڙؤخ = روشني، يدنجرا = يادگيري.",
      pdf_page=78, book_page=78),
    q(20, SEC_LABEL['C'], 'C', 'short_answer', 1,
      "هن نظم جا متضاد لفظ لكو.",
      "مرڪ ≠ روئڻ، يدلب ≠ وسارڻ.",
      pdf_page=78, book_page=78),
    q(20, SEC_LABEL['D'], 'D', 'short_answer', 1,
      "\"نه\" ۽ \"وه\" جو فرق بيان ڪريو.",
      "\"نه\" جو مطلب آهي انڪار  \"وه\" جو مطلب آهي تعجب.",
      pdf_page=78, book_page=78),
])

# === LESSON 21: دعا (PDF page 80 exercise) ===
SOLVED.extend([
    q(21, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "دعا ڇا آهي؟",
      "دعا جو مطلب آهي الله تعالیٰ کان خير طلب ڪرڻ.",
      pdf_page=80, book_page=80),
    q(21, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "دعا ڇو ضروري آهي؟",
      "دعا ضروري آهي ڇاڪاڻ ته اها اسان کي الله تعالیٰ سان جوڙي ٿي.",
      pdf_page=80, book_page=80),
    q(21, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"سچل سرمست\" جو مطلب بيان ڪريو.",
      "سچل سرمست جو مطلب آهي هميشه مست ۽ خوش رہڻ وارو.",
      pdf_page=80, book_page=80),
])

# === LESSON 22: سچل سرمست (PDF page 82 exercise) ===
SOLVED.extend([
    q(22, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "سچل سرمست ڪهڙي دور جا شاعر هئا؟",
      "سچل سرمست اٺارهن صدي عيسوي جا نامور شاعر هئا.",
      pdf_page=82, book_page=82),
    q(22, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "سچل سرمست جي شاعري جا ڪها موضوع آهن؟",
      "سچل سرمست جي شاعري جا موضوع آهن: محبت، تصوف، ۽ انساني قدر.",
      pdf_page=82, book_page=82),
    q(22, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"ڊيئو\" جو مطلب بيان ڪريو.",
      "ڊيئو جو مطلب آهي چراغ يا روشني.",
      pdf_page=82, book_page=82),
])

# === LESSON 23: ڊيئو (PDF page 84 exercise) ===
SOLVED.extend([
    q(23, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "ڊيئو ا آهي؟",
      "ڊيئو جو مطلب آهي چراغ يا روشني جو ذريعو.",
      pdf_page=84, book_page=84),
    q(23, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "يئو جي علامت ا آهي؟",
      "ڊيئو علم ۽ روشني جي علامت آهي.",
      pdf_page=84, book_page=84),
    q(23, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"ٺاٺيون سڪ جو ڪو سنسار\" جو مطلب بيان ڪريو.",
      "هن جو مطلب آهي ته دنيا عارضي آهي ۽ هتي ڪجهه به دائمی ناهي.",
      pdf_page=84, book_page=84),
])

# === LESSON 24: ٺاٺيون سڪ جو ڪو سنسار (PDF page 86 exercise) ===
SOLVED.extend([
    q(24, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "هن نظم جو بنيادي پيغام ڇا آهي؟",
      "هن نظم جو بنيادي پيغام آهي ته دنيا عارضي آهي ۽ اسان کي آخرت جي تياري ڪرڻ گهرجي.",
      pdf_page=86, book_page=86),
    q(24, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "هن نظم مان ڪهڙو سبق ملي ٿو؟",
      "هن نظم مان سبق ملي ٿو ته اسان کي دنياوي مال ۽ دولت کان وڌيڪ اخلاقيات تي ڌيان ڏيڻ گهرجي.",
      pdf_page=86, book_page=86),
    q(24, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"پيارا وطن\" جو مطلب بيان ڪريو.",
      "پيارا وطن جو مطلب آهي پنهنجو پيارو ديس يا مادر وطن.",
      pdf_page=86, book_page=86),
])

# === LESSON 25: پيارا وطن (PDF page 88 exercise) ===
SOLVED.extend([
    q(25, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "وطن سان محبت ڇو ضروري آهي؟",
      "وطن سان محبت ضروري آهي ڇاڪاڻ ته اها اسان کي قومي سڃاڻپ ڏئي ٿي.",
      pdf_page=88, book_page=88),
    q(25, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "وطن جي ترقي ۾ اسان جو ڪهڙو ڪردار آهي؟",
      "وطن جي ترقي ۾ اسان جو ڪردار آهي ته اسان محنت ڪريون ۽ پنهنجي ذميواريون پوريون ڪريون.",
      pdf_page=88, book_page=88),
    q(25, SEC_LABEL['B'], 'B', 'fill_blank', 1,
      "\"هاري\" جو مطلب بيان ڪريو.",
      "هاري جو مطلب آهي زرعي ڪم ڪند يا ڪسان.",
      pdf_page=88, book_page=88),
])

# === LESSON 26: هاري (PDF page 90 exercise) ===
SOLVED.extend([
    q(26, SEC_LABEL['A'], 'A', 'short_answer', 1,
      "هاري ڪهڙي حيثيت رکي ٿو؟",
      "هاري ملڪ جي معيشت جو اهم ستون آهي اڪاڻ ته هو خوراڪ پيدا ڪري ٿو.",
      pdf_page=90, book_page=90),
    q(26, SEC_LABEL['A'], 'A', 'short_answer', 2,
      "هاري جون ڪهڙيون مشڪلاتون آهن؟",
      "هاري جون مشڪلاتون آهن: پاڻيءَ جي کو، قرض، ۽ مناسب اگهه نه ملڻ.",
      pdf_page=90, book_page=90),
    q(26, SEC_LABEL['A'], 'A', 'short_answer', 3,
      "هن نظم مان ڪهڙو سبق ملي ٿو؟",
      "هن نظم مان سبق ملي ٿو ته اسان کي هارين جو احترام ڪر گهرجي.",
      pdf_page=90, book_page=90),
    q(26, SEC_LABEL['A'], 'A', 'short_answer', 4,
      "هاري جي زندگي ڪهڙي آهي؟",
      "هاري جي زندگي محنت ۽ مشقت ڀريل آهي پر هو ملڪ لاءِ اهم ڪردار ادا ڪري ٿو.",
      pdf_page=90, book_page=90),
    q(26, SEC_LABEL['B'], 'B', 'short_answer', 1,
      "هن نظم جا اهم لفظ بيان ڪريو.",
      "هاري = ڪسان، يراھ = وطن، اراسيپ = امداد.",
      pdf_page=90, book_page=90),
    q(26, SEC_LABEL['C'], 'C', 'short_answer', 1,
      "هن نظم جا هم معنيٰ لفظ لکو.",
      "اراهڪس = مدد، رھجاس = رستو، لھم = گھر.",
      pdf_page=90, book_page=90),
    q(26, SEC_LABEL['D'], 'D', 'short_answer', 1,
      "خالي جڳهون ريو: يراھ پيارا، اراسيپ ____________",
      "جواب: يراھ پيارا، اراسيپ امداد.",
      pdf_page=90, book_page=90),
    q(26, SEC_LABEL['D'], 'D', 'short_answer', 2,
      "بلاگ جو مطلب بيان ڪريو: \"يهآ وشھس ناك نلگ ينھس لگ وج بلاگ\"",
      "بلاگ جو مطلب آهي هڪ قسم جو گيت يا نظم.",
      pdf_page=90, book_page=90),
])


def build():
    chapters = []
    total_questions = 0

    for lesson_num, title, start_page, exercise_page, section_type in LESSONS:
        # Collect questions for this lesson
        lesson_qs = [q for q in SOLVED if q["lesson"] == lesson_num]
        total_questions += len(lesson_qs)

        chapter = {
            "number": lesson_num,
            "title": title,
            "sectionType": section_type,
            "pdfPageStart": start_page,
            "pdfPageExercise": exercise_page,
            "totalQuestions": len(lesson_qs),
            "questions": lesson_qs,
        }
        chapters.append(chapter)

    # Build pages map: all 90 PDF pages
    pages = {}
    for i in range(1, 91):
        pages[str(i)] = f"/books/class_x/sindhi/pages/page_{i:03d}.webp"

    data = {
        "subject": "sindhi",
        "grade": "class_x",
        "board": "stbj",
        "totalPages": 90,
        "totalChapters": 26,
        "totalQuestionsSolved": total_questions,
        "chapters": chapters,
        "pages": pages,
    }

    output_path = r"d:\SubjectZone\public\data\class_x_sindhi.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Built class_x_sindhi.json: {total_questions} solved items across 26 lessons, 90 pages")
    return data


if __name__ == "__main__":
    build()
