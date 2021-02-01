#!/bin/bash
#查看屏幕

'''
scrcpy -s 设备ID 来连接使用指定的设备
关闭手机屏幕	scrcpy -S
限制画面分辨率	scrcpy -m 1024 (比如限制为 1024)
修改视频码率	scrcpy -b 4M (默认 8Mbps，改成 4Mbps)
裁剪画面	scrcpy -c 1224:1440:0:0
表示分辨率 1224x1440 并且偏移坐标为 (0,0)
多设备切换	scrcpy -s 设备ID (使用 adb devices 命令查看设备ID)
窗口置顶	scrcpy -T
显示触摸点击	scrcpy -t
在演示或录制教程时，可在画面上对应显示出点击动作
全屏显示	scrcpy -f
文件传输默认路径	scrcpy --push-target /你的/目录
将文件拖放到 scrcpy 可以传输文件，此命令指定默认保存目录
只读模式(仅显示不控制)	scrcpy -n
屏幕录像	scrcpy -r 视频文件名.mp4 或 .mkv
屏幕录像 (禁用电脑显示)	scrcpy -Nr 文件名.mkv
设置窗口标题	scrcpy --window-title "异次元好棒！"
'''

'''
Scrcpy 快捷键列表

全屏	MOD+f
向左旋转屏幕	MOD+← (左)
向右旋转屏幕	MOD+→ (右)
将窗口大小重置为1:1 (像素优先)	MOD+g
将窗口大小重置为消除黑边	MOD+w | 双击¹
点按 主屏幕	MOD+h | 点击鼠标中键
点按 返回	MOD+b | 点击鼠标右键²
点按 切换应用	MOD+s
点按 菜单 （解锁屏幕）	MOD+m
点按 音量+	MOD+↑ (up)
点按 音量-	MOD+↓ (down)
点按 电源	MOD+p
打开屏幕	点击鼠标右键²
关闭设备屏幕（但继续在电脑上显示）	MOD+o
打开设备屏幕	MOD+Shift+o
旋转设备屏幕	MOD+r
展开通知面板	MOD+n
展开快捷操作	MOD+Shift+n
复制到剪贴板³	MOD+c
剪切到剪贴板³	MOD+x
同步剪贴板并黏贴³	MOD+v
导入电脑剪贴板文本	MOD+Shift+v
打开/关闭FPS显示（在 stdout)	MOD+i
捏拉缩放	Ctrl+点按并移动鼠标



屏幕录像：
scrcpy -r file.mp4
scrcpy -Nr file.mp4

-b 1M
-m 800

scrcpy -s 8514c020 -S 关闭屏

'''


scrcpy -s 4857d2bc -b 1M -m 800

scrcpy -s e3656a1b -b 1M -m 800

scrcpy -s 8514c020 -b 1M -m 800


