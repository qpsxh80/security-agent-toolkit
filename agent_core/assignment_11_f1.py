import csv

fail_count = 0

with open("gichan_input.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["result"] == "FAIL":
            fail_count = fail_count + 1

print(fail_count)