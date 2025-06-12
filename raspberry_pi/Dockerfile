# Use ARM64 version of the ros:jazzy-ros-base-noble image
FROM arm64v8/ros:jazzy-ros-base-noble

# Install ROS Jazzy Desktop and required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-jazzy-desktop=0.11.0-1* \
    git \
    python3-pip \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# Create and setup the workspace
WORKDIR /ros2_ws/src
RUN git clone https://github.com/Slamtec/rplidar_ros.git -b ros2

# Build the workspace
WORKDIR /ros2_ws
RUN . /opt/ros/jazzy/setup.sh && \
    colcon build --symlink-install

# Source the workspace in .bashrc
RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc

# Set the workspace as working directory
WORKDIR /ros2_ws
