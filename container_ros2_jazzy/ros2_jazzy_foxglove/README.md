# ROS2 Jazzy Container for Robogardener

This folder contains the Docker Compose configuration for running the ROS2 Jazzy desktop environment with supporting services for the robogardener project.

## Services

### ROS2 Service
- **Container**: `ros2_jazzy_desktop`
- **Purpose**: Main ROS2 environment for robogardener digital twin
- **Build**: Uses local `Dockerfile`
- **Volumes**: Maps repository path and X11 for GUI support
- **Environment**: Configured for display forwarding

### Traefik Reverse Proxy
- **Purpose**: Load balancer and reverse proxy
- **Image**: `traefik:v3.1.2`
- **Ports**: 
  - HTTP: 81 (mapped from 80)
  - Dashboard: 8081 (mapped from 8080)
- **Features**: SSL certificate management with Let's Encrypt
- **Email**: grahanoi@students.zhaw.ch (for SSL certificates)

### Foxglove Bridge
- **Purpose**: WebSocket bridge for ROS2 visualization
- **Build**: Uses local `Dockerfile_foxglove`
- **Port**: 8765
- **Command**: Launches foxglove bridge on specified port
- **Integration**: Accessible through Traefik proxy with domain routing

## Docker Files

### Dockerfile
- **Purpose**: Builds the main ROS2 Jazzy desktop environment
- **Base**: Likely ROS2 Jazzy base image with desktop components
- **Usage**: Used by the `ros2` service for the main robogardener application

### Dockerfile_foxglove
- **Purpose**: Builds container specifically for Foxglove Bridge
- **Usage**: Used by the `foxglove_bridge` service for ROS2 visualization
- **Functionality**: Contains foxglove_bridge package and launch configurations

## Environment Variables Required

The following environment variables must be set before running:

```bash
# Repository path (absolute path to your robogardener repo)
REPO_PATH=/path/to/your/robogardener/repo

# Display configuration (Linux/WSL)
DISPLAY=:0

# Domain for Traefik routing
DOMAIN=your-domain.com
```

## Known Issues

### Windows Compatibility Error

When running on Windows, the following error occurs:

```
time="2025-07-03T06:28:06+02:00" level=warning msg="The \"REPO_PATH\" variable is not set. Defaulting to a blank string."
time="2025-07-03T06:28:06+02:00" level=warning msg="The \"DISPLAY\" variable is not set. Defaulting to a blank string."
time="2025-07-03T06:28:06+02:00" level=warning msg="The \"DOMAIN\" variable is not set. Defaulting to a blank string."
invalid spec: :/ros_ws/src/digital_twin: empty section between colons
```

**Root Cause**: Missing environment variables cause Docker volume mapping to fail with empty REPO_PATH.

**Status**: ⚠️ **Needs testing on Ubuntu** - This configuration may work properly on Linux systems where X11 forwarding and environment variables are handled differently.

## Setup Instructions

### For Linux/Ubuntu (Recommended)

1. Set required environment variables:
```bash
export REPO_PATH=/absolute/path/to/robogardener/repo
export DISPLAY=:0
export DOMAIN=localhost  # or your actual domain
```

2. Allow X11 forwarding (if using GUI):
```bash
xhost +local:docker
```

3. Start services:
```bash
docker compose up -d
```

### For Windows (Currently Not Working)

The current configuration is not compatible with Windows due to:
- X11 display forwarding requirements (`/tmp/.X11-unix` volume)
- Volume mapping syntax issues with empty REPO_PATH
- Environment variable handling differences

**TODO**: Test and verify functionality on Ubuntu system.

## ROS Environment Variables

To add ROS-specific networking configuration, modify the `ros2` service environment section:

```yaml
environment:
  - DISPLAY=${DISPLAY}
  - QT_X11_NO_MITSHM=1
  - ROS_DOMAIN_ID=42
  - ROS_AUTOMATIC_DISCOVERY_RANGE=off
  - ROS_STATIC_PEERS=${ROS_STATIC_PEERS}
```

Set `ROS_STATIC_PEERS` to your Tailscale IP address for network discovery.

## Access Points

Once running successfully:
- **Traefik Dashboard**: http://localhost:8081
- **Foxglove Bridge**: ws://localhost:8765
- **Foxglove via Domain**: ws://${DOMAIN}:8765 (if DOMAIN is set)
- **Main Application**: http://localhost:81

## Networks

All services run on the `ros_network` bridge network, allowing inter-container communication.

## Troubleshooting

1. **Environment Variables**: Ensure all required variables are set before running
2. **Volume Permissions**: Check that REPO_PATH exists and is accessible
3. **Display Forwarding**: On Linux, you may need to run `xhost +local:docker`
4. **SSL Certificates**: Let's Encrypt certificates stored in `./letsencrypt` directory
5. **Build Issues**: Ensure both Dockerfiles exist and build successfully
6. **Network Issues**: Verify Docker network connectivity between services