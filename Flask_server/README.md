# Flask Server - Yoga Feedback API

These scripts provide a Flask-based API for giving feedback on yoga poses using pose name. It gets the pose name to compare with the live image it captures, processes it, and returns feedback based on the pose. More specifically, it :

- Accepts a POST request with pose name.
- Captures a live image of the user for analysis.
- Uses the `get_feedback` function to analyze the pose and generate feedback.

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

#### Request Example:
```json
{
    "pose_name": "warrior"
}
```
#### Response Example:

Success:
``` bash
{
    "message": "Put your left arm down a little \pau=300\ Extend the angle of right knee  \pau=300\ "
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

The server will run on `http://127.0.0.1:5000` by default. To adjust the IP address to run on edit the `server_config.txt` file. 

## Example POST request with Python

```python 
import requests
import base64

url = "http://127.0.0.1:5000/get_yoga_feedback"

payload = {
    "pose_name": "warrior",
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print("Message:", response.json().get("message"))
else:
    print("Error:", response.json().get("error"))
```