def summarize(value):
    sum = 0
    for v in value:
        sum += v
    return f"합계 {sum}"

result = summarize([2, 3])

with open("report.txt", "w", encoding="utf-8") as f:
    f.write(result + "\n")

print(result)