'''
    手机端常用方法,封装的主要原因，添加log
'''

from logger import Logger
from appium.common.exceptions import NoSuchContextException
import time

class BaseM():
    def __init__(self,driver):
        '''
        :param driver:
        '''
        self.driver = driver
        self.mylog = Logger(logger='BaseM').getlog()
    def cur_activity(self):
        '''
        获取当前currentActivity的值
        :return:
        '''
        cur = self.driver.current_activity
        self.mylog.info("当前页面的current_activity的为：{}".format(cur))
        return cur

    def el_find(self,selector,timeout=10,poll_frequency=0.5):
        '''
        查找元素,20181114-增加循环请求和超时报错
        :param:selector - 字典，type为类型，text为类型对应的内容
        :param:timeout - 请求超时的时间
        :param:poll_frequency - 没有请求到多久再次请求
        :return:
        '''
        # 结束时间
        end_time = time.time() + timeout
        while True:
            try:
                element = self.find_method(selector)
                self.mylog.info("找到的元素为{}".format(element))
                return element
            except NoSuchContextException:
                self.mylog.error("没有找到{}元素,报错信息：NoSuchContextException,重试中。。。".format(selector))

            except TimeoutError:
                self.mylog.error("没有找到{}元素,报错信息：TimeoutError".format(selector))
                # 加上截图操作

    def find_method(self,selector):
        selector_type = selector['type']
        selector_text = selector['value']
        if selector_type == "id":
            element = self.driver.find_element_by_id(selector_text)
        elif selector_type == "class" or selector_type == "class_name":
            element = self.driver.find_element_by_class_name(selector_text)
        elif selector_type == "android":
            element = self.driver.find_elements_by_android_uiautomator(selector_text)
        elif selector_type == "accessibility_id" or selector_type == "accessibility":
            element = self.driver.find_element_by_accessibility_id(selector_text)
        elif selector_type == "xpath":
            element = self.driver.find_element_by_xpath(selector_text)
        elif selector_type == "name":
            element = self.driver.find_element_by_name(selector_text)
        else:
            raise NameError("类型错误")
        return element


    def el_click(self,selector):
        '''
        点击，tap或click
        :param:selector - 字典，type为类型，text为类型对应的内容
        :return:
        '''
        el = self.el_find(selector)
        try:
            el.click()
            self.mylog.info("{}元素被点击".format(selector))
        except NameError:
            self.mylog.error("{}元素被点击时报错,报错信息:NameError".format(selector))
        except Exception as e:
            self.mylog.error("{}元素被点击时报错,报错信息:{}".format(selector,e))
            # 加上截图操作

    def el_send_keys(self,selector,text):
        el = self.el_find(selector)
        try:
            el.send_keys(text)
            self.mylog.info("{}元素输入内容为{}".format(selector,text))
        except NameError:
            self.mylog.error("{}元素在输入内容时报错,报错信息NameError".format(selector))
        except Exception as e:
            self.mylog.error("{}元素在输入内容时报错，报错信息{}".format(selector,e))

    def wait_activity(self,activity,timeout,interval=1):
        flag = self.driver.wait_activity(activity,timeout,interval)
        if flag:
           self.mylog.info("当前activity为{}".format(activity))
        else:
            self.mylog.error("在等待{}出现时，等待时间超过{}".format(activity,timeout))
            raise TimeoutError("超时")