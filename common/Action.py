# -*- coding:utf-8 -*

__author__ = "xcz"
__version__ = "v1.0.1"

import os
import sys
import unittest
from time import sleep
import datetime
import shutil
from configparser import ConfigParser



_path=os.getcwd()
home_path = os.path.dirname(_path)

nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")

log_A=ConfigParser()
log_A.read("../conf/logs_conf.ini")



nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
class create_file(object):
	"""docstring for Move"""
	def __init__(self, arg):
		super(create_file, self).__init__()
		self.arg = arg
	def mk(self,name):
		file_path=self.arg+"/"+name
		print(file_path)
		if os.path.exists(file_path):
			print("file is alredy")
		else :
			print("crteat {}".format(file_path))
			os.mkdir(file_path)
	def shanchu(self,name):
		file_path=self.arg+"/"+name
		try:
			shutil.rmtree(file_path)
		except Exception, e:
			print("delete file eror")
class get_xml(object):
	"""docstring for get_xml"""
	def __init__(self, arg):
		super(get_xml, self).__init__()
		self.arg = arg
	def test(self,file_):
		from xml.dom.minidom import parse
		import xml.dom.minidom
		print home_path
		xmlfile=_path+"/app_xml/"+file_

		resource_list = []
		text_list=[]
		# 使用minidom解析器打开 XML 文档
		DOMTree = xml.dom.minidom.parse(xmlfile)
		collection = DOMTree.documentElement
		if collection.hasAttribute("rotation"):
		   print "Root element : %s" % collection.getAttribute("rotation")
		 
		# 在集合中获取所有电影
		tag_list=["android.widget.TextView","android.widget.FrameLayout","android.widget.ImageView","android.widget.RelativeLayout","android.widget.TextView","android.widget.Button","android.view.View"]
		for i in tag_list:
			print "*****{}*****".format(i)
			movies = collection.getElementsByTagName(i)
			for tag_text in movies:
				if tag_text.hasAttribute("resource-id"):
					resource_id=tag_text.getAttribute("resource-id")
					text_ = tag_text.getAttribute("text")
					# print "text: %s" % (text_)
					# print "resource_id: %s" % resource_id
					lei = tag_text.getAttribute("class")
					# print "lei: %s" % lei
					package = tag_text.getAttribute("package")
					# print "package: %s" % package
					bounds = tag_text.getAttribute("bounds")
					# print "bounds: %s" % bounds
					index = tag_text.getAttribute("index")
					# print "index: %s" % index
					resource_list.append(resource_id)
					text_list.append(text_)
		return {"resource_id":resource_list,"text_list":text_list}
