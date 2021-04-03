#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import string
from pprint import pprint
import random
from urllib.parse import urlencode, quote

import requests
from urllib import parse


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

    def post_user(self, d=None):
        data = None
        if d is None:
            data = {
                "userid": "piaozhongji",
                "name": "票终极",
                "department": [1],
                "mobile": "13800000356"
            }
        else:
            data = d
        d = json.dumps(data).encode("utf-8")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?debug=1&access_token={self._access_token}",
                          data=d,
                          headers=headers)

        # data = {
        #     "userid": "piaozhongji",
        #     "name": "票终极",
        #     "department": [1],
        #     "mobile": "13800000356"
        # }
        # headers = {
        #     "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?debug=1&"
        #                   f"access_token={self._access_token}",
        #                   json=data)

        return r.json()

    def del_user(self, user_id="jingshulan"):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self._access_token}"
                         f"&userid={user_id}")
        return r.json()


if __name__ == '__main__':
    w = WeiXin()
    pprint(w.post_user(), indent=2)

    # data = {
    #     "userid": "piaozhongji",
    #     "name": "票终极",
    #     "department": [1],
    #     "mobile": "13800000356"
    # }
    # b = json.dumps(data)
    # print(b)
    # new_str = b.encode("utf-8")
    # print(new_str)
    # print(type(new_str))
