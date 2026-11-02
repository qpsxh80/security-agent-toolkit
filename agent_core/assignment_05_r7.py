line = "03:22,hacker,LOGIN_FAIL,10.0.9.9"

parts = line.split(",")
time = parts[0]
hour = int(time.split(":")[0])

if hour >= 0 and hour <= 6:
    print("야간")