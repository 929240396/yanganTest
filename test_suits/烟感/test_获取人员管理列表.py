# -*- coding:utf-8 -*-

import unittest
from common_utils.send_request import RunMethod
from base_data.base_data import *
import json
from common_utils.getAuthorization import get_auth

run = RunMethod()
class Test(unittest.TestCase):
    """获取人员管理列表"""
    @classmethod
    def setUpClass(cls):
        # cls.url = base_data.get_ip() + "/web/message/list?randomtime=1597153994280&currentPage=1&pageSize=10&phone="
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    def test01(self):
        """参数正常"""
        self.url = base_data.get_ip() + "/web/user/list?randomtime=1597159917886&currentPage=1&pageSize=10&search="
        header = {"authorization":get_auth()}
        r = run.run_main("GET",self.url,header=header)
        res = r.json()
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual(200, res["code"])
        self.assertNotEqual([], res["data"]["list"])

    def test02(self):
        """currentPage为空"""
        self.url = base_data.get_ip() + "/web/user/list?randomtime=1597153994280&currentPage=&pageSize=10&search="
        header = {"authorization": get_auth()}
        r = run.run_main("GET", self.url, header=header)
        res = r.json()
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual("服务内部异常！", res["message"])
        self.assertTrue(res["data"] is None)
        self.assertIsNone( res["data"])

    def test03(self):
        """pageSize为空"""
        self.url = base_data.get_ip() + "/web/user/list?randomtime=1597153994280&currentPage=1&pageSize=&search="
        header = {"authorization": get_auth()}
        r = run.run_main("GET", self.url, header=header)
        res = r.json()
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual("服务内部异常！", res["message"])
        self.assertTrue(res["data"] is None)
        self.assertIsNone( res["data"])

    def test04(self):
        """输入姓名搜索指定人员"""
        self.url = base_data.get_ip() + "/web/user/list?randomtime=1597153994280&currentPage=1&pageSize=10&search=陈晓峰"
        header = {"authorization": get_auth()}
        r = run.run_main("GET", self.url, header=header)
        res = r.json()
        print(json.dumps(res, indent=2, sort_keys=False, ensure_ascii=False))
        self.assertEqual("已获取资源信息", res["message"])
        self.assertNotEqual([], res["data"]["list"])


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test01')('test02')('test03')('test04'))
    runner = unittest.TextTestRunner()
    runner.run(suite)