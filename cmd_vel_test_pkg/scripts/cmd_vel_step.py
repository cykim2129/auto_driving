#!/usr/bin/env python3

import rclpy
from geometry_msgs.msg import Twist
import time

def publish_cmd_vel():
    rclpy.init()
    node = rclpy.create_node('cmd_vel_publisher')

    publisher = node.create_publisher(Twist, '/cmd_vel', 10)

    msg = Twist()

    # Step 함수의 파형을 정의
    def linear_wave(t):
        if 0 <= t < 3.0:
            return 2.0
        elif 3.0 <= t < 6.0:
            return 0.0
        elif 6.0 <= t < 9.0:
            return 1.5
        elif 9.0 <= t < 12.0:
            return 0.0
        elif 12.0 <= t < 15.0:
            return 1.0
        elif 15.0 <= t < 18.0:
            return 0.0
        elif 18.0 <= t < 21.0:
            return 0.5
        else:
            return 0.0

    def angular_wave(t):
        if 0 <= t < 3.0:
            return 2.0
        elif 3.0 <= t < 6.0:
            return 0.0
        elif 6.0 <= t < 9.0:
            return 1.5
        elif 9.0 <= t < 12.0:
            return 0.0
        elif 12.0 <= t < 15.0:
            return 1.0
        elif 15.0 <= t < 18.0:
            return 0.0
        elif 18.0 <= t < 21.0:
            return 0.5
        else:
            return 0.0



    start_time = time.time()

    try:
        while rclpy.ok():
          current_time = time.time() - start_time

          msg.linear.x = linear_wave(current_time)
          msg.angular.z = angular_wave(current_time)

          publisher.publish(msg)
          node.get_logger().info(f'Publishing cmd_vel: linear={msg.linear.x}, angular={msg.angular.z}')


          time.sleep(0.1)

    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    publish_cmd_vel()
