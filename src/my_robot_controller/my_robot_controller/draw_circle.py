#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCycleNode(Node):
    def __init__(self):
        super().__init__("draw_cycle")
        self.command_vel_pub = self.create_publisher(Twist, "turtle1/cmd_vel", 10)         
        self.timer = self.create_timer(0.5, self.send_velocity_command) 
        self.get_logger().info("Draw cycle node has been started.") 

    def send_velocity_command(self):
        msg = Twist() 
        msg.linear.x = 2.0 
        #msg.linear.y = 0.0
        #msg.linear.z = 0.0
        #msg.angular.x = 0.0
       # msg.angular.y = 0.0
        msg.angular.z = 1.0 
        self.command_vel_pub.publish(msg) 

def main(args=None):
    rclpy.init(args=args) 
    node = DrawCycleNode() 
    rclpy.spin(node)
    rclpy.shutdown() 

#if __name__ == '__main__':
#   main() 