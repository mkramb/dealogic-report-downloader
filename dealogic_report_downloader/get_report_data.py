import os
import requests

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
REPORT_ID = os.environ["REPORT_ID"]

# More information about the API is available here:
# https://api.reporting.cortex.dealogic.com/index.html

url  = f'https://api.reporting.cortex.dealogic.com/api/v1.1/data/{REPORT_ID}/EndOfDay'
headers = {
    'oauthtoken': ACCESS_TOKEN,
    'origin': 'https://cortex.dealogic.com',
    'referer': 'https://cortex.dealogic.com'
}

response = requests.get(url, headers=headers)

# Important attributes are: 
# Schema & ResultSet
print(response.text)
