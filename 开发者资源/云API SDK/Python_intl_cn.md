为方便Python开发者调试和接入云API， 我们提供了基于Python的SDK。

[从 Githb 访问 >>](https://github.com/QcloudApi/qcloudapi-sdk-python)
[点击下载 Python SDK >>](https://mc.qcloudimg.com/static/archive/b61ee1ce734e7437530304152c20ee14/qcloudapi-sdk-python-master.zip)

qcloudapi-sdk-python 是为了让 Python 开发者能够在自己的代码里更快捷方便的使用腾讯云的 API 而开发的 SDK 工具包。


## 1. 资源
见不同模块API的公共参数、API概览、错误码。如[云服务器API公共参数](http://cloud.tencent.com/document/api/213/6976)、[云服务器API概览](http://cloud.tencent.com/doc/api/229/API%E6%A6%82%E8%A7%88)、[云服务器API错误码](http://cloud.tencent.com/doc/api/229/%E9%94%99%E8%AF%AF%E7%A0%81)。

## 2. 安装
安装python环境，若已有python环境可跳过本步骤。
```
$ wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
$ tar -zxvf Python-2.7.12.tgz
$ cd Python-2.7.12
$ ./configure
$ make
$ sudo make install
```
## 3. 入门
1) [获取安全凭证](https://console.cloud.tencent.com/capi)。在第一次使用云API之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretId 和 SecretKey, SecretId 是用于标识 API 调用者的身份，SecretKey是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。


2) 下载SDK，放入到您的程序目录。详细使用方法请参考下面的示例。
[从 Githb 访问 >>](https://github.com/QcloudApi/qcloudapi-sdk-python)
[点击下载 Python SDK >>](https://mc.qcloudimg.com/static/archive/b61ee1ce734e7437530304152c20ee14/qcloudapi-sdk-python-master.zip)

## 4. 示例

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
from src.QcloudApi.qcloudapi import QcloudApi

'''
module 设置需要加载的模块
已有的模块列表：
cvm      对应   cvm.api.qcloud.com
cdb      对应   cdb.api.qcloud.com
lb       对应   lb.api.qcloud.com
trade    对应   trade.api.qcloud.com
sec      对应   csec.api.qcloud.com
image    对应   image.api.qcloud.com
monitor  对应   monitor.api.qcloud.com
cdn      对应   cdn.api.qcloud.com
wenzhi   对应   wenzhi.api.qcloud.com
'''
module = 'sec'

'''
action 对应接口的接口名，请参考产品文档上对应接口的接口名
'''
action = 'CaptchaQuery'

config = {
    'Region': '区域参数',
    'secretId': '你的secretId',
    'secretKey': '你的secretKey',
    'method': 'get'
}

'''
params 请求参数，请参考产品文档上对应接口的说明
'''
params = {
    'userIp': '127.0.0.1',
    'businessId': 1,
    'captchaType': 1,
    'script': 0,
    # 'Region': 'gz', # 当Region不是上面配置的DefaultRegion值时，可以重新指定请求的Region
}
try:
    service = QcloudApi(module, config)

    # 请求前可以通过下面四个方法重新设置请求的secretId/secretKey/region/method参数
    # 重新设置请求的secretId
    secretId = '你的secretId'
    service.setSecretId(secretId)
    # 重新设置请求的secretKey
    secretKey = '你的secretKey'
    service.setSecretKey(secretKey)
    # 重新设置请求的region
    region = 'sh'
    service.setRegion(region)
    # 重新设置请求的method
    method = 'post'
    service.setRequestMethod(method)

    # 生成请求的URL，不发起请求
    print service.generateUrl(action, params)
    # 调用接口，发起请求
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
```

## 4. 常见问题
如果碰到ImportError: No module named requests.auth 请安装 requests([request说明](https://github.com/kennethreitz/requests))。
