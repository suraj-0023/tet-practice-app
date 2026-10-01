import json
from part1_data import DATA_1_60
from part2_data import DATA_61_120
from part3_data import DATA_121_180
from part4_data import DATA_181_240

JSON_PATH = "/Users/surajkunuku/Desktop/TET quiz/physics_questions.json"
MD_PATH = "/Users/surajkunuku/Desktop/TET quiz/physics_questions.md"

def update_all():
    # 1. Merge hints & tips
    all_tips = {}
    all_tips.update(DATA_1_60)
    all_tips.update(DATA_61_120)
    all_tips.update(DATA_121_180)
    all_tips.update(DATA_181_240)

    print(f"Total hints & memory tips loaded: {len(all_tips)}")
    assert len(all_tips) == 240, f"Expected 240 tips, got {len(all_tips)}"

    # 2. Read existing JSON
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)

    print(f"Total questions loaded from JSON: {len(questions)}")
    assert len(questions) == 240, f"Expected 240 questions, got {len(questions)}"

    # 3. Update questions in JSON
    for q in questions:
        qid = q["id"]
        tip_info = all_tips[qid]
        q["hint"] = tip_info["hint"]
        q["memory_tip"] = tip_info["memory_tip"]

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Updated {JSON_PATH} successfully.")

    # 4. Generate updated Markdown
    with open(MD_PATH, "w", encoding="utf-8") as f:
        f.write("# TET Paper 2A - Physical Science Practice Questions\n\n")
        f.write(f"> Total Questions: {len(questions)} | Bilingual (English & Telugu) with Official Answer Keys\n\n---\n\n")

        for q in questions:
            num = q["id"]
            q_text = q["question"]
            ans = q["answer"]
            hint = q["hint"]
            tip = q["memory_tip"]

            f.write(f"### Question {num}\n\n")
            f.write(f"{q_text}\n\n")

            for opt in q["options"]:
                f.write(f"({opt['key']}) {opt['text']}\n")

            f.write(f"\n**Answer:** ({ans})\n")
            f.write(f"**Hint:** {hint}\n")
            f.write(f"**Memory Tip / Formula:** {tip}\n\n")
            f.write("---\n\n")

    print(f"Updated {MD_PATH} successfully.")

if __name__ == "__main__":
    update_all()
