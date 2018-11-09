# 用于处理在使用configparser时，options的值返回全小写
import configparser

class MyConfig(configparser.ConfigParser):
    def __init__(self,defaults=None):
        configparser.ConfigParser.__init__(self,defaults=defaults)

    # 直接返回optionstr，不做任何处理
    def optionxform(self,optionstr):
        return optionstr