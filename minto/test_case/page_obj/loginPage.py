from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
class login(Page):
    '''
    用户登录页
    '''

    url = '/'

    login_username_loc = (By.ID,"u34_input")
    login_password_loc = (By.ID,"u35_input")
    login_button_loc = (By.ID,"loginBut")
    #登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)
    #登录密码
    def login_password(self, password):
        self.find_element(*self.login_username_loc).send_keys(password)
    #登录按钮
    def login_button(self):
        self.find_element(self.login_button_loc).click()
    #定义统一登录入口
    def user_login(self, username="system", password="123456"):
        '''获取的用户名密码登录'''
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)
    error_hint_loc = (By.ID, "errShow")
    user_login_success_loc = (By.title, "")
    #错误提示
    def error_hint(self):
        return self.find_element()
    #登录成功title
