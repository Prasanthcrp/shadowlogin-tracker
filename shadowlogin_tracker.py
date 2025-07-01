import datetime

# Sample login logs (username, IP address, login time)
login_logs = [
    {"user": "Cristiano", "ip": "128.101.101.101", "time": "2025-07-01 10:00:00"},
    {"user": "Cristiano", "ip": "203.0.113.5", "time": "2025-07-01 10:15:00"},
    {"user": "Ronaldo", "ip": "203.0.113.5", "time": "2025-07-01 10:30:00"},
    {"user": "Ront", "ip": "128.101.101.101", "time": "2025-07-01 10:40:00"},
]

# Mock IP-to-country mapping
def mock_geo_location(ip):
    ip_map = {
        "128.101.101.101": "USA",
        "203.0.113.5": "India",
    }
    return ip_map.get(ip, "Unknown")

# Detect suspicious logins
def detect_suspicious_logins(logs):
    user_activity = {}
    suspicious = []

    for log in logs:
        user = log["user"]
        ip = log["ip"]
        time = datetime.datetime.strptime(log["time"], "%Y-%m-%d %H:%M:%S")
        location = mock_geo_location(ip)

        if user not in user_activity:
            user_activity[user] = []

        for entry in user_activity[user]:
            time_diff = abs((time - entry["time"]).total_seconds() / 60)
            if entry["location"] != location and time_diff < 30:
                suspicious.append({
                    "user": user,
                    "from": entry["location"],
                    "to": location,
                    "time_diff_minutes": round(time_diff, 2),
                    "timestamp1": entry["time"],
                    "timestamp2": time
                })

        user_activity[user].append({"ip": ip, "location": location, "time": time})

    return suspicious

# Run the detection
result = detect_suspicious_logins(login_logs)

# Print suspicious activity
if result:
    print("\u26a0\ufe0f  Suspicious logins detected:")
    for entry in result:
        print(f"- User: {entry['user']} | Location changed from {entry['from']} to {entry['to']} "
              f"in {entry['time_diff_minutes']} mins "
              f"({entry['timestamp1']} → {entry['timestamp2']})")
else:
    print("\u2705 No suspicious activity detected.")
