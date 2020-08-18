import requests
from urllib import parse

def get_auth():
# 定义请求header
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8', 'Dev': 'pc'}
# 定义请求地址
    url = "https://wx.rayeye.cn/yg/api/web/auth/login?randomtime=1597078175359"
# 通过字典方式定义请求body
    FormData = {"account": '18994736992', "password": '123456'}
# 字典转换k1=v1 & k2=v2 模式
    data = parse.urlencode(FormData)
# 请求方式
    result = requests.post(url=url, headers=HEADERS, data=data)
    auth = result.json()['data']['authorization']
    return auth
if __name__ == '__main__':
    print(get_auth())