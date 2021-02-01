#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys as oSys
import base as oUtils
from app_list import oAppMoveList
from element import Element
from math import trunc

oEmt = Element() # 初始化工具

vmSize = oUtils.vmSize()
print(vmSize)
gridW = trunc(int(vmSize['w']) / 10)
gridH = trunc(int(vmSize['h']) / 10)
print(gridH)

oEmt.init()
moive = oEmt.findElementByName(u"视频")
print(moive)