logs = [
    {"user": "kim01", "result": "FAIL"},
    {"user": "lee02", "result": "OK"},
    {"user": "park03", "result": "FAIL"},
]

def collect_failed_users(logs):
    failed_users = []
    for log in logs:
        if log["result"] == "FAIL":
            failed_users.append(log["user"])
    return failed_users

print(collect_failed_users(logs))