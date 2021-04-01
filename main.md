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