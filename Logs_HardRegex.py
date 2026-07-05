import re

Existing_ips = []
ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

with open("Server_L2.txt", "r") as file:
    for line in file:
        sim = re.search(ip_pattern, line)
        
        if sim:
            pure_ip = sim.group()
            
            # THE FIX: Indented this block so it only runs if 'sim' is True
            if pure_ip not in Existing_ips: 
                Existing_ips.append(pure_ip)

print("---Regex Search Hunting---")
print(f"Extracted IP Addresses: {len(Existing_ips)}")
print(f"List of Extracted IP Addresses: {Existing_ips}")