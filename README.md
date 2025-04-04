# Docker Containers for RoboGardener Project

This repository contains all Docker containers built during the **RoboGardener** project.

## ROS 2 Jazzy Container

This folder includes a `Dockerfile` and a `docker-compose.yml` file. The Dockerfile is based on the osrf/ros:jazzy-desktop.
Additionaly it includes:
ros_entrypoint.sh:This is a shell script that acts as the entrypoint for the Docker container. It is executed when the container starts.

**addition**
To run the conatiner a .env file has to be created. 
.env: This file contains environment variables that can be used to configure the Docker container or services. In this file the path to the repository which should be used, can be settled.

For this thesis the repository [digital_twin](https://github.com/digital-twin-autonomous-farmbot/digital_twin.git) is used.

### Running the Container with GUI Support (Windows 11 + XLaunch)
To start the container with GUI output using the **XLaunch** application on Windows 11, run:

```bash
docker compose up -d
```

After the containers are built and running, you can open an interactive terminal inside the ROS 2 container with:

```bash
docker compose run ros2 bash
```

This setup allows you to interact with ROS 2 within the container while using graphical tools like Rviz and XLaunch.

