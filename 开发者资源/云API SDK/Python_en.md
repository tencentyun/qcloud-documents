Tencent Cloud provides Python-based SDKs for Python developers.

Github directory: <br>https://github.com/QcloudApi/qcloudapi-sdk-python

With the qcloudapi-sdk-python tool kit, Python developers can use Tencent Cloud APIs easily in their codes.


## 1. Resources
You can find common parameters, API overviews and error codes for each Tencent Cloud products from their documents, like [CVM API Common Request Parameters](http://cloud.tencent.com/doc/api/229/%E5%85%AC%E5%85%B1%E5%8F%82%E6%95%B0), [CVM API Overview](http://cloud.tencent.com/doc/api/229/API%E6%A6%82%E8%A7%88), [CVM API Error Codes](http://cloud.tencent.com/doc/api/229/%E9%94%99%E8%AF%AF%E7%A0%81).

## 2. Installation
Install Python environment. (Skip this step if your environment is ready)
```
$ wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
$ tar -zxvf Python-2.7.12.tgz
$ cd Python-2.7.12
$ ./configure
$ make
$ sudo make install
```
## 3. Getting Started
1) Obtain the security credential on the [Console](https://console.cloud.tencent.com/capi). Before using Tencent Cloud APIs, you need to apply for security credential on the Console. The security credential includes SecretId (indicating the identity of API calling entity) and SecretKey (used for signature encryption, must be kept safe).


2) [Download SDK](https://github.com/QcloudApi/qcloudapi-sdk-python) and add it to your program directory. See the sample codes below:

## 4. Sample Codes

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import the Tencent Cloud API main module
from src.QcloudApi.qcloudapi import QcloudApi

'''
module Modules you want to load
Exisiting module list:
cvm      refer to   cvm.api.qcloud.com
cdb      refer to   cdb.api.qcloud.com
lb       refer to   lb.api.qcloud.com
trade    refer to   trade.api.qcloud.com
sec      refer to   csec.api.qcloud.com
image    refer to   image.api.qcloud.com
monitor  refer to   monitor.api.qcloud.com
cdn      refer to   cdn.api.qcloud.com
wenzhi   refer to   wenzhi.api.qcloud.com
'''
module = 'sec'

'''
action Corresponding API names （see the API name stated in the product document)
'''
action = 'CaptchaQuery'

config = {
    'Region': 'Region parameter',
    'secretId': 'Your secretId',
    'secretKey': 'Your secretKey',
    'method': 'get'
}

'''
params Request parameters (see details from related product API files)
'''
params = {
    'userIp': '127.0.0.1',
    'businessId': 1,
    'captchaType': 1,
    'script': 0,
    \# 'Region': 'gz', # When the Region you want is not the one configured in DefaultRegion, you can specify the Region again.
}
try:
    service = QcloudApi(module, config)

    # Before starting the request, you can reset its secretId/secretKey/region/method parameters as belows:
    # Reset secretId of the request
    secretId = 'Your secretId'
    service.setSecretId(secretId)
    # Reset secretKey of the reqeust
    secretKey = 'Your secretKey'
    service.setSecretKey(secretKey)
    # Reset region of the request
    region = 'sh'
    service.setRegion(region)
    # Reset method of the request
    method = 'post'
    service.setRequestMethod(method)

    # Generate the request URL, but not start the request
    print service.generateUrl(action, params)
    # Call the API and start the request
    print service.call(action, params)
except Exception, e:
    print 'exception:', e

```

## 5. FAQ
If the message *"ImportError: No module named requests.auth"* appears, please install *requests* (see [here](https://github.com/kennethreitz/requests) for details).
