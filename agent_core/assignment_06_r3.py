count = 0
with open("sample_logs.csv", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
        count += 1
print(f"총 {count}줄")