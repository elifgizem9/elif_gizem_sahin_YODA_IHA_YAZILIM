#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleMover(Node):
    def __init__(self):
        super().__init__('turtle_mover_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_turtle)
        self.get_logger().info('Kaplumbaga Hareketi Baslatildi')

    def move_turtle(self):
        msg = Twist()
        msg.linear.x = 2.0 
        msg.angular.z = 1.0 
        self.publisher_.publish(msg)
        self.get_logger().info(f'Hiz : Linear X: {msg.linear.x}, Angular Z: {msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleMover()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
