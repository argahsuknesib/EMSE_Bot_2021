#! /usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
import math
import csv
from emse_eri_robot_obstacle_14x14 import obstacles
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

def odometry_callback(msg):
    raw_x= msg.pose.pose.position.x
    raw_y = msg.pose.pose.position.y

    raw_x_four_decimal = round(raw_x, 4)
    raw_y_four_decimal = round(raw_y, 4)

    one_one_position = ""
    one_two_position = ""
    one_three_position = ""
    one_four_position = ""
    one_five_position = ""
    one_six_position = ""
    one_seven_position = ""
    two_one_position = ""
    two_two_position = ""
    two_three_position = ""
    two_four_position = ""
    two_five_position = ""
    two_six_position = ""
    two_seven_position = ""
    three_one_position = ""
    three_two_position = ""
    three_three_position = ""
    three_four_position = ""
    three_five_position = ""
    three_six_position = ""
    three_seven_position = ""
    four_one_position = ""
    four_two_position = ""
    four_three_position = ""
    four_four_position = "robot"
    four_five_position = ""
    four_six_position = ""
    four_five_position = ""
    four_six_position = ""
    four_seven_position = ""
    five_one_position = ""
    five_two_position = ""
    five_three_position = ""
    five_four_position = ""
    five_five_position = ""
    five_six_position = ""
    five_seven_position = ""
    six_one_position = ""
    six_two_position = ""
    six_three_position = ""
    six_four_position = ""
    six_five_position = ""
    six_six_position = ""
    six_seven_position = ""
    seven_one_position = ""
    seven_two_position = ""
    seven_three_position = ""
    seven_four_position = ""
    seven_five_position = ""
    seven_six_position = ""
    seven_seven_position = ""

    x = round(raw_x, 1)
    y = round(raw_y, 1)

    seven_seven_grid = []
    time = rospy.get_time()
    seven_seven_grid.append(time)
    seven_seven_grid.append(raw_x_four_decimal)
    seven_seven_grid.append(raw_y_four_decimal)

    if (x + 0.3, y + 0.3) in obstacles:
        one_one_position = "obstacle"
        seven_seven_grid.append(one_one_position)
    else:
        one_one_position = "free"
        seven_seven_grid.append(one_one_position)
    
    if (x + 0.3, y + 0.2) in obstacles:
        one_two_position = "obstacle"
        seven_seven_grid.append(one_two_position)
    else:
        one_two_position = "free"
        seven_seven_grid.append(one_two_position)

    if (x + 0.3, y + 0.1) in obstacles:
        one_three_position = "obstacle"
        seven_seven_grid.append(one_three_position)
    else:
        one_three_position = "free"
        seven_seven_grid.append(one_three_position)
    
    if (x + 0.3, y ) in obstacles:
        one_four_position = "obstacle"
        seven_seven_grid.append(one_four_position)
    else:
        one_four_position = "free"
        seven_seven_grid.append(one_four_position)

    if (x + 0.3, y - 0.1) in obstacles:
        one_five_position = "obstacle"
        seven_seven_grid.append(one_five_position)
    else:
        one_five_position = "free"
        seven_seven_grid.append(one_five_position)

    if (x + 0.3, y - 0.2) in obstacles:
        one_six_position = "obstacle"
        seven_seven_grid.append(one_six_position)
    else:
        one_six_position = "free"
        seven_seven_grid.append(one_six_position)
    
    if (x + 0.3, y - 0.3) in obstacles:
        one_seven_position = "obstacle"
        seven_seven_grid.append(one_seven_position)
    else:
        one_seven_position = "free"
        seven_seven_grid.append(one_seven_position)

    if (x + 0.2, y + 0.3) in obstacles:
        two_one_position = "obstacle"
        seven_seven_grid.append(two_one_position)
    else:
        two_one_position = "free"
        seven_seven_grid.append(two_one_position)

    if (x + 0.2, y + 0.2) in obstacles:
        two_two_position = "obstacle"
        seven_seven_grid.append(two_two_position)
    else:
        two_two_position = "free"
        seven_seven_grid.append(two_two_position)

    if (x + 0.2, y + 0.1) in obstacles:
        two_three_position = "obstacle"
        seven_seven_grid.append(two_three_position)
    else:
        two_three_position = "free"
        seven_seven_grid.append(two_three_position)

    if (x + 0.2, y ) in obstacles:
        two_four_position = "obstacle"
        seven_seven_grid.append(two_four_position)

    else:
        two_four_position = "free"
        seven_seven_grid.append(two_four_position)

    if (x + 0.2, y - 0.1) in obstacles:
        two_five_position = "obstacle"
        seven_seven_grid.append(two_five_position)
    else:
        two_five_position = "free"
        seven_seven_grid.append(two_five_position)

    if (x + 0.2, y - 0.2) in obstacles:
        two_six_position = "obstacle"
        seven_seven_grid.append(two_six_position)
    else:
        two_six_position = "free"
        seven_seven_grid.append(two_six_position)
    
    if (x + 0.2, y - 0.3) in obstacles:
        two_seven_position = "obstacle"
        seven_seven_grid.append(two_seven_position)
    else:
        two_seven_position = "free"
        seven_seven_grid.append(two_seven_position)

    if (x + 0.1, y + 0.3) in obstacles:
        three_one_position = "obstacle" 
        seven_seven_grid.append(three_one_position)
    else:
        three_one_position = "free"
        seven_seven_grid.append(three_one_position)

    if (x + 0.1, y + 0.2) in obstacles:
        three_two_position = "obstacle"
        seven_seven_grid.append(three_two_position)
    else:
        three_two_position = "free"
        seven_seven_grid.append(three_two_position)

    if (x + 0.1, y + 0.1) in obstacles:
        three_three_position = "obstacle"
        seven_seven_grid.append(three_three_position)
    else:
        three_three_position = "free"
        seven_seven_grid.append(three_three_position)
    
    if (x + 0.1, y) in obstacles:
        three_four_position = "obstacle"
        seven_seven_grid.append(three_three_position)
    else:
        three_four_position = "free"
        seven_seven_grid.append(three_four_position)
    
    if (x + 0.1, y - 0.1) in obstacles:
        three_five_position = "obstacle"
        seven_seven_grid.append(three_five_position)
    else:
        three_five_position = "free"
        seven_seven_grid.append(three_five_position)

    if (x + 0.1, y - 0.2) in obstacles:
        three_six_position = "obstacle"
        seven_seven_grid.append(three_six_position)
    else:
        three_six_position = "free"
        seven_seven_grid.append(three_six_position)
    if (x + 0.1, y - 0.3) in obstacles:
        three_seven_position = "obstacle"
        seven_seven_grid.append(three_seven_position)
    else:
        three_seven_position = "free"
        seven_seven_grid.append(three_seven_position)

    if (x, y + 0.3) in obstacles:
        four_one_position = "obstacle"
        seven_seven_grid.append(four_one_position)

    else:
        four_one_position = "free"
        seven_seven_grid.append(four_one_position)

    if (x, y + 0.2) in obstacles:
        four_two_position = "obstacle"
        seven_seven_grid.append(four_two_position)
    else:
        four_two_position = "free"
        seven_seven_grid.append(four_two_position)

    if (x, y + 0.1) in obstacles:
        four_three_position = "obstacle"
        seven_seven_grid.append(four_three_position)
    else:
        four_three_position = "free"
        seven_seven_grid.append(four_three_position)

    seven_seven_grid.append(four_four_position) 

    if (x, y - 0.1) in obstacles:
        four_five_position = "obstacle"
        seven_seven_grid.append(four_five_position)
    else:
        four_five_position = "free"
        seven_seven_grid.append(four_five_position)
    
    if (x, y - 0.2) in obstacles:
        four_six_position = "obstacle"
        seven_seven_grid.append(four_six_position)
    else:
        four_six_position = "free"
        seven_seven_grid.append(four_six_position)

    if (x, y - 0.3) in obstacles:
        four_seven_position = "obstacle"
        seven_seven_grid.append(four_seven_position)
    else:
        four_seven_position = "free"
        seven_seven_grid.append(four_seven_position)

    if (x - 0.1, y + 0.3) in obstacles:
        five_one_position = "obstacle"
        seven_seven_grid.append(five_one_position)
    else:
        five_one_position = "free"
        seven_seven_grid.append(five_one_position)

    if (x - 0.1, y + 0.2) in obstacles:
        five_two_position = "obstacle"
        seven_seven_grid.append(five_two_position)
    else:
        five_two_position = "free"
        seven_seven_grid.append(five_two_position)

    if (x - 0.1, y + 0.1) in obstacles:
        five_three_position = "obstacle"
        seven_seven_grid.append(five_three_position)
    else:
        five_three_position = "free"
        seven_seven_grid.append(five_three_position)
    
    if (x - 0.1, y) in obstacles:
        five_four_position = "obstacle"
        seven_seven_grid.append(five_four_position)
    else:
        five_four_position = "free"
        seven_seven_grid.append(five_four_position)

    if (x - 0.1, y - 0.1) in obstacles:
        five_five_position = "obstacle"
        seven_seven_grid.append(five_five_position)
    else:
        five_five_position = "free"
        seven_seven_grid.append(five_five_position)

    if (x - 0.1, y - 0.2) in obstacles:
        five_six_position = "obstacle"
        seven_seven_grid.append(five_six_position)
    else:
        five_six_position = "free"
        seven_seven_grid.append(five_six_position)

    if (x - 0.1, y - 0.3) in obstacles:
        five_seven_position = "obstacle"
        seven_seven_grid.append(five_seven_position)
    else:
        five_seven_position = "free"
        seven_seven_grid.append(five_seven_position)

    if (x - 0.2, y + 0.3) in obstacles:
        six_one_position = "obstacle"
        seven_seven_grid.append(six_one_position)
    else:
        six_one_position = "free"
        seven_seven_grid.append(six_one_position)

    if (x - 0.2, y + 0.2) in obstacles:
        six_two_position = "obstacle"
        seven_seven_grid.append(six_two_position)

    else:
        six_two_position = "free"
        seven_seven_grid.append(six_two_position)

    if (x - 0.2, y + 0.1) in obstacles:
        six_three_position = "obstacle"
        seven_seven_grid.append(six_three_position)

    else:
        six_three_position = "free"
        seven_seven_grid.append(six_three_position)      

    if (x - 0.2, y) in obstacles:
        six_four_position = "obstacle"
        seven_seven_grid.append(six_four_position)
    else:
        six_four_position = "free"
        seven_seven_grid.append(six_four_position)

    if (x - 0.2, y - 0.1) in obstacles:
        six_five_position = "obstacle"
        seven_seven_grid.append(six_five_position)
    else:
        six_five_position = "free"
        seven_seven_grid.append(six_five_position)

    if (x - 0.2, y - 0.2) in obstacles:
        six_six_position = "obstacle"
        seven_seven_grid.append(six_six_position)
    else:
        six_six_position = "free"
        seven_seven_grid.append(six_six_position)
    
    if (x - 0.2, y - 0.3) in obstacles:
        six_seven_position = "obstacle"
        seven_seven_grid.append(six_seven_position)
    else:
        six_seven_position = "free"
        seven_seven_grid.append(six_seven_position)

    if (x - 0.3, y + 0.3) in obstacles:
        seven_one_position = "obstacle"
        seven_seven_grid.append(seven_one_position)
    else:
        seven_one_position = "free"
        seven_seven_grid.append(seven_one_position)

    if (x - 0.3, y + 0.2) in obstacles:
        seven_two_position = "obstacle"
        seven_seven_grid.append(seven_two_position)
    else:
        seven_two_position = "free"
        seven_seven_grid.append(seven_two_position)
    
    if (x - 0.3, y + 0.1) in obstacles:
        seven_three_position = "obstacle"
        seven_seven_grid.append(seven_three_position)
    else:
        seven_three_position = "free"
        seven_seven_grid.append(seven_three_position)
    if (x - 0.3, y ) in obstacles:
        seven_four_position = "obstacle"
        seven_seven_grid.append(seven_four_position)
    else:
        seven_four_position = "free"
        seven_seven_grid.append(seven_four_position)

    if (x - 0.3, y - 0.1) in obstacles:
        seven_five_position = "obstacle"
        seven_seven_grid.append(seven_five_position)
    else:
        seven_five_position = "free"
        seven_seven_grid.append(seven_five_position)

    if (x - 0.3, y -0.2) in obstacles:
        seven_six_position = "obstacle"
        seven_seven_grid.append(seven_six_position)
    else:
        seven_six_position = "free"
        seven_seven_grid.append(seven_six_position)
    
    if (x - 0.3, y -0.3) in obstacles:
        seven_seven_position = "obstacle"
        seven_seven_grid.append(seven_seven_position)
    else:
        seven_seven_position = "free"
        seven_seven_grid.append(seven_seven_position)

    robot_to_goal_manhattan = distance_manhattan(raw_x_four_decimal, raw_y_four_decimal, goal_x, goal_y)
    seven_seven_grid.append(robot_to_goal_manhattan)
    robot_to_goal_eucledian = distance_euclidean(raw_x_four_decimal, raw_y_four_decimal, goal_x, goal_y)
    seven_seven_grid.append(robot_to_goal_eucledian)
    relative_position_to_goal_x = calculate_relative_position_x(raw_x_four_decimal, goal_x)
    relative_position_to_goal_x_round = round(relative_position_to_goal_x, 2)
    seven_seven_grid.append(relative_position_to_goal_x_round)
    relative_position_to_goal_y = calculate_relative_position_y(raw_y_four_decimal, goal_y)
    relative_position_to_goal_y_round = round(relative_position_to_goal_y, 2)
    seven_seven_grid.append(relative_position_to_goal_y_round)

    global roll, pitch, yaw
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]

    roll, pitch, yaw = euler_from_quaternion(orientation_list)
    yaw_in_degrees = yaw * 57.2958
    yaw_in_degrees_round = round(yaw_in_degrees)

    seven_seven_grid.append(yaw_in_degrees_round)

    with open('/home/whiskygrandee/catkin_ws/src/EMSE_Bot_2021/log/configuration_space/14x14_space_7x7_grid.csv', 'a', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(seven_seven_grid)

def main():
    rospy.init_node('location_grid')
    rospy.Subscriber("/odom", Odometry, odometry_callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass