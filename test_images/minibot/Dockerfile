FROM osrf/ros:jazzy-desktop

COPY entrypoint.sh .

RUN mkdir -p ~/ros_ws/src

RUN apt-get update && apt-get install -y \
    x11-xserver-utils \
    sudo apt-get install ros-${ROS_DISTRO}-ros-gz \
    sudo apt install ros-jazzy-ros2-control \
    sudo apt install ros-jazzy-navigation2 ros-jazzy-nav2-bringup \
    sudo apt install ros-jazzy-twist-mux \
    sudo apt install libserial-dev \
    && rm -rf /var/lib/apt/lists/*

RUN cd ~/ros2_ws/src && \
    git clone -b ros2 https://github.com/Slamtec/rplidar_ros.git \
    git clone https://github.com/joshnewans/twist_stamper.git \
    git clone https://github.com/YJ0528/diffdrive_arduino.git \
    git clone https://github.com/joshnewans/serial \
    git clone https://github.com/digital-twin-autonomous-farmbot/minibot.git \
    cd ../ && colcon build --symlink-install

RUN echo "source ~/ros_ws/install/setup.bash" >> ~/.bashrc








