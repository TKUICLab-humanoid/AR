#include "strategy/strategy_main.h"
void KidsizeStrategy::strategyclassify(){  //濾雜訊及存取正確目標物之資訊
    for(int Red_count = 0; Red_count < strategy_info->color_mask_subject_cnts[Target_red_color];Red_count++)
    {
        for(int Yellow_count = 0; Yellow_count < strategy_info->color_mask_subject_cnts[Target_yellow_color];Yellow_count++)
        {
            for(int Blue_count = 0; Blue_count < strategy_info->color_mask_subject_cnts[Target_blue_color];Blue_count++)
            {
                if(strategy_info->color_mask_subject[Target_red_color][Red_count].size >= 75)
                {
                    if(strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].size >= 1000)
                    {
                        if(strategy_info->color_mask_subject[Target_blue_color][Blue_count].size >= 2000)
                        {
                            if(strategy_info->color_mask_subject[Target_red_color][Red_count].XMin > strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].XMin)
                            {
                                if(strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].XMin > strategy_info->color_mask_subject[Target_blue_color][Blue_count].XMin)
                                {
                                    if(abs(strategy_info->color_mask_subject[Target_red_color][Red_count].XMin -
                                           strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].XMin) <= 80)
                                    {
                                        if(abs(strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].XMin -
                                                strategy_info->color_mask_subject[Target_blue_color][Blue_count].XMin) <= 60)
                                        {
                                            if(abs(strategy_info->color_mask_subject[Target_red_color][Red_count].Width -
                                                   strategy_info->color_mask_subject[Target_red_color][Red_count].Height) <=5)
                                            {
                                                if(strategy_info->color_mask_subject[Target_blue_color][Blue_count].YMin < strategy_info->color_mask_subject[Target_red_color][Red_count].YMin)
                                                {
                                                    classifyflag = true;
                                                    //red_Data
                                                    Archeryinfo->RedTarget.XMin = strategy_info->color_mask_subject[Target_red_color][Red_count].XMin ;
                                                    Archeryinfo->RedTarget.XMax = strategy_info->color_mask_subject[Target_red_color][Red_count].XMax ;
                                                    Archeryinfo->RedTarget.YMin = strategy_info->color_mask_subject[Target_red_color][Red_count].YMin;
                                                    Archeryinfo->RedTarget.YMax = strategy_info->color_mask_subject[Target_red_color][Red_count].YMax;
                                                    Archeryinfo->RedTarget.X    = strategy_info->color_mask_subject[Target_red_color][Red_count].X ;
                                                    Archeryinfo->RedTarget.Y    = strategy_info->color_mask_subject[Target_red_color][Red_count].Y ;
                                                    Archeryinfo->RedTarget.size  = strategy_info->color_mask_subject[Target_red_color][Red_count].size;
                                                    Archeryinfo->RedTarget.Width = strategy_info->color_mask_subject[Target_red_color][Red_count].Width;
                                                    Archeryinfo->RedTarget.Height = strategy_info->color_mask_subject[Target_red_color][Red_count].Height;
                                                    //yellow_Data
                                                    Archeryinfo->YellowTarget.XMin = strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].XMin ;
                                                    Archeryinfo->YellowTarget.XMax = strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].XMax ;
                                                    Archeryinfo->YellowTarget.YMin = strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].YMin;
                                                    Archeryinfo->YellowTarget.YMax = strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].YMax;
                                                    Archeryinfo->YellowTarget.X    = strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].X ;
                                                    Archeryinfo->YellowTarget.Y    = strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].Y ;
                                                    Archeryinfo->YellowTarget.size  = strategy_info->color_mask_subject[Target_yellow_color][Yellow_count].size;
                                                    //blue_Data
                                                    Archeryinfo->BlueTarget.XMin = strategy_info->color_mask_subject[Target_blue_color][Blue_count].XMin ;
                                                    Archeryinfo->BlueTarget.XMax = strategy_info->color_mask_subject[Target_blue_color][Blue_count].XMax ;
                                                    Archeryinfo->BlueTarget.YMin = strategy_info->color_mask_subject[Target_blue_color][Blue_count].YMin;
                                                    Archeryinfo->BlueTarget.YMax = strategy_info->color_mask_subject[Target_blue_color][Blue_count].YMax;
                                                    Archeryinfo->BlueTarget.X    = strategy_info->color_mask_subject[Target_blue_color][Blue_count].X ;
                                                    Archeryinfo->BlueTarget.Y    = strategy_info->color_mask_subject[Target_blue_color][Blue_count].Y ;
                                                    Archeryinfo->BlueTarget.size  = strategy_info->color_mask_subject[Target_blue_color][Blue_count].size;
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
void KidsizeStrategy::initparameterpath(void)
{
	while(parameter_path == "N")
	{
		parameter_path = tool->getPackagePath("strategy");
	}
	printf("parameter_path is %s\n", parameter_path.c_str());
}
void KidsizeStrategy::read_head_position(void)
{
    fstream fin;//宣告fstream類別，類別變數名稱為fin(自取名)
    string sTmp;//宣告字串，變數名稱為sTmp
    char line[100];//宣告字元陣列，陣列名稱為line，大小為100
    char path[200];//宣告字元陣列，陣列名稱為path，大小為200
    strcpy(path, parameter_path.c_str());//因為path宣告的是字元，而PATH宣告的是字串，c_str是讓字串內容轉換成字元陣列，轉換後將PATH內容複製到path裡
    strcat(path, "/read_head_position.ini");//path內容後面接上/read_head_position.ini
    fin.open(path, ios::in);//進到path路徑開啟檔案(檔案名稱為read_head_position.ini)
    try
    {
        dirdata[0] = tool->readvalue(fin, "turn_head_position", 0); // 0->int 1->double//dirdata變數名稱自取
        dirdata[1] = tool->readvalue(fin, "turn_waist_big_position", 1);//fin為進去檔案
        dirdata[2] = tool->readvalue(fin, "turn_waist_small_position", 1);
        dirdata[3] = tool->readvalue(fin, "shoot_delay", 0); 
        dirdata[4] = tool->readvalue(fin, "hand_up_cnt_ave", 0);//基準Y
		dirdata[5] = tool->readvalue(fin, "test", 0);//簡化判斷測試
        dirdata[6] = tool->readvalue(fin, "Blue_size", 0);
        dirdata[7] = tool->readvalue(fin, "Yellow_size", 0);
        dirdata[8] = tool->readvalue(fin, "delay1", 1);//區間1微調
        dirdata[9] = tool->readvalue(fin, "delay2", 1);//區間2微調
        dirdata[10] = tool->readvalue(fin, "delay3", 1);//區間3微調
        dirdata[11] = tool->readvalue(fin, "delay4", 1);//區間4微調
        dirdata[12] = tool->readvalue(fin, "delay5", 1);//區間5微調
		dirdata[13] = tool->readvalue(fin, "Y_low", 0);//調完動作後的Y最低點
    }
    catch (exception e)
    {
	ROS_INFO("READ ERROR\n");
    }
}
void KidsizeStrategy::save_target_xyvalue(int xvalue, int yvalue) //將影像擷取到的目標靶的每個點存入記事本 (debug用)
{
    char path[200];
    strcpy(path, parameter_path.c_str());
    strcat(path, "/save_target_value.ini");
    fstream OutFile;
    
    ROS_INFO("Savetargetvalue");
    if(!first_write_path)
    {
        OutFile.open(path, ios::app/*|ios::out*/ /*|ios::trunc*/);
        OutFile << "Find_target_max&min_x||y"<<endl;
        first_write_path = true;
    }
    if(Trace_period_first_path)
    {
        OutFile.open(path, ios::app/*|ios::trunc*/);
        OutFile << "Trace_period_x||y"<<endl;
        Trace_period_first_path = false;
    }
    OutFile.open(path, ios::app);
    OutFile << xvalue;
    OutFile <<"	";
    OutFile << yvalue<<endl;
    ROS_INFO("SavetargetvalueEnd");
    OutFile.close();    
}
void KidsizeStrategy::Gamestart_Initialization(){  //初始化參數
    if(DIOSTARTAGAIN == false)
    {   
        if(!prepare_flag)  //若在比賽前沒有執行預備動作 則在init內執行
        {
            DelayspinOnce(1000);
            ros_com->sendBodySector(Preparatoryaction);  //call sector34
            DelayspinOnce(3000);
            ROS_INFO("PREPARE");
            read_head_position();
            Archeryinfo->Initialization_function();
            HeadPosition(HeadMotorID::VerticalID,2077,120);  //將頭轉低30度 開策略轉回正常刻度 為了確認只播是否有撥成功
            DelayspinOnce(50);
            HeadPosition(HeadMotorID::VerticalID,2077,120);
            DelayspinOnce(50);
            HeadPosition(HeadMotorID::VerticalID,2077,120);
            DelayspinOnce(500);
            HeadPosition(HeadMotorID::HorizontalID,dirdata[0],50);
            DelayspinOnce(50);
            HeadPosition(HeadMotorID::HorizontalID,dirdata[0],50);
            DelayspinOnce(50);
            HeadPosition(HeadMotorID::HorizontalID,dirdata[0],50);
            DelayspinOnce(1500);
            prepare_flag = true;
        }
	    HeadPosition(HeadMotorID::VerticalID,2047,120);
        DelayspinOnce(50);
        HeadPosition(HeadMotorID::VerticalID,2047,120);
        DelayspinOnce(50);
        HeadPosition(HeadMotorID::VerticalID,2047,120);
        DelayspinOnce(500);
        HeadPosition(HeadMotorID::HorizontalID,dirdata[0],50);
        DelayspinOnce(50);
        HeadPosition(HeadMotorID::HorizontalID,dirdata[0],50);
        DelayspinOnce(50);
        HeadPosition(HeadMotorID::HorizontalID,dirdata[0],50);
        DelayspinOnce(1500);
        i = 0;
        DIOSTARTAGAIN =true;  //變成true讓初始化參數迴圈不會再執行一次
    	sendbodystandflag = false;  //初始化站姿flag
    	Periodflag = false;  //初始化找週期flag
        first_write_path = false;  //初始化第一次寫入記事本flag
        countdown_flag = false;  //初始化符合射擊條件flag
        target_low_flag = false;  //初始化找到最低點flag
        target_high_flag = false;  //初始化找到最高點flag
        end_flag = false;  //初始化射擊結束flag
        find_target_flag = false;  //初始化找目標靶flag
        wait_for_shoot = false;  //初始化等待射擊中斷flag
        old_target_go_up = false; ////////
        turn_waist_position = 0;  //初始化轉腰刻度
        headbug_cnt = 0;
    	turn_waist_cnt = 0;  //初始化位找到目標靶的轉腰次數
        hand_up_cnt = 0; //初始化抬手次數
        xvalue_cnt = 0;  //初始化最高最低點之x數量
        th_error_judgment = 5;  //初始化最高點誤差像素
        tl_error_judgment = 5;  //初始化最低點誤差像素
        target_y_high = 240;  //初始化最高點y值
        target_y_low = 0;  //初始化最低點y值
        target_x_low_sum = 0;  //初始化最低點x平均
        target_x_high_sum = 0;  //初始化最高點x平均
        target_x_low_ave = 0;
        oldstrategy_find_low_time = 5000;  //初始化舊策略找最低點花費時間
    	Archeryinfo->Robot_state = find_target; 
        fixed_target = false;
    }   
}
void KidsizeStrategy::Draw_Function(){  //在人機介面之影像畫線
    ros_com->drawImageFunction(1, DrawMode::DrawObject,Archeryinfo->RedTarget.XMin,Archeryinfo->RedTarget.XMax,Archeryinfo->RedTarget.YMin,Archeryinfo->RedTarget.YMax,255,0,0);  //框出目標靶紅色區域
    ros_com->drawImageFunction(2, DrawMode::DrawObject,Archeryinfo->YellowTarget.XMin,Archeryinfo->YellowTarget.XMax,Archeryinfo->YellowTarget.YMin,Archeryinfo->YellowTarget.YMax,0,255,0);  //框出目標靶黃色區域
    ros_com->drawImageFunction(3, DrawMode::DrawObject,Archeryinfo->BlueTarget.XMin,Archeryinfo->BlueTarget.XMax,Archeryinfo->BlueTarget.YMin,Archeryinfo->BlueTarget.YMax,0,0,255);  //框出目標靶藍色區域
    ros_com->drawImageFunction(4, DrawMode::DrawLine, Archeryinfo->RedTarget.XMin, Archeryinfo->RedTarget.XMax, Archeryinfo->RedTarget.Y, Archeryinfo->RedTarget.Y, 0, 230, 230);  //標示紅心中心線
    ros_com->drawImageFunction(5, DrawMode::DrawLine, Archeryinfo->RedTarget.X, Archeryinfo->RedTarget.X, Archeryinfo->RedTarget.YMin, Archeryinfo->RedTarget.YMax, 0, 230, 230);  //標示紅心中心線
    ros_com->drawImageFunction(6, DrawMode::DrawLine, 150, 170, 120, 120, 255, 255, 255);  //白線
    ros_com->drawImageFunction(7, DrawMode::DrawLine, 160, 160, 110, 130, 255, 255, 255);  //白線
}
void KidsizeStrategy::Find_target(){  //找目標靶副函式
    if(Archeryinfo->RedTarget.XMin > Archeryinfo->YellowTarget.XMin)  //判斷紅模之xmin是否比黃模xmin大
    {
        if(Archeryinfo->YellowTarget.XMin > Archeryinfo->BlueTarget.XMin)  //判斷黃模xmin是否比藍模xmin大
        {
            if(Archeryinfo->RedTarget.XMin > Archeryinfo->BlueTarget.XMin)  //判斷紅模xmin是否比藍模xmin大
            {                
                gettimeofday(&tstart, NULL);  //開始計時
                y[i] = Archeryinfo->RedTarget.Y;  //儲存當前目標物紅心y值
                x[i] = Archeryinfo->RedTarget.X;  //儲存當前目標物紅心x值
                find_target_flag = true;  //找到目標靶flag變true
                Archeryinfo->Robot_state =find_target_mode;
            }
        }
    }
           
    if(!find_target_flag)  //沒找到目標靶
    {
        switch(Archeryinfo->HeadTurnSide)
        {
            case TurnRight:  //頭向右轉
                if ((Archeryinfo->HorizontalHeadPosition - Archeryinfo->HeadTurnPosition) > Archeryinfo->NewpullHorizontalMinAngle)//HorizontalMinAngle 2745
                {
                    headbug_cnt++;
                    ROS_INFO("LOOOOOOOOOOOOOOOOOOOOOK    =====     %d",headbug_cnt); //防止到點的第一瞬間沒抓到靶造成錯誤修正
                    if(headbug_cnt>100)
                    {
                        ROS_INFO("Find_target_head Turn Right");
                        HeadPosition(HeadMotorID::HorizontalID,Archeryinfo->HorizontalHeadPosition - Archeryinfo->HeadTurnPosition,120);
                        turn_waist_cnt++;
                        DelayspinOnce(150);
                    }
                }
                else  //超過轉頭極限則換方向
                {
                    ROS_INFO("Turn Right ELSE");
                    Archeryinfo->HeadTurnSide = TurnLeft;
                }
                break;
            case TurnLeft:  //頭向左轉
                if ((Archeryinfo->HorizontalHeadPosition + Archeryinfo->HeadTurnPosition) < Archeryinfo->NewpullHorizontalMaxAngle)//HorizontalMaxAngle 3400
                {
                    ROS_INFO("Find_target_head Turn Left");
                    HeadPosition(HeadMotorID::HorizontalID, Archeryinfo->HorizontalHeadPosition + Archeryinfo->HeadTurnPosition,120);
                    turn_waist_cnt--;
                    DelayspinOnce(150);
                }
                else  //超過轉頭極限則換方向
                {
                    ROS_INFO("Turn Left ELSE");
                    Archeryinfo->HeadTurnSide = TurnRight;
                }
                break;
        }
    }
}

void KidsizeStrategy::Find_target_mode() {  //找目標靶方式
    /* 新策略(找最高最低點) */
    if(strategy_info->DIOValue.Switch.D0)  //101 指撥功能 小轉腰
    {
        i++;
        y[i] = Archeryinfo->RedTarget.Y;
        x[i] = Archeryinfo->RedTarget.X;
        
        if(y[i] > y[i-1])//找最低
        {
            ROS_INFO("find_target_lowest");
            Archeryinfo->Robot_state =find_Target_y;
            Archeryinfo->Find_y_state = find_target_lowest;
        }
        else if(y[i] < y[i-1])//找最高
        {
            ROS_INFO("find_target_highest");
            Archeryinfo->Robot_state =find_Target_y;
            Archeryinfo->Find_y_state = find_target_highest;
        }
        
    }
    else  /* 不動靶策略 */
    {
        // target_x_low_ave = Archeryinfo->RedTarget.X;
        // target_y_low = Archeryinfo->RedTarget.Y;
        // Archeryinfo->Robot_state = start_timer;
        Archeryinfo->Robot_state = find_target_mode_old;
        Periodtime = 5000;  //shooting after 5sec 
        fixed_target = true;
    }
}

void KidsizeStrategy::Find_Target_y(){
    if(classifyflag)
    {
        gettimeofday(&tend, NULL);
        i++;
        y[i] = Archeryinfo->RedTarget.Y;
        x[i] = Archeryinfo->RedTarget.X;
        get_point_time[i] = (1000000*(tend.tv_sec - tstart.tv_sec) + (tend.tv_usec - tstart.tv_usec))/1000;  //儲存目前採集點的時間
        save_target_xyvalue(x[i], y[i]);  //將影像擷取到的目標靶的每個點存入記事本 (debug用)
    
        ROS_INFO("i = %d",i);
        ROS_INFO("x_i-1 = %d , x_i = %d",x[i-1], x[i]);
        ROS_INFO("y_i-1 = %d , y_i = %d",y[i-1], y[i]);
        ROS_INFO("get_point_time = %f", get_point_time[i]);
        
        switch(Archeryinfo->Find_y_state)
        {
            case find_target_lowest:  //抓靶到最低點
                ROS_INFO("find_target_lowest");
                if(!target_low_flag)
                {
                    Ycmpvalue = y[i];

                    if (Ycmpvalue >= target_y_low)
                    {
                        target_y_low =Ycmpvalue;//如果Ycompvalue大於當前的target_y_low則刷新target_y_low的值
                        ROS_INFO("target_y_low = %d",Ycmpvalue);
                    }
                    else if(target_y_low -1 > y[i])
                    {
                        target_x_low_sum = 0;
                        
                        for(int k = 0; k<=i; k++)
                        {
                            ROS_INFO("xvalue_cnt = %d", xvalue_cnt);
                            ROS_INFO("y[i-k] = %d", y[i-k]);
                            ROS_INFO("target_y_low = %d", target_y_low);
                            if(target_y_low == y[i-k])
                            {
                                ROS_INFO("target_y_low == y[i-k]");
                                target_x_low_sum += x[i-k];//將所有最低點的x值加起來
                                xvalue_cnt++;//最低點的個數

                            }
                            if(target_y_low - 2 > y[i-k])
                            {
                                if(xvalue_cnt == 0)//重新再找一次
                                {
                                    ROS_INFO("find_again");
                                    Archeryinfo->Robot_state =find_target_mode;
                                    target_y_low = 0;
                                    target_low_flag = false;
                                    target_high_flag = false;
                                    break;
                                }
                                target_x_low_ave = target_x_low_sum/xvalue_cnt;//取所有最低點x值的平均
                                target_lowest_time = get_point_time[i];
                                xvalue_cnt = 0;
                                target_low_flag = true;
                                Archeryinfo->Find_y_state = find_target_lowest;
                                ROS_INFO("find_target_lowest_end");
                                tool->Delay(500);
                                break;
                            }
                        }
                    }
                }
                else
                {
                    ROS_INFO("find_target_lowest_end!");
                    Archeryinfo->Find_y_state = find_target_highest;
                }
                break;
            case find_target_highest:  //抓靶到最高點
                ROS_INFO("find_target_highest");
                if(!target_high_flag)
                {
                    Ycmpvalue = y[i];
                                      
					if (Ycmpvalue <= 25)
					{
						Archeryinfo->Robot_state = find_target_mode_old;
                        break;
					}
                    else if (Ycmpvalue <= target_y_high)//如果Ycompvalue小於當前的target_y_low則刷新target_y_low的值
                    {
                        target_y_high =Ycmpvalue;
                        ROS_INFO("target_y_high = %d",Ycmpvalue);
                    }
                    else if(target_y_high +1 < y[i])
                    {
                        ROS_INFO("target_y_high +1 < y[i]");
                        target_x_high_sum = 0;
                        for(int k = 0; k<=i; k++)
                        {
                            ROS_INFO("xvalue_cnt = %d", xvalue_cnt);
                            ROS_INFO("y[i-k] = %d", y[i-k]);
                            ROS_INFO("target_y_high = %d", target_y_high);
                            
                            if(target_y_high == y[i-k])
                            {
                                target_x_high_sum += x[i-k];//將所有最高點的x值加起來
                                xvalue_cnt++;//最高點的個數
                            }
                            if(target_y_high + 2 < y[i-k])
                            {
                                if(xvalue_cnt == 0)
                                {
                                    ROS_INFO("find_again");
                                    Archeryinfo->Robot_state =find_target_mode;
                                    target_y_high = 240;
                                    target_low_flag = false;
                                    target_high_flag = false;
                                    break;
                                }
                                target_x_high_ave = target_x_high_sum/xvalue_cnt;//取所有最高點x值的平均
                                target_highest_time = get_point_time[i];
                                xvalue_cnt = 0;
                                target_high_flag = true;
                                Archeryinfo->Find_y_state = find_target_lowest;
                                ROS_INFO("find_target_highest_end");
                                tool->Delay(500);
                                break;
                            }
                        }
                    }
                }
                else
                {
                    ROS_INFO("find_target_highest_end!");
                    Archeryinfo->Find_y_state = find_target_lowest;
                }
                break;
        }
    }
    if(target_low_flag && target_high_flag)  //如果最高點跟最低點都找到則執行以下策略
    {
        ROS_INFO("i = %d", i);
        ROS_INFO("target_x_low_ave_%d",target_x_low_ave);
        ROS_INFO("target_y_low_%d",target_y_low);
        ROS_INFO("target_x_high_ave_%d",target_x_high_ave);
        ROS_INFO("target_y_high_%d",target_y_high);
        if(i<=30)  //如果採樣點少於30點 則重新取樣首次採集的範圍
        {
            switch (Archeryinfo->Find_y_state)
            {
                case find_target_lowest :
                    target_x_low_sum = 0;
                    target_y_low = 0;
                    target_low_flag = false;
                    // tl_error_judgment = 5;
                    ROS_INFO("Q1");
                    break;
                case find_target_highest :
                    target_x_high_sum = 0;
                    target_y_high = 240;
                    target_high_flag = false;
                    // th_error_judgment = 5;
                    ROS_INFO("Q2");
                    break;
            }
            
            tool->Delay(500);
        }
        else if(abs(target_x_low_ave - target_x_high_ave) > 4)  //如果最高跟最低點誤差大於4個像素點
        {
            y[20] = y[i];
            x[20] = x[i];
            get_point_time[0] = get_point_time[i];            
            ROS_INFO("target_x_low_ave = %d, target_x_high_ave = %d", target_x_low_ave, target_x_high_ave);
            target_y_low = 0;
            target_y_high = 240;
            target_x_low_sum = 0;
            target_x_high_sum = 0;
            target_low_flag = false;
            target_high_flag = false;
            i = 20;
            tool->Delay(500);
        }
        /* else  //如果沒有以上條件 則成功採集最高及最低點
        {
            Periodtime = 2*(abs(target_lowest_time-target_highest_time));
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            ROS_INFO("Periodtime = %f ==========================================", Periodtime);
            
            if(Periodtime<=14000)
            {
                ROS_INFO("Periodtime = %f ==========================================\n\n\n\n\n\n", Periodtime);
                Archeryinfo->Robot_state = find_period;
            }
            else if(Periodtime>14000)
            {
                tool->Delay(200);
                Trace_period_first_path = true;
                Archeryinfo->Robot_state = start_timer;
            }
        }
        */
    }
}
void KidsizeStrategy::Find_target_mode_old(){	//舊策略
	ROS_INFO("old");
	ROS_INFO("old");
	ROS_INFO("old");
	gettimeofday(&tend, NULL);
    oldstrategy_timeuse = (1000000*(tend.tv_sec - tstart.tv_sec) + (tend.tv_usec - tstart.tv_usec))/1000;
    if (oldstrategy_timeuse < oldstrategy_find_low_time)//8sec
    {
        Ycmpvalue = Archeryinfo->RedTarget.Y;  //目標靶當前y值
        if (!target_low_flag)
        {
            target_y_low = Archeryinfo->RedTarget.Y;  //取第一個y值用來判斷
            target_x_low_ave = Archeryinfo->RedTarget.X;
            target_low_flag = true;  //取到最低點後flag變true
        }
        else
        {                               
            if (Ycmpvalue >= target_y_low)  //與基準值做判斷
            {
                target_y_low = Ycmpvalue;
                target_x_low_ave = Archeryinfo->RedTarget.X;
                ROS_INFO("RedTarget.XMin = %d",Archeryinfo->RedTarget.X);
                ROS_INFO("Ycmpvalue = %d",Ycmpvalue);
                old_target_go_up = true;
            }
            if (old_target_go_up)
            {  
                if(Ycmpvalue <= target_y_low-5)
                {
                    Archeryinfo->Robot_state = find_period ;
                }
            }
        }
    }
    if (oldstrategy_timeuse >= oldstrategy_find_low_time)  //超過設定的時間就跳出這個副函式
    {
        if(fixed_target)
        {
            Archeryinfo->Robot_state = start_timer;
        }
        else
        {
            ROS_INFO("target_x_low_ave=%d", target_x_low_ave);
            ROS_INFO("target_y_low=%d", target_y_low);
            Archeryinfo->Robot_state = find_period;
        }
    }
    
}
void KidsizeStrategy::Trace_period(){  //舊策略找週期
    ROS_INFO("RedTarget.Y=%d",Archeryinfo->RedTarget.Y);
    ROS_INFO("0000000000000");
    if(target_y_low < 70){
        target_y_low = 0;
        Archeryinfo->Robot_state = find_target_mode_old;
        ROS_INFO("1111111111111");
    }
    if((Archeryinfo->RedTarget.Y + 20) >= target_y_low)//在最低點的時候(2是誤差值)
    {
        ROS_INFO("2222222222222");
        ROS_INFO("target_x_low_ave=%d", target_x_low_ave);
        if(Archeryinfo->RedTarget.X == target_x_low_ave || Archeryinfo->RedTarget.X +1 == target_x_low_ave || Archeryinfo->RedTarget.X -1 == target_x_low_ave)//判斷x值有無在最低點的x值//if(Archeryinfo->RedTarget.X+1 >= target_x_low_ave)0715
        {
            ROS_INFO("3333333333333");
            if(!Periodflag)
            {
                ROS_INFO("44444444444444");
                gettimeofday(&tstart, NULL);//第一次在最低點時開始計時
                Periodflag = true;
                DelayspinOnce(1000);//slow speed increase //fast speed decrease //為了使轉靶可以離開上述條件
            }
            else
            {
                ROS_INFO("5555555555");
                gettimeofday(&tend, NULL);//第二次在最低點時停止計時
                Periodtime  = (1000000*(tend.tv_sec - tstart.tv_sec) + (tend.tv_usec - tstart.tv_usec))/1000;//算週期
                ROS_INFO("Period is %f",Periodtime);
                tool->Delay(2000);
                Archeryinfo->Robot_state = start_timer;
            }
       }
        
    }
    
}
void KidsizeStrategy::Start_timer(ros::NodeHandle nh) {  //等待符合條件進行中斷射擊
    if(Periodtime < 4300)//週期小於轉腰的時間要將週期x2
    {
        countdown_time = 2*Periodtime - dirdata[3];
    }
    else
    {
        countdown_time = Periodtime - dirdata[3];
    }
// judge automaticlly testing

//     if(Periodtime < 3000 )//週期小於轉腰的時間要將週期x2
//     {
//         countdown_time = (((Periodtime-2800)/100*0.004)+ (dirdata[3]/100))*Periodtime +dirdata[8];//
//         ROS_INFO("111111111111111111111111111111111");
//     }
//     else if(Periodtime >= 3000 && Periodtime < 5200)
//     {
//         countdown_time = (((Periodtime-3000)/100*0.008)+ (dirdata[3]/100))*Periodtime +dirdata[9];
//         ROS_INFO("222222222222222222222222222222222");

//     }
//    else if(Periodtime >= 5200 && Periodtime < 10000)
//     {
//         countdown_time = (((Periodtime-4300)/100*0.0020)+ (dirdata[5]/1000))*Periodtime +dirdata[10];//0.0017
//         ROS_INFO("333333333333333333333333333333333");

//     }
//     else if(Periodtime >= 10000 && Periodtime < 20000)
//     {
//         countdown_time = (((Periodtime-10000)/100*0.00085)+ ((dirdata[5]/1000)+0.1))*Periodtime +dirdata[11];
//         ROS_INFO("44444444444444444444444444444444");

//     }
//     else{
//         countdown_time = 0.96*Periodtime +dirdata[12];
//         ROS_INFO("555555555555555555555555555555");
//     }

    ROS_INFO("x = %d, x_low = %d", Archeryinfo->RedTarget.X, target_x_low_ave);
    ROS_INFO("y = %d, y_low = %d", Archeryinfo->RedTarget.Y, target_y_low);
    ROS_INFO("Red size = %d",Archeryinfo->RedTarget.size);
    ROS_INFO("Blue size = %d",Archeryinfo->BlueTarget.size);
    ROS_INFO("Yellow size = %d",Archeryinfo->YellowTarget.size);
    
    if(!countdown_flag)
    {
        if(classifyflag)
        {
            if((Archeryinfo->RedTarget.Y +2) >= target_y_low)//到最低點時                
            {
                if(Archeryinfo->RedTarget.X +1 == target_x_low_ave || Archeryinfo->RedTarget.X == target_x_low_ave || Archeryinfo->RedTarget.X -1 == target_x_low_ave)
               {
                    timer_s = nh.createTimer(ros::Duration(countdown_time/1000),&KidsizeStrategy::Shooting_target,this,true,false); 
                    timer_s.start();//開始倒數計時
                    countdown_flag =true; 
                    Archeryinfo->Robot_state=Trace_waist;
                }
            }
        }
    }
}
void KidsizeStrategy::Trace_target_waist() {  //執行轉腰抬手function

    if(strategy_info->DIOValue.DInput == 28)  //0010 指撥功能 大轉腰
    {
        ROS_INFO("Dial value is 28");	
        if(target_x_low_ave>160)
        {
            turn_waist_cnt = dirdata[1]; 
        }
        else
        {
            turn_waist_cnt = -dirdata[1]; 
        }
    }
    else if(strategy_info->DIOValue.DInput == 26)  //0100 指撥功能 小轉腰
    {
        ROS_INFO("Dial value is 26");	
        if(target_x_low_ave>160)
        {
            turn_waist_cnt = dirdata[2]; 
        }
        else
        {
            turn_waist_cnt = -dirdata[2]; 
        }
    }
    else if(strategy_info->DIOValue.DInput == 30)  //0110 指撥功能 小轉腰
    {
        ROS_INFO("Dial value is 30");
        for(int i=0;i<2;i++){
            ros_com->sendBodySector(Raise_Hand);
        }	
        
    }
     else if(strategy_info->DIOValue.DInput == 31)  //1110 指撥功能 小轉腰
    {
        ROS_INFO("Dial value is 31");
        for(int i=0;i<2;i++){
            ros_com->sendBodySector(28);
        }	
        
    }
     if(Archeryinfo->BlueTarget.size >= 7400 && Archeryinfo->BlueTarget.size < 8500 )
     {
         if(Archeryinfo->YellowTarget.size < 2800)
         {
              ROS_INFO("third state");
             ros_com->sendBodySector(5);
             ros_com->sendBodySector(5);
         }else{
             ROS_INFO("second state");
        
             ros_com->sendBodySector(5);
         }

     }
     else if(Archeryinfo->BlueTarget.size>= 8500 && Archeryinfo->BlueTarget.size < 9500)
     {   
         if(Archeryinfo->YellowTarget.size >= 2800&& Archeryinfo->YellowTarget.size < 3200){
             ROS_INFO("second state");
             ros_com->sendBodySector(5);
         }else{
             ROS_INFO("third state");
             ros_com->sendBodySector(5);
             ros_com->sendBodySector(5);
         }
               
     }
     else if(Archeryinfo->BlueTarget.size >=9500 && Archeryinfo->BlueTarget.size < 10900)
     {
         if(Archeryinfo->YellowTarget.size >= 3200&&Archeryinfo->YellowTarget.size < 3700){
             ROS_INFO("first state");
         }
     }
         else{
         ROS_INFO("none");
     }
    // if(Archeryinfo->BlueTarget.size >= dirdata[6]*0.679 && (Archeryinfo->BlueTarget.size)< dirdata[6]*0.78)
    // {
    //     if(Archeryinfo->YellowTarget.size < dirdata[7]*0.757)
    //     {
    //         ROS_INFO("third state");
    //         ros_com->sendBodySector(5);
    //         ros_com->sendBodySector(5);
    //     }else{
    //         ROS_INFO("second state");
    //    
    //         ros_com->sendBodySector(5);
    //     }

    // }
    //else if(Archeryinfo->BlueTarget.size <= dirdata[6]*0.73)
    //{   
    //    if(Archeryinfo->YellowTarget.size <= dirdata[7]*0.7)
    //    {
    //        ROS_INFO("third state");
    //        ros_com->sendBodySector(5);
    //        ros_com->sendBodySector(5);
    //    }else{
    //        ROS_INFO("second state");
    //        ros_com->sendBodySector(5);
    //        
    //    }
    //           
    //}
    //else if(Archeryinfo->BlueTarget.size >=dirdata[6]*0.872 && Archeryinfo->BlueTarget.size < dirdata[6])
    //{
    //    if(Archeryinfo->YellowTarget.size >= dirdata[7]*0.864&&Archeryinfo->YellowTarget.size < dirdata[7])
    //    {
    //        ROS_INFO("first state");
    //    }
    //}
    //    else{
    //    ROS_INFO("none");
    //}

    hand_up_cnt = (-(target_y_low - dirdata[13]) )/ 3 ;//抬手次數
    turn_waist_position = (-(target_x_low_ave - 160))/1*2.5 + turn_waist_cnt*(Archeryinfo->WaistTurnPosition);//轉腰次數
    
    ROS_INFO("turnwaistposition:%d", turn_waist_position);
    ros_com->sendSingleMotor(9, turn_waist_position, 200); 
    DelayspinOnce(500);
    if (hand_up_cnt > 0)
    {
		ROS_INFO("UPUPUPUPUPUP");
        ROS_INFO("hand_up_cnt = %d ",hand_up_cnt);
        while (hand_up_cnt != 0)//抬手的次數,每抬一次減一
        {
            ros_com->sendBodySector(Raise_Hand);//執行36磁區
            DelayspinOnce(150);
            hand_up_cnt = hand_up_cnt - 1 ;
        }
    }
	else if(hand_up_cnt < 0)
	{
		ROS_INFO("DOWNDOWN");
		ROS_INFO("hand_up_cnt = %d ",hand_up_cnt);
		while (hand_up_cnt != 0)//抬手的次數,每抬一次減一
        {
            ros_com->sendBodySector(28);//執行28磁區
            DelayspinOnce(150);
            hand_up_cnt = hand_up_cnt + 1 ;
        }
	}
    tool->Delay(1000);
    ROS_INFO("countdown_time = %f", countdown_time);
    ROS_INFO("wait for shoot");
    Archeryinfo->Robot_state = Shoot;
}
void KidsizeStrategy::Shooting_target(const ros::TimerEvent& event){ //射擊function
    ROS_INFO("Shooting");
    
    ros_com->sendBodySector(Shooting);
    DelayspinOnce(1000);
    timer_f.stop();
    ShootFlag = true;            
    Archeryinfo->Robot_state = End;             
}
void KidsizeStrategy::Shoot_Forcibly(const ros::TimerEvent& event) 
{  //強制射擊function
    if(!ShootFlag)
    {
        ROS_INFO("Forcibly_Shooting");
        ros_com->sendBodySector(Shooting);
        DelayspinOnce(1000);
        ShootFlag = true;            
        Archeryinfo->Robot_state = End; 
    }
}

void KidsizeStrategy::DelayspinOnce(int timedelay){  //使其在delay時還能夠繼續收值
    strategy_info->get_image_flag = true;
    strategy_info->get_label_model_flag = true;
    classifyflag = false;
	ros::spinOnce();
	double timeuse;
    struct timeval tstart, tend;
    gettimeofday(&tstart, NULL);
    gettimeofday(&tend, NULL);
    timeuse = (1000000*(tend.tv_sec - tstart.tv_sec) + (tend.tv_usec - tstart.tv_usec))/1000;
    while (timeuse <= timedelay)
    {
        gettimeofday(&tend, NULL);
        timeuse = (1000000*(tend.tv_sec - tstart.tv_sec) + (tend.tv_usec - tstart.tv_usec))/1000;
    }
}

void KidsizeStrategy::HeadPosition(HeadMotorID ID, int Position, int Speed){//絕對角度
    ros_com->sendHeadMotor(ID,Position,Speed);
	if(ID ==HeadMotorID::HorizontalID)
	    Archeryinfo->HorizontalHeadPosition = Position;//將目前的角度記下來
	else
	    Archeryinfo->VerticalHeadPosition = Position;
}


int main(int argc, char** argv)
{
	ros::init(argc, argv, "kidsize");
	ros::NodeHandle nh;
	KidsizeStrategy KidsizeStrategy(nh);
    
	ros::Rate loop_rate(60);

    KidsizeStrategy.initparameterpath();

	while (nh.ok()) 
	{
		ros::spinOnce();
		KidsizeStrategy.strategymain(nh);
		loop_rate.sleep();
	}
	return 0;
}


void KidsizeStrategy::strategymain(ros::NodeHandle nh)
{
	strategy_info->get_image_flag = true;
    strategy_info->get_label_model_flag = true;
    classifyflag = false;  //初始化影像擷取flag
    Archeryinfo->RedTarget = {0, 0, 0, 0, 0, 0, 0, 0, 0};  //初始化紅模數值
    Archeryinfo->YellowTarget = {0, 0, 0, 0, 0, 0, 0, 0, 0};  //初始化黃模數值
    Archeryinfo->BlueTarget = {0, 0, 0, 0, 0, 0, 0, 0, 0};  //初始化藍模數值
    strategyclassify();  //擷取影像副函式
    Draw_Function();  //在人機介面之影像畫線

	if(strategy_info->getStrategyStart())  //策略指撥開啟
	{	
		timer_f.start();
        //tool->Delay(2000);
        ROS_INFO("case_%d",Archeryinfo->Robot_state);
        switch(Archeryinfo->Robot_state)
        {
            case Initialization:  //初始化
                Gamestart_Initialization();
                break;
            case find_target:  //找目標靶
                Find_target();
                break;
            case find_target_mode:  //找目標靶紅心方式
                Find_target_mode();
                break;
            case find_Target_y:  //找紅心最低點
                Find_Target_y();
                break; 
            case start_timer:  //等待符合條件進行中斷射擊
                Start_timer(nh);
                break;
            case Trace_waist:  //執行轉腰抬手
                Trace_target_waist();
                break;
            case find_target_mode_old: //舊策略
                Find_target_mode_old();
                break;
            case find_period: //舊策略找週期
                Trace_period();
                break;
            case Shoot:  //等待射擊中斷
                if(!wait_for_shoot)
                {
                   
                    ROS_INFO("countdown_time = %f", countdown_time);
                    ROS_INFO("wait for shoot");
                    wait_for_shoot = true;
                }                
                break;
            case End:  //射擊結束
                // if(!end_flag)
                // {
                    ROS_INFO("target_x_low_ave_%d",target_x_low_ave);
                    ROS_INFO("target_y_low_%d",target_y_low);
                    ROS_INFO("target_x_high_ave_%d",target_x_high_ave);
                    ROS_INFO("target_y_high_%d",target_y_high);
                    ROS_INFO("DIO = %d",strategy_info->DIOValue.DInput); 
                    ROS_INFO("Periodtime = %f",Periodtime);
                    ROS_INFO("turnwaistposition = %d",turn_waist_position);
                    ROS_INFO("hand_up_cnt = %d ",hand_up_cnt);
                    ROS_INFO("countdown_time = %f", countdown_time);
                    ROS_INFO("end");
                    tool->Delay(2000);
                //    end_flag = true;
                // }    
                break;
            }
	}
    else if((strategy_info->DIOValue.DInput == 0x09))  //10000 預備射擊動作
    {
        if(!prepare_flag)
        {
            DelayspinOnce(1000);
            ros_com->sendBodySector(Preparatoryaction);
            DelayspinOnce(3000);
            ROS_INFO("PREPARE");
            //DelayspinOnce(1000);
            Archeryinfo->Initialization_function();
            read_head_position();
            HeadPosition(HeadMotorID::VerticalID,2007,120);
            HeadPosition(HeadMotorID::VerticalID,2007,120);
            HeadPosition(HeadMotorID::VerticalID,2007,120);
            DelayspinOnce(500);
            HeadPosition(HeadMotorID::HorizontalID,dirdata[0],50);
            HeadPosition(HeadMotorID::HorizontalID,dirdata[0],50);
            HeadPosition(HeadMotorID::HorizontalID,dirdata[0],50);
            DelayspinOnce(500);
            prepare_flag = true;																																																																																					
            sendbodystandflag = false;
            ROS_INFO("Red size = %d",Archeryinfo->RedTarget.size);
            ROS_INFO("B size = %d",Archeryinfo->BlueTarget.size);
            ROS_INFO("YY size = %d",Archeryinfo->YellowTarget.size);
        }
    }
	else if((strategy_info->DIOValue.DInput == 0x08) || (strategy_info->DIOValue.DInput == 0x00))  //恢復站立姿勢
	{

        if(!sendbodystandflag)
        {
            timer_f.stop(); 
            timer_s.stop();           
            ROS_INFO("etArcheryReady"); 
            ros_com->sendBodySector(StandUp);
            DelayspinOnce(500);
            HeadPosition(HeadMotorID::VerticalID,2077,120);
            HeadPosition(HeadMotorID::VerticalID,2077,120);
            HeadPosition(HeadMotorID::VerticalID,2077,120);
            DelayspinOnce(500);
            HeadPosition(HeadMotorID::HorizontalID,2047,120);
            HeadPosition(HeadMotorID::HorizontalID,2047,120);
            HeadPosition(HeadMotorID::HorizontalID,2047,120);
            DelayspinOnce(500);
            sendbodystandflag =true;
            DIOSTARTAGAIN = false;
            ShootFlag = false;
            prepare_flag = false;
            Archeryinfo->Robot_state = Initialization;
            
        }            
        //Draw_Function();
        
    
    }
}
