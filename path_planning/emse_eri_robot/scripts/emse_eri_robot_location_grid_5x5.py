#! /usr/bin/env python
import rospy
import math
import csv
from nav_msgs.msg import Odometry
from emse_eri_robot_obstacle_14x14 import obstacles
from move_base_msgs.msg import MoveBaseActionGoal
from tf.transformations import euler_from_quaternion

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

def calculate_relative_position_x(x1, x2):
    x_d = x2 - x1
    return x_d

def calculate_relative_position_y(y1, y2):
    y_d = y2 - y1
    return y_d

def goal_callback(msg):
    global goal_x, goal_y

def odometry_callback(msg):
    raw_x = msg.pose.pose.position.x
    raw_y = msg.pose.pose.position.y

    raw_x_four_decimal = round(raw_x, 4)
    raw_y_four_decimal = round(raw_y, 4)

    x = round(raw_x, 1)
    y = round(raw_y, 1)

    one_one_position = ""
    one_two_position = ""
    one_three_position = ""
    one_four_position = ""
    one_five_position = ""
    two_one_position = ""
    two_two_position = ""
    two_three_position = ""
    two_four_position = ""
    two_five_position = ""
    three_one_position = ""
    three_two_position = ""
    three_three_position = "robot"
    three_four_position = ""
    three_five_position = ""
    four_one_position = ""
    four_two_position = ""
    four_three_position = ""
    four_four_position = ""
    four_five_position = ""
    five_one_position = ""
    five_two_position = ""
    five_three_position = ""
    five_four_position = ""
    five_five_position = ""

    five_five_grid = []
    time = rospy.get_time()
    five_five_grid.append(time) 
    five_five_grid.append(raw_x_four_decimal)
    five_five_grid.append(raw_y_four_decimal)

    if (x - 0.2, y + 0.2) in obstacles:
        one_one_position = "obstacles"
        five_five_grid.append(obstacles)
    else:
        one_one_position = "free"
        five_five_grid.append(one_one_position)
    
    if (x - 0.1, y + 0.2) in obstacles:
        one_two_position = "obstacles"
        five_five_grid.append(one_two_position)
    else:
        one_two_position = "free"
        five_five_grid.append(one_two_position)

    if (x + 0, y + 0.2) in obstacles:
        one_three_position = "obstacles"
        five_five_grid.append(one_three_position)
    else:
        one_three_position = "free"
        five_five_grid.append(one_three_position)

    if (x + 0.1, y + 0.2) in obstacles:
        one_four_position = "obstacles"
        five_five_grid.append(one_four_position)    
    else:
        one_four_position = "free"
        five_five_grid.append(one_four_position)

    if (x + 0.2, y + 0.2) in obstacles:
        one_five_position = "obstacles"
        five_five_grid.append(one_five_position)
    else:
        one_five_position = "free"
        five_five_grid.append(one_five_position)
    
    if (x - 0.2, y + 0.1) in obstacles:
        two_one_position = "obstacles"
        five_five_grid.append(two_one_position)
    else:
        two_one_position = "free"
        five_five_grid.append(two_one_position)

    if (x - 0.1, y + 0.1) in obstacles:
        two_two_position = "obstacles"
        five_five_grid.append(two_two_position)
    else:
        two_two_position = "free"
        five_five_grid.append(two_two_position)

    if (x + 0, y + 0.1) in obstacles:
        two_three_position = "obstacles"
        five_five_grid.append(two_three_position)
    else:
        two_three_position = "free"
        five_five_grid.append(two_three_position)

    if (x + 0.1, y + 0.1) in obstacles:
        two_four_position = "obstacles"
        five_five_grid.append(two_four_position)
    else:
        two_three_position = "free"
        five_five_grid.append(two_four_position)

    if (x + 0.2, y + 0.1) in obstacles:
        two_five_position = "obstacles"
        five_five_grid.append(two_five_position)
    else:
        two_five_position = "free"
        five_five_grid.append(two_five_position)

    if (x - 0.2, y) in obstacles:
        three_one_position = "obstacles"
        five_five_grid.append(three_one_position)
    else:
        three_one_position = "free"
        five_five_grid.append(three_one_position)

    if (x - 0.1, y) in obstacles:
        three_two_position = "obstacles"
        five_five_grid.append(three_two_position)
    else:
        three_two_position = "free"
        five_five_grid.append(three_two_position)
    
    five_five_grid.append(three_three_position)

    if (x + 0.1, y) in obstacles:
        three_four_position = "obstacles"
        five_five_grid.append(three_four_position)
    else:
        three_four_position = "free"
        five_five_grid.append(three_four_position)

    if (x + 0.2, y) in obstacles:
        three_five_position = "obstacles"
        five_five_grid.append(three_five_position)
    else:
        three_five_position = "free"
        five_five_grid.append(three_five_position)

    if (x - 0.2, y - 0.1) in obstacles:
        four_one_position = "obstacles"
        five_five_grid.append(four_one_position)

    else:
        four_one_position = "free"
        five_five_grid.append(four_one_position)

    if (x - 0.1, y - 0.1) in obstacles:
        four_two_position = "obstacles"
        five_five_grid.append(four_two_position)
    else:
        four_two_position = "free"
        five_five_grid.append(four_two_position)

    if(x, y - 0.1) in obstacles:
        four_three_position = "obstacles"
        five_five_grid.append(four_three_position)

    else:
        four_three_position = "free"
        five_five_grid.append(four_three_position) 

    if (x + 0.1, y - 0.1) in obstacles:
        four_four_position = "obstacles"
        five_five_grid.append(four_four_position)
    else:
        four_four_position = "free"
        five_five_grid.append(four_four_position)

    if (x + 0.2, y - 0.1) in obstacles:
        four_five_position = "obstacles"
        five_five_grid.append(four_five_position)

    else:
        four_five_position = "free"
        five_five_grid.append(four_four_position)

    if (x -0.2, y - 0.2) in obstacles:
        five_one_position = "obstacles"
        five_five_grid.append(five_one_position)

    else:
        five_one_position = "free"
        five_five_grid.append(five_one_position)

    if (x - 0.1, y - 0.2) in obstacles:
        five_two_position = "obstacles"
        five_five_grid.append(five_two_position)
    else:
        five_two_position = "free"
        five_five_grid.append(five_two_position)

    if (x, y -0.2) in obstacles:
        five_three_position = "obstacles"
        five_five_grid.append(five_three_position)

    else:
        five_three_position = "free"
        five_five_grid.append(five_three_position)

    if (x + 0.1, y - 0.2) in obstacles:
        five_four_position = "obstacles"
        five_five_grid.append(five_four_position)

    else:
        five_four_position = "free"
        five_five_grid.append(five_four_position)
    
    if (x + 0.2, y - 0.2) in obstacles:
        five_five_position = "obstacles"
        five_five_grid.append(five_five_position)

    else:
        five_five_position = "free"
        five_five_grid.append(five_five_position)
    
    robot_to_goal_manhattan = distance_manhattan(raw_x_four_decimal, raw_y_four_decimal, goal_x, goal_y)
    five_five_grid.append(robot_to_goal_manhattan)
    robot_to_goal_eucledian = distance_euclidean(raw_x_four_decimal, raw_y_four_decimal, goal_x, goal_y)
    five_five_grid.append(robot_to_goal_eucledian)
    relative_position_to_goal_x = calculate_relative_position_x(raw_x_four_decimal, goal_x)
    five_five_grid.append(relative_position_to_goal_x)

    with open('/home/whiskygrandee/catkin_ws/src/EMSE_Bot_2021/log/configuration_space/14x14_space_5x5_grid.csv', 'a', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(five_five_grid)
    
  
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