import requests
import base64
import os

url = "http://127.0.0.1:5000/get_yoga_feedback"

current_directory = os.path.dirname(os.path.abspath(__file__))
payload = {
    "pose_name": "warrior",
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("Message:", response.json().get("message"))
else:
    print("Error:", response.json().get("error"))