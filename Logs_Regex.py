import re

log_line ="2026-07-04 Critical Alert: Unauthorized access attempt from source IP 185.220.101.5 on port 443"
 
ip_pattern= r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

sim = re.search(ip_pattern, log_line)

print("---Regex Search Hunting---")

if sim:
    captured_ip = sim.group()
    print(f"Captured IP Address: {captured_ip}")

else:
    print("No IP address found in the log line.")
