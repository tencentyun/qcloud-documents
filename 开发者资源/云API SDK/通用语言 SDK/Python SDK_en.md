
## Overview
Welcome to Tencent Cloud Software Development Kit (SDK). To help Python developers debug and connect to the Tencent Cloud product API, here we introduce the Tencent Cloud SDK suitable for Python, and provide a simple example of getting started with the SDK. Then, you can quickly get the Tencent Cloud Python SDK and start calling.

## Supported Environment
1. Supported environment: Python version 2.6 to 3.6
2. Activate the corresponding product on [Tencent Cloud Console](https://console.cloud.tencent.com).
3. [Get SecretID and SecretKey](https://console.cloud.tencent.com/capi). For more information, please see product descriptions.
4. Download the relevant information and configure the relevant files.

## Installation
Before installing Python SDK, you should obtain the security credential first. Before calling the Cloud API for the first time, you need to apply for a security credential on the Tencent Cloud console. A security credential consists of a SecretID, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and the key used to verify the signature string on the server end. You must keep your SecretKey strictly confidential to avoid disclosure.

### Obtaining Source Code via GitHub for Installation
Click on the GitHub address of Python SDK provided by Tencent Cloud. [Get GitHub resources >>](https://github.com/QcloudApi/qcloudapi-sdk-python).
1. Download source code from the Github address of `qcloudapi-sdk-python`
2. Extract the source code to the proper location of your project
3. Install the source code to the project:
```
    $ git clone https://github.com/QcloudApi/qcloudapi-sdk-python
    $ cd qcloudapi-sdk-python
    $ python setup.py install
```

### Installing via pip
You can install Tencent Cloud Python SDK into your project using pip. If pip has not been installed in your project environment, please see [pip official website](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o) for installation.
```
$ pip install qcloudapi-sdk-python
```


## Quick Start Demo
Take CVM's "Query" (DescribeInstances) as an example:
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Introduce the Cloud API entry module
from QcloudApi.qcloudapi import QcloudApi

'''
module: Set the module to be loaded
List of existing modules:
cvm      corresponds to   cvm.api.qcloud.com
cdb      corresponds to   cdb.api.qcloud.com
lb       corresponds to   lb.api.qcloud.com
trade    corresponds to   trade.api.qcloud.com
sec      corresponds to   csec.api.qcloud.com
image    corresponds to   image.api.qcloud.com
monitor  corresponds to   monitor.api.qcloud.com
cdn      corresponds to   cdn.api.qcloud.com
'''
module = 'cvm'

'''
action: Corresponds to the API name. Refer to the API name of the corresponding API in the product documentation
'''
action = 'DescribeInstances'

'''
config: The public parameter of Cloud API
'''
config = {
    'Region': 'ap-guangzhou',
    'secretId': 'Your secretId',
    'secretKey': 'Your secretKey',
}

# API Parameters
action_params = {
    'limit':1,
}

try:
    service = QcloudApi(module, config)
    print(service.generateUrl(action, action_params))
    print(service.call(action, action_params))
except Exception as e:
    import traceback
    print('traceback.format_exc():\n%s' % traceback.format_exc())
```

