#!/usr/bin/bash
# set -x
 

if [ -d "task_ws" ]; then
  # Actions to perform if task_ws exists
  cd task_ws
  source devel/setup.bash
  
  roslaunch recruitment24_nav_task simulation.launch &

  source kivy_venv/bin/activate
  python3 src/recruitment24_nav_task/ui/controller.py &
  python3 src/recruitment24_nav_task/scripts/checker.py &
  
  rosbag record -O nav_output.bag /odom /position_status &
  wait
  
else
  # Actions to perform if task_ws does not exist
  mkdir -p task_ws/src
  cd task_ws/src

  sudo apt-get update
  sudo apt-get install \
  git \
  python3-pip \
  ros-noetic-turtlebot3 -y
  git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
  git clone https://github.com/InterplanetarCodebase/recruitment24_nav_task.git
  cd ..

  catkin_make
  source devel/setup.bash
  
  roslaunch recruitment24_nav_task simulation.launch &

  python3 -m pip install --upgrade pip setuptools virtualenv
  python3 -m venv kivy_venv
  source kivy_venv/bin/activate

  pip3 install "kivy[base]" rospkg defusedxml numpy pyyaml

  python3 src/recruitment24_nav_task/ui/controller.py &
  python3 src/recruitment24_nav_task/scripts/checker.py &
  
  rosbag record -O nav_output.bag /odom /position_status &
  wait
fi
