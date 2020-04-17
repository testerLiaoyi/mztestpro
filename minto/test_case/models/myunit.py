# _*_ coding: utf-8 _*_
# @Author   : 廖大爷
# @time     : 2019/7/11 16:35
from selenium import webdriver
from .driver import browser
import unittest
import os

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()