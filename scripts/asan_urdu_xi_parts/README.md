# Asan Urdu XI — part-file spec

Book: Sindh Textbook Board, Jamshoro — Asan Urdu XI (printed cover: آسان اردو گیارہویں جماعت کے لیے), 88 PDF pages.
Page images: `public/books/class_xi/asan_urdu_xi/pages/page_XXX.webp`
(printed page number = PDF page number).

The PDF text layer only carries Urdu page numerals, so read the rendered pages.

## Lessons (TOC page = PDF page)

1. حمد (نظم) — ابوالاثر حفیظ جالندھری — p5
2. نبی کریم ﷺ کی ہجرت — علامہ سید سلیمان ندوی — p8
3. نام وہ ادبیوں کے خطوط — غالب، اکبر، شبلی، نذیر احمد، سر سید — p12
4. حبِ وطن (نظم) — مولانا حالی — p16
5. جیسی کرنی ویسی بھرنی — خواجہ حسن نظامی — p19
6. ایران کا بادشاہ — مولوی محمد حسین آزاد — p23
7. آدمی نامہ (نظم) — نظیر اکبر آبادی — p26
8. نصوح کا خواب — مولوی نذیر احمد — p29
9. اسلامی حکومت کا امیر سب کا خادم ہوتا ہے — p33
10. آسمان اور تارے (نظم) — مولوی محمد اسماعیل میرٹھی — p36
11. سب سے بڑا اسلامی شاعر — p38
12. چچا کبر — نفیسہ پریم چند — p40
13. رباعیات (نظم) — انیس، حالی، اکبر، واعظ — p47
14. ایک وصیت کی تعمیل — مرزا فرحت اللہ بیگ — p51
15. پاکستان کے لیے پہلا جہاد — مؤلف — p56
16. طالبِ علموں کے نام سرسید کا ایک خط — سرسید احمد خان — p60
17. مردِ مجاہد (نظم) — مولوی شفیع الدین نیر — p63
18. اردو کی آخری کتاب — پطرس بخاری — p66
19. مولانا محمد علی جوہر — مولانا عبدالماجد دریا آبادی — p69
20. آمدِ بہار (نظم) — احمد علی شوق قدوائی — p73
21. اردو کی کہانی — مولوی عبدالحق — p76
22. حضرت صدیق اکبرؓ ایک شاعر (نظم) — علامہ اقبال — p79
23. اسلامی کردار دار — مؤلف — p81
24. میر معصوم شاہ بکھری — عبدالواحد سندھی — p85

Lessons run from page 5 to page 88; the book contains 24 lessons, not 14.
Each lesson's exercise is labelled **مشق** on the page following the text; it
has lettered parts (الف، ب، ج، د) with 1–10 numbered questions. Some lessons
also carry **اشارے** (explanatory notes) — those are reference notes, not
questions; do not create items from them.

## Item schema (JSON array, UTF-8)

```json
{
  "id": "asan_xi_l01_q1",
  "lesson": 1,
  "section": "مشق",
  "sectionCode": "L01",
  "type": "sq",
  "number": "1",
  "question": "…verbatim Urdu question…",
  "answer": "…answer…",
  "explanation": "…how/where the answer is found…",
  "bookPage": 7,
  "options": null,
  "optionsRaw": null,
  "correctAnswer": null
}
```

- `type`: `"sq"` for short/descriptive questions, `"mcq"` for multiple choice.
- MCQ items: `options` = `[{"key":"a","text":"…"}, …]` (four), `optionsRaw` =
  `"(a) …   (b) …   (c) …   (d) …"`, `correctAnswer` = `"(b) …"`.
- `number` mirrors the printed tag, e.g. `1`, `2`, `(الف)-1` when needed to
  disambiguate lettered sections.
- `bookPage` = PDF page number where the question is printed.
- Copy questions verbatim (keep printed spelling); answers in Urdu.
- Zero omission: every numbered question and lettered part is its own item.
