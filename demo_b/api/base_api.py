#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests


class BaseApi:
    cookies = None

    def send(self, data):
        return requests.request(**data)
