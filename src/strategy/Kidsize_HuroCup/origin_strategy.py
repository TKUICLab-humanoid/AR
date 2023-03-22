#!/usr/bin/env python
#coding=utf-8
import rospy
import numpy as np
from Python_API import Sendmessage
import time
import timeit
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
HH = True
#============================================================================
#找靶子中心
#============================================================================
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
                #確保真的是靶子
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
 
    return rcolor_X,rcolor_Y

#============================================================================
#找紅色圓圈的最低點
#============================================================================
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
                            time.sleep(0.27) #修改
                                  
    return X_low ,Y_low

def all():
    Find_Target()
    #time.sleep(0.4)
    Low_xy(5)

imagedata = [[None for H in range(240)]for W in range(320)]

#=============================================================================
#用於移動靶算周期
#=============================================================================

def TS_time(i):
    global start
    global end
    global k 
    a = 0
    s = Low_xy(i)

    if  -11 <= s[0]-Find_Target()[0] <= 11 and -11 <= s[1]-Find_Target()[1] <= 11 and k == 0 :
        print("\n開始計時\n")         
        start =time.time()
        # time.sleep(2)
        k = 1
        
    if -11 <= s[0]-Find_Target()[0] <= 11 and -11 <= s[1]-Find_Target()[1] <= 11 and k == 1 :
        end = time.time()
 
    return start,end

if __name__ == '__main__':
    try:
        send = Sendmessage()
        waist = 0 #m
        mi = 0
        startM = 0
        endM = 0
        g = 0
        h = 0
        i = 0
        d_cnt = 0
        up_cnt = 0
        k = 0
        down = 0 #hl
        up = 0 #hhl
        back = 0 #lll
        hll = 0
        hlll = 0
        rh = 0
        rlh = 0
        rr = 0
        rrl = 0
        endd = 0
        lowy = 0
        DIO = True
        while not rospy.is_shutdown():
            send.drawImageFunction(4,0,0,320,120,120,0,0,0)
            send.drawImageFunction(5,0,160,160,0,240,0,0,0)
            
            if send.is_start == True :
                
                if HH == True:
                    time.sleep(0.5)
##頭部
                    send.sendHeadMotor(1,3048,80)
                    send.sendHeadMotor(1,3048,80)
                    time.sleep(3)
                    HH = False 

                all() 
                s = Low_xy(5)  
                
                if  -10 <= s[0]-Find_Target()[0] <= 10 and endd == 0  :

                    all()   
                    print('\nX軸差距 = ============',Low_xy(5)[0] - 257)  
                    print('\nY軸差距 = ============',Low_xy(5)[1] - 120) 

#========================================================================
#開始變動x軸
#========================================================================

                    if Low_xy(5)[0] - 257 > 10 or 257- Low_xy(5)[0]>10: #and  Low_xy(5)[1]>120:
                        waist = 257 - Low_xy(5)[0] 
                        mi = waist + mi
   
                        send.sendSingleMotor(9,int(waist*1.5),15)
                        time.sleep(3) 
                        X_low = 0
                        Y_low = 0 

                    print("現在Y值： ===============",Low_xy(5)[1])
#========================================================================
#開始變動y軸
#========================================================================

                    lowy = 125              #紅色圓最低點高低改這裡 

                    if hlll == 0:
                        if -10<= Low_xy(5)[0] - 257 <= 10:
                            if Low_xy(5)[1] >lowy :
                                print("dddddoooooowwwwwnnnn")
                                down =Low_xy(5)[1] - lowy
                                d_cnt = int(down/2)
#現在y差比較多的時候，調整手部馬達
                                if down >= 0:         
                                    down = int(down/4)
                                    print(down)
                                    print(d_cnt)

#手太高，調整手部馬達向下 
                                    for hll in range(0,down) :
                                        send.sendBodySector(38)
                                        print("\n現在的手太gao了，手部馬達需要向xia調整\n")
                                        #print("hand high")
                                        down = down+ 1
                                        rh = rh +1
                                        time.sleep(0.5)
#現在y差不多的時候，調整腿部馬達
                                for hll in range(0,d_cnt) :
                                    send.sendBodySector(36)
                                    print("\ny軸還有小小的偏差，所以向xia調整腿部馬達\n")
                                    time.sleep(1)
                                    #print("HIGH")
                                    rlh = rlh +1
                                    hll = hll+ 1
                                X_low = 0
                                Y_low = 0 
                                i = 0
                                hlll = hlll+1
#比賽在練習的上面所以腿部馬達向上
                            if Low_xy(5)[1] <lowy :
                                print("uuuuuuuuppppppppp")
                                up = lowy - Low_xy(5)[1]
                                up_cnt = int(up/2)
                                if up_cnt >= 5 :
                                    jin = int(up_cnt/5)
                                    jin = jin - 1
                                    for ji in range(0,jin):
                                        print("123456789 = ",jin)
                                        send.sendBodySector(66)
                                        time.sleep(1)
                                        up_cnt = up_cnt - 5
                                        up = up - 2
                                        print("dddddddddddddddddddddddddddddddddd",up_cnt)
                                
#現在y差比較多的時候，調整手部馬達
                                if up >= 0:         
                                    up = int(up/4)
                                    print(up)
                                    print(up_cnt)
                                    
#手太高，調整手部馬達向下 
                                    for hll in range(0,up) :
                                        send.sendBodySector(39)
                                        print("\n現在的手太di了，手部馬達需要向shang調整y軸\n")
                                        #print("hand high")
                                        hll = hll+ 1
                                        rh = rh +1
                                        time.sleep(0.5)
#現在y差不多的時候，調整腿部馬達
                                if up_cnt >= 0:
                                    #up_cnt = int(up_cnt/1.5)
                                    for hll in range(0,up_cnt) :
                                        send.sendBodySector(37)
                                        print("\ny軸還有小小的偏差，所以向shang調整腿部馬達\n")
                                        time.sleep(1)
                                        #print("HIGH")
                                        rlh = rlh +1
                                        hll = hll+ 1
                                X_low = 0
                                Y_low = 0 
                                i = 0
                                hlll = hlll+1
				                
#===================================================================================                            
#已經找到目標
#===================================================================================
                    if -10<= Low_xy(5)[0] - 257 <= 10:# and -10 <= Low_xy(5)[1] -162 <= 10 :  
#再次確保
                        print("\ntime start\n")
                        
                        all()
                        TS_time(5)
                        endM = TS_time(5)[1]
                        startM = TS_time(5)[0]                          
                        if endM -startM >= 0 and y == True:             
#結束時間大於開始時間（一定會成立再次確保）
                            y = False     
                        all()
                        if -10 <= Low_xy(5)[0] - 257 <= 10  and z== True:#and Low_xy(5)[1]>120
                            l =  Low_xy(5)  
                            z = False  
                        
                        if y==False and z== False:                        
#一定要執行前面兩條
                            print("\n測量時間：%f 秒" % (endM -startM ))
                            g = endM - startM
                            
                            print("\n新的最低點XY是：",l)
                            print("\n轉腰的數值是：",waist)

                            if g >= 1.42:   
                                h = g - 1.42
                            if g < 1.42:
                                h = g*2 -1.42    #數值加大 箭矢往右邊
                            print(h)
                            start = end
                            
                            print(h)
                            v = False
                            y = True
                            z = True
                            
                            # if h <= 0:
                            #     h = 1  
                            all()
                            time.sleep(1.5)
                            if -10<= Low_xy(5)[0] - 257 <= 10 and h != 0 and endd == 0:
                                print(h)
                                    
                                #time.sleep(h)
                                print("射擊")
                                print('up = %d',up)
                                print('down = %d',down)
#執行調整腰部馬達
                                # if send.DIOValue == 25:
                                #     ## send.sendBodySector(10)
                                #     # time.sleep(2)

                                #     #####send.sendSingleMotor(9,int(-hhll),10)
                                #     print("\n腰部馬達向左轉\n")
                                #     time.sleep(2)
                                #     #####send.sendSingleMotor(9,int(-hl),10)
                                #     print("\n腰部馬達再向左轉\n")
                                #     print("\n轉了：", int(-hhll*0.45))
                                #     time.sleep(5)
                                #     DIO = True
#調整手部馬達進行拉弓
                                send.sendBodySector(32) #微轉腰
                                time.sleep(3.5)
                                send.sendBodySector(33)      
                                print("\n手部所有馬達做出拉弓的動作\n")
                                time.sleep(2)
                                print("\naaaaaaaaaaaaaaaaaaaaa\n")
                                back = 1
                                endd = 1
                                print ("\n總轉腰數值 ：",mi)
                                
                            

            if send.is_start == False : 
                print("\nHHHHHHHH\n")
                if back == 1:
                    print("\n腰部馬達歸位\n")
                    #####send.sendHeadMotor(1,2048,40)
                    print("\n頭部馬達歸位\n")
                    time.sleep(2)
                    #####send.sendBodySector(2)
                    print("\n手部的拉弓動作歸位\n")
                    time.sleep(1)
                    for rr in range(0,rlh) :
                        #####send.sendBodySector(5)
                        print("\n腿部馬達向上調整\n")
                        time.sleep(1)
                        
                        rr = rr +1
                    time.sleep(2)

                    for rrl in range(0,rh) :
                        #####send.sendBodySector(8)
                        print("\n調整手部馬達的y軸，使其歸位\n")
                        time.sleep(0.5)
                        
                        rrl = rrl +1

                    time.sleep(2)
                    if DIO == True:
                        #####send.sendSingleMotor(9,int(hhll),15)
                        print("\n腰部馬達向右轉\n")
                        #####send.sendSingleMotor(9,int(hl),10)
                        print("\n腰部馬達向右轉完，歸位\n")
                        DIO = False
                    back = 0 
    except rospy.ROSInterruptException:
        pass

