from flask import Flask, request, jsonify
import base64
import os

from yoga_feedback import get_feedback 

current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

app = Flask(__name__)

@app.route('/get_yoga_feedback', methods=['POST'])
def get_yoga_feedback():
	try:
		pose_name = request.json.get('pose_name')
		image_data = request.json.get('image_data')

		print(f"Received pose_name: {pose_name}")
		print(f"Received image data: {image_data[:100]}...")
		
		image_bytes = base64.b64decode(image_data)

		image_path = 'received_image.jpg'

		#save the image
		with open(image_path, 'wb') as image_file:
			image_file.write(image_bytes)

		#give feedback
		message = get_feedback(image_path, pose_name)

		#here we can add something like llm to fix the message feedback
		
		#remove image
		os.remove(image_path)

		return jsonify(message=message), 200
	except Exception as e:
		print(str(e))
		return jsonify(error=str(e)), 400

def get_server_config():
	try:
		with open('server_config.txt', 'r') as config_file:
			config_line = config_file.readline().strip()
			ip_address, port = config_line.split(':')
			port = int(port)
			return ip_address, port
	except Exception as e:
		print(f"Error reading the config file: {str(e)}")
		return None, None

if __name__ == '__main__':
	ip_address, port = get_server_config()
	if ip_address and port:
		app.run(host=ip_address, port=port, debug=True)
