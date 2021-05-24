#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import os
import random

import pytest

from demo_b.util.handle_http import HandleHttp
from demo_b.util.handle_log import HandleLog
from demo_b.util.handle_path import data_dir
from demo_b.util.handle_excel import HandleExcel
from demo_b.util.generate_data import gen_str, gen_phone


class TestUserManage:
    wx = os.path.join(data_dir, "weixin_api.xlsx")
    logger = HandleLog()

    @classmethod
    def setup_class(cls):
        cls.http = HandleHttp()

    def user_id_judge(self, user_id):
        if user_id == "length=1":
            return gen_str(1, "_-@.")
        elif user_id == "length=64":
            return gen_str(64, "_-@.")
        elif user_id == "1<length<64":
            r = random.randint(2, 63)
            return gen_str(r, "_-@.")
        elif user_id == "" or user_id == "length>64" or user_id == "#ERROR#":
            return ''
        else:
            return user_id

    def name_judge(self, name):
        if name == "length=1":
            return gen_str(1, lower_or_upper=True)
        elif name == "length=64":
            return gen_str(64, lower_or_upper=True)
        elif name == "1<length<64":
            r = random.randint(2, 63)
            return gen_str(r, lower_or_upper=True)
        elif name == "" or name == "length>64" or name == "#ERROR#":
            return ''
        else:
            return name

    def department_judge(self, department):
        if department == "this<100":
            r = random.randint(1, 99)
            return r
        elif department == "this=100":
            return 100
        elif department == "" or department == "this>100" or department == "#ERROR#":
            return 103
        else:
            return department

    def mobile_judge(self, mobile):
        if mobile == "#MOBILE#":
            return gen_phone()
        elif mobile == "#ERROR#":
            return ''
        else:
            return mobile

    @pytest.mark.usefixtures('token')
    @pytest.mark.parametrize('case', HandleExcel(wx, "删除成员").get_all_data())
    def test_add_user(self, case, token):
        params = case['Params']
        params['access_token'] = token if params['access_token'] == "#ACCESS_TOKEN#" else ''
        params['userid'] = self.user_id_judge(params['userid'])
        data = {
            "method": case['Method'],
            "url": case['Url'],
            "params": {
                "access_token": params['access_token'],
                "userid": params['userid']
            },
            # "params": case['Params'],
            # "data": case['Params'],
            # "json": case['Params']
        }
        self.logger.info("发送 http 请求： \n\t请求参数: " + json.dumps(data))
        res = self.http.send(data)
        res_json = res.json()
        self.logger.info(res_json)

        code = case['Expectation']['errcode']
        msg = case['Expectation']['errmsg']
        if res_json['errcode'] == code and res_json['errmsg'] == msg:
            HandleExcel(self.wx, "删除成员").update(case, "pass")
        else:
            HandleExcel(self.wx, "删除成员").update(case, res_json)


if __name__ == '__main__':
    pytest.main(["-sv", "test_user_manage_delete.py"])
