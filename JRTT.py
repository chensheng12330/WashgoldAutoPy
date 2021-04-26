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
run_count = 2


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

    while count < max_count:
        count += 1
        print('\n\033[1;44m----------------启动自动化---------------------\033[0m')

        tt.readNewsAndEatBox()

        adb.setSleep(2)

        # 进入下一次循环
        print('--- 执行次数：%d, ' % count)
        print("当前设备: %s \n" % curDevicesName)
        continue

    # 等待界面稳定
    adb.setSleep(10)
    print('>>> 点击文章列表')
    news.tapNewsList(0)
    adb.setSleep(5)

    #点击红包进入到任务中心
    adb.tap(170, 140)
    
    print('>>> 跳转到任务中心，等待10分钟...')
    adb.setSleep(10*60)
    #开启宝箱10分钟一次
    count = 0
    max_count = 100000

    # 10分钟一次开宝箱.
    sleepTime = 10*60

    #等待宝箱10分钟倒计时.
    #adb.setSleep(sleepTime)

    while count < max_count:
        count += 1
        print('\n\033[1;44m----------------启动任务页面开宝箱自动化---------------------\033[0m')

        tt.eatBoxAndAD()

        adb.setSleep(sleepTime)

        # 进入下一次循环
        print('--- 执行次数：%d, ' % count)
        print("当前设备: %s \n" % curDevicesName)
        continue


# 启动开始
main()
