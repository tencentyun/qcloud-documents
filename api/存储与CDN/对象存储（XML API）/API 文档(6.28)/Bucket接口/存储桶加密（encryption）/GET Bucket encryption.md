## 功能描述

GET Bucket encryption 接口用于查询指定存储桶下的默认加密配置。

要执行此接口，必须拥有 GetBucketEncryption 权限。默认情况下，Bucket  的持有者直接拥有权限使用该 API 接口，Bucket  持有者也可以将权限授予其他用户。

## 请求

**请求示例**

```sh
GET /?encryption HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

**请求参数**

此接口无请求参数。

**请求头**

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

**请求体**

此接口无请求体。

## 响应

**响应头**

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**响应体**

以下是返回 SSE-COS 加密的响应体：

```sh
<ServerSideEncryptionConfiguration>
      <Rule>
            <ApplyServerSideEncryptionByDefault>
                <SSEAlgorithm>AES256</SSEAlgorithm>
            </ApplyServerSideEncryptionByDefault>
      </Rule>
</ServerSideEncryptionConfiguration>
```


具体元素如下：

| 元素名称                           | 父节点                             | 描述                                                         | 类型      |
| ---------------------------------- | ---------------------------------- | ------------------------------------------------------------ | --------- |
| ServerSideEncryptionConfiguration  | 无                                 | 包含默认加密的配置参数                                       | Container |
| Rules                              | ServerSideEncryptionConfiguration  | 默认的服务端加密配置规则                                     | Container |
| ApplyServerSideEncryptionByDefault | Rules                              | 服务端加密的默认配置信息                                     | Container |
| SSEAlgorithm                       | ApplyServerSideEncryptionByDefault | 要使用的服务端加密算法，枚举值：AES256 | String    |

**错误码**

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

**请求**

```sh
GET /?encryption HTTP 1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 17 Jun 2019 08:37:35 GMT
Authorization: signatureValue
```

**响应**

```sh
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: xxxx
Date: Mon, 17 Jun 2019 08:37:36 GMT
Server: tencent-cos
x-cos-request-id: NWQwNzUxNTBfMzdiMDJhMDlfOWM0Nl85NDFk****



<?xml version = "1.0" encoding = "UTF-8">
<ServerSideEncryptionConfiguration>
      <Rule>
            <ApplyServerSideEncryptionByDefault>
                <SSEAlgorithm>AES256</SSEAlgorithm>
            </ApplyServerSideEncryptionByDefault>
      </Rule>
</ServerSideEncryptionConfiguration>
```
