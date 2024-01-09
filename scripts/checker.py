#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import String
import math


cir_center_coords = [(0, 0), (0.21, 0.74), (0.79, 0.2), (-0.8, -0.21)]

squ_center_coords = {
    1: (-0.55, 0.65),
    2: (0.83, 0.87),
    3: (0.41, -0.59),
    4: (-0.7, -0.89),
}

RED = 0
BOX = []
last_circle = 0


def is_inside_circle(center_x, center_y, x, y):
    dist = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    return dist < 0.2  # circle radius is 0.2


def is_inside_square(center_x, center_y, x, y):
    half_side = 0.2
    return (
        center_x - half_side <= x <= center_x + half_side
        and center_y - half_side <= y <= center_y + half_side
    )


def odom_callback(msg):
    global RED
    global pub
    global last_circle
    # Get x, y coordinates from Odometry message
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    # rospy.loginfo(f"callback x:{x:.3f}, y:{y:.3f}")

    red = False
    for idx, (xx, yy) in enumerate(cir_center_coords):
        val = is_inside_circle(xx, yy, x, y)
        red |= val
        if val and idx != last_circle:
            last_circle = idx
            RED += 1
    if not red:
        last_circle = -1

    for idx, (xx, yy) in squ_center_coords.items():
        if is_inside_square(xx, yy, x, y) and (len(BOX) == 0 or BOX[-1] != idx):
            BOX.append(idx)

    # rospy.loginfo(f"RED:{RED}, BOX:{BOX}")
    msg = String()
    msg.data = f"RED:{RED}, BOX:{BOX}"
    pub.publish(msg)


pub = None


def main():
    global pub
    rospy.init_node("checker")
    pub = rospy.Publisher("/position_status", String, queue_size=10)
    rospy.Subscriber("/odom", Odometry, odom_callback)

    while not rospy.is_shutdown():
        rospy.spin()


if __name__ == "__main__":
    main()
