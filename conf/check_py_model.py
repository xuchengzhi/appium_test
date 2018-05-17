#-*- coding:utf-8 -*-

__author__ = "xcz"
__version__ = "v1.0.1"

import os
import sys
def checkmodel():
	check="pip install -r requirements.txt"
	print("start install rely for python \n please wait")
	checkmod=os.system(check)
	f=open('conf/folderlist.txt')
	file_list=f.readlines()
	for name in file_list:
		if os.path.exists(name.split()[0]):
			print("%s file already" % name.split()[0])
		else :
			os.mkdir(name.split()[0])

	return True
# checkmodel()