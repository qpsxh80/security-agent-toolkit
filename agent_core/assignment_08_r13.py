import json
summary = {"date": "9/28", "note": "야간 실패 많음", "fail": 4}
with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)