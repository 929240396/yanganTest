# -*- coding:utf-8 -*-
from common_utils.read_config import ReadConfig
import os


class BaseData:
    def __init__(self):
        self.data = ReadConfig()


    def get_ip(self):
        """从配置文件中获取固定ip"""
        ip = self.data.get_host("url")
        return ip

base_data = BaseData()

print(base_data.get_ip())