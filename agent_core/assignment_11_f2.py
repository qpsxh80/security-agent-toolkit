import json

with open("gichan_input.json", encoding="utf-8") as f:
    logs = json.load(f)

total = len(logs)
fail_count = 0
for log in logs:
    if log["result"] == "FAIL":
        fail_count = fail_count + 1

summary = f"전체 {total}건, 실패 {fail_count}건"

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary + "\n")

print(summary)