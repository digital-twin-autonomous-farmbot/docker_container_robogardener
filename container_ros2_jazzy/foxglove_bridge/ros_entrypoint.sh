#!/bin/bash
echo "Sourcing ros_entrypoint.sh"
source /opt/ros/jazzy/setup.bash

exec "$@"