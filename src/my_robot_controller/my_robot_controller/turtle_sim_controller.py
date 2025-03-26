#!/usr/bin/env python3

import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleSimControl(Node):
    def __init__(self):
        super().__init__("turtle_sim_controller")
        self.cmd_velocity_publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.postion_subscriber = self.create_subscription(Pose, "turtle1/pose", self.pose_callback, 10)
        self.get_logger().info("TurtleSim controller started!")

    def pose_callback(self, pose: Pose):
        cmd = Twist()

        if pose.x > 9.5 or pose.x < 2.0 or pose.y > 9.5 or pose.y < 2.0:
            cmd.linear.x = 1.0 
            cmd.angular.z = 9.10
        else:
            cmd.linear.x = 6.0
            cmd.angular.z = 0.0
        self.cmd_velocity_publisher.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSimControl()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()