def collect_over_3(values):
    result = []
    for v in values:
        if v >= 3:
            result.append(v)
    return result



print(collect_over_3([0, 4, 2, 5]))
print(collect_over_3([]))