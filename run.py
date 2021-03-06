#-*- coding:utf-8 -*-

__author__ = "xcz"
__version__ = "v1.0.1"

import os
import sys
import time
import unittest
from configparser import ConfigParser
from selenium import webdriver
from appium import webdriver
from conf.appium_config import appium_start
from common.unlock import unlocks
from common.utils import *
from Login import Login
import datetime
from common.Action import create_file
from Home import Home_Action
from CreateFont import El_chuangjianziti

nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
home_path=os.getcwd()

#读取config.ini
cfg = ConfigParser()
cfg.read("conf/element.ini")

sections = cfg.sections() 


def handle_page_return(driver,el):
    """
    当从下级页面返回到上级页面时,因元素无法定位或发生异常时,
    使用系统返回键返回，从而不影响后续case执行。
    """
    try:
        el_id_click(driver,el)
    except Exception as e:
        print(e)
        driver.keyevent(4)

class ProductInformation(unittest.TestCase):
    """
    TestCase: 
    Description: 
    """

    #@classmethod,在此类中只进行一次初始化和清理工作 
    @classmethod
    def setUpClass(self):
        self.driver = appium_start()

        screenshot(self.driver,"app_start")
        # self.driver.get_screenshot_as_file("ddd.png")
        # dev_=unlocks(self.driver)
        # if dev_.unlock() is True :
        #     print("right")
        #     MobileSwipe().swipe_right(self.driver)
        #     print("down")
        #     MobileSwipe().swipe_down(self.driver)
        #     for i in range(8,11):
        #         os.system("adb shell input keyevent {}".format(i))
        # time.sleep(2)
        # self.pg_home_nologin=(self.driver.page_source)

    def test_initial(self):
        if self.driver.current_activity != ".main.SplashActivity":
            self.driver.implicitly_wait(20)
        time.sleep(3)
        for n in range(5):
            self.swipe.swipe_down(self.driver)
    def test_Register(self):
        pass
    def test_chuangjianziti(self):
        Home_Action(self.driver).El_chuanjianzit()
        screenshot(self.driver,"zitirukou")
        time.sleep(1)
        El_chuangjianziti(self.driver).writefont("xuchengzhi")
    def test_login(self):
        Login(self.driver).phone_login("13912345678","112233")
        
        # if "方正手迹平台协议" not in pg_home_nologin :
        #     time.sleep(3)
        # el_id_click(self.driver,cfg.get('Home','El_MobileLogin'))
        # time.sleep(1)
        # el_id_click(self.driver,cfg.get('Login','El_Username'))
        # el_send_keys(self.driver,cfg.get('Login','El_Username'),"13912345678")
        # el_id_click(self.driver,cfg.get('Login','El_Passwd'))
        # el_send_keys(self.driver,cfg.get('Login','El_Passwd'),"112233")
        # el_id_click(self.driver,cfg.get('Login','El_Enter'))
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("app quit")

# texture Testcase
def suite_goods():
    tests = [
        # "test_initial", 
        "test_login",
        "test_chuangjianziti",
    ]
    return unittest.TestSuite(map(ProductInformation,tests))




if __name__ == "__main__":
    create_file(home_path).shanchu("screen")
    time.sleep(1)
    create_file(home_path).mk("screen")
    unittest.TextTestRunner(verbosity=2).run(suite_goods())
