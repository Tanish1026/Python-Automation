import os
import re
import requests
import time

# --- CONFIGURATION LAYER ---
YOUR_API_KEY = os.environ.get("MY_API")

if not YOUR_API_KEY:
 print("Some problem in locating the api key")
 exit()
LOG_FILE_PATH = "Server1.txt"
API_ENDPOINT = "https://api.abuseipdb.com/api/v2/check"

# --- PHASE 1: THE LOCAL LOG PARSER (REGEX) ---
print("Scanning local log files for network indicators...")

# The classic regex pattern to accurately match IPv4 addresses
ip_regex = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
extracted_ips = []

try:
    with open(LOG_FILE_PATH, "r") as file:
        for line in file:
            # Find all strings matching the IP pattern in the current line
            matches = re.findall(ip_regex, line)
            if matches:
                # Add the found IPs to our collection list
                extracted_ips.extend(matches)
except FileNotFoundError:
    print(f"❌ Error: Could not find the file '{LOG_FILE_PATH}'. Please create it first.")
    exit()

# --- PHASE 2: DEDUPLICATION ---
# Converting the list into a Python 'set' automatically deletes duplicate entries,
# protecting your API daily budget from being wasted!
unique_ips = list(set(extracted_ips))
print(f"Found {len(extracted_ips)} total IPs in log. (Isolated {len(unique_ips)} unique IPs for analysis).\n")


# --- PHASE 3: LIVE THREAT INTELLIGENCE ENGINE ---
print("--- Launching Live Threat Contextualization Loop ---")

for current_ip in unique_ips:
    print(f"Investigating IP: {current_ip}...")
    
    # Setup parameters required by the AbuseIPDB /check manual
    querystring = {
        'ipAddress': current_ip,
        'maxAgeInDays': '90'
    }
    
    headers = {
        'Accept': 'application/json',
        'Key': YOUR_API_KEY
    }
    
    try:
        # Fire request over the internet
        response = requests.get(API_ENDPOINT, headers=headers, params=querystring)
        
        # Stop execution and print an error if the route is wrong or API key is bad (e.g., 404 or 401)
        response.raise_for_status()
        
        data = response.json()
        
        # 1. STRUCTURAL INTEGRITY AUDIT
        # We explicitly verify the blueprint hasn't changed before parsing data
        if 'data' not in data:
            print(f"⚠️ STRUCTURAL ANOMALY DETECTED FOR IP {current_ip}!")
            print(f"   Reason: The root 'data' key has changed or is missing.")
            print(f"   Raw Payload for Debugging: {data}")
            
            # FAIL-SECURE PROTOCOL: We do NOT assume the IP is safe. 
            # We flag it as an unverified hazard (-1) so it gets isolated for manual review.
            score = -1
            country = "UNVERIFIED"
            isp = "UNVERIFIED"
        else:
            # 2. SAFE EXTRACTION (The blueprint is confirmed valid)
            score = data['data'].get('abuseConfidenceScore', 0)
            country = data['data'].get('countryName', 'Unknown Country')
            isp = data['data'].get('isp', 'Unknown ISP')
        
        # 3. ADVANCED DECISION MATRIX
        if score >= 50:
            print(f"🚨 ALERT! Malicious activity confirmed for IP: {current_ip}")
            print(f"   [Threat Level] {score}% Confidence Score | Country: {country} | ISP: {isp}")
            print(f"   [Action Taken] IP added to firewall blocking list.")
            
        elif score == -1:
            print(f"🛑 CRITICAL: Bypassing automatic triage for {current_ip}.")
            print(f"   [Action Required] API blueprint misalignment. Inspect script immediately.")
            
        else:
            print(f"✅ IP {current_ip} verified clean (Score: {score}%). Skipping block action.")
            
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ Failed to look up {current_ip} due to API Error: {http_err}")
    except Exception as e:
        print(f"❌ An unexpected processing error occurred: {e}")
        
    print("-" * 60)
    # Pause for 1.5 seconds to respect free-tier rate limits
    time.sleep(1.5)

print("\nAll pipeline tasks successfully complete.")