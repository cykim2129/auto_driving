#!/usr/bin/env python3


import rclpy
from geometry_msgs.msg import Twist
import time
import math

def publish_cmd_vel():
    rclpy.init()
    node = rclpy.create_node('cmd_vel_publisher')

    publisher = node.create_publisher(Twist, '/cmd_vel', 10)

    msg = Twist()

    # Sine 파형으로 선속도와 각속도를 제어
    def sine_wave(t, amplitude, frequency):
        return amplitude * math.sin(2 * math.pi * frequency * t)

    loop_frequency = 10  # 루프 주기를 결정하는 변수 (Hz)
    loop_period = 1.0 / loop_frequency  # 루프 주기

    start_time = time.time()

    while rclpy.ok():
        current_time = time.time() - start_time

        # Sine 파형으로 선속도와 각속도 제어
        amplitude_linear = 0.2  # 선속도의 진폭
        frequency_linear = 0.5  # 선속도의 주파수 (Hz)

        amplitude_angular = 0.1  # 각속도의 진폭
        frequency_angular = 0.2  # 각속도의 주파수 (Hz)

        msg.linear.x = sine_wave(current_time, amplitude_linear, frequency_linear)
        msg.angular.z = sine_wave(current_time, amplitude_angular, frequency_angular)

        publisher.publish(msg)
        node.get_logger().info(f'Publishing cmd_vel: linear={msg.linear.x}, angular={msg.angular.z}')

        # time.sleep()을 사용하여 루프 주기를 조절
        time.sleep(loop_period)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    publish_cmd_vel()
