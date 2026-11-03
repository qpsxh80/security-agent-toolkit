with open("check.txt", "w", encoding="utf-8") as f:
    f.write("점검 시작\n")
    f.write("점검 끝\n")

with open("check.txt", encoding="utf-8") as f:
    print(f.read())