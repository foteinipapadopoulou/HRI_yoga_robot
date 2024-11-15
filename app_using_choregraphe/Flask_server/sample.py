import requests
import base64

url = "http://127.0.0.1:5000/get_yoga_feedback"

with open(r"images\cat.jpg", "rb") as image_file:
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