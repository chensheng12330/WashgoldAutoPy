#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from adb_cmd import adb_utils as adb  # 导入adb工具
from app_flow import toutiao  # 导入今日头导操作
from mobile_run import devices_list as devlist
from app_flow import read_news as news

'''
进行今日头条的文章阅读，开宝箱操作.
半屏坐标.

执行40分钟文章阅读，
连续执行开宝箱操作.
'''

# 执行的次数
run_count = 100


def main():
    """
    1. 初使化设备列表
    2. 获取当前用户选择的设备
    3. 执行命令
    """

    # 设置当前的设备为 用户选择输入.
    curDevicesName = devlist.getUserSelectDevice()
    adb.gb_devices_name = curDevicesName

    tt = toutiao.Toutiao() 

    count = 0
    max_count = run_count
    count = 0
    max_count = run_count

    print('\n\033[1;44m---------启动今日头条的视频观看----------\033[0m')

    while count < max_count:
        count += 1
        
        adx = adb.getRandom(400, 500)

        begY =  adb.getRandom(1200, 1300)
        endY =  adb.getRandom(300, 400)

        tt.slideUpVideo(adx, begY, endY, 500)

        sleepT = adb.getRandom(15, 30)
        adb.setSleep(sleepT)

        # 进入下一次循环
        print('--- 执行次数：%d, ' % count)
        print("当前设备: %s \n" % curDevicesName)
        continue

    #手机关机.
    adb.closePhone()

    #手机关闭屏幕
    #adb.closeScreen()


# 启动开始
main()
