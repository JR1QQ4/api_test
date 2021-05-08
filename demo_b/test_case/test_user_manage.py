#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

import pytest

from demo_b.util.handle_path import data_dir
from demo_b.util.handle_excel import HandleExcel
from demo_b.util.generate_data import gen_str

class TestUserManage:
    wx = os.path.join(data_dir, "weixin.xlsx")

    def token_

    @pytest.mark.usefixtures('token')
    @pytest.mark.parametrize('cases', HandleExcel(wx).get_all_data())
    def test_add_user(self, cases, token):
        print(len(token))
        print(token)
        params = cases['Params']
        access_token = params['access_token']
        user_id = params['userid']
        name = params['name']
        department = params['department']
        mobile = params['mobile']
        # print(params)


if __name__ == '__main__':
    pytest.main(["-sv", "test_user_manage.py"])
