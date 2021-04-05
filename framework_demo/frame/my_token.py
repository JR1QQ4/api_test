#!/usr/bin/python
# -*- coding:utf-8 -*-
from framework_demo.frame.base_api import BaseApi


class MyToken(BaseApi):
    _t = {
        "corpid": "ww13ef03a4459fae68",
        "corpsecret": "t_cw7KxjEKN0tTSnteb26OY5TK4kA7JGw1XdTxBjUOs"
    }

    def get(self):
        data = self.template("token.yaml", self._t)
        res = self.http(data)
        return res


if __name__ == '__main__':
    token = MyToken()
    print(token.get().json()["access_token"])
