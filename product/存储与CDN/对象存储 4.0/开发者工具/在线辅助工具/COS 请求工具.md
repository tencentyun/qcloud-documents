## 功能概述

COS 请求工具是腾讯云对象存储（ COS） 为您提供的 Web 端调试工具，集成在云 API 3.0 Explorer 平台上，可用于 API 接口的调试工作。

>! COS 请求工具发送的请求将被真实发送到 COS 的业务服务器，**所有操作均等同于真实操作，当您选择 DELETE 类操作时请谨慎操作。**

目前 COS 请求工具所支持的 API 版本为 XML API，不支持 JSON API 版本。
- JSON API 是腾讯云 COS 服务在推出 XML API 前为用户提供接入使用 COS 的 API 接口，接口与标准 XML 的 API 底层架构相同，数据互通，可以交叉使用，但是接口不兼容。
- XML API 具有更加丰富的功能和特性，腾讯云对象存储强烈建议您升级使用 XML API 版本。

## 工具地址

单击进入 [COS 请求工具](https://console.cloud.tencent.com/api/explorer?Product=cos)。

## 使用方法

选择【对象存储】产品，选择所需的 API 接口，填写该接口下相应的参数，单击发送请求后获取相应的请求响应结果。

COS 请求工具的整体页面，从左至右依次是产品栏，接口栏，参数栏和结果栏。您可以在不同的栏目执行相应的操作，最终在结果栏发送请求并获取响应结果和相关的过程参数信息。如下图所示：
![](https://main.qcloudimg.com/raw/6329b432ed56516ca311bcbe5720d13f.png)

有关 COS 请求工具的详细操作请查看如下步骤。

**1. 选择对象存储产品**

在最左侧的产品栏中单击【对象存储】，将可以看到在 API 接口栏中与 COS 相关的 API 接口。

>?COS 请求工具集成在云 API 3.0平台，该平台上搭载着其他腾讯云产品的 API 调试工具，您同样可以根据您的需要在该平台上选择其他产品并调试相应的接口。

**2. 选择需要调试的 API 接口**

您可以根据您的需求选择相应的 API 接口进行调试。API 接口栏中展示了三大类与 COS 相关的 API 接口： Service 接口、Bucket 接口和 Object 接口。

- 在 Service 类接口中，如 GET Service。此 API 可列出您账号下的所有存储桶信息，您需要输入您的 API 密钥信息。如果您需要获取您账户在指定区域内的存储桶信息，可在参数栏中选择对应的地域。如需了解更多该 API 的详细信息，请参见 [GET Service](https://cloud.tencent.com/document/product/436/8291) 文档。
- 在 Bucket 类接口中，包含对存储桶进行操作的 API 接口，如 PUT Bucket lifecycle。如需了解更多的 Bucket 类接口，请参见 [Bucket 接口](https://cloud.tencent.com/document/product/436/7731)。
- 在 Object 类接口中，包含各个可对对象进行操作的 API 接口，如 PUT Object。如需了解更多的 Object 类接口，请参见 [Object 接口](https://cloud.tencent.com/document/product/436/7739)。

**3. 输入 API 所需的参数信息**

参数栏将展示您所选的 API 接口的必填参数。有关 COS 的各个 API 接口的参数信息，请参见 [API 文档](https://cloud.tencent.com/document/product/436/10009) 了解。

API 密钥信息是在调用 API 接口这一环节中必填的参数。当您使用 API 接口对您的存储桶或者对象等资源进行操作时，您需要输入 API 密钥信息，用于授权此次 API 请求操作。您可以在访问管理控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面上获取您的 API 密钥信息。

>?对于每一个 API 接口，COS 请求工具在每一个必填的参数项后均加上了红色星号标识以提醒您该参数项为必填项。您也可以勾选【只看必填参数】，以减少参数栏上非必填的参数显示。

**4. 发送请求及查看响应结果**

当您选中 API，填写好相应的参数后，在【在线调用】选项卡中单击【发送请求】，此时系统会将您的请求发送到服务器，根据您的请求操作您的存储桶或者对象资源。

>!COS 请求工具发送的请求将真实发送到 COS 的业务服务器，**所有操作均等同于真实操作，当您选择 DELETE 类操作时请谨慎操作。**

发送请求后，返回的结果和请求参数将会显示在结果栏下方。在结果栏下方，您可以在【请求参数】中查看您的 HTTP 请求体信息，在【响应结果】中查看本次请求的响应体信息，在【签名过程】中查看本次请求中涉及的签名及其生成流程，同时系统会在【Curl】中为您提供 Curl 调用的语句。

**示例**

以 GET Object 为例，当发送请求以获取一份名为0001.txt的文件时，【请求参数】中将展示您本次请求的请求参数信息，本次请求的请求示例如下：
```http
GET https://bucketname-appid.cos.ap-region.myqcloud.com/0001.txt
Host: bucketname-appid.cos.ap-region.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDwqaGoCIWIG4hDWdJUTL5e3hn04xiD5kI&q-sign-time=1543398166;1543405366&q-key-time=1543398166;1543405366&q-header-list=host&q-url-param-list=&q-signature=f50ddd3e0b54a92df9d4efe2d0c3734a8c9007ec
```

首行展示的是您的 HTTP Verb 及访问的链接，次行展示的是访问的域名，最后一行展示的是本次请求的签名信息。对于 PUT 类的请求，其请求头部信息较为复杂，但同样存在一些公共请求头部。有关公共请求头部的信息，请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728)。

【签名过程】中可以查看本次请求中涉及的签名及其生成流程。有关签名算法的详细介绍，请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 详细了解，如果您需要对请求签名进行生成和调试，建议您使用 [COS 签名工具](https://cos5.cloud.tencent.com/static/cos-sign/)。

COS 返回的响应结果如下：

```http
200 OK
content-type: text/plain
content-length: 6
connection: close
accept-ranges: bytes
date: Wed, 28 Nov 2018 09:42:49 GMT
etag: "5a8dd3ad0756a93ded72b823b19dd877"
last-modified: Tue, 27 Nov 2018 20:05:26 GMT
server: tencent-cos
x-cos-request-id: NWJmZTYzMTlfOWUxYzBiMDlfOTA4NF8yMWI2YjE=
x-cos-version-id: MTg0NDY3NDI1MzAzODkyMjUzNjM
hello!
```

首行200 OK代表该请求返回的状态码信息，如请求失败，则会返回相应的错误码，有关错误码详细信息，请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。此后为响应头部信息，不同 API 的响应体均有所差异，但存在一些公共响应头部信息。有关公共响应头部的详细信息，请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729)。



## 注意事项
当您单击【发送请求】，确认将已填写必填参数的请求发送至 COS 服务端时，COS 将对您的存储桶和对象进行相应的操作，该操作无法撤回，无法回滚，请您在操作前慎重考虑。
