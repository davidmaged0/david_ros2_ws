#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 

from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class PositionSubscriber(Node):
    def __init__(self):
        super().__init__("position_subscriber")
        self.postion_subscriber = self.create_subscription(Pose, 
                    "turtle1/pose", self.Pose_Callback, 10)
        self.get_logger().info("Position subscriber has been started.")

    def Pose_Callback(self, msg):
        #self.get_logger().info(f"X: {msg.x}, Y: {msg.y}, Theta: {msg.theta}")
        self.get_logger().info(str(msg))

def main(args=None):
    rclpy.init(args=args)
    node = PositionSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()