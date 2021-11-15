#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import unittest

import requests
from unittestreport import ddt, list_data

from demo_d.common.handle_conf import conf
from demo_d.common.handle_excel import HandleExcel
from demo_d.common.handle_log import my_log
from demo_d.common.handle_path import DATA_DIR


def assertDicIn(expected, res):
    for k, v in expected.items():
        if res.get(k) and res.get(k) == v:
            print(k, v, "res 中找到了这个键和值")
        else:
            raise AssertionError("{} not in {}".format(expected, res))


@ddt
class TestRegister(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), "register")
    cases = excel.read_data()

    base_url = conf.get('env', 'base_url')
    headers = eval(conf.get('env', 'headers'))

    @list_data(cases)
    def test_register(self, item):
        # 第一步、准备用例数据
        # 1.接口地址
        url = self.base_url + item['url']
        # 2.接口请求参数
        params = eval(item['data'])
        # 3.请求头
        # 4.请求方法
        method = item['method'].lower()
        # 5.用例预期结果
        expected = eval(item['expected'])

        # 第二步、请求接口，获取返回实际结果
        # requests.post(url, json=params, headers=self.headers)
        response = requests.request(method, url, json=params, headers=self.headers)
        res = response.json()
        print(response.json())

        # 第三步、断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except AssertionError as e:
            my_log.error("用例--【{}】--执行失败".format(item['title']))
            # my_log.error(e)
            my_log.exception(e)
            raise e
        else:
            my_log.error("用例--【{}】--执行通过".format(item['title']))
