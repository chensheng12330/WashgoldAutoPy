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

    print("可选的设备的序号:")
    show_str = ""
    cout = 0
    for devDict in devlist.devices_list:
        phone_no = devDict['phone_no']
        dev_no = devDict['dev_no']
        show_str += "序号:" + str(cout) + "    手机号：" + phone_no + " 设备号：" + dev_no + "\r\n"
        cout += 1

    print(show_str)

    dev_dict = {}
    while 1:

        sel_num = input("请选择需要执行的序号：")
        int_sel_num = int(sel_num)

        if 0 <= int_sel_num < len(devlist.devices_list):
            dev_dict = devlist.devices_list[int_sel_num]
            print(dev_dict)
            break
        else:
            print("输入错误，请重新选择")

    # 设置当前的设备为 (4857d2bc) ->135设备.
    adb.gb_devices_name = dev_dict["dev_no"]

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
        print(f"当前设备: {dev_dict} \n")
        continue


# 启动开始
main()
