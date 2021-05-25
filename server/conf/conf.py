
HOST = '0.0.0.0'
PORT = 8083
BUF_SIZE = 102400

TEST = True

MAIN_INTERFACE = [[['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "r/min"]],
                  [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]],
                  [['CPU温度', "C"], ['总电流', "A"]],
                  []]

BATERY_INTERFACE = [[['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]],
                    [['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]]]

ENGINE_INTERFACE = [[['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]],
                    [['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]]]

SETTING_INTERFACE = [[['速度', "60"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]],
                    [['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]]]


ONE_COL_NAME = {
    "电动车速度": ["时间", "速度"],
    "发动机转速": ["时间", "发动机转速"],
    "电流": ["时间", "电流"],
    "电压": ["时间", "电压"],
    "油门": ["时间", "油门"]
}

TOTAL_COL_NAME = {
    "车信息": ["时间", "行驶里程", "车最大速度", "车每秒速度", "发动机最大转速", "发动机每秒转速",
                 "使用电量", "每秒电池电流", "每秒电池电压", "每秒油门", "汽油使用量"],
}

LOG_PATH = "./logs"

DATABASES_PATH = "./databases"