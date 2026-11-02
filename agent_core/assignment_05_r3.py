with open("sample_logs_broken.csv", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        try:
            print(parts[1], parts[3])
        except IndexError:
            pass