#-*- coding:utf-8 -*-

__author__ = "xcz"
__version__ = "v1.0.1"

import os
import sys
def checkmodel():
	check="pip install -r requirements.txt"
	print("start install rely for python \n please wait")
	checkmod=os.system(check)

	return True