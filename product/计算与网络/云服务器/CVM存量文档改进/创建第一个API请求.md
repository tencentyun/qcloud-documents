本文档用于帮助开发者了解及使用腾讯云 API。为了完成 API 的使用，需要您具备基础的软件及网络传输协议的知识，并且对本产品的基本功能有一定了解。

## 前提条件

在开始创建第一个 API 请求之前，您需要准备以下几点：
1. 注册腾讯云账户。
2. 获取 API Keys。由于 API 请求需要验证您的身份并鉴权，在注册腾讯云账户之后，您可以登录 [腾讯云 API 密钥管理控制台](https://console.cloud.tencent.com/cam/capi) 获取 SecretId 和 SecretKey。
>! 如果您是第一次登录 API 密钥管理控制台，您需要新建密钥生成 SecretID 和 SecretKey。
> 您的 API 密钥代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。   
>

## 完成第一次 API 请求

下面以“查询地域列表”为例，介绍如何通过 API Explorer 工具创建第一个 API 请求。

1. 打开 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=cvm&Version=2017-03-12)，进入 API Explorer 操作界面。
2. 在左侧导航栏中，选择【云服务器】>【地域相关接口】>【查询地域列表】，进入查询地域列表的 API 操作界面。
![](https://main.qcloudimg.com/raw/4ef3e12723042eef43413bb8c3cbb34a.png)
 - **个人密钥**：填写已获取的 SecretId 和 SecretKey。
 - **输入参数**，设置 Region 参数。
Region 参数为可选参数，若保持默认值（即设置为空），在调用 API 请求时将查询所有示例地域。
更多详情请参考 [查询地域列表](https://cloud.tencent.com/document/product/213/15708) 文档。
 - 在右侧的页签栏中，选择【在线调用】页签，并单击【发送请求】，即可在响应结果中看到您第一个 API 请求（查询地域列表）的返回结果。

3. 查看返回结果。以 Region 参数保持默认值（即设置为空）为例，正常的返回结果会显示所有云服务器的可用地域，以及您对应的 RequestID。具体的请求结构，您可以对照 [查询地域列表（输出参数）](https://cloud.tencent.com/document/product/213/15708#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) 查看。

 >! 此查询操作不涉及费用。但部分 API 操作会产生费用，如创建实例、创建镜像等。建议在进行 API 请求操作前，先了解其产品的计费规则。
 >

## API Explorer工具

[API Explorer](https://console.cloud.tencent.com/api/explorer?Product=cvm&Version=2017-03-12) 是腾讯云提供给您进行在线调用、签名验证、SDK 代码生成和快速检索接口等能力，推荐初次使用 API 接口的开发者使用 API 工具，降低使用云 API 的难度。


## API 接口文档

对于每一个 API 接口，API 接口文档提供您详细的接口、输入参数和输出参数的的详细描述，错误码指引。推荐您配合 API Explorer 使用对应产品的 API 接口文档。具体产品的 API 文档，可以访问 [腾讯云 API 中心](https://cloud.tencent.com/document/api)。


## API 鉴权

腾讯云 API 会对每个请求进行身份验证，用户需要使用安全凭证，经过特定的步骤对请求进行签名（Signature），每个请求都需要在公共请求参数中指定该签名结果并以指定的方式和格式发送请求。腾讯云提供 TC3-HMAC-SHA256 以及 HmacSHA1 和 HmacSHA256 两种签名方法。

TC3-HMAC-SHA256 签名方法相比以前的 HmacSHA1 和 HmacSHA256 签名方法，功能上覆盖了以前的签名方法，而且更安全，支持更大的请求，支持 JSON 格式，性能有一定提升，**建议使用该签名方法计算签名**。

>? 作为初学者，如果您使用 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=cvm&Version=2017-03-12) 工具，在输入对应的 SecretId 和 SecretKey 之后即可完成鉴权，免去您自己编写代码进行鉴权。
>

如果您想自己拼接 API 鉴权请求，可以参考 [接口鉴权 V3](https://cloud.tencent.com/document/product/213/30654)。
