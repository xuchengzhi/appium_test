#-*- coding:utf-8 -*-

__author__ = "xcz"
__version__ = "v1.0.1"

import os
import sys
import time
import unittest
from configparser import ConfigParser
from selenium import webdriver
from appium import webdriver
from conf.appium_config import appium_start
from common.unlock import unlocks
from common.utils import *