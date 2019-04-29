## 最终的请求 URL 的组成
最终的请求 URL 由以下几部分组成：
- **请求域名：**[查询私有网络列表](https://cloud.tencent.com/document/product/215/1372)(DescribeVpcEx)的请求域名为`vpc.api.qcloud.com`。实际的请求域名根据接口所属模块的不同而不同, 详见各接口说明。
- **请求路径：** 云 API 的请求路径固定为`/v2/index.php`。
- **最终请求参数串：** 包括公共请求参数和接口请求参数。

## 最终的请求 URL 的拼接规则
最终的请求 URL 的拼接规则为： `https://` + `请求域名` +`请求路径 `+ `?` +`最终请求参数串`

因此，我们得到最终的请求 URL 如下，其中前 6 个参数为公共请求参数，其后参数为接口请求参数。

```
https://vpc.api.qcloud.com/v2/index.php?
Action=DescribeVpcEx
&SecretId=您的secretId
&Region=gz
&Timestamp=1507645389
&Nonce=59485
&Signature=本串的签名(可参考后台示例程序或官网其它说明文档)
&vpcId=vpc-2ari9m7h
&offset=0
&limit=1
&orderDirection=desc
```
## 最终的请求 URL 的帮助小程序

获取最终请求 URL 的示例程序：
- 本示例修改自腾讯云官网提供的云 api python SDK，旨在帮助用户了解签名及最终请求串。
- 正式使用时，建议使用 [官网提供的 SDK](https://cloud.tencent.com/document/developer-resource)，如`pip install qcloudapi-sdk-python` 。 使用  SDK 时，可以方便的填写参数，而后实现云 API 调用，优于本示例程序。

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import binascii
import hashlib
import hmac
import sys
import time
import random

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

class Sign:
    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey
        if sys.version_info[0] > 2:
            self.Py2 = False
        else:
            self.Py2 = True

    def make(self, requestHost, requestUri, params, method = 'POST', sign_method='HmacSHA1'):
        new_params = {}
        for param_key in params:
            if method == 'POST' and str(params[param_key])[0:1] == "@":
                continue
            new_params[param_key] = params[param_key]
        #签名用的串有字典序的要求
        srcStr = method.upper() + requestHost + requestUri + '?' + "&".join(k.replace("_",".") + "=" + str(new_params[k]) for k in sorted(new_params.keys()))  
        print "url string for making a signature: " + srcStr
        if sign_method == 'HmacSHA256':
            if self.Py2:
                hashed = hmac.new(self.secretKey, srcStr, hashlib.sha256)
            else:
                hashed = hmac.new(bytes(self.secretKey, 'latin-1'), bytes(srcStr, 'latin-1'), hashlib.sha256)
        else:
            if self.Py2:
                hashed = hmac.new(self.secretKey, srcStr, hashlib.sha1)
            else:
                hashed = hmac.new(bytes(self.secretKey, 'latin-1'), bytes(srcStr, 'latin-1'), hashlib.sha1)

        if self.Py2:
            return binascii.b2a_base64(hashed.digest())[:-1]
        else:
            return binascii.b2a_base64(hashed.digest())[:-1].decode()

    def getUrl(self, requestHost, requestUri, params):
        sign_str = self.make(requestHost, requestUri, params, method='GET')
        print "Signature: " + sign_str
        params['Signature'] = sign_str
        data_str = urlencode(params)
        final_url = "https://" + requestHost + requestUri + '?' + data_str 
        return final_url


def main():
    ''' 
    本示例得到的最终请求串
    https://vpc.api.qcloud.com/v2/index.php?Nonce=2659996141967&SecretId=您的secretId&limit=1&offset=0&Action=DescribeVpcEx&Timestamp=1507699141&Region=gz&vpcId=vpc-2ari9m7h&orderDirection=desc&Signature=本代码自动填充的签名

    本示例程序步骤：
       1. 根据排序后的参数获得签名；
       2. 根据签名和参数获得最终请求串。
    注意：若您未安装 Python, 可执行`yum install python-pip`进行安装。

    本示例程序意义:
       本示例修改自腾讯云官网提供的云 api python SDK，旨在帮助用户了解签名及最终请求串。

    建议：
       正式使用时，使用官网提供 SDK，如"pip install qcloudapi-sdk-python"。
    '''
    secretId = '您的secretId'
    secretKey = '您的secretKey'
    params = {
        'Action':'DescribeVpcEx',
        'SecretId': secretId,
        'Region': 'gz', #地域
        'Timestamp': int(time.time()),  #时间
        'Nonce': random.randint(0,1000000), #随机整数

        'vpcId': 'vpc-2ari9m7h',
        'offset': 0,
        'limit': 1,
        'orderDirection': 'desc',
    }
    sign = Sign(secretId, secretKey)
    final_url = sign.getUrl('vpc.api.qcloud.com', '/v2/index.php', params)
    print "final url: " + final_url

if (__name__ == '__main__'):
    main()
```
