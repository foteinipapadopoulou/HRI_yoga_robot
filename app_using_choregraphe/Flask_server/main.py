from flask import Flask, request, jsonify
import base64
import os

from yoga_feedback import get_feedback 

app = Flask(__name__)

@app.route('/get_yoga_feedback', methods=['POST'])
def get_yoga_feedback():
    try:
        pose_name = request.json.get('pose_name')
        image_data = request.json.get('image_data')
        
        image_bytes = base64.b64decode(image_data)
        
        #save the image
        with open("received_image.jpg", "wb") as image_file:
            image_file.write(image_bytes)

        #give feedback
        message = get_feedback("received_image.jpg", pose_name)

        #here we can add something like llm to fix the message feedback

        #remove image
        os.remove("received_image.jpg")
        print(message)
        return jsonify(message=message), 200
    except Exception as e:
        print(str(e))
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
