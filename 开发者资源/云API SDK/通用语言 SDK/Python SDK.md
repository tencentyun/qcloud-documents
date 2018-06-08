## 简介
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK3.0 是云 API3.0 平台的配套工具。目前已经支持 cvm、vpc、cbs 等产品，后续所有的云服务产品都会接入进来。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，统一的错误码和返回包格式这些优点。
为方便 Python 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 Python 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 Python SDK 并开始调用。
## 支持的产品

|产品名称|支持 Python SDK3.0|
|----|------|
|云服务器 (CVM)|是|
|云硬盘 (CBS) |是|
|私有网络 (VPC)|是|
|云数据库(CDB)|是|
|批量计算|是|
|云数据库 MariaDB|是|
|无服务器云函数|是|
|分布式数据库 DCDB|是|
|物联网套件|是|
|渠道合作伙伴|是|
| Web漏洞扫描  | 是  |
|腾讯机器翻译|是|
|云数据库 PostgreSQL|是|


## 依赖环境
1. 依赖环境：Python 2.7 到 3.6 版本。
2. 从 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应产品。
3. 获取 SecretID、SecretKey 以及调用地址（endpoint），endpoint 一般形式为*.tencentcloudapi.com，如CVM 的调用地址为 cvm.tencentcloudapi.com，具体参考各产品说明。

## 获取安装
安装 Python SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey, SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。
### 通过 Pip 安装(推荐)
您可以通过 pip 安装方式将腾讯云 API Python SDK 安装到您的项目中，如果您的项目环境尚未安装 pip，请详细参见 [pip 官网](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o) 安装。
通过 pip 方式安装请在命令行中执行以下命令：
```bash
pip install tencentcloud-sdk-python
```
### 通过源码包安装
前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-python) 下载最新代码，解压后
```
	$ cd tencentcloud-sdk-python
    $ python setup.py install
```
## 示例
以查询可用区接口为例:
```python
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.cvm.v20170312 import cvm_client, models
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")

    # 实例化要请求产品(以cvm为例)的client对象
    client = cvm_client.CvmClient(cred, "ap-shanghai")

    # 实例化一个请求对象
    req = models.DescribeZonesRequest()

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeZones(req)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
```
您可以在 [github仓库](https://github.com/tencentcloud/tencentcloud-sdk-python) 中 examples 目录下找到更详细的示例。
## 旧版 SDK
旧版本的 SDK 存放于 QcloudApi 目录，详细使用说明请到 [旧版 Python SDK ](https://github.com/QcloudApi/qcloudapi-sdk-python)，但不再维护更新，推荐使用新版 SDK。
