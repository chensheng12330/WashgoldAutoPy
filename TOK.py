#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from adb_cmd import adb_utils as adb  # 导入adb工具
from core_action import action_tool as act
from app_flow import tiktok  # 导入今日头导操作
from mobile_run import devices_list as devlist  # 设备列表

'''
进行抖音的开宝箱操作，做广告任务.

宝箱：10分钟一次
广告任务：20分钟一次

需要全屏页面，将任务列表栏

'''


def main():
    # 获取当前选择的设备

    adb.gb_devices_name = devlist.getUserSelectDevice()

    tok = tiktok.Tiktok()

    count = 0
    maxCount = 100000

    print('\n\033[1;44m----------------启动抖音开宝箱，做视频广告任务--------------------\033[0m')

    act.wait(3)
    print("> 1.开宝箱,点广告，领金币.")
    tok.openBox()
    act.wait(10)
    print("> 2.做视频广告任务-.")
    tok.open20AdVideo()

    while count < maxCount:
        print(">>> 开始一个20分钟的循环操作...")
        count += 1

        # 等10分钟....
        act.wait(11 * 60)
        print(">>> 1.开宝箱,点广告，领金币.")
        tok.openBox()

        act.wait(10 * 60)
        print(">>> 2.开宝箱,点广告，领金币.")
        tok.openBox()

        # 需要点击，防止睡了.
        print(">>> 3.做视频广告任务-.")
        tok.open20AdVideo()

        # 进入下一次循环
        print('--- 执行次数：%d, \n' % count)
        continue


# 启动开始
main()
