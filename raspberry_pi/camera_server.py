from flask import Flask
import subprocess
import os

app = Flask(__name__)

@app.route('/take-picture', methods=['GET'])
def take_picture():
    script_path = '/home/pi/digital_twin_plants/picture_taking_scripts/take_picture_and_upload.py'
    if not os.path.isfile(script_path):
        return f"Script not found at {script_path}", 404

    try:
        result = subprocess.run(
            ['python3', script_path],
            capture_output=True,
            text=True,
            check=True
        )
        return f"Script executed successfully:\n{result.stdout}", 200
    except subprocess.CalledProcessError as e:
        return f"Script execution failed:\n{e.stderr}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
