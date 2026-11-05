alerts = [
    {"rule": "brute_force", "user": "admin", "tags": ["야간", "실패"]},
    {"rule": "night_login", "user": "lee02", "tags": ["야간"]},
]

print(alerts[0]["tags"][1])