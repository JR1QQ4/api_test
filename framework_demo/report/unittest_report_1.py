# -*- coding:utf-8 -*-
import unittest
from time import sleep

from TestRunner import HTMLTestRunner
from TestRunner import SMTP
from selenium import webdriver


class YouTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver.exe")
        cls.base_url = "https://www.baidu.com"
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_success(self):
        """测试百度搜索：HTMLTestRunner """
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        self.driver.find_element_by_id("su").click()
        sleep(2)

    def test_error(self):
        """测试百度搜索，定位失败 """
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("python")
        self.driver.find_element_by_id("su22").click()
        sleep(2)

    def test_fail(self):
        """测试百度搜索，断言失败 """
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("unittest")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        self.assertEqual(self.driver.title, "unittest")


# 虫师：https://github.com/SeldomQA/HTMLTestRunner
suit = unittest.TestSuite()
suit.addTest(YouTest("test_success"))
suit.addTest(YouTest("test_error"))
suit.addTest(YouTest("test_fail"))

# 确定生成报告的路径
report = './unittest_report_1.html'
with open(report, 'wb') as fp:
    # 生成报告的Title,描述
    runner = HTMLTestRunner(
        stream=fp,
        title='Seldom自动化测试报告',
        description='浏览器chrome，平台windows'
    )
    # 运行测试用例
    runner.run(suit)
