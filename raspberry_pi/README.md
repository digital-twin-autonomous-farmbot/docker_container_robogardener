# Raspberry Pi Camera and Image API Service

This folder contains the necessary components to run the camera service and image API on a Raspberry Pi.

## Components

### Camera Server
- [`camera_server.py`](camera_server.py): Flask server that handles requests to take pictures
- [`start_camera_server.sh`](start_camera_server.sh): Script to set up and start the camera server
- [`trigger_picture.sh`](trigger_picture.sh): Utility script to trigger picture taking remotely

### Image API
- [`image_api/app.py`](image_api/app.py): Flask API for handling image uploads to MongoDB
- [`image_api/Dockerfile`](image_api/Dockerfile): Container definition for the image API
- [`image_api/requirements.txt`](image_api/requirements.txt): Python dependencies

### Docker Configuration
- [`docker-compose.yml`](docker-compose.yml): Defines services for:
  - ROS plant monitoring service
  - Image API service
  - MongoDB database

## Setup and Usage

1. Start all services using Docker Compose:
```bash
docker compose up -d
```

2. The following services will be available:
- Camera Server: Port 5050
- Image API: Port 6000
- MongoDB: Port 27017

3. To trigger a picture remotely:
```bash
./trigger_picture.sh
```

## Environment Requirements

- Raspberry Pi with camera module
- Docker and Docker Compose installed
- Python 3.x
- MongoDB (runs in container)

## Service Architecture

1. Camera Server (`:5050`)
   - Handles incoming requests to take pictures
   - Executes camera scripts on the Raspberry Pi

2. Image API (`:6000`)
   - Manages image uploads
   - Stores images in MongoDB with metadata

3. MongoDB
   - Stores images and metadata
   - Persists data using Docker volume