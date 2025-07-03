# Minibot Docker Image

This folder contains the Docker configuration for building a image bases on the https://github.com/digital-twin-autonomous-farmbot/minibot.git repository using a ROS2 Jazzy desktop environment.

## Image Overview

### Base Image
- **Base**: `osrf/ros:jazzy-desktop`
- **Purpose**: Provides ROS2 Jazzy desktop environment with GUI capabilities

### Image Components

The minibot Docker image is designed to include:

- **X11 Support**: X11 server utilities for GUI applications
- **ROS2 Packages**:
  - `ros-jazzy-ros-gz`: Gazebo integration with ROS2
  - `ros-jazzy-ros2-control`: Control framework for robots
  - `ros-jazzy-navigation2` & `ros-jazzy-nav2-bringup`: Navigation stack
  - `ros-jazzy-twist-mux`: Twist message multiplexer
- **Serial Communication**: `libserial-dev` for hardware communication
- **Workspace**: Creates `~/ros_ws/src` directory for ROS2 packages

### Files

- **Dockerfile**: Defines the minibot container build process
- **entrypoint.sh**: Entry point script for container initialization

## Purpose

This image is intended for running minibot robotics applications with:
- Navigation capabilities
- Gazebo simulation support
- Hardware control interfaces
- GUI applications through X11 forwarding

## TODO

### Build Error - GPG Key Issue

The Docker build process currently fails with the following error:

```
ERROR: failed to solve: process "/bin/sh -c apt-get update && apt-get install -y     x11-xserver-utils     sudo apt-get install ros-${ROS_DISTRO}-ros-gz     sudo apt install ros-jazzy-ros2-control     sudo apt install ros-jazzy-navigation2 ros-jazzy-nav2-bringup     sudo apt install ros-jazzy-twist-mux     sudo apt install libserial-dev     && rm -rf /var/lib/apt/lists/*" did not complete successfully: exit code: 100
```

**Root Cause**: 
```
W: GPG error: http://packages.ros.org/ros2/ubuntu noble InRelease: The following signatures were invalid: EXPKEYSIG F42ED6FBAB17C654 Open Robotics <info@osrfoundation.org>
E: The repository 'http://packages.ros.org/ros2/ubuntu noble InRelease' is not signed.
```

The ROS2 repository GPG key has expired, preventing package installation.

**Status**: ❌ **Build currently fails** - GPG key validation error prevents successful image creation.

## Usage (Once Fixed)

```bash
# Build the image
docker build -t minibot .

# Run the container (example)
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  minibot
```

## Environment Variables

When running the container, you may need:
- `DISPLAY`: For X11 forwarding
- `ROS_DOMAIN_ID`: For ROS2 network configuration
- Additional ROS2 networking variables as needed

## Integration

This minibot image is designed to work alongside other containers in the robogardener ecosystem, potentially communicating via ROS2 topics and services.