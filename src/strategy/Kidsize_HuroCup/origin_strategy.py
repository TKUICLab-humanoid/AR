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
k = 0
Y_low = 0
X_low = 0
NY_low = 0
NX_low = 0


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
                if   50 < send.color_mask_subject_Width[2][j] < 150 and 50 < send.color_mask_subject_Height[2][j] < 150 :
                    if  5 < send.color_mask_subject_Width[1][k] <90 and 5 < send.color_mask_subject_Height[1][k] < 90:
                        if  0 < send.color_mask_subject_Width[5][m]< 25 and 0 < send.color_mask_subject_Height[5][m] < 25:
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
                                send.drawImageFunction(0,1,bcolor_XMin,bcolor_XMax,bcolor_YMin,bcolor_YMax,0,0,255)
                                send.drawImageFunction(1,1,ycolor_XMin,ycolor_XMax,ycolor_YMin,ycolor_YMax,0,0,255)
            send.drawImageFunction(2,1,rcolor_XMin,rcolor_XMax,rcolor_YMin,rcolor_YMax,0,0,255)
               
 

    return rcolor_X,rcolor_Y
    
def Low_xy(i):
    global Y_low
    global X_low
    k = 3
    l_XMin =0
    l_XMax =0
    l_YMin =0
    l_YMax =0
    for j in range (send.color_mask_subject_cnts[i]):
        if 0 < send.color_mask_subject_Width[i][j]< 25 and 0 < send.color_mask_subject_Height[i][j] < 25:
            l_XMin = send.color_mask_subject_XMin[i][j]
            l_XMax = send.color_mask_subject_XMax[i][j]
            l_YMin = send.color_mask_subject_YMin[i][j]
            l_YMax = send.color_mask_subject_YMax[i][j]
        
            if send.color_mask_subject_Y[i][j] >= Y_low:
                Y_low = send.color_mask_subject_Y[i][j]
                X_low = send.color_mask_subject_X[i][j]
                time.sleep(0.4)
                send.drawImageFunction(3,1,l_XMin,l_XMax,l_YMin,l_YMax,255,48,48)    
    return X_low ,Y_low



def all():
    Find_Target()
    Low_xy(5)


# def TS_time(i):
#     global start
#     global end
#     global k 
#     a = 0
#     s = Low_xy(i)
#     if  Find_Target()[1] == s[1] and k ==0 :
                    
#         start =time.time()
#         time.sleep(1)
#         k = 1
#     if  Find_Target()[1] == s[1] and k ==1 :
#         end = time.time()

#     print(start,end)
        
#     return start,end

    
def NLow_xy(i):
    global NX_low
    global NY_low 

   
    Nl_XMin =0
    Nl_XMax =0
    Nl_YMin =0
    Nl_YMax =0
   
    for j in range (send.color_mask_subject_cnts[i]):
        if  0 < send.color_mask_subject_Width[i][j]< 30 and 0 < send.color_mask_subject_Height[i][j] < 30:
            Nl_XMin = send.color_mask_subject_XMin[i][j]
            Nl_XMax = send.color_mask_subject_XMax[i][j]
            Nl_YMin = send.color_mask_subject_YMin[i][j]
            Nl_YMax = send.color_mask_subject_YMax[i][j]
          
        
            if  send.color_mask_subject_Y[i][j] >= NY_low  :
                NY_low = send.color_mask_subject_Y[i][j]
                NX_low = send.color_mask_subject_X[i][j]
                time.sleep(0.4)
                send.drawImageFunction(6,1,Nl_XMin,Nl_XMax,Nl_YMin,Nl_YMax,0,100,0)    
    return NX_low ,NY_low 

def Nall():
    
    Find_Target()
    NLow_xy(5)

imagedata = [[None for H in range(240)]for W in range(320)]

def TS_time(i):
    global start
    global end
    global k 
    a = 0
    s = NLow_xy(i)

    if  -2<s[1]-Find_Target()[1]<2  and k ==0 :
                 
        start =time.time()
        time.sleep(2)
        k = 1
        
        

    if -5<s[1]-Find_Target()[1]<5  and k ==1 :
        end = time.time()
        
       
        


        
    return start,end
v = False
z = True
y = True

if __name__ == '__main__':
    try:
        send = Sendmessage()
        
        m = 0
        
        startM = 0
        endM = 0
        while not rospy.is_shutdown():
            send.drawImageFunction(4,0,0,320,120,120,0,0,0)
            send.drawImageFunction(5,0,160,160,0,240,0,0,0)
            
            if send.Web == True :
               
                all()
                    
                # Find_Target(3,5)
                s = Low_xy(5) 
                   
                   
                
                if  -3 <= s[1]-Find_Target()[1] <= 3 and -10 <= s[0]-Find_Target()[0] <= 10   :
                    all()
                    
                    NLow_xy(5)  
                        
                    if Low_xy(5)[0] - 160 > 10 or 160 - Low_xy(5)[0]>10 and v == False:
                        m = 160 - Low_xy(5)[0]            
                        send.sendSingleMotor(9,int(m*3),15)
                        
                        
                        time.sleep(5) 
                        X_low = 0
                        Y_low = 0
                        NX_low = 0
                        NY_low = 0
                        
                        
                    if -10< Low_xy(5)[0] - 160 < 10:
                        v = True
                        

                      
                
                    all()
                        
                     
                    if -5 <= NLow_xy(5)[0]- 160 <= 5:
                        TS_time(5)


                    endM = TS_time(5)[1]
                    startM = TS_time(5)[0]
         
                            
                    if endM -startM > 0 and y == True:
                            
                        y = False
                         
                    Find_Target()
                    NLow_xy(5)
                    if -5<= NLow_xy(5)[0] - 160 <= 5 and NLow_xy(5)[1]>120 and z== True:
                            
                        z = False
                       
                        
                    if y==False and z== False:
                        print("測量時間：%f 秒" % (endM -startM ))
                        print("\n新的最低點XY是：",NLow_xy(5))
                        break

    except rospy.ROSInterruptException:
        pass