#!/usr/bin/python
# -*- coding:utf-8 -*-
import base64
import hashlib
import string
import random

# def __init__(self):
#     print([chr(i) for i in range(65, 91)])  # 大写字母
#     print([chr(i) for i in range(97, 123)])  # 小写字母
#     print([chr(i) for i in range(48, 58)])  # 数字
#     print(string.whitespace)  # ' \t\n\r\v\f'
#     print(string.ascii_lowercase)  # 小写字母
#     print(string.ascii_uppercase)  # 大写字母
#     print(string.ascii_letters)  # 所有 ASCII字母
#     print(string.digits)  # 十进制位数的字符串
#     print(string.hexdigits)  # 十六进制字符串
#     print(string.octdigits)  # 八进制字符串
#     print(string.punctuation)  # 所有标点字符
#     print(string.printable)  # 所有可打印的字符的字符串


def gen_str_lower_or_upper(length=1, lower_or_upper=None):
    if lower_or_upper == 'lower':
        all_atr = string.ascii_lowercase
    elif lower_or_upper == 'upper':
        all_atr = string.ascii_uppercase
    else:
        all_atr = string.ascii_letters
    return ''.join(random.choices(all_atr, k=length))


def gen_str_has_int(length=1):
    temp = string.ascii_letters + string.digits
    return ''.join(random.choices(temp, k=length))


def gen_str(length=1, lower_or_upper=False, has_int=True, other=None):
    """
    生成字符串
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
    if other is not None:
        _temp += other
    return ''.join(random.choices(_temp, k=length))


def gen_hash(value: str, name="md5", encode_type="utf-8"):
    value = value.encode(encode_type)
    if name in ('MD5', 'md5'):  # 32位
        return hashlib.md5(value).hexdigest()
    elif name in ('SHA1', 'sha1'):  # 40 位
        return hashlib.sha1(value).hexdigest()
    elif name in ('SHA256', 'sha256', 'SHA224', 'sha224'):  # 64 位
        return hashlib.sha256(value).hexdigest()
    elif name in ('SHA512', 'sha512', 'SHA384', 'sha384'):  # 128 位
        return hashlib.sha512(value).hexdigest()
    elif name in ('blake2b', 'blake2s'):  # 64 位
        return hashlib.blake2s(value).hexdigest()
    elif name in {'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
                  'shake_128', 'shake_256'}:  # 128 位
        return hashlib.sha3_512(value).hexdigest()
    else:
        return hashlib.md5(value).hexdigest()


def base64_encode(value):
    if type(value) is str:
        return base64.b64encode(value.encode()).decode()
    elif type(value) is bytes:
        return base64.b64encode(value).decode()


def base64_decode(value):
    try:
        return base64.b64decode(value.encode()).decode()
    except UnicodeDecodeError:
        return base64.b64decode(value.encode())


if __name__ == '__main__':
    test1 = gen_str_has_int(64)
    test2 = gen_hash("adssa123", 'md5')

    a = "http://www.baidu.com?a=b&b=d"
    test3 = base64_encode(a)
    test4 = base64_decode(test3)
    # with open("1.jpg", "rb") as f:
    #     r = f.read()
    #     s = base64_encode(r)
    #     v = base64_decode(s)
    #     with open("2.jpg", "wb") as c:
    #         c.write(v)

    test5 = gen_str(64, other="_-@.")
    # while True:
    #     test6 = gen_str(64, other="_-@.")
    #     print("-" * 50)
    #     print(test6)
    #     print("-" * 50)
    #     if test6[0] in string.ascii_lowercase + string.digits:
    #         break
