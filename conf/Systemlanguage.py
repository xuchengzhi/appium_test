#-*- coding:utf-8 -*-

__author__ = "xcz"
__version__ = "v1.0.1"

import os
import sys
import time
import platform
def set_utf():
	if platform.system()=="Windows":
		reload(sys)
		sys.setdefaultencoding("utf-8")
	else :
		reload(sys)
		sys.setdefaultencoding("utf-8")