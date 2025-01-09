import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

class SensorSubscriber(Node):
    def __init__(self):
        super().__init__('sensor_subscriber')
        self.subscription = self.create_subscription(Int32, '/sensor1_signal', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def listener_callback(self, msg):
        twist = Twist()
        sensor_value = msg.data

        if sensor_value < 0:  
            twist.angular.z = -2.0944
        elif sensor_value % 2 == 1:  
            twist.linear.x = 4.0 
        elif sensor_value % 2 == 0: 
            twist.linear.x = 2.0

        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    sensor_subscriber = SensorSubscriber()
    rclpy.spin(sensor_subscriber)
    sensor_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()