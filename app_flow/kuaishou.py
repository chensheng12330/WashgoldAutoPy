#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 快手
import sys as oSys
import base as oUtils
from app_list import oAppMoveList


iDefMin = 5
iDefMax = 10
iVideoTime = 30
sDefApp = oAppMoveList['kuaishou']

oUtils.callApp(sDefApp)
oUtils.setSleep(20)
