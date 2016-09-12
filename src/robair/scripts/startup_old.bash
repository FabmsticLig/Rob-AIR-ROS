#!/bin/bash

source /opt/ros/indigo/setup.bash
source /home/robair/catkin_ws/install/setup.bash

source /home/robair/.bashrc

sleep 15

cd /home/robair/catkin_ws/src/robair/scripts
#./gstreamer_cameras.sh&
sleep 10

cd /home/robair/catkin_ws/src/robair/launch

#roslaunch robair robair.launch&


sleep 10
# Start Web interface
cd /home/robair/RobAirInterfaces/server
#nodejs server.js&
cd /home/robair/RobAirInterfaces/signalingserver
#nodejs server.js&
