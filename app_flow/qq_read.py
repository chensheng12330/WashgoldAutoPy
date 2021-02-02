#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# QQ阅读操作流程
from adb_cmd import adb_utils
from app_flow import read_news as news
from core_action import action_tool as act


class QQRead(object):
    """
    QQ阅读
    """

    def __init__(self):
        pass

    def nextPage(self, maxY=1000, tapX=1060):
        """ 阅读小说进行翻页,(1060, (140~1000) )

        :param tapX: 点击翻页的时的X坐标值，默认值为：1060
        :param maxY: 点击的Y坐标最大的偏移随机值，用于防止系统变为机器人
        :return: none
        """

        adb_utils.setSleep(2)

        pageY = adb_utils.getRandom(140, maxY)

        print('>>> 执行翻页操作,坐标: (%d,%d) ' % (tapX, pageY))
        adb_utils.tap(tapX, pageY)

        # 等待动画
        adb_utils.setSleep(3)

        # print('>>> 完成点击宝箱操作')
        return

if __name__ == "__main__":
    pass
    # test_openBox()
