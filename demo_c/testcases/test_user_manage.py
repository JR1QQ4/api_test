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

exl1 = HandleExcel(os.path.join(sources_dir, 'weixin_api.xlsx'), "创建成员")
exl2 = HandleExcel(os.path.join(sources_dir, 'weixin_api.xlsx'), "获取成员")

create_cases = exl1.get_all_cases()
get_cases = exl2.get_all_cases()


@ddt
class TestUserManageCreate(unittest.TestCase):
    all_userid = []

    @classmethod
    def handle_userid(cls, userid):
        res = re.match(r'(\d+)?(<=|<)?length(<=|<|=)(\d+)?', userid)
        if res is None:
            num = random.randint(2, 63)
            return gen_str(num)
        else:
            group1 = res.group(1)
            group2 = res.group(2)
            group3 = res.group(3)
            group4 = res.group(4)
            if group2 is None:
                if group3 == '<':
                    return gen_str(int(group4) + 1)
                elif group3 == '<=':
                    return gen_str(int(group4) + 2)
                elif group3 == '=':
                    return gen_str(int(group4))
            elif group2 == '<':
                if group3 is None:
                    return gen_str(int(group1) + 1)
                elif group3 == '<':
                    return gen_str(random.randint(int(group1) + 1, int(group4) - 1))
                elif group3 == '<=':
                    return gen_str(random.randint(int(group1) + 1, int(group4)))
            elif group2 == '<=':
                if group3 is None:
                    return gen_str(int(group1))
                elif group3 == '<':
                    return gen_str(random.randint(int(group1), int(group4) - 1))
                elif group3 == '<=':
                    return gen_str(random.randint(int(group1), int(group4)))
            else:
                return userid

    @classmethod
    def handle_name(cls, name):
        if name == 'length=1':
            return gen_str(1)
        elif name == 'length=64':
            return gen_str(64)
        elif name == '#NAME#':
            return gen_str(random.randint(2, 63))
        else:
            return name

    @classmethod
    def handle_mobile(cls, mobile):
        if mobile == 'length=10':
            return gen_phone(7)
        elif mobile == '#MOBILE#':
            return gen_phone()
        else:
            return mobile

    @classmethod
    def handle_department(cls, dept):
        if dept == '#DEPARTMENT#':
            return random.randint(1, 23)
        else:
            return dept

    @classmethod
    def handle_email(cls, email):
        if email == '#EMAIL#':
            return gen_email()
        else:
            return email

    @data(*create_cases)
    def test_user_manage(self, case):
        request_data = case['request_data']
        userid = self.handle_userid(request_data['userid'])
        name = self.handle_name(request_data['name'])
        send_data = {
            'userid': userid,
            'name': name,
            'department': request_data['department']
        }

        # _a = getattr(EnvData, 'all_userid')
        # _a.append({
        #     'title': '创建成员时创建的userid_' + str(case['id']),
        #     'userid': userid
        # })
        # self.all_userid.append({
        #     'title': '创建成员时创建的userid_' + str(case['id']),
        #     'userid': userid
        # })

        logger.info("******创建成员********")
        if 'mobile' in request_data:
            mobile = self.handle_mobile(request_data['mobile'])
            send_data['mobile'] = mobile
        elif 'email' in request_data:
            email = self.handle_email(request_data['email'])
            send_data['email'] = email
        res = send(case['method'], case['url'], json=send_data)
        res_json = res.json()
        logger.info("响应结果 {}".format(str(res_json)))
        logger.info("实际结果 {}，期望结果 {}".format(res_json['errcode'], case['expected']['errcode']))
        logger.info("实际结果 {}，期望结果 {}".format(res_json['errmsg'], case['expected']['errmsg']))
        assert_that(str(res_json['errcode']), contains_string(case['expected']['errcode']))
        assert_that(res_json['errmsg'], contains_string(case['expected']['errmsg']))

        logger.info("******获取成员********")
        get_cases[0]['request_data'] = {
            'userid': userid
        }
        res = send(get_cases[0]['method'], get_cases[0]['url'], params=get_cases[0]['request_data'])
        res_json = res.json()
        logger.info("响应结果 {}".format(str(res_json)))
        logger.info("实际结果 {}，期望结果 {}".format(res_json['errcode'], get_cases[0]['expected']['errcode']))
        logger.info("实际结果 {}，期望结果 {}".format(res_json['errmsg'], get_cases[0]['expected']['errmsg']))
        assert_that(str(res_json['errcode']), contains_string(get_cases[0]['expected']['errcode']))
        assert_that(res_json['errmsg'], contains_string(get_cases[0]['expected']['errmsg']))
