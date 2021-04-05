#!/usr/bin/python
# -*- coding:utf-8 -*-
from framework_demo.frame.test_base import TestBase


class TestToken(TestBase):
    def test_get_token(self):
        assert self.token.get().json()["errcode"] == 0