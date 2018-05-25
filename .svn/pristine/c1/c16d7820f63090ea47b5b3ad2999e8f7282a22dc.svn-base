# -*- coding:utf-8 -*-

import os
import sys
import time
import re
from appium import webdriver

sys.path.append("..")
#用于解决多个手机连接问题
from common.mobile import get_serialno

#Read mobile deviceId
device_id = get_serialno()

#Read mobile os Version
os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read()
    
def appium_start():
    config = {
        'platformName':'Android',                      #平台
        'platformVersion':os_version,                  #系统版本
        'deviceName':device_id,                        #测试设备ID
        # 'appPackage':'com.jiuai',
        # 'appActivity':'.activity.MainActivity',
        'app':'/Users/xiaohutu/GitHub/Android-Test/com.jiuai.apk',      #apk路径
        #'app':'D:\com.jiuai.apk',
        'newCommandTimeout':30,    
        'automationName': 'Appium',
        'unicodeKeyboard':True,                         #编码,可解决中文输入问题
        'resetKeyboard':True}
    return  webdriver.Remote('http://localhost:4723/wd/hub', config)

作者：一直小鱼
链接：https://www.jianshu.com/p/8b06f76be7e6
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。