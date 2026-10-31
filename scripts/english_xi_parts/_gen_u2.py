# -*- coding: utf-8 -*-
"""Generate unit_02.json for English XI (Unit 2 - Preservation of Nature)."""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'unit_02.json')
items = []


def add(**kw):
    items.append(kw)


def mcq(id, num, q, opts, correct, ans, expl, page):
    keys = 'abcd'
    options = [{'key': keys[i], 'text': t} for i, t in enumerate(opts)]
    add(id=id, sectionCode='U2S1', type='mcq', number=str(num), question=q,
        answer=ans, explanation=expl, bookPage=page, options=options,
        optionsRaw='   '.join('(%s) %s' % (o['key'], o['text']) for o in options),
        correctAnswer='(%s) %s' % (keys[correct], opts[correct]))


# ---------------------------------------------------------------- PRE-READING
add(id='u2_r_pre_q1', sectionCode='U2S1', type='sq', number='1',
    question='Look at the pictures and compare and contrast them.',
    answer=(
        "The left-hand picture shows a mountain lake that is still unspoiled: clear turquoise water, "
        "a pine forest along the shore, snow-capped peaks reflected in the lake, and no people or litter in sight. "
        "The right-hand picture shows a city waterway that has been badly polluted: grey, muddy water, heaps of "
        "plastic bags and rubbish on the bank and in the water, a concrete bridge and high-rise buildings behind, "
        "and people picking through the waste.\n\n"
        "Similarities: both are inland water bodies with banks and shallow edges; both are fed by rain and streams "
        "and would normally support fish, birds and plants; both are part of a landscape that people use for travel, "
        "work or leisure.\n\n"
        "Differences: the lake is clear and silent, the waterway is grey and noisy; the lake is framed by trees and "
        "mountains, the waterway by concrete and traffic; the lake is clean, the waterway is choked with plastic; the "
        "lake suggests solitude, the waterway suggests overcrowding. In short, the first picture shows nature "
        "preserved and the second shows nature degraded by human waste."),
    explanation=(
        "Open-ended pre-reading task: any two valid similarities and two differences are acceptable. The aim is to "
        "activate the language of comparison and contrast (both, whereas, unlike, in contrast) and to predict the "
        "unit theme. Encourage students to notice colour, clarity, setting and human presence."),
    bookPage=18)

add(id='u2_r_pre_q2', sectionCode='U2S1', type='sq', number='2',
    question='Guess the theme of the text you are going to study.',
    answer=(
        "The theme is the preservation of nature, seen through a personal return to a childhood lake. The pair of "
        "pictures sets an unspoiled lake against a polluted city waterway, the unit is titled 'Preservation of "
        "Nature', and the text is called 'Once More to the Lake'. The title suggests a nostalgic journey back to a "
        "natural place that may have been changed by modern life. The extract confirms this: the writer revisits a "
        "lake in Maine after many years, wonders how time and the new tarred road have 'marred' it, and is disturbed "
        "by outboard motors and crowds. So the text is about memory, the passing of time, and the need to protect "
        "natural places."),
    explanation=(
        "Open-ended prediction. A good answer names the theme (preservation of nature / nostalgia for an unspoiled "
        "place) and supports it with the unit title, the text title and the picture contrast."),
    bookPage=18)

# ------------------------------------------------------------ WHILE-READING 1
add(id='u2_r_ex1', sectionCode='U2S1', type='sq', number='Exercise 1',
    question=('Work in pairs and deduce the meaning of words given in column A and write their contextual meaning '
              'in column B.'),
    answer=(
        "No. | Column A | Column B (contextual meaning)\n"
        "1 | marred | spoilt, damaged or disfigured in appearance - the writer fears time has spoilt 'this unique, "
        "this beautiful spot'\n"
        "2 | tarred | covered with tar, a black sticky substance used to make a hard road surface - 'the tarred "
        "road' that now reaches the lake\n"
        "3 | grooves | narrow tracks or ruts; here, the familiar channels or paths of memory that the mind follows "
        "- 'return into the grooves which lead back'\n"
        "4 | sneak | move quietly and secretly so as not to be noticed - he would 'sneak out into the sweet "
        "outdoors' before the others woke\n"
        "5 | illusion | a false impression or belief; something that seems real but is not - 'the illusion that he "
        "was I'\n"
        "6 | creepy | causing an uneasy, frightened, 'goose-flesh' feeling - 'It gave me a creepy sensation'\n"
        "7 | moss | a small, soft green plant that grows in damp places - 'the same damp moss covering the worms'\n"
        "8 | jollity | cheerful, merry, lively happiness - 'There had been peace and goodness and jollity'\n"
        "9 | sedative | calming, soothing, making a person sleepy - the inboard motors' noise was 'a sedative, an "
        "ingredient of summer sleep'\n"
        "10 | petulant | irritable, bad-tempered, peevish - the outboard motors made 'a petulant, irritable sound'"),
    explanation=(
        "Meanings are deduced from context, not copied from a dictionary: each word is defined by the phrase in "
        "which it appears. Accept close synonyms (marred = spoiled; grooves = familiar tracks/patterns; jollity = "
        "cheerfulness; sedative = soothing; petulant = cranky)."),
    bookPage=21)

# ------------------------------------------------------------ WHILE-READING 2
mcq('u2_r_ex2_q1', 1,
    "The writer in the essay 'Once More to the Lake' is accompanied by his ______.",
    ['brother', 'son', 'wife', 'pet'], 1, '(b) son',
    "Text: 'I took along my son, who had never had any fresh water up his nose and who had seen lily pads only "
    "from train windows.' The boy is with him throughout the return visit, so (b) is correct; no brother, wife or "
    "pet is mentioned as making the trip.",
    21)

mcq('u2_r_ex2_q2', 2,
    "In the beginning of 'Once More to the Lake', the writer characterizes himself as ______.",
    ['lake-water man', 'pond-water man', 'salt-water man', 'ordinary man'], 2, '(c) salt-water man',
    "In the essay White says he has 'since become a salt-water man' - as an adult he lives by the sea - though in "
    "summer he longs for the placidity of a lake in the woods. The abridged textbook extract omits that sentence, "
    "but the question tests it, so the intended answer is (c). He is not a pond-water man, and 'ordinary man' "
    "ignores the specific phrase.",
    21)

mcq('u2_r_ex2_q3', 3,
    'The writer has referred the word "placidly" in the context of ______.',
    ['peacefulness', 'calmness', 'loneliness', 'idleness'], 1, '(b) calmness',
    "'Placid' means calm, still and undisturbed. The extract describes the lake as 'cool and motionless', as water "
    "that 'had not stirred', 'this constant and trustworthy body of water'. 'Calmness' is therefore the closest "
    "meaning; 'peacefulness' is related but refers more to mood than to the water's stillness, while loneliness and "
    "idleness are unrelated.",
    21)

mcq('u2_r_ex2_q4', 4,
    'The ______ were/was tapping on the roof of the camp of writer.',
    ['mosquitoes', 'swarm', 'squirrel', 'mouse'], 2, '(c) squirrel',
    "Text: 'in the morning, the red squirrel would be on the roof, tapping out his happy routine.' Mosquitoes "
    "appear only in a simile for the whine of outboard motors at night, and no swarm or mouse is mentioned.",
    21)

mcq('u2_r_ex2_q5', 5,
    'The writer felt in the end of the essay ______.',
    ['the fear of storm', 'the danger of life', 'happy', 'the loneliness'], 2, '(c) happy',
    "The extract closes with 'We had a good week at the camp', sunshine 'day after day', sleep that 'would come "
    "easily' and the squirrel's 'happy routine', while the writer lies in bed 'remembering everything' - a mood of "
    "contentment. (The unabridged essay ends more darkly with a thunderstorm, but that passage is not in the "
    "printed text.)",
    22)

mcq('u2_r_ex2_q6', 6,
    '______ caught two fish before lunch.',
    ['son', 'father', 'both son & father', 'spinner'], 2, '(c) both son & father',
    "Text: 'We caught two fish. When we got back for a swim before lunch...' The pronoun 'we' refers to the writer "
    "and his son fishing together, so both caught the fish. A spinner is only the lure the writer bought; it cannot "
    "catch fish by itself.",
    22)

mcq('u2_r_ex2_q7', 7,
    'The writer revisited the lake with his son in ______ season.',
    ['summer', 'winter', 'autumn', 'spring'], 0, '(a) summer',
    "The family went 'for the month of August' and 'returned summer after summer--always on August 1st'; the "
    "writer's own return with his son is also a summer visit.",
    22)

mcq('u2_r_ex2_q8', 8,
    "The writer's son has seen ______ while travelling by train.",
    ['weeds', 'lily pads', 'sheltered bay', 'wet woods'], 1, '(b) lily pads',
    "Text: 'who had seen lily pads only from train windows' - the boy knew lily pads only as a glimpse from a "
    "train, never up close.",
    22)

mcq('u2_r_ex2_q9', 9,
    'The writer used to visit lake ______.',
    ['in New York', 'in Maine', 'near his form house', 'in his school'], 1, '(b) in Maine',
    "Text: 'my father rented a camp on a lake in Maine'; the title and the whole return journey point to that lake "
    "in Maine. New York, his former house and his school are not named as the lake's location.",
    22)

mcq('u2_r_ex2_q10', 10,
    'For ______, the writer used to go to the lake.',
    ['fishing', 'seeing waves', 'enjoying cool water', 'enjoying swimming'], 0, '(a) fishing',
    "Text: 'returned to the lake where we used to go, for a week's fishing and to revisit old place.' Fishing is "
    "the stated purpose; waves, cool water and swimming are incidental pleasures, not the reason given.",
    22)

# ------------------------------------------------------------ WHILE-READING 3
add(id='u2_r_ex3', sectionCode='U2S1', type='sq', number='Exercise 3',
    question=('Read the text individually. First, write the five things that writer observed and loved in the past. '
              'Then, write five changes that took place later on.'),
    answer=(
        "Past scene of lake | Later scene\n"
        "1. Cool, motionless early mornings, with the bedroom smelling of lumber and wet woods and the lake misty "
        "and still. | 1. The mornings are still calm, but the silence is broken by 'an unfamiliar nervous sound of "
        "the outboard motors'.\n"
        "2. Canoeing alone close to the shore 'in the long shadows of the pines' before the others woke. | 2. The "
        "writer now comes as a father with his son, and feels that he is his own father - 'I seemed to be living a "
        "dual existence'.\n"
        "3. Inboard one- and two-cylinder motors: 'The one-lungers throbbed and fluttered, and the twin-cylinder "
        "ones purred and purred' - a sleepy, sedative sound. | 3. 'But now the campers all had outboards', which "
        "make 'a petulant, irritable sound' by day and 'whined about one's ears like mosquitoes' at night.\n"
        "4. A quiet, half-wild lake with cottages 'sprinkled around the shores', where the family lived at the "
        "shore and ate meals at the farmhouse. | 4. The tarred road now 'led to within half a mile of the shore', "
        "and other campers crowd the shore and the water - the place is easy to reach and no longer remote.\n"
        "5. The same boat, moss, dragonfly, waves and red squirrel, and 'peace and goodness and jollity' - a world "
        "where 'the years were a mirage'. | 5. The years move again: the writer sees his son reliving his own "
        "boyhood and feels the 'creepy' pressure of time and ageing."),
    explanation=(
        "The extract deliberately stresses continuity (the lake, boat, moss, dragonfly and squirrel are unchanged), "
        "so the 'later scene' column records the changes the writer actually registers: outboard motors, easier "
        "road access, more campers and cottages, and his own changed role as a father. Wording may vary, but every "
        "point must be text-based."),
    bookPage=22)

# ------------------------------------------------------------ WHILE-READING 4
add(id='u2_r_ex4', sectionCode='U2S1', type='sq', number='Exercise 4',
    question=('Analyse the text and write five examples of similes, and five examples of metaphors in respective '
              'columns.'),
    answer=(
        "No. | Similes | No. | Metaphors\n"
        "1 | 'they whined about one's ears like mosquitoes' - the outboard motors are compared to mosquitoes with "
        "the word 'like' (the one strict simile in the extract). | 1 | 'the years were a mirage' - time is called an "
        "optical illusion, as if the past had never happened.\n"
        "2 | 'none of us ever thought there was any place in the world like that lake in Maine' - the lake is "
        "compared with every other place through 'like' (hyperbolic comparison). | 2 | 'This seemed an utterly "
        "enchanted sea' - the fresh-water lake is called a magical sea.\n"
        "3 | 'It is strange how much you can remember about places like that' - remembered places are compared to "
        "the lake through 'like' (implied comparison). | 3 | 'the noise they made was a sedative, an ingredient of "
        "summer sleep' - sound is described as a drug and as an ingredient of sleep.\n"
        "4 | 'the water felt thin and clear and insubstantial' - the water is compared to something almost without "
        "substance (implied simile). | 4 | 'this constant and trustworthy body of water' - the lake is given the "
        "human quality of trustworthiness (personification).\n"
        "5 | 'I began to sustain the illusion that he was I ... that I was my father' - father and son are compared "
        "by identity, as if they were the same person (implied comparison). | 5 | 'each fish with its small, "
        "individual shadow, doubling the attendance' - the shadows are treated as extra guests at a gathering."),
    explanation=(
        "The printed extract is heavily abridged and contains only one full simile with 'like' ('like mosquitoes'); "
        "the textbook nevertheless asks for five. Rows 2-5 of the simile column are therefore the passage's other "
        "comparative constructions, clearly implied rather than stated with 'like/as'. The metaphor column is "
        "straightforward. If strict similes are required, the class can add examples from the full essay; the "
        "important skill is distinguishing 'like/as' comparison from direct metaphorical identification."),
    bookPage=23)

# -------------------------------------------------------------- POST-READING
add(id='u2_r_ex5_q1', sectionCode='U2S1', type='sq', number='1',
    question='Why does writer take a vacation at this particular lake?',
    answer=(
        "Because the lake is the place of his boyhood holidays and his happiest family memories. His father rented "
        "a camp there in 1904 and the family returned every August; he says 'none of us ever thought there was any "
        "place in the world like that lake in Maine.' As an adult 'this feeling got so strong' that he bought 'a "
        "couple of fish hooks and a spinner' and went back 'for a week's fishing and to revisit old place'. He also "
        "takes his son so that the boy can experience the same fresh-water world that he knew."),
    explanation=(
        "The opening paragraph supplies the reason: a lifelong attachment formed in childhood, strengthened by "
        "years of family holidays, and a wish to relive the place. The son's presence makes the visit a link "
        "between generations."),
    bookPage=23)

add(id='u2_r_ex5_q2', sectionCode='U2S1', type='sq', number='2',
    question='Which key concerns the writer has expressed in the text?',
    answer=(
        "The writer's key concerns are:\n"
        "(i) whether time and modern 'improvements' have spoilt the place - 'I wondered how time would have marred "
        "this unique, this beautiful spot';\n"
        "(ii) whether the tarred road has 'found it out' and 'in what other ways it would be desolated';\n"
        "(iii) the passing of time and his own ageing, felt as the 'creepy' sense of living a 'dual existence' in "
        "which he is both himself and his father;\n"
        "(iv) the loss of the lake's quiet, wild quality to outboard motors and to crowds of campers.\n"
        "Underlying all four is the larger concern for the preservation of nature."),
    explanation=(
        "These are the anxieties announced in the introduction ('how time would have marred...') and developed "
        "during the visit (the road, the outboards, the dual existence). The question asks for 'concerns', so the "
        "answer should group them rather than retell the story."),
    bookPage=23)

add(id='u2_r_ex5_q3', sectionCode='U2S1', type='sq', number='3',
    question='How has the lake changed since he was a boy?',
    answer=(
        "The lake itself has hardly changed: the water is 'exactly where we had left it', the boat is 'the same "
        "boat' with its ribs broken in the same places, and the moss, dragonfly, waves and red squirrel are all the "
        "same. What has changed is the human setting. In the past 'all motors were inboard' and made a sleepy, "
        "sedative sound; 'now the campers all had outboards' whose 'petulant, irritable' noise and mosquito-like "
        "whine break the stillness. The tarred road now 'led to within half a mile of the shore', so the lake is "
        "easy to reach, and cottages and other campers crowd the shores. The writer himself has changed from boy to "
        "father."),
    explanation=(
        "White separates the natural lake (unchanged) from its human use (changed). The only thing 'wrong now' is "
        "the sound of the outboard motors, which 'would sometimes break the illusion and set the years moving'."),
    bookPage=23)

add(id='u2_r_ex5_q4', sectionCode='U2S1', type='sq', number='4',
    question='What contrast does the writer make between the sea and the lake?',
    answer=(
        "The sea is restless, tidal and cold, while the lake is still, 'constant and trustworthy'. He calls the "
        "lake 'an utterly enchanted sea, this lake you could leave to its own devices for a few hours and come "
        "back to, and find that it had not stirred'. In the full essay he says he has 'since become a salt-water "
        "man', yet in summer he longs for 'the placidity of a lake in the woods'. The sea moves, rises and falls "
        "and changes; the lake holds still and seems to preserve time."),
    explanation=(
        "The contrast is between movement/change (sea) and stillness/continuity (lake). The phrase 'an utterly "
        "enchanted sea' makes the lake a magical, gentler version of the sea. The 'salt-water man' sentence is from "
        "the original essay and is the basis of MCQ 2 of Exercise 2."),
    bookPage=23)

add(id='u2_r_ex5_q5', sectionCode='U2S1', type='sq', number='5',
    question="Why does writer repeatedly call the lake as 'wild lake'?",
    answer=(
        "He uses 'wild lake' for the lake of memory - a secluded, unspoilt, pine-shadowed sheet of water where a "
        "boy could canoe alone in the early morning and feel close to untouched nature. He immediately qualifies "
        "the phrase, however: 'The lake had never been what you would call a wild lake', since cottages, farms and "
        "campers were always around it. The expression therefore conveys his romantic, idealised view of the place "
        "rather than literal wilderness; the 'wildness' is in his memory, and it is exactly what modern noise and "
        "crowds threaten."),
    explanation=(
        "The text actually denies that the lake was wild ('had never been what you would call a wild lake'), so a "
        "good answer notes the qualification: the word reflects the writer's boyish impression and his longing for "
        "an unspoilt place, not a geographical fact."),
    bookPage=23)

add(id='u2_r_ex5_q6', sectionCode='U2S1', type='sq', number='6',
    question='Why is the arriving at the lake less exciting now than in the past?',
    answer=(
        "Because the mystery and difficulty of the journey are gone. As a boy the lake was reached after a long, "
        "eagerly awaited trip, and part of the excitement was wondering whether the 'tarred road would have found "
        "it out'. Now the tarred road 'led to within half a mile of the shore', so the place is easy to reach; he "
        "knows 'it was going to be pretty much the same as it had been before' and can predict everything. "
        "Familiarity, easy access and the noise of outboards replace the surprise and adventure of childhood, and "
        "he is no longer the child for whom the trip was a great event."),
    explanation=(
        "The text links the loss of excitement to the tarred road and to the writer's certainty that nothing had "
        "changed: anticipation depends on uncertainty, and the road has removed it."),
    bookPage=23)

add(id='u2_r_ex5_q7', sectionCode='U2S1', type='sq', number='7',
    question='How are the boat motors different in the present situation?',
    answer=(
        "In the past 'all motors were inboard' - one-cylinder engines that 'throbbed and fluttered' and "
        "two-cylinder engines that 'purred and purred', making a 'sleepy', 'sedative' sound that was 'an ingredient "
        "of summer sleep'. Now 'the campers all had outboards': in the hot mornings they make 'a petulant, "
        "irritable sound', and at night 'they whined about one's ears like mosquitoes'. The change turns a soothing "
        "sound into a jarring, 'unfamiliar nervous sound' that 'break[s] the illusion and set[s] the years "
        "moving'."),
    explanation=(
        "The contrast is in both mechanism (inboard vs outboard) and effect (sleepy/sedative vs petulant/whining). "
        "The noise is 'the only thing that was wrong now' and the one detail that destroys the writer's sense of "
        "timelessness."),
    bookPage=23)

add(id='u2_r_ex5_q8', sectionCode='U2S1', type='sq', number='8',
    question="The writer calls the lake as a 'holy spot'. How does he further develop this idea?",
    answer=(
        "He develops the idea by making the return a pilgrimage and a ritual. He travels back to 'revisit old "
        "place'; he remembers the smallest sensory details - the smell of lumber and wet woods, the damp moss, the "
        "dragonfly on the rod tip, the waves chucking the rowboat - as if reciting a sacred litany. The lake is "
        "'this unique, this beautiful spot', 'an utterly enchanted sea', a place of 'peace and goodness and "
        "jollity' where 'the years were a mirage and there had been no years'. Its 'holiness' lies in its power to "
        "erase time and to join three generations - his father, himself and his son - in one continuous "
        "experience."),
    explanation=(
        "The exact phrase 'holy spot' is not printed in the abridged extract, which says 'this unique, this "
        "beautiful spot'; the idea of a sacred place is developed through ritual return, reverent sensory memory "
        "and the language of enchantment and timelessness. Accept answers that trace these features."),
    bookPage=23)

add(id='u2_r_ex5_q9', sectionCode='U2S1', type='sq', number='9',
    question='What kind of sensation persisted and grew in the mind of the writer?',
    answer=(
        "The 'creepy sensation' of a dual existence - the illusion 'that he was I, and therefore, by simple "
        "transposition, that I was my father'. It 'persisted, kept cropping up all the time we were there' and 'in "
        "this setting it grew much stronger', so that in the middle of ordinary acts (picking up a bait box, laying "
        "down a table fork, speaking) he felt it was 'not I but my father who was saying the words or making the "
        "gesture'. It is the sensation of time collapsing and of living two lives - his father's and his own - at "
        "once."),
    explanation=(
        "The sensation is introduced as an 'illusion', becomes a 'dual existence', and is described as 'creepy' "
        "because it undermines his sense of a single, separate self. The dragonfly and the unchanged boat "
        "strengthen it."),
    bookPage=23)

add(id='u2_r_ex5_q10', sectionCode='U2S1', type='sq', number='10',
    question='What is the central idea of the text?',
    answer=(
        "The central idea is the continuity of life and the preservation of nature: a place loved in childhood can "
        "seem unchanged, and a father can relive his own boyhood through his son, yet time does move and the modern "
        "world - roads, outboard motors, crowds - steadily alters the places we love. The lake gives the writer a "
        "sense of timelessness ('the years were a mirage'), peace and 'jollity', and teaches him that such places "
        "must be valued and protected, because they connect generations and hold memory."),
    explanation=(
        "A good answer links the personal theme (memory, ageing, father-son continuity) with the unit theme "
        "(preservation of nature). The text's closing emphasis on remembered happiness supports the positive, "
        "elegiac tone."),
    bookPage=23)

add(id='u2_r_ex6', sectionCode='U2S1', type='sq', number='Exercise 6',
    question=('Work individually and recollect your past impression of natural things of your city or village. '
              'Enlist these all and also write the changes that have taken place now. Share all these with the '
              'class.'),
    answer=(
        "Natural thing | My past impression | The change today\n"
        "1. The stream / pond near my village | Clear water, fish, buffaloes cooling in it, children swimming, reeds "
        "and kingfishers. | Sewage and plastic bags, a silted bed, no fish; the banks are used as a dumping ground.\n"
        "2. The mango orchard on the edge of the town | Dense shade, koels and parrots, fallen fruit, a cool breeze "
        "in May. | Cut down for a housing scheme; only two old trees remain and the ground is paved.\n"
        "3. The seashore | Clean sand, shells, crabs and a few fishermen's boats. | A crowded promenade, food "
        "wrappers and plastic bottles, jet skis and noise.\n"
        "4. The night sky | Stars and the Milky Way clearly visible; frogs and crickets loud after rain. | Light "
        "pollution hides most stars; fewer frogs and crickets because of pesticides and concrete.\n"
        "5. The monsoon | Gentle, predictable rains that filled tanks and ponds; the smell of wet earth. | Erratic, "
        "short, heavy downpours that flood the streets and are followed by long dry spells.\n"
        "6. The sparrows and kites | Sparrows nesting under the eaves; kites circling all afternoon. | Sparrows "
        "almost gone; fewer kites, while crows and pigeons have increased.\n"
        "7. The farmland at the edge of the city | Wheat and vegetables, earthworms in the soil, bullock carts. | "
        "Factories and plots; the soil is hard and full of rubble.\n"
        "8. The old banyan tree at the crossroads | A shady meeting place, squirrels and mynahs, elders chatting in "
        "the evening. | Cut down for road-widening; a concrete bus stop stands in its place."),
    explanation=(
        "Open-ended personal response: the table is a model, and every student's list will differ. Keep the two "
        "columns parallel - past impressions in the past tense, present changes in the present perfect or present "
        "tense - and end with a sentence saying what should be preserved."),
    bookPage=23)

json.dump(items, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(len(items), 'items written')
