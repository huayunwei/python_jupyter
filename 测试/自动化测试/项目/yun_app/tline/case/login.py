import sys
import os
print(sys.path)
print(os.path)

'''
登录页面相关测试：
    1.如果为状态选择页面：点击链接
    2.如果直接进入首页，点击我的，进入页面
测试用例包括：
    1.账号密码登录
    2.快捷登录
    3.修改密码后使用账号密码登录
    4.使用微信登录
'''
from framework.app_engine import AppEngine
import time

a = AppEngine()
driver = a.open_app()

print(driver.current_activity)
time.sleep(10)
print(driver.current_activity)
