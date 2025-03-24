#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import sys

class GameNode(Node):
    def __init__(self):
        super().__init__("parametric_motion_node")
        self.command_vel_pub = self.create_publisher(Twist, "turtle1/cmd_vel", 10)         
        self.timer = self.create_timer(0.5, self.send_velocity_command) 
        self.get_logger().info("Draw cycle node has been started.") 

    def send_velocity_command(self):
        msg = Twist() 
        # w (angular Vel) = Vel. / r 
        linear_velocity = float(sys.argv[1])
        radius =float(sys.argv[2])
        msg.linear.x = linear_velocity 
        msg.linear.y = 0.0
        #msg.linear.z = 0.0
        #msg.angular.x = 0.0
       # msg.angular.y = 0.0
        msg.angular.z = linear_velocity / radius 
        self.command_vel_pub.publish(msg) 

def main(args=None):
    rclpy.init(args=args) 
    node = GameNode() 
    rclpy.spin(node)
    rclpy.shutdown() 

#if __name__ == '__main__':
#   main() 