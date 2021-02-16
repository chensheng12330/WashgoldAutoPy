#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from adb_cmd import adb_utils as adb  # 导入adb工具
from app_flow import toutiao  # 导入今日头导操作
from mobile_run import devices_list as devlist
from os import popen  # 管道处理

'''
进行今日头条的文章阅读，开宝箱操作.
半屏坐标.

4857d2bc	device
8514c020	device
e3656a1b
'''

def main():
    
    popen('adb -s 4857d2bc shell input tap 426 1000') 
    popen('adb -s 8514c020 shell input tap 426 1000') 
    popen('adb -s e3656a1b shell input tap 426 1000') 

# 启动开始
main()
