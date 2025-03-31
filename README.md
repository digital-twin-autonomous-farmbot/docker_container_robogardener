# Docker Containers for RoboGardener Project

This repository contains all Docker containers built during the **RoboGardener** project.

## ROS 2 Jazzy Container

This folder includes a `Dockerfile` and a `docker-compose.yml` file. The Dockerfile is based on the latest Ubuntu image and installs the ROS 2 Jazzy desktop environment.

The installation follows the official ROS 2 guide:  
[ROS 2 Jazzy Installation Guide](https://docs.ros.org/en/jazzy/Installation/Alternatives/Ubuntu-Development-Setup.html#enable-required-repositories)

Additionally, the repository [digital_twin](https://github.com/digital-twin-autonomous-farmbot/digital_twin.git) is cloned into the container.

### Running the Container with GUI Support (Windows 11 + XLaunch)
To start the container with GUI output using the **XLaunch** application on Windows 11, run:

```bash
docker compose up -d
```

After the containers are built and running, you can open an interactive terminal inside the ROS 2 container with:

```bash
docker exec -it ros2_jazzy bash
```

This setup allows you to interact with ROS 2 within the container while using graphical tools like Rviz and XLaunch.
