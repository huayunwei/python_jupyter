import logging
import os.path
import time

'''
日志类:
    调用方式：
        mylogger = Logger(logger='xxxx').getlog()
    使用方式
        mylogger.info("xxx")
'''
class Logger():
    def __init__(self,logger):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件将日志存入指定的文件中
            :param logger:
        '''
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        '''
        # 创建一个handler,用于写入日志文件
        # time.localtime返回time.struct_time(tm_year=2018, tm_mon=11, tm_mday=7, tm_hour=10, tm_min=22, tm_sec=7, tm_wday=2, tm_yday=311, tm_isdst=0)
        # time.time()返回时间戳
        rq = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')+'/logs/')
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        '''


        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        #self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger