# -*- coding:utf-8 -*-

import requests
import json
from requests.exceptions import RequestException



class RunMethod:
    """定义一个执行接口请求的类"""

    @staticmethod
    def send_get(url, data=None, header=None):
        response = requests.get(url=url, params=data, headers=header, timeout=20)
        try:
            if response.status_code == 200:
                r = response
                return r
            else:
                return None
        except RequestException:
            print("请求失败")
            return None


    @staticmethod
    def send_post(url, data=None, header=None):
        response = requests.post(url=url, data=data, headers=header, timeout=20)
        try:
            if response.status_code == 200:
                r = response
                return r
            else:
                return None
        except RequestException:
            print("请求失败")
            return None

    def run_main(self, method, url, data=None, header=None):
        if method == "GET":
            res = self.send_get(url, data, header)
        else:
             res = self.send_post(url, data, header)
        return res

if __name__ == '__main__':
    url = ""
    data = {

    }
    t = RunMethod()



