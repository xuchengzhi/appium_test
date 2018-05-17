#-*-coding:utf-8-*-
import pyDes
import os
import sys
import base64

class DES():

#初始化key,iv

    def __init__(self,key,iv):
        self.iv=iv
        self.key=key
    #进行des加密
    def encrypt(self,data):

        k=pyDes.des(self.key,pyDes.CBC,self.iv,pad=None,padmode=pyDes.PAD_PKCS5)
        d=k.encrypt(data)
        d=base64.encodestring(d)
        return {"jiamijieguo":d}
    #解密
    def decrypt(self,data):
    	print data
        k=pyDes.des(self.key,pyDes.CBC,self.iv,pad=None,padmode=pyDes.PAD_PKCS5)
        data=base64.decodestring(data)
        d=k.decrypt(data)
       
        return {"jiamijieguo":d}

#该函数不需要key,iv
    def nokey(self,data):
        d=base64.encodestring(data)
        return d
    
        
ke='-1-h2,:+'
# ke='UITN25LM'
def run(num,ke='-1-h2,:+'):
	
	if num.isdigit():
		test=DES(ke,ke)
    	#调用class，传入key,iv
   		num1=test.encrypt(num).get('jiamijieguo').replace("=","-").replace('\n',"")#加密
   		# print num1
   		return num1
   		
   	else :
   		test=DES(ke,ke)
    	num2=test.decrypt(num.replace("-","="))#解密
    	# print num2
    	return num2
    	
    
    # for i in txt:
    #     ziti=i.replace('\n',"")[0:4]#读取TXT字体
    #     use=i.replace('\n',"")[4:]#读取TXT用户
    #     ziti=test.encrypt('3').get('jiamijieguo').replace("=","-").replace('\n',"")#输入加密字体id，也可传入TXT读取内容
    #     use=test.encrypt('3700').get('jiamijieguo').replace("=","-").replace('\n',"")#输入加密user id
    #     return{"z":ziti,"u":use}

# run("tlK7zEOQgJs-")