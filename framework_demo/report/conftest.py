#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest


def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "Linux超博客园自动化测试项目v1.0"
    config._metadata['接口地址'] = 'https://www.cnblogs.com/linuxchao/'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")

@pytest.mark.optionalhookdef pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: xx测试中心")])
    prefix.extend([html.p("测试人员: Linux超")])

