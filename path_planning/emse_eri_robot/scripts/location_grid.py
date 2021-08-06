#! /usr/bin/env python
import rospy
import math
from nav_msgs.msg import Odometry
from emse_eri_robot_obstacle_14x14 import obstacles
from move_base_msgs.msg import MoveBaseActionGoal

global goal_x
global goal_y


def distance_manhattan(x1, y1, x2, y2):
    x_d = x2 - x1
    y_d = y2 - y1

    value = abs(abs(x_d) + abs(y_d))
    return value

def distance_euclidean(x1, y1, x2, y2):
    x_d = (x2 - x1)^2
    y_d = (y2 - y1)^2

    value = math.sqrt(x_d + y_d)
    return value

def goal_callback(msg):
    global goal_x, goal_y
    raw_goal_x = msg.goal.target_pose.pose.position.x
    raw_goal_y = msg.goal.target_pose.pose.position.y

    goal_x = round(raw_goal_x, 1)
    goal_y = round(raw_goal_y, 1)

    return goal_x, goal_y

goal_x, goal_y = goal_callback()
rospy.loginfo("{}".format(goal_x))

def odometry_callback(msg):
    raw_x = msg.pose.pose.position.x
    raw_y = msg.pose.pose.position.y

    raw_x_one_decimal = round(raw_x, 1)
    raw_y_one_decimal = round(raw_y, 1)

    one_one_position = ""
    one_two_position = ""
    one_three_position = ""
    two_one_position = ""
    two_two_position = "robot"
    two_three_position = ""
    three_one_position = ""
    three_two_position = ""
    three_three_position = ""

    x = round(raw_x * 2)/2
    y = round(raw_y * 2)/2

    three_three_grid = []


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

    robot_to_goal_manhattan = distance_manhattan(raw_x_one_decimal, raw_y_one_decimal, goal_x, goal_y)
    three_three_grid.append(robot_to_goal_manhattan)
    robot_to_goal_eucledian = distance_euclidean(raw_x_one_decimal, raw_y_one_decimal, goal_x, goal_y)
    three_three_grid.append(robot_to_goal_eucledian)
    # rospy.loginfo(three_three_grid)

def main():
    rospy.init_node('location_grid')
    rospy.Subscriber("/odom", Odometry, odometry_callback)
    rospy.Subscriber("/move_base/goal", MoveBaseActionGoal, goal_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass