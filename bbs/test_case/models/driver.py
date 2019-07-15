# _*_ coding: utf-8 _*_
# @Author   : 廖大爷
# @time     : 2019/7/11 16:35
from selenium.webdriver import Remote
import time
from selenium import webdriver
#启动浏览器驱动
def browser():
    driver = webdriver.Chrome()
    host = '127.0.0.1:4444'  #运行主机ip端口
    dc = {'borwserName':'Chrome'}  #指定浏览器
    # driver = Remote(command_executor='http://' + host + '/wd/hub',desired_capabilities=dc)
    return driver
if __name__ == '__main__':
    dr = browser()
    dr.get('https://www.baidu.com')
    # time.sleep(3)
    # dr.quit()