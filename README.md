# ROS2 Jazzy Container Collection

This repository contains multiple Docker configurations and images for ROS2 Jazzy-based robotics applications, developed as part of a robogardener digital twin project.

## Repository Structure

## test images:

### ros2_jazzy_foxglove/
**Main ROS2 Application Container**
- **Purpose**: Primary ROS2 Jazzy desktop environment with Foxglove visualization
- **Services**: 
  - ROS2 Jazzy desktop with GUI support
  - Traefik reverse proxy (ports 81, 8081)
  - Foxglove Bridge for WebSocket visualization (port 8765)
- **Status**: ⚠️ Currently has Windows compatibility issues - needs Ubuntu testing
- **Features**: SSL certificates, domain routing, X11 forwarding

### minibot/
**Minibot Robotics Container**
- **Purpose**: Container for minibot applications based on [minibot repository](https://github.com/digital-twin-autonomous-farmbot/minibot.git)
- **Base Image**: `osrf/ros:jazzy-desktop`
- **Includes**: Navigation2, Gazebo integration, ROS2 control, serial communication
- **Status**: ❌ Build currently fails due to expired GPG keys for ROS2 repositories
- **Features**: Hardware control interfaces, autonomous navigation capabilities

## raspberry pi

### raspberry_pi/
**Raspberry Pi Services**
- **Purpose**: Camera services and image API for Raspberry Pi deployment
- **Services**:
  - Flask camera server (port 5050)
  - Image API with MongoDB integration (port 6000)
  - ROS plant monitoring service
- **Usage**: 🎓 **Used in Bachelor Thesis:  Autonomous Robot for Plant Management and Energy Efficiency on Photovoltaic Green Rooftops**
- **Features**: Remote picture triggering, image storage, Docker Compose deployment


## Academic Context

### Bachelor Thesis Integration
The **raspberry_pi** folder contains configurations that were specifically developed and utilized in the Bachelor Thesis "Autonomous Robot for Plant Management and Energy Efficiency on Photovoltaic Green Rooftops" focused on autonomous agricultural robotics and digital twin development.

## Common Technologies

All containers in this repository utilize:
- **ROS2 Jazzy**: Latest LTS release of Robot Operating System 2
- **Docker & Docker Compose**: Containerization and orchestration
- **Foxglove Studio**: Modern robotics visualization platform
- **Ubuntu Noble (24.04)**: Base operating system
- **Gazebo**: 3D robotics simulation environment

## Environment Configuration

### Required Environment Variables
Most containers require these environment variables:
```bash
export ROS_DOMAIN_ID=42
export ROS_AUTOMATIC_DISCOVERY_RANGE=off
export ROS_STATIC_PEERS=<tailscale-ip>
export REPO_PATH=/path/to/robogardener/repo
export DISPLAY=:0  # For GUI applications
export DOMAIN=your-domain.com  # For web access
```

### Network Configuration
- **ROS Domain**: ID 42 for network isolation
- **Discovery**: Static peers via Tailscale for secure networking
- **Ports**: Various services exposed on different ports (5050, 6000, 8081, 8765)

## Getting Started

1. **Choose your target platform** (preferably Linux/Ubuntu)
2. **Set required environment variables** for your specific setup
3. **Navigate to the desired container folder**
4. **Follow the specific README** in each folder for detailed instructions

## Known Issues

### General Issues
- **Windows Compatibility**: Most containers have X11 and environment variable issues on Windows
- **GPG Key Expiration**: ROS2 repository keys need updating for successful builds
- **Environment Variables**: Missing variables cause volume mapping failures

### Recommendations
- **Use Ubuntu/Linux** for best compatibility
- **Test on Raspberry Pi** for intended deployment scenarios
- **Update GPG keys** before building images

## Future Development

- Resolve Windows compatibility issues
- Update GPG keys for ROS2 repositories
- Test and validate Ubuntu compatibility
- Enhance cross-platform support
- Integrate additional robogardener services