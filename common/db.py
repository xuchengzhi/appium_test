#-*-coding:utf-8-*-

__author__ = "xcz"
__version__ = "v1.0.1"

#引用包部分
import os,sys
import json
import time
import datetime
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