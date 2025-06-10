import rclpy
from rclpy.node import Node
from rob499_final_cm.msg import Position
import os
import json

class AveragingNode(Node):
    def __init__(self):
        super().__init__('averaging_node')
        self.publisher = self.create_publisher(Position, 'averaged_position', 10)
        self.timer = self.create_timer(1.0, self.prompt_folder)

    def prompt_folder(self):
        folder = input('Enter folder to average (e.g., position_1_raw): ')
        path = os.path.expanduser(f'~/.ros/ROB499_FINAL/{folder}')
        if not os.path.exists(path):
            self.get_logger().info('Folder does not exist.')
            return

        files = [f for f in os.listdir(path) if f.endswith('.json')]
        if len(files) == 0:
            self.get_logger().info('No files to average.')
            return

        total = [0] * 5
        for file in files:
            with open(os.path.join(path, file), 'r') as f:
                data = json.load(f)
                for i in range(5):
                    total[i] += data['angles'][i]

        avg = [round(val / len(files)) for val in total]
        msg = Position()
        msg.angles = avg
        self.publisher.publish(msg)
        self.get_logger().info(f'Published averaged position: {avg}')

def main(args=None):
    rclpy.init(args=args)
    node = AveragingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
