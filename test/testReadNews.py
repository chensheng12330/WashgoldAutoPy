#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import unittest
import read_news as news
import base as oUtils


class read_news_Test(unittest.TestCase):
    
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

    def test_other(self):
        pass

#全量运行时
if __name__ == '__main__':
    '''
    suite = unittest.TestSuite()
    suite.addTest(MyclassTest('test_add'))
    suite.addTest(MyclassTest('test_sub'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''
    pass