#!/usr/bin/env python3

import rclpy
from geometry_msgs.msg import Twist



def publish_cmd_vel():
    rclpy.init()
    node = rclpy.create_node('cmd_vel_publisher')

    publisher = node.create_publisher(Twist, '/cmd_vel', 10)

    msg = Twist()
    msg.linear.x = 0.3  #선속도를 0.2로 설정
    msg.angular.z = 0.2  # 각속도를 0.1로 설정

    try:
        while rclpy.ok():
            publisher.publish(msg)
            node.get_logger().info('Publishing cmd_vel')
            rclpy.spin_once(node, timeout_sec=0.02)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    publish_cmd_vel()
