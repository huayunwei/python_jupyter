'''
    登录页面的所有元素的选择
'''
import sys
from framework import base_m
from framework.myConfig import MyConfig
from page_element import page_elements
import time
import os

class Login:

    # 状态选择页面的登录跳转链接，通过id
    def __init__(self,driver):
        self.baseM = base_m.BaseM(driver)
        self.login_el = page_elements.LoginPage()
        self.conf = MyConfig()
        self.conf.read(os.path.dirname(os.path.dirname(__file__)) + '\\config\\config_login.ini', encoding='utf-8')


    def login_in(self):
        '''
        判断当前页面的activity，根据不同的页面执行不同操作，进入到登录页面
        :return:
        '''
        cur_activity = self.baseM.cur_activity()
        # 选择页
        if cur_activity == '.activity.ChooseStateActivity':
            # 点击跳转到登录页面
            self.baseM.el_click(self.login_el.login_text)
        elif cur_activity == '.activity.Main2Activity':
            self.baseM.el_click(self.login_el.me_btn)
            time.sleep(2)
            self.baseM.el_click(self.login_el.me_ok_btn)
        print("开始等待")
        # 等待进入输入账号和密码的页面
        self.baseM.wait_activity('.activity.LoginActivity',10)
        print("结束")

    # 直接输入账号和密码登录
    def login_by_pwd(self):
        phone_txt = self.conf.get('phone','phone')
        pwd_txt = self.conf.get('pwd','pwd')
        self.baseM.el_send_keys(self.login_el.phone_input,phone_txt)
        self.baseM.el_send_keys(self.login_el.pwd_input,pwd_txt)
        self.baseM.el_click(self.login_el.login_btn)

    # 使用验证码登录
    def login_by_yzm(self):
        phone_txt = self.conf.get('phone', 'phone')
        pwd_txt = self.conf.get('pwd', 'pwd')
        self.baseM.el_send_keys()

    # 使用微信登录
    def login_by_wechat(self):



