#!/usr/bin/env python
#coding=utf-8
import rospy
import numpy as np
from Python_API import Sendmessage
import time
import timeit

send = Sendmessage()

class AR:
    def __init__(self):
        self.calculate_time = True
        self.code_start = True
        self.status = "Zero"
        self.first_target_x = 0
        self.first_target_y = 0
        self.center_x = 0
        self.center_y = 0
        self.low_y_old = 0
        self.low_x_old  = 0
        self.low_y_end = 0
        self.low_x_end = 0
        self.time_start = 0
        self.time_end = 0
        self.full_period_time = 0
        self.x_left_distance = 0
        self.x_right_distance = 0
        self.y_bottom_distance = 0
        self.y_bottom_count = 0
        self.y_top_distance = 0
        self.y_top_count = 0
        self.motion_time = 0
        self.time_delay = 0

    def find_target(self):
        for j in range (send.color_mask_subject_cnts[2]):
            for k in range (send.color_mask_subject_cnts[1]):
                for m in range (send.color_mask_subject_cnts[5]):
                 if -2 <= send.color_mask_subject_X[2][j] - send.color_mask_subject_X[1][k] <=2 and -2 <= send.color_mask_subject_Y[2][j] - send.color_mask_subject_Y[1][k] <=2:
                    if -2 <= send.color_mask_subject_X[1][k] - send.color_mask_subject_X[5][m] <= 2 and  -2 <= send.color_mask_subject_Y[1][k] - send.color_mask_subject_Y[5][m] <= 2 :
                        self.center_x = send.color_mask_subject_X[5][m]
                        self.center_y = send.color_mask_subject_Y[5][m]

    def low_xy(self):
        self.find_target()
        if self.first_target_y > self.center_y:
            rospy.loginfo(f"aaaaaaaaaaaaaaaaa")
        else:
            #while self.low_y_old <= self.center_y:
               # self.find_target()
            if self.low_y_old <= self.center_y:
                self.low_y_old = self.center_y
                self.low_x_old = self.center_x
                rospy.loginfo(f"aaaaaaaaaaaaaaaaa{self.low_y_old}")
            else:
                self.low_y_end = self.center_y
                self.low_x_end = self.center_x
                rospy.loginfo(f"The lowest center x is {self.low_x_end}")
                rospy.loginfo(f"The lowest center y is {self.low_y_end}")
                self.time_of_period()
                time.sleep(0.5)
                self.status = "second"
                

    def time_of_period(self):
        if self.calculate_time:
            self.time_start = time.time()
        if not self.calculate_time:
            self.time_end = time.time()
            
    def main(self):
        if send.is_start:
            #self.find_target()
            if self.status == "Zero":
               
                self.find_target()
                self.first_target_y = self.center_y
                self.first_target_x = self.center_x
                rospy.loginfo(f"Zero{self.first_target_x},{self.first_target_y}")
                self.status = "First"
            elif self.status == "First":
                self.find_target()
                self.low_xy()
                rospy.loginfo(f"First{self.low_x_end},{self.low_y_end}")
                # self.time_of_period()
                rospy.loginfo(f"Start time is {self.time_start}")
                # if self.first_target_y == self.low_y_old:
                #     self.low_x_end = self.low_x_old
                #     self.low_y_end = self.low_y_old
                #     rospy.loginfo("cccccccccccccccccccccccccc")
                #     self.time_of_period()
                #     rospy.loginfo(f"Start time is {self.time_start}")
                #     self.status = 'second'
                time.sleep(0.1)
            elif self.status == 'second':
                
                self.find_target()
                rospy.loginfo(f"x = {self.center_x - self.low_x_end}, y = {self.center_y - self.low_y_end}")
                if abs(self.center_x - self.low_x_end) <= 1 and abs(self.center_y - self.low_y_end) <= 1:
                    self.calculate_time = False
                    self.time_of_period()
                    rospy.loginfo(f"End time is {self.time_end}")
                    self.full_period_time = self.time_end - self.time_start
                    rospy.loginfo(f"period{self.full_period_time}")
                    self.status = "other"
            elif self.status == "other":
                if self.low_x_end < 257:
                    self.x_left_distance = 257 - self.low_x_end
                    rospy.loginfo(f"turn left")
                    send.sendSingleMotor(9,int(2.5*self.x_left_distance),30)
                    time.sleep(3)
                elif self.low_x_end > 257:
                    self.x_right_distance = 257 - self.low_x_end
                    rospy.loginfo(f"turn right")
                    send.sendSingleMotor(9,int(2.5*self.x_right_distance),30)
                    time.sleep(3)
                # if self.low_y_end > 120:
                #     self.y_bottom_distance = 120 - self.low_y_end
                #     self.y_bottom_count = int(self.y_bottom_distance / 4.2)
                #     for self.count in range(0,self.y_bottom_count):
                #         rospy.loginfo(f"low")
                #         send.sendBodySector(36)
                #         time.sleep(0.5)
                #         rospy.loginfo(f"Extension {self.count}")
                # elif self.low_y_end < 120:
                #     self.y_top_distance = self.low_y_end - 120
                #     self.y_top_count = int(self.y_top_distance / 4.2)
                #     for self.count in range(0,self.y_top_count):
                #         rospy.loginfo(f"high")
                #         send.sendBodySector(37)
                #         time.sleep(0.5)
                #         rospy.loginfo(f"Shortening {self.count}")
                self.motion_time = 2 + 3 + 0.5 * self.y_bottom_count + 0.5 * self.y_top_count
                rospy.loginfo(f"time {self.motion_time}")
                if self.motion_time * 0.67 <= self.full_period_time < self.motion_time:
                    self.full_period_time *= 2
                    rospy.loginfo(f"one")
                elif self.motion_time * 0.33 <= self.full_period_time < self.motion_time * 0.67:
                    self.full_period_time *= 1.95
                    rospy.loginfo(f"three")
                else:
                    self.full_period_time *= 1
                    rospy.loginfo(f"two")
                self.time_delay = self.full_period_time - self.motion_time + 0.5
                if self.time_delay < 0:
                    self.time_delay = self.time_delay + self.motion_time + 0.5
                    rospy.loginfo("bbbbbbbbbbbbbbbbbbbbbb") 
                time.sleep(self.time_delay)
                rospy.loginfo(f"other")
                rospy.loginfo(f"{self.time_delay}")
                rospy.loginfo(f"射擊")
                send.sendBodySector(33)
                self.status = "End"
            elif self.status == "End":
                rospy.loginfo("finish")
                time.sleep(2)
        elif not send.is_start:
            rospy.loginfo(f"歸位")
            time.sleep(2)

if __name__ == '__main__':
    try:
        strategy = AR()
        r = rospy.Rate(20)
        while not rospy.is_shutdown():
            strategy.main()
            r.sleep()
    except rospy.ROSInterruptException:
        pass

