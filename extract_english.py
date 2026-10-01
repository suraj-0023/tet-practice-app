import fitz
import re
import json
import os

PDF_PATH = "/Users/surajkunuku/Downloads/TET 2A ENGLISH.pdf"
OUT_MD = "/Users/surajkunuku/Desktop/TET quiz/english_questions.md"
OUT_JSON = "/Users/surajkunuku/Desktop/TET quiz/english_questions.json"

def extract_english():
    print(f"Opening {PDF_PATH}...")
    doc = fitz.open(PDF_PATH)
    
    # 1. Extract Answer Key from pages 210-217 (indices 209-216)
    print("Extracting answer keys...")
    ans_map = {}
    for p in range(209, len(doc)):
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
    print(f"Total answer keys extracted: {len(ans_map)}")

    # 2. Extract Question Pages 2 to 209 (indices 1 to 208)
    print("Reading question pages...")
    pages_text = [doc[p].get_text() for p in range(1, 209)]
    full_text = "\n".join(pages_text)
    raw_lines = [l.strip() for l in full_text.splitlines() if l.strip()]

    clean_lines = []
    skip_headers = {
        'TET PRACTICE QUESTIONS',
        'ENGLISH IIA (30M)',
        'TET – PRACTICE QUESTIONS',
        'ENGLISH – II A'
    }
    for l in raw_lines:
        if l in skip_headers:
            continue
        clean_lines.append(l)

    # 3. Parse questions and options
    questions = []
    cur_q = {'num': 1, 'text': [], 'options': {}}
    cur_opt = 0

    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        q_target = cur_q['num']

        if cur_opt == 0:
            m = re.match(rf'^{q_target}(?:[\.\s\)]+|$)(.*)', line)
            if m:
                content = m.group(1).strip()
                if content:
                    cur_q['text'].append(content)
                cur_opt = 1
                i += 1
                continue

        if 1 <= cur_opt <= 4:
            m_opt = re.match(rf'^(?:(?:\({cur_opt}\))|{cur_opt}[\.\)]|\b{cur_opt}\b\s*)(.*)', line)
            if m_opt:
                opt_content = m_opt.group(1).strip()
                if not opt_content and i + 1 < len(clean_lines):
                    next_l = clean_lines[i + 1]
                    if not re.match(r'^(?:(?:\([1-4]\))|[1-4][\.\)]|\b\d+[\.\)])', next_l):
                        opt_content = next_l
                        i += 1
                cur_q['options'][cur_opt] = opt_content
                cur_opt += 1
                i += 1
                continue

        next_q = q_target + 1
        m_next = re.match(rf'^{next_q}(?:[\.\s\)]+|$)(.*)', line)
        if m_next and cur_opt > 1:
            questions.append(cur_q)
            cur_q = {'num': next_q, 'text': [], 'options': {}}
            content = m_next.group(1).strip()
            if content:
                cur_q['text'].append(content)
            cur_opt = 1
            i += 1
            continue

        if cur_opt == 1:
            cur_q['text'].append(line)
        elif cur_opt > 1:
            prev_opt = min(cur_opt - 1, 4)
            if prev_opt in cur_q['options']:
                cur_q['options'][prev_opt] += ' ' + line
            else:
                cur_q['options'][prev_opt] = line
        i += 1

    if cur_q['text']:
        questions.append(cur_q)

    print(f"Parsed {len(questions)} questions!")

    # 4. Write Markdown & JSON
    formatted_data = []
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("# TET Paper 2A - English Practice Questions\n\n")
        f.write(f"> Total Questions: {len(questions)} | With Official Answer Keys\n\n---\n\n")
        
        for q in questions:
            num = q['num']
            q_text = "\n".join(q['text'])
            ans = ans_map.get(num, "N/A")
            
            f.write(f"### Question {num}\n\n")
            f.write(f"{q_text}\n\n")
            
            opts_list = []
            for opt_idx in [1, 2, 3, 4]:
                opt_str = q['options'].get(opt_idx, "")
                f.write(f"{opt_idx}. {opt_str}\n")
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
    extract_english()
