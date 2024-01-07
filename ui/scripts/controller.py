#!/usr/bin/env python3
    
import rospy 
from kivy.app import App
from kivy.lang import Builder

class NavigationGUIApp(App):
    def build(self):
        return Builder.load_file('navigation_gui.kv')
    


    ########## FUNCTION ON SLIDER ADJUSTMENT ##############
    def on_slider_change(self, value):
        print(f"Speed: {value}%")




    ############ FUNCTION FOR FORWARD BUTTON ################
    def forward(self):
        print(f"Forward")




    ############ FUNCTION FOR BACKWARD BUTTON ################
    def backward(self):
        print(f"Backward")



    ############ FUNCTION FOR YAW LEFT BUTTON ################
    def left(self):
        print(f"Yaw Left")



    ############ FUNCTION FOR YAW RIGHT BUTTON ################
    def right(self):
        print(f"Yaw Right")



    ############ FUNCTION FOR STOP BUTTON ################
    def stop(self):
        print(f"Stop")





if __name__ == '__main__':

    ############### FUNCTIONALITY FOR CONTROLLER NODE #################
    rospy.init_node('navigation_gui')
    NavigationGUIApp().run()
