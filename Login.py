#-*- coding:utf-8 -*-

# __author__ = "xcz"
# __version__ = "v1.0.1"

import os
import sys
import time
from configparser import ConfigParser
from selenium import webdriver
from appium import webdriver
from conf.appium_config import appium_start
from common.unlock import unlocks
from common.utils import *
import datetime
from common.Action import *
nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#读取config.ini
log_=ConfigParser()
log_.read("conf/logs_conf.ini")

cfg = ConfigParser()
cfg.read("conf/element.ini")
home_path=os.getcwd()

nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")



class Login(object):
	"""docstring for Login"""
	def __init__(self, arg):
		super(Login, self).__init__()
		self.arg = arg
		create_file(home_path).mk(log_.get('log','path'))
		self.login_status=""
		dev_=unlocks(self.arg)
		if dev_.unlock() is True :
			print("unlocking...")
			screenshot(self.arg,"phonelock")
			print("right")
			MobileSwipe().swipe_right(self.arg)
			print("down")
			MobileSwipe().swipe_down(self.arg)
			for i in range(8,11):
				os.system("adb shell input keyevent {}".format(i))
		time.sleep(5)
		self.pg_home_nologin=(self.arg.page_source)
		f=open(home_path+"/"+log_.get('log','path')+"/nologin.xml","w")
		f.write(self.pg_home_nologin)
		f.close()
		self.pg_t=get_xml(home_path).test("nologin.xml").get("text_list")
		for i in self.pg_t:
			print i
		if '跳过' in self.pg_t:
			time.sleep(5)
			if "我的" in self.arg.page_source:
				self.login_status="True"
		elif '《方正手迹平台协议》' in self.pg_t:
			self.login_status="False"
			pass
		elif "我的" in self.pg_t:
			self.login_status="True"
			print " Already login "

			#com.handwriting.makefont/com.handwriting.makefont.main.ActivityMainCreate
		else:
			self.arg.start_activity("com.handwriting.makefont","com.handwriting.makefont.main.SplashActivity")
	def phone_login(self,username,passwd):
		t_n=1
		time.sleep(t_n)
		# self.arg.start_activity("com.handwriting.makefont","com.handwriting.makefont.main.SplashActivity")
		# while ("com.handwriting.makefont:id/splash_jump_rl" not in self.arg.page_source) or ("com.handwriting.makefont:id/phone_login_ll" not in self.arg.page_source):
		# 	time.sleep(t_n)
		# 	t_n+=1
			# self.pg_home_nologin=(self.arg.page_source)
			# print self.pg_home_nologin
			# self.arg.start_activity("com.handwriting.makefont","com.handwriting.makefont.main.SplashActivity")
			# wait_activity("com.handwriting.makefont/com.handwriting.makefont.main.SplashActivity",1,1)
		if self.login_status == "True":
			print " Already login"
			pass
		else :
			print "not login "
			time.sleep(2)
			screenshot(self.arg,"login")
			el_id_click(self.arg,cfg.get('Home','El_MobileLogin'))
			time.sleep(1)
			screenshot(self.arg,"phone_login_detail")
			el_id_click(self.arg,cfg.get('Login','El_Username'))
			el_send_keys(self.arg,cfg.get('Login','El_Username'),username)
			el_id_click(self.arg,cfg.get('Login','El_Passwd'))
			el_send_keys(self.arg,cfg.get('Login','El_Passwd'),passwd)
			screenshot(self.arg,"login_info_sucess")
			el_id_click(self.arg,cfg.get('Login','El_Enter'))
			time.sleep(2)
			screenshot(self.arg,"login_sucess")
			f=open(home_path+"/"+log_.get('log','path')+"/login_sucess.xml","w")
			f.write(self.arg.page_source)
			f.close()
			time.sleep(2)
			try:
				source_id = get_xml(home_path).test("login_sucess.xml")
				pg_text=source_id.get("text_list")
				if '【新版本的自白】' in pg_text:
					el_id_click(self.arg,"com.handwriting.makefont:id/dialog_font_close")
					screenshot(self.arg,"shouye")
			except Exception, e:
				print("read xml error")
				com.handwriting.makefont/com.handwriting.makefont.main.ActivityMainCreateFontListMine