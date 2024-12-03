#!/bin/bash
source /opt/ros/noetic/setup.bash
source /home/field/project11/catkin_ws/devel/setup.bash
echo "Logging previous two minutes..."
rosrun rosbag_snapshot snapshot -t -o /media/field/doop2T/past_data/log_
notify-send "Recording complete, saved to /media/field/doop2T/past_data/"

