#!/usr/bin/python
# -*- coding:utf-8 -*-
from demo_b.api.base_api import BaseApi


class User(BaseApi):
    """企业微信成员管理"""

    def create(self, data=None):
        return self.send(data)

    def get(self, data=None):
        return self.send(data)

    def update(self, data=None):
        return self.send(data)

    def delete(self, data=None):
        return self.send(data)
