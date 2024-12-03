#!/bin/bash
source /opt/ros/noetic/setup.bash
source /home/field/project11/catkin_ws/devel/setup.bash
echo "Incorrect detect! Logging previous minute and the next...."
sleep 60s
rosrun rosbag_snapshot snapshot -t -o /media/field/doop2T/incorrect_data/
notify-send "Recording complete, saved to /media/field/doop2T/incorrect_data/"
