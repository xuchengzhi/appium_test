#-*-coding:utf-8-*-

#引用包部分
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
import des
import json
import redis
import multiprocessing



from configparser import ConfigParser

# read config.ini
cfg = configParser()
cfg.read('config.ini')
cfg.get('login','user')
driver.find_element_by_id(cfg.get('login','user')).click()