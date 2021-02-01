#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 快手

import base as oUtils

iDefMin = 5
iDefMax = 10
iVideoTime = 30
# sDefApp = 'com.ss.android.ugc.livelite/com.ss.android.ugc.live.commerce.ExcitingVideoAdActivity'
sDefApp = 'com.ss.android.ugc.livelite/com.ss.android.ugc.live.main.MainActivity'

oUtils.callApp(sDefApp)
oUtils.setSleep(20)

# 刷新视频
iLen = 100
i = 0
while i < iLen:
  i += 1
  iRan = oUtils.getRandom(8, 25)
  print('执行次数：%d, 时长：%d' % (i, iRan)) # 打印
  oUtils.move(425, 1200, 460, 800) # 上滑
  oUtils.setSleep(iRan) # 延时
