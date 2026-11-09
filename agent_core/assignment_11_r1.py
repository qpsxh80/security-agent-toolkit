import csv

count = 0
with open("logs_with_header.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        count = count + 1
print(f"총 {count}줄")