#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from adb_cmd import adb_utils
from core_action import action_tool as act

"""阅读文章操作事件"""

def tapNewsList(offsetY):
    """[点击文章列表中的某篇文章]

    Args:
        offsetY ([数字]): [文章的Y坐标值]
    """
    iRanY = adb_utils.getRandom(500, 520) - offsetY
    adb_utils.setSleep(1)
    adb_utils.tap(500, iRanY)
    adb_utils.setSleep(1)
    return


# 移动文章列表
def moveNextNewsList(moveX=500, BegY=770, EndY=130, delay=800):
    """
    移动文章列表，使其处理顶部位置，方便行文章点击操作  
    可配合 [tapNewsList] 操作

    Args:
        moveX (int, optional): [移动的X坐标值]. Defaults to 500.
        BegY (int, optional): [移动开始的Y坐标]. Defaults to 870.
        EndY (int, optional): [移动结束的Y坐标]. Defaults to 230.
        delay (int, optional): [移动持续时长,单位ms]. Defaults to 800.
    """
    adb_utils.setSleep(1)
    adb_utils.move(moveX, BegY, moveX, EndY, delay)
    adb_utils.setSleep(1)
    return


def moveLastNewsList():
    adb_utils.setSleep(1)
    adb_utils.move(500, 226, 500, 874, 2000)
    adb_utils.setSleep(2)
    return


def readNews(beginY=600, readTime=10):
    """[查阅文章，上下滑动 ]  
    #10分钟一次阅读,8分钟向下滑动，2分钟向上滑动 

    Args:
        beginY (int, optional): [滑动开始的位置]. Defaults to 600.
        readTime (int, optional): [阅读文章时长，单位分钟]. Defaults to 10分钟.
    """

    # 5秒休息一次，10分钟反向滑动
    # 向上移动8分钟，向下移动2分钟，共10分钟.

    moveCout = (readTime - 1) * 60
    moveNum = 0

    coEggX = 500
    coEggY = beginY

    # 向上滑动
    while moveCout > 1:
        adX = adb_utils.getRandom(coEggX - 20, coEggX + 20)
        adY = adb_utils.getRandom(coEggY - 5, coEggY + 5)
        adL = adb_utils.getRandom(45, 70)
        adb_utils.move(adX, adY, adX, adY - adL, 700)
        adb_utils.setSleep(5)
        moveCout -= 5
        moveNum += 1
        print(">>> 文章阅读中，->向上移动次数 (%d) 阅读时长(%d)..." % (moveNum, moveNum * 5))

    # 向下滑动
    moveNum = 0
    moveCout = 1 * 60
    while moveCout > 1:
        adX = adb_utils.getRandom(coEggX - 20, coEggX + 20)
        adY = adb_utils.getRandom(coEggY - 5, coEggY + 5)
        adL = adb_utils.getRandom(45, 80)
        adb_utils.move(adX, adY - adL, adX, adY, 700)
        adb_utils.setSleep(5)
        moveCout -= 5
        moveNum += 1
        print(">>> 文章阅读中，<-向下移动次数 (%d) 阅读时长(%d)..." % (moveNum, moveNum * 5))


def test_main():
    '''测试主流程'''

    while 1:
        adb_utils.setSleep(1)
        tapNewsList(0)
        adb_utils.setSleep(1)
        readNews(940)
        adb_utils.setSleep(1)
        adb_utils.backKey()
        adb_utils.setSleep(2)
        moveNextNewsList()


# 执行


def test_1():
    '''其它'''
    moveNextNewsList()


if __name__ == "__main__":
    test_main()
    # adb_utils.gb_devices_name = "a790be09"
    # readNews()
    # moveNextNewsList()
    # pass

