#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from ast import If
from unittest import case
from adb_cmd import adb_utils as adb  # 导入adb工具
from mobile_run import devices_list as devlist

'''
手机群操作
'''

function_list = [
    {"fun_no":"0", "fun_name":"关机"},
    {"fun_no":"1", "fun_name":"重启"},
    {"fun_no":"2", "fun_name":"关屏"}
    ]

#当前功能选择
def getSelectFuction():
    """获取当前用户选择的设备"""

    print("选择你需要的功能:")
    show_str = ""
    count = 0
    for devDict in function_list:
        fun_no   = devDict['fun_no']
        fun_name = devDict['fun_name']

        show_str += "序号:" + fun_no + "    功能名：" + fun_name + '\n'
        count += 1

    print('-------------------------------------')
    print('\033[1;34m%s \033[0m' % show_str)
    print('-------------------------------------')

    dev_dict = {}
    while 1:

        sel_num = input(">请选择需要执行的序号(退出请输入 q)：")
        if sel_num == 'q':
            exit(0)

        int_sel_num = int(sel_num)

        if 0 <= int_sel_num < len(function_list):
            dev_dict = function_list[int_sel_num]
            print(dev_dict)
            break
        else:
            print("输入错误，请重新选择")

    return dev_dict["fun_no"]



def main():
    """
    1. 功能选择清单
    2. 执行操作
    3. 完成回馈
    """

    curFuction = getSelectFuction()
    
    if curFuction == '0':
        curDevicesName = devlist.getUserSelectDevice()
        adb.gb_devices_name = curDevicesName
        adb.closePhone()
    elif curFuction == '1':

        curDevicesName = devlist.getUserSelectDevice()
        adb.gb_devices_name = curDevicesName
        adb.rebootPhone() 
    elif curFuction == '2':
        curDevicesName = devlist.getUserSelectDevice()
        adb.gb_devices_name = curDevicesName
        adb.closeScreen()

    return
    # 设置当前的设备为 用户选择输入.
    curDevicesName = devlist.getUserSelectDevice()
    adb.gb_devices_name = curDevicesName


    print('\n\033[1;44m---------启动今日头条的视频观看----------\033[0m')

    while count < max_count:
        count += 1
        
        adY = adb.getRandom(300, 500)

        begX = adb.getRandom(800, 1000)
        endX = adb.getRandom(100, 300)

        tt.slideVideo(adY, begX, endX, 500)

        sleepT = adb.getRandom(15, 30)
        adb.setSleep(sleepT)

        # 进入下一次循环
        print('--- 执行次数：%d, ' % count)
        print("当前设备: %s \n" % curDevicesName)
        continue

    #手机关闭屏幕
    adb.closeScreen()


# 启动开始
main()
