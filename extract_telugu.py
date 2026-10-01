import fitz
import json
import re
import os

PDF_PATH = "/Users/surajkunuku/Downloads/Paper 2A_Telugu.pdf"
CACHE_JSON = "/Users/surajkunuku/Desktop/TET quiz/telugu_ocr_pages.json"
OUT_MD = "/Users/surajkunuku/Desktop/TET quiz/telugu_questions.md"
OUT_JSON = "/Users/surajkunuku/Desktop/TET quiz/telugu_questions.json"

def extract_answers(doc):
    print("Extracting Telugu answer keys...")
    ans_map = {}
    for p in range(147, len(doc)):
        tabs = doc[p].find_tables()
        for tab in tabs:
            rows = tab.extract()
            for row in rows[1:]:
                for c in range(0, len(row), 2):
                    if c + 1 < len(row):
                        q = row[c]
                        a = row[c + 1]
                        if q and a and q.strip().isdigit() and a.strip().isdigit():
                            ans_map[int(q.strip())] = int(a.strip())
    print(f"Total Telugu answer keys: {len(ans_map)}")
    return ans_map

def clean_opt(s):
    return re.sub(r'^[“"\'_—\s]*\d+\)\s*(?:[_\.A-Za-z—\-]*\s*)?', '', s).strip()

def clean_prompt_line(s, qnum):
    return re.sub(rf'^[“"\'_—\s]*{qnum}\.\s*(?:[_\.A-Za-z—\-]*\s*)?', '', s).strip()

def parse_telugu():
    doc = fitz.open(PDF_PATH)
    ans_map = extract_answers(doc)

    if not os.path.exists(CACHE_JSON):
        print("Error: telugu_ocr_pages.json not found! Run OCR first.")
        return

    with open(CACHE_JSON, "r", encoding="utf-8") as f:
        pages = json.load(f)

    all_lines = []
    skip_headers = {
        'TET PRACTICE BITS',
        'SUBJECT — TELUGU - 30 MARKS',
        'SUBJECT - TELUGU - 30 MARKS',
        'TET PRACTICE QUESTIONS'
    }

    for p_num in range(2, 148):
        p_str = str(p_num)
        txt = pages.get(p_str, '')
        for l in txt.splitlines():
            s = l.strip()
            if s and s not in skip_headers:
                all_lines.append(s)

    questions = []
    cur_prompt = []
    cur_opts = {1: [], 2: [], 3: [], 4: []}
    cur_opt_idx = 0
    cur_q_num = 1

    for l in all_lines:
        s = l.strip()
        m_opt = re.match(r'^[“"\'_—\s]*([1-4])\)\s*(.*)', s)
        if m_opt:
            opt_num = int(m_opt.group(1))
            if opt_num == 1 and cur_opt_idx == 0:
                cur_opt_idx = 1
                cur_opts[1].append(clean_opt(s))
            elif 1 <= cur_opt_idx <= 3 and opt_num == cur_opt_idx + 1:
                cur_opt_idx = opt_num
                cur_opts[opt_num].append(clean_opt(s))
            elif cur_opt_idx == 4 and opt_num == 1:
                questions.append({
                    'num': cur_q_num,
                    'prompt': cur_prompt,
                    'options': {k: ' '.join(v).strip() for k, v in cur_opts.items()}
                })
                cur_q_num += 1
                cur_prompt = []
                cur_opts = {1: [], 2: [], 3: [], 4: []}
                cur_opt_idx = 1
                cur_opts[1].append(clean_opt(s))
            elif cur_opt_idx > 0:
                cur_opts[cur_opt_idx].append(s)
            else:
                cur_prompt.append(s)
            continue

        m_q = re.match(r'^[“"\'_—\s]*(\d+)\.\s*(.*)', s)
        if m_q and cur_opt_idx == 4:
            questions.append({
                'num': cur_q_num,
                'prompt': cur_prompt,
                'options': {k: ' '.join(v).strip() for k, v in cur_opts.items()}
            })
            cur_q_num = int(m_q.group(1))
            first_line = clean_prompt_line(s, cur_q_num)
            cur_prompt = [first_line] if first_line else []
            cur_opts = {1: [], 2: [], 3: [], 4: []}
            cur_opt_idx = 0
            continue

        if cur_opt_idx == 4:
            questions.append({
                'num': cur_q_num,
                'prompt': cur_prompt,
                'options': {k: ' '.join(v).strip() for k, v in cur_opts.items()}
            })
            cur_q_num += 1
            cur_prompt = [s]
            cur_opts = {1: [], 2: [], 3: [], 4: []}
            cur_opt_idx = 0
        elif cur_opt_idx == 0:
            cur_prompt.append(clean_prompt_line(s, cur_q_num))
        elif 1 <= cur_opt_idx <= 4:
            cur_opts[cur_opt_idx].append(s)

    if cur_opts[1]:
        questions.append({
            'num': cur_q_num,
            'prompt': cur_prompt,
            'options': {k: ' '.join(v).strip() for k, v in cur_opts.items()}
        })

    print(f"Total parsed Telugu questions: {len(questions)}")

    formatted_data = []
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("# TET Paper 2A - Telugu Practice Questions\n\n")
        f.write(f"> Total Questions: {len(questions)} | With Official Answer Keys\n\n---\n\n")

        for q in questions:
            num = q['num']
            q_text = "\n".join(q['prompt']).strip()
            ans = ans_map.get(num, "N/A")

            f.write(f"### Question {num}\n\n")
            f.write(f"{q_text}\n\n")

            opts_list = []
            for opt_idx in [1, 2, 3, 4]:
                opt_str = q['options'].get(opt_idx, "").strip()
                f.write(f"{opt_idx}) {opt_str}\n")
                opts_list.append({"key": opt_idx, "text": opt_str})

            f.write(f"\n**Answer:** {ans}\n\n---\n\n")

            formatted_data.append({
                "id": num,
                "question": q_text,
                "options": opts_list,
                "answer": ans
            })

    with open(OUT_JSON, "w", encoding="utf-8") as jf:
        json.dump(formatted_data, jf, ensure_ascii=False, indent=2)

    print(f"Successfully generated:")
    print(f" - Markdown: {OUT_MD}")
    print(f" - JSON: {OUT_JSON}")

if __name__ == "__main__":
    parse_telugu()
