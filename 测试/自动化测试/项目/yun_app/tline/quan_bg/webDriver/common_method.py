import os
from datetime import datetime
from PIL import Image
from io import BytesIO
import base64
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exception
from selenium.webdriver.support.ui import Select

class CommonMethod():
    '''
    包括常用的方法
    调用方式：
        b = common_method.CommonMethod(driver)
    '''
    # 父元素的父元素的路径
    p_path = os.path.dirname(os.path.dirname(__file__))

    def __init__(self,driver,p_path=p_path):
        '''
        :param driver: 驱动
        :param p_path: 文件执行时自动获得
        '''
        self.save_path = p_path + '/screenshots'
        self.driver = driver

    def take_screenshot(self,pic_name):
        '''
        截整个浏览器的图，并保存在当前目录上层目录的Screenshots文件夹下
        :param：pic_name -- 图片的名字,不包括后缀名
        :return:NONE
        '''
        # 创建一个文件Screenshots
        try:
            os.mkdir(self.save_path)
        except FileExistsError:
            print("文件已经存在")

        # 保存的名字
        save_name = pic_name + datetime.now().strftime("%Y%m%d%H%M") + '.png'
        # 截图:
        try:
            self.driver.get_screenshot_as_file(self.save_path+'/'+save_name)
            return save_name
        except Exception as e:
            raise Exception("take_screenshot-截图没有截取保存成功，报错信息：{}".format(e))

    def take_screenshot_as_base64(self):
        '''
        截取整个浏览器的图，返回base64编码
        :return:图片的base64编码
        '''
        try:
            return self.driver.get_screenshot_as_base64()
        except Exception as e:
            raise Exception("take_screenshot_as_base64-返回截图的base64编码时出现错误,错误提示{}".format(e))

    def take_element_pic(self,element,pic_name='浏览器截图'):
        '''
        截取某个元素的图
        实现方法：
        1.先截取整个浏览器的图
        2.获取指定元素的位置
        3.使用pillow，从之前截取的整个浏览器的图中，裁剪下元素位置处的截图，保存
        :param:element -- webElement元素
        :return:
        '''
        save_name = self.take_screenshot(pic_name)
        file_path = self.save_path+'/'+save_name
        left = element.location['x']
        right = element.location['x'] + element.size['width']
        top = element.location['y']
        bottom = element.location['y'] + element.size['height']
        try:
            im = Image.open(file_path)
            im = im.crop((left,top,right,bottom))
            im.save(file_path)
            return file_path
        except Exception as e:
            raise Exception("take_element_pic-处理后的图片没有保存成功",e)

    def take_element_pic_as_base64(self,element,pic_name='元素截图'):
        '''
        功能：截取某个元素的图，返回base64位的编码
        :param element:要截取的元素
        :param pic_name:图片名字
        :return:
        '''
        pic_path = self.take_element_pic(element,pic_name)
        # 打开处理后的图片
        im = Image.open(pic_path)
        # 转成base64位
        output_buffer = BytesIO()
        im.save(output_buffer,format='PNG')
        byte_data = output_buffer.getvalue()
        # 结果为bytes
        base64_str = base64.b64encode(byte_data)
        # 不用做处理直接可以在html中使用
        base64_str = 'data:image/png;base64,'+ base64_str.decode('utf-8')
        # 删除图片
        try:
            if os.path.exists(pic_path):
                os.remove(pic_path)
        except Exception as e:
            print("take_element_pic_as_base64-图片没有删除成功，报错信息{},图片地址为{}".format(e,pic_path))
        return base64_str

    def find_one(self,type,type_text,timeout=10,poll_frequency=0.5):
        '''
        功能：查找元素，返回查找到的元素
        :param type: 根据那种类型查找元素
        :param value: 可以定位的元素的值
        :return: 查找到的元素本身
        '''
        sel_type = type.lower()
        try:
            if sel_type == 'id':
                return WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located((By.ID,type_text)))
            elif sel_type == 'xpath':
                return WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located((By.XPATH,type_text)))
            elif sel_type == 'class_name':
                return WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located((By.CLASS_NAME,type_text)))
            elif sel_type == 'tag_name':
                return WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located((By.TAG_NAME, type_text)))
            elif sel_type == 'link_text':
                return WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located((By.LINK_TEXT,type_text)))
            elif sel_type == 'partial_link_text':
                return WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,type_text)))
            else:
                raise Exception("find_one - 类型{}不存在".format(type))
        except exception.TimeoutException:
            raise exception.TimeoutException("find_one - 超时")

    def input(self,type,type_text,inputvalue,timeout=10,poll_frequency=0.5):
        '''
        功能：send_keys方法
        :param type:选择元素的类型
        :param value:
        :param inputvalue:
        :return:
        '''
        try:
            self.find_one(type,type_text,timeout,poll_frequency).send_keys(inputvalue)
        except Exception:
            raise Exception("input - 输入内容时报错")

    def el_click(self,type,type_text,timeout=10,poll_frequency=0.5):
        '''
        功能：click方法
        :param type: 查找元素的方式
        :param type_text: 元素的特有属性值
        '''
        sel_type = type.lower()
        try:
            if sel_type == 'id':
                WebDriverWait(self.driver,timeout,poll_frequency).until(EC.element_to_be_clickable((By.ID,type_text))).click()
            elif sel_type == 'xpath':
                WebDriverWait(self.driver,timeout,poll_frequency).until(EC.element_to_be_clickable((By.XPATH,type_text))).click()
            elif sel_type == 'class_name':
                WebDriverWait(self.driver,timeout,poll_frequency).until(EC.element_to_be_clickable((By.CLASS_NAME,type_text))).click()
            elif sel_type == 'tag_name':
                WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable((By.TAG_NAME, type_text))).click()
            elif sel_type == 'link_text':
                WebDriverWait(self.driver,timeout,poll_frequency).until(EC.element_to_be_clickable((By.LINK_TEXT,type_text))).click()
            elif sel_type == 'partial_link_text':
                WebDriverWait(self.driver,timeout,poll_frequency).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,type_text))).click()
            else:
                raise Exception("el_click - 类型{}不存在".format(type))
        except exception.TimeoutException:
            raise exception.TimeoutException("el_click - 超时")

    def sel_option_by_text(self,select_el,value):
        '''
        功能：通过option的文字内容选择
        :param select_el:select元素
        :param value:值
        :return:
        '''
        select = Select(select_el)
        select.select_by_visible_text(value)

    def sel_option_by_index(self,select_el,index):
        '''
        功能：通过option的下标选择
        :param select_el:select元素
        :param index:值
        :return:
        '''
        select = Select(select_el)
        select.select_by_index(int(index))

    def sel_option_by_value(self,select_el,value):
        '''
        功能：通过option的value值选择
        :param select_el: select元素
        :param value: 值
        :return:
        '''
        select = Select(select_el)
        select.select_by_value(value)

    def switch_iframe(self,iframe,timeout=10,poll_frequency=0.5):
        '''
        功能：如果有iframe并且可以切换，则切换过去
        :param iframe: iframe元素
        :param timeout:
        :param poll_frequency:
        :return:
        '''
        try:
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(iframe))
        except exception.TimeoutException:
            raise exception.TimeoutException("switch_iframe - 超时没有找到指定的iframe元素")


    def switch_alert(self,timeout=10,poll_frequency=0.5):
        '''
        功能：返回找到的alert元素
        :param timeout:
        :param poll_frequency:
        :return:alert元素
        '''
        try:
            return WebDriverWait(self.driver,timeout,poll_frequency).until(EC.alert_is_present())
        except exception.TimeoutException:
            raise exception.TimeoutException("switch_alert - 超时没有找到alert元素")


    def switch_window_by_title(self,title):
        '''
        功能：通过窗口的题目跳转到指定窗口
        :param title:窗口题目
        :return:
        '''
        windows = self.driver.window_handles
        for handle in windows:
            self.driver.switch_to_window(handle)
            if title in self.driver.title:
                break

        raise Exception("switch_window_by_title - 没有找到题目为{}的窗口".format(title))

    def switch_window_by_index(self,index):
        '''
        功能：通过窗口的下标跳转到指定窗口
        :param index: 窗口下标
        :return:
        '''
        windows = self.driver.window_handles
        win_len = len(windows)
        if index > win_len - 1:
            raise Exception("switch_window_by_index -  参数index为{},超过当前窗口数量{}".format(index,win_len))