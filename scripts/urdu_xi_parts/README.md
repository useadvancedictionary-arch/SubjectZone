# Gulzar-E-Urdu XI — part-file spec

Book: Sindh Textbook Board, Jamshoro — Gulzar-E-Urdu XI, 192 PDF pages.
Page images: `public/books/class_xi/urdu_gulzar/pages/page_XXX.webp`
(printed page number = PDF page number; footer numeral matches the file number).

The PDF has no usable text layer. Read the rendered page images.

## Book structure (TOC, actual starts may be ±3 pages)

Prose (حصہ نثر) — printed TOC serials 1–19 (page starts verified against TOC)
1. قومی اتفاق — سر سید احمد خان — p10
2. زبان گویا — مولانا الطاف حسین حالی — p16
3. فاقہ میں روزہ — خواجہ حسن نظامی — p20
4. پٹرولیم کی کہانی — آقاب حسن — p26
5. کیچ دھریجہ تعلیم کے باب میں — ڈاکٹر ابو اللیث صدیقی — p32
6. سندھی شعری کے تراجم — ڈاکٹر الیاس عشقی — p37
7. زبور کا دنتا — نفیسہ پریم چند — p43
8. با با نور — احمد ندیم قاسمی — p53
9. آب حیات — غلام ربانی آگرو (ترجمہ: ناہید انظر سومرو) — p60
10. میدان جنگ — آغا شاہ کریم شیری — p68
11. بیگم کی بیٹی — امتیاز علی تاج — p74
12. تھر کی نادیہ کلاچی — مستنصر حسین تارڑ — p85
13. مملکت بلقیس کا محسن — قمر علی عباسی — p90
14. خواہشوں کی لڑائی — شوکت تھانوی — p96
15. جیوڑیاں — شفیق الرحمن — p101
16. ایک تار اور چند پتھر — ابن انشاء — p105
17. جب نام میر مہدی مجروح — مرزا اسداللہ خان غالب — p109
18. خان محمد ناز الدین کے نام — ڈاکٹر سر علامہ محمد اقبال — p113
19. جب نام صدیق جاوید — مشفق خواجہ (کتبیات) — p116

NOTE: the earlier short list omitted TOC serial 4 «پیدائشی کہانی»; all prose
numbers below 4 are correct, all above 4 are shifted by one in that old list.
Parts labelled with the old numbering were renumbered (lessons 11–13 file).

Poetry (حصہ نظم)
20. حمد — ماہر القادری
21. نعت — اقبال عظیم
22. رے نام اللہ کا — ظہیر اکبر آبادی
23. داستانِ تیتری میں باغ کی (مثنوی) — میر حسن
24. یا رب! چمن نظم کو ... (مرثیہ) — میر انیس
25. چیخ کی داد — خواجہ الطاف حسین حالی
26. مردِ مسلمان — ڈاکٹر سر علامہ محمد اقبال
27. نوائے سروش — احسان دانش
28. رباعیات — میر انیس / جوش / صادق دہلوی
29. تن بہ تقدیر (قطعہ) — ڈاکٹر سر علامہ محمد اقبال
30. محکم (قطعہ) — رئیس امروہوی
31. سائیڈ ایفیکٹس (شعری مزاح) — انور مسعود
32. جانِ میری زمیں (طویل نظم) — ساقی جاوید
33. افتتاح (آزاد نظم) — انور عارف
34. مشورہ (آزاد نظم) — پروین شاکر
35. غزلیات — خواجہ میر درد
36. غزلیات — میر تقی میر
37. غزلیات — خواجہ حیدر علی آتش
38. غزلیات — مرزا اسداللہ خان غالب
39. غزل — داغ دہلوی
40. غزل — حسرت موہانی
41. غزل — منیر نیازی
42. غزل — احمد فراز
43. غزل — قائل امرہوی
44. پیامِ لطیف — آنکھ صداقت
(Verbatim titles on the TOC must be used if they differ.)

Pages 181–192 are the glossary (فہرست); no exercises there.
Pages 5–9 are teacher guidance; page 10 is lesson 1.

Each lesson is followed by a **مشق** block (pink headings: سوال نمبر 1 ...). Solve
every numbered question and every sub-part (الف، ب، ج، د ...; MCQ options 1–4).
Some lessons also carry a "سرگرمی" writing-skill page — it has guidance, not
numbered questions; do not invent items for it.

## Item schema (JSON array, UTF-8)

```json
{
  "id": "gulzar_xi_l01_q1a",
  "lesson": 1,
  "section": "مشق",
  "sectionCode": "L01",
  "type": "sq",
  "number": "1(الف)",
  "question": "…verbatim Urdu question…",
  "answer": "…answer…",
  "explanation": "…how/where the answer is found, or defect note…",
  "bookPage": 13,
  "options": null,
  "optionsRaw": null,
  "correctAnswer": null
}
```

- `type`: `"sq"` for short/descriptive questions, `"mcq"` for multiple choice.
- MCQ items: `options` = `[{"key":"a","text":"…"}, …]` (four), `optionsRaw` =
  `"(a) …   (b) …   (c) …   (d) …"`, `correctAnswer` = `"(b) …"`.
- `number` should mirror the printed tag, e.g. `1(الف)`, `3-2`, `5`.
- `bookPage` = PDF page number where the question is printed.
- Questions are copied verbatim (do not correct printed spelling).
- Answers are in Urdu; quote the text for comprehension answers.
- Summaries (خلاصہ) and essays (مضمون) get a model answer plus an explanation
  that other valid answers are acceptable.
- Never merge two printed questions into one item and never skip a sub-part.
