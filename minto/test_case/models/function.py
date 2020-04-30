# _*_ coding: utf-8 _*_
# @Author   : 廖大爷
# @time     : 2019/7/11 16:35
from selenium import webdriver
import os

#截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    file_path = base + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)




if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://localhost:80/tc_web")
    driver.maximize_window()
    insert_img(driver, 'denglu1.jpg')
    driver.quit()