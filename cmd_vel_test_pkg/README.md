# Build

### /cmd_vel 토픽발행  sine파형,step파형,test(직선)파형
-------------


1.scripts 안에 파일들 권한추가

    $chmod -R +x scripts

2.빌드

    $colcon build --symlink-install

3.실행

    $ros2 run cmd_vel_test_pkg cmd_vel_sine.py
    $ros2 run cmd_vel_test_pkg cmd_vel_step.py
    $ros2 run cmd_vel_test_pkg cmd_vel_test.py
    
