#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests

from demo_c.common.handle_conf import conf
from demo_c.common.handle_log import logger


class Token:
    token = None

    def __init__(self):
        if self.token is None:
            self.token = self.__get_token()

    @classmethod
    def __get_token(cls):
        _http_json = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "ww13ef03a4459fae68",
                "corpsecret": "t_cw7KxjEKN0tTSnteb26JVv0AgR3hypEhh0pqBwavM"
            }
        }
        _res = requests.request(**_http_json)
        return _res.json()["access_token"]


def __handle_url(url: str):
    if url.startswith("/"):
        url = conf.get('server', 'base_url') + url
    elif url.startswith('http://') or url.startswith('https://'):
        pass
    else:
        url = conf.get('server', 'base_url') + '/' + url
    return url + "?access_token=" + Token().token


def send(method, url, **kwargs):
    """
    发送 http 请求
    :param method: 请求方式
    :param url: 请求地址
    :param kwargs: 请求参数
    :return: 响应结果
    """
    __url = __handle_url(url)
    logger.info("发送请求，请求方式 {}，请求地址 {}，请求参数{}".format(method, __url, str(kwargs)))
    return requests.request(method, __url, **kwargs)


if __name__ == '__main__':
    __http_json = {
        "method": "GET",
        "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
        "params": {
            "userid": "cangxueqing"
        }
    }
    res = send(**__http_json)
    print(res.json())
