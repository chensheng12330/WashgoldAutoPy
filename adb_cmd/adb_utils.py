#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os as osOs  # 内置shell交互
from os import popen as osPopen  # 管道处理
from os import system as osSystem
import os  # 管道处理
import random as osRandom  # 随机数
from time import sleep as osSleep
import re as osRe

# 全局变量：设备号, 默认连接的设备只有一台，可以不用使用.
gb_devices_name = ""


def setCurDevicesName(devicesName):
    global gb_devices_name
    gb_devices_name = devicesName

    return


# 如有多设备，需要组装相应的字符串
def get_devices_str():
    cmd_dev_name = ""
    if gb_devices_name != "":
        cmd_dev_name = "-s " + gb_devices_name

    return cmd_dev_name


# 随机函数
def getRandom(iMin, iMax):
    return osRandom.randint(iMin, iMax)


# 延时
def setSleep(iMin, iMax=999):
    iRandom = iMin
    if iMax != 999:
        iRandom = getRandom(iMin, iMax)
    osSleep(iRandom)


# 点击
def tap(iX, iY):
    """[点击手势]
  [点击屏幕上某个点坐标]

  Args:
      iX ([int]): [点击的坐标x]
      iY ([int]): [点击的坐标y]
  """
    osPopen('adb %s shell input tap %d %d' % (get_devices_str(), iX, iY))
    return


# 滑动
def move(iStartX, iStartY, iEndX, iEndY, dura=800):
    """[滑动手势,从起点滑动到终点]

  Args:
      iStartX ([int]): [开始坐标x]
      iStartY ([int]): [开始坐标y]
      iEndX ([int]): [终点坐标x]
      iEndY ([int]): [终点坐标y]
      dura (int, optional): [滑动时长ms]. Defaults to 800ms.
  """
    osPopen('adb %s shell input swipe %d %d %d %d %d' % (get_devices_str(), iStartX, iStartY, iEndX, iEndY, dura))
    return


# 其它按键
def keyCode(number):
    osPopen('adb %s shell input keyevent %d' % (get_devices_str(), number))

#关闭手机屏幕，启动休眠.
def closeScreen():
    osPopen('adb %s shell input keyevent 26' % (get_devices_str()))

#关机
def closePhone():
    osPopen('adb %s shell reboot -p' % (get_devices_str()))

#重启
def rebootPhone():
    osPopen('adb %s reboot -p' % (get_devices_str()))

# 返回键
def backKey():
    """[返回键]
  """
    osPopen('adb %s shell input keyevent 4' % (get_devices_str()))
    return


# 调用app
def callApp(sVal):
    osPopen('adb %s shell am start -D -S -n %s' % (get_devices_str(), sVal))

# 调用app
def closeApp(sVal):
    osPopen('adb %s shell am force-stop %s' % (get_devices_str(), sVal))


def vmSize():
    sVmSize = osPopen('adb shell wm size').read()
    aVmSize = osRe.search(r'(\d+)x(\d+)', sVmSize)
    return {'w': aVmSize.group(1), 'h': aVmSize.group(2)}


# 设置屏亮度 最大值255
def screen_brightness(iLen=255):
    osPopen('adb %s shell settings put system screen_brightness %d ' % (get_devices_str(), iLen))


# 设置屏是否自动调节模式  isAuto: 1是， 0：否.
def screen_brightness_mod(isAuto=1):
    osPopen('adb %s shell settings put system screen_brightness_mode %d' % (get_devices_str(), isAuto))


# 点亮主屏
def ligtPhone():
    osPopen('adb %s shell input keyevent 224' % (get_devices_str()))


# 当前已连接设备
def getConnectedDevices():
    """[获取当前已连接的设备]

  Returns:
      [list]: [设备列表]
  """
    connected = []
    osPopen('adb devices > t.txt')
    with open('t.txt') as f:
        lines = f.read().splitlines()

    lines.remove(lines[-1])
    lines.remove(lines[0])
    for i in lines:
        a = str(i).partition('\tdevic')[0]
        connected.append(a)

    osOs.remove('t.txt')

    print(connected)
    try:
        return connected
    except:
        return


# 判断当前设备是否连接
def isConnected(deviceName):
    cmdRes = "404"
    cmdRes = getResponse('adb -s {} get-serialno'.format(deviceName))
    if cmdRes.find(deviceName) == 0:
        return True
    return False


# 获取当前屏宽
def grabScreenResolution():
    a = getResponse('adb %s shell dumpsys window | grep "mUnrestrictedScreen"' % get_devices_str())
    a = a.partition(") ")[2]
    a, b = a.split("x")
    return [int(a), int(b)]


# 获取命令执行结果
def getResponse(command):
    osOs.system('{} > tmp'.format(command))
    return open('tmp', 'r').read()


# 直接执行命令,是否需要超级管理员权限
def runCommand(command, forcesudo=False):
    if 'sudo' in command.lower():
        command = command.replace('sudo ', '')
    if forcesudo == True:
        osOs.system('sudo {}'.format(command))
    else:
        osOs.system('{}'.format(command))


# 获取当前快照
# 失败，有待进一步调试
def takeScreenshot(fileName=None):
    if fileName == None:
        screenshot = gb_devices_name + '.png'
    else:
        screenshot = fileName

    Command = "adb " + get_devices_str() + " shell screencap -p | sed 's/\r$//' > " + str(screenshot)
    runCommand(str(Command))
    return screenshot


def turnDownVolume():
    for i in range(10):
        runCommand('adb {} shell input keyevent 25'.format(get_devices_str()))


def clearCache(app):
    runCommand('adb {} shell pm clear {}'.format(get_devices_str(), app))


def forceClose(udid, app):
    runCommand('adb {} shell am force-stop {}'.format(get_devices_str(), app))


def startApplication(udid, app):
    runCommand("adb {} shell monkey -p {} -c android.intent.category.LAUNCHER 1".format(get_devices_str(), app))

def getAppMemInfo(app):
    runCommand("adb {} shell dumpsys meminfo {}".format(get_devices_str(), app))

def getAppCPUInfo(app):
    runCommand("adb {} shell dumpsys cpuinfo | grep {}".format(get_devices_str(), app))


#adb -s 4857d2bc shell dumpsys cpuinfo | grep com.ss.android.article.lite
#adb -s 4857d2bc shell top -n 1|find "com.ss.android.article.lite"

'''
----------------------------------------------------------------
下面是测试用例,仅供调试时使用.
'''


# test 用列
def test_tip():
    global gb_devices_name
    gb_devices_name = "e3656a1b"
    # tap(500,300)
    move(500, 600, 500, 300, 1000)
    return


def test_userDevcies():
    global gb_devices_name
    gb_devices_name = "e3656a1b"
    screen_brightness(100)


def test_NOuserDevcies():
    # global gb_devices_name
    # gb_devices_name = "-s e3656a1b"
    screen_brightness(100)

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

if __name__ == "__main__":
    # print('状态：{}'.format(isConnected("4857d2bc")))
    # print('状态：{}'.format(isConnected("1001")))

    # print('%s' % grabScreenResolution())
    # getResponse('adb -s 23123 shell pwd')
    # takeScreenshot('23123')
    # ligtPhone()
    pass
# test_userDevcies()
# test_NOuserDevcies()
# test_tip()
