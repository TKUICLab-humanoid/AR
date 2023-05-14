#!/usr/bin/env python
#coding=utf-8
import rospy
import numpy as np
from Python_API import Sendmessage
import time
import timeit
import math
#X Y 基準點  PS:想要射越右邊、越下面值要加大
#sendBodySector(3) 向右轉
#sendBodySector(4) 向左轉
#sendBodySector(5) 向下轉
#sendBodySector(6) 向上轉
#sendBodySector(7) 舉手
#sendBodySector(8) 右手內凹
#sendBodySector(9) 左手手爪轉動90度
#sendBodySector(10)
class FindTarget:
    def __init__(self) :
        self.bcolor_xmin = 0
        self.bcolor_xmax = 0
        self.bcolor_ymin = 0
        self.bcolor_ymax = 0
        self.ycolor_xmin = 0
        self.ycolor_xmax = 0
        self.ycolor_ymin = 0
        self.ycolor_ymax = 0
        self.rcolor_xmin = 0
        self.rcolor_xmax = 0
        self.rcolor_ymin = 0
        self.rcolor_ymax = 0
        self.RCOLOR_X = 0
        self.RCOLOR_Y = 0
        
    def Find_Target(self):
        for j in range (send.color_mask_subject_cnts[2]):
            for k in range (send.color_mask_subject_cnts[1]):
                for m in range (send.color_mask_subject_cnts[5]):
                    if -5 <= send.color_mask_subject_X[2][j] - send.color_mask_subject_X[1][k] < 5 and \
                        -5 <= send.color_mask_subject_Y[2][j] - send.color_mask_subject_Y[1][k] <= 5:
                        if -5 <= send.color_mask_subject_X[1][k] - send.color_mask_subject_X[5][m] <= 5 and \
                            -5 <= send.color_mask_subject_Y[1][k] - send.color_mask_subject_Y[5][m] <= 5 :
                            self.bcolor_xmin = send.color_mask_subject_XMin[2][j]
                            self.bcolor_xmax = send.color_mask_subject_XMax[2][j]
                            self.bcolor_ymin = send.color_mask_subject_YMin[2][j]
                            self.bcolor_ymax = send.color_mask_subject_YMax[2][j]
                            self.ycolor_xmin = send.color_mask_subject_XMin[1][k]
                            self.ycolor_xmax = send.color_mask_subject_XMax[1][k]
                            self.ycolor_ymin = send.color_mask_subject_YMin[1][k]
                            self.ycolor_ymax = send.color_mask_subject_YMax[1][k] 
                            self.rcolor_xmin = send.color_mask_subject_XMin[5][m]
                            self.rcolor_xmax = send.color_mask_subject_XMax[5][m]
                            self.rcolor_ymin = send.color_mask_subject_YMin[5][m]
                            self.rcolor_ymax = send.color_mask_subject_YMax[5][m]
                            self.RCOLOR_X = send.color_mask_subject_X[5][m]
                            self.RCOLOR_Y = send.color_mask_subject_Y[5][m]
                            
                            send.drawImageFunction(2, 1, self.rcolor_xmin, self.rcolor_xmax, self.rcolor_ymin, self.rcolor_ymax, 0, 0, 255)
                                    #print(rcolor_x,rcolor_yY) 

class FindMoveShoot:
    def __init__(self) :
        self.move = 0 #要動多少
        self.turn_right = 0 #向右的次數
        self.turn_left = 0 #向左的次數
        self.down = 0 #向下的次數
        self.up = 0 #向上的次數
        self.circulate = 0 #用於迴圈
        self.loop = 0 #用於迴圈
        self.time_find_point = 0#所有的點與沒點加起來的總時間
        self.move_time = 0#做完所有動作需要的時間
        self.stand = 0#用於啟動起始站姿
        self.FIXED_TARGET_WAIT = 0 #固定靶時間補償
        self.waist_move = 0
        self.hand_move = 0
        self.wait_time = 0
        self.LOWEST_X = 320#最低點x座標存放處
        self.LOWEST_Y = 0#最低點y座標存放處
        self.start_count = 0
        self.end_count = 0
        self.all_time = 0
        self.flag = 'round'
        self.j = 0
    def Find_Move_Shoot(self):
        Find = FindTarget()
        if send.is_start:#啟動電源與擺頭
            Find.Find_Target() 
        #======================================================

            while self.flag == 'round' :#比較每個點後取代最低點並更新最低點
                Find.Find_Target()
                if (self.LOWEST_Y <= Find.RCOLOR_Y) :
                    self.LOWEST_X = Find.RCOLOR_X
                    self.LOWEST_Y = Find.RCOLOR_Y
                    rospy.loginfo(f'LOWEST_Y:{self.LOWEST_Y}')
                    rospy.loginfo(f'LOWEST_X:{self.LOWEST_X}')
                    self.j = self.j + 1 
                elif abs(self.LOWEST_Y - Find.RCOLOR_Y) <= 2 and abs(self.LOWEST_X - Find.RCOLOR_X) <= 2 and self.j > 10 :
                    self.start_count = time.time() 
                    rospy.logwarn(f'LOWEST_Y:{Find.RCOLOR_Y}')
                    rospy.logwarn(f'LOWEST_X:{Find.RCOLOR_X}')
                    rospy.logwarn(f'START:{self.start_count}')
                    time.sleep(1)
                    self.flag = 'round2'

            if self.flag == 'round2' :
                Find.Find_Target()
                rospy.logwarn(f'LOWEST_Y:{Find.RCOLOR_Y}')
                rospy.logwarn(f'LOWEST_X:{Find.RCOLOR_X}')
                if abs(self.LOWEST_Y - Find.RCOLOR_Y) <= 1 and abs(self.LOWEST_X - Find.RCOLOR_X) <= 1 :
                    self.end_count = time.time()
                    rospy.logwarn(f'END:{self.end_count}')
                    self.flag = 'round3'

        #======================================================
            if self.flag == 'round3' :
                self.all_time = self.end_count - self.start_count
                rospy.loginfo(f'all_time{self.all_time}')
                self.x_diff = self.LOWEST_X - 166 #計算目標點與瞄準點的差距(瞄準點是[172,152]) 改大射左
                self.y_diff = self.LOWEST_Y - 153 #改大射高
                self.waist_move = round(self.x_diff / 4.6)#將x與y的差距變成是接近馬達的刻度
                self.hand_move = round(self.y_diff / 1.4)
                rospy.loginfo(f'{self.waist_move} , {self.hand_move}')
                rospy.loginfo(f'{self.x_diff}')
                if self.waist_move > 0:#當x_diff 的值是正的，就正常向右轉
                        for self.move in range (0 , self.waist_move):
                            send.sendBodySector(3)
                            self.turn_right = self.turn_right + 1
                            time.sleep(0.1)
                        self.waist_move = 0
                elif self.waist_move < 0:#當x_diff 的值是負的，得先將x_diff變成正的，再用迴圈向左轉
                        self.waist_move = self.waist_move * (-1) - 2
                        for self.move in range (0,self.waist_move):
                            send.sendBodySector(4)
                            self.turn_left= self.turn_left + 1
                            time.sleep(0.1)
                        self.waist_move=0
                if self.hand_move > 0:#當y_diff 的值是正的，就正常機體向下
                        for self.move in range (0,self.hand_move):
                            send.sendBodySector(5)
                            self.down = self.down + 1
                            time.sleep(0.1)
                        self.hand_move = 0
                elif self.hand_move < 0:#當y_diff 的值是負的，得先將y_diff變成正的，再用迴圈向上
                        self.hand_move = self.hand_move*(-1)
                        for self.move in range (0,self.hand_move):
                            send.sendBodySector(6)
                            send.sendBodySector(11)
                            send.sendBodySector(16)
                            self.up = self.up + 1
                            time.sleep(0.1)
                        self.hand_move = 0

                self.move_time = ((self.turn_right + self.turn_left + self.up + self.down) * 0.1) + 1.4
                rospy.loginfo(f'move_time{self.move_time}')

                if self.all_time < 3 : 
                    self.wait_time = (self.all_time * 2) - self.move_time 
                    time.sleep(self.wait_time)
                else :
                    self.wait_time = self.all_time - self.move_time
                    time.sleep(self.wait_time)
                    
                send.sendBodySector(87)
                self.loop = 1
                self.circulate = 1
                self.flag = 'round4'
            if self.flag == 'round4' :
                rospy.loginfo(f'向右{self.turn_right},向左{self.turn_left},向上{self.up},向下{self.down}')
                rospy.loginfo(f'最低點{self.LOWEST_X},{self.LOWEST_Y}')
                time.sleep(5)

        if not send.is_start:
            #Find.Find_Target()
            #rospy.loginfo(f'final_point:{Find.RCOLOR_X} ,{Find.RCOLOR_Y} ')
             if self.stand == 0:
                #send.sendBodySector(10)
                time.sleep(0.5)
                send.sendHeadMotor(1,2912,80)
                time.sleep(0.5)
                send.sendHeadMotor(1,2912,80)
                time.sleep(0.5)
                send.sendBodySector(7)
                time.sleep(2)
                send.sendBodySector(8)
                time.sleep(2)
                rospy.loginfo("lkj is idiot")
                self.stand = 1
                #rospy.loginfo(f'final_point:{Find.RCOLOR_X} ,{Find.RCOLOR_Y} ')
            # if self.loop == 1 and self.circulate == 1:
            #     if self.turn_right > 0:
            #         for self.move in range ( 0 , self.turn_right ):
            #             send.sendBodySector(13)
            #             time.sleep(0.25)
            #         self.turn_right = 0
            #     if self.turn_left > 0:
            #         for self.move in range ( 0 , self.turn_left ):
            #             send.sendBodySector(14)
            #         time.sleep(0.25)
            #         self.turn_left = 0
            #     if self.down > 0:
            #         for self.move in range ( 0 , self.down ):
            #             send.sendBodySector(19)
            #         time.sleep(0.25)
            #         self.down = 0
            #     if self.up > 0:
            #         for self.move in range ( 0 , self.up ):
            #             send.sendBodySector(20)
            #             send.sendBodySector(17)
            #             send.sendBodySector(15)
            #         time.sleep(0.2)
            #         self.up = 0
            #     time.sleep(1)
            #     send.sendBodySector(12)
            #     time.sleep(0.5)
            #     self.loop = 0
            #     self.FIXED_TARGET_WAIT = 0
            #     self.LOWEST_X = 0#最低點x座標存放處
            #     self.LOWEST_Y = 0#最低點y座標存放處

if __name__ == '__main__':
    try:
        send = Sendmessage()
        strategy = FindMoveShoot()
        r =rospy.Rate(20)
        while not rospy.is_shutdown():#劃出起始十字
            send.drawImageFunction(4,0,0,320,120,120,0,0,0)
            send.drawImageFunction(5,0,160,160,0,240,0,0,0)
            strategy.Find_Move_Shoot()
    except rospy.ROSInterruptException:
        pass
