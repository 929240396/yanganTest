import requests
# import json
# from common_utils.getAuthorization import get_auth
#
# # data = [{       "currentPage":"1",
# #                 "pageSize":"10",
# #                 "phone":"18994736992",
# #                 "randomtime":"1597081744848"
# # }]
# # data_json = json.dumps(data)
# url ='https://wx.rayeye.cn/yg/api/web/message/list?randomtime=1597153120262&currentPage=1&pageSize=10&phone='
# auth = get_auth()
# headers = {"Authorization":auth}
#
# r = requests.get(url=url,headers=headers)
# print(r.headers)
# print(r.text)
# url = 'https://wx.rayeye.cn/yg/api/web/user/list?randomtime=1597152604123&currentPage=1&pageSize=10&search='
#
# header = {"authorization":get_auth()}
# response = (requests.get(url=url,headers=header)).text
# print(response)

url = "http://v.juhe.cn/postcode/query"
data = { "postcode":"215001",
         "key":"7bedef4eeea83942542874a89011939b",
         "dtype":"json"

}
response = requests.post(url=url,data=data)
r= response.text
print(r)