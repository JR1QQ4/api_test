#!/usr/bin/python
# -*- coding:utf-8 -*-
from pprint import pprint
import random

import requests


def get_token(corp_id="ww13ef03a4459fae68", corp_secret="t_cw7KxjEKN0tTSnteb26OY5TK4kA7JGw1XdTxBjUOs"):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + corp_id + "&corpsecret=" + corp_secret
    r = requests.get(url)
    return r.json()['access_token']


class WeiXin:
    _access_token = ''

    def __init__(self):
        self._access_token = get_token()
        print(self._access_token)

    def get_department_list(self):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self._access_token}")
        return r.json()

    def get_user(self, user_id="wangxiaoming"):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get"
                         "?access_token=" + self._access_token + "&userid=" + user_id)
        return r.json()

    def post_user(self):
        data = {
            "userid": "aaaaaaaaa",
            "name": "里斯",
            "department": [1],
            "mobile": "	13800000356"
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self._access_token}",
                          data=data)
        return r.json()


if __name__ == '__main__':
    w = WeiXin()
    pprint(w.post_user(), indent=2)