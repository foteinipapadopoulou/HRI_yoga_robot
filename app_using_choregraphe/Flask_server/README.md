# Flask Server - Yoga Feedback API

These scripts provide a Flask-based API for giving feedback on yoga poses using image and pose name. It decodes an image in Base64 format, processes it, and returns feedback based on the pose. More specifically, it :

- Accepts a POST request with pose name and Base64-encoded image.
- Saves the image temporarily for analysis.
- Uses the `get_feedback` function to analyze the pose and generate feedback.
- Deletes the temporary image.

## Installation
1. Clone this repository.
2. Create a virtual environment.

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

   - On **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## API Endpoint

### `POST /get_yoga_feedback`
This endpoint accepts JSON data with the following fields:
- `pose_name`: Name of the yoga pose. The supported poses can be found on the `constants.py` file.
- `image_data`: Base64-encoded string of the yoga pose image.

#### Request Example:
```json
{
    "pose_name": "warrior",
    "image_data": "<base64-encoded-image>"
}
```
#### Response Example:

Success:
``` bash
{
    "message": "Put your arm down a little. Put your arm down a little. Extend the angle at right hip. Extend the angle at left hip. Extend the angle of right knee."
}
```

Error:
```bash
{
    "error": ""
}
```

## Running the Application

Start the Flask server by running:

``` bash
python3 main.py
```

The server will run on `http://127.0.0.1:5000` by default.

## Example POST request with Python

```python 
import requests
import base64

url = "http://127.0.0.1:5000/get_yoga_feedback"

with open("<yourimagepath>", "rb") as image_file:
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
```