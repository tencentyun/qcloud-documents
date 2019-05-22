为方便Python开发者调试和接入云API， 我们提供了基于Python的SDK。

[从 Githb 访问 >>](https://github.com/QcloudApi/qcloudapi-sdk-python)

qcloudapi-sdk-python 是为了让 Python 开发者能够在自己的代码里更快捷方便的使用腾讯云的 API 而开发的 SDK 工具包。我们已经将其打包发布到 [pypi](https://pypi.python.org/pypi/qcloudapi-sdk-python/) ，您可以使用 pip 工具将 SDK 安装到本地，pip 工具在各操作系统的安装方式请参考[如何安装python环境和pip工具](https://cloud.tencent.com/doc/product/440/6181)。您也可以将其添加到项目的依赖列表中，或者使用 [git submodule](https://git-scm.com/docs/git-submodule) 功能将其直接置于您的项目中。

## 资源
见不同模块API的公共参数、API概览、错误码。如[云服务器API公共参数](http://cloud.tencent.com/document/api/213/6976)、[云服务器API概览](http://cloud.tencent.com/doc/api/229/API%E6%A6%82%E8%A7%88)、[云服务器API错误码](http://cloud.tencent.com/doc/api/229/%E9%94%99%E8%AF%AF%E7%A0%81)。

## 获取安全凭证
[获取安全凭证](https://console.cloud.tencent.com/capi)。在第一次使用云API之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretId 和 SecretKey, SecretId 是用于标识 API 调用者的身份，SecretKey是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

## 示例

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

## 常见问题
如果碰到ImportError: No module named requests.auth 请安装 requests([request说明](https://github.com/kennethreitz/requests))。
