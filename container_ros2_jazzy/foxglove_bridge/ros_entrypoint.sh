#!/bin/bash
set -e

# Debug: Print environment info
echo "=== ENTRYPOINT STARTED ==="
echo "ROS_DISTRO: $ROS_DISTRO"
echo "WORKSPACE: /ros_ws"

# Source ROS (with error checking)
if [ -f "/opt/ros/jazzy/setup.bash" ]; then
    source /opt/ros/jazzy/setup.bash
    echo "ROS sourced successfully"
else
    echo "ERROR: ROS setup.bash not found!"
    exit 1
fi

# Workspace build logic
if [ -d "/ros_ws/src/digital_twin" ]; then
    echo "Source code detected at /ros_ws/src/digital_twin"
    
    # Remove any build blockers
    rm -f /ros_ws/src/COLCON_IGNORE 2>/dev/null
    
    # Always install dependencies (no harm in re-running)
    echo "Installing dependencies..."
    cd /ros_ws
    rosdep install --from-paths src --ignore-src -r -y
    
    # Build if needed
    if [ ! -d "/ros_ws/install" ] || [ "/ros_ws/src/digital_twin" -nt "/ros_ws/install" ]; then
        echo "Building workspace..."
        colcon build --symlink-install
        
        # Verify build
        if [ $? -ne 0 ]; then
            echo "ERROR: Build failed! Check logs in /ros_ws/log"
            exit 1
        fi
    else
        echo "Workspace already built (install/ is up-to-date)"
    fi
    
    # Source the workspace
    if [ -f "/ros_ws/install/setup.bash" ]; then
        source /ros_ws/install/setup.bash
        echo "Workspace sourced successfully"
    else
        echo "ERROR: Workspace setup.bash not found!"
        exit 1
    fi
else
    echo "ERROR: Source code not found at /ros_ws/src/digital_twin!"
    echo "Contents of /ros_ws/src:"
    ls -la /ros_ws/src
    exit 1
fi

echo "=== ENTRYPOINT COMPLETE ==="

# Keep container alive if no command specified
if [ "$#" -eq 0 ]; then
    exec bash
else
    exec "$@"
fi