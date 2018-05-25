#-*- coding:utf-8 -*-

# __author__ = "xcz"
# __version__ = "v1.0.1"

import os
import sys
import time
from conf.Systemlanguage import set_utf
set_utf()
from configparser import ConfigParser
cfg=ConfigParser()
cfg.read('conf/code.conf')
def changecode(msg):
	if type(msg) is unicode:
		return msg.encode("utf-8")