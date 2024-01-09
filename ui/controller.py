from kivy.app import App
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.graphics.texture import Texture
from kivy.clock import Clock

import cv2
import numpy as np
import time
import random

import rospy
from sensor_msgs.msg import Image as Image_topic
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge

BURGER_MAX_LIN_VEL = 0.22
BURGER_MAX_ANG_VEL = 2.84

current_frame = 0
toggle = False
fps = 24.0


def callback_img(data):
    global current_frame
    global toggle
    toggle = True
    # Used to convert between ROS and OpenCV images
    br = CvBridge()
    # Convert ROS Image message to OpenCV image
    current_frame = br.imgmsg_to_cv2(data)


class NavigationGUIApp(App):
    def __init__(self, publisher):
        super().__init__()
        self.pub = publisher
        self.rate = rospy.Rate(1)
        self.slider_value = 50.0
        self.target_lin_vel = self.map_slider_value(
            self.slider_value, 0, 100, 0, BURGER_MAX_LIN_VEL
        )
        self.target_ang_vel = self.map_slider_value(
            self.slider_value, 0, 100, 0, BURGER_MAX_ANG_VEL
        )

    def timed_events(self, *args):
        global toggle
        if toggle:
            toggle = False
            imageFrame = current_frame
            buffer = cv2.flip(imageFrame, 0).tostring()
            texture = Texture.create(
                size=(imageFrame.shape[1], imageFrame.shape[0]), colorfmt="bgr"
            )
            texture.blit_buffer(buffer, colorfmt="rgb", bufferfmt="ubyte")
            self.image_feed.texture = texture

    def map_slider_value(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def on_start(self):
        self.speed_values_field = self.root.ids.speed_values_field
        self.image_feed = self.root.ids.image_frame
        self.task_order = self.root.ids.task_order
        task = [1, 2, 3, 4]
        random.shuffle(task)
        self.task_order.text = f"Task order\n{task[0]}-{task[1]}-{task[2]}-{task[3]}"

    def build(self):
        Clock.schedule_interval(self.timed_events, 1.0 / fps)
        return Builder.load_file("navigation_gui.kv")

    ########## FUNCTION ON SLIDER ADJUSTMENT ##############
    def on_slider_change(self, value):
        self.slider_value = value
        self.target_lin_vel = self.map_slider_value(
            self.slider_value, 0, 100, 0, BURGER_MAX_LIN_VEL
        )
        self.target_ang_vel = self.map_slider_value(
            self.slider_value, 0, 100, 0, BURGER_MAX_ANG_VEL
        )
        self.speed_values_field.text = f"Linear: {self.target_lin_vel:.3f} m/s, Angular: {self.target_ang_vel:.3f} rad/s"
        print(f"Speed: {value}%")

    ############ FUNCTION FOR FORWARD BUTTON ################
    def forward(self):
        print(f"Forward")
        # self.target_lin_vel = self.map_slider_value(self.slider_value, 0, 100, 0, BURGER_MAX_LIN_VEL)
        twist = Twist()
        twist.linear.x = self.target_lin_vel
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        self.pub.publish(twist)

    ############ FUNCTION FOR BACKWARD BUTTON ################
    def backward(self):
        print(f"Backward")
        # self.target_lin_vel = self.map_slider_value(self.slider_value, 0, 100, 0, BURGER_MAX_LIN_VEL)
        twist = Twist()
        twist.linear.x = -self.target_lin_vel
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        self.pub.publish(twist)

    ############ FUNCTION FOR Turn Left BUTTON ################
    def left(self):
        print(f"Turn Left")
        # self.target_ang_vel = self.map_slider_value(self.slider_value, 0, 100, 0, BURGER_MAX_ANG_VEL)
        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = self.target_ang_vel
        self.pub.publish(twist)

    ############ FUNCTION FOR Turn Right BUTTON ################
    def right(self):
        print(f"Turn Right")
        # self.target_ang_vel = self.map_slider_value(self.slider_value, 0, 100, 0, BURGER_MAX_ANG_VEL)
        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = -self.target_ang_vel
        self.pub.publish(twist)

    ############ FUNCTION FOR STOP BUTTON ################
    def stop(self):
        print(f"Stop")
        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        self.pub.publish(twist)


if __name__ == "__main__":
    ############### FUNCTIONALITY FOR CONTROLLER NODE #################
    rospy.init_node("navigation_gui")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    cam_sub = rospy.Subscriber("/image_raw", Image_topic, callback_img)
    app = NavigationGUIApp(pub)
    try:
        app.run()
    except KeyboardInterrupt:
        app.stop()
        pass
