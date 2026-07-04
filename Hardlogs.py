print("--- Reading Live Log File ---")
connection_counts = {}

with open("Server_L.txt", "r") as file:
    
    for data in file:
        if "Connected to External IP" in data:
            computer_name = data.split(' - ')[0].strip()

            if computer_name in connection_counts:
                connection_counts[computer_name] += 1
            else:
                connection_counts[computer_name] = 1     

print("\n--- Final connection counts ---")
print(connection_counts)

print("\n--- Threat detection alerts ---")
for computer_name, count in connection_counts.items():
    if count >= 3:
        print(f"ALERT: {computer_name} has connected to external IPs {count} times.")