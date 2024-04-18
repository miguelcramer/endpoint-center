import requests
import json

url = "http://186.179.163.205:8008"

auth_token = "MRC"

# Example messages
messages = [
    {"role": "user", "content": "What is the capital of Texas?"}
]

headers = {"Content-Type": "application/json"}


def send_request():
    response = requests.post(
        url, 
        data=json.dumps({"messages": messages, "verify_token":auth_token}), 
        headers={"Content-Type": "application/json"}
    )
    print("Response:", response.json()["response"])

send_request()
