def judge(fail_count):
    if fail_count >= 3:
        return "추가 확인"
    else:
        return "기록 유지"

print(judge(2))
print(judge(3))