#-*-coding:utf-8-*-

#第三方引用包部分
import os,sys
import urllib
import urllib2
import ssl
import random
import base64;
import time;
import hashlib
import StringIO
import pycurl
import cookielib
import datetime
import json
import redis
import multiprocessing
import configparser
import redis
import re
import subprocess
import commands

#本地引用
from Api import Run
from handwriting_api import *
# import des
reload(sys)
sys.setdefaultencoding("utf-8")

t_time=str(int(round(time.time() * 1000)))
riqi='%Y-%m-%d %X'
time_now=time.localtime()
stat_time= time.strftime(riqi,time_now)
start_time=datetime.datetime.now()
app_sys="T_iOS11.1"

cf = configparser.ConfigParser()
cf.read("./conf/config.ini")
pool = redis.ConnectionPool(host=cf.get("config","host"), port=6379, db=0,password=cf.get("config","Authentication"))
redis_con = redis.Redis(connection_pool=pool)
class works(object):
	"""docstring for works

	   作品相关接口

	   anthor: xuchengzhi
	"""

	def __init__(self,arg):
		self.arg=arg
	def create_works(self,url,user_id):
		'''
		接口名称：创建作品

		加密规则： md5(user_id + md5(sys + t))
		'''
		data={}
		data["t"]=t_time
		data["token"]=Font_api.get_md5(user_id+Font_api.get_md5(app_sys+str(t_time)).get("token")).get("token")
		data["sys"]=app_sys
		data["url"]="http://{}/mobile.php?c=Sjproduction&a=s_production".format(url)
		data["user_id"]=user_id
		data["p_id"]=""
		req=Run.url_run("create_works","post",**data)
		req=json.loads(req)
		if "id" in req:
			return req.get("id")
		else :
			sys.exit("创建作品失败")
			

		 
	def update_works(self,url,user_id,p_id,s_name,s_author,s_size,model_id,ziku_list):
		'''
		接口名称：更新作品

		加密规则：md5($user_id . md5($sys . $t) . $p_id);
		'''
		data={}
		data["url"]="http://{}/mobile.php/Sjproduction/update_production".format(url)
		data["t"]=t_time
		data["token"]=Font_api.get_md5(user_id+Font_api.get_md5(app_sys+str(t_time)).get("token")+p_id).get("token")
		data["s_name"]=s_name
		data["s_author"]=s_author
		data["model_id"]=model_id
		data["s_size"]=s_size
		data["ziku_list"]=ziku_list
		data["sys"]=app_sys
		data["user_id"]=user_id
		data["production_id"]=p_id
		req=Run.url_run("update_works","post",**data)
	def get_product_list(self,url,user_id,target_id):
		'''
		接口名称：获取作品列表
		
		user_id 当前登录用户id

		target_id 个人主页的用户id，如果是进入自己的个人主页和user_id一样

		加密规则为： md5($t . md5($uid . $target_id) . $sys);
		'''
		data={}
		data["url"]="http://{}/mobile.php/Homepage/get_production".format(url)
		data["user_id"]=user_id
		data["target_id"]=target_id
		data["t"]=t_time
		data["token"]=Font_api.get_md5(str(t_time)+Font_api.get_md5(user_id+target_id).get("token")+app_sys).get("token")
		data["sys"]=app_sys
		data["last_proid"]=""
		req=Run.url_run("get_product_list","post",**data)
		print(req)
	def report_works(self,url,target_id,user_id,product_id):
		'''
		接口： 举报作品
		
		target_id 被举报人id

		user_id 举报人id

		product_id 作品id

		sys 当前操作系统

		t 时间戳

		token 加密后的字符串

		加密方式：md5($t .$product_id. md5($user_id . $target_id) . $sys)

		anthor ：xuchengzhi
		'''
		data={}
		data["url"]="http://hwdev.xiezixiansheng.com/mobile.php/Sjproduction/report_prodution"
		data["target_id"]=target_id
		data["user_id"]=user_id
		data["product_id"]=product_id
		data["sys"]=app_sys
		data["t"]=t_time
		data["token"]=Font_api.get_md5(str(t_time)+product_id+Font_api.get_md5(user_id+target_id).get("token")+app_sys).get("token")
		req=Run.url_run("report_works","post",**data)
		print(req)
	def huoqumoban():
		'''
		接口：获取模板 

		参数1: sys 操作系统

		参数2: t 时间戳

		参数3: page 默认第一页,展示10页

		参数4: token 加密后的字符串

		加密规则： md5(g_model . md5($sys . $t) );

		'''
		data={}
		data["url"]="http://hwdev.xiezixiansheng.com/mobile.php/Sjproduction/g_model"
		data["sys"]=app_sys
		data["t"]=t_time
		data["token"]=Font_api.get_md5("g_model"+Font_api.get_md5(app_sys+str(t_time)).get("token")).get("token")
		data["page"]=page
		req=Run.url_run("huoqumoban","get",**data)
	def del_works(self,url,production_id,user_id):
		'''
		方法：删除作品

		加密规则： $tokenStr = md5($user_id . md5($sys . $t) . $production_id);

		production_id：作品id、user_id：用户id、t：时间戳、sys：系统、token：加密串
		'''
		data={}
		data["url"]="http://{}/mobile.php/Sjproduction/delete_production".format(url)
		data["production_id"]=production_id
		data["user_id"]=user_id
		data["t"]=t_time
		data["sys"]=app_sys
		data["token"]=Font_api.get_md5(user_id+Font_api.get_md5(app_sys+str(t_time)).get("token")+production_id).get("token")
		req=Run.url_run("del_works","post",**data)
	def works_detail(self,url,production_id,user_id):
		'''
			方法：作品详情

			加密规则： $tokenStr = md5($user_id . md5($sys . $t) . $production_id);

			production_id作品id,user_id用户id,t时间戳,sys系统,token加密串
		'''
		data={}
		data["url"]="http://{}/mobile.php/Sjproduction/production_detail".format(url)
		data["production_id"]=production_id
		data["user_id"]=user_id
		data["t"]=t_time
		data["sys"]=app_sys
		data["token"]=Font_api.get_md5(user_id+Font_api.get_md5(app_sys+str(t_time)).get("token")+production_id).get("token")
		req=Run.url_run("works_detail","post",**data)
		print(req)
	def works_likes(self,url,production_id,user_id):
		'''
		加密规则为： md5($production_id . md5($user_id . $sys) . $t);
		production_id 作品id,user_id 用户id,sys 当前操作系统,t 时间戳,token 加密后的字符串
		'''
		data={}
		data["url"]="http://{}/mobile.php/Sjproduction/zan_production".format(url)
		data["production_id"]=production_id
		data["user_id"]=user_id
		data["sys"]=app_sys
		data["t"]=t_time
		data["token"]=Font_api.get_md5(production_id+Font_api.get_md5(user_id+app_sys).get("token")+t_time).get("token")
		req=Run.url_run("works_likes","post",**data)
		print(req)


class redis_(object):
	"""docstring for redis_"""
	def __init__(self, arg):
		super(redis_, self).__init__()
		self.arg = arg
	def getConfigValue(self, name):
	    value = cf.get("config",name)
	    return value
	def redis_select(self,key_,type=False):
		msg=[]
		redis_keys=redis_con.keys()
		regex = re.compile(key_)
		self.redis_keys=redis_keys
		for i in self.redis_keys:
			match = regex.search(i)
			if match:
				msg.append(i)
			elif type==True:
				print("{}是{}类型".format(i,redis_con.type(i)))
		# try:
		# 	assert("zikuinfo_145462_count" in msg)
		# 	print("断言成功")
		# except Exception, e:
		# 	print("断言失败")

class Test_anything:
	"""docstring for Test_anything"""
	# def __init__(self, arg):
	# 	super(Test_anything, self).__init__()
	# 	self.arg = arg
	def sql(self,sqls):
		import sqlite3
		conn=sqlite3.connect('./DataBase/databasetest.db')
		sql=conn.cursor()
		delete='drop table docs'
		create_table="create table docs (id INTEGER PRIMARY KEY AUTOINCREMENT,urls text)"
		create_db="create databases Test"
		#创建一个表
		sql.execute(sqls)
		
		# sql.execute()
		#往表格插入一行数据
		num=0
		link='www.baidu.com'
		# sql.execute('insert into docs values (?,?)',(num,link))
		# sql.execute(delete)
		#查询表格内容
		# sql.execute('select * from docs')
		#得到查询结果
		# result=sql.fetchall()
		# print(type(result),result)
		conn.commit()
		conn.close()
	def android_con(self):
		# cmds="adb -s 127.0.0.1:21503 logcat com.tencent.mobileqq"
		cmds="tasklist | findstr \"MEmu*\""# 
		cmd_port_check='netstat -aon | findstr \"6804\"'
		re=os.popen(cmds)
		# result=re.read().splitlines()
		# sql_=Test_anything()
		for i in re:
			s="".join(i)
			print(s.split())
			ss=os.popen('netstat -aon | findstr \"{}\"'.format(s.split()[1]))
			for i in ss:
				sss=os.popen('adb connect {}'.format(i.split()[1]))
		os.system("adb devices")

		# # 	time.sleep(1)
			# try:
			# 	sql_.sql('insert into docs (\'urls\') values(\'{}\')'.format(i))
			# except Exception, e:
			# 	print("insert db error")
		# result.close()
	def start_app(self):
		print("start app")
		os.system("C:\\Program Files\\Microvirt\\MEmu\\MEmu.exe")
if __name__ == '__main__':
	url_test="hwdev.xiezixiansheng.com"
	shoujizaozi_api=works("null")
	Redis_=redis_(cf)
	Run=Run()
	user_id_list=[3621,3623,3632,3637,3658,3661,3665,3667,3668]
	user_id="2409"
	zuopin_id="26"
	Test=Test_anything()
	# Test.sql('insert into docs (\'urls\') values(\'ddaff\')')
	Test.start_app()
	# shoujizaozi_api.works_detail(url_test,user_id,"19")
	# for i in user_id_list:
		# shoujizaozi_api.works_likes(url_test,zuopin_id,str(i))
	# Redis_.redis_select("2409",True)
	# zuopin_id=shoujizaozi_api.create_works(url_test,"2409")
	# shoujizaozi_api.update_works(url_test,"2409",zuopin_id,"今天天气不错a","阿卜杜拉.二狗子","45","1","2564")
	# shoujizaozi_api.report_works(url_test,"2409","3621","20")
	# shoujizaozi_api.get_product_list(url_test,"3621","2409")
	# handwriting_api.recommend_list(url_test,"2409","")