import json

logs = [
    {"time": "09:01", "user": "kim01", "event": "LOGIN_OK", "ip": "10.0.3.21"},
    {"time": "09:05", "user": "admin", "event": "LOGIN_FAIL", "ip": "10.0.9.8"},
    {"time": "09:12", "user": "admin", "event": "LOGIN_FAIL", "ip": "10.0.9.8"},
    {"time": "09:18", "user": "lee02", "event": "LOGIN_FAIL", "ip": "10.0.7.5"},
    {"time": "09:21", "user": "admin", "event": "LOGIN_FAIL", "ip": "10.0.9.8"},
]

with open("logs.json", "w", encoding="utf-8") as f:
    json.dump(logs, f, ensure_ascii=False, indent=2)

with open("logs.json", encoding="utf-8") as f:
    logs = json.load(f)

fail = 0
for log in logs:
    if log.get("event") == "LOGIN_FAIL":
        fail += 1
print(f"실패 {fail}건")