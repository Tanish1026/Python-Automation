import requests

# 1. Your unique password key from your free account profile
MY_API_KEY = "cfc3be7191d359107278d8789a450ef67e124c0fccc07cc75e98d078db86875dcd86a1ce3780a560"
target_ip = "185.220.101.5"

url = "https://api.abuseipdb.com/api/v2/check"

# 2. These parameters tell the API what IP you want to check
querystring = {
    'ipAddress': target_ip,
    'maxAgeInDays': '90'
}

# 3. This is where your API Key is securely passed to the server
headers = {
    'Accept': 'application/json',
    'Key': MY_API_KEY
}

# 4. Make the call with the headers and parameters attached
response = requests.get(url, headers=headers, params=querystring) #.get() used here is the requests library method not the python dictionaries
data = response.json() # data(response) converted from raw multiple line of hefty text lines to json()

# 5. Extract the explicit security score!
score = data.get('data',{}).get('abuseConfidenceScore','0') # changed the bracket notation['data']['abuseConfidenceScore'] as it might crash the script

if score > 50:
    print(f"🚨 ALERT! AbuseIPDB confidence score is {score}%! Malicious host.")