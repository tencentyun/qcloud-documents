## 简介
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0是云 API 3.0平台的配套工具。目前已经支持 CVM、VPC、CBS 等产品，后续所有的云服务产品都会陆续接入。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。
本文主要介绍适用于 PHP 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例，让 PHP 开发者快速掌握如何调试和接入腾讯云产品 API。

## 支持 SDK 3.0版本的云产品列表

SDK 3.0支持全部 API 3.0下的云产品，本列表可能滞后于实际代码，如有疑问请咨询具体的云产品。


| 云产品名称 | 英文名称及缩写 | SDK 包名 |
|---------|---------|---------|
| <a href="https://cloud.tencent.com/document/api/213/15689">云服务器</a> | Cloud Virtual Machine，CVM | cvm |
| <a href="https://cloud.tencent.com/document/api/386/18637">黑石物理服务器</a> | Cloud Physical Machine，CPM | bm |
| <a href="https://cloud.tencent.com/document/api/362/15634">云硬盘</a> | Cloud Block Storage，CBS | cbs |
| …… | …… | …… |

## API Explorer
[API Explorer](https://console.cloud.tencent.com/api/explorer) 提供了在线调用、签名验证、 SDK 代码生成和快速检索接口等能力，能显著降低使用云 API 的难度。



## 旧版 SDK
推荐使用新版 SDK，旧版 SDK 将不再维护更新，PHP、Python、.Net、Node.js 和 Java 的旧版 SDK 使用指引如下：
- 旧版 PHP SDK
 详细使用说明请参考 [旧版 PHP SDK](https://github.com/QcloudApi/qcloudapi-sdk-php)。
- 旧版 Python SDK
 详细使用说明请参考 [旧版 Python SDK ](https://github.com/QcloudApi/qcloudapi-sdk-python)。
- 旧版 .Net SDK
 详细使用说明请参考 [旧版 .Net SDK](https://github.com/qcloudapi/qcloudapi-sdk-dotnet)。
- 旧版 Node.js SDK
 详细使用说明请参考 [旧版 Node.js SDK](https://github.com/CFETeam/qcloudapi-sdk)。
- 旧版 Java SDK
 在您的 Maven pom.xml 添加以下依赖项即可：
```xml
<dependency>
<groupId>com.qcloud</groupId>
<artifactId>qcloud-java-sdk</artifactId>
<version>2.0.6</version>
</dependency>
```
