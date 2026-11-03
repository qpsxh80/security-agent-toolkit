import os
import sys

print("Python 파일이 실행되는 폴더:", os.getcwd())
print("지금 쓰는 파이썬     :", sys.executable)

if os.path.basename(os.getcwd()) == "agent_core":
    print("준비 완료")
else:
    print("이 Python 파일을 security-agent-toolkit 폴더 안의 agent_core 폴더로 옮긴 뒤 다시 엽니다")