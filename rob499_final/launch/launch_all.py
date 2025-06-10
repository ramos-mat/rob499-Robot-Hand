from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rob499_final',
            executable='arduino_comm_node',
            name='arduino_comm_node',
            output='screen'
        ),
        Node(
            package='rob499_final',
            executable='position_input_node',
            name='position_input_node',
            output='screen'
        ),
        Node(
            package='rob499_final',
            executable='averaging_node',
            name='averaging_node',
            output='screen'
        ),
        Node(
            package='rob499_final',
            executable='processed_position_node',
            name='processed_position_node',
            output='screen'
        ),
        Node(
            package='rob499_final',
            executable='keypad_trigger_node',
            name='keypad_trigger_node',
            output='screen'
        )
    ])
