# rob499-Robot-Hand
This is a repository for my rob499 class. The goal is to get ros2 and arduino IDE communication. The end goal is to use ros2 to try and recreate muscle memory though averaging of hand positions.
Project Overview:
Contains two main components:
- ROS 2 Packages
- Arduino Sketches
  
Here is the structure for my repositories:
my_robot_project/
├── rob499_final_cm/ # Custom ROS 2 messages & services (CMake)
│ ├── msg/Position.msg
│ ├── srv/SelectPosition.srv
│ ├── CMakeLists.txt
│ └── package.xml
├── rob499_final/ # ROS 2 Python nodes and launch files
│ ├── rob499_final/
│ │ ├── arduino_comm_node.py
│ │ ├── position_input_node.py
│ │ ├── averaging_node.py
│ │ ├── processed_position_node.py
│ │ ├── keypad_trigger_node.py
│ ├── launch/launch_all.py
│ ├── setup.py
│ ├── setup.cfg
│ └── package.xml
├── rob499_arduino_code/ # USES PCA9685 servo‐driver sketch
│ └── rob499_arduino_code.ino
├── rob499_arduino_no_driver/ # Arduino direct‐drive (no driver board) sketch
│ └── rob499_arduino_no_driver.ino

Uses BSD-3 Clause License

Running Robot hand Code:
1. Clone the repo:
   ```bash
   cd ~
   git clone git@github.com:ramos-mat/rob499-Robot-Hand.git my_robot_project
   cd my_robot_project
2. Install dependecies:
   sudo apt update
   sudo apt install python3-colcon-common-extensions ros-jazzy-rclpy ros-jazzy-std-msgs
3. Building my ROS workspace:
   cd ~/my_robot_project
   colcon build
   source install/setup.bash
4. Launching ROS 2 with one command:
   ros2 launch rob499_final launch_all.py


There are two possible sketches that can be ran, depending on the set up used.
- Arduino sketch that uses servo motor driver (PCA9685).
- Arduino sketch that is connected directly to ESP32 board.

For more information such as the set-up of the arduino, make sure to check out the full documentation guide.
