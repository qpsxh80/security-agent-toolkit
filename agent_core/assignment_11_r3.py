THRESHOLD = 2
failed_users = ["kim01", "kim01", "lee02"]

def count_fail(users, name):
    count = 0
    for user in users:
        if user == name:
            count = count + 1
    return count

if count_fail(failed_users, "kim01") >= THRESHOLD:
    print("확인 필요: kim01")