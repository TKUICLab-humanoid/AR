#!/usr/bin/env python
#coding=utf-8
import rospy
import numpy as np
from Python_API import Sendmessage
import time
import timeit
import math
bcolor_XMin = 0
bcolor_XMax = 0
bcolor_YMin = 0
bcolor_YMax = 0
ycolor_XMin = 0
ycolor_XMax = 0
ycolor_YMin = 0
ycolor_YMax = 0
rcolor_XMin = 0
rcolor_XMax = 0
rcolor_YMin = 0
rcolor_YMax = 0
rcolor_X = 0
rcolor_Y = 0
start = 0
end = 0

Y_low = 0
X_low = 0
v = True
z = True
y = True
l = 0
tt = 0
power = True
#sendBodySector(1) 向右轉
#sendBodySector(2) 向左轉
#sendBodySector(3) 向下轉
#sendBodySector(4) 向上轉
def Find_Target():
    global bcolor_XMin 
    global bcolor_XMax 
    global bcolor_YMin 
    global bcolor_YMax 
    global ycolor_XMin 
    global ycolor_XMax 
    global ycolor_YMin 
    global ycolor_YMax 
    global rcolor_XMin 
    global rcolor_XMax 
    global rcolor_YMin 
    global rcolor_YMax 
    global rcolor_X 
    global rcolor_Y 
    for j in range (send.color_mask_subject_cnts[2]):
        for k in range (send.color_mask_subject_cnts[1]):
            for m in range (send.color_mask_subject_cnts[5]):
                if -2 <= send.color_mask_subject_X[2][j] - send.color_mask_subject_X[1][k] <=2 and -2 <= send.color_mask_subject_Y[2][j] - send.color_mask_subject_Y[1][k] <=2:
                    if -2 <= send.color_mask_subject_X[1][k] - send.color_mask_subject_X[5][m] <= 2 and  -2 <= send.color_mask_subject_Y[1][k] - send.color_mask_subject_Y[5][m] <= 2 :
                # if   send.color_mask_subject_Width[2][j] - send.color_mask_subject_Width[1][k]>0  and send.color_mask_subject_Height[2][j] - send.color_mask_subject_Height[1][k] >0 :
                #     if   send.color_mask_subject_Width[1][k] - send.color_mask_subject_Width[5][m] >0 and send.color_mask_subject_Height[1][k] -send.color_mask_subject_Height[5][m] >0 :
                        bcolor_XMin = send.color_mask_subject_XMin[2][j]
                        bcolor_XMax = send.color_mask_subject_XMax[2][j]
                        bcolor_YMin = send.color_mask_subject_YMin[2][j]
                        bcolor_YMax = send.color_mask_subject_YMax[2][j]
                        ycolor_XMin = send.color_mask_subject_XMin[1][k]
                        ycolor_XMax = send.color_mask_subject_XMax[1][k]
                        ycolor_YMin = send.color_mask_subject_YMin[1][k]
                        ycolor_YMax = send.color_mask_subject_YMax[1][k] 
                        rcolor_XMin = send.color_mask_subject_XMin[5][m]
                        rcolor_XMax = send.color_mask_subject_XMax[5][m]
                        rcolor_YMin = send.color_mask_subject_YMin[5][m]
                        rcolor_YMax = send.color_mask_subject_YMax[5][m]
                        rcolor_X = send.color_mask_subject_X[5][m]
                        rcolor_Y = send.color_mask_subject_Y[5][m]
                        # send.drawImageFunction(0,1,bcolor_XMin,bcolor_XMax,bcolor_YMin,bcolor_YMax,0,0,255)#  這邊有修改
                        # send.drawImageFunction(1,1,ycolor_XMin,ycolor_XMax,ycolor_YMin,ycolor_YMax,0,0,255)
                        send.drawImageFunction(2,1,rcolor_XMin,rcolor_XMax,rcolor_YMin,rcolor_YMax,0,0,255)
                                #print(rcolor_X,rcolor_Y) 
                else :
                    rcolor_Y=0
                    rcolor_X=0
    return rcolor_X,rcolor_Y
    
def Low_xy(i):
    global Y_low
    global X_low
    k = 3
    l_XMin =0
    l_XMax =0
    l_YMin =0
    l_YMax =0
    for f in range (send.color_mask_subject_cnts[2]):
        for g in range (send.color_mask_subject_cnts[1]):
            for h in range (send.color_mask_subject_cnts[5]):
                if -2 <= send.color_mask_subject_X[2][f] - send.color_mask_subject_X[1][g] <=2 and -2 <= send.color_mask_subject_Y[2][f] - send.color_mask_subject_Y[1][g] <=2:
                    if -2 <= send.color_mask_subject_X[1][g] - send.color_mask_subject_X[5][h] <= 2 and  -2 <= send.color_mask_subject_Y[1][g] - send.color_mask_subject_Y[5][h] <= 2 :
                # if   send.color_mask_subject_Width[2][f] - send.color_mask_subject_Width[1][g]>0  and send.color_mask_subject_Height[2][f] - send.color_mask_subject_Height[1][g] >0 :
                #     if   send.color_mask_subject_Width[1][g] - send.color_mask_subject_Width[5][h] >0 and send.color_mask_subject_Height[1][g] -send.color_mask_subject_Height[5][h] >0 :
                        l_XMin = send.color_mask_subject_XMin[5][h]
                        l_XMax = send.color_mask_subject_XMax[5][h]
                        l_YMin = send.color_mask_subject_YMin[5][h]
                        l_YMax = send.color_mask_subject_YMax[5][h]       
                        if send.color_mask_subject_Y[i][h] >= Y_low:
                            Y_low = send.color_mask_subject_Y[5][h]
                            X_low = send.color_mask_subject_X[5][h]
            # time.sleep(0.4)
                            send.drawImageFunction(3,1,l_XMin,l_XMax,l_YMin,l_YMax,255,48,48) 
                            time.sleep(0.27) #修改====================================================================================================================
                                  
    return X_low ,Y_low

imagedata = [[None for H in range(240)]for W in range(320)]

def TS_time(i):
    global start
    global end
    global k 
    a = 0
    s = Low_xy(i)

    if  -11 <= s[0]-Find_Target()[0] <= 11 and -11 <= s[1]-Find_Target()[1] <= 11 and k == 0 :
        print("開始計時")         
        start =time.time()
        # time.sleep(2)
        k = 1
        
    if -11 <= s[0]-Find_Target()[0] <= 11 and -11 <= s[1]-Find_Target()[1] <= 11 and k == 1 :
        end = time.time()
        

 
    return start,end

if __name__ == '__main__':
    try:
        send = Sendmessage()
        point_x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#全部點的x座標
        point_y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#全部點的y座標
        i=0#計數用
        j=0#計算目前總共紀錄了幾個點
        k=0#no_point在預設區間出現的個數
        x=0#要動多少
        y=0
        z=0
        w=0
        x_diff=0#計算瞄準點與目標點的x差距
        y_diff=0#計算瞄準點與目標點的y差距
        waist_move=0
        hand_move=0
        target_point_x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#真正有值的點x座標存放處
        target_point_y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#真正有值的點y座標存放處
        while not rospy.is_shutdown():#劃出起始十字
            send.drawImageFunction(4,0,0,320,120,120,0,0,0)
            send.drawImageFunction(5,0,160,160,0,240,0,0,0)
            
            if send.is_start == True :#啟動電源與擺頭
                
                if power == True:
                    time.sleep(0.5)
                    power = False

                
                    while j<90 and i<20:#抓出每一個點
                        Find_Target()
                        if Find_Target()[0]!=0 or Find_Target()[1]!=0:
                            point_x[j]=Find_Target()[0]
                            point_y[j]=Find_Target()[1]
                            i=i+1
                            j=j+1
                            time.sleep(0.25)
                        if Find_Target()[0]==0 or Find_Target()[1]==0:
                            point_x[j]=0
                            point_y[j]=0
                            j=j+1
                            time.sleep(0.25)

                    i=0
                    while i<90 and z<20:#將全部的點開始做過濾
                        if point_x[i]!=0 or point_y[i]!=0:
                            target_point_x[z]=point_x[i]
                            target_point_y[z]=point_y[i]
                            print(target_point_x[z],target_point_y[z])
                            z=z+1
                            i=i+1
                        elif point_x[i]==0 or point_y[i]==0:
                            print("沒點")
                            if 17>z>4:
                                if point_x[i]==0 or point_y[i]==0:
                                    k=k+1
                            i=i+1

                    print(k)
                    x_diff=target_point_x[16]-160#計算目標點與中心點的差距
                    y_diff=target_point_y[16]-162
                    waist_move=round(x_diff/9)
                    hand_move=round(y_diff/2)
                    print(waist_move,hand_move)
                    while w==0:#持續追蹤靶
                        Find_Target()
                        time.sleep(0.25)
                        now_target=Find_Target()
                        if -15<now_target[0]-target_point_x[3]<15 and -15<now_target[1]-target_point_y[3]<15:#判斷通過基準點，我們設定是第4個點
                            print("i find you!")
                            if waist_move>0:#當x_diff 的值是正的，就正常向右轉
                                for x in range (0,waist_move):
                                    send.sendBodySector(1)
                                    print("向右轉")
                                time.sleep(0.1)
                                waist_move=0
                            if waist_move<0:#當x_diff 的值是負的，得先將x_diff變成正的，再用迴圈向左轉
                                waist_move=waist_move*(-1)
                                for x in range (0,waist_move):
                                    send.sendBodySector(2)
                                    print("向左轉")
                                time.sleep(0.1)
                                waist_move=0
                            if hand_move>0:#當y_diff 的值是正的，就正常機體向下
                                for x in range (0,hand_move):
                                    send.sendBodySector(3)
                                    print("向下")
                                time.sleep(0.1)
                                hand_move=0
                            if hand_move<0:#當y_diff 的值是負的，得先將y_diff變成正的，再用迴圈向上
                                hand_move=hand_move*(-1)
                                for x in range (0,hand_move):
                                    send.sendBodySector(4)
                                    print("向上")
                                time.sleep(0.5)
                                hand_move=0


            if send.is_start == False :
                print("lkj is idiot")
    except rospy.ROSInterruptException:
        pass
