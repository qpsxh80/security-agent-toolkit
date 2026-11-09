import csv
from collections import Counter

THRESHOLD = 2

failed_users = []
with open("logs_with_header.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["result"] == "FAIL":
            failed_users.append(row["user"])

counts = Counter(failed_users)
for user, count in counts.items():
    if count >= THRESHOLD:
        print(f"확인 필요: {user} · {count}회")