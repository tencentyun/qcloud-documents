本文主要介绍适用于 Python 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例，让 Python 开发者快速掌握如何调试和接入腾讯云产品 API。
支持 SDK 3.0 版本的云产品列表请参见 [SDK 简介](https://cloud.tencent.com/document/product/494/42698)。

## 依赖环境
- 依赖环境：Python 2.7 到 3.6 版本。
- 登录 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应云产品。
- 在访问管理控制台 >【[API密钥管理](https://console.cloud.tencent.com/cam/capi)】页面获取 SecretID 和 SecretKey。
 - SecretID 用于标识 API 调用者的身份。
 - SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥，**SecretKey 需妥善保管，避免泄露**。
- 获取调用地址（endpoint），endpoint 一般格式为`*.tencentcloudapi.com`，例如 CVM 的调用地址为`cvm.tencentcloudapi.com`，具体地址请参考各云产品说明。

## 获取安装

### 通过 pip 安装（推荐）
1. 下载并安装 [pip](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o)。
2. 执行以下命令安装 SDK。
```bash
pip install tencentcloud-sdk-python
```
3. 中国大陆地区的用户可以使用国内镜像源提高下载速度，例如`pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python`。

>!如果同时有 python2 和 python3 环境， python3 环境需要使用 pip3 命令安装。

### 通过源码包安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-python) 或者 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-python/tencentcloud-sdk-python.zip) 下载最新代码。
2. 解压后依次执行以下命令安装 SDK。
```
    $ cd tencentcloud-sdk-python
    $ python setup.py install
```

## 示例
本文以云服务器查询可用区接口为例，介绍 SDK 的基础用法，更多示例请参考 [examples 目录](https://github.com/TencentCloud/tencentcloud-sdk-python/tree/master/examples)。

```python
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的 client models。
from tencentcloud.cvm.v20170312 import cvm_client, models
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")

    # 实例化要请求产品（以 CVM 为例）的 client 对象
    client = cvm_client.CvmClient(cred, "ap-shanghai")

    # 实例化一个请求对象
    req = models.DescribeZonesRequest()

    # 通过 client 对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeZones(req)
    # 输出 JSON 格式的字符串回包
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
```

## 相关配置
### 代理
在有代理的环境下，需要设置系统环境变量 `https_proxy`，否则可能无法正常调用，抛出连接超时的异常。

### 证书问题
在 Mac 操作系统下，Python 不再使用系统默认的证书，且本身也不提供证书，在进行 HTTPS 请求时，需要使用 certifi 库提供的证书，但 SDK 不支持指定。
因此在 Mac 操作系统安装 Python 3.6 或以上版本时，您需要使用`/Applications/Python 3.6/Install Certificates.command`命令安装证书，以防出现证书错误`Error: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056).`。

## 旧版 SDK
旧版本的 SDK 存放于 QcloudApi 目录，详细使用说明请参考 [旧版 Python SDK ](https://github.com/QcloudApi/qcloudapi-sdk-python)，但不再维护更新，推荐使用新版 SDK。
