#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from requests.sessions import Session


def get_token(corp_id="ww13ef03a4459fae68", corp_secret="t_cw7KxjEKN0tTSnteb26JVv0AgR3hypEhh0pqBwavM"):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + corp_id + "&corpsecret=" + corp_secret
    r = requests.get(url)
    return r.json()['access_token']


class HandleHttp:
    cookies = None
    headers = None
    auth = None
    def http(self, data):
        """
        发送 http 请求
        :param data:
            method, url,
            params = None, data = None, headers = None, cookies = None, files = None,
            auth = None, timeout = None, allow_redirects = True, proxies = None,
            hooks = None, stream = None, verify = None, cert = None, json = None
        :return: 返回请求结果
        """
        res = requests.request(**data)
        return


if __name__ == '__main__':
    hh = HandleHttp()
    request_data = {
        "method": "get",
        "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        "params": {
            "corpid": "ww13ef03a4459fae68",
            "corpsecret": "t_cw7KxjEKN0tTSnteb26JVv0AgR3hypEhh0pqBwavM"
        }
    }
    res = hh.http(request_data)
    print(res.text)
    print(res.json())
    print(res.status_code)
