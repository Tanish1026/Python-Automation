


log_data = [
    "PC-HR - Connected to External IP",
    "PC-Marketing - Downloaded File",
    "PC-HR - Connected to External IP",
    "PC-IT - Login Failed",
    "PC-HR - Connected to External IP",
    "PC-Finance - Accessed Confidential Data",
    "PC-Marketing - Connected to External IP",
    "PC-HR - Connected to External IP",
]
print("---Scanning logs ---")
connection_counts = {}

for line in log_data:
    if "Connected to External IP" in line:
        computer_name = line.split(' - ')[0]

        if computer_name in connection_counts:
            connection_counts[computer_name] += 1
        else:
            connection_counts[computer_name] = 1    

print("---Final connection counts---")
print(connection_counts)

print("---Threat detection alerts---")
for computer_name, count in connection_counts.items():
    if count >= 3:
        print(f"ALERT: {computer_name} has connected to external IPs {count} times.")
