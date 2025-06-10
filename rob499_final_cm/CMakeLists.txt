cmake_minimum_required(VERSION 3.8)
project(ROB499_FINAL_CM)

find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Position.msg"
  "srv/SelectPosition.srv"
  DEPENDENCIES std_msgs builtin_interfaces
)

ament_package()
