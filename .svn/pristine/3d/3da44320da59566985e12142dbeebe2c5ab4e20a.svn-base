#coding=utf-8
import os
import sys
import time
import datetime
import appium
import unittest
import platform  
import tempfile  
import shutil
import AppiumExtend
# from extend import Appium_Extend  
from appium import webdriver
from PIL import Image  


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:21503'
desired_caps['appPackage'] = 'com.handwriting.makefont'
desired_caps['appActivity'] = '.main.SplashActivity'
desired_caps['app'] = 'C:\\Users\\FD_XU\\Desktop\\apk\\shoujizaozi-test.apk'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
c_id=driver.find_element_by_id
# extend = AppiumExtend(driver)
print "启动客户端"
# driver.launch_app()

'''
	底部导航：
	我的字体 id/layout_main_tab_create
	发现 id/layout_main_tab_fontlib
	新建字体 id/layout_main_tab_
	消息 id/layout_main_tab_msg
	我的 id/layout_main_tab_mine


'''

pk="com.handwriting.makefont"
time.sleep(10)
#activity
driver.wait_activity('.main.SplashActivity',5,2)
wechat_login="com.handwriting.makefont:id/weixin_login_iv"
phone_login="com.handwriting.makefont:id/phone_login_iv"
qq_login_iv="com.handwriting.makefont:id/qq_login_iv"
#id
phone_num="id/login_phone_num_et"
phone_pwd="id/login_pwd_num_et"
login_button="id/login_ensure_tv"

# sreach_window=browser.current_window_handle
#点击手机登录
class handwriting(object):

	"""docstring for handwriting"""
	def __init__(self, arg):
		super(handwriting, self).__init__()
		self.arg = arg
	def phone_login(self,usr_name,pwd):
		print usr_name
		print pwd
		self.usr_name=usr_name
		self.pwd=pwd
		print pk+phone_num
		c_id("com.handwriting.makefont:id/login_phone_num_et").click()
		c_id("com.handwriting.makefont:id/login_phone_num_et").send_keys(usr_name)
		c_id("com.handwriting.makefont:id/login_pwd_num_et").click()
		c_id("com.handwriting.makefont:id/login_pwd_num_et").send_keys(pwd)
		c_id("com.handwriting.makefont:id/login_ensure_tv").click()
	def wechat_login(self):
		driver.find_element_by_id("com.handwriting.makefont:id/weixin_login_iv").click()
		time.sleep(3)
	def qq_login_iv(self):
		driver.find_element_by_id().click()
	def create_photo(self):
		
	



# def phone_login():
	
# 	print "进行手机号登录"
	
# 	print "输入手机号"
# 	driver.find_element_by_id("com.handwriting.makefont:id/login_phone_num_et").send_keys("13888888892")#输入手机号
# 	time.sleep(1)
# 	driver.find_element_by_id("com.handwriting.makefont:").click()
# 	time.sleep(1)
# 	print "输入密码"
# 	driver.find_element_by_id("com.handwriting.makefont:id/login_pwd_num_et").send_keys("112233")#输入密码
# 	time.sleep(1)
# 	print "点击登录"
# 	dianji=driver.find_element_by_id("com.handwriting.makefont:id/login_ensure_tv").click()
# 	print driver.current_context
# 	print driver.activate_ime_engine
# 	print driver.app_strings
# 	print driver.capabilities
# 	print driver.contexts
# 	print driver.app_strings
# 	print driver.current_activity
# 	time.sleep(10)
# 	driver.start_activity("com.handwriting.makefont", ".settings.myfonts.ActivityFonts")
# 	print driver.current_activity
# 	time.sleep(10)
# 	driver.start_activity("com.handwriting.makefont", ".main.ActivityLoading")
# 	print driver.current_activity
# 	time.sleep(10)
# 	driver.start_activity("com.handwriting.makefont", ".personal.ActivityChangeTel")
# 	print driver.current_activity
	
# 	time.sleep(10)
# 	driver.start_activity("com.handwriting.makefont", ".settings.ActivityFeedBack")
# 	print driver.current_activity
# 	print "2"
# 	time.sleep(10)
# 	driver.start_activity("com.handwriting.makefont", ".settings.ActivitySettingsAboutUs")
# 	print driver.current_activity
# 	print "3"
# 	time.sleep(10)
# 	driver.start_activity("com.handwriting.makefont", ".creator.write.ActivityPersonalFontCreatePreview")
# 	print driver.current_activity
# 	print "4"
# 	time.sleep(10)
# 	driver.start_activity("com.handwriting.makefont", ".creator.write.ActivityPersonalFontCreateFontStyle")
# 	print driver.current_activity
# 	print "5"
# 	time.sleep(10)
# 	driver.start_activity("com.handwriting.makefont", ".login.ActivityRegister")
# 	print driver.current_activity
# 	time.sleep(10)




	


# sh=driver.find_element_by_name('手机登录')


handwriting=handwriting(phone_login)
if __name__ == '__main__':

	handwriting.phone_login(13888888892,112233)
	driver.quit()