import json
text = '{"user": "admin", "fail": 3}'
data = json.loads(text)
print(data["fail"])