#!/usr/bin/env python
#coding=utf-8
import rospy
import numpy as np
# import sys
# sys.path.append('/home/iclab/Desktop/adult_hurocup/src/strategy')
from Python_API import Sendmessage
import time
import timeit
import math

HORIZON_HEAD = 3048
HEAD_CHECK = 2080
VERTICAL_HEAD = 2048
X_BENCHMARK = 255   #改大射左
Y_BENCHMARK = 150   #改大射高
SHOOT_DELAY = 0.25   #改大變快  不同週期須測試 0.3sOK 0.2~sOK

#motion sector
PREPARE = 123   #預備動作
SHOOT = 456       #射擊磁區
HAND_UP = 111     #抬手
HAND_BACK = 112
LEG_DOWN = 1218   #降手
LEG_BACK = 1219

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
                        if np.array(send.color_mask_subject_size[2])[j] > 3500:
                            if -5 <= np.array(send.color_mask_subject_X[2])[j] - np.array(send.color_mask_subject_X[1])[k] < 5 and \
                                -5 <= np.array(send.color_mask_subject_Y[2])[j] - np.array(send.color_mask_subject_Y[1])[k] <= 5:
                                if -5 <= np.array(send.color_mask_subject_X[1])[k] - np.array(send.color_mask_subject_X[5])[m] <= 5 and \
                                    -5 <= np.array(send.color_mask_subject_Y[1])[k] - np.array(send.color_mask_subject_Y[5])[m] <= 5:
                                    self.red_x = np.array(send.color_mask_subject_X[5])[m]
                                    self.red_y = np.array(send.color_mask_subject_Y[5])[m]
                                    self.red_y = np.array(send.color_mask_subject_Y[5])[m]
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
        self.turn_value = 0
        self.hand_move_cnt = 0
        self.leg_move_cnt = 0
        self.start_time = 0
        self.end_time = 0
        self.period = 0
        self.init_cnt = 0
        self.archery_action_ready = False
        self.timer = 0
        self.back_flag = False
        self.turn_left_cnt = 0
        self.turn_right_cnt = 0
        self.hand_back_cnt = 0
        self.leg_back_cnt = 0
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
        self.turn_value = 0
        self.hand_move_cnt = 0
        self.leg_move_cnt = 0
        self.start_time = 0
        self.end_time = 0
        self.period = 0
        self.archery_action_ready = False
        self.timer = 0
        self.back_flag = False
        self.turn_left_cnt = 0
        self.turn_right_cnt = 0
        self.hand_back_cnt = 0
        self.leg_back_cnt = 0
        self.waist_delay = 0

    def shoot(self, event):
        rospy.logerr("###### in SHOOT func #####")
        if self.archery_action_ready:
            time.sleep(self.period - SHOOT_DELAY + self.waist_delay)
            rospy.loginfo(f"shoot delay = {self.period - SHOOT_DELAY + self.waist_delay}")
            rospy.logerr("!!!!!! SHOOT !!!!!!!")
            send.sendBodySector(SHOOT)
            send.drawImageFunction(6, 1, self.lowest_x-1, self.lowest_x+1, self.lowest_y-1, self.lowest_y+1, 255, 0, 255)
            time.sleep(2)
            send.sendBodySector(999)    #手部退回
            self.timer.shutdown()
            self.archery_action_ready = False
            self.back_flag = True

    def main(self):
        if send.is_start:

            if self.init_cnt == 1:
                self.initial()
                send.sendHeadMotor(2,2078,50)
                time.sleep(0.2)
                send.sendHeadMotor(2,2048,50)
                time.sleep(1)
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
                            self.period = self.end_time - self.start_time
                            rospy.loginfo(f"endtime = {self.end_time}")
                            rospy.loginfo(f"period = {self.period}")
                            rospy.loginfo(f'low_y = :{self.lowest_y}')
                            rospy.loginfo(f'low_x = :{self.lowest_x}')
                
                            self.ctrl_status = 'wait_lowest_point'

                    else:
                        self.start_time = time.time()
                        rospy.loginfo(f'starttime = {self.start_time}')

            elif self.ctrl_status == 'wait_lowest_point':
                dis = ((self.archery_target.red_x-self.lowest_x)**2 + (self.archery_target.red_y-self.lowest_y)**2)**0.5
                if dis <= 1:
                    self.timer = rospy.Timer(rospy.Duration(self.period), self.shoot)
                    send.drawImageFunction(6, 1, self.lowest_x-2, self.lowest_x+2, self.lowest_y-2, self.lowest_y+2, 0, 0, 255)
                    rospy.loginfo("at lowest y")
                    self.ctrl_status = 'archery_action'

            elif self.ctrl_status == 'archery_action':
                # archery_action call sector
                #turn waist
                if self.lowest_x - X_BENCHMARK > 0:
                    self.turn_right = X_BENCHMARK - self.lowest_x
                    send.sendSingleMotor(9,int(2.8*self.turn_right),20)
                    rospy.loginfo('turn right')
                    rospy.loginfo(f'turn angle:{self.turn_right}')
                    self.turn_right_cnt = 1
                    # self.waist_delay = 0.3
                    time.sleep(2)

                else:
                    self.turn_left = X_BENCHMARK - self.lowest_x
                    # if self.turn_left > 110 or self.turn_left < 30:
                    #     self.turn_value = 2.25
                    # else:
                    self.turn_value = 2.3

                    send.sendSingleMotor(9,int(self.turn_value*self.turn_left),20)    
                    rospy.loginfo(f'turn left : {self.turn_left}')
                    rospy.loginfo(f'turn value :{self.turn_value}')
                    rospy.loginfo(f'turn angle :{self.turn_value*self.turn_left}')
                    self.turn_left_cnt = 1
                    time.sleep(3)

                #hand move
                if self.lowest_y - Y_BENCHMARK > 0:
                    self.leg_move_cnt = abs(int((Y_BENCHMARK - self.lowest_y) / 2))
                    self.leg_back_cnt = self.leg_move_cnt
                    rospy.loginfo('LEG_DOWN')
                    while self.leg_move_cnt != 0:
                        send.sendBodySector(LEG_DOWN)
                        self.leg_move_cnt -= 1
                        time.sleep(0.5)
                    
                else:
                    self.hand_move_cnt = abs(int((self.lowest_y - Y_BENCHMARK) / 2))
                    self.hand_back_cnt = self.hand_move_cnt
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
                # send.sendBodySector(PREPARE)
                time.sleep(2.8)
                rospy.logerr('not start')
                self.stand = 1

            if self.back_flag:
                if self.turn_right_cnt != 0:
                    send.sendSingleMotor(9,int(-(2.8*self.turn_right)),15)
                    rospy.loginfo(f'turn left angle :{self.turn_value*self.turn_left}')
                    time.sleep(2)

                elif self.turn_left_cnt != 0:
                    send.sendSingleMotor(9,int(-(self.turn_value*self.turn_left)),15)
                    rospy.loginfo(f'turn right angle :{self.turn_value*self.turn_left}')
                    time.sleep(2)

                for i in range(0, self.hand_back_cnt):
                    send.sendBodySector(HAND_BACK)
                    rospy.loginfo(f'HAND_back_cnt:{self.hand_back_cnt}')
                    self.hand_back_cnt -= 1
                    time.sleep(0.5)

                for i in range(0, self.leg_back_cnt):
                    send.sendBodySector(LEG_BACK)
                    rospy.loginfo(f'LEG_back_cnt:{self.leg_back_cnt}')
                    self.hand_back_cnt -= 1
                    time.sleep(0.5)

                self.back_flag = False
                rospy.logerr('not start')
   
            self.init_cnt = 1
            time.sleep(0.2)    




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