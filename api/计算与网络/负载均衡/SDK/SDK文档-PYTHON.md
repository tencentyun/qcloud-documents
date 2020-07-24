## CLB SDK 使用说明

## Python SDK 使用简介(Linux)

### 环境依赖
Python 2.x 目前不支持 Python 3

依赖的库：requests

获取 Python 版本的方法（Linux Shell ）：

```

    $python -V

    Python 2.7.11
```

### CLB SDK 下载与配置
#### 云 API 密钥使用说明
使用 SDK 时，首先需要用户的云 API 密钥，云 API 密钥是对用户身份的合法性验证。

获取云 API 密钥的方法如下：
1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在左侧导航栏选择【访问密钥】>【API 密钥管理】。
2. 用户可在此新建新的云 API 密钥或使用现有密钥。
![](https://main.qcloudimg.com/raw/ad5adad7719bf7aa6d7979d9f6f617ae.png)


#### CLB Python SDK下载
下载最新版 [CLB Python SDK](http://clbsdk-1251740579.cossh.myqcloud.com/CLB_PYTHON_SDK_0.0.3.zip)。

                          
### 使用 CLB Python SDK

#### 1. 配置云 API 密钥
在 SDK 的文件 `CLB_SDK_0.0.1/src/QcloudApi/qcloudapi.py` 指定 secretId 和 secretKey，以下为该文件中的部分代码：

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

下面的代码在 Python SDK 中的 sample/application 目录下，创建负载均衡四层监听器的接口 CreateForwardLBFourthLayerListeners.py，代码中 `region` 指的是要操作的实例的地域，根据实际情况来指定。

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'CreateForwardLBFourthLayerListeners'  # 创建负载均衡四层监听器

"""
loadBalancerId 必传 负载均衡ID
listeners.n.loadBalancerPort  必传   负载均衡监听器监听端口
listeners.n.protocol          必传   负载均衡监听器监听协议 2：TCP， 3：UDP
listeners.n.listenerName      非必传 负载均衡监听器名字
listeners.n.sessionExpire	 非必传	负载均衡监听器的会话保持时间，单位: 秒。内网负载均衡暂不支持会话保持,默认 0，表示不开启。
listeners.n.healthSwitch	  非必传	负载均衡实例监听器是否开启健康检查：1（开启）、0（关闭）。默认值1，表示打开。
listeners.n.timeOut	       非必传	负载均衡监听器健康检查的响应超时时间，可选值:2-60，默认值:2，单位:秒。响应超时时间要小于检查间隔时间。
listeners.n.intervalTime	  非必传	负载均衡监听器检查间隔时间，默认值:5，可选值:5-300，单位:秒。
listeners.n.healthNum	     非必传	负载均衡监听器健康阈值，默认值:3，表示当连续探测三次健康则表示该转发正常，可选值:2-10，单位：次。
listeners.n.unhealthNum	   非必传	负载均衡监听器不健康阈值，默认值:3，表示当连续探测三次健康则表示该转发正常，可选值:2-10，单位：次。

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
