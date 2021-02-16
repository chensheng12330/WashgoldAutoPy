#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 抖音直播操作流程

from adb_cmd import adb_utils
from core_action import action_tool as act


class Tiktok(object):
    """
    视频观看，上下滑动
    """

    def __init__(self):
        pass

    def moveUpVideo(self):
        """
        上一个视频
        """
        act.wait(1)
        act.moveDownWithRand(780, 160, 20, 600, 300)
        act.wait(1)
        return

    # 下一个视频

    def moveDownVideo(self):
        act.wait(1)
        act.moveUpWithRand(780, 700, 20, 600, 300)
        act.wait(1)
        return

    # 点击红包,并开宝箱，点广告
    def eatRadBagAndOpenBox(self):
        act.tapWithRand(110, 480)
        # 等任务页面加载（任务中心加载时长较大）
        act.wait(10)

        # 点击宝箱
        act.tapWithRand(920, 720)

        # 等宝箱打开页面加载
        act.wait(4)

        # 点击广告
        act.tapWithRand(550, 720)

        # 等广告页面看完
        act.wait(40)

        # 退出下载页面
        adb_utils.backKey()
        act.wait(3)

        # 退出广告页面
        adb_utils.backKey()
        act.wait(3)

        # 退出任务中心页面
        adb_utils.backKey()
        act.wait(3)

        # 完成.
        return

    # 观看视频，上下滑动,每20分钟点红包到任务中心开宝臬
    def readVideo(self):
        # 收藏里共三个视频，循环一次10分钟.

        i = 7
        while i > 1:

            print(">>> 正在观看第(%d)视频,时长3分钟..." % (7 - i + 1))

            act.wait(3 * 60)
            if i <= 4:
                self.moveUpVideo()

            else:
                self.moveDownVideo()
            # 减一.
            i -= 1

        return

    def open20AdVideo(self):
        """限时任务. 半屏模式，需要装限时任务栏滑动到导航栏下.
        """

        act.wait(3)
        # 半屏坐标
        act.tapWithRand(700, 380, 16)
        # 等广告看完
        act.wait(60)
        # oUtils.backKey()
        # act.wait(3)
        adb_utils.backKey()
        act.wait(3)
        return

    def openBox(self):
        """开宝箱并看广告.
        """
        act.wait(3)
        # 点击宝箱
        print(">> 点击宝箱")
        act.tapWithRand(920, 720)

        # 等宝箱打开页面加载
        act.wait(4)

        # 点击广告
        print(">> 点击广告")
        act.tapWithRand(550, 720)

        # 等广告页面看完
        print(">> 等广告页面看完")
        act.wait(80)

        #点击进入广告的下载页面

        # 退出下载页面
        # oUtils.backKey()
        # act.wait(3)

        # 退出广告页面
        print(">> 退出广告页面")
        adb_utils.backKey()
        act.wait(4)

        return


if __name__ == "__main__":
    #print(f"pass {__file__}")
    pass
    # Tiktok().eatRadBagAndOpenBox()
    # tiktok().moveUpVideo()
    # tiktok().moveDownVideo()
