# update_english_questions.py
import json
import os

from enhancements.topic1_5 import TIPS as t1
from enhancements.topic6_10 import TIPS as t2
from enhancements.topic11_15 import TIPS as t3
from enhancements.topic16_20 import TIPS as t4
from enhancements.topic21_25 import TIPS as t5
from enhancements.topic26_30 import TIPS as t6

JSON_PATH = "/Users/surajkunuku/Desktop/TET quiz/english_questions.json"
MD_PATH = "/Users/surajkunuku/Desktop/TET quiz/english_questions.md"

def update():
    all_tips = {}
    for d in [t1, t2, t3, t4, t5, t6]:
        all_tips.update(d)

    print(f"Loaded {len(all_tips)} tips.")

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print(f"Loaded {len(questions)} questions from JSON.")

    # Fix anomalies
    for q in questions:
        qid = q["id"]
        if qid == 311 and q["answer"] == 74:
            q["answer"] = 4
        elif qid == 67:
            q["options"] = [
                {"key": 1, "text": "twetter"},
                {"key": 2, "text": "twitar"},
                {"key": 3, "text": "twittar"},
                {"key": 4, "text": "twitter"}
            ]
            q["answer"] = 4
        elif qid == 69:
            q["options"] = [
                {"key": 1, "text": "diesaster"},
                {"key": 2, "text": "disaster"},
                {"key": 3, "text": "disastar"},
                {"key": 4, "text": "desaster"}
            ]
            q["answer"] = 2

        tip = all_tips.get(qid, {})
        q["hint"] = tip.get("hint", "")
        q["memory_tip"] = tip.get("memory_tip", "")

    # Save JSON
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Updated {JSON_PATH} successfully.")

    # Generate Markdown
    md_lines = [
        "# TET Paper 2A - English Practice Questions",
        "",
        "> Total Questions: 720 | With Official Answer Keys, Hints & Memory Tips",
        "",
        "---",
        ""
    ]

    for q in questions:
        qid = q["id"]
        md_lines.append(f"### Question {qid}")
        md_lines.append("")
        md_lines.append(q["question"].strip())
        md_lines.append("")
        for opt in q["options"]:
            md_lines.append(f"{opt['key']}. {opt['text']}")
        md_lines.append("")
        md_lines.append(f"**Answer:** {q['answer']}")
        md_lines.append("")
        md_lines.append(f"**Hint:** {q['hint']}")
        md_lines.append(f"**Memory Tip:** {q['memory_tip']}")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"Updated {MD_PATH} successfully.")

if __name__ == "__main__":
    update()
