#-*-coding:utf-8-*-
import json  
import requests  
import time  
import os,sys
import shutil
import ssl
import random
import urllib
import urllib2
reload(sys)
sys.setdefaultencoding("utf-8")
agetname=["Safari/5.0 (TestiPhone 6SPLUS; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/6.0 MQQBrowser/5.6 Mobile/12A365 Safari/8536.25",
"Safari/5.0 (TestiPhone 5S; CPU iPhone OS 9_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/6.0 MQQBrowser/5.6 Mobile/12A365 Safari/8536.25",
"Safari/5.0 (TestiPhone 7PLUS; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/6.0 MQQBrowser/5.6 Mobile/12A365 Safari/8536.25",
]
header1={#"Host":"newlife.newaircloud.com:8087",
"User-Agent":random.choice(agetname),
"Accept":"application/json, text/javascript, */*; q=0.01",
"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding":"gzip, deflate",
"X-Requested-With":"XMLHttpRequest",
# "Referer":"http://newlife.newaircloud.com:8087/amucsite/act/applyApp.jsp?actid=100&tc=uc",
"Connection":"keep-alive"}


class Run():
	'''
	接口：处理http请求
	'''
	def url_run(self,arg1,method,header=header1,**dictArg):
		'''
		接口名称：发送http请求，参数名arg1：接口名称，参数名method：请求方式，参数**dictArg：请求内容(字典dict)
		'''
		self.arg1=arg1
		self.method=method
		if method=="post":
			print "接口名：{}为post请求".format(arg1)
			self.header=header
			data=dictArg
			post_data=urllib.urlencode(data)
			url=dictArg.get("url")
			ssl._create_default_https_context = ssl._create_unverified_context
			# req_ms=urllib2.Request(url=url,data=post_data,headers=header)
			try:
				# req=urllib2.urlopen(req_ms)
				req=urllib2.urlopen(url,post_data)
				result=req.read()
				# return {"result",result}
				
				return result
			except urllib2.URLError as cuowu:
				# print cuowu
				return "error"
		else :
			print "接口名：{},请求方式get".format(arg1)
			data=dictArg
			try:
				url=dictArg.get("url")
				print url
				print "="*100+"\n"
				req=urllib2.urlopen(url)
				return req.read()
			except Exception, e:
				print "get url Error"