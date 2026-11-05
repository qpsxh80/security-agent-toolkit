from collections import Counter

failed_users = ["kim01", "kim01", "kim01", "park03"]

def report_suspects(failed_users, threshold=2):
    counts = Counter(failed_users)
    for user, count in counts.items():
        if count >= threshold:
            print(f"확인 필요: {user} · {count}회")

report_suspects(failed_users)