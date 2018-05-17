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
# print cfg.sections()
shouye = cfg.options("chuangjianrukou")
# print shouye
home_path=os.getcwd()
nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
class El_chuangjianziti(object):
	"""docstring for chuangjianziti"""
	def __init__(self, arg):
		super(El_chuangjianziti, self).__init__()
		self.arg = arg
	def writefont(self,fontname):
		el_id_click(self.arg,cfg.get('chuangjianrukou','el_writefont'))
		time.sleep(5)
		f=open(home_path+"/"+log_.get('log','path')+"/nologin.xml","w")
		f.write(self.arg.page_source)
		f.close()
		
		screenshot(self.arg,"writefont")
	def camrefont_pen(self,fontname):
		el_id_click(self.arg,cfg.get('chuangjianrukou','el_camerafont2'))
		time.sleep(5)
		print(self.arg.page_source)
		screenshot(self.arg,"camrefont_pen")
		
	def camrefont_brush(self,fontname):
		el_id_click(self.arg,cfg.get('chuangjianrukou','el_camerafont1'))
		time.sleep(5)
		print(self.arg.page_source)
		screenshot(self.arg,"camrefont_brush")
		
	def works(self):
		el_id_click(self.arg,cfg.get('chuangjianrukou','el_works'))
		time.sleep(5)
		print(self.arg.page_source)
		screenshot(self.arg,"works")