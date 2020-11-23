## 功能描述

GET Bucket IntelligentTiering 接口用于查询存储桶的智能分层配置信息。

> ?
> - 只有主账号或者被授权 GET Bucket IntelligentTiering 接口权限的子账号可以调用该接口。
> - 该配置有未启用和启用两种状态：
> - 如果您从未在存储桶上启用智能分层存储配置，则响应为：
```shell
	<IntelligentTieringConfiguration/>
```
> - 如果您启用了存储桶的智能分层配置，则响应为：
```shell
<IntelligentTieringConfiguration xmlns="cos xmlns/"> 
       <Status>Enabled</Status>
       <Transition>
          <Days>30</Days>
       </Transition>
</IntelligentTieringConfiguration>
```

## 请求

#### 请求示例

```shell
GET /?intelligenttiering HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Authorization: Auth String
```

> ?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

```shell
<IntelligentTieringConfiguration xmlns="cos xmlns/"> 
  <Status>Enabled</Status>
  <Transition>
    <Days>30|60|90</Days>
  </Transition>
</IntelligentTieringConfiguration>
```

具体的节点描述如下：

| 名称                            | 父节点                                     | 描述                                                         | 类型      |
| ------------------------------- | ------------------------------------------ | ------------------------------------------------------------ | --------- |
| IntelligentTieringConfiguration | 无                                         | 智能分层存储配置的具体信息                                   | Container |
| Status                          | IntelligentTieringConfiguration            | 说明智能分层存储配置是否开启，枚举值：Suspended、Enabled     | Enum      |
| Transition                      | IntelligentTieringConfiguration            | 指定智能分层存储配置中有关数据转换的配置信息                 | Container |
| Days                            | IntelligentTieringConfiguration.Transition | 指定智能分层存储配置中标准层数据转换为低频层数据的天数限制，可选值为30、60和90，默认值为30天 | Int       |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
GET /?intelligenttiering HTTP/1.1
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9Sm****&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=versioning&q-header-list=host&q-signature=5118a936049f9d44482bbb61309235cf4abe****
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 120
Connection: keep-alive
Date: Sun, 23 Aug 2020 08:15:16 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5OTRfZDNhZDM1MGFfMjYyMTFfZmU3****

<IntelligentTieringConfiguration xmlns="cos xmlns/"> 
  <Status>Enabled</Status>
  <Transition>
    <Days>30</Days>
  </Transition>
</IntelligentTieringConfiguration>
```
