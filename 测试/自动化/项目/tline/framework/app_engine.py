import sys
from framework.myConfig import MyConfig
from framework.logger import Logger
from appium import webdriver
from urllib3 import exceptions
import os
'''
    app引擎类
    调用方式：
        a = AppEngine()
        a.open_app()
'''

class AppEngine():
    def __init__(self):
        # 创建日志实例
        self.mylog = Logger(logger='appEngine').getlog()
        # 读取配置文件中的启动appium需要的参数
        conf = MyConfig()
        # 读取ini文件
        filePath = os.path.dirname(os.path.dirname(__file__))
        conf.read(filePath+'\\config\\config.ini',encoding='utf-8')
        self.mylog.info("读取文件../config/config.ini")
        # 获取选择的section的名字
        sel = conf.get('select','app')
        self.mylog.info("选择的手机参数为{}下的值".format(sel))
        # 获取上面获取的section下的所有options的值
        self.options = conf.items(sel)
        self.url = 'http://localhost:{}/wd/hub'.format(conf.get('appium','port'))
        self.mylog.info("链接appium的地址为：{}".format(self.url))

    # 开启app
    def open_app(self):
        # 转换成caps
        caps = {}
        for i in self.options:
            caps[i[0]] = i[1]
        try:
            self.driver = webdriver.Remote(self.url,caps)
            self.mylog.info("与appium链接成功")
            return self.driver
        except exceptions.MaxRetryError:
            self.mylog.error("请求多次appium失败，查看服务是否有问题")
        except Exception as e:
            self.mylog.error("报错信息：{}".format(e))

    # 关闭app
    def quit_app(self):
        self.driver.quit()
