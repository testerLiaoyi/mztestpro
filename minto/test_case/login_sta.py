from time import sleep
import unittest, random, sys
# sys.path.append("./models")
# sys.path.append("./page_obj")
from .models import myunit, function
from .page_obj.loginPage import login

class loginTest(myunit.MyTest):
    '''登录测试'''
    #测试用户登录
