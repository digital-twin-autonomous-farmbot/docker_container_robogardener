from flask import Flask
import subprocess
import os

app = Flask(__name__)

@app.route('/take-picture', methods=['GET'])
def take_picture():
    script_path = '/home/pi/digital_twin_plants/picture_taking_scripts/take_plant_picture.sh'
    if not os.path.isfile(script_path):
        return f"Script not found at {script_path}", 404

    try:
        result = subprocess.run(['bash', script_path], capture_output=True, text=True, check=True)
        return f"Script executed successfully:\n{result.stdout}", 200
    except subprocess.CalledProcessError as e:
        return f"Script execution failed:\n{e.stderr}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
from flask import Flask
import subprocess
import os
import requests

app = Flask(__name__)

# Path to the shell script
SCRIPT_PATH = '/home/pi/digital_twin_plants/picture_taking_scripts/take_plant_picture.sh'
# Folder where images are saved
IMAGE_DIR = '/home/pi/calib_images'

# Set this to your laptop's IP or Tailscale hostname
IMAGE_API_ENDPOINT = 'http://100.72.230.30:6000/upload'  # Or e.g., http://image_api:6000/upload

@app.route('/take-picture', methods=['GET'])
def take_picture():
    if not os.path.isfile(SCRIPT_PATH):
        return f"Script not found at {SCRIPT_PATH}", 404

    try:
        # Run the script that takes the pictures
        subprocess.run(['bash', SCRIPT_PATH], check=True)

        # Upload each .jpg image to the MongoDB API
        success_count = 0
        for filename in os.listdir(IMAGE_DIR):
            if filename.endswith('.jpg', '.txt'):
                file_path = os.path.join(IMAGE_DIR, filename)
                content_type = 'image/jpeg' if filename.endswith('.jpg') else 'text/plain'

                with open(file_path, 'rb') as f:
                    response = requests.post(
                        IMAGE_API_ENDPOINT,
                        files={'file': (filename, f, content_type)}
                    )
                    if response.ok:
                        success_count += 1
                    else:
                        print(f"Failed to upload {filename}: {response.status_code}")

        return f"Script executed and {success_count} images uploaded.", 200

    except subprocess.CalledProcessError as e:
        return f"Script execution failed:\n{e.stderr}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
