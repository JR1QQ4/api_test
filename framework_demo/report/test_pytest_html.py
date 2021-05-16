"""
------------------------------------
@Time : 2019/8/28 19:45
@Auth : linux超
@File : test_pytest_html.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import pytest


def login(username, password):
    """模拟登录"""
    user = "linux超"
    pwd = "linux超哥"
    if user == username and pwd == password:
        return {"code": 1001, "msg": "登录成功", "data": None}
    else:
        return {"code": 1000, "msg": "用户名或密码错误", "data": None}


test_data = [{
    "case": "用户名正确, 密码正确",
    "user": "linux超",
    "pwd": "linux超哥",
    "expected": {"code": 1001, "msg": "登录成功", "data": None}
},
    {
        "case": "用户名正确, 密码为空",
        "user": "linux超",
        "pwd": "",
        "expected": {"code": 1000, "msg": "用户名或密码错误", "data": None}
    },
    {
        "case": "用户名为空, 密码正确",
        "user": "",
        "pwd": "linux超哥",
        "expected": {"code": 1000, "msg": "用户名或密码错误", "data": None}
    },
    {
        "case": "用户名错误, 密码错误",
        "user": "linux",
        "pwd": "linux",
        "expected": {"code": 1000, "msg": "用户名或密码错误", "data": None}
    }
]


class TestLogin(object):

    @pytest.mark.parametrize("data", test_data)
    def test_login(self, data):
        result = login(data["user"], data["pwd"])
        assert result == data["expected"]


if __name__ == '__main__':
    pytest.main(['-sv', "test_pytest_html.py", "--html", "pytest_report_1.html"])
