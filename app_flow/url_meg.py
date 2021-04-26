#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# URL 合并

baseUrl = "https://img.gushi365.com/"
count = 0

#配置模块.
queueUrl= "img/cangshuyeye-"
picUlr= ".jpg"
max_count = 4


while count < max_count:
        count += 1

        outUrl = baseUrl + queueUrl + str(count) + picUlr
        print("%s" % outUrl)
        continue