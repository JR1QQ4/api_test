#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests


class BaseApi:
    def send(self, data):
        return requests.request(**data).json()


if __name__ == '__main__':
    a = {
        "user": "username",
        "pwd": "password",
        "data": {
            "name": "涨三倍",
            "mobile": "12457861236"
        }
    }
    # base = BaseApi()
    # base.send(a)
