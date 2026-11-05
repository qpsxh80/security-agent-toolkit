count = 0

with open("sample_logs.csv", encoding="utf-8") as f:
    for line in f:
        if "FAIL" in line:
            print(line.strip())
            count = count + 1

print(f"실패 {count}줄")