import subprocess
import time
import configparser
from framework.logger import Logger
import os
'''
功能：
1.检查当前端口是否被占用，处于占用状态则换一个端口，重复判断直到端口没有被占用
2.开启服务
3.查找timeout时间，每隔poll_frequency时间查询一次，判断服务是否已经被启动
4.如果timeout了，则直接报错，后面的内容不可以再执行
5.怎么判断所有内容都执行完毕了？ -- 线程？，所有内容都执行完毕后kill掉该进程
'''

class Appium():

    # 获取端口号，从配置文件中获取端口号
    def __init__(self):
        # 创建日志实例
        self.mylog = Logger(logger='appEngine').getlog()
        # 读取配置文件中的启动appium需要的参数
        self.conf = configparser.ConfigParser()
        # 读取ini文件,获取端口号
        filePath = os.path.dirname(os.path.dirname(__file__))
        self.conf.read(filePath + '\\config\\config.ini', encoding='utf-8')
        self.port = self.conf.get("appium","port")

    # 开启appium
    def start_appium(self,timeout=30,poll_frequency=3):
        '''

        :param port:
        :param timeout: 秒
        :param poll_frequency:秒
        :return:
        '''
        flag = subprocess.getoutput('netstat -ano | findstr {}'.format(self.port))
        # 判断当前端口是否被占用
        while flag:
            # 当前端口已经被占用，端口号增加1
            self.port = self.port + 1
            self.conf.set("appium","port",self.port)
            # 再判断
            flag = subprocess.getoutput('netstat -ano | findstr {}'.format(self.port))
            # 如果当前端口不再被占用，开启appium

        # 使用/c，在cmd中执行的内容停止后会自动关闭cmd页面
        # 使用/t，在cmd中执行的内容停止后cmd依旧保持存在的状态
        # 用cmd中参数时可以加上cmd.exe
        subprocess.run("start cmd.exe /c appium -a 127.0.0.1 -p {} --session-override".format(self.port), shell=True)
        # 如果不用cmd中的参数需要去掉cmd.exe
        #subprocess.run("start appium -a 127.0.0.1 -p {} -U D3H5T18312000636 --session-override".format(port), shell=True)

        # 循环判断是否超时
        # time.time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
        now_time = time.time()
        end_time = now_time + timeout
        while now_time < end_time:
            flag = subprocess.getoutput('netstat -ano | findstr {}'.format(self.port))
            if flag:
                print("appium服务在端口{}启动成功".format(self.port))
                break
            else:
                print("端口号为{}的进程没有搜索到，重新搜索".format(self.port))
                time.sleep(poll_frequency)
                now_time = now_time + poll_frequency
        else:
            # 如果没有开启成功，直接关闭cmd
            # 可以停掉appium服务，但是cmd页面关闭不了
            subprocess.run("taskkill /F /IM node.exe /t", shell=True)
            raise TimeoutError("appium在端口{}没有开启成功".format(self.port))


    # 关闭服务器
    def stop_appium(self):
        # 可以停掉appium服务，但是cmd页面关闭不了
        subprocess.run("taskkill /F /IM node.exe /t", shell=True)
