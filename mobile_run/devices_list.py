#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 设备与手机绑定字典表
devices_list = [{"phone_no": "135", "dev_no": "4857d2bc"},
{"phone_no": "158", "dev_no": "8514c020"},
{"phone_no": "171", "dev_no": "e3656a1b"},
{"phone_no": "137", "dev_no": "a790be09"}]


def getUserSelectDevice():
    """获取当前用户选择的设备"""

    print("可选的设备的序号:")
    show_str = ""
    count = 0
    for devDict in devices_list:
        phone_no = devDict['phone_no']
        dev_no = devDict['dev_no']
        show_str += "序号:" + str(count) + "    手机号：" + phone_no + " 设备号：" + dev_no + "\r\n"
        count += 1

    print(show_str)

    dev_dict = {}
    while 1:

        sel_num = input("请选择需要执行的序号(退出请输入 q)：")
        if sel_num == 'q':
            exit(0)

        int_sel_num = int(sel_num)

        if 0 <= int_sel_num < len(devices_list):
            dev_dict = devices_list[int_sel_num]
            print(dev_dict)
            break
        else:
            print("输入错误，请重新选择")

    return dev_dict["dev_no"]
