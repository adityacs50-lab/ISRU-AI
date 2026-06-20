#!/usr/bin/env python3
import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node

class RoverController(Node):
    def __init__(self):
        super().__init__('rover_controller')
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info("Rover Controller Started. Moving forward...")
        
    def timer_callback(self):
        twist = Twist()
        twist.linear.x = 0.5  # Move forward at 0.5 m/s
        twist.angular.z = 0.0
        self.cmd_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    controller = RoverController()
    try:
        rclpy.spin(controller)
    except KeyboardInterrupt:
        pass
    finally:
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
