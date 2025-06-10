import rclpy
from rclpy.node import Node
from rob499_final_cm.msg import Position
import os
import json

class ProcessedPositionNode(Node):
    def __init__(self):
        super().__init__('processed_position_node')
        self.subscription = self.create_subscription(
            Position,
            'averaged_position',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        label = input('Label this position (e.g., position_1): ')
        data = {'angles': list(msg.angles)}
        path = os.path.expanduser(f'~/.ros/ROB499_FINAL/{label}.json')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(data, f)
        self.get_logger().info(f'Saved {label}.json: {data}')


def main(args=None):
    rclpy.init(args=args)
    node = ProcessedPositionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
