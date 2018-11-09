from selenium import webdriver
import os
import configparser

class BrowerEngine():
    '''
        封装浏览器引擎类
        调用方式：
            a = BrowerEngine()
            a.open_browser("http://www.baidu.com")
    '''
    # 相对路径的值:不论在那个位置执行，run_path的值都为文件当前所在位置
    run_path = os.path.dirname(__file__)
    def __init__(self,dr_path=run_path):
        self.run_path = dr_path

    def open_browser(self,url):
        # 获取配置文件中的浏览器类型

        config = configparser.ConfigParser()
        config_file = self.run_path + '\\browser_type.ini'
        config.read(config_file)
        browser_type = config.get("browserType","browserName")

        driver = None

        # 默认是Chrome的驱动，如果需要修改，在browser_type.ini中修改
        if browser_type == "Chrome":
            driver = webdriver.Chrome(self.run_path + '\\driver\\chromedriver.exe')
        elif browser_type == "IE":
            driver = webdriver.Ie(self.run_path + '\\driver\\IEDriverServer.exe')
        elif browser_type == "Firefox":
            driver = webdriver.Firefox(executable_path=self.run_path + '\\driver\\geckodriver.exe')
        elif browser_type == "Edge":
            driver = webdriver.Edge(self.run_path + '\\driver\\MicrosoftWebDriver.exe')
        else:
            print("没有这个类型的浏览器驱动")

        if driver:
            # 开启页面
            driver.get(url)

            # 将页面最大化
            driver.maximize_window()

            # 设置等待时间
            driver.implicitly_wait(10)

            return driver
        else:
            raise Exception("driver没有获取到")

