import json

with open(r'd:\SubjectZone\public\data\class_x_chemistry.json', encoding='utf-8') as f:
    data = json.load(f)

print("Total questions:", data['totalQuestionsSolved'])
for ch in data['chapters']:
    print(f"Chapter {ch['number']}: {ch['title']} -> {ch['totalQuestions']} questions")
    sample_q = ch['questions'][0] if ch['questions'] else None
    if sample_q:
        print(f"   Sample Q1: [{sample_q['type']}] {sample_q['question'][:60]}...")
