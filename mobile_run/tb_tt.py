#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from adb_cmd import adb_utils as adb  # 导入adb工具
from core_action import action_tool as act
from app_flow import tiktok  # 导入今日头导操作
from mobile_run import devices_list as devlist  # 设备列表

"""
上部分头条，下部分淘宝 （10分钟一次操作）
"""

def main():
    maxCount=100000
    count=0

    #头条对象
    tt = toutao.toutiao()

    #淘宝对象
    tb = taobao.taobao()

    while count<maxCount:

        count += 1

        print('\n\033[1;44m----------------启动自动化---------------------\033[0m')

        #-------头条执行--------------------------------------
        print('\033[1;35m>>> 头条夺宝\033[0m')

        #点击宝箱
        tt.eatBox(905,665)
        oUtils.setSleep(3)

        #看广告
        tt.eatAD(575,785,1)

        #休息3s
        oUtils.setSleep(4)

        #-------淘宝执行--------------------------------------
        print('\n\033[1;32m>>> 淘宝夺宝 \033[0m')

        #点击直播蛋
        tb.eatEggs(905,1705)

        #休息2s
        oUtils.setSleep(2)

        #点击直播蛋到彩蛋页面
        tb.eatEggs(905,1705)
        #点击彩蛋
        tb.eatColEggs(905,1460)
        
        oUtils.setSleep(2)

        #休息到下转值 10分钟一次 10*60
        iRan = oUtils.getRandom(600, 610)

        print('--- 执行次数：%d, 休眠时长：%d' % (count, iRan)) # 打印
        print('----------------休眠中---------------------')
        #print('eggY: %d,sleepT: %d,iRan: %d' % (eggY, sleepT, iRan))
        sleepTime = iRan/3.0   #分4次处理.

        while iRan>6 :
            iRan -= sleepTime

            print('>>> 休眠中(剩余:%d s, 当前: %d s) \n' % (iRan,sleepTime))
            oUtils.setSleep(sleepTime)

            #醒来了一下
            oUtils.tap(500,5) #防止屏黑.

            if iRan>10:
                tb.eatEggs(905,1705)

                
            


#-------------------------------------------------
#执行主程序
main()