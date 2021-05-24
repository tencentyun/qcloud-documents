## 功能描述

PUT Bucket encryption 接口用于设置指定存储桶下的默认加密配置。

要执行此接口，必须拥有 PutBucketEncryption 权限。默认情况下，Bucket 的持有者直接拥有权限使用该 API 接口，Bucket 持有者也可以将权限授予其他用户。

## 请求

**请求示例**

```sh
PUT /?encryption HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

**请求参数**

此接口无请求参数。

**请求头**

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

**请求体**

用户在请求体中使用 XML 语言设置存储桶默认加密配置信息。加密配置信息主要为加密项。

以下是用于设置 SSE-COS 的请求体：

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

| 元素名称                           | 父节点                             | 描述                                   | 类型      | 是否必选 |
| ---------------------------------- | ---------------------------------- | -------------------------------------- | --------- | -------- |
| ServerSideEncryptionConfiguration  | 无                                 | 包含默认加密的配置参数                 | Container | 是       |
| Rules                              | ServerSideEncryptionConfiguration  | 默认的服务端加密配置规则               | Container | 是       |
| ApplyServerSideEncryptionByDefault | Rules                              | 服务端加密的默认配置信息               | Container | 是       |
| SSEAlgorithm                       | ApplyServerSideEncryptionByDefault | 要使用的服务端加密算法，枚举值：AES256 | String    | 是       |

## 响应

**响应头**

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**响应体**

该请求的响应体返回为空。

**错误码**

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

**请求**

以下示例表示给存储桶 examplebucket-1250000000 设置 SSE-COS 加密。

```sh
PUT /?encryption HTTP 1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 17 Jun 2019 08:37:35 GMT
Authorization: signatureValue



<ServerSideEncryptionConfiguration>
      <Rule>
         <ApplyServerSideEncryptionByDefault>
             <SSEAlgorithm>AES256</SSEAlgorithm>
         </ApplyServerSideEncryptionByDefault>
      </Rule>
</ServerSideEncryptionConfiguration>
```

**响应**

```sh
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Mon, 17 Jun 2019 08:37:36 GMT
Server: tencent-cos
x-cos-request-id: NWQwNzUxNTBfMzdiMDJhMDlfOWM0Nl85NDFk****
```
