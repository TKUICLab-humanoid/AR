#!/usr/bin/env python
#coding=utf-8
import rospy
import numpy as np
from Python_API import Sendmessage
import time
import timeit
import math

HORIZON_HEAD = 3048
HEAD_CHECK = 2080
VERTICAL_HEAD = 2048
X_BENCHMARK = 250   #改大射左
Y_BENCHMARK = 138   #改大射高
SHOOT_DELAY = 0.3   #改大變快

#motion sector
PREPARE = 123   #預備動作
SHOOT = 456       #射擊磁區
HAND_UP = 111     #抬手
LEG_DOWN = 1218   #降手

send = Sendmessage()

class ArcheryTarget:
    def __init__(self):
        self.red_x = 0
        self.red_y = 0
        self.found = False
        
    def find(self):
        if send.get_object:
            for j in range (send.color_mask_subject_cnts[2]):
                for k in range (send.color_mask_subject_cnts[1]):
                    for m in range (send.color_mask_subject_cnts[5]):
                        if -5 <= send.color_mask_subject_X[2][j] - send.color_mask_subject_X[1][k] < 5 and \
                            -5 <= send.color_mask_subject_Y[2][j] - send.color_mask_subject_Y[1][k] <= 5:
                            if -5 <= send.color_mask_subject_X[1][k] - send.color_mask_subject_X[5][m] <= 5 and \
                                -5 <= send.color_mask_subject_Y[1][k] - send.color_mask_subject_Y[5][m] <= 5:
                                self.red_x = send.color_mask_subject_X[5][m]
                                self.red_y = send.color_mask_subject_Y[5][m]
                                self.found = True

            send.get_object = False
        else:
            self.red_x, self.red_y = 0, 0

class Archery:
    def __init__(self):
        rospy.init_node('ar', anonymous=True, log_level=rospy.INFO)

        self.archery_target = ArcheryTarget()
        self.stand = 0
        self.x_points = []
        self.y_points = []
        self.first_point = False
        self.ctrl_status = 'find_period'
        self.lowest_x = 0
        self.lowest_y = 0
        self.turn_right = 0
        self.turn_left = 0
        self.hand_move_cnt = 0
        self.start_time = 0
        self.end_time = 0
        self.init_cnt = 0
        self.archery_action_ready = False
        self.waist_delay = 0

    def initial(self):
        self.x_points = []
        self.y_points = []
        self.first_point = False
        self.ctrl_status = 'find_period'
        self.lowest_x = 0
        self.lowest_y = 0
        self.turn_right = 0
        self.turn_left = 0
        self.hand_move_cnt = 0
        self.start_time = 0
        self.end_time = 0
        self.archery_action_ready = False
        self.waist_delay = 0

    def shoot(self, event):
        rospy.logerr("###### in SHOOT func #####")
        if self.archery_action_ready:
            time.sleep(self.end_time - self.start_time - SHOOT_DELAY)# + self.waist_delay)
            rospy.logerr("!!!!!! SHOOT !!!!!!!")
            send.sendBodySector(SHOOT)
            send.drawImageFunction(6, 1, self.lowest_x-1, self.lowest_x+1, self.lowest_y-1, self.lowest_y+1, 255, 0, 255)
            time.sleep(2)
            send.sendBodySector(999)    #手部退回
            self.archery_action_ready = False

    def main(self):
        if send.is_start:
            if self.init_cnt == 1:
                self.initial()
                send.sendHeadMotor(2,2078,50)
                time.sleep(0.2)
                send.sendHeadMotor(2,2048,50)
                time.sleep(0.8)
                self.init_cnt = 0
            self.archery_target.find()
            if self.ctrl_status == 'find_period':
                if self.archery_target.found:
                    self.x_points.append(self.archery_target.red_x)
                    self.y_points.append(self.archery_target.red_y)
                    rospy.logwarn(f"x: {self.archery_target.red_x}")
                    rospy.logwarn(f'Y: {self.archery_target.red_y}')
                    if not self.first_point:
                        if self.x_points[0] and self.y_points[0] != 0:
                            time.sleep(0.2)
                            self.first_point = True
                    self.archery_target.found = False

                    if len(self.x_points) > 1:
                        dis = ((self.archery_target.red_x-self.x_points[0])**2 + (self.archery_target.red_y-self.y_points[0])**2)**0.5
                        if dis <= 1.5:
                            self.end_time = time.time()
                            self.lowest_y = max(self.y_points)
                            self.lowest_x = self.x_points[self.y_points.index(self.lowest_y)]
                            rospy.loginfo(f"endtime = {self.end_time}")
                            rospy.loginfo(f"period = {self.end_time - self.start_time}")
                            rospy.loginfo(f'low_y = :{self.lowest_y}')
                            rospy.loginfo(f'low_x = :{self.lowest_x}')
                            self.ctrl_status = 'wait_lowest_point'
                    else:
                        self.start_time = time.time()
                        rospy.loginfo(f'starttime = {self.start_time}')

            elif self.ctrl_status == 'wait_lowest_point':
                dis = ((self.archery_target.red_x-self.lowest_x)**2 + (self.archery_target.red_y-self.lowest_y)**2)**0.5
                if dis <= 1:
                    rospy.Timer(rospy.Duration(self.end_time - self.start_time), self.shoot)
                    send.drawImageFunction(6, 1, self.lowest_x-2, self.lowest_x+2, self.lowest_y-2, self.lowest_y+2, 0, 0, 255)
                    rospy.loginfo("at lowest y")
                    self.ctrl_status = 'archery_action'

            elif self.ctrl_status == 'archery_action':
                # archery_action call sector
                #turn waist
                if self.lowest_x - X_BENCHMARK > 0:
                    self.turn_right = X_BENCHMARK - self.lowest_x
                    send.sendSingleMotor(9,int(2.8*self.turn_right),15)
                    rospy.loginfo('turn right')
                    rospy.loginfo(f'turn angle:{self.turn_right}')
                    # self.waist_delay = 0.3
                    time.sleep(3)

                else:
                    self.turn_left = X_BENCHMARK - self.lowest_x
                    send.sendSingleMotor(9,int(2.4*self.turn_left),15)
                    rospy.loginfo('turn left')
                    rospy.loginfo(f'turn angle:{self.turn_left}')
                    # self.waist_delay = 0.3
                    time.sleep(3)

                #hand move
                if self.lowest_y - Y_BENCHMARK > 0:
                    self.hand_move_cnt = abs(int((Y_BENCHMARK - self.lowest_y) / 2))
                    rospy.loginfo('LEG_DOWN')
                    while self.hand_move_cnt != 0:
                        send.sendBodySector(LEG_DOWN)
                        self.hand_move_cnt -= 1
                        time.sleep(0.5)
                    
                else:
                    self.hand_move_cnt = abs(int((self.lowest_y - Y_BENCHMARK) / 2))
                    rospy.loginfo('HAND_UP')
                    rospy.loginfo(f'HAND_UP_cnt:{self.hand_move_cnt}')
                    while self.hand_move_cnt != 0:
                        send.sendBodySector(HAND_UP)
                        rospy.loginfo(f'HAND_UP_cnt:{self.hand_move_cnt}')
                        self.hand_move_cnt -= 1
                        time.sleep(0.5)


                self.archery_action_ready = True
                self.ctrl_status = 'wait_shoot' 
            
            elif self.ctrl_status == 'wait_shoot':
                time.sleep(1)
                rospy.loginfo('wait shoot')

        else:
            if self.stand == 0:
                send.sendHeadMotor(1, HORIZON_HEAD, 80)
                time.sleep(0.5)
                send.sendHeadMotor(1, HORIZON_HEAD, 80)
                time.sleep(0.5)
                send.sendBodySector(PREPARE)
                time.sleep(2.8)
                self.stand = 1
            rospy.logerr('not start')   
            self.init_cnt = 1
            time.sleep(2)    




if __name__ == '__main__':
    try:
        strategy = Archery()
        r =rospy.Rate(20)
        while not rospy.is_shutdown():#劃出起始十字
            send.drawImageFunction(4, 0, 0, 320, 120, 120, 0, 0, 0)
            send.drawImageFunction(5, 0, 160, 160, 0, 240, 0, 0, 0)
            strategy.main()
    except rospy.ROSInterruptException:
        pass