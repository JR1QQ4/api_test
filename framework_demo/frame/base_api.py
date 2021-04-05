#!/usr/bin/python
# -*- coding:utf-8 -*-


class BaseApi:
    def http(self, data):
        import requests
        return requests.request(**data)

    def template(self, path, t):
        from string import Template
        import yaml
        with open(path) as f:
            temp = Template(f.read()).substitute(t)
            return yaml.safe_load(temp)


if __name__ == '__main__':
    replace = {
        "corpid": "ww13ef03a4459fae68",
        "corpsecret": "t_cw7KxjEKN0tTSnteb26OY5TK4kA7JGw1XdTxBjUOs"
    }
    base_api = BaseApi()
    r = base_api.template("token.yaml", replace)
    print(r)
    h = base_api.http(r)
    print(h.text)