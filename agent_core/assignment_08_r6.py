report = {
    "admin": {"fail": 3, "ip": "10.0.9.8"},
    "lee02": {"fail": 1, "ip": "10.0.7.5"},
}

for user in report:
    if report[user]["fail"] >= 2:
        print(f"확인 필요: {user}")