#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from adb_cmd import adb_utils as adb  # 导入adb工具
from app_flow import toutiao  # 导入今日头导操作
from mobile_run import devices_list as devlist

'''
进行今日头条的文章阅读，开宝箱操作.
半屏坐标.
'''

# 执行的次数
run_count = 4


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

        adb.setSleep(1)

        # 进入下一次循环
        print('--- 执行次数：%d, ' % count)
        print("当前设备: %s \n" % curDevicesName)
        continue


# 启动开始
main()
