#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 今日头条操作流程
from adb_cmd import adb_utils
from app_flow import read_news as news
from core_action import action_tool as act


class Toutiao(object):
    """
    今日头条应用流
    """

    def __init__(self):
        pass

    # 宝箱坐标：eggX,eggY
    def eatBox(self, eggX, eggY):
        adb_utils.setSleep(2)
        # 点击宝箱
        eggX = adb_utils.getRandom(eggX - 5, eggX + 5)
        eggY = adb_utils.getRandom(eggY - 5, eggY + 5)

        print('>>> 执行点击宝箱操作,坐标: (%d,%d) ' % (eggX, eggY))
        adb_utils.tap(eggX, eggY)

        # 等待动画
        adb_utils.setSleep(3)

        print('>>> 完成点击宝箱操作')
        return

    def eatAD(self, adX, adY, needBack):
        """
        :param adX: 视频广告坐标X
        :param adY: 视频广告坐标Y
        :param needBack: 是否结束时返回上级页面 0:NO, >0 YES
        """

        adb_utils.setSleep(1)
        # 看广告,点击位置
        adX = adb_utils.getRandom(adX - 5, adX + 5)
        adY = adb_utils.getRandom(adY - 5, adY + 5)

        print('>>> 执行点击观看广告操作,坐标: (%d,%d) ' % (adX, adY))
        adb_utils.tap(adX, adY)

        # 等待广告看完
        print('>>> 等待广告看完')
        adb_utils.setSleep(22)

        # 循环8次后将会提示需要再次查看广告
        # TODO  待处理

        # 返回到上级页面
        # if needBack:
        # adb_utils.backKey()

        # 等待动画完成
        # adb_utils.setSleep(2)

        print('>>> 完成视频广告操作')
        return

    def readNewsAndEatBox(self):
        """
        阅读文章并开箱
        """
        # 等待界面稳定
        adb_utils.setSleep(1)

        print('\n\033[1;32m>>> 文章阅读 \033[0m')
        adb_utils.setSleep(1)

        # 点击文章列表

        print('>>> 点击文章列表')
        news.tapNewsList(0)
        # 等待界面稳定
        adb_utils.setSleep(2)

        # 阅读新闻 10分钟一次
        print('>>> 阅读新闻,10分钟一次')
        news.readNews(600)

        adb_utils.setSleep(1)

        # 点击红包到任务中心
        self.tipRadBagToBox_pri()

        # 返回到文章列表
        print('>>> 返回到文章列表.')
        adb_utils.backKey()
        adb_utils.setSleep(3)

        # 移动到新的文章列表
        print('>>> 移动到下篇文章.')
        news.moveNextNewsList()
        # 等待下一次循环

        return

    # --------------------------
    def tipRadBagToBox_pri(self):
        """
        #点击红包到任务中心
        ##点击开宝箱,10分钟一次  
        """
        # 
        # --------------------------
        # 
        print('>>> 跳转到任务中心，等待6s...')
        adb_utils.tap(170, 140)

        # 等任务中心加载出来
        adb_utils.setSleep(6)

        # 点击宝箱
        print('>>> 点击宝箱，开宝箱')
        self.eatBox(905, 665)
        adb_utils.setSleep(3)

        # 看广告
        self.eatAD(575, 785, 1)

        # 返回到任务中心
        adb_utils.backKey()

        # 休息3s
        adb_utils.setSleep(1)

        # 返回到文章页面.
        adb_utils.backKey()
        adb_utils.setSleep(2)
        # --------------------------
        return


# 测试用例
def tt_test_main():
    tt = Toutiao()
    tt.eatBox(55, 33)
    tt.eatAD(12, 43, 1)
    return


def test_openBox():
    """测试从红包
    """
    tt = Toutiao()

    print('>>> 跳转到任务中心，等待6s...')
    adb_utils.tap(170, 140)

    # 等任务中心加载出来
    adb_utils.setSleep(6)

    # 点击宝箱
    print('>>> 点击宝箱，开宝箱')
    tt.eatBox(905, 665)
    adb_utils.setSleep(3)

    # 看广告
    tt.eatAD(575, 785, 1)

    adb_utils.setSleep(1)

    adb_utils.backKey()

    # 休息4s
    adb_utils.setSleep(4)

    # 返回到文章页面.
    adb_utils.backKey()
    adb_utils.setSleep(2)
    # --------------------------

    # 返回到文章列表
    print('>>> 返回到文章列表.')
    adb_utils.backKey()
    adb_utils.setSleep(3)


if __name__ == "__main__":
    pass
    # test_openBox()
