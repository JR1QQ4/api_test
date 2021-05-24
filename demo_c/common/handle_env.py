#!/usr/bin/python
# -*- coding:utf-8 -*-
class EnvData:
    all_userid = []


def clear_env_attrs():
    # 清理 EnvData里设置的属性
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)


if __name__ == '__main__':
    a = getattr(EnvData, 'all_userid')
    print(a)
    a.append({'title': '1', 'userid': 'a'})
    a.append({'title': '2', 'userid': 'a'})
    a = getattr(EnvData, 'all_userid')
    print(EnvData.__dict__)
    print(a)
