# Use ARM64 version of the ros:jazzy-ros-base-noble image
FROM arm64v8/ros:jazzy-ros-base-noble

# Install ROS Jazzy Desktop
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-jazzy-desktop=0.11.0-1* \
    && rm -rf /var/lib/apt/lists/*
