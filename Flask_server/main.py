from flask import Flask, request, jsonify
import os
from refine_feedback import get_refined_feedback
from yoga_feedback import get_feedback 

current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

app = Flask(__name__)

@app.route('/get_yoga_feedback', methods=['POST'])
def get_yoga_feedback():
	"""
	Get the yoga feedback message for the given pose name
	"""
	try:
		pose_name = request.json.get('pose_name')

		message = get_feedback(pose_name)

		message = get_refined_feedback(message)
		print(message)

		return jsonify(message=message), 200
	except Exception as e:
		print(str(e))
		return jsonify(error=str(e)), 400

def get_server_config():
	"""
	Read the server configuration from the config file
	and return the IP address and port number to run the Flask server
	"""
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
