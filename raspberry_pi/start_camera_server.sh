#!/bin/bash

# Set paths
SCRIPT_PATH="/home/pi/digital_twin_plants/picture_taking_scripts/take_plant_picture.sh"
SERVER_PATH="/home/pi/docker_container_robotgardener/camera_server.py"
VENV_PATH="/home/pi/camera_env"

# Make sure the camera script is executable
chmod +x "$SCRIPT_PATH"

# Create and activate virtual environment if it doesn't exist

source "$VENV_PATH/bin/activate"

# Run the Flask server
python3 "$SERVER_PATH"
