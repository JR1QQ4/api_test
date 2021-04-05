#!/usr/bin/python
# -*- coding:utf-8 -*-
import base64
import json

import requests


class TestB64:
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }

    def send(self, data: dict):
        res = requests.request(data["method"], data['url'], headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(res.content))
