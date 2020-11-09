# 创建第一个API请求

本文档用于帮助开发者了解及使用腾讯云 API，为了完成API的使用，需要您具备基础的软件及网络传输协议的知识，并且对您产品的基本功能有一定了解。



## 前提条件

在开始创建第一个API请求之前，您需要准备以下几点：

1. 注册腾讯云账户。

2. 获取API Keys。由于API请求需要验证您的身份并鉴权，在注册腾讯云账户之后，你可以登录 [腾讯云API密钥管理控制台](https://console.cloud.tencent.com/cam/capi) 获取 SecretId 和 SecretKey。

   >如果您是第一次登录API密钥管理控制台，您需要新建密钥生成 SecretID 和 SecretKey。
   >
   >您的 API 密钥代表您的账号身份和所拥有的权限，等同于您的登录密码，切勿泄露他人。

   

## 完成第一次API请求

下面以“查询地域列表”为例，介绍如何通过 API Explorer 工具创建第一个API请求。

1. 打开 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=cvm&Version=2017-03-12)，在左侧导航树分别选择“云服务器”->“地域相关接口”->“查询地域列表”，在个人密钥中填写在第2步中获取的 SecretId 和 SecretKey。

2. 查看 [查询地域列表(输入参数)](https://cloud.tencent.com/document/product/213/15708#2.-.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0) 文档，输入参数中“Region”为可选参数，留空则默认查询所有示例地域。在API Explorer中，输入参数留空。

3. 单击右侧 “在线调用” 并 “发送请求”，可以在响应结果中看到您第一个API请求（查询云服务器实例）的返回结果，正常的返回结果会显示所有云服务器的可用地域，以及您对应的RequestID。请求结果的结构可以对照 [查询地域列表(输出参数)](https://cloud.tencent.com/document/product/213/15708#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) 查看。

   ![image-20200506132347464](/Users/reneewang/Library/Application Support/typora-user-images/image-20200506132347464.png)

4. 如果您的返回结果正常，您就成功的完成了第一次API请求。



## API Explorer工具

[API Explorer](https://console.cloud.tencent.com/api/explorer?Product=cvm&Version=2017-03-12) 是腾讯云提供给您进行在线调用、签名验证、SDK 代码生成和快速检索接口等能力，推荐初次使用API接口的开发者使用API工具，降低使用云 API 的难度。



## API 接口文档

对于每一个API接口，API接口文档提供您详细的接口、输入参数和输出参数的的详细描述，错误码指引。推荐您配合API Explorer使用对应产品的API接口文档。具体产品的API文档，可以访问 [腾讯云API中心](https://cloud.tencent.com/document/api)。



## API 鉴权

腾讯云 API 会对每个请求进行身份验证，用户需要使用安全凭证，经过特定的步骤对请求进行签名（Signature），每个请求都需要在公共请求参数中指定该签名结果并以指定的方式和格式发送请求。腾讯云提供TC3-HMAC-SHA256 以及 HmacSHA1 和 HmacSHA256 两种签名方法。

TC3-HMAC-SHA256 签名方法相比以前的 HmacSHA1 和 HmacSHA256 签名方法，功能上覆盖了以前的签名方法，而且更安全，支持更大的请求，支持 json 格式，性能有一定提升，**建议使用该签名方法计算签名**。

> 作为初学者，如果您使用 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=cvm&Version=2017-03-12) 工具，在输入对应的SecretId 和 SecretKey之后即可完成鉴权，免去您自己编写代码进行鉴权。

如果您想自己拼接API鉴权请求，可以参考 [接口鉴权V3](https://cloud.tencent.com/document/product/213/30654)。
