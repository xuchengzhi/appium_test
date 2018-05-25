#-*-coding:utf-8-*-
import os
import sys
from common.Action import create_file
import shutil
home_path=os.getcwd()
def clear_():
	for files,root,dir in os.walk("."):
		for i in root:
			folder=i
			for files,root,dir in os.walk(folder):
				file_=dir
				for i in file_:
					try:
						if i.split(".")[1]=="pyc":
							os.remove(home_path+"/"+folder+"/"+str(i))
					except Exception, e:
						pass