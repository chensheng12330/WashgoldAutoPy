#!/usr/bin/python3
# coding=utf-8

import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET


# 通过元素定位,需要Android 4.0以上
class Element(object):
    # 初始化，获取系统临时文件存储目录，定义匹配数字模式
    def __init__(self):
        # self.tempFile = tempfile.gettempdir() # /var/folders/m0/dbkt2wx15cx93kws4djfcqd80000gn/T
        self.tempFile = "/tmp"
        self.pattern = re.compile(r"\d+")
        print(self.tempFile)

    # 获取当前Activity控件树
    def __uidump(self):
        os.popen("adb shell uiautomator dump /data/local/tmp/uidump.xml")
        os.popen("adb pull /data/local/tmp/uidump.xml " + self.tempFile)

    # 同属性单个元素，返回单个坐标元组
    def __element(self, attrib, name):
        self.__uidump()
        tree = ET.ElementTree(file=self.tempFile + "/uidump.xml")
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if elem.attrib[attrib] == name:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])

                return Xpoint, Ypoint

    # 同属性多个元素，返回坐标元组列表
    def __elements(self, attrib, name):
        list = []
        # self.__uidump()
        tree = ET.ElementTree(file=self.tempFile + "/uidump.xml")
        treeIter = tree.iter(tag="node")
        for elem in treeIter:
            if elem.attrib[attrib] == name:
                bounds = elem.attrib["bounds"]
                coord = self.pattern.findall(bounds)
                Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
                list.append((Xpoint, Ypoint))
        return list

    def init(self):
        self.__uidump()

    # 通过元素名称定位  usage: findElementByName(u"相机")
    def findElementByName(self, name):
        return self.__element("text", name)

    def findElementsByName(self, name):
        return self.__elements("text", name)

    # 通过元素类名定位  usage: findElementByClass("android.widget.TextView")
    def findElementByClass(self, className):
        return self.__element("class", className)

    def findElementsByClass(self, className):
        return self.__elements("class", className)

    # 通过元素的resource-id定位  usage: findElementsById("com.android.deskclock:id/imageview")
    def findElementById(self, id):
        return self.__element("resource-id", id)

    def findElementsById(self, id):
        return self.__elements("resource-id", id)