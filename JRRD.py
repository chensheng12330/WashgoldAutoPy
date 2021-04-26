#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from adb_cmd import adb_utils as adb  # 导入adb工具
from app_flow import toutiao  # 导入今日头导操作
from mobile_run import devices_list as devlist
from app_flow import read_news as news

'''
进行今日头条的小说阅读
半/全屏坐标.
'''

# 执行的次数
run_count = 100000


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

    print('\n\033[1;44m---------启动今日头条的小说阅读----------\033[0m')

    while count < max_count:
        count += 1
        
        sleepT = adb.getRandom(5, 15)
        adb.setSleep(sleepT)
        
        coEggX = 1024
        coEggY = 600
        adX = adb.getRandom(coEggX - 20, coEggX + 20)
        adY = adb.getRandom(coEggY - 200, coEggY + 300)

        adb.tap(adX, adY)

        # 进入下一次循环
        print('--- 执行次数：%d, ' % count)
        print("当前设备: %s \n" % curDevicesName)
        continue

# 启动开始
main()
