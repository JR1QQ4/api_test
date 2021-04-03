#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests

from demo_a.api.base_api import BaseApi


class Util(BaseApi):
    def get_token(self, corp_id="ww13ef03a4459fae68", corp_secret="t_cw7KxjEKN0tTSnteb26OY5TK4kA7JGw1XdTxBjUOs"):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corp_id,
                "corpsecret": corp_secret
            }
        }
        return self.send(data)["access_token"]


if __name__ == '__main__':
    u = Util()
    print(u.get_token())
