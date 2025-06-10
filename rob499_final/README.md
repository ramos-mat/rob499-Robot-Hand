# ROB499 Final Project – Simulated ROS 2 Gesture
This project simulates communication between ROS 2 and an Arduino-based robot hand using an ESP32. It features gesture recording, averaging, and triggering based on keypad input.

# Nodes USed

`arduino_comm_node.py`: Simulates sending a gesture to Arduino
`position_input_node.py`: Accepts user input and stores it to a raw folder
`averaging_node.py`: Averages gesture files in a raw folder
`processed_position_node.py`: Saves the averaged gesture to a labeled file
`keypad_trigger_node.py`: Pretends to receive keypad input and triggers a gesture


# To run it
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch rob499_final launch_all.py
