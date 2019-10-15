#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
import os

class Bag_Teleop:
    """
    Class responsible for interpreting joystick commands
    """
    def __init__(self):
        
        # Subscribe should be last, in order to set all required variables
        rospy.Subscriber("/joy", Joy, self.update_joy)
        self.bag_recording = False
        rospy.loginfo("{} is initialized".format(rospy.get_name()))

    def update_joy(self, msg):
        
	if msg.buttons[2]: # X Button
            if self.bag_recording:
                self.bag_recording = False
                os.system("rosnode kill /record")
                rospy.logwarn("Killing recording")
            else:
                self.bag_recording = True
                os.system("roslaunch bag_teleop bag_loc.launch &")
                rospy.logwarn("Launching bag")

        if msg.buttons[6]: # BACK BUTTON
            if self.bag_recording:
                self.bag_recording = False
                os.system("rosnode kill /record")
                rospy.logwarn("killing recording")
            else:
                self.bag_recording = True
                os.system("roslaunch bag_teleop bag.launch &")
                rospy.logwarn("Launching bag")
        if msg.buttons[0]: # A BUTTON
            if self.bag_recording:
                self.bag_recording = False
                os.system("rosnode kill /record")
                rospy.logwarn("killing recording")
            else:
                self.bag_recording = True
                os.system("roslaunch bag_teleop bag_no_lidar.launch &")
                rospy.logwarn("Launching bag no lidar")


    def start(self):
        r = rospy.Rate(20)
        while not rospy.is_shutdown():
            try:
                r.sleep()
            except KeyboardInterrupt:
                break

        rospy.logwarn("{} is shutting down".format(rospy.get_name()))

if __name__ == "__main__":
    rospy.init_node("bag_teleop")
    t = Bag_Teleop()
    t.start()
