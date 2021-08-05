#! /usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from emse_eri_robot_obstacle_14x14 import obstacles

def distance(x1, x2, y1, y2):
    x_d = x2 - x1
    y_d = y2 - y1

    value = abs(abs(x_d) + abs(y_d))
    return value


def odometry_callback(msg):
    raw_x = msg.pose.pose.position.x
    raw_y = msg.pose.pose.position.y
    

    x = round(raw_x, 1)
    y = round(raw_y, 1)

    one_one_position = None
    two_one_position = None
    three_one_position = None
    one_two_position = None
    three_two_position = None
    one_three_position = None
    two_three_position = None
    three_three_position = None

    dist_to_x_minus = x - 0.5
    dist_to_x_plus = x + 0.5
    dist_to_y_minus = y - 0.5
    dist_to_y_plus = y + 0.5

    if (x - 0.5, y) in obstacles:
        two_one_position = "obstacle"
    else:
        two_one_position = "free"

    if (x, y + 0.5) in obstacles:
        one_two_position = "obstacle"
    else:
        two_one_position = "free"

    if (x, y - 0.5) in obstacles:
        three_two_position = "obstacle"
    else:
        three_two_position = "free"
    
    if (x + 0.5, y) in obstacles:
        two_three_position = "obstacle"
    else:
        two_three_position = "free"

    if (x + 0.7, y + 0.7) in obstacles:
        one_three_position = "obstacle"
    else:
        one_three_position = "free"

    if (x - 0.7, y + 0.7) in obstacles:
        one_one_position = "obstacle"
    else:
        one_one_position = "free"
    
    if (x + 0.7, y - 0.7) in obstacles:
        three_three_position = "obstacle"
    else:
        three_three_position = "free"
    
    rospy.loginfo(x)
    rospy.loginfo(y)
    rospy.loginfo(one_one_position)
    rospy.loginfo(three_three_position)


        
        

def main():
    rospy.init_node('location_grid')
    rospy.Subscriber("/odom", Odometry, odometry_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass