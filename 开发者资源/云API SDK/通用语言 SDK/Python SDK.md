# Python SDK
## 简介
欢迎使用腾讯云开发者工具套件（SDK）。为方便 Python 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 Python 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 Python SDK 并开始调用。

## 依赖环境
1.  依赖环境：Python 2.6 到 3.6 版本
2. 从 [腾讯云控制台](https://console.qcloud.com) 开通相应产品，
3. [获取 SecretID、SecretKey](https://console.qcloud.com/capi) 具体参考各产品说明。
4. 下载相关资料并做好相关文件配置。

## 获取安装
安装 Python SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey, SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

### 通过 GitHub 获取源码安装
打开腾讯云为您提供的 PHP SDK GitHub 地址，[获取 GitHub 资源 >>](https://github.com/QcloudApi/qcloudapi-sdk-python)。
1. 在 `qcloudapi-sdk-python`的 github 地址上下载源码
2. 解压源码到您项目合适的位置
3. 安装到项目：
```
    $ git clone https://github.com/QcloudApi/qcloudapi-sdk-python
    $ cd qcloudapi-sdk-python
    $ python setup.py install
```

### 通过 pip 获取安装
您可以通过 pip 安装方式将腾讯云 Python SDK 安装到您的项目中，如果您的项目环境尚未安装 pip，请详细参见 [pip官网](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o) 安装。
```
$ pip install qcloudapi-sdk-python
```


## 入门 DEMO
以 CVM 查询（DescribeInstances）为例：
```
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
from QcloudApi.qcloudapi import QcloudApi

'''
module: 设置需要加载的模块
已有的模块列表：
cvm      对应   cvm.api.qcloud.com
cdb      对应   cdb.api.qcloud.com
lb       对应   lb.api.qcloud.com
trade    对应   trade.api.qcloud.com
sec      对应   csec.api.qcloud.com
image    对应   image.api.qcloud.com
monitor  对应   monitor.api.qcloud.com
cdn      对应   cdn.api.qcloud.com
'''
module = 'cvm'

'''
action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
'''
action = 'DescribeInstances'

'''
config: 云API的公共参数
'''
config = {
    'Region': 'ap-guangzhou',
    'secretId': '您的secretId',
    'secretKey': '您的secretKey',
}

# 接口参数
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