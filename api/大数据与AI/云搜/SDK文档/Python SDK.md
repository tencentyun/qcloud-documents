qcloudapi-sdk-python 是为了让 Python 开发者能够在自己的代码里更快捷方便的使用腾讯云的 API 而开发的 SDK 工具包。

### 使用方法
1. 申请安全凭证。
在第一次使用云 API 之前，首先需要在腾讯云网站上申请安全凭证，安全凭证包括 SecretId 和 SecretKey，SecretId 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。
2. 使用 SDK
下载 SDK，放入到程序目录，使用方法请参考下面的示例。

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
    '''
    module = 'sec'

    '''
    action 对应接口的接口名，请参考wiki文档上对应接口的接口名
    '''
    action = 'CaptchaQuery'

    config = {
        'Region': '区域参数',
        'secretId': '您的secretId',
        'secretKey': '您的secretKey',
        'method': 'get'
    }

    '''
    params 请求参数，请参考 wiki 文档上对应接口的说明
    '''
    params = {
        'userIp': '10.0.0.1',
        'businessId': 1,
        'captchaType': 1,
        'script': 0,
        # 'Region': 'gz',当 Region 不是上面配置的 DefaultRegion 值时，可以重新指定请求的 Region
        # 'SignatureMethod':'HmacSHA256',指定所要用的签名算法，可选 HmacSHA256 或 HmacSHA1，默认为 HmacSHA1
        }
        
    try:
        service = QcloudApi(module, config)

        # 请求前可以通过下面四个方法重新设置请求的 secretId/secretKey/region/method 参数
        # 重新设置请求的 secretId
        secretId = '您的secretId'
        service.setSecretId(secretId)
        # 重新设置请求的 secretKey
        secretKey = '您的secretKey'
        service.setSecretKey(secretKey)
        # 重新设置请求的 region
        region = 'sh'
        service.setRegion(region)
        # 重新设置请求的 method
        method = 'post'
        service.setRequestMethod(method)

        # 生成请求的 URL，不发起请求
        print service.generateUrl(action, params)
        # 调用接口，发起请求
        print service.call(action, params)
    except Exception, e:
        print 'exception:', e
```

### 常见问题
* 如果碰到 `ImportError: No module named requests.auth` 请安装 [request](https://github.com/kennethreitz/requests)。
