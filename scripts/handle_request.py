"""
Time:2019/12/14 0014
"""
import requests
import json


class HandleRequest:
    def __init__(self):
        self.one_session = requests.Session()

    def common_heads(self, heads):
        self.one_session.headers.update(heads)

    def send(self, url, method='post', data=None, is_json=True, **kwargs):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except NameError as n:
                data = eval(data)
        method = method.lower()
        if method == 'get':
            res = self.one_session.request(method, url=url, params=data, **kwargs)
        elif method in ('post', 'put', 'delete', 'patch'):
            """
            json 和data两种参数传送方式
            """
            if is_json:
                res = self.one_session.request(method, url=url, json=data, **kwargs)
            else:
                res = self.one_session.request(method, url=url, data=data, **kwargs)
        else:
            res = None
            print('{}方法没有返回值'.format(method))
        return res

    def close(self):
        self.one_session.close()
