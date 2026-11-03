with open("check.txt", "a", encoding="utf-8") as f:
    f.write("추가 점검\n")

with open("check.txt", encoding="utf-8") as f:
    print(f.read())