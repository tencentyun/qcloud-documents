## 操作场景

该任务指导您使用 Python 语言，通过应用认证来对您的 API 进行认证管理。

## 操作步骤

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“应用认证”（参见 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参见 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台 [应用管理](https://console.cloud.tencent.com/apigateway/app) 界面创建应用。
4. 在应用列表中选中已经创建好的应用，单击**绑定 API**，选择服务和 API 后单击**提交**，即可将应用与 API 建立绑定关系。
5. 参见 [示例代码](#示例代码)，使用 Python 语言生成签名内容。

## 环境依赖

API 网关提供 Python 2.7 和 Python 3 两个版本， 以及 JSON 请求方式和 form 请求方式两种请求方式的示例代码，请您根据自己业务的实际情况合理选择。

## 注意事项

- 应用生命周期管理，以及 API 向应用授权、应用绑定 API 等操作请您参见 [应用管理](https://cloud.tencent.com/document/product/628/55087)。
- 应用生成签名过程请您参见 [应用认证方式](https://cloud.tencent.com/document/product/628/55088)。


## 示例代码[](id:示例代码)

<dx-accordion>
::: Python 2.7 JSON 请求方式示例代码
<dx-codeblock>
:::  python

# -*- coding: utf-8 -*-

import base64
import datetime
import hashlib
import hmac
import json
import requests
from urlparse import urlparse

#应用 ApiAppKey
ApiAppKey = 'Your ApiAppKey'
#应用 ApiAppSecret
ApiAppSecret = 'Your ApiAppSecret'

# apigw 访问地址

Url = 'http://service-xxx-xxx.gz.apigw.tencentcs.com/'
HTTPMethod = 'GET'  # method
Accept = 'application/json'
ContentType = 'application/json'

urlInfo = urlparse(Url)
Host = urlInfo.hostname
Path = urlInfo.path

# 签名path不带环境信息

if Path.startswith(('/release', '/test', '/prepub')) :
    Path = '/' + Path[1:].split('/',1)[1]
Path = Path if Path else '/'

# 拼接query参数，query参数需要按字典序排序

if urlInfo.query :
    queryStr = urlInfo.query
    splitStr = queryStr.split('&')
    splitStr = sorted(splitStr)
    sortStr = '&'.join(splitStr)
    Path = Path + '?' + sortStr 

ContentMD5 = ''
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
xDate = datetime.datetime.utcnow().strftime(GMT_FORMAT)

# 修改 body 内容

if HTTPMethod == 'POST' :
    body = { "arg1": "a", "arg2": "b" }
    body_json = json.dumps(body)
    ContentMD5 = base64.b64encode(hashlib.md5(body_json).hexdigest())

# 获取签名串

signing_str = 'x-date: %s\n%s\n%s\n%s\n%s\n%s' % (
    xDate, HTTPMethod, Accept, ContentType, ContentMD5, Path)

# 计算签名

sign = hmac.new(ApiAppSecret, msg=signing_str, digestmod=hashlib.sha1).digest()
sign = base64.b64encode(sign)
auth = "hmac id=\"" + ApiAppKey + "\", algorithm=\"hmac-sha1\", headers=\"x-date\", signature=\""
sign = auth + sign + "\""

# 发送请求

headers = {
    'Host': Host,
    'Accept': Accept,
    'Content-Type': ContentType,
    'x-date': xDate,
    'Authorization': sign
}
if(HTTPMethod == 'GET'):
    ret = requests.get(Url, headers=headers)
if(HTTPMethod == 'POST'):
    ret = requests.post(Url, headers=headers, data=body_json)

print(ret.headers)
print(ret.text)
:::
</dx-codeblock>
:::
::: Python 2.7 form 请求方式示例代码
<dx-codeblock>
:::  python

# -*- coding: utf-8 -*-

import base64
import datetime
import hashlib
import hmac
import json
import requests
import urllib
from urlparse import urlparse

#应用 ApiAppKey
ApiAppKey = 'Your ApiAppKey'
#应用 ApiAppSecret
ApiAppSecret = 'Your ApiAppSecret'

# apigw 访问地址

Url = 'http://service-xxx-xxx.gz.apigw.tencentcs.com/'
HTTPMethod = 'POST'  # method
Accept = 'application/json'
ContentType = 'application/x-www-form-urlencoded'

urlInfo = urlparse(Url)
Host = urlInfo.hostname
Path = urlInfo.path

# 签名path不带环境信息

if Path.startswith(('/release', '/test', '/prepub')) :
    Path = '/' + Path[1:].split('/',1)[1]
Path = Path if Path else '/'

ContentMD5 = ''
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
xDate = datetime.datetime.utcnow().strftime(GMT_FORMAT)

# 修改 body 内容

body = { "arg1": "a", "arg2": "b" }
argBody = urllib.urlencode(body)

# 签名时，form参数拼接query参数，参数需要按字典序排序

if urlInfo.query :
    argBody = argBody + '&' + urlInfo.query

splitStr = argBody.split('&')
argBody = sorted(splitStr)
sortStr = '&'.join(argBody)
Path = Path + '?' + sortStr

# 获取签名串

signing_str = 'x-date: %s\n%s\n%s\n%s\n%s\n%s' % (
    xDate, HTTPMethod, Accept, ContentType, ContentMD5, Path)

# 计算签名

sign = hmac.new(ApiAppSecret, msg=signing_str, digestmod=hashlib.sha1).digest()
sign = base64.b64encode(sign)
auth = "hmac id=\"" + ApiAppKey + "\", algorithm=\"hmac-sha1\", headers=\"x-date\", signature=\""
sign = auth + sign + "\""

# 发送请求

headers = {
    'Host': Host,
    'Accept': Accept,
    'Content-Type': ContentType,
    'x-date': xDate,
    'Authorization': sign
}
if(HTTPMethod == 'GET'):
    ret = requests.get(Url, headers=headers)
if(HTTPMethod == 'POST'):
    ret = requests.post(Url, headers=headers, data=body)

print(ret.headers)
print(ret.text)
:::
</dx-codeblock>
:::
::: Python 2.7 mutlipart/form-data 请求方式示例代码
<dx-codeblock>
:::  python
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import datetime
import hashlib
import hmac
import httplib, mimetypes
from urlparse import urlparse

# 应用 ApiAppKey
ApiAppKey = 'Your ApiAppKey'
# 应用 ApiAppSecret
ApiAppSecret = 'Your ApiAppSecret'
Url = 'http://service-xxx-xxx.gz.apigw.tencentcs.com/'

# 设置form参数
# fields is a sequence of (name, value) elements for regular form fields.
# files is a sequence of (name, filename, value) elements for data to be uploaded as files
#Example:
#Fields = [("arg1", "a"), ("arg2", "b")]
#Files = [("file", "@test.txt", open("test.txt", "r").read())]
Fields = []
Files = []

HTTPMethod = 'POST'
Accept = 'application/json'

urlInfo = urlparse(Url)
Host = urlInfo.hostname
Path = urlInfo.path

# 签名path不带环境信息
if Path.startswith(('/release', '/test', '/prepub')) :
    Path = '/' + Path[1:].split('/',1)[1]
Path = Path if Path else '/'

# 拼接query参数，query参数需要按字典序排序
if urlInfo.query :
    queryStr = urlInfo.query
    splitStr = queryStr.split('&')
    splitStr = sorted(splitStr)
    sortStr = '&'.join(splitStr)
    Path = Path + '?' + sortStr

GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
xDate = datetime.datetime.utcnow().strftime(GMT_FORMAT)

def post_multipart(host, selector, fields, files):
    content_type, body = encode_multipart_formdata(fields, files)
    
    ContentMD5 = base64.b64encode(hashlib.md5(body).hexdigest())
    # 获取签名串
    signing_str = 'x-date: %s\n%s\n%s\n%s\n%s\n%s' % (
        xDate, HTTPMethod, Accept, content_type, ContentMD5, Path)

    sign = hmac.new(ApiAppSecret, msg=signing_str, digestmod=hashlib.sha1).digest()
    sign = base64.b64encode(sign)
    auth = "hmac id=\"" + ApiAppKey + "\", algorithm=\"hmac-sha1\", headers=\"x-date\", signature=\""
    sign = auth + sign + "\""

    h = httplib.HTTPConnection(host)
    h.putrequest(HTTPMethod, selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.putheader('accept', Accept)
    h.putheader('x-date', xDate)
    h.putheader('Authorization', sign)
    h.endheaders()
    h.send(body)
    response = h.getresponse()
    output = response.read()
    return output

def encode_multipart_formdata(fields, files):
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

output = post_multipart(Host, Path, Fields, Files)

print(output)

:::
</dx-codeblock>

:::
::: Python 3 form 请求方式示例代码
<dx-codeblock>
:::  python

# -*- coding: utf-8 -*-

import base64
import datetime
import hashlib
import hmac
import json
import requests
from urllib.parse import urlparse
from urllib.parse import urlencode

#应用 ApiAppKey
ApiAppKey = 'Your ApiAppKey'
#应用 ApiAppSecret
ApiAppSecret = 'Your ApiAppSecret'

# apigw 访问地址

Url = 'http://service-xxx-xxx.gz.apigw.tencentcs.com/'
HTTPMethod = 'POST'  # method
Accept = 'application/json'
ContentType = 'application/x-www-form-urlencoded'

urlInfo = urlparse(Url)
Host = urlInfo.hostname
Path = urlInfo.path

# 签名path不带环境信息

if Path.startswith(('/release', '/test', '/prepub')) :
    Path = '/' + Path[1:].split('/',1)[1]
Path = Path if Path else '/' 

ContentMD5 = ''
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
xDate = datetime.datetime.utcnow().strftime(GMT_FORMAT)

# 修改 body 内容

body = { "arg1": "a", "arg2": "b" }
argBody = urlencode(body)

# 签名时，form参数拼接query参数，参数需要按字典序排序

if urlInfo.query :
    argBody = argBody + '&' + urlInfo.query

splitStr = argBody.split('&')
argBody = sorted(splitStr)
sortStr = '&'.join(argBody)
Path = Path + '?' + sortStr

# 获取签名串

signing_str = 'x-date: %s\n%s\n%s\n%s\n%s\n%s' % (
    xDate, HTTPMethod, Accept, ContentType, ContentMD5, Path)

# 计算签名

sign = hmac.new(ApiAppSecret.encode(), msg=signing_str.encode(), digestmod=hashlib.sha1).digest()
sign = base64.b64encode(sign).decode()
auth = "hmac id=\"" + ApiAppKey + "\", algorithm=\"hmac-sha1\", headers=\"x-date\", signature=\""
sign = auth + sign + "\""


# 发送请求

headers = {
    'Host': Host,
    'Accept': Accept,
    'Content-Type': ContentType,
    'x-date': xDate,
    'Authorization': sign
}

if HTTPMethod == 'GET' :
    ret = requests.get(Url, headers=headers)
if HTTPMethod == 'POST' :
    ret = requests.post(Url, headers=headers, data=body)

print(ret.headers)
print(ret.text)
:::
</dx-codeblock>
:::
::: Python 3 json 请求方式示例代码
<dx-codeblock>
:::  python
# -*- coding: utf-8 -*-
import base64
import datetime
import hashlib
import hmac
import json
import requests
from urllib.parse import urlparse

#应用 ApiAppKey
ApiAppKey = 'Your ApiAppKey'
#应用 ApiAppSecret
ApiAppSecret = 'Your ApiAppSecret'

# apigw 访问地址
Url = 'http://service-xxx-xxx.gz.apigw.tencentcs.com/'
HTTPMethod = 'GET'  # method
Accept = 'application/json'
ContentType = 'application/json'

urlInfo = urlparse(Url)
Host = urlInfo.hostname
Path = urlInfo.path

# 签名path不带环境信息
if Path.startswith(('/release', '/test', '/prepub')) :
    Path = '/' + Path[1:].split('/',1)[1]
Path = Path if Path else '/'

# 拼接query参数，query参数需要按字典序排序
if urlInfo.query :
    queryStr = urlInfo.query
    splitStr = queryStr.split('&')
    splitStr = sorted(splitStr)
    sortStr = '&'.join(splitStr)
    Path = Path + '?' + sortStr

ContentMD5 = ''
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
xDate = datetime.datetime.utcnow().strftime(GMT_FORMAT)

# 修改 body 内容
if HTTPMethod == 'POST' :
    body = { "arg1": "a", "arg2": "b" }
    body_json = json.dumps(body)
    body_md5 = hashlib.md5(body_json.encode()).hexdigest()
    ContentMD5 = base64.b64encode(body_md5.encode()).decode()

# 获取签名串
signing_str = 'x-date: %s\n%s\n%s\n%s\n%s\n%s' % (
    xDate, HTTPMethod, Accept, ContentType, ContentMD5, Path)

# 计算签名
sign = hmac.new(ApiAppSecret.encode(), msg=signing_str.encode(), digestmod=hashlib.sha1).digest()
sign = base64.b64encode(sign).decode()
auth = "hmac id=\"" + ApiAppKey + "\", algorithm=\"hmac-sha1\", headers=\"x-date\", signature=\""
sign = auth + sign + "\""


# 发送请求
headers = {
    'Host': Host,
    'Accept': Accept,
    'Content-Type': ContentType,
    'x-date': xDate,
    'Authorization': sign
}

if HTTPMethod == 'GET' :
    ret = requests.get(Url, headers=headers)
if HTTPMethod == 'POST' :
    ret = requests.post(Url, headers=headers, data=body_json)

print(ret.headers)
print(ret.text)
:::
</dx-codeblock>
:::
::: Python 3 mutlipart/form-data 请求方式示例代码
<dx-codeblock>
:::  python
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import datetime
import hashlib
import hmac
import http.client as httplib
import mimetypes
from urllib.parse import urlparse


# 应用 ApiAppKey
ApiAppKey = 'Your ApiAppKey'
# 应用 ApiAppSecret
ApiAppSecret = 'Your ApiAppSecret'
Url = 'http://service-xxx-xxx.gz.apigw.tencentcs.com/'

# 设置form参数
# fields is a sequence of (name, value) elements for regular form fields.
# files is a sequence of (name, filename, value) elements for data to be uploaded as files
#Example:
#Fields = [("arg1", "a"), ("arg2", "b")]
#Files = [("file", "@test.txt", open("test.txt", "r").read())]
Fields = []
Files = []

HTTPMethod = 'POST'
Accept = 'application/json'

urlInfo = urlparse(Url)
Host = urlInfo.hostname
Path = urlInfo.path

# 签名path不带环境信息
if Path.startswith(('/release', '/test', '/prepub')) :
    Path = '/' + Path[1:].split('/',1)[1]
Path = Path if Path else '/'

# 拼接query参数，query参数需要按字典序排序
if urlInfo.query :
    queryStr = urlInfo.query
    splitStr = queryStr.split('&')
    splitStr = sorted(splitStr)
    sortStr = '&'.join(splitStr)
    Path = Path + '?' + sortStr

GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
xDate = datetime.datetime.utcnow().strftime(GMT_FORMAT)

def post_multipart(host, selector, fields, files):
    content_type, body = encode_multipart_formdata(fields, files)
    
    body_md5 = hashlib.md5(body.encode()).hexdigest()
    ContentMD5 = base64.b64encode(body_md5.encode()).decode()
    #ContentMD5 = base64.b64encode((hashlib.md5(body.encode).hexdigest()).encode).decode()
    # 获取签名串
    signing_str = 'x-date: %s\n%s\n%s\n%s\n%s\n%s' % (
        xDate, HTTPMethod, Accept, content_type, ContentMD5, Path)

    sign = hmac.new(ApiAppSecret.encode(), msg=signing_str.encode(), digestmod=hashlib.sha1).digest()
    sign = base64.b64encode(sign).decode()
    auth = "hmac id=\"" + ApiAppKey + "\", algorithm=\"hmac-sha1\", headers=\"x-date\", signature=\""
    sign = auth + sign + "\""

    h = httplib.HTTPConnection(host)
    h.putrequest(HTTPMethod, selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.putheader('accept', Accept)
    h.putheader('x-date', xDate)
    h.putheader('Authorization', sign)
    h.endheaders()
    h.send(body.encode())
    response = h.getresponse()
    output = response.read().decode()
    return output

def encode_multipart_formdata(fields, files):
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

output = post_multipart(Host, Path, Fields, Files)

print(output)

:::
</dx-codeblock>
:::
</dx-accordion>


