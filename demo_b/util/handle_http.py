#!/usr/bin/python
# -*- coding:utf-8 -*-
import json

import requests

from demo_b.util.handle_log import HandleLog


def get_token(corp_id="ww13ef03a4459fae68", corp_secret="t_cw7KxjEKN0tTSnteb26JVv0AgR3hypEhh0pqBwavM"):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + corp_id + "&corpsecret=" + corp_secret
    r = requests.get(url)
    return r.json()['access_token']


def raise_error():
    def out_wrapper(func):
        def wrapper(data):
            try:
                return func(data)
            except Exception as e:
                raise e

        return wrapper

    return out_wrapper


class HandleHttp:
    _session = None

    def __init__(self):
        if self._session is None:
            self._session = requests.Session()

    @staticmethod
    @raise_error()
    def send(data: dict):
        """
        发送 http 请求
        :param data:
            method, url,
            params = None, data = None, headers = None, cookies = None, files = None,
            auth = None, timeout = None, allow_redirects = True, proxies = None,
            hooks = None, stream = None, verify = None, cert = None, json = None
        :return: :class:`Response <Response>` object
        """
        return requests.request(**data)

    @staticmethod
    def post(data: dict):
        # (url, data=None, json=None, **kwargs)
        return requests.post(**data)

    @staticmethod
    def get(data: dict):
        # (url, params=None, **kwargs)
        return requests.get(**data)

    def session_send(self, data):
        # (self, method, url,
        #             params=None, data=None, headers=None, cookies=None, files=None,
        #             auth=None, timeout=None, allow_redirects=True, proxies=None,
        #             hooks=None, stream=None, verify=None, cert=None, json=None)
        return self._session.request(**data)

    def session_post(self, data):
        # (self, url, data=None, json=None, **kwargs)
        return self._session.post(**data)

    def session_get(self, data):
        # (self, url, **kwargs)
        return self._session.get(**data)


if __name__ == '__main__':
    get_token = {
        "method": "get",
        "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        "params": {
            "corpid": "ww13ef03a4459fae68",
            "corpsecret": "t_cw7KxjEKN0tTSnteb26JVv0AgR3hypEhh0pqBwavM"
        }
    }
    httpbin_get = {
        "method": "get",
        "url": "https://httpbin.org/get",
        "headers": {
            "content-type": "application/json"
        }
    }

    res = HandleHttp.send(httpbin_get)
    print(res.text)


