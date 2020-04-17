# _*_ coding: utf-8 _*_
# @Author   : 廖大爷
# @time     : 2019/7/11 16:35
from selenium.webdriver import Remote
import time
from selenium import webdriver
#启动浏览器驱动
def browser():
    driver = webdriver.Chrome()
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get('http://127.0.0.1:8080/tc_web')
    time.sleep(3)
    dr.quit()