#!/bin/bash

source /home/field/project11/catkin_ws/devel/setup.bash
session_name="buoy_detection"
tmux new-session -s $session_name -n 1 -d 
tmux select-window -t $session_name:1
tmux split-window -v
tmux send-keys -t $session_name:1.0 "roscore" C-m
sleep 5s
tmux send-keys -t $session_name:1.1 "mon launch detect_buoys detect_buoys.launch" C-m

