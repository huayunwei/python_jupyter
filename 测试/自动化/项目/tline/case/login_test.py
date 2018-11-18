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
import time
import pytest
from framework.app_engine import AppEngine
from pageobjects.login import Login

engine = AppEngine()
driver = engine.open_app()
login = Login(driver)

def test_login_by_pwd():
    '''
    通过密码登录
    :return:
    '''
    login.login_in()
    time.sleep(2)
    flag = login.login_by_pwd()
    if flag:
        print("登录成功")
        login.logout()
    else:
        # 截图，报错，返回到上一页
        driver.get_screenshot_as_file('1.jpg')

''''
def test_login_by_wechat(out):
    '''
'''
    通过微信登录
    :param out:
    :return:

    login.login_in()
    time.sleep(2)
    login.login_by_wechat()
'''

if __name__ == "__main__":
    pytest.main('-s','login_test.py')

