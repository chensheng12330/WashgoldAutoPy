#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 淘宝直播操作流程
from adb_cmd import adb_utils as adb  # 导入adb工具


class TaoBao(object):

    # 金币页面彩蛋坐标：coEggX,coEggY
    def eatColEggs(self, coEggX, coEggY):
        # 等待界面稳定
        adb.setSleep(2)

        # 点击彩蛋
        adX = adb.getRandom(coEggX - 5, coEggX + 5)
        adY = adb.getRandom(coEggY - 5, coEggY + 5)

        print('>>> 执行点击彩蛋操作,坐标: (%d,%d) ' % (adX, adY))
        adb.tap(adX, adY)

        adb.setSleep(1)

        adb.backKey()

        adb.setSleep(2)

        print('>>> 完成金币页面彩蛋操作')

        # 完成操作
        return

    # 看直播鸡蛋坐标：eggx,eggy
    def eatEggs(self, eggX, eggY):
        # 等待界面稳定
        adb.setSleep(2)

        # 获取点击的坐标，范围内随机值，10个像素的偏移
        eggX = adb.getRandom(eggX - 5, eggX + 5)
        eggY = adb.getRandom(eggY - 5, eggY + 5)

        # 点击蛋蛋
        print('>>> 执行点击蛋蛋操作,坐标: (%d,%d) ' % (eggX, eggY))

        adb.tap(eggX, eggY)

        # 等待动画完成
        adb.setSleep(2)

        print('>>> 完成点击直播鸡蛋操作')
        return


def tb_test_main():
    tt = TaoBao()
    tt.eatEggs(222, 111)
    tt.eatColEggs(222, 234)

# tb_test_main()
