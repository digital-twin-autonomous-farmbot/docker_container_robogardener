# Base image with latest Ubuntu
FROM ubuntu:latest

# Set non-interactive mode to avoid interactive prompts
# Set DEBIAN_FRONTEND=noninteractive to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive 
ENV ROS_WS=/ros_ws

# Update system and install dependencies
RUN apt-get update && apt-get install -y \
    git \
    x11-xserver-utils \
    python3-pip \
    software-properties-common \
    curl \
    # Enable required repositories
    && add-apt-repository universe \
    && apt-get update \
    && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null \
    && apt-get update && apt-get install -y \
    # Install ROS 2 Jazzy packages
    ros-jazzy-desktop \
    ros-dev-tools \
    ros-jazzy-xacro \
    ros-jazzy-joint-state-publisher \
    ros-jazzy-joint-state-publisher-gui \
    ros-jazzy-ament-lint-auto \
    # Install development tools
    python3-flake8-blind-except \
    python3-flake8-class-newline \
    python3-flake8-deprecated \
    python3-mypy \
    python3-pip \
    python3-pytest \
    python3-pytest-cov \
    python3-pytest-mock \
    python3-pytest-repeat \
    python3-pytest-rerunfailures \
    python3-pytest-runner \
    python3-pytest-timeout \
    && rm -rf /var/lib/apt/lists/*

# Initialize rosdep
RUN rosdep init && rosdep update

# Ensure ROS 2 is sourced in every new shell
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc

# Set up workspace and clone repository
RUN mkdir -p ${ROS_WS}/src
WORKDIR ${ROS_WS}/src
RUN git clone https://github.com/digital-twin-autonomous-farmbot/digital_twin.git

# Install ROS dependencies
WORKDIR ${ROS_WS}
RUN rosdep install --from-paths src --ignore-src -r -y --skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers"

# Build the workspace
RUN bash -c "source /opt/ros/jazzy/setup.bash && colcon build --symlink-install"

# Source ROS environment in bashrc
RUN echo "source ${ROS_WS}/install/setup.bash" >> ~/.bashrc

# Set up X11 forwarding for GUI applications
ENV DISPLAY=:2
ENV QT_X11_NO_MITSHM=1

# run command: docker run -it --env="DISPLAY=172.30.144.1:2" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" ros2_jazzy 