#include <ros/ros.h>
#include <ros/package.h>
#include <vector>
#include <stdio.h>
#include <std_msgs/String.h>
#include "tku_libs/strategy_info.h"
#include "tku_libs/TKU_tool.h"
#include "tku_libs/RosCommunication.h"
#include "strategy/archeryinfo.h"
#include <ctime>
#include <iostream>
#include <string>

#define Preparatoryaction 34
#define Raise_Hand 36
#define Shooting 35
#define StandUp 29

using namespace std;

class KidsizeStrategy
{
public:
	KidsizeStrategy(ros::NodeHandle &nh)
	{
		timer_f = nh.createTimer(ros::Duration(100),&KidsizeStrategy::Shoot_Forcibly,this,true,false); 
		strategy_info = StrategyInfoInstance::getInstance();
		tool = ToolInstance::getInstance();
		ros_com = RosCommunicationInstance::getInstance();
	};
	~KidsizeStrategy(){};
	void strategymain(ros::NodeHandle nh);
	void strategyclassify();
	void initparameterpath(void);
	void read_head_position(void);
	void save_target_xyvalue(int xvalue, int yvalue);
	void Gamestart_Initialization();
	void Draw_Function();
	void Find_target();
	void Find_target_mode();
	void Find_target_mode_old();
	void Find_Target_y();
	void Trace_target_waist(); 
	void Shooting_target(const ros::TimerEvent& event);
	void Shoot_Forcibly(const ros::TimerEvent& event);
	void DelayspinOnce(int timedelay);
	void HeadPosition(HeadMotorID ID, int Position, int Speed);
	void Start_timer(ros::NodeHandle nh);
	void Get_lowest_point_time();
	void Get_highest_point_time();
	void Trace_period();
	ros::Timer timer_f;
	ros::Timer timer_s;

	RosCommunicationInstance *ros_com;
	ToolInstance *tool;
	StrategyInfoInstance *strategy_info;

	bool sendbodystandflag = false;
	bool DIOSTARTAGAIN = false;
	bool classifyflag = false;
	bool countdown_flag = false;
	bool Periodflag = false;
	bool ShootFlag = false;
	// bool Trace_period_Flag = false;
	bool target_low_flag = false;
	bool target_high_flag = false;
	//bool Shooting_Forcibly = false;
	bool first_write_path = false;
	bool Trace_period_first_path = false;
	bool find_target_flag = false;
	bool prepare_flag = false;
	bool end_flag = false;
	bool wait_for_shoot = false;
	bool old_target_go_up = false;
	bool fixed_target = false;

	int i = 0;
	int r = 0;

	int Ycmpvalue = 0;  //舊策略的y值基準
	int xvalue_cnt = 0;
	int hand_up_cnt = 0;
	int headbug_cnt = 0;
	int turn_waist_cnt = 0;
	int turn_head_position = 0;
	int turn_waist_position = 0;
	int oldstrategy_find_low_time = 0;

	int target_y_low = 0;
	int target_y_high = 0;
	int target_x_low_sum = 0;
	int target_x_high_sum = 0;
	int target_x_low_ave = 0;
	int target_x_high_ave = 0;
	int tl_error_judgment = 0;
	int th_error_judgment = 0;
	int target_lowest_error = 0;
	int target_highest_error = 0;

	int x[2000];
	int y[2000];
	double get_point_time[10000];

	double dirdata[20];
	double Period = 0;
	double Periodtime;
	double countdown_time = 0;
	double Find_redTarget_time = 0;
	double target_lowest_time = 0;
	double target_highest_time = 0;
	double oldstrategy_timeuse = 0;

	string parameter_path = "N";

	struct timeval tstart, tend;

	clock_t start_time;
	clock_t end_time;

};
