from time import sleep
import unittest, random, sys
# sys.path.append("./models")
# sys.path.append("./page_obj")
from .models import myunit, function
from .page_obj.loginPage import login

class loginTest(myunit.MyTest):
    '''登录测试'''

    #测试用户登录
    def user_login_verify(self,username='',password=''):
        login(self.driver).user_login(username,password)

    def test_login1(self):
        """用户名密码登录为空"""
        self.user_login_verify()
        po = login(self.driver)