#!/usr/bin/python
# -*- coding:utf-8 -*-


class TestBase:
    token = None

    def setup(self):
        from framework_demo.frame.my_token import MyToken
        self.token = MyToken()
