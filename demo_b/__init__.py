#!/usr/bin/python
# -*- coding:utf-8 -*-
# api: 把所有发送请求和返回响应的api汇集在此
#   - base_api：所有api类的父类，实现了各种有用的方法
# conf：配置文件
# data：测试数据
# out：输出
#   - log：日志
# test_case：测试用例
# util：存放工具类和方法
# pytest.ini文件：pytest的配置文件

# allure 使用
# pytest test/ --alluredir ./result/
# pytest test/ --allure_features='购物车功能' --allure_stories='加入购物车'
# allure generate ./result/ -o ./report/ --clean
