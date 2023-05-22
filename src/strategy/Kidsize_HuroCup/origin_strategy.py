#!/usr/bin/env python
#coding=utf-8
import rospy
import numpy as np
from Python_API import Sendmessage
import time
import timeit
import math

HORIZON_HEAD = 2912
HEAD_CHECK = 2080
VERTICAL_HEAD = 2048
X_BENCHMARK = 158   #改大射左
Y_BENCHMARK = 157   #改大射高A
X_MOTOR_SCALE = 4.6
Y_MOTOR_SCALE = 1.4
LEFT_WAIST_FIX = 1
SHOOT_FLOW_WAIT = 1.4

send = Sendmessage()

class FindTarget:
    def __init__(self):
        self.red_color_xmin = 0
        self.red_color_xmax = 0
        self.red_color_ymin = 0
        self.red_color_ymax = 0
        self.red_color_x = 0
        self.red_color_y = 0
        
    def find_target(self):
        for j in range (send.color_mask_subject_cnts[2]):
            for k in range (send.color_mask_subject_cnts[1]):
                for m in range (send.color_mask_subject_cnts[5]):
                    if -3 <= send.color_mask_subject_X[2][j] - send.color_mask_subject_X[1][k] <= 3 and \
                        -3 <= send.color_mask_subject_Y[2][j] - send.color_mask_subject_Y[1][k] <= 3:
                        if -3 <= send.color_mask_subject_X[1][k] - send.color_mask_subject_X[5][m] <= 3 and \
                            -3 <= send.color_mask_subject_Y[1][k] - send.color_mask_subject_Y[5][m] <= 3:
                            self.red_color_xmin = send.color_mask_subject_XMin[5][m]
                            self.red_color_xmax = send.color_mask_subject_XMax[5][m]
                            self.red_color_ymin = send.color_mask_subject_YMin[5][m]
                            self.red_color_ymax = send.color_mask_subject_YMax[5][m]
                            self.red_color_x = send.color_mask_subject_X[5][m]
                            self.red_color_y = send.color_mask_subject_Y[5][m]
                            
                            send.drawImageFunction(2, 1, self.red_color_xmin, self.red_color_xmax, self.red_color_ymin, self.red_color_ymax, 0, 0, 255)

class FindMoveShoot:
    def __init__(self):
        self.x_diff = 0
        self.y_diff = 0 
        self.turn_right = 0     #向右的次數
        self.turn_left = 0      #向左的次數
        self.down = 0           #向下的次數
        self.up = 0             #向上的次數
        self.circulate = 0      #用於迴圈
        self.loop = 0           #用於迴圈
        self.move_time = 0      #做完所有動作需要的時間
        self.stand = 0          #用於啟動起始站姿
        self.waist_move = 0
        self.hand_move = 0
        self.wait_time = 0
        self.lowest_x = 320     #最低點x座標存放處
        self.lowest_y = 0       #最低點y座標存放處
        self.start_count = 0
        self.end_count = 0
        self.all_time = 0
        self.step = 'start'
        self.wait_point = 0

    def main(self):
        find = FindTarget()
        if send.is_start:       #啟動電源與擺頭
            if self.step == 'start':
                send.sendHeadMotor(2, HEAD_CHECK, 80)
                time.sleep(0.05)
                send.sendHeadMotor(2, VERTICAL_HEAD, 80)
                time.sleep(0.7)
                self.step = 'find_lowest' 
            if self.step == 'find_lowest':#比較每個點後取代最低點並更新最低點
                find.find_target()
                if (self.lowest_y <= find.red_color_y):
                    self.lowest_x = find.red_color_x
                    self.lowest_y = find.red_color_y
                    rospy.loginfo(f'LOWEST_X : {self.lowest_x}, LOWEST_Y : {self.lowest_y}')
                    self.wait_point = self.wait_point + 1 
                elif abs(self.lowest_y - find.red_color_y) <= 1 and abs(self.lowest_x - find.red_color_x) <= 3  and self.wait_point > 20:
                    self.start_count = time.time() 
                    rospy.logwarn(f'LOWEST_X : {find.red_color_x} , LOWEST_Y : {find.red_color_y}')
                    rospy.logwarn(f'START: {self.start_count}')
                    time.sleep(1)
                    self.step = 'count'

            if self.step == 'count':
                find.find_target()
                rospy.logwarn(f'LOWEST_Y: {find.red_color_y}')
                rospy.logwarn(f'LOWEST_X: {find.red_color_x}')
                if abs( self.lowest_y - find.red_color_y ) <= 2 and abs( self.lowest_x - find.red_color_x ) <= 2:
                    self.end_count = time.time()
                    rospy.logwarn(f'END: {self.end_count}')
                    self.step = 'move_shoot'

            if self.step == 'move_shoot':
                self.all_time = self.end_count - self.start_count
                rospy.loginfo(f'All_time: {self.all_time}')
                self.x_diff = self.lowest_x - X_BENCHMARK               #計算目標點與瞄準點的差距(瞄準點是[172,152]) 改大射左
                self.y_diff = self.lowest_y - Y_BENCHMARK               #改大射高
                self.waist_move = round(self.x_diff / X_MOTOR_SCALE)    #將x與y的差距變成是接近馬達的刻度
                self.hand_move = round(self.y_diff / Y_MOTOR_SCALE)
                rospy.loginfo(f'Waist_move: {self.waist_move} , Hand_move: {self.hand_move}')
                rospy.loginfo(f'x_diff: {self.x_diff}')
                if self.waist_move > 0:                                 #當x_diff 的值是正的，就正常向右轉
                        for x in range (0, self.waist_move):
                            send.sendBodySector(3)
                            self.turn_right = self.turn_right + 1
                            time.sleep(0.1)
                        self.waist_move = 0
                elif self.waist_move < 0:                               #當x_diff 的值是負的，得先將x_diff變成正的，再用迴圈向左轉
                        self.waist_move = self.waist_move * (-1) - LEFT_WAIST_FIX
                        for x in range (0, self.waist_move):
                            send.sendBodySector(4)
                            self.turn_left = self.turn_left + 1
                            time.sleep(0.1)
                        self.waist_move = 0
                if self.hand_move > 0:                                  #當y_diff 的值是正的，就正常機體向下
                        for y in range (0, self.hand_move):
                            send.sendBodySector(5)
                            self.down = self.down + 1
                            time.sleep(0.1)
                        self.hand_move = 0
                elif self.hand_move < 0:                                #當y_diff 的值是負的，得先將y_diff變成正的，再用迴圈向上
                        self.hand_move = self.hand_move * (-1)
                        for y in range (0, self.hand_move):
                            send.sendBodySector(6)
                            send.sendBodySector(11)
                            send.sendBodySector(16)
                            self.up = self.up + 1
                            time.sleep(0.1)
                        self.hand_move = 0

                self.move_time = ((self.turn_right + self.turn_left + self.up + self.down) * 0.1) + SHOOT_FLOW_WAIT
                rospy.loginfo(f'Move_time: {self.move_time}')

                if self.all_time < 4: 
                    self.wait_time = (self.all_time * 2) - self.move_time 
                    time.sleep(self.wait_time)
                else:
                    self.wait_time = self.all_time - self.move_time
                    time.sleep(self.wait_time)
                    
                send.sendBodySector(87)
                self.loop = 1
                self.circulate = 1
                self.step = 'End'

            if self.step == 'End':
                rospy.loginfo(f'向右: {self.turn_right}, 向左: {self.turn_left}, 向上: {self.up}, 向下: {self.down}')
                rospy.loginfo(f'最低點: {self.lowest_x}, {self.lowest_y}')
                time.sleep(5)

        if not send.is_start:
            #find.find_target()
            #rospy.loginfo(f'final_point:{find.red_color_x} ,{find.red_color_y} ')
            if self.stand == 0:
                #send.sendBodySector(10)
                time.sleep(0.5)
                send.sendHeadMotor(1, HORIZON_HEAD, 80)
                time.sleep(0.5)
                send.sendHeadMotor(1, HORIZON_HEAD, 80)
                time.sleep(0.5)
                send.sendBodySector(7)
                time.sleep(1)
                send.sendBodySector(8)
                time.sleep(1)
                rospy.loginfo("lkj is idiot")
                self.stand = 1
                rospy.loginfo(f'final_point:{find.red_color_x} ,{find.red_color_y} ')
            if self.loop == 1 and self.circulate == 1:
                if self.turn_right > 0:
                    for x in range (0, self.turn_right ):
                        send.sendBodySector(13)
                        time.sleep(0.25)
                    self.turn_right = 0
                if self.turn_left > 0:
                    for x in range (0, self.turn_left ):
                        send.sendBodySector(14)
                    time.sleep(0.25)
                    self.turn_left = 0
                if self.down > 0:
                    for y in range (0, self.down ):
                        send.sendBodySector(19)
                    time.sleep(0.25)
                    self.down = 0
                if self.up > 0:
                    for y in range (0, self.up ):
                        send.sendBodySector(20)
                        send.sendBodySector(17)
                        send.sendBodySector(15)
                    time.sleep(0.2)
                    self.up = 0
                time.sleep(1)
                send.sendBodySector(12)
                time.sleep(0.5)
                self.loop = 0
                self.lowest_x = 320#最低點x座標存放處
                self.lowest_y = 0#最低點y座標存放處
                self.wait_point = 0
                self.step = 'start'

if __name__ == '__main__':
    try:
        strategy = FindMoveShoot()
        r =rospy.Rate(20)
        while not rospy.is_shutdown():#劃出起始十字
            send.drawImageFunction(4, 0, 0, 320, 120, 120, 0, 0, 0)
            send.drawImageFunction(5, 0, 160, 160, 0, 240, 0, 0, 0)
            strategy.main()
    except rospy.ROSInterruptException:
        pass

#sendBodySector(3) 向右轉
#sendBodySector(4) 向左轉
#sendBodySector(5) 向下轉
#sendBodySector(6) 向上轉
#sendBodySector(7) 舉手
#sendBodySector(8) 右手內凹
#sendBodySector(9) 左手手爪轉動90度
#sendBodySector(10) 

