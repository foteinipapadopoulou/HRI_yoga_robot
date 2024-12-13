import requests
import base64
import os

url = "http://192.168.0.101:5000/get_yoga_feedback"

current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'images/cat.jpg')
with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode('utf-8')

payload = {
    "pose_name": "warrior",
    "image_data": image_data
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("Message:", response.json().get("message"))
else:
    print("Error:", response.json().get("error"))