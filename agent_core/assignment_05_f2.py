values = ["2", "bad", "3"]
total = 0

for value in values:
    try:
        total += int(value)
    except ValueError:
        print("건너뜀", value)

print("합계", total)