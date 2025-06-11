import rclpy
from rclpy.node import Node
import os
import json
from datetime import datetime

class PositionInputNode(Node):
    def __init__(self):
        super().__init__('position_input_node')
        self.timer = self.create_timer(1.0, self.prompt_input)

    def prompt_input(self):
        folder = input('Enter target folder name (e.g., position_1_raw): ')
        try:
            angles = [int(input(f'Angle {i+1} (0-180): ')) for i in range(5)]
        except ValueError:
            print('Invalid input. Try again.')
            return

        data = {'angles': angles}
        path = os.path.expanduser(f'~/.ros/rob499_final/{folder}')
        os.makedirs(path, exist_ok=True)
        filename = datetime.now().strftime('%Y%m%d%H%M%S') + '.json'
        with open(os.path.join(path, filename), 'w') as f:
            json.dump(data, f)
        self.get_logger().info(f'Saved input to {folder}/{filename}')


def main(args=None):
    rclpy.init(args=args)
    node = PositionInputNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
