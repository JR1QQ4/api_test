#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from jsonpath import jsonpath

# res = requests.post('https://www.imooc.com/search/hotwords')
# print(res.json())

data = {'result': 0, 'data': [{'word': 'Java工程师', 'is_default': '1'}, {'word': 'Vue', 'is_default': '0'},
                              {'word': 'Python', 'is_default': '0'}, {'word': 'Go', 'is_default': '0'},
                              {'word': 'SpringBoot', 'is_default': '0'}, {'word': 'Docker', 'is_default': '0'},
                              {'word': 'React', 'is_default': '0'}, {'word': '小程序', 'is_default': '0'}], 'msg': '成功'}
print(jsonpath(data, "$"))  # False，$ 表示根节点
print(jsonpath(data, "$."))  # False，. 表示直接点
print(jsonpath(data, "$.result"))  # [0]
print(jsonpath(data, "$[result]"))  # [0]，同上
print(jsonpath(data, "$..msg"))  # ['成功']，.. 表示子孙节点
print(jsonpath(data, "$.error"))  # False，匹配不到数据
print(jsonpath(data, "$.data[0]"))  # [{'word': 'Java工程师', 'is_default': '1'}]，通过索引获取 列表 的值
print(jsonpath(data, "$.data[2].word"))  # ['Python']
print(jsonpath(data, "$.data[2][word,is_default]"))  # ['Python', '0']，同时获取多个值，逗号两边不能有空格
print(jsonpath(data, "$.data[?(@.word=='Docker')]"))  # [{'word': 'Docker', 'is_default': '0'}]，条件过滤
print(jsonpath(data, "$.data[?(@.is_default=='1')]"))  # [{'word': 'Java工程师', 'is_default': '1'}]，字符串要加引号

