#-*-coding:utf-8-*-

__author__ = "xcz"
__version__ = "v1.0.1"

#引用包部分
import os,sys
import json
import time
import datetime
import appium
import unittest
import platform  
import tempfile  
import shutil
from appium import webdriver
# from PIL import Image  
import sqlite3
import subprocess
import platform
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

nowtime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
homepath=os.getcwd()


def check_exsit(process_name):  
	import win32com.client  
	WMI = win32com.client.GetObject('winmgmts:')  
	processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)  
	if len(processCodeCov) > 0:
		print '%s is exists' % process_name 
		return True 
	else:  
		print '%s is not exists' % process_name
		return False
		

#get adb devices 
'''
	Windows windows
	Linux linux
	Darwin Mac
'''
if platform.system()=="Windows":
	adb_devices_cmd="adb devices"
	appium_cmd="start cmd /K appium  >>{}/logs/appium.log".format(homepath)
	appium_list=check_exsit('node.exe')
	if appium_list is True:
		print("ok")
	reload(sys)
	sys.setdefaultencoding("utf-8")
elif platform.system()=="Linux":
	adb_devices_cmd="adb devices"
	appium_list="ps -aux | grep node"
	appium_cmd="nuhup appium >/usr/local/logs/appium_{}.log 2>1 &".format(nowtime)
	print(appium_cmd)
else :
	adb_devices_cmd="adb devices"
	appium_cmd="nuhup appium >/usr/local/logs/appium_{}.log 2>1 &".format(nowtime)

android_sys=os.popen("adb shell getprop ro.build.version.release").read().splitlines()
wechat_login="com.handwriting.makefont:id/weixin_login_iv"
phone_login="com.handwriting.makefont:id/phone_login_iv"
qq_login_iv="com.handwriting.makefont:id/qq_login_iv"
phone_num="id/login_phone_num_et"
phone_pwd="id/login_pwd_num_et"
login_button="id/login_ensure_tv"



def get_process_count(imagename):
	p = os.popen('tasklist /FI "IMAGENAME eq %s"' % imagename)
	return p.read().count(imagename)


class App(object):
	"""docstring for App"""
	def __init__(self, arg):
		super(App, self).__init__()	
		
		if get_process_count("node.exe")==1:
			print("appium alread start")
		else :
			try:
				print("start appium")
				os.system(appium_cmd)

			except Exception, e:
				print(e)
				sys.exit("appium start fail")
		time.sleep(2)
		dev=os.popen(adb_devices_cmd).read().splitlines()[1].split()
		print dev
		try:
			if dev[1].index("device")!=0 :
				print("online devices:{}".format(dev[1]))
		except Exception, e:
			sys.exit("device not online")
		self.arg = arg
		self.arg['capability']='appium'
		self.arg['platformName'] = 'Android'
		self.arg['platformVersion'] = android_sys[0]
		self.arg['deviceName'] = dev[0]
		self.arg['appPackage'] = 'com.handwriting.makefont'
		self.arg['appActivity'] = '.main.SplashActivity'
		self.arg['app'] = homepath+'/apk/shoujizaozi.apk'
		self.arg['autoLaunch']='True'
		self.arg['automationName']='Uiautomator2'
		self.arg['noReset'] = 'True'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.arg)
		self.driver.wait_activity('.main.SplashActivity',5,2)
		self.x = self.driver.get_window_size()['width']
		self.y = self.driver.get_window_size()['height']

	def __setitem__(self, k, v):
		self.k = v
	def __str__(self):
		return "name:%s, %s" % (self.name, self.k)

	def run(self):
		try:
			print("app start")
		except Exception, e:
			sys.exit("app error")
		
		self.driver.get_screenshot_as_png()
		time.sleep(5)

	def phone_login(self):
		sql_=sql()
		sql_.select("select * from appium_logs")
		sys_cmd=system_cmd()
		c_id=self.driver.find_element_by_id
		# self.driver.swipe(79, 139, 0, 0, 500)
		pg_home_nologin=(self.driver.page_source)
		c_id("com.handwriting.makefont:id/phone_login_iv").click()
		pg_login=(self.driver.page_source)
		c_id("com.handwriting.makefont:id/login_phone_num_et").click()
		c_id("com.handwriting.makefont:id/login_phone_num_et").send_keys("13912345678")
		c_id("com.handwriting.makefont:id/login_pwd_num_et").click()
		c_id("com.handwriting.makefont:id/login_pwd_num_et").send_keys("123456")
		c_id("com.handwriting.makefont:id/login_ensure_tv").click()
		login_re_pg=(self.driver.page_source)
		try:
			toast_loc = ("xpath", ".//*[contains(@text,'用户名或密码错误')]")
			t = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
			if t.text =="用户名或密码错误":
				print("input password retry")
				print self.driver.find_elements_by_accessibilityid("请输入手机号码").text
				c_id("com.handwriting.makefont:id/login_pwd_num_et").click()
				c_id("com.handwriting.makefont:id/login_pwd_num_et").send_keys("112233")
				c_id("com.handwriting.makefont:id/login_ensure_tv").click()
				time.sleep(1)
				print self.driver.current_context
				print self.driver.activate_ime_engine
				print self.driver.app_strings
				print self.driver.capabilities
				print self.driver.contexts
				print self.driver.app_strings
				print self.driver.current_activity
				home_pg=(self.driver.page_source)
				# print home_pg
				# toast_loc = ("xpath", ".//*[contains(@text,'用户名或密码错误')]")
				# t = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))
			else :
				print driver.current_context
				print driver.activate_ime_engine
				print driver.app_strings
				print driver.capabilities
				print driver.contexts
				print driver.app_strings
				print driver.current_activity
				return False
				# self.driver.start_activity("com.handwriting.makefont",".main.SplashActivity")
		except Exception, e:
			return False
		
		# print sys_cmd.is_toast_exist(self.driver, "再按一次退出")
	def app_quit(self):
		self.driver.quit()
	def wait_activity(self, activity, timeout, interval=1):
		print("fgdgdf")
		try:
			WebDriverWait(self, timeout, interval).until(
				lambda d: d.current_activity == activity)
			return True
		except TimeoutException:
			print("time out")
			return False
class system_cmd():
	def is_toast_exist(driver,text,timeout=30,poll_frequency=0.5):
		try:
			toast_loc = ("xpath", ".//*[contains(@text,'%s')]"%text)
			WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
			return True
		except:
			return False
class sql():
	"""docstring for sql"""
	def run(self,sqls):
		
		conn=sqlite3.connect('./DataBase/AppiumDataBase.db')
		sql=conn.cursor()
		delete='drop table docs'
		create_table="create table docs (id INTEGER PRIMARY KEY AUTOINCREMENT,urls text)"
		create_db="create databases Test"
		#创建一个表
		sql.execute(sqls)
		# sql.execute()
		#往表格插入一行数据
		num=0
		# sql.execute('insert into docs values (?,?)',(num,link))
		# sql.execute(delete)
		#查询表格内容
		# sql.execute('select * from docs')
		#得到查询结果
		# result=sql.fetchall()
		# print(type(result),result)
		conn.commit()
		conn.close()
	def select(self,sqls):
		conn=sqlite3.connect('./DataBase/AppiumDataBase.db')
		sql=conn.cursor()
		sql.execute(sqls)
		result=sql.fetchall()
		print("sql")
		print(result)
# if __name__ == '__main__':
# 	desired_caps = {}
# 	sql_=sql()
# 	try:
# 		sql_.run("create table appium_logs (id INTEGER PRIMARY KEY AUTOINCREMENT,logs text,time text)")
# 	except Exception, e:
# 		print(e)
# 	app=App(desired_caps)
# 	app.run()
# 	app.phone_login()
# 	# if app.phone_login()=False:
# 	# 	app.wait_activity(".main.SplashActivity",10)
# 	app.app_quit()
# 	os.popen("taskkill /im node.exe /F")
# 	os.system("taskkill /im cmd.exe /F")
# 	sys.exit("complete")
# import usb


# busses = usb.busses()

# for bus in busses:
# 	devices = bus.devices
# 	for dev in devices:
# 		for config in dev.configurations:
# 			for intf in config.interfaces:
# 				for alt in intf:
# 					print " --------alt.interfaceClass:",alt.interfaceClass
# 					if alt.interfaceClass == 3:
# 						print 'hahhaahhaah'
# 						cmd = 'sudo rmmod psmouse'
# 						os.system(cmd)