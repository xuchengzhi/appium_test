# -*- coding:utf-8 -*-

import os
import sys
import time
import re
from appium import webdriver
import platform
sys.path.append("..")
from conf.appium_config import appium_start


class unlocks(object):
	"""docstring for lock"""
	def __init__(self, arg):
		super(unlocks, self).__init__()
		self.arg = arg
		self.pg=self.arg.page_source
	def unlock(self):
		if "com.android.systemui" in str(self.pg) :
			return True
		else :
			return False

#test code
# driver = appium_start()
# test=unlocks(driver)
# print test.unlock()
#test code