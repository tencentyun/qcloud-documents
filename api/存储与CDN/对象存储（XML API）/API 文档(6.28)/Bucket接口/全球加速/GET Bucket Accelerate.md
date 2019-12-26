## 功能描述

GET Bucket Accelerate 接口实现查询存储桶的全球加速功能配置。

**细节分析**

1. 如果您从未在存储桶上启用过全球加速功能，则 GET Bucket Accelerate 请求不返回全球加速功能配置状态。
2. 全球加速功能状态值合法返回值为 Enabled 或者 Suspended，表示开启全球加速功能和暂停全球加速功能。
3. 如果您是为子账号，需要查询存储桶的全球加速功能配置信息，您需要有该配置的读取权限。

## 请求

#### 请求示例

```shell
GET /?accelerate HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Authorization: Auth String
```

> ? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。 

#### 响应体

```shell
<AccelerateConfiguration xmlns="cos xmlns/"> 
  <Status>Enabled</Status> 
  <Type>COS</Type>
</AccelerateConfiguration>
```

具体的数据内容如下：

| 节点名称（关键字）      | 父节点                  | 描述                                                 | 类型      |
| ----------------------- | ----------------------- | ---------------------------------------------------- | --------- |
| AccelerateConfiguration | 无                      | 全球加速的具体信息                                   | Container |
| Status                  | AccelerateConfiguration | 说明全球加速功能是否开启，枚举值：Suspended、Enabled | Enum      |
| Type                    | AccelerateConfiguration | 指定全球加速功能的类型，枚举值：COS  | Enum      |

#### 错误码

此接口无特殊错误信息，全部错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
GET /?accelerate HTTP/1.1
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Connection: keep-alive
Authorization: authorization string
Content-Type: text/plain
```

#### 响应1（开启全球加速状态）

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 73
Connection: keep-alive
Date: Wed, 23 Aug 2019 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0ZThm

<AccelerateConfiguration>
  <Status>Enabled</Status>
  <Type>COS</Type>
</AccelerateConfiguration>
```

#### 响应2（暂停全球加速状态）

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 73
Connection: keep-alive
Date: Wed, 23 Aug 2019 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0ZThm

<AccelerateConfiguration>
  <Status>Disabled</Status>
  <Type>COS</Type>
</AccelerateConfiguration>
```

#### 响应3（未开启全球加速状态）

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 73
Connection: keep-alive
Date: Wed, 23 Aug 2019 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0ZThm

<AccelerateConfiguration/>
```
