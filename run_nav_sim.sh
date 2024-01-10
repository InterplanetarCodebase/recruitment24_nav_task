#!/usr/bin/bash
# set -x
 

if [ -d "task_ws" ]; then
  # Actions to perform if task_ws exists
  cd task_ws
  source devel/setup.bash
  
  roslaunch recruitment24_nav_task simulation.launch & 
  source kivy_venv/bin/activate

  echo "DONE --------------------------------- 1"
  
  python3 src/recruitment24_nav_task/ui/controller.py &
  python3 src/recruitment24_nav_task/scripts/checker.py &
  rosbag record -O nav_output.bag /odom /position_status &
  wait
  
  echo "DONE --------------------------------- 2"

else
  # Actions to perform if task_ws does not exist
  mkdir -p task_ws/src
  cd task_ws/src

  sudo apt-get update
  sudo apt-get install \
  git \
  python3-pip \
  ros-noetic-turtlebot3 -y
  
  echo "DONE --------------------------------- 4"
  
  git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
  
  echo "DONE --------------------------------- 5"
  
  git clone https://github.com/InterplanetarCodebase/recruitment24_nav_task.git
  
  echo "DONE --------------------------------- 6"
  
  cd ..

  catkin_make 
  
  echo "DONE --------------------------------- 7"
  
  source devel/setup.bash
  
  roslaunch recruitment24_nav_task simulation.launch &

  python3 -m pip install --upgrade pip setuptools virtualenv
  
  echo "DONE --------------------------------- 9"
  
  python3 -m venv kivy_venv
  
  echo "DONE --------------------------------- 10"
  
  source kivy_venv/bin/activate

  pip3 install "kivy[base]" rospkg defusedxml numpy pyyaml opencv-python
  
  echo "DONE --------------------------------- 11"

  python3 src/recruitment24_nav_task/ui/controller.py &
  python3 src/recruitment24_nav_task/scripts/checker.py &
  rosbag record -O nav_output.bag /odom /position_status &
  wait
  
  echo "DONE --------------------------------- 12"
fi
