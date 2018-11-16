'''
    登录页面的所有元素的选择
'''
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

    # 判断当前页面的activity，根据不同的页面执行不同操作，进入到登录页面
    def login_in(self):
        cur_activity = self.baseM.cur_activity()
        # 选择页
        if cur_activity == '.activity.ChooseStateActivity':
            # 点击跳转到登录页面
            self.baseM.el_click(self.login_el.login_text)
        elif cur_activity == '.activity.Main2Activity':
            self.baseM.el_click(self.login_el.me_btn)
            time.sleep(2)
            self.baseM.el_click(self.login_el.me_ok_btn)
        # 等待进入输入账号和密码的页面
        self.baseM.wait_activity('.activity.LoginActivity',10)

    # 直接输入账号和密码登录
    def login_by_pwd(self):
        phone_txt = self.conf.get('phone','phone')
        pwd_txt = self.conf.get('pwd','pwd')
        self.baseM.el_send_keys(self.login_el.phone_input,phone_txt)
        #self.baseM.el_send_keys(self.login_el.pwd_input,pwd_txt)
        self.baseM.el_click(self.login_el.login_btn)
        # 判断是否登录到系统中,登录页面：.activity.LoginActivity
        cur_activity = self.baseM.cur_activity()
        if cur_activity == '.activity.Main2Activity':
            return True
        else:
            return False

    # 使用微信登录：这个函数不包括没有绑定的账号
    def login_by_wechat(self):
        # 点击微信登录按钮
        self.baseM.el_click(self.login_el.wechat_login)
        # 读取配置文件中的账号和密码
        wechat_name_text = self.conf.get('wechat','user')
        wechat_pwd_text = self.conf.get('wechat','pwd')
        # 输入用户名密码
        self.baseM.el_send_keys(self.login_el.wechat_name_input,wechat_name_text)
        self.baseM.el_send_keys(self.login_el.wechat_pwd_input,wechat_pwd_text)
        # 点击登录按钮
        self.baseM.el_click(self.login_el.login_wechat)
        # 如果提示登录失败，点击重试
        while True:
            try:
                self.baseM.el_click(self.login_el.wechat_login_retry)
                # 输入用户名密码
                self.baseM.el_send_keys(self.login_el.wechat_name_input,wechat_name_text)
                self.baseM.el_send_keys(self.login_el.wechat_pwd_input,wechat_pwd_text)
                # 点击登录按钮
                self.baseM.el_click(self.login_el.login_wechat)
            except Exception:
                print("微信登录成功")
                break

    # 退出登录
    def logout(self):
        # 点击我的
        self.baseM.el_click(self.login_el.me_btn)
        # 点击设置按钮
        self.baseM.el_click(self.login_el.setting_btn)
        # 点击退出
        self.baseM.el_click(self.login_el.logout_btn)
        # 确认
        self.baseM.el_click(self.login_el.logout_ok)


