#!/bin/bash
#设置手机屏幕亮度: 0~255  ./setBgl 135|171|158 100

#先设置为手动模式

list=("4857d2bc" "e3656a1b" "8514c020" "a790be09")

for((i=0;i<${#list[*]};i++));
do
    echo "/r/n>>>设备号: ${list[i]}"
    #adb -s ${list[i]} shell dumpsys battery set status 2
    adb -s ${list[i]} shell dumpsys battery
done
exit 0

adb -s 4857d2bc shell dumpsys battery
adb -s e3656a1b shell dumpsys battery
adb -s 8514c020 shell dumpsys battery
adb -s a790be09 shell dumpsys battery
exit 0

if [[ -z $1 ]]; 
then
    echo "> setBgl [0~255]  [135|171|158]"
    echo "> 参数2: 亮度值 , 参数1: 手机名"
    echo "> 使用示例: setBgl 50 135"
    exit 0
fi

dev_name=""

if [ $2 = "135" ]; 
then
    dev_name='-s 4857d2bc'
fi

if [ $2 = "171" ];
then 
    dev_name='-s e3656a1b'
fi

if [ $2 = "158" ]; 
then 
    dev_name='-s 8514c020'
fi

if [ $2 = "137" ]; 
then 
    dev_name='-s a790be09'
fi

if [ $2 = "" ]; 
then 
    adb $dev_name shell dumpsys battery
        
fi

# echo $1
# echo $2
# echo $dev_name
echo "> 执行中..."
echo "> 手机号:$2 ,设备号: $dev_name "


