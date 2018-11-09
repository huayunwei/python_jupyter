'''
    手机端常用方法,封装的主要原因，添加log
'''

from logger import Logger
from appium.common.exceptions import NoSuchContextException

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

    def el_find(self,selector):
        '''
        查找元素
        :param:selector - 字典，type为类型，text为类型对应的内容
        :return:
        '''
        selector_type = selector['type']
        selector_text = selector['value']
        try:
            #element = None
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
        except NoSuchContextException:
            self.mylog.error("通过{}没有找到{}元素,报错信息：NoSuchContextException".format(selector_type,selector_text))
        except Exception as e:
            self.mylog.error("通过{}没有找到{}元素,报错信息：{}".format(selector_type,selector_text,e))
            # 加上截图操作

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