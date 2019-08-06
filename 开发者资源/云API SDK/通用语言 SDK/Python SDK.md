## 简介
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK3.0 是云 API3.0 平台的配套工具。目前已经支持 CVM、VPC、CBS 等产品，后续所有的云服务产品都会接入进来。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，统一的错误码和返回包格式这些优点。
为方便 Python 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 Python 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 Python SDK 并开始调用。

## 支持 3.0 版本的产品列表
SDK3.0支持全部 API3.0下的产品，本列表可能滞后于实际代码，如有疑问请咨询具体的产品。

<table>
  <tr>
<td><a href="https://cloud.tencent.com/document/api/213/15689">云服务器</a></td>
<td><a href="https://cloud.tencent.com/document/api/386/18637">黑石物理服务器</a></td>
<td><a href="https://cloud.tencent.com/document/api/362/15634">云硬盘</a></td>
<td><a href="https://cloud.tencent.com/document/api/457/31853">容器服务</a></td>
<td><a href="https://cloud.tencent.com/document/api/858/17761">容器实例服务</a></td>
</tr>
<tr>
 <td><a href="https://cloud.tencent.com/document/api/377/20423">弹性伸缩</a></td>
  <td><a href="https://cloud.tencent.com/document/api/583/17235">无服务器云函数</a></td>
  <td><a href="https://cloud.tencent.com/document/api/599/15880">批量计算</a></td>
<td><a href="https://cloud.tencent.com/document/api/214/30667">负载均衡</a></td>
<td><a href="https://cloud.tencent.com/document/api/215/15755">私有网络</a></td>
  </tr>
  <tr>
 <td><a href="https://cloud.tencent.com/document/api/216/18404">专线接入</a></td>
 <td><a href="https://cloud.tencent.com/document/api/236/15830">云数据库 MySQL</a></td>
<td><a href="https://cloud.tencent.com/document/api/239/20002">云数据库 Redis</a></td>
 <td><a href="https://cloud.tencent.com/document/api/240/31797">云数据库 MongoDB</a></td>
  <td><a href="https://cloud.tencent.com/document/api/571/18122">数据传输服务 DTS</a></td>
 </tr>
  <tr>
<td><a href="https://cloud.tencent.com/document/api/237/16144">云数据库 MariaDB</a></td>
<td><a href="https://cloud.tencent.com/document/api/557/16124">分布式数据库 DCDB</a></td>
 <td><a href="https://cloud.tencent.com/document/api/238/19927">云数据库 SQL Server</a></td>
  <td><a href="https://cloud.tencent.com/document/api/409/16761">云数据库 PostgreSQL</a></td>
   <td><a href="https://cloud.tencent.com/document/api/228/30974">内容分发网络</a></td>
   </tr>
   <tr>
<td><a href="https://cloud.tencent.com/document/api/296/19825">主机安全</a></td>
  <td><a href="https://cloud.tencent.com/document/api/692/16733">Web 漏洞扫描</a></td>
   <td><a href="https://cloud.tencent.com/document/api/283/17742">应用安全</a></td>
   <td><a href="https://cloud.tencent.com/document/api/266/31753">云点播</a></td>
<td><a href="https://cloud.tencent.com/document/api/267/20456">云直播</a></td>
   </tr>
   <tr>
<td><a href="https://cloud.tencent.com/document/api/441/17362">智能语音服务</a></td>
 <td><a href="https://cloud.tencent.com/document/api/551/15612">机器翻译</a></td>
<td><a href="https://cloud.tencent.com/document/api/656/18281">催收机器人</a></td>
<td><a href="https://cloud.tencent.com/document/api/884/19310">智聆口语评测</a></td>
<td><a href="https://cloud.tencent.com/document/api/853/18384">腾讯优评</a></td>
 </tr>
 <tr>
<td><a href="https://cloud.tencent.com/document/api/845/30620">Elasticsearch Service</a></td>
<td><a href="https://cloud.tencent.com/document/api/634/19469">物联网通信</a></td>
 <td><a href="https://cloud.tencent.com/document/api/663/19455">TBaaS</a></td>
<td><a href="https://cloud.tencent.com/document/api/248/30343">云监控</a></td>
 <td><a href="https://cloud.tencent.com/document/api/659/18591">迁移服务平台</a></td>
</tr>
 <tr>
 <td><a href="https://cloud.tencent.com/document/api/869/17778">电子合同服务</a></td>
 <td><a href="https://cloud.tencent.com/document/api/555/19170">计费相关</a></td>
 <td><a href="https://cloud.tencent.com/document/api/563/16034">渠道合作伙伴</a></td>
  <td><a href="https://cloud.tencent.com/document/api/1007/31320">人脸核身-云智慧眼</a></td>
  <td><a href="https://cloud.tencent.com/document/api/1013/31737">威胁情报云查</a></td>
  </tr>
  <tr>
 <td><a href="https://cloud.tencent.com/document/api/1012/31720">样本智能分析平台</a></td>
  <td><a href="https://cloud.tencent.com/document/api/1004/30607">数学作业批改</a></td>
   <td><a href="https://cloud.tencent.com/document/api/670/31052">人脸融合</a></td>
<td><a href="https://cloud.tencent.com/document/api/867/32770">人脸识别</a></td>
<td><a href="https://cloud.tencent.com/document/api/1000/30698">数字版权管理</a></td>
   </tr>
  </table>



## API Explorer
[API Explorer](https://console.cloud.tencent.com/api/explorer) 提供了在线调用、签名验证、 SDK 代码生成和快速检索接口等能力，能显著降低使用云 API 的难度，推荐使用。

## 依赖环境
1. 依赖环境：Python 2.7 到 3.6 版本。
2. 从 [腾讯云控制台](https://console.cloud.tencent.com/) 开通相应产品。
3. 获取 SecretID、SecretKey 以及调用地址（endpoint），endpoint 一般形式为*.tencentcloudapi.com，如CVM 的调用地址为 cvm.tencentcloudapi.com，具体参考各产品说明。

## 获取安装
安装 Python SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey，SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。
### 通过 Pip 安装（推荐）
您可以通过 pip 安装方式将腾讯云 API Python SDK 安装到您的项目中，如果您的项目环境尚未安装 pip，请详细参见 [pip 官网](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o) 安装。
通过 pip 方式安装请在命令行中执行以下命令：
```bash
pip install tencentcloud-sdk-python
```
### 通过源码包安装
前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-python) 或者 [快速下载地址](https://tencentcloud-sdk-1253896243.file.myqcloud.com/tencentcloud-sdk-python/tencentcloud-sdk-python.zip) 下载最新代码，解压后
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
# 导入对应产品模块的 client models。
from tencentcloud.cvm.v20170312 import cvm_client, models
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")

    # 实例化要请求产品(以 CVM 为例)的 client 对象
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

## 更多示例

您可以在 GitHub 仓库中 [examples 目录](https://github.com/TencentCloud/tencentcloud-sdk-python/tree/master/examples) 下找到更详细的示例。

## 旧版 SDK
旧版本的 SDK 存放于 QcloudApi 目录，详细使用说明请到 [旧版 Python SDK ](https://github.com/QcloudApi/qcloudapi-sdk-python)，但不再维护更新，推荐使用新版 SDK。
