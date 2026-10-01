import json
import re

SPECIFIC_FIXES = {
    179: [
        {'key': 1, 'text': '(CA / MA) × 100'},
        {'key': 2, 'text': '(MA / CA) × 100'},
        {'key': 3, 'text': '(MA × CA) / 100'},
        {'key': 4, 'text': '(MA / CA) + 100'}
    ],
    205: [
        {'key': 1, 'text': 'Spatial Intelligence ప్రాద్వశిక్ ప్రజా'},
        {'key': 2, 'text': 'Bodily – Kinaesthetic Intelligence శారీయక్ క్ండయ సూరాశతమక్ ప్రజా'},
        {'key': 3, 'text': 'Mathematical – Logical Intelligence గణిత – తరిిక్ ప్రజా'},
        {'key': 4, 'text': 'Musical Intelligence సంగీత ప్రజా'}
    ],
    244: [
        {'key': 1, 'text': 'Scholastic Aptitude Test విద్యయ విషమక్ సహజ సాభయాా ఩రీక్ష'},
        {'key': 2, 'text': 'Vocational Aptitude Test వృతిి సంఫంధ సహజ సాభయాా ఩రీక్ష'},
        {'key': 3, 'text': 'Aesthetic Aptitude Test సందయయ క్ళ్ల సంఫంధిత సహజ సాభయాా ఩రీక్ష'},
        {'key': 4, 'text': 'Sports Aptitude Test క్రీడా సంఫంధిత సహజ సాభయాా ఩రీక్ష'}
    ],
    302: [
        {'key': 1, 'text': 'Sanguine – ఔతసహకులు'},
        {'key': 2, 'text': 'Pyknic – పీయసకామలు'},
        {'key': 3, 'text': 'Athletic – క్రీడాకామలు'},
        {'key': 4, 'text': 'Leptosomatic – ప్రాంశుకామలు'}
    ],
    405: [
        {'key': 1, 'text': 'Discontinuous Reinforcement Schedule వియళ పునయభలన నిమభం'},
        {'key': 2, 'text': 'Fixed Interval Reinforcement Schedule స్కాయకాల వయవధి పునయభలన నిమభం'},
        {'key': 3, 'text': 'Fixed Ratio Reinforcement Schedule స్కాయ నిషూతిి పునయభలన నిమభం'},
        {'key': 4, 'text': 'Variable Reinforcement Schedule చయశీల పునయభలన నిమభం'}
    ],
    466: [
        {'key': 1, 'text': 'Identifying the problem సభసయను గురిించడం'},
        {'key': 2, 'text': 'Preparation of the report నివేదిక్ను తయారుచేమడం'},
        {'key': 3, 'text': 'Preparation of Research plan ఩రిశోధనా ప్రణాళిక్ను తయారుచేమడం'},
        {'key': 4, 'text': 'Implementation of Research plan ఩రిశోధనా ప్రణాళిక్ను ఄభలు఩యచడం'}
    ],
    478: [
        {'key': 1, 'text': 'Build a confidence in students విద్యయరుీలలో నభమకానిు క్లిగించడం'},
        {'key': 2, 'text': 'Manage time effectively కాలనిు సరిగా నియేహంచగలగడం'},
        {'key': 3, 'text': 'Encourage conflicts సంఘయిణలను ప్రోతసహంచడం'},
        {'key': 4, 'text': 'Motivate students విద్యయరుీలకు ప్రేయణ క్లిగించడం'}
    ],
    538: [
        {'key': 1, 'text': 'Rote learning ఫటీట ఄబయసనం'},
        {'key': 2, 'text': 'Remembering Information సమాచారానిు గురుించ్చకోవడం'},
        {'key': 3, 'text': 'Analytical Thinking విశ్లీషణాతమక్ అలోచన'},
        {'key': 4, 'text': 'Securing good marks భంచి మారుిలు సాధించడం'}
    ],
    539: [
        {'key': 1, 'text': 'Holistic development of the students విద్యయరుీల యొక్ి సంపూరాణభివృదిీనిగూరిి'},
        {'key': 2, 'text': 'Only the marks of the students విద్యయరుీల మారుిలు మాత్రమే'},
        {'key': 3, 'text': 'Information about the lessons పాఠాయంశాలకు సంఫంధించిన సమాచాయం'},
        {'key': 4, 'text': 'Information about the teachers ఈపాధ్యయమఫృంద్యనిక సంఫంధించిన సమాచాయం'}
    ]
}

def load_tips():
    all_tips = {}
    for i in range(1, 7):
        with open(f"cdp_enhancer/batch_{i}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for k, v in data.items():
                all_tips[int(k)] = v
    return all_tips

def clean_question_and_options(q):
    qid = q['id']
    qtext = q['question']
    opts = q['options']

    if qid in SPECIFIC_FIXES:
        return qtext.strip(), SPECIFIC_FIXES[qid]

    if not any(o['text'].strip() for o in opts):
        lines = qtext.splitlines()
        q_lines = []
        opt_lines = {1: [], 2: [], 3: [], 4: []}
        cur_opt = 0

        for l in lines:
            m = re.match(r'^\s*([1-4])[\)\.]\s*(.*)', l)
            if m:
                cur_opt = int(m.group(1))
                rest = m.group(2).strip()
                if rest:
                    opt_lines[cur_opt].append(rest)
            elif cur_opt == 0:
                q_lines.append(l)
            else:
                opt_lines[cur_opt].append(l.strip())

        cleaned_q = '\n'.join(q_lines).strip()
        fixed_opts = [
            {'key': k, 'text': ' '.join(opt_lines[k]).strip()}
            for k in [1, 2, 3, 4]
        ]
        return cleaned_q, fixed_opts

    return qtext.strip(), opts

def run():
    with open("cdp_questions.json", "r", encoding="utf-8") as f:
        cdp_data = json.load(f)

    tips = load_tips()
    final_data = []

    for q in cdp_data:
        qid = q['id']
        cq, fopts = clean_question_and_options(q)
        tip_info = tips[qid]

        final_data.append({
            "id": qid,
            "question": cq,
            "options": fopts,
            "answer": q['answer'],
            "hint": tip_info["hint"],
            "memory_tip": tip_info["memory_tip"]
        })

    # Validate
    for item in final_data:
        assert item["hint"].strip(), f"Empty hint in Q{item['id']}"
        assert item["memory_tip"].strip(), f"Empty tip in Q{item['id']}"
        for opt in item["options"]:
            assert opt["text"].strip(), f"Empty option {opt['key']} in Q{item['id']}"

    print(f"Validation successful! All {len(final_data)} questions have complete questions, options, answers, hints, and memory tips.")

    # Write JSON
    with open("cdp_questions.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    # Write Markdown
    with open("cdp_questions.md", "w", encoding="utf-8") as f:
        f.write("# TET Paper 2A - Child Development & Pedagogy (CDP) Practice Questions\n\n")
        f.write(f"> Total Questions: {len(final_data)} | Bilingual (English & Telugu) with Official Answer Keys\n\n---\n\n")

        for q in final_data:
            num = q['id']
            q_text = q['question']
            ans = q['answer']
            hint = q['hint']
            memory_tip = q['memory_tip']

            f.write(f"### Question {num}\n\n")
            f.write(f"{q_text}\n\n")

            for opt in q['options']:
                opt_key = opt['key']
                opt_text = opt['text']
                f.write(f"({opt_key}) {opt_text}\n")

            f.write(f"\n**Answer:** ({ans})\n\n")
            f.write(f"**Hint:** {hint}\n\n")
            f.write(f"**Memory Tip:** {memory_tip}\n\n---\n\n")

    print("Successfully wrote cdp_questions.json and cdp_questions.md!")

if __name__ == "__main__":
    run()
