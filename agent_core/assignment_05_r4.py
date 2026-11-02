broken = 0

with open("sample_logs_broken.csv", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        try:
            parts[3]
        except IndexError:
            broken += 1

print(f"깨진 줄 {broken}건")