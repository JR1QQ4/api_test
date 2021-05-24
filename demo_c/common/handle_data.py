#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import string


def gen_str(length: int = 1, lower_or_upper: bool = False, has_int: bool = False, other: str = ''):
    """
    生成指定长度的字符串
    :param length: 生成的字符串长度
    :param lower_or_upper: 是否区分大小写
    :param has_int: 是否包含数字
    :param other: 包含除了字母数字以外的字符
    :return: 字符串
    """
    _temp = ""
    if lower_or_upper:
        _temp += string.ascii_letters
    else:
        _temp += string.ascii_lowercase
    if has_int:
        _temp += string.digits
    if other:
        _temp += other
    return ''.join(random.choices(_temp, k=length))


def gen_phone(length=8):
    """
    生成手机号
    :param length: 除了手机号前缀以外的长度
    :return: 手机号
    """
    head = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
            "153", "155", "156", "157", "158", "159", "186", "187", "188", "189"]
    head = random.choice(head)
    body = ''.join(random.choices(string.digits, k=length))
    return head + body


def gen_email(length: int = None, suffix: str = None):
    _suffix = ['@163.com', '@qq.com', '@gmail.com', '@foxmail.com', '@yahoo.com', '@msn.com', '@hotmail.com',
               '@live.com']
    if suffix is None:
        _suffix = random.choice(_suffix)
    if length is None:
        _length = random.randint(6, 18)
    else:
        _length = max(6, length)
    return gen_str(_length, True, True) + _suffix


if __name__ == '__main__':
    print(gen_str(1))
    print(gen_str(64))
    print(gen_str(32, has_int=True))
    print(gen_phone(8))
    print(gen_phone(7))
    print(gen_email(12))
