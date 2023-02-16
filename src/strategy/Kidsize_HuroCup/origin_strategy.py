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

#sendBodySector(3) 向右轉
#sendBodySector(4) 向左轉
#sendBodySector(5) 向下轉
#sendBodySector(6) 向上轉
#sendBodySector(7) 舉手
#sendBodySector(8) 右手內凹
#sendBodySector(9) 左手手爪轉動90度
#sendBodySector(10)
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

if __name__ == '__main__':
    try:
        send = Sendmessage()
        point_x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#全部點的x座標
        point_y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#全部點的y座標
        i=0#實際有數值的點個數
        j=0#計算目前總共紀錄了幾個點
        k=0#no_point在預設區間出現的個數
        x=0#要動多少
        y=0#向右的次數
        z=0#向左的次數
        t=0#向上的次數
        s=0#向右的次數
        w=0#用於迴圈
        f=0
        x_diff=0#計算瞄準點與目標點的x差距
        y_diff=0#計算瞄準點與目標點的y差距
        time1=0
        all_point=0
        stand=0
        waist_move=0
        hand_move=0
        target_point_x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#真正有值的點x座標存放處
        target_point_y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#真正有值的點y座標存放處
        while not rospy.is_shutdown():#劃出起始十字
            send.drawImageFunction(4,0,0,320,120,120,0,0,0)
            send.drawImageFunction(5,0,160,160,0,240,0,0,0)
            
            if send.is_start == True :#啟動電源與擺頭
                
                    while j<90 and i<20:
                        Find_Target()
                        if Find_Target()[0]!=0 or Find_Target()[1]!=0:#抓出每一個點，然後將實際的點放在另一個list裡
                            point_x[j]=Find_Target()[0]
                            point_y[j]=Find_Target()[1]
                            target_point_x[i]=point_x[j]
                            target_point_y[i]=point_y[j]
                            print(target_point_x[i],target_point_y[i])
                            i=i+1
                            j=j+1
                            if i>5 and -2<=target_point_x[0]-target_point_x[5]<=2 and -2<=target_point_y[0]-target_point_y[5]<=2:#快速判斷定靶
                                target_point_x[18]=target_point_x[5]
                                target_point_y[18]=target_point_y[5]
                                i=20
                            time.sleep(0.2)
                        if Find_Target()[0]==0 or Find_Target()[1]==0:#將空的點設置為零放在大LIST內
                            point_x[j]=0
                            point_y[j]=0
                            j=j+1
                            if 17>i>4:#計算起始點跟瞄準點中間有多少個沒點
                                if point_x[j]==0 or point_y[j]==0:
                                    k=k+1
                            print("沒點")
                            time.sleep(0.2)

                    while w==0:#持續追蹤靶
                        Find_Target()
                        time.sleep(0.25)
                        now_target=Find_Target()
                        if -15<now_target[0]-target_point_x[3]<15 and -15<now_target[1]-target_point_y[3]<15:#判斷通過基準點，我們設定是第4個點
                            print("i find you!")
                            print(k)
                            x_diff=target_point_x[18]-160#計算目標點與中心點的差距
                            y_diff=target_point_y[18]-160
                            waist_move=round(x_diff/5)#將x與y的差距變成是接近馬達的刻度
                            hand_move=round(y_diff/2)
                            print(waist_move,hand_move)
                            if waist_move>0:#當x_diff 的值是正的，就正常向右轉
                                for x in range (0,waist_move):
                                    send.sendBodySector(3)
                                    y=y+1
                                time.sleep(0.25)
                                waist_move=0
                            if waist_move<0:#當x_diff 的值是負的，得先將x_diff變成正的，再用迴圈向左轉
                                waist_move=waist_move*(-1)-1
                                for x in range (0,waist_move):
                                    send.sendBodySector(4)
                                    z=z+1
                                time.sleep(0.25)
                                waist_move=0
                            if hand_move>0:#當y_diff 的值是正的，就正常機體向下
                                for x in range (0,hand_move):
                                    send.sendBodySector(5)
                                    t=t+1
                                time.sleep(0.25)
                                hand_move=0
                            if hand_move<0:#當y_diff 的值是負的，得先將y_diff變成正的，再用迴圈向上
                                hand_move=hand_move*(-1)
                                for x in range (0,hand_move):
                                    send.sendBodySector(6)
                                    send.sendBodySector(11)
                                    send.sendBodySector(16)
                                    s=s+1
                                time.sleep(0.25)
                                hand_move=0
                            all_point=15+k
                            time1=all_point*0.2
                            time.sleep(2)
                            send.sendBodySector(9)
                            time.sleep(2)
                            send.sendBodySector(10)
                            time.sleep(1)
                            print("向右",y,"向左",z,"向上",s,"向下",t)
                            w=1
                            f=1

            if send.is_start == False :
                if stand==0:
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
                    print("lkj is idiot")
                    stand=1
                if f==1 and w==1:
                    for x in range (0,y):
                        send.sendBodySector(13)
                        time.sleep(0.25)
                    y=0
                    for x in range (0,z):
                        send.sendBodySector(14)
                        time.sleep(0.25)
                    z=0
                    for x in range (0,t):
                        send.sendBodySector(6)
                        time.sleep(0.25)
                    t=0
                    for x in range (0,s):
                        send.sendBodySector(5)
                        send.sendBodySector(17)
                        send.sendBodySector(15)
                        time.sleep(0.1)
                    time.sleep(0.1)
                    send.sendBodySector(12)
                    s=0
                    time.sleep(0.5)
                    w=0
                    f=0
                    i=0
                    j=0
                    k=0

    except rospy.ROSInterruptException:
        pass
