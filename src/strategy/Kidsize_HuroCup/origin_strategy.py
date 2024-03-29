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

def all():
    Find_Target()
    #time.sleep(0.4)
    Low_xy(5)

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
        m = 0
        mi = 0
        msum = 0
        startM = 0
        endM = 0
        g = 0
        h = 0
        i = 0
        hh = 0
        hhll = 0
        r = rospy.Rate(5)
        k = 0
        hl = 0
        lll =0
        hll = 0
        hlll = 0
        rh = 0
        rlh = 0
        rll = 0
        rr = 0
        rrl = 0
        rrll = 0
        endd = 0
        lowy = 0
        hlltr = True
        DIO = True
        while not rospy.is_shutdown():
            send.drawImageFunction(4,0,0,320,120,120,0,0,0)
            send.drawImageFunction(5,0,160,160,0,240,0,0,0)
            
            if send.is_start == True :
                
                if HH == True:
                    time.sleep(0.5)
                    send.sendHeadMotor(1,2812,80)
                    send.sendHeadMotor(1,2812,80)
                    # send.sendSingleMotor(9,10,15) #啟動轉腰
                    time.sleep(3)
                    HH = False 

                all() 
                s = Low_xy(5)  
                
                if  -10 <= s[0]-Find_Target()[0] <= 10 and endd == 0  :

                    all()   
                    print('X軸差距 = ============',Low_xy(5)[0] - 160)  
                    print('Y軸差距 = ============',Low_xy(5)[1] - 120) 
                    
                    if Low_xy(5)[0] - 160 > 1 or 160 - Low_xy(5)[0]>1: #and  Low_xy(5)[1]>120:
                        m = 160 - Low_xy(5)[0] 
                        mi = m*3 
                        msum = msum + mi
                        print(msum)
                        if msum > 800 or msum < -800:
                            print("暴轉========================================================================================================================================================")
                            time.sleep(2)
                            send.sendSingleMotor(9,int(-800),10)
                            Low_xy(5)
                            Find_Target()
                            msum = 0
                            time.sleep(5)


   
                        
                        
                         
                        send.sendSingleMotor(9,int(m*3),15)
                        time.sleep(3) 
                        X_low = 0
                        Y_low = 0 

                    print("現在Y值： ===============",Low_xy(5)[1])


 
                    lowy = 141                   #最低點高低改這裡
                    if hlll == 0:
                        if -1<= Low_xy(5)[0] - 160 <= 1:
                            if Low_xy(5)[1] > lowy:           #改151
                                hl = Low_xy(5)[1] - lowy
                                
                                print(hl)
                                if hl >= 13:
                                    hl = 13
                                hhll = hhll - hl 
                                if hll < hl and hlltr == True: 
                                    for hll in range(0,hl) :
                                        send.sendBodySector(5)
                                        time.sleep(1)
                                        print("LOW")
                                        hll = hll+ 1
                                        rll = rll+1
                                        if hll == 13 :
                                            hlltr = False



                                
                                    # for hll in range(0,hhll) :
                                    #     send.sendBodySector(10)
                                    #     print("hand LOW")
                                    #     hll = hll+ 1
                                    #     rh = rh +1
                                    #     time.sleep(0.5)

                                
                            
                                X_low = 0
                                Y_low = 0 
                                i = 0
                                hlll = hlll+1
                                

                        if -1<= Low_xy(5)[0] - 160 <= 1:
                            if Low_xy(5)[1] <lowy :
                                hl =lowy -  Low_xy(5)[1]
                                hhll = hl

                                print(hl)
                                if hl >= 3:
                                    hl = 3
                                    hhll = hhll - hl 
                                    for hll in range(0,hhll) :
                                        send.sendBodySector(7)
                                        print("hand high")
                                        hll = hll+ 1
                                        rh = rh +1
                                        time.sleep(0.5)

                                    
                                for hll in range(0,hl) :
                                    send.sendBodySector(4)
                                    time.sleep(1)
                                    print("HIGH")
                                    rlh = rlh +1
                                    hll = hll+ 1
                                X_low = 0
                                Y_low = 0 
                                i = 0
                                hlll = hlll+1
                            

                    
                    if -1<= Low_xy(5)[0] - 160 <= 1:# and -10 <= Low_xy(5)[1] -162 <= 10 :
                        print("time start")
                        
                        all()
                        TS_time(5)
                        endM = TS_time(5)[1]
                        startM = TS_time(5)[0]                          
                        if endM -startM >= 0 and y == True:       
                            y = False     
                        all()
                        if -10 <= Low_xy(5)[0] - 160 <= 10  and z== True:#and Low_xy(5)[1]>120
                            l =  Low_xy(5)  
                            z = False  
                        
                        if y==False and z== False:
                            print("\n測量時間：%f 秒" % (endM -startM ))
                            g = endM - startM
                            
                            print("\n新的最低點XY是：",l)
                            print("\n轉腰的數值是：",mi)

                            if g >= 1.42:   
                                h = g - 1.42
                            if g<1.42:
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
                            if -1 <= Low_xy(5)[0] - 160 <= 1 and h != 0 and endd == 0:
                                print(h)
                                    
                                #time.sleep(h)
                                print("射擊")
                                if send.DIOValue == 25:
                                    # send.sendBodySector(10)
                                    # time.sleep(2)

                                    send.sendSingleMotor(9,int(-hhll),10)
                                    send.sendSingleMotor(9,int(-hl),10)
                                    print("轉了：", int(-hhll*0.45))
                                    time.sleep(5)
                                    DIO = True
                                send.sendBodySector(3)
                                time.sleep(2)
                                print("aaaaaaaaaaaaaaaaaaaaa")
                                lll = 1
                                endd = 1
                                print ("總轉腰數值 ：",msum)
                                
                                #send.is_start = False
                            

            if send.is_start == False : 
                print("HHHHHHHH")
                if lll == 1:
                    send.sendSingleMotor(9,int(-1*msum),15)
                    send.sendHeadMotor(1,2048,40)
                    time.sleep(2)
                    send.sendBodySector(2)
                    time.sleep(1)
                    for rr in range(0,rlh) :
                        send.sendBodySector(5)
                        time.sleep(1)
                        
                        rr = rr +1
                    time.sleep(2)

                    for rrl in range(0,rh) :
                        send.sendBodySector(8)
                        time.sleep(0.5)
                        
                        rrl = rrl +1

                    time.sleep(2)
                    for rrll in range(0,rll) :
                        send.sendBodySector(4)
                        time.sleep(1)
                        
                        rrll = rrll +1
                    time.sleep(2)
                    if DIO == True:
                        send.sendSingleMotor(9,int(hhll),15)
                        send.sendSingleMotor(9,int(hl),10)
                        DIO = False
                    lll = 0

                

                        
                        # g = 0
                        # k = 0
                        # X_low = 0
                        # Y_low = 0
                        
                       # if g >= 3 :
                       #     send.sendBodySector(1) #動作串198 射擊   
            r.sleep()
    except rospy.ROSInterruptException:
        pass

#加上轉頭 完成
#修改不要直接跳出 完成
#轉腰的最大範圍 完成
# AR2022.ini motion
# 212:站姿
# 400:暫時測試(站平）

#初始：212->201->200->199->400
#9:蹲下 128:起
#198(射擊）:11->143->11->143->110->72->144
#198(new):11->11->110->72->144
#100:100 300夾
#m6:270 m2:-180

# 99 要修改




#左手往上-33 右手1次10
#3號馬達選轉6*2次
