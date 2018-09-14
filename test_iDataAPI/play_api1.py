
# coding:utf-8
"""
Compatible for python2.x and python3.x
requirement: pip install requests
"""
from __future__ import print_function
import requests
import json
# 请求示例 url 默认请求参数已经做URL编码
url = "http://120.76.205.241:8000/comment/eastmoneyguba?id=583619366&pageToken=5&apikey=hN51t9PTdfju7q7DYe8tp4u7o9E0ZOidfUIprkTh1VyLg1EsgAGiFvGeHRgtMv6y"
headers = {
"Accept-Encoding": "gzip",
"Connection": "close"
}
if __name__ == "__main__":

    r = requests.get(url, headers=headers)
    json_obj = r.json()
    print(json_obj)

# 路由的设计  http://120.76.205.241:8000     comment/eastmoneyguba   ?  id=583619366   pageToken=5   apikey=hN51t9PTdfju7q7DYe8tp4u7o9E0ZOidfUIprkTh1VyLg1EsgAGiFvGeHRgtMv6y

# 使用SQLAlchemy
