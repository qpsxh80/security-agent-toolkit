import json
report = {"admin": 3}
with open("report.json", "w", encoding="utf-8") as f:
    json.dump(report, f)
with open("report.json", encoding="utf-8") as f:
    back = json.load(f)
print(back["admin"])