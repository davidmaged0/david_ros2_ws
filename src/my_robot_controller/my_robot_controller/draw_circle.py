#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCycleNode(Node):
    def __init__(self):
        super().__init__('draw_cycle')
        self.command_vel_pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10) [1]
        self.timer = self.create_timer(0.5, self.send_velocity_command) [2]
        self.get_logger().info('Draw cycle node has been started.') [3]

    def send_velocity_command(self):
        msg = Twist() [4]
        msg.linear.x = 2.0 [4]
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 1.0 [4]
        self.command_vel_pub.publish(msg) [4]

def main(args=None):
    rclpy.init(args=args) [3]
    draw_cycle_node = DrawCycleNode() [2]
    rclpy.spin(draw_cycle_node) [2]
    draw_cycle_node.destroy_node()
    rclpy.shutdown() [3]

if __name__ == '__main__':
    main() 