import csv

failed_users = []
with open("logs_with_header.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["result"] == "FAIL":
            failed_users.append(row["user"])
print(failed_users)