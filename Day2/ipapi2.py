import requests
import time

sus_ip = [
    "8.8.8.8",         # Google DNS (Expected / Safe)
    "185.220.101.5",   # Tor Exit Node (Suspicious)
]

for current_ip in sus_ip:
    api_url = f"https://ipapi.co/{current_ip}/json/"
    
    # Adding a custom header makes our script look more like a browser,
    # which helps prevent the free API from immediately blocking us.
    headers = {"User-Agent": "SOC-Test-Script"}
    response = requests.get(api_url, headers=headers)
    
    data = response.json()

    org = data.get("org", "Unknown")
    country = data.get("country_name", "Unknown")

    # FIXED LOGIC: Explicitly checking the string values
    if "Tor" in org or country == "Russia":
        print(f"🚨 ALERT! Critical threat detected from IP: {current_ip}")
        print(f"   [Details] Location: {country} | Provider: {org}")
        print(f"   [Action] Routing to Incident Response Team immediately.")
    else:
        print(f"✅ IP {current_ip} processed: Safe traffic verified ({org}).")
        
    print("-" * 50)
    
    # Increased wait time to 2 seconds to be extra polite to the free API
    time.sleep(2)