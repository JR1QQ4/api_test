#!/usr/bin/python
# -*- coding:utf-8 -*-
# https://www.httpbin.org/
import json

import pystache
import requests
from jsonpath import jsonpath
from requests_xml import XMLSession
from hamcrest import *
from jsonschema import validate


class TestHttpBin:
    _url = "http://www.httpbin.org/"
    _get = _url + 'get'
    _post = _url + 'post'

    def test_get(self):
        r = requests.get(self._get)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_get_with_params(self):
        payload = {"key1": "value1", "key2": "value2"}
        r = requests.get(self._get, params=payload)
        print(r.text)
        print(r.json())
        print(r.status_code)

    def test_post_form(self):
        payload = {"key1": "value1", "key2": "value2"}
        r = requests.post(self._post, data=payload)
        print(r.text)

    def test_get_has_header(self):
        r = requests.get(self._get, headers={"H": "header demo"})
        print(r.text)
        print(r.headers)

    def test_post_json(self):
        payload = {"key1": "value1", "key2": "value2"}
        r = requests.post(self._post, json=payload)
        print(r.text)

    def test_post_xml(self):
        xml = """<?xml version='1.0' encoding='utf-8'?><a>(っ °Д °;)っ</a>""".encode('utf-8')
        headers = {'Content-Type': 'application/xml; charset=UTF-8'}
        r = requests.post(self._post, data=xml, headers=headers)
        print(type(r.text))
        print(r.text)
        print(r.text.encode('utf-8').decode('utf-8'))

    def test_mustache(self):
        context = {'author': 'Chris Wanstrath', 'maintainer': 'Chris Jerdonek'}
        result = pystache.render("Author: {{author}}\nMaintainer: {{maintainer}}", context)
        print(result)

    def test_json_path_assert(self):
        obj = {"store": {
            "book": [
                {"category": "reference",
                 "author": "Nigel Rees",
                 "title": "Sayings of the Century",
                 "price": 8.95
                 },
                {"category": "fiction",
                 "author": "Evelyn Waugh",
                 "title": "Sword of Honour",
                 "price": 12.99
                 },
                {"category": "fiction",
                 "author": "Herman Melville",
                 "title": "Moby Dick",
                 "isbn": "0-553-21311-3",
                 "price": 8.99
                 },
                {"category": "fiction",
                 "author": "J. R. R. Tolkien",
                 "title": "The Lord of the Rings",
                 "isbn": "0-395-19395-8",
                 "price": 22.99
                 }
            ],
            "bicycle": {
                "color": "red",
                "price": 19.95
            }
        }
        }
        assert obj['store']['bicycle']['color'] == 'red'
        print(jsonpath(obj, "$..category"))
        assert jsonpath(obj, "$..category")[0] == "reference"

    def test_xml_assert(self):
        session = XMLSession()
        r = session.get('https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss')
        print(r.xml.links)
        item = r.xml.xpath('//item', first=True)
        print(item)
        print(item.text)
        rss = r.xml.xpath('//rss', first=True)
        print(rss.attrs)
        print(item.xml)
        print(item.xpath('//enclosure')[0].attrs['url'])
        print(r.xml.search('<title>{}</title>'))

    def test_hamcrest(self):
        assert_that("hamcrest", equal_to_ignoring_case("Hamcrest"))

    def test_json_schema(self):
        # schema = {
        #     "type": "object",
        #     "properties": {
        #         "price": {"type": "number"},
        #         "name": {"type": "string"},
        #     },
        # }
        # validate(instance={"name": "Eggs", "price": 34.99}, schema=schema)
        # validate(
        #     instance={"name": "Eggs", "price": "Invalid"}, schema=schema,
        # )  # <ValidationError: "'Invalid' is not of type 'number'">
        data = requests.get(self._get, params={"limit": 2}).json()
        schema = json.load(open("schema.json"))
        validate(data, schema=schema)

    def test_add_cookie(self):
        headers = {
            # "Cookie": "username=password",
            "User-Agent": "wang"
        }
        cookies = {"su": "todo"}
        r = requests.get(self._get, headers=headers, cookies=cookies)
        print(r.request.headers)
        print(r.headers)

    def test_auth(self):
        """测试认证"""
        from requests.auth import HTTPBasicAuth
        r = requests.get(self._get, auth=HTTPBasicAuth("username", "password"))
