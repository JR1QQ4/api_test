#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest
import os

from demo_b.api.base_api import BaseApi
from demo_b.util.handle_path import conf_dir
from demo_b.util.handle_yaml import HandleYaml


@pytest.fixture(scope="session")
def token():
    token_yaml = os.path.join(conf_dir, "token.yaml")
    token = HandleYaml(token_yaml).get_section()
    api = BaseApi()
    return api.send(token).json()['access_token']