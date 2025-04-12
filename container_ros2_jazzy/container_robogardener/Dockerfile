# Use the existing ROS2 Jazzy desktop image
FROM osrf/ros:jazzy-desktop

# Set non-interactive mode to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive 
ENV ROS_WS=/ros_ws

# Update system and install additional dependencies
RUN apt-get update && apt-get install -y \
    x11-xserver-utils \
    python3-pip \
    software-properties-common \
    curl \
    # Install ros2 jazzy packages
    ros-dev-tools \
    ros-jazzy-xacro \
    ros-jazzy-joint-state-publisher \
    ros-jazzy-joint-state-publisher-gui \
    ros-jazzy-ament-lint-auto \
    ros-jazzy-gz-ros2-control \
    # Install development tools
    python3-flake8-blind-except \
    python3-flake8-class-newline \
    python3-flake8-deprecated \
    python3-mypy \
    python3-pytest \
    python3-pytest-cov \
    python3-pytest-mock \
    python3-pytest-repeat \
    python3-pytest-rerunfailures \
    python3-pytest-runner \
    python3-pytest-timeout \
    && rm -rf /var/lib/apt/lists/*

# Wichtig für ament_python
RUN pip3 install setuptools==58.2.0
# Initialize rosdep if not already initialized
RUN if [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then \
      rosdep init; \
    fi && \
    rosdep update

# Set up workspace
RUN mkdir -p ${ROS_WS}/src
WORKDIR ${ROS_WS}

# Pre-install dependencies (without source code)
RUN touch src/COLCON_IGNORE  # Prevents colcon from failing on empty dir
RUN rosdep install --from-paths src --ignore-src -r -y --skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers"

# Copy entrypoint script
COPY ros_entrypoint.sh /ros_entrypoint.sh
RUN chmod +x /ros_entrypoint.sh

# Source ROS in .bashrc
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc && \
    echo "source ${ROS_WS}/install/setup.bash" >> ~/.bashrc

# X11 and entrypoint
ENV DISPLAY=:2 QT_X11_NO_MITSHM=1
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
