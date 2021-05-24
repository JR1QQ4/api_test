#!/usr/bin/python
# -*- coding:utf-8 -*-
import os.path
import random
import re
import unittest
from hamcrest import *
from unittestreport import TestRunner

from demo_c.common.handle_data import gen_str, gen_phone, gen_email
from demo_c.common.handle_env import EnvData
from demo_c.common.handle_excel import HandleExcel
from demo_c.common.handle_http import send
from demo_c.common.handle_log import logger
from demo_c.common.handle_path import sources_dir, outputs_dir
from demo_c.common.myddt import ddt, data

exl2 = HandleExcel(os.path.join(sources_dir, 'weixin_api.xlsx'), "获取成员")

get_cases = exl2.get_all_cases()


@ddt
class TestUserManageGet(unittest.TestCase):
    all_userid = getattr(EnvData, 'all_userid')

    @data(*all_userid)
    def test_1_get_user(self, userid):
        """获取成员"""
        _userid = userid['userid']
        get_cases[0]['request_data'] = {
            'userid': _userid
        }
        res = send(get_cases[0]['method'], get_cases[0]['url'], params=get_cases[0])
        res_json = res.json()
        logger.info("响应结果 {}".format(str(res_json)))
        logger.info("实际结果 {}，期望结果 {}".format(res_json['errcode'], get_cases[0]['expected']['errcode']))
        logger.info("实际结果 {}，期望结果 {}".format(res_json['errmsg'], get_cases[0]['expected']['errmsg']))
        assert_that(str(res_json['errcode']), contains_string(get_cases[0]['expected']['errcode']))
        assert_that(res_json['errmsg'], contains_string(get_cases[0]['expected']['errmsg']))





