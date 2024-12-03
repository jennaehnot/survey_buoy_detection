#!/bin/bash
source /opt/ros/noetic/setup.bash
source /home/field/project11/catkin_ws/devel/setup.bash
echo "Saving the previous minute..."
echo "Logging the next minute..."
sleep 60s
rosrun rosbag_snapshot snapshot -t -o /media/field/doop2T/data/log_
notify-send "Recording complete, saved to /media/field/doop2T/data/"

