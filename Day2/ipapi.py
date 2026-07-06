import requests
import time

suspicious_ips = [
    "185.220.101.5",   # Tor Exit Node (Germany)
    "8.8.8.8",         # Google DNS (USA)
    "109.248.9.15"     # Known scanning server (Russia)
]

print(f"Starting analysis on {len(suspicious_ips)} IP addresses...\n")

# 2. The Conveyor Belt (The For Loop)
# This means: "Take one IP from our list, call it 'current_ip', and run the code below."
for current_ip in suspicious_ips:
    
    print(f"--- Querying Threat Intel API for: {current_ip} ---")
    
    # 3. Dynamic URL creation using the 'current_ip'
    api_url = f"https://ipapi.co/{current_ip}/json/"
    
    # 4. Ask the internet for the data
    response = requests.get(api_url)
    
    # 5. Translate the text into a Python Map (Dictionary)
    data = response.json()
    
    # 6. Extract the specific pieces we care about
    country = data.get("country_name", "Unknown Country")
    org = data.get("org", "Unknown Owner")
    
    # 7. Print the specific results for this current IP
    print(f"[RESULTS] IP: {current_ip}")
    print(f"[RESULTS] Location: {country}")
    print(f"[RESULTS] Owner/ISP: {org}")
    print("-" * 40) # Prints a line to separate the results visually
    
    # 8. A polite pause (1 second) so we don't spam the free API server too fast
    time.sleep(1)

print("Automation task complete! All IPs processed successfully.")