counts = [0, 4, 2, 5]
selected = 0
total = 0

for count in counts:
    if count >= 3:
        selected += 1
        total += count

print(selected, total)