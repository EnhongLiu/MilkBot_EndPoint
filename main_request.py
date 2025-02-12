import requests
import json

# Endpoint URL and Token
endpoint_url = "https://adb-65044996157806.6.azuredatabricks.net/serving-endpoints/milkbot_python/invocations"
api_token = "xxxx"

# Headers
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

parity1_para= requests.post(endpoint_url, headers=headers, data=json.dumps(parity1)).json()

parity2_para= requests.post(endpoint_url, headers=headers, data=json.dumps(parity2)).json()

parity3_para= requests.post(endpoint_url, headers=headers, data=json.dumps(parity3)).json()
