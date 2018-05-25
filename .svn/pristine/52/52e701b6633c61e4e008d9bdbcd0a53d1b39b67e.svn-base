#-*- coding:utf-8 -*-

# __author__ = "xcz"
# __version__ = "v1.0.1"

import os
import sys
import time
import random
sys.path.append('..')
# from common.Action import *
from common.Changecodes import changecode
from conf.Systemlanguage import set_utf
set_utf()


def hanzi(num):
	f=open("conf/fontcode.txt").readlines()
	font_list=[]
	s = ""
	for i in range(num):
		code=random.randint(1,770)
		s+=f[code].decode("utf-8").replace("\n","")
	return s