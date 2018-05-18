# -*- coding:utf-8 -*-

import os
import sys
import time
import re
from appium import webdriver
import platform
sys.path.append("..")
from conf.appium_config import appium_start
from conf.Systemlanguage import set_utf
set_utf()

class unlocks(object):
	"""docstring for lock"""
	def __init__(self, arg):
		super(unlocks, self).__init__()
		self.arg = arg
		self.pg=self.arg.page_source
	def unlock(self):
		s=u"com.android.systemui"
		ss=self.pg
		if s in ss :
			return True
		else :
			return False