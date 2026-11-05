import json
with open("logs.json", encoding="utf-8") as f:
    logs = json.load(f)
print(f"로그 {len(logs)}건")