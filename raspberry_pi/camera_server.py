from flask import Flask
import subprocess
import datetime
import os

app = Flask(__name__)
IMAGE_DIR = "/home/pi/plant_images"
SCRIPT_PATH = "/home/pi/digital_twin_plants/picture_taking_scripts/take_plant_picture.sh"

@app.route("/take-picture")
def take_picture():
    os.makedirs(IMAGE_DIR, exist_ok=True)
    # Make sure the script is executable
    subprocess.run(["chmod", "+x", SCRIPT_PATH])
    # Run the script
    result = subprocess.run([SCRIPT_PATH])
    
    if result.returncode == 0:
        return "OK: Picture taken successfully\n"
    else:
        return "ERROR: Could not capture image\n", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
