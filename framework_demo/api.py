#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
    在请求之前，对请求的 url 进行替换
    1. 需要二次封装 requests，对请求进行定制化
    2. 将请求的结构体的 url 从一个写死的 ip 地址改为一个（任意的）域名
    3. 使用一个 env 配置文件，存放各个环境的配置信息
    4. 然后将请求结构体中的 url 替换为 env 配置文件中个人选择的 url
    5. 将 env 配置文件使用 yaml 进行管理
"""

import requests
import yaml
import os

class Api:
    # env = {
    #     "default": "dev",
    #     "testing-studio": {
    #         "dev": "www.httpbin.org",
    #         "test": "127.0.0.1"
    #     }
    # }
    env_filepath = os.path.dirname(os.path.abspath(__file__)) + os.sep + "env.yaml"
    env = yaml.safe_load(open(env_filepath))
    data = {
        "method": "get",
        "url": "https://testing-studio/get",
        "headers": None,
    }

    def send(self, data: dict):
        print(self.env)
        data['url'] = str(data['url']).replace("testing-studio", self.env["testing-studio"][self.env["default"]])
        return requests.request(method=data["method"], url=data['url'], headers=data["headers"], verify=False)


class TestApi:
    data = {
        "method": "get",
        "url": "https://testing-studio/get",
        "headers": None
    }

    def test_get(self):
        api = Api()
        r = api.send(self.data)
        print(r.text)


if __name__ == '__main__':
    env_filepath = os.path.dirname(os.path.abspath(__file__)) + os.sep + "env.yaml"
    print(env_filepath)