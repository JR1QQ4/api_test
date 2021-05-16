#!/usr/bin/python
# -*- coding:utf-8 -*-
# https://github.com/musen123/UnitTestReport
import unittest

from unittestreport import rerun

from unittestreport import TestRunner


class TestClass(unittest.TestCase):
    @rerun(count=4, interval=2)
    def test_case_01(self):
        a = 100
        b = 99
        assert a == b


test_suite = unittest.TestSuite()
test_suite.addTest(TestClass("test_case_01"))
runner = TestRunner(test_suite,  # 测试套件（必传）
                    tester='测试人员—小柠檬',  # 测试人员名称
                    filename="unittest_report_3.html",  # 指定报告文件名
                    report_dir=".",  # 指定存放报告路径
                    title='这里设置报告标题',  # 指定测试报告的标题
                    desc='小柠檬项目测试生成的报告描述',
                    templates=2)  # 可以指定1，2，3三个风格的模板
runner.run()
