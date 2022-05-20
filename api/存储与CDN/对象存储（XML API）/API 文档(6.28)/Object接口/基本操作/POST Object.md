## 功能描述

POST Object 接口请求可以将本地不超过5GB的对象（Object）以网页表单（HTML Form）的形式上传至指定存储桶中。该 API 的请求者需要对存储桶有写入权限。

> !
> - POST Object 接口不使用 COS 对象存储统一的请求签名，而是拥有自己的签名要求，请参见本文档的 [签名保护](#id1) 及相关字段的描述。
> - 如果试图添加已存在的同名对象且没有启用版本控制，则新上传的对象将覆盖原来的对象，成功时按照指定的返回方式正常返回。
> 

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=PostObject&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>


#### 版本控制

- 如果对存储桶启用版本控制，对象存储将自动为要添加的对象生成唯一的版本 ID。对象存储使用 x-cos-version-id 响应头部在响应中返回此标识。
- 如果暂停存储桶的版本控制，则对象存储始终将 null 用作存储在存储桶中的对象的版本 ID，且不返回 x-cos-version-id 响应头部。

## 请求

#### 请求示例

```shell
POST / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: multipart/form-data; boundary=Multipart Boundary
Content-Length: Content Length



[Multipart Form Data]
```

>? Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> 

#### 请求表单

此接口请求体通过 multipart/form-data 编码，在 HTML 网页中通过 &lt;form&gt; 元素发送请求时，需将 &lt;form&gt; 元素的 enctype 属性设置为 multipart/form-data，随后使用 HTML 表单元素（例如 &lt;input&gt;、&lt;select&gt; 等）添加所需表单字段。

**表单字段**

| 名称                    | 描述                                                         | 类型    | 是否必选 |
| ----------------------- | ------------------------------------------------------------ | ------- | -------- |
| key                     | 对象键，可在对象键中指定`${filename}`通配符，此时将使用实际上传的文件的文件名替换对象键中的通配符，相关示例请参见本文档的 [案例七](#step7) | string  | 是       |
| Cache-Control           | RFC 2616 中定义的缓存指令，将作为对象元数据保存              | string  | 否       |
| Content-Disposition     | RFC 2616 中定义的文件名称，将作为对象元数据保存              | string  | 否       |
| Content-Encoding        | RFC 2616 中定义的编码格式，将作为对象元数据保存              | string  | 否       |
| Content-Type            | RFC 2616 中定义的 HTTP 内容类型（MIME），将作为对象元数据保存<br>**注意：**通过网页表单上传文件时，浏览器会自动把指定文件的 MIME 类型携带在请求中，但对象存储 COS 并不会使用浏览器携带的 MIME 类型，您需要显式指定 Content-Type 表单字段作为对象的内容类型 | string  | 否       |
| Expires                 | RFC 2616 中定义的缓存失效时间，将作为对象元数据保存          | string  | 否       |
| success_action_redirect | 上传成功时重定向的目标 URL 地址，如果设置，那么在上传成功时将返回 HTTP 状态码为303（Redirect）及 Location 响应头部，Location 响应头部的值为该字段指定的 URL 地址，并附加 bucket、key 和 etag 参数，相关示例请参见本文档的 [案例八](#step8) | string  | 否       |
| success_action_status   | 上传成功时返回的 HTTP 状态码，可选200、201或204，默认为204。如果指定了 success_action_redirect 字段，则此字段会被忽略。相关示例请参见本文档的 [案例九](#step9) | number  | 否       |
| x-cos-meta-\*           | 包括用户自定义元数据头部后缀和用户自定义元数据信息，将作为对象元数据保存，大小限制为2KB<br>**注意：**用户自定义元数据信息支持下划线（_），但用户自定义元数据头部后缀不支持下划线，仅支持减号（-） | string  | 否       |
| x-cos-storage-class     | 对象存储类型。枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 MAZ_STANDARD、MAZ_STANDARD_IA、INTELLIGENT_TIERING、MAZ_INTELLIGENT_TIERING、STANDARD_IA、ARCHIVE、DEEP_ARCHIVE。默认值：STANDARD | Enum    | 否       |
| x-cos-traffic-limit     | 针对本次上传进行流量控制的限速值，必须为数字，单位默认为 bit/s。限速值设置范围为819200 - 838860800，即100KB/s - 100MB/s，如果超出该范围将返回400错误 | integer | 否       |
| Content-MD5             | 经过 Base64 编码的文件内容 MD5 哈希值，用于完整性检查，验证文件内容在传输过程中是否发生变化 | string  | 否       |
| file                    | 文件的信息和内容，通过网页表单上传时，浏览器将自动设置该字段的值为正确的格式<br>**注意：**file 字段必须放在整个表单的最后面。 | file    | 是       |

**访问控制列表（ACL）相关表单字段**

在上传对象时可以通过指定下列表单字段来设置对象的访问权限：

| 名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 描述                                                         | 类型   | 是否必选 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------ | -------- |
| acl                                                          | 定义对象的访问控制列表（ACL）属性。枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E9.A2.84.E8.AE.BE.E7.9A.84-acl) 文档中对象的预设 ACL 部分，例如 default，private，public-read 等，默认为 default<br>**注意：**如果您不需要进行对象 ACL 控制，请设置为 default 或者此项不进行设置，默认继承存储桶权限 | Enum   | 否       |
| x-cos-grant-read                                             | 赋予被授权者读取对象的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-read-acp                                         | 赋予被授权者读取对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-write-acp                                        | 赋予被授权者写入对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-full-control                                     | 赋予被授权者操作对象的所有权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |

**服务端加密（SSE）相关表单字段**

在上传对象时可以通过指定下列表单字段来使用服务端加密：

| 名称                                            | 描述                                                         | 类型   | 是否必选                                   |
| ----------------------------------------------- | ------------------------------------------------------------ | ------ | ------------------------------------------ |
| x-cos-server-side-encryption                    | 服务端加密算法，支持 AES256、cos/kms                         | string | 使用 SSE-COS 或 SSE-KMS 时，此字段为必选项 |
| x-cos-server-side-encryption-customer-algorithm | 服务端加密算法，支持 AES256                                  | string | 使用 SSE-C 时，此字段为必选项              |
| x-cos-server-side-encryption-cos-kms-key-id     | 当 x-cos-server-side-encryption 值为 cos/kms 时，用于指定 kms 的用户主密钥 CMK，如不指定则使用 COS 默认创建的 CMK，更多详细信息可参见 [SSE-KMS 加密](https://cloud.tencent.com/document/product/436/18145#sse-kms-.E5.8A.A0.E5.AF.86) | string | 否                                         |
| x-cos-server-side-encryption-context            | 当 x-cos-server-side-encryption 值为 cos/kms 时，用于指定加密上下文，值为 JSON 格式加密上下文键值对的 Base64 编码<br>例如`eyJhIjoiYXNkZmEiLCJiIjoiMTIzMzIxIn0=` | string | 否                                         |
| x-cos-server-side-encryption-customer-key       | 服务端加密密钥的 Base64 编码<br/>例如`MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=` | string | 使用 SSE-C 时，此字段为必选项              |
| x-cos-server-side-encryption-customer-key-MD5   | 服务端加密密钥的 MD5 哈希值，使用 Base64 编码<br/>例如`U5L61r7jcwdNvT7frmUG8g==` | string | 使用 SSE-C 时，此字段为必选项              |

<span id="id1"></span>

#### 签名保护

POST Object 接口要求在请求中携带签名相关字段，COS 服务器端收到消息后，进行身份验证，验证成功则可接受并执行请求，否则将会返回错误信息并丢弃此请求。

签名流程如下：

#### 1. 准备工作

在访问管理控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面中获取 SecretId 和 SecretKey。

#### 2. 生成 KeyTime

a. 获取当前时间对应的 Unix 时间戳 StartTimestamp，Unix 时间戳是从 UTC（协调世界时，或 GMT 格林威治时间）1970年1月1日0时0分0秒（北京时间：1970年1月1日8时0分0秒）起至现在的总秒数。
b. 根据上述时间戳和期望的签名有效时长算出签名过期时间对应的 Unix 时间戳 EndTimestamp。
c. 拼接签名有效时间，格式为`StartTimestamp;EndTimestamp`，即为 KeyTime。

#### 3. 构造“策略”（Policy）

策略为一个 JSON 文本，一个典型的策略如下：

```shell
{
    "expiration": "2019-08-30T09:38:12.414Z",
    "conditions": [
        { "acl": "default" },
        { "bucket": "examplebucket-1250000000" },
        [ "starts-with", "$key", "folder/subfolder/" ],
        [ "starts-with", "$Content-Type", "image/" ],
        [ "starts-with", "$success_action_redirect", "https://my.website/" ],
        [ "eq", "$x-cos-server-side-encryption", "AES256" ],
        { "q-sign-algorithm": "sha1" },
        { "q-ak": "AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q" },
        { "q-sign-time": "1567150692;1567157892" }
    ]
}
```

其中：

- expiration：该策略的过期时间，ISO8601 格式字符串
- conditions：该策略的具体条件限定数组，限定条件的具体规则如下表。

| 类型     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| 完全匹配 | 使用`{ "key": "value" }`或`[ "eq", "$key", "value" ]`方式表达，其中 key 为被限定的表单字段，value 为被限定的值 |
| 前缀匹配 | 使用`[ "starts-with", "$key", "value" ]`方式表达，其中 key 为被限定的表单字段，value 为被限定的前缀，可为空 |
| 范围匹配 | 仅适用于`[ "content-length-range", minNum, maxNum ]`，用于限定文件的长度必须在 minNum 和 maxNum 范围内 |

支持被限定的表单字段如下：

| 字段名称                                                     | 描述                                                         | 匹配方式&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 是否必选 |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------------- | -------- |
| acl                                                          | 对象的访问控制列表（ACL）属性                                | 完全、前缀                                         | 否       |
| bucket                                                       | 上传的存储桶                                                 | 完全                                               | 否       |
| key                                                          | 对象键。如果在上传时对象键使用`${filename}`通配符，那么对象键将在验证策略前被处理为最终的对象键，此时在策略中应该使用前缀匹配，而不应该出现`${filename}`通配符 | 完全、前缀                                         | 否       |
| content-length-range                                         | 文件长度范围                                                 | 范围                                               | 否       |
| Cache-Control, Content-Type, Content-Disposition, Content-Encoding, Expires | RFC 2616 中定义的相关头部，将在下载对象时作为响应头部返回    | 完全、前缀                                         | 否       |
| success_action_redirect                                      | 上传成功时重定向的目标 URL 地址                              | 完全、前缀                                         | 否       |
| success_action_status                                        | 上传成功时返回的 HTTP 状态码                                 | 完全                                               | 否       |
| x-cos-meta-*                                                 | 用户自定义的元数据头部字段                                   | 完全、前缀                                         | 否       |
| x-cos-*                                                      | 本文档中提到的其他 COS 相关表单字段，例如 ACL 和 SSE 相关字段 | 完全                                               | 否       |
| q-sign-algorithm                                             | 签名哈希算法，固定为 sha1                                    | 完全                                               | 是       |
| q-ak                                                         | 上文所述的 SecretId                                          | 完全                                               | 是       |
| q-sign-time                                                  | 上文所生成的 KeyTime                                         | 完全                                               | 是       |

> ! 
> - “策略”（Policy）中限定的除 bucket 以外的字段，都必须出现在表单字段中。例如限定了`{ "acl": "default" }`，那么表单中必须出现 acl 且值为 default。
> - 基于安全考虑，强烈建议您对所有可以限定的表单字段进行限定。

#### 4. 生成 SignKey

使用 HMAC-SHA1 以 SecretKey 为密钥，以 KeyTime 为消息，计算消息摘要（哈希值，16进制小写形式），即为 SignKey，例如：`39acc8c9f34ba5b19bce4e965b370cd3f62d2fba`。

#### 5. 生成 StringToSign

使用 SHA1 对上文中构造的策略（Policy）文本计算消息摘要（哈希值，16进制小写形式），即为 StringToSign，例如：`d5d903b8360468bc81c1311f134989bc8c8b5b89`。

#### 6. 生成 Signature

使用 HMAC-SHA1 以 SignKey 为密钥（字符串形式，非原始二进制），以 StringToSign 为消息（字符串形式，非原始二进制），计算消息摘要（哈希值，16进制小写形式），即为 Signature，例如：`7758dc9a832e9d301dca704cacbf9d9f8172fdef`。

#### 7. 将签名附加到表单

将上述策略和签名相关信息，以下表中描述的方式附加到表单中：

| 名称                 | 描述                                                         | 类型   | 是否必选                                   |
| -------------------- | ------------------------------------------------------------ | ------ | ------------------------------------------ |
| x-cos-security-token | 使用临时安全凭证时需要传入的安全令牌字段，详情请参见 [临时安全凭证](https://cloud.tencent.com/document/product/436/31315#.E4.B8.B4.E6.97.B6.E5.AE.89.E5.85.A8.E5.87.AD.E8.AF.81) 相关说明 | string | 否，当使用临时<br>密钥时，此表单项为必选项 |
| policy               | 经过 Base64 编码的“策略”（Policy）内容                       | string | 是                                         |
| q-sign-algorithm     | 签名哈希算法，固定为 sha1                                    | string | 是                                         |
| q-ak                 | 上文所述的 SecretId                                          | string | 是                                         |
| q-key-time           | 上文所生成的 KeyTime                                         | string | 是                                         |
| q-signature          | 上文所生成的 Signature                                       | string | 是                                         |

> !签名表单字段需要在 file 表单字段之前。

**签名保护实际案例**

**准备工作**

登录访问管理控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取其 APPID、SecretId 和 SecretKey，举例如下：

| APPID      | SecretId                             | SecretKey                        |
| ---------- | ------------------------------------ | -------------------------------- |
| 1250000000 | AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q | BQYIM75p8x0iWVFSIgqEKwFprpRSVHlz |

**构造策略**

```shell
{
    "expiration": "2019-08-30T09:38:12.414Z",
    "conditions": [
        { "acl": "default" },
        { "bucket": "examplebucket-1250000000" },
        [ "starts-with", "$key", "folder/subfolder/" ],
        [ "starts-with", "$Content-Type", "image/" ],
        [ "starts-with", "$success_action_redirect", "https://my.website/" ],
        [ "eq", "$x-cos-server-side-encryption", "AES256" ],
        { "q-sign-algorithm": "sha1" },
        { "q-ak": "AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q" },
        { "q-sign-time": "1567150692;1567157892" }
    ]
}
```

**中间变量**

- KeyTime = `1567150692;1567157892`
- SignKey = `39acc8c9f34ba5b19bce4e965b370cd3f62d2fba`
- StringToSign = `d5d903b8360468bc81c1311f134989bc8c8b5b89`
- Signature = `7758dc9a832e9d301dca704cacbf9d9f8172fdef`

**签名表单字段**

- policy = `ewogICAgImV4cGlyYXRpb24iOiAiMjAxOS0wOC0zMFQwOTozODoxMi40MTRaIiwKICAgICJjb25kaXRpb25zIjogWwogICAgICAgIHsgImFjbCI6ICJkZWZhdWx0IiB9LAogICAgICAgIHsgImJ1Y2tldCI6ICJleGFtcGxlYnVja2V0LTEyNTAwMDAwMDAiIH0sCiAgICAgICAgWyAic3RhcnRzLXdpdGgiLCAiJGtleSIsICJmb2xkZXIvc3ViZm9sZGVyLyIgXSwKICAgICAgICBbICJzdGFydHMtd2l0aCIsICIkQ29udGVudC1UeXBlIiwgImltYWdlLyIgXSwKICAgICAgICBbICJzdGFydHMtd2l0aCIsICIkc3VjY2Vzc19hY3Rpb25fcmVkaXJlY3QiLCAiaHR0cHM6Ly9teS53ZWJzaXRlLyIgXSwKICAgICAgICBbICJlcSIsICIkeC1jb3Mtc2VydmVyLXNpZGUtZW5jcnlwdGlvbiIsICJBRVMyNTYiIF0sCiAgICAgICAgeyAicS1zaWduLWFsZ29yaXRobSI6ICJzaGExIiB9LAogICAgICAgIHsgInEtYWsiOiAiQUtJRFFqejNsdG9tcFZqQm5pNUxpdGtXSEZsRnB3a245VTVxIiB9LAogICAgICAgIHsgInEtc2lnbi10aW1lIjogIjE1NjcxNTA2OTI7MTU2NzE1Nzg5MiIgfQogICAgXQp9`
- q-sign-algorithm = `sha1`
- q-ak = `AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q`
- q-key-time = `1567150692;1567157892`
- q-signature = `7758dc9a832e9d301dca704cacbf9d9f8172fdef`

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

| 名称     | 描述                                                         | 类型   |
| -------- | ------------------------------------------------------------ | ------ |
| Location | <li>当使用 success_action_redirect 表单字段时，此响应头部的值为 success_action_redirect 指定的 URL 地址，并附加 bucket、key 和 etag 参数，相关示例请参见本文档的 [案例八](#step8)<br><li>当未使用 success_action_redirect 表单字段时，此响应头部的值为完整的对象访问 URL 地址，相关示例请参见本文档的 [案例一](#step1) | string |

**版本控制相关头部**

在启用版本控制的存储桶中上传对象，将返回下列响应头部：

| 名称             | 描述          | 类型   |
| ---------------- | ------------- | ------ |
| x-cos-version-id | 对象的版本 ID | string |

**服务端加密（SSE）相关头部**

如果在上传对象时使用了服务端加密，则此接口将返回服务端加密专用头部，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7729#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

<span id="step1"></span>

#### 案例一：简单案例（未启用版本控制）

#### 请求

<dx-codeblock>
:::  shell
POST / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 29 Aug 2019 07:39:34 GMT
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryZBPbaoYE2gqeB21N
Content-Length: 1119
Connection: close

------WebKitFormBoundaryZBPbaoYE2gqeB21N
Content-Disposition: form-data; name="key"

exampleobject
------WebKitFormBoundaryZBPbaoYE2gqeB21N
Content-Disposition: form-data; name="policy"

eyJjb25kaXRpb25zIjpbeyJxLXNpZ24tYWxnb3JpdGhtIjoic2hhMSJ9LHsicS1hayI6IkFLSUQ4QTBmQlZ0WUZyTm0wMm9ZMWcxSlFRRjBjM0pPNk5FdSJ9LHsicS1zaWduLXRpbWUiOiIxNTY3MDY0Mzc0OzE1NjcwNzE1NzQifV0sImV4cGlyYXRpb24iOiIyMDE5LTA4LTI5VDA5OjM5OjM0LjQ3MVoifQ==
------WebKitFormBoundaryZBPbaoYE2gqeB21N
Content-Disposition: form-data; name="q-sign-algorithm"

sha1
------WebKitFormBoundaryZBPbaoYE2gqeB21N
Content-Disposition: form-data; name="q-ak"

AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****
------WebKitFormBoundaryZBPbaoYE2gqeB21N
Content-Disposition: form-data; name="q-key-time"

1567064374;1567071574
------WebKitFormBoundaryZBPbaoYE2gqeB21N
Content-Disposition: form-data; name="q-signature"

74ba120129a13d8f0e19479fbdc01bca3bca****
------WebKitFormBoundaryZBPbaoYE2gqeB21N
Content-Disposition: form-data; name="file"; filename="example.jpg"
Content-Type: image/jpeg

[Object Content]
------WebKitFormBoundaryZBPbaoYE2gqeB21N--
:::
</dx-codeblock>

#### 响应

```shell
HTTP/1.1 204 
Content-Length: 0
Connection: close
Date: Thu, 29 Aug 2019 07:39:34 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Location: http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject
Server: tencent-cos
x-cos-request-id: NWQ2NzgxMzZfMmViMDJhMDlfY2NjOF84NGQz****
```

<span id="step2"></span>

#### 案例二：使用表单字段指定元数据和 ACL

#### 请求

<dx-codeblock>
:::  shell
POST / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 29 Aug 2019 07:39:34 GMT
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Length: 2146
Connection: close

------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="key"

exampleobject
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="acl"

public-read
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="Cache-Control"

max-age=86400
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="Content-Disposition"

attachment; filename=example.jpg
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="Content-Type"

image/jpeg
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="x-cos-meta-example-field"

example-value
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="Content-MD5"

7o3pGNBWQBRbGPcPTDqmAg==
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="policy"

eyJjb25kaXRpb25zIjpbeyJhY2wiOiJwdWJsaWMtcmVhZCJ9LHsiYnVja2V0IjoiZXhhbXBsZWJ1Y2tldC0xMjUyMjQ2NTU1In0seyJrZXkiOiJleGFtcGxlb2JqZWN0In0sWyJlcSIsIiRDb250ZW50LURpc3Bvc2l0aW9uIiwiYXR0YWNobWVudDsgZmlsZW5hbWU9ZXhhbXBsZS5qcGciXSxbInN0YXJ0cy13aXRoIiwiJENvbnRlbnQtVHlwZSIsImltYWdlLyJdLFsiZXEiLCIkeC1jb3MtbWV0YS1leGFtcGxlLWZpZWxkIiwiZXhhbXBsZS12YWx1ZSJdLHsicS1zaWduLWFsZ29yaXRobSI6InNoYTEifSx7InEtYWsiOiJBS0lEOEEwZkJWdFlGck5tMDJvWTFnMUpRUUYwYzNKTzZORXUifSx7InEtc2lnbi10aW1lIjoiMTU2NzA2NDM3NDsxNTY3MDcxNTc0In1dLCJleHBpcmF0aW9uIjoiMjAxOS0wOC0yOVQwOTozOTozNC45MzdaIn0=
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="q-sign-algorithm"

sha1
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="q-ak"

AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="q-key-time"

1567064374;1567071574
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="q-signature"

228a89b5f7b8fce7fdfa4a3b36cfb5a5eafb****
------WebKitFormBoundary9JtEhEGHSdx8Patg
Content-Disposition: form-data; name="file"; filename="example.jpg"
Content-Type: image/jpeg

[Object Content]
------WebKitFormBoundary9JtEhEGHSdx8Patg--
:::
</dx-codeblock>

#### 响应

```shell
HTTP/1.1 204 
Content-Length: 0
Connection: close
Date: Thu, 29 Aug 2019 07:39:35 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Location: http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject
Server: tencent-cos
x-cos-request-id: NWQ2NzgxMzdfM2NhZjJhMDlfMTQzYV84Nzhh****
```

<span id="step3"></span>

#### 案例三：使用服务端加密 SSE-COS

#### 请求

<dx-codeblock>
:::  shell
POST / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 29 Aug 2019 07:39:35 GMT
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryBVaHvBJQJnQrAxKY
Content-Length: 1296
Connection: close

------WebKitFormBoundaryBVaHvBJQJnQrAxKY
Content-Disposition: form-data; name="key"

exampleobject
------WebKitFormBoundaryBVaHvBJQJnQrAxKY
Content-Disposition: form-data; name="x-cos-server-side-encryption"

AES256
------WebKitFormBoundaryBVaHvBJQJnQrAxKY
Content-Disposition: form-data; name="policy"

eyJjb25kaXRpb25zIjpbeyJ4LWNvcy1zZXJ2ZXItc2lkZS1lbmNyeXB0aW9uIjoiQUVTMjU2In0seyJxLXNpZ24tYWxnb3JpdGhtIjoic2hhMSJ9LHsicS1hayI6IkFLSUQ4QTBmQlZ0WUZyTm0wMm9ZMWcxSlFRRjBjM0pPNk5FdSJ9LHsicS1zaWduLXRpbWUiOiIxNTY3MDY0Mzc1OzE1NjcwNzE1NzUifV0sImV4cGlyYXRpb24iOiIyMDE5LTA4LTI5VDA5OjM5OjM1LjUyN1oifQ==
------WebKitFormBoundaryBVaHvBJQJnQrAxKY
Content-Disposition: form-data; name="q-sign-algorithm"

sha1
------WebKitFormBoundaryBVaHvBJQJnQrAxKY
Content-Disposition: form-data; name="q-ak"

AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****
------WebKitFormBoundaryBVaHvBJQJnQrAxKY
Content-Disposition: form-data; name="q-key-time"

1567064375;1567071575
------WebKitFormBoundaryBVaHvBJQJnQrAxKY
Content-Disposition: form-data; name="q-signature"

65f3f8864bb1b271e1235d1ec7d1cb508ffa****
------WebKitFormBoundaryBVaHvBJQJnQrAxKY
Content-Disposition: form-data; name="file"; filename="example.jpg"
Content-Type: image/jpeg

[Object Content]
------WebKitFormBoundaryBVaHvBJQJnQrAxKY--
:::
</dx-codeblock>

#### 响应

```shell
HTTP/1.1 204 
Content-Length: 0
Connection: close
Date: Thu, 29 Aug 2019 07:39:35 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Location: http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject
Server: tencent-cos
x-cos-request-id: NWQ2NzgxMzdfMTljMDJhMDlfNTg4ZF84Njgx****
x-cos-server-side-encryption: AES256
```

<span id="step4"></span>

#### 案例四：使用服务端加密 SSE-C

#### 请求

<dx-codeblock>
:::  shell
POST / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 29 Aug 2019 07:39:36 GMT
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Length: 1667
Connection: close

------WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Disposition: form-data; name="key"

exampleobject
------WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Disposition: form-data; name="x-cos-server-side-encryption-customer-algorithm"

AES256
------WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Disposition: form-data; name="x-cos-server-side-encryption-customer-key"

MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=
------WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Disposition: form-data; name="x-cos-server-side-encryption-customer-key-MD5"

U5L61r7jcwdNvT7frmUG8g==
------WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Disposition: form-data; name="policy"

eyJjb25kaXRpb25zIjpbeyJ4LWNvcy1zZXJ2ZXItc2lkZS1lbmNyeXB0aW9uLWN1c3RvbWVyLWFsZ29yaXRobSI6IkFFUzI1NiJ9LHsicS1zaWduLWFsZ29yaXRobSI6InNoYTEifSx7InEtYWsiOiJBS0lEOEEwZkJWdFlGck5tMDJvWTFnMUpRUUYwYzNKTzZORXUifSx7InEtc2lnbi10aW1lIjoiMTU2NzA2NDM3NjsxNTY3MDcxNTc2In1dLCJleHBpcmF0aW9uIjoiMjAxOS0wOC0yOVQwOTozOTozNi4wODdaIn0=
------WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Disposition: form-data; name="q-sign-algorithm"

sha1
------WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Disposition: form-data; name="q-ak"

AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****
------WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Disposition: form-data; name="q-key-time"

1567064376;1567071576
------WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Disposition: form-data; name="q-signature"

0273a4b4ede39d0e5162758e145ea0c3e9ef****
------WebKitFormBoundaryYa6H7Gd4xuhlyfJb
Content-Disposition: form-data; name="file"; filename="example.jpg"
Content-Type: image/jpeg

[Object Content]
------WebKitFormBoundaryYa6H7Gd4xuhlyfJb--
:::
</dx-codeblock>

#### 响应

```shell
HTTP/1.1 204 
Content-Length: 0
Connection: close
Date: Thu, 29 Aug 2019 07:39:36 GMT
ETag: "582d9105f71525f3c161984bc005efb5"
Location: http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject
Server: tencent-cos
x-cos-request-id: NWQ2NzgxMzhfMzdiMDJhMDlfNDA4YV84MzQx****
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==
```

<span id="step5"></span>

#### 案例五：启用版本控制

#### 请求

<dx-codeblock>
:::  shell
POST / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 29 Aug 2019 07:40:07 GMT
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJspR3QIUhGJLALwf
Content-Length: 1119
Connection: close

------WebKitFormBoundaryJspR3QIUhGJLALwf
Content-Disposition: form-data; name="key"

exampleobject
------WebKitFormBoundaryJspR3QIUhGJLALwf
Content-Disposition: form-data; name="policy"

eyJjb25kaXRpb25zIjpbeyJxLXNpZ24tYWxnb3JpdGhtIjoic2hhMSJ9LHsicS1hayI6IkFLSUQ4QTBmQlZ0WUZyTm0wMm9ZMWcxSlFRRjBjM0pPNk5FdSJ9LHsicS1zaWduLXRpbWUiOiIxNTY3MDY0NDA3OzE1NjcwNzE2MDcifV0sImV4cGlyYXRpb24iOiIyMDE5LTA4LTI5VDA5OjQwOjA3LjQ4OFoifQ==
------WebKitFormBoundaryJspR3QIUhGJLALwf
Content-Disposition: form-data; name="q-sign-algorithm"

sha1
------WebKitFormBoundaryJspR3QIUhGJLALwf
Content-Disposition: form-data; name="q-ak"

AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****
------WebKitFormBoundaryJspR3QIUhGJLALwf
Content-Disposition: form-data; name="q-key-time"

1567064407;1567071607
------WebKitFormBoundaryJspR3QIUhGJLALwf
Content-Disposition: form-data; name="q-signature"

699ad0ce7780eb559b75e88f77e95743d829****
------WebKitFormBoundaryJspR3QIUhGJLALwf
Content-Disposition: form-data; name="file"; filename="example.jpg"
Content-Type: image/jpeg

[Object Content]
------WebKitFormBoundaryJspR3QIUhGJLALwf--
:::
</dx-codeblock>

#### 响应

```shell
HTTP/1.1 204 
Content-Length: 0
Connection: close
Date: Thu, 29 Aug 2019 07:40:07 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Location: http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject
Server: tencent-cos
x-cos-request-id: NWQ2NzgxNTdfNzFiNDBiMDlfMmE3ZmJfODQ1****
x-cos-version-id: MTg0NDUxNzcwMDkzMDE3NDQ0MDU
```

<span id="step6"></span>

#### 案例六：暂停版本控制

#### 请求

<dx-codeblock>
:::  shell
POST / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 29 Aug 2019 07:40:38 GMT
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryX8hd2lxTMzIBk5Li
Content-Length: 1119
Connection: close

------WebKitFormBoundaryX8hd2lxTMzIBk5Li
Content-Disposition: form-data; name="key"

exampleobject
------WebKitFormBoundaryX8hd2lxTMzIBk5Li
Content-Disposition: form-data; name="policy"

eyJjb25kaXRpb25zIjpbeyJxLXNpZ24tYWxnb3JpdGhtIjoic2hhMSJ9LHsicS1hayI6IkFLSUQ4QTBmQlZ0WUZyTm0wMm9ZMWcxSlFRRjBjM0pPNk5FdSJ9LHsicS1zaWduLXRpbWUiOiIxNTY3MDY0NDM4OzE1NjcwNzE2MzgifV0sImV4cGlyYXRpb24iOiIyMDE5LTA4LTI5VDA5OjQwOjM4LjA5MloifQ==
------WebKitFormBoundaryX8hd2lxTMzIBk5Li
Content-Disposition: form-data; name="q-sign-algorithm"

sha1
------WebKitFormBoundaryX8hd2lxTMzIBk5Li
Content-Disposition: form-data; name="q-ak"

AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****
------WebKitFormBoundaryX8hd2lxTMzIBk5Li
Content-Disposition: form-data; name="q-key-time"

1567064438;1567071638
------WebKitFormBoundaryX8hd2lxTMzIBk5Li
Content-Disposition: form-data; name="q-signature"

bb04222322bfb17f4d1f43833bbbac0a03aa****
------WebKitFormBoundaryX8hd2lxTMzIBk5Li
Content-Disposition: form-data; name="file"; filename="example.jpg"
Content-Type: image/jpeg

[Object Content]
------WebKitFormBoundaryX8hd2lxTMzIBk5Li--
:::
</dx-codeblock>

#### 响应

```shell
HTTP/1.1 204 
Content-Length: 0
Connection: close
Date: Thu, 29 Aug 2019 07:40:38 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Location: http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject
Server: tencent-cos
x-cos-request-id: NWQ2NzgxNzZfMjFjOTBiMDlfMWY3YTFfNjY2****
```

<span id="step7"></span>

#### 案例七：对象键（表单字段 key）使用`${filename}`通配符

#### 请求

<dx-codeblock>
:::  shell
POST / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 29 Aug 2019 12:35:07 GMT
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryHrAMWZO4BNyT0rca
Content-Length: 1188
Connection: close

------WebKitFormBoundaryHrAMWZO4BNyT0rca
Content-Disposition: form-data; name="key"

folder/subfolder/${filename}
------WebKitFormBoundaryHrAMWZO4BNyT0rca
Content-Disposition: form-data; name="policy"

eyJjb25kaXRpb25zIjpbWyJzdGFydHMtd2l0aCIsIiRrZXkiLCJmb2xkZXIvc3ViZm9sZGVyLyJdLHsicS1zaWduLWFsZ29yaXRobSI6InNoYTEifSx7InEtYWsiOiJBS0lEOEEwZkJWdFlGck5tMDJvWTFnMUpRUUYwYzNKTzZORXUifSx7InEtc2lnbi10aW1lIjoiMTU2NzA4MjEwNzsxNTY3MDg5MzA3In1dLCJleHBpcmF0aW9uIjoiMjAxOS0wOC0yOVQxNDozNTowNy44OTlaIn0=
------WebKitFormBoundaryHrAMWZO4BNyT0rca
Content-Disposition: form-data; name="q-sign-algorithm"

sha1
------WebKitFormBoundaryHrAMWZO4BNyT0rca
Content-Disposition: form-data; name="q-ak"

AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****
------WebKitFormBoundaryHrAMWZO4BNyT0rca
Content-Disposition: form-data; name="q-key-time"

1567082107;1567089307
------WebKitFormBoundaryHrAMWZO4BNyT0rca
Content-Disposition: form-data; name="q-signature"

3cc37f8c81e36f57506efa02d0a3b6c9d551****
------WebKitFormBoundaryHrAMWZO4BNyT0rca
Content-Disposition: form-data; name="file"; filename="photo.jpg"
Content-Type: image/jpeg

[Object Content]
------WebKitFormBoundaryHrAMWZO4BNyT0rca--
:::
</dx-codeblock>

#### 响应

```shell
HTTP/1.1 204 
Content-Length: 0
Connection: close
Date: Thu, 29 Aug 2019 12:35:08 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Location: http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/folder/subfolder/photo.jpg
Server: tencent-cos
x-cos-request-id: NWQ2N2M2N2NfNWZhZjJhMDlfNmUzMV84OTg4****
```

<span id="step8"></span>

#### 案例八：指定 success_action_redirect 表单字段

#### 请求

<dx-codeblock>
:::  shell
POST / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 29 Aug 2019 08:02:29 GMT
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJ0bRH1MwgMq5eu6H
Content-Length: 1351
Connection: close

------WebKitFormBoundaryJ0bRH1MwgMq5eu6H
Content-Disposition: form-data; name="key"

exampleobject
------WebKitFormBoundaryJ0bRH1MwgMq5eu6H
Content-Disposition: form-data; name="success_action_redirect"

https://my.website/upload_success.html
------WebKitFormBoundaryJ0bRH1MwgMq5eu6H
Content-Disposition: form-data; name="policy"

eyJjb25kaXRpb25zIjpbWyJzdGFydHMtd2l0aCIsIiRzdWNjZXNzX2FjdGlvbl9yZWRpcmVjdCIsImh0dHBzOi8vbXkud2Vic2l0ZS8iXSx7InEtc2lnbi1hbGdvcml0aG0iOiJzaGExIn0seyJxLWFrIjoiQUtJRDhBMGZCVnRZRnJObTAyb1kxZzFKUVFGMGMzSk82TkV1In0seyJxLXNpZ24tdGltZSI6IjE1NjcwNjU3NDk7MTU2NzA3Mjk0OSJ9XSwiZXhwaXJhdGlvbiI6IjIwMTktMDgtMjlUMTA6MDI6MjkuMjcyWiJ9
------WebKitFormBoundaryJ0bRH1MwgMq5eu6H
Content-Disposition: form-data; name="q-sign-algorithm"

sha1
------WebKitFormBoundaryJ0bRH1MwgMq5eu6H
Content-Disposition: form-data; name="q-ak"

AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****
------WebKitFormBoundaryJ0bRH1MwgMq5eu6H
Content-Disposition: form-data; name="q-key-time"

1567065749;1567072949
------WebKitFormBoundaryJ0bRH1MwgMq5eu6H
Content-Disposition: form-data; name="q-signature"

c4a8ae7411687bc3d6ed2ac9b249e87a50b5****
------WebKitFormBoundaryJ0bRH1MwgMq5eu6H
Content-Disposition: form-data; name="file"; filename="example.jpg"
Content-Type: image/jpeg

[Object Content]
------WebKitFormBoundaryJ0bRH1MwgMq5eu6H--
:::
</dx-codeblock>

#### 响应

```shell
HTTP/1.1 303 Redirect
Content-Length: 0
Connection: close
Date: Thu, 29 Aug 2019 08:02:29 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Location: https://my.website/upload_success.html?bucket=examplebucket-1250000000&key=exampleobject&etag=%22ee8de918d05640145b18f70f4c3aa602%22
Server: tencent-cos
x-cos-request-id: NWQ2Nzg2OTVfMTRiYjI0MDlfZGFkOV85MDA4****
```

<span id="step9"></span>

#### 案例九：指定 success_action_status 表单字段

#### 请求

<dx-codeblock>
:::  shell
POST / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 29 Aug 2019 08:04:29 GMT
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryST9Mz8AGzCDphgJF
Content-Length: 1270
Connection: close

------WebKitFormBoundaryST9Mz8AGzCDphgJF
Content-Disposition: form-data; name="key"

exampleobject
------WebKitFormBoundaryST9Mz8AGzCDphgJF
Content-Disposition: form-data; name="success_action_status"

200
------WebKitFormBoundaryST9Mz8AGzCDphgJF
Content-Disposition: form-data; name="policy"

eyJjb25kaXRpb25zIjpbeyJzdWNjZXNzX2FjdGlvbl9zdGF0dXMiOiIyMDAifSx7InEtc2lnbi1hbGdvcml0aG0iOiJzaGExIn0seyJxLWFrIjoiQUtJRDhBMGZCVnRZRnJObTAyb1kxZzFKUVFGMGMzSk82TkV1In0seyJxLXNpZ24tdGltZSI6IjE1NjcwNjU4Njk7MTU2NzA3MzA2OSJ9XSwiZXhwaXJhdGlvbiI6IjIwMTktMDgtMjlUMTA6MDQ6MjkuMzI3WiJ9
------WebKitFormBoundaryST9Mz8AGzCDphgJF
Content-Disposition: form-data; name="q-sign-algorithm"

sha1
------WebKitFormBoundaryST9Mz8AGzCDphgJF
Content-Disposition: form-data; name="q-ak"

AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****
------WebKitFormBoundaryST9Mz8AGzCDphgJF
Content-Disposition: form-data; name="q-key-time"

1567065869;1567073069
------WebKitFormBoundaryST9Mz8AGzCDphgJF
Content-Disposition: form-data; name="q-signature"

e46285af04d4fb68e0624fdd0a525b6a07ab****
------WebKitFormBoundaryST9Mz8AGzCDphgJF
Content-Disposition: form-data; name="file"; filename="example.jpg"
Content-Type: image/jpeg

[Object Content]
------WebKitFormBoundaryST9Mz8AGzCDphgJF--
:::
</dx-codeblock>

#### 响应

```shell
HTTP/1.1 200 
Content-Length: 0
Connection: close
Date: Thu, 29 Aug 2019 08:04:29 GMT
ETag: "ee8de918d05640145b18f70f4c3aa602"
Location: http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject
Server: tencent-cos
x-cos-request-id: NWQ2Nzg3MGRfZjhjODBiMDlfOGM3N184Nzdl****
```
