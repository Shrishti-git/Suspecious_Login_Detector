import pandas as pd

# Read login data
data = pd.read_csv("../logs/sample_logins.csv")

print("=== LOGIN DATA ===")
print(data)

print("\n=== SUSPICIOUS ACTIVITY DETECTED ===")

# Find failed logins
failed_logins = data[data["status"] == "FAILED"]

# Count failed attempts by IP
ip_counts = failed_logins["ip_address"].value_counts()

# Alert if failed attempts are 3 or more
for ip, count in ip_counts.items():
    if count >= 3:
        print(f"ALERT: Suspicious IP detected -> {ip}")
        print(f"Failed Attempts: {count}\n")