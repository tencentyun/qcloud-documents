## CLB SDK 使用说明文档

## PYTHON SDK 使用简介(Linux)

### 环境依赖
python2.x 目前不支持python3

依赖的库 requests

获取python版本的方法：

linux shell 

```

    $python -V

    Python 2.7.11
```

### CLB SDK 下载与配置
#### 云 API 密钥使用说明
使用 SDK 时，首先需要用户的云 API 密钥，云 API 密钥是对用户身份的合法性验证。获取云 API 密钥的方法如下：登录[腾讯云控制台](https://console.qcloud.com/)，选择【云产品】-【云 API 密钥】选项

![](https://mc.qcloudimg.com/static/img/b04d51df61bc4e9259dcee293981b644/5.png)

用户可在此新建新的云 API 密钥或使用现有密钥。点击密钥 ID 进入详情页获取使用的密钥 secretId 和对应的 secretKey。
![](https://mc.qcloudimg.com/static/img/47b2cf18add4d32a867f115fffb6af48/2.png)





#### CLB PYTHON SDK下载
下载最新版[CLB PYTHON SDK](http://clbsdk-1251740579.cossh.myqcloud.com/CLB_PYTHON_SDK_0.0.1.zip)


### 使用 CLB PYTHON SDK

#### 1. 配置云 API 密钥
在SDK的文件CLB_SDK_0.0.1/src/QcloudApi/qcloudapi.py指定secretId和secretKey，以下为该文件中的部分代码：

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

config = {
    'Region':'gz',
    'secretId': '',
    'secretKey': '',
    'method': 'post'
}

class QcloudApi:
    def __init__(self, module='lb', config=config, region='gz'):
```

#### 2. 针对具体某个接口的使用示例：

下面的代码也是 PYTHON SDK 中的sample/application下的，创建应用型负载均衡四层监听器的接口CreateForwardLBFourthLayerListeners.py， 代码中region指的是要操作的实例的地域，根据实际情况来指定

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'CreateForwardLBFourthLayerListeners'  # 创建应用型负载均衡四层监听器

"""
loadBalancerId 必传 负载均衡ID
listeners.n.loadBalancerPort 必传   负载均衡监听器监听端口
listeners.n.protocol         必传   负载均衡监听器监听协议 2：TCP， 3：UDP
listeners.n.listenerName     非必传 负载均衡监听器名字
listeners.n.sessionExpire	非必传	负载均衡监听器的会话保持时间，单位: 秒。内网负载均衡暂不支持会话保持,默认 0，表示不开启。
listeners.n.healthSwitch	非必传	负载均衡实例监听器是否开启健康检查：1（开启）、0（关闭）。默认值1，表示打开。
listeners.n.timeOut	非必传	负载均衡监听器健康检查的响应超时时间，可选值:2-60，默认值:2，单位:秒。响应超时时间要小于检查间隔时间。
listeners.n.intervalTime	非必传	负载均衡监听器检查间隔时间，默认值:5，可选值:5-300，单位:秒。
listeners.n.healthNum	非必传	负载均衡监听器健康阀值，默认值:3，表示当连续探测三次健康则表示该转发正常，可选值:2-10，单位：次。
listeners.n.unhealthNum	非必传	负载均衡监听器不健康阀值，默认值:3，表示当连续探测三次健康则表示该转发正常，可选值:2-10，单位：次。

"""
region = 'gz'
params = {
    'loadBalancerId': "lb-j2nvt9hq",
    'listeners.0.loadBalancerPort': 80,
    'listeners.0.protocol': 2,
    'listeners.0.listenerName': "test",
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e

```