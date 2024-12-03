#!/bin/bash
source /opt/ros/noetic/setup.bash
source /home/field/project11/catkin_ws/devel/setup.bash
echo "Logging next two minutes..."
sleep 120s
rosrun rosbag_snapshot snapshot -t -o /media/field/doop2T/new_data/log_
notify-send "Recording complete, saved to /media/field/doop2T/new_data/"

