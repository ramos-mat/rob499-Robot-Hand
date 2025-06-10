import rclpy
from rclpy.node import Node
from rob499_final_cm.msg import Position
from std_msgs.msg import Int32

class ArduinoCommNode(Node):
    def __init__(self):
        super().__init__('arduino_comm_node')
        self.subscription = self.create_subscription(
            Position,
            'final_position',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        joint_str = ', '.join([str(angle) for angle in msg.angles])
        self.get_logger().info(f'Sending to Arduino: [{joint_str}]')
        self.get_logger().info('LCD Message: Position sent.')

def main(args=None):
    rclpy.init(args=args)
    node = ArduinoCommNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

