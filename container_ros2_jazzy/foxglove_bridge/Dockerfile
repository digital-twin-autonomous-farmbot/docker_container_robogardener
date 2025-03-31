FROM osrf/ros:jazzy-desktop-full

# Install foxglove_bridge package
RUN apt-get update && \
    apt-get install -y ros-jazzy-foxglove-bridge && \
    rm -rf /var/lib/apt/lists/*

# Copy ros_entrypoint.sh to the container
COPY ros_entrypoint.sh /ros_entrypoint.sh

# Make sure ros_entrypoint.sh is executable
RUN chmod +x /ros_entrypoint.sh

# Set the entrypoint to use the copied script
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
