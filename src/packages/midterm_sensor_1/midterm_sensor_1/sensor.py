import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class SensorNode(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Int32, 'sensor1_signal', 10)
        timer_period = 1.2  # 1.2 seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.commands = ['FW', 'TR', 'LF', 'TR']

    def timer_callback(self):
        cmd = self.commands[self.i%4]
                        
        msg = Int32()
        if cmd == 'FW':
            msg.data = random.choice(range(1, 1002, 2))
        elif cmd == 'TR':
            msg.data = - random.choice(range(1, 1002, 2))
        elif cmd == 'LF':
            msg.data = random.choice(range(1, 1002, 2))+1

        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    sensor_node = SensorNode()
    rclpy.spin(sensor_node)
    sensor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()