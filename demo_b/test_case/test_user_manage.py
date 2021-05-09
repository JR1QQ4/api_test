#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import random

import pytest

from demo_b.util.handle_http import HandleHttp
from demo_b.util.handle_log import HandleLog
from demo_b.util.handle_path import data_dir
from demo_b.util.handle_excel import HandleExcel
from demo_b.util.generate_data import gen_str, gen_phone


class TestUserManage:
    wx = os.path.join(data_dir, "weixin.xlsx")
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
        else:
            return ''

    def name_judge(self, name):
        if name == "length=1":
            return gen_str(1, lower_or_upper=True)
        elif name == "length=64":
            return gen_str(64, lower_or_upper=True)
        elif name == "1<length<64":
            r = random.randint(2, 63)
            return gen_str(r, lower_or_upper=True)
        else:
            return ''

    def department_judge(self, department):
        if department == "this<100":
            r = random.randint(1, 99)
            return r
        elif department == "this=100":
            return 100
        else:
            return 103

    def mobile_judge(self, mobile):
        if mobile == "#MOBILE#":
            return gen_phone()
        else:
            return ''

    @pytest.mark.usefixtures('token')
    @pytest.mark.parametrize('case', HandleExcel(wx).get_all_data())
    def test_add_user(self, case, token):
        params = case['Params']
        params['access_token'] = token if params['access_token'] == "#ACCESS_TOKEN#" else ''
        params['userid'] = self.user_id_judge(params['userid'])
        params['name'] = self.name_judge(params['name'])
        params['department'] = self.department_judge(params['department'])
        params['mobile'] = self.mobile_judge(params['mobile'])
        data = {
            "method": case['Method'],
            "url": case['Url'],
            "params": case['Params'],
            "data": case['Params'],
            "json": case['Params']
        }
        res = self.http.send(data)
        assert res.status_code == 200
        self.logger.info(res.json())


if __name__ == '__main__':
    pytest.main(["-sv", "test_user_manage.py"])
