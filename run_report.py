# coding: utf-8
# author: cxf


import HTMLTestRunner
from common_utils.configEmail import SendEmail
import unittest
import time, os
import getpathInfo



path = getpathInfo.get_Path()
report_path = os.path.join(path, 'result')
root_dir = os.path.dirname(os.path.abspath(__file__)) # 获取当前脚本目录
case_dir = root_dir + '/test_suits'  # 根据项目所在路径，找到用例所在的相对项目的路径
# case_dir1 = ''
print(root_dir)
print(case_dir)


"""
1.case_dir 即测试用例所在目录
2.pattern='test_*.py' : 表示用力文件名的匹配原则， "*"表示任意多个字符
3.top_level_dir=None:测试模块的顶层目录，如果没有顶层目录（也就是说测试用例不是放在多层级目录中），默认为None
"""

# if __name__ == '__main__':


    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='电子证照库接口测试报告',description='测试结果如下: ')
    # runner.run(suit)
    # fp.close()  # 普通方式打开文件


    # runner.run(suits)
suits = unittest.defaultTestLoader.discover(case_dir, pattern='test_*.py', top_level_dir=None)
suit = unittest.TestLoader().discover(case_dir)  # 加载用例

send_mail = SendEmail(
        username='m18994736992_1@163.com',
        passwd='AKZFZWBJQCUPTYIZ',
        recv=['929240396@qq.com'],
        title='测试报告',
        content='测试发送邮件',
        file=r'C:\Users\Administrator\PycharmProjects\untitled2\reports\report.html',
        ssl=True,
    )


# class AllTest():
#     def __init__(self):
#         global resultPath
#         resultPath = os.path.join(report_path,"repotr.html")
#
#     def run(self):
#         """
#         run test
#         :return:
#         """
#
#
#
#         try:
#
#             suits = unittest.defaultTestLoader.discover(case_dir, pattern='test_*.py', top_level_dir=None)
#             suit = unittest.TestLoader().discover(case_dir)  # 加载用例
#             if suit is not None:
#                 with open(filename, 'wb') as fp:
#                     """使用withopen操作文件"""
#                 runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
#                 runner.run(suits)
#             else:
#                 print("have no case to test.")
#
#         except Exception as ex:
#             print(str(ex))
#
#         finally:
#             print("*****************Test End***************")
#

filename = root_dir + '/reports/' + 'report.html'  # 定义报告文件
with open(filename, 'wb') as fp:
    """使用withopen操作文件"""
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
    runner.run(suits)
send_mail.send_email()