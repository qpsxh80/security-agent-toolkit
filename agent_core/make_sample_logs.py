lines = [
    "09:01,kim01,10.0.3.21,LOGIN,FAIL",
    "09:03,lee02,10.0.7.5,LOGIN,OK",
    "09:05,kim01,10.0.3.21,LOGIN,FAIL",
    "09:08,park03,10.0.9.8,FILE_OPEN,OK",
    "09:11,kim01,10.0.3.21,LOGIN,FAIL",
    "09:14,park03,10.0.9.8,LOGIN,FAIL",
]

with open("sample_logs.csv", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(f"{line}\n")

print("agent_core에 sample_logs.csv를 만들었습니다")