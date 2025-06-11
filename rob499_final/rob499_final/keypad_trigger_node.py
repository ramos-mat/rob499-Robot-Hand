import rclpy
from rclpy.node import Node
from rob499_final_cm.msg import Position
import os
import json

class KeypadTriggerNode(Node):
    def __init__(self):
        super().__init__('keypad_trigger_node')
        self.publisher = self.create_publisher(Position, 'final_position', 10)
        self.timer = self.create_timer(1.0, self.check_input)

    def check_input(self):
        key = input('Enter keypad input (1-9): ')
        if not key.isdigit():
            return
        filename = f'position_{key}.json'
        path = os.path.expanduser(f'~/.ros/rob499_final/{filename}')
        if not os.path.exists(path):
            self.get_logger().info(f'{filename} not found.')
            return
        with open(path, 'r') as f:
            data = json.load(f)
            msg = Position()
            msg.angles = data['angles']
            self.publisher.publish(msg)
            self.get_logger().info(f'Sent position_{key} to final_position topic.')

def main(args=None):
    rclpy.init(args=args)
    node = KeypadTriggerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
