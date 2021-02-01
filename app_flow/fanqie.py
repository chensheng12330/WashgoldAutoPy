#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 番茄小说

import base as oUtils

iDefMin = 5
iDefMax = 10
iVideoTime = 40
sDefApp = 'com.dragon.read/com.dragon.read.pages.splash.SplashActivity'

oUtils.callApp(sDefApp)
oUtils.setSleep(iDefMax) # 广告

# 点击福利
oUtils.tap(577, 2258)
oUtils.setSleep(iDefMin)

# 点击宝箱
# oUtils.tap(948, 1964)
# oUtils.setSleep(3)
# oUtils.tap(528, 1449)
# oUtils.setSleep(iVideoTime)
# oUtils.tap(973, 91)
# oUtils.setSleep(iDefMin)

# 刷新视频
oUtils.move(425, 1200, 460, 400) # 上滑
iLen = 10
i = 0
while i < iLen:
  i += 1
  print('执行次数：%d, 时长：%d' % (i, iVideoTime)) # 打印
  oUtils.tap(847, 1259)
  oUtils.setSleep(iVideoTime) # 延时
  oUtils.tap(964, 117) # 关闭
  oUtils.setSleep(3, 5)