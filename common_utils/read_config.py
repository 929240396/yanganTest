# -*- coding:utf-8 -*-


import configparser
import os

class ReadConfig:
    def __init__(self, filepath=None):
        if filepath:
            configpath1 = filepath
        else:
            root_dir1 = os.path.dirname(__file__)  #获取当前脚本目录
            configpath1 = os.path.join(root_dir1, "config.ini") #拼接路径
            # print(root_dir1)

            # root_dir = os.path.dirname(os.path.abspath('.'))   # 获取当前脚本所在目录的上一级目录
            # configpath = os.path.join(root_dir, "common_utils/config.ini") # 拼接路径
            # print(root_dir)


        self.cf = configparser.ConfigParser()
        self.cf.read(configpath1)

    def get_host(self, param):
        value = self.cf.get("URL", param)
        return value

base_url = ReadConfig()

# if __name__ == '__main__':
#     test = ReadConfig()
#     t = test.get_host("url")
#     print(t)
#     print(base_url.get_host("URL"))