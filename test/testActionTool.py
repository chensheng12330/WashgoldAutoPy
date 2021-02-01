#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import base as oUtils
import unittest
import action_tool as act

class testActionTool(unittest.TestCase):
    def setUp(self) -> None:
        '''
        测试之前的准备工作
        :return:
        '''
        

    def tearDown(self) -> None:
        '''
        测试之后的收尾
        如关闭数据库
        :return:
        '''
        pass

    def test_keepAlive(self):
        print("休息一秒")
        act.wait()
        print("休息5秒")
        act.wait(5)

        act.keepAlive()

    def test_tapWithRand(self):
        print("点击：(500,300)")
        act.tapWithRand(500,300)
        act.wait(2)

        print("点击：(500,600)")
        act.tapWithRand(500,600,600)
        act.wait(2)

    def test_moveUpDownWithRand(self):

        print("UP：(300,500,40)")
        act.wait(2)
        act.moveUpWithRand(300,500,40)

        print("DOWN：(300,500,40)")
        act.wait(2)
        act.moveDownWithRand(300,500,40)


if __name__ == '__main__':
    test = testActionTool()
    # test.test_keepAlive()
    # test.test_tapWithRand()
    test.test_moveUpWithRand()
