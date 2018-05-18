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
from conf.Systemlanguage import set_utf
set_utf()
from common.Changecodes import changecode


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
	def writefont(self,fontname,summary):
		el_id_click(self.arg,cfg.get('chuangjianrukou','el_writefont'))
		time.sleep(5)
		f=open(home_path+"/"+log_.get('log','path')+"/nologin.xml","w")
		f.write(self.arg.page_source)
		f.close()
		screenshot(self.arg,"writefont")
		el_id_click(self.arg,cfg.get("shouixieshezhi","El_xiayibu"))
		el_id_click(self.arg,cfg.get("shouixieshezhi","El_zitimingcheng"))
		f=open(home_path+"/"+log_.get('log','path')+"/tianxiezitimingcheng.xml","w")
		f.write(self.arg.page_source)
		f.close()
		time.sleep(3)
		screenshot(self.arg,"shuruzitiming")
		el_id_click(self.arg,cfg.get("shouixieshezhi","El_zitimingcheng"))
		el_send_keys(self.arg,cfg.get("shouixieshezhi","El_zitimingcheng"),fontname.decode("utf-8"))
		el_id_click(self.arg,cfg.get("shouixieshezhi","El_zitijianjie"))
		el_send_keys(self.arg,cfg.get("shouixieshezhi","El_zitijianjie"),summary.decode("utf-8"))
		el_id_click(self.arg,cfg.get("shouixieshezhi","El_100"))
		screenshot(self.arg,"shezhizitixinxi")
		el_id_click(self.arg,cfg.get("shouixieshezhi","El_kaishixiezi"))
		time.sleep(2)
		screenshot(self.arg,"kaishixiezi")
		time.sleep(2)
		f=open(home_path+"/"+log_.get('log','path')+"/chuangjianziti.xml","w")
		f.write(changecode(self.arg.page_source))
		f.close()
		pgs=(changecode(self.arg.page_source))
		print(type(pgs))
		print("*"*10)
		print(pgs)
		time.sleep(2)
		screenshot(self.arg,"huidaoshouye")
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