# -*- coding:utf-8 -*-
import os
import sys
import time
import re
from appium import webdriver
import platform
import datetime

_path=os.getcwd()

nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")

home_path = os.path.dirname(_path)

sys.path.append('..')
from common.mobile import get_serialno

#Read mobile deviceId
device_id = get_serialno()

# # Read mobile os Version
os_version = os.popen('adb -s {0} shell getprop ro.build.version.release'.format(device_id)).read().split()[0]

if platform.system()=="Windows":
    adb_devices_cmd="adb devices"
    appium_cmd="start cmd /K appium --no-reset".format(home_path)
    reload(sys)
    sys.setdefaultencoding("utf-8")
    def win_app_status():
        import win32com.client  
        WMI = win32com.client.GetObject('winmgmts:')  
        processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % ("node.exe"))  
        if len(processCodeCov) > 0:
            return True 
        else:  
            return False
elif platform.system()=="Linux":
    adb_devices_cmd="adb devices"
    appium_cmd="nuhup appium >/usr/local/logs/appium_{}.log 2>1 &".format(nowtime)
    def linux_appium_status():
        appium_ps="ps -aux | grep node"
        appium_list=os.popen(appium_ps).read().split()
        time.sleep(2)
        if "/usr/bin/appium" in appium_list:
            return True
        else :
            return False

else :
    adb_devices_cmd="adb devices"
    appium_cmd="nuhup appium >/usr/local/logs/appium_{}.log 2>1 &".format(nowtime)


def appium_start():
    if platform.system()=="Windows":
        if win_app_status() is True:
            print("Appium Already Start")
        else :
            os.popen(appium_cmd)
            t_n=1
            print("try start appium")
            while win_app_status() is False:
                time.sleep(t_n)
                sys.stdout.write(">")
                sys.stdout.flush()
                t_n+=1
                time.sleep(t_n)
            print("\n")
            print("Appium is Start")
    else :
        if linux_appium_status() is True :
            print("Appium  Already Start")
        else :
            t_n=1
            print("try start appium")
            while linux_appium_status() is False:
                time.sleep(t_n)
                sys.stdout.write(">")
                sys.stdout.flush()
                t_n+=1
                time.sleep(t_n)
            print("\n")
            print("Appium is Start")

    config = {
        'platformName':'Android',
        'platformVersion':os_version,
        'deviceName':device_id,
        'appPackage':'com.handwriting.makefont',
        'appActivity':'.main.SplashActivity',
        'app':_path+'/apk/shoujizaozi.apk',
        'newCommandTimeout':10,    
        'automationName': 'Appium',
        'unicodeKeyboard':True,
        'autoAcceptAlerts':True,
        'resetKeyboard':True}
    return webdriver.Remote('http://localhost:4723/wd/hub', config)