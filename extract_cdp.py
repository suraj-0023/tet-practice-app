import fitz
import re
import json

PDF_PATH = "/Users/surajkunuku/Downloads/TET 2A CDP.pdf"
OUT_MD = "/Users/surajkunuku/Desktop/TET quiz/cdp_questions.md"
OUT_JSON = "/Users/surajkunuku/Desktop/TET quiz/cdp_questions.json"

def normalize_pua(text):
    res = []
    for c in text:
        code = ord(c)
        if 0xF000 <= code <= 0xF0FF:
            res.append(chr(code - 0xF000))
        else:
            res.append(c)
    return "".join(res)

def extract_cdp():
    print(f"Opening {PDF_PATH}...")
    doc = fitz.open(PDF_PATH)

    # 1. Extract Answer Keys from pages 223-229 (indices 222-228)
    print("Extracting answer keys...")
    ans_map = {}
    for p in range(222, len(doc)):
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

    # 2. Extract Question Pages 2 to 222 (indices 1 to 221)
    print("Reading question pages...")
    pages_text = [doc[p].get_text() for p in range(1, 222)]
    full_text = "\n".join(pages_text)
    full_text = normalize_pua(full_text)
    raw_lines = [l.strip() for l in full_text.splitlines() if l.strip()]

    clean_lines = []
    skip_headers = {
        'TET – PRACTICE QUESTIONS',
        'CDP – II A',
        'TET PRACTICE QUESTIONS',
        'CDP – IIA',
        'TET - PRACTICE QUESTIONS'
    }
    for l in raw_lines:
        if l in skip_headers:
            continue
        clean_lines.append(l)

    # 3. Locate question starts (1 to 630)
    expected_q = 1
    q_indices = []
    for i, l in enumerate(clean_lines):
        if l.startswith('('):
            continue
        m = re.match(r'^(\d+)[\.\s]+(.*)', l)
        if m:
            num = int(m.group(1))
            if expected_q == 319 and num == 318:
                num = 319
            if num == expected_q:
                q_indices.append((expected_q, i))
                expected_q += 1

    print(f"Matched {len(q_indices)} questions...")

    all_parsed = []
    for idx, (qnum, start_i) in enumerate(q_indices):
        end_i = q_indices[idx + 1][1] if idx + 1 < len(q_indices) else len(clean_lines)
        block = clean_lines[start_i:end_i]

        first = re.sub(r'^\d+[\.\s]+', '', block[0]).strip()
        block_lines = ([first] if first else []) + block[1:]

        q_text_lines = []
        options = {1: [], 2: [], 3: [], 4: []}
        cur_opt = 0
        for l in block_lines:
            m_opt = re.match(r'^\((\d)\)\s*(.*)', l)
            if m_opt:
                cur_opt = int(m_opt.group(1))
                opt_rest = m_opt.group(2).strip()
                if opt_rest:
                    options[cur_opt].append(opt_rest)
            elif cur_opt == 0:
                q_text_lines.append(l)
            elif 1 <= cur_opt <= 4:
                options[cur_opt].append(l)

        opts_dict = {k: " ".join(v).strip() for k, v in options.items()}
        all_parsed.append({
            'num': qnum,
            'question': "\n".join(q_text_lines).strip(),
            'options': opts_dict,
            'answer': ans_map.get(qnum, "N/A")
        })

    # 4. Write Markdown & JSON
    formatted_data = []
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("# TET Paper 2A - Child Development & Pedagogy (CDP) Practice Questions\n\n")
        f.write(f"> Total Questions: {len(all_parsed)} | Bilingual (English & Telugu) with Official Answer Keys\n\n---\n\n")

        for q in all_parsed:
            num = q['num']
            q_text = q['question']
            ans = q['answer']

            f.write(f"### Question {num}\n\n")
            f.write(f"{q_text}\n\n")

            opts_list = []
            for opt_idx in [1, 2, 3, 4]:
                opt_str = q['options'].get(opt_idx, "")
                f.write(f"({opt_idx}) {opt_str}\n")
                opts_list.append({"key": opt_idx, "text": opt_str})

            f.write(f"\n**Answer:** ({ans})\n\n---\n\n")

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
    extract_cdp()
