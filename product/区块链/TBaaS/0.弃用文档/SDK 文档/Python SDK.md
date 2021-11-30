## 简介
欢迎使用腾讯云 TBaaS 产品开发者工具套件（SDK）3.0，SDK3.0 是云 API3.0 平台的配套工具。为方便 Python 开发者调试和接入腾讯云 TBaaS 产品 API，这里向您介绍适用于 Python 的腾讯云 TBaaS 产品开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 TBaaS 产品 Python SDK 并开始调用。

## 依赖环境
1.	依赖环境：Python 2.7到3.6版本。
2.	通过腾讯云控制台开通 TBaaS 产品。
3.	获取 [SecretID、SecretKey](https://console.cloud.tencent.com/cam/capi) 以及调用地址（tbaas.tencentcloudapi.com）。

## 获取安装
安装 Python SDK 和第一次使用云 API 之前，用户需要在腾讯云控制台上申请并获取安全凭证。安全凭证包括 SecretID 和 SecretKey。SecretID 用于标识 API 调用者的身份，SecretKey 用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

### 通过 Pip 安装（推荐）
您可以通过执行以下命令，将腾讯云 API Python SDK 安装到您的项目中。如果您的项目环境尚未安装 pip，请参见 [pip官网](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o) 进行安装。
```
pip install tencentcloud-sdk-python
```
>! 如果您的项目环境中同时搭建 Python2 和 Python3 环境，在 Python3 环境下，请使用 pip3 命令进行安装。

### 通过源码包安装
1. 前往 Github 代码托管地址 下载最新代码。
2. 将获取到的源码包解压缩，并执行以下命令进行安装。
```
$ cd tencentcloud-sdk-python
$ python setup.py install
```

## 接口列表

| 接口名称 | 接口功能 |
|---------|---------|
| Invoke | 新增交易（支持同步模式和异步模式） |
| Query | 查询交易 |
| GetInvokeTx | 查询 Invoke 异步调用结果 |
| GetBlockList | 查询区块列表 |
| GetBlockTransactionListForUser | 获取区块内的交易列表 |
| GetClusterSummary | 获取区块链网络概要 |
| GetLatesdTransactionList | 获取最新交易列表 |
| GetTransactionDetailForUser | 获取交易详情 |
| ApplyUserCert | 申请用户证书 |
| DownloadUserCert | 下载用户证书 |
| SrvInvoke | trustsql 服务统一接口 |
| BlockByNumberHandler | 按块高查询区块信息 |
| DeployDynamicContractHandler | 动态部署合约 |
| GetBlockListHandler | 查询区块列表 |
| GetTransByHashHandler | 根据交易哈希查询交易信息 |
| GetTransListHandler | 查询交易列表 |
| SendTransactionHandler | 发送交易 |
| TransByDynamicContractHandler | 根据动态部署的合约发送交易 |

## 示例
以新增交易（Invoke）接口为例：
```
# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.tbaas.v20180416 import tbaas_client, models
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户密钥对secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")

    # 配置访问域名
    # SDK会自动指定域名。通常是不需要特地指定域名的，但是如果您访问的是金融区的服务，
    # 则必须手动指定域名，例如云服务器的上海金融区域名： tbaas.ap-shanghai-fsi.tencentcloudapi.com
    httpProfile = HttpProfile()
    httpProfile.endpoint = "tbaas.tencentcloudapi.com"
    # 实例化Tbaas的client对象
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    #第二个参数是地域信息，根据资源所属地域填写相应的地域信息，例如广州地域的资源可以直接填写字符串ap-guangzhou，或者引用预设的常量
    client = tbaas_client.TbaasClient(cred, "ap-guangzhou", clientProfile) 

    # 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
    params = '{"Module":"transaction","Operation":"invoke","ClusterId":"251005746ctestenv","ChaincodeName":"pettycc1","ChannelName":"pettyc1","Peers":[{"PeerName":"peer0.pettycorg.ctestenv","OrgName":"pettycOrg"}],"FuncName":"invoke","Args":["a","b","10"],"AsyncFlag":0,"GroupName":"pettycOrg"}'
    req = models.InvokeRequest()
    # 调用InvokeRequest的from_json_string方法，使用params初始化req对象
    req.from_json_string(params)

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.Invoke(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)

```
