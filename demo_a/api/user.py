#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests


class User:
    def create(self, user_id, name, mobile):
        # 创建成员
        data = {
            "userid": user_id,
            "name": name,
            "department": [1],
            "mobile": mobile
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?debug=1&access_token={self._access_token}",
                          json=data)
        return r.json()

    def del_user(self, user_id):
        # 删除成员
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self._access_token}"
                         f"&userid={user_id}")
        return r.json()

    def update(self, user_id, name, mobile):
        # 更新成员
        data = {
            "userid": user_id,
            "name": name,
            "department": [1],
            "mobile": mobile
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?debug=1&access_token={self._access_token}",
                          json=data)
        return r.json()

    def get(self, user_id):
        # 获取成员
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get"
                         "?access_token=" + self._access_token + "&userid=" + user_id)
        return r.json()
