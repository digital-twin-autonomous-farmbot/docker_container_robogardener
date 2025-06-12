from flask import Flask
import subprocess
import datetime
import os

app = Flask(__name__)
IMAGE_DIR = "/home/pi/plant_images"

@app.route("/take-picture")
def take_picture():
    os.makedirs(IMAGE_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = os.path.join(IMAGE_DIR, f"plant_{timestamp}.jpg")
    result = subprocess.run(["libcamera-jpeg", "-o", image_path])
    if result.returncode == 0:
        return f"OK: {image_path}\n"
    else:
        return "ERROR: Could not capture image\n", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
