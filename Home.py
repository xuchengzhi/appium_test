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
from Home import *
nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#读取config.ini
log_=ConfigParser()
log_.read("conf/logs_conf.ini")

cfg = ConfigParser()
cfg.read("conf/element_.ini")
shouye = cfg.options("shouye")
home_path=os.getcwd()
nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")

class Home_Action(object):
	"""docstring for Home_Action"""
	def __init__(self, arg):
		super(Home_Action, self).__init__()
		self.arg = arg
	def El_chuanjianzit(self):
		el_id_click(self.arg,cfg.get('shouye','el_createfont'))
	def El_geren(self):
		el_id_click(self.arg,cfg.get('shouye','el_personal'))
	def El_shouye(self):
		el_id_click(self.arg,cfg.get('shouye','el_home'))
	def El_xiaoxi(self):
		el_id_click(self.arg,cfg.get('shouye','el_messge'))
	def El_zitiye(self):
		el_id_click(self.arg,cfg.get('shouye','el_fonts'))
	def El_sosuo(self):
		el_id_click(self.arg,cfg.get('shouye','el_find'))
	def El_faxian(self):
		el_id_click(self.arg,cfg.get('shouye','el_discover'))
	def El_xieyi(self):
		el_id_click(self.arg,cfg.get('shouye','agreement'))

dirver = appium_start()
# print("qidong activity")
# dirver.wait_activity("com.handwriting.makefont/com.handwriting.makefont.personal.ActivityEditInfoChangeEmail.avtivity",10,1)
# print ("end")