# 接口测试

## requests

### 发送请求

```python
import requests
# get 
payload = {"key1": "value1", "key2": "value2"}
r = requests.get("http://www.httpbin.org/get", params=payload)
print(r.text)
# post 
payload = {"key1": "value1", "key2": "value2"}
r = requests.post("http://www.httpbin.org/post", data=payload)
print(r.text)
```

#### 添加 Cookie

两种方式传递 Cookie，只能选择一种方式传递，两个都选择会忽略 cookies

```python
import requests
# 第一种方法
headers = {
    # "Cookie": "username=password",
    "User-Agent": "wang"
}
# 第二种方法
cookies = {"su": "todo"}
r = requests.get("http://www.httpbin.org/get", headers=headers, cookies=cookies)
```

#### 认证体系

```python
import requests
from requests.auth import HTTPBasicAuth
r = requests.get("http://www.httpbin.org/get", auth=HTTPBasicAuth("username", "password"))
```

### 结果分析

```python
# get
get = {
  "args": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "www.httpbin.org", 
    "User-Agent": "python-requests/2.25.0", 
    "X-Amzn-Trace-Id": "Root=1-60655596-48bb11dd2d0a51383097f0aa"
  }, 
  "url": "http://www.httpbin.org/get?key1=value1&key2=value2"
}
# post_form
post_form = {
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "X-Amzn-Trace-Id": "Root=1-606554b8-3ab04b9e4e6408c912747ca8"
  }, 
  "json": "null", 
  "url": "http://www.httpbin.org/post"
}
# post_json
post_json = {
  "args": {}, 
  "data": "{\"key1\": \"value1\", \"key2\": \"value2\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Content-Length": "36", 
    "Content-Type": "application/json", 
    "X-Amzn-Trace-Id": "Root=1-606558ed-7e9795b254f7f71b46c898f6"
  }, 
  "json": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "url": "http://www.httpbin.org/post"
}
```

### 响应结果

- r.text = r.encoding + r.content
- r.json() = r.encoding + r.content + content type json
- r.raw.read(10)
- r.request
- r.headers
- r.cookies
- r.url
- r.status_code

### 模板字符串

mustache
- pystache：pip install pystache

```python
import pystache
context = {'author': 'Chris Wanstrath', 'maintainer': 'Chris Jerdonek'}
result = pystache.render("Author: {{author}}\nMaintainer: {{maintainer}}", context)
print(result)
```

### json 断言

json_path: pip install jsonpath

```python
from jsonpath import jsonpath
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
```

### xml 断言

requests_xml：pip install requests-xml

```python
from requests_xml import XMLSession
session = XMLSession()
r = session.get('https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss')
print(r.xml.links)
```

### hamcrest 断言

hamcrest：pip install PyHamcrest

```python
from hamcrest import *
assert_that("hamcrest", equal_to_ignoring_case("Hamcrest"))
```

### schema 断言

json_schema：pip install jsonschema

```python
from jsonschema import validate
schema = {
    "type": "object",
    "properties": {
        "price": {"type": "number"},
        "name": {"type": "string"},
    },
}
validate(instance={"name": "Eggs", "price": 34.99}, schema=schema)
validate(
    instance={"name": "Eggs", "price": "Invalid"}, schema=schema,
)  # <ValidationError: "'Invalid' is not of type 'number'">
```

## 框架

### Api 对象

- 架构设计
    - 多协议支持，http tcp thrift等，需要不同的底层引擎
    - 保证用例和协议无关，基于接口或者抽象实现；把不变的作为一种抽象，把变的作为一种实现
- 实现
    - code方式：输出=业务.功能（输入）
    - 配置文件方式：yaml格式、json格式

### 架构实现和管理

- 架构的实现
    - Java + RestAssured + JUnit4/JUnit5/TestNG + Allure2
    - Python + Requests + PyTest + Allure2 = HttpRunner
- 架构管理
    - 使用 package 管理业务模块
    - 使用 class 管理业务功能
    - 使用 method 完成业务具体行为
    - 使用配置文件读取初始配置
    - 使用集成规划用例执行顺序
    - 使用 testcase 完成测试用例的落地
    - 使用数据文件管理用例的数据驱动
    - 使用 jenkins 完成持续集成

### 基于加密接口的测试用例设计

在得到响应后对响应做解密处理
1. 如果知道使用的是哪个通用加密算法的话，自行解决
2. 如果不了解对应的加密算法的话，可以让研发提供加解密的 lib 
3. 如果既不是通用加密算法、研发也无法提供加解密的 lib 的话，可以让加密方提供远程解析服务，这样算法依然是保密的

### 多环境下的接口测试

在请求之前，对请求的 url 进行替换
1. 需要二次封装 requests，对请求进行定制化
2. 将请求的结构体的 url 从一个写死的 ip 地址改为一个（任意的）域名
3. 使用一个 env 配置文件，存放各个环境的配置信息
4. 然后将请求结构体中的 url 替换为 env 配置文件中个人选择的 url
5. 将 env 配置文件使用 yaml 进行管理

### api object

原则
- 每个公共方法代表接口所提供功能
- 不要暴露 api 内部细节
- 不要再接口实现层写断言
- 每个 method 返回其他的 api object 或者用来断言的信息
- 不需要每个 api 都进行实现，只要与 case 相关的才进行实现

### 框架封装

- 测试步骤的数据驱动
    - 使用 yaml 文件对测试步骤进行数据驱动
    - 在 yaml 文件中实现变量传递，使用 Template 进行模板替换
- 测试数据的数据驱动
    - 使用 @pytest.mark.parameterize() 传参
    - 使用 yaml、JSON、CSV 等等文件管理测试数据
- 配置的数据驱动
    - 把配置信息保存在 yaml、JSON 等文件中进行管理
- 通用测试用例封装
    - 创建一个 TestBase 类，其他的 case 都继承于 TestBase
- 通用测试框架构建

rabotframework






