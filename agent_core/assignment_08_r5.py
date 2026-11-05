report = {
    "admin": {"fail": 3, "ip": "10.0.9.8"},
    "lee02": {"fail": 1, "ip": "10.0.7.5"},
}

for user in report:
    print(user, report[user]["fail"])