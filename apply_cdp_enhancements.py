import json
import re
import os

JSON_PATH = "cdp_questions.json"
MD_PATH = "cdp_questions.md"

def load_batches():
    all_tips = {}
    for i in range(1, 7):
        bfile = f"cdp_enhancer/batch_{i}.json"
        with open(bfile, "r", encoding="utf-8") as f:
            data = json.load(f)
            for k, v in data.items():
                all_tips[int(k)] = v
    print(f"Loaded {len(all_tips)} tips from batches.")
    return all_tips

def fix_options_and_q(q):
    opts = q['options']
    # If options already have text, keep question and options
    if any(o['text'].strip() for o in opts):
        return q['question'], opts

    qid = q['id']
    qtext = q['question']

    if qid == 179:
        fixed_opts = [
            {'key': 1, 'text': '(CA / MA) × 100'},
            {'key': 2, 'text': '(MA / CA) × 100'},
            {'key': 3, 'text': '(MA × CA) / 100'},
            {'key': 4, 'text': '(MA / CA) + 100'}
        ]
        return 'IQ =', fixed_opts

    # Extract 1) ... 2) ...
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

def update_all():
    print(f"Reading {JSON_PATH}...")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        cdp_data = json.load(f)

    tips = load_batches()

    enhanced_json_data = []

    for q in cdp_data:
        qid = q['id']
        cleaned_q, fixed_opts = fix_options_and_q(q)
        tip_info = tips.get(qid, {})

        hint = tip_info.get("hint", "")
        memory_tip = tip_info.get("memory_tip", "")

        if not hint or not memory_tip:
            print(f"WARNING: Missing hint or memory tip for Q{qid}!")

        new_obj = {
            "id": qid,
            "question": cleaned_q,
            "options": fixed_opts,
            "answer": q['answer'],
            "hint": hint,
            "memory_tip": memory_tip
        }
        enhanced_json_data.append(new_obj)

    print(f"Writing updated JSON ({len(enhanced_json_data)} questions) to {JSON_PATH}...")
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(enhanced_json_data, f, ensure_ascii=False, indent=2)

    print(f"Writing updated Markdown to {MD_PATH}...")
    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write("# TET Paper 2A - Child Development & Pedagogy (CDP) Practice Questions\n\n")
        f.write(f"> Total Questions: {len(enhanced_json_data)} | Bilingual (English & Telugu) with Official Answer Keys\n\n---\n\n")

        for q in enhanced_json_data:
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

    print("Update completed successfully!")

if __name__ == "__main__":
    update_all()
