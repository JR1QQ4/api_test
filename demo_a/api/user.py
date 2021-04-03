#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests

from demo_a.api.base_api import BaseApi
from demo_a.api.util import Util


class User(BaseApi):
    def __init__(self):
        self.token = Util().get_token()

    def create(self, user_id, name, mobile):
        # 创建成员
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "debug": "1",
                "access_token": self.token
            },
            "json": {
                "userid": user_id,
                "name": name,
                "department": [1],
                "mobile": mobile
            }
        }
        return self.send(data)

    def delete(self, user_id):
        # 删除成员
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "userid": user_id,
                "access_token": self.token
            }
        }
        return self.send(data)

    def update(self, user_id, name, mobile):
        # 更新成员
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params": {
                "debug": "1",
                "access_token": self.token
            },
            "json": {
                "userid": user_id,
                "name": name,
                "department": [1],
                "mobile": mobile
            }
        }
        return self.send(data)

    def get(self, user_id):
        # 获取成员
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "userid": user_id,
                "access_token": self.token
            }
        }
        return self.send(data)
