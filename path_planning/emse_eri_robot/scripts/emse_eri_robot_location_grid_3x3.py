#! /usr/bin/env python
import rospy
import math
import csv
from nav_msgs.msg import Odometry
from emse_eri_robot_obstacle_14x14 import obstacles
from tf.transformations import euler_from_quaternion

pub = None

goal_x = 1
goal_y = 1

roll = pitch = yaw = 0

def distance_manhattan(x1, y1, x2, y2):
    x_d = x2 - x1
    y_d = y2 - y1

    value = abs(abs(x_d) + abs(y_d))
    value_rounded_two_decimal = round(value, 2)
    return value_rounded_two_decimal

def distance_euclidean(x1, y1, x2, y2):
    x_d = (x2 - x1)**2
    y_d = (y2 - y1)**2

    value = math.sqrt(x_d + y_d)
    value_rounded_two_decimal = round(value, 2)
    return value_rounded_two_decimal

def goal_callback(msg):
    global goal_x, goal_y
    raw_goal_x = msg.goal.target_pose.pose.position.x
    raw_goal_y = msg.goal.target_pose.pose.position.y

    goal_x = round(raw_goal_x, 1)
    goal_y = round(raw_goal_y, 1)

    return goal_x, goal_y


def odometry_callback(msg):
    raw_x = msg.pose.pose.position.x
    raw_y = msg.pose.pose.position.y

    raw_x_four_decimal = round(raw_x, 4)
    raw_y_four_decimal = round(raw_y, 4)

    one_one_position = ""
    one_two_position = ""
    one_three_position = ""
    two_one_position = ""
    two_two_position = "robot"
    two_three_position = ""
    three_one_position = ""
    three_two_position = ""
    three_three_position = ""

    x = round(raw_x, 1)
    y = round(raw_y, 1)

    three_three_grid = []
    time = rospy.get_time()
    three_three_grid.append(time)
    three_three_grid.append(raw_x_four_decimal)
    three_three_grid.append(raw_y_four_decimal)

    if (x + 1, y + 1) in obstacles:
        one_one_position = "obstacle"
        three_three_grid.append(one_one_position)
    else:
        one_one_position = "free"
        three_three_grid.append(one_one_position)

    if (x + 1, y) in obstacles:
        one_two_position = "obstacle"
        three_three_grid.append(one_two_position)
    else:
        one_two_position = "free"
        three_three_grid.append(one_two_position)

    if (x + 1, y - 1) in obstacles:
        one_three_position = "obstacle"
        three_three_grid.append(one_three_position)
    else:
        one_three_position = "free"
        three_three_grid.append(one_three_position)

    if (x, y + 1)in obstacles:
        two_one_position = "obstacle"
        three_three_grid.append(two_one_position)
    else:
        two_one_position = "free"
        three_three_grid.append(two_one_position)

    two_two_position = "robot"
    three_three_grid.append(two_two_position)

    if (x, y - 1) in obstacles:
        two_three_position = "obstacle"
        three_three_grid.append(two_three_position)
    else:
        two_three_position = "free"
        three_three_grid.append(two_three_position)
    
    if (x - 1, y + 1) in obstacles:
        three_one_position = "obstacle"
        three_three_grid.append(three_one_position)
    else:
        three_one_position = "free"
        three_three_grid.append(three_one_position)

    if (x - 1, y) in obstacles:
        three_two_position = "obstacle"
        three_three_grid.append(three_two_position)
    else:
        three_two_position = "free"
        three_three_grid.append(three_two_position)
    
    if (x - 1, y -1) in obstacles:
        three_three_position = "obstacle"
        three_three_grid.append(three_three_position)
    else:
        three_three_position = "free"
        three_three_grid.append(three_three_position)

    robot_to_goal_manhattan = distance_manhattan(raw_x_four_decimal, raw_y_four_decimal, goal_x, goal_y)
    three_three_grid.append(robot_to_goal_manhattan)
    robot_to_goal_eucledian = distance_euclidean(raw_x_four_decimal, raw_y_four_decimal, goal_x, goal_y)
    three_three_grid.append(robot_to_goal_eucledian)


    global roll, pitch, yaw
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]

    roll, pitch, yaw = euler_from_quaternion(orientation_list)
    yaw_in_degrees = yaw * 57.2958
    yaw_in_degrees_round = round(yaw_in_degrees)
    three_three_grid.append(yaw_in_degrees_round)

    with open('/home/whiskygrandee/catkin_ws/src/emse_bot/log/configuration_space/14x14_space_3x3_grid.csv', 'a', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(three_three_grid)

def main():
    rospy.init_node('location_grid')
    rospy.Subscriber("/odom", Odometry, odometry_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass