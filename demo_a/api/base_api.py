#!/usr/bin/python
# -*- coding:utf-8 -*-


class BaseApi:
    def send(self, **data):
        print(data)


if __name__ == '__main__':
    a = {
        "user": "username",
        "pwd": "password",
        "data": {
            "name": "涨三倍",
            "mobile": "12457861236"
        }
    }
    base = BaseApi()
    base.send(a)

