## 功能描述

PUT LiveChannel - Switch 接口可以使指定通道（Live Channel）在启用（Enabled）和禁用（Disabled）两种状态之间切换。

>!
> - 只有存储桶的拥有者才能进行该请求操作。
> - 对处于 Disabled 状态的通道发送推流请求会失败。
> - 即使在推流过程中，也可调用此接口。
> - 在推流过程中，调用此接口将通道从 Enabled 切换成 Disabled，COS 会强制断开推流链接（可能会有10秒左右延迟）。

## 请求

#### 请求示例

```plaintext
PUT /<ChannelName>?live&switch=<NewSwitch> HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Content-Length: Content Size
Content-Md5: Content MD5
Authorization: Auth String

XML Body
```

> ? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求参数

| 名称      | 描述                                                         | 类型       | 是否必选 |
| --------- | ------------------------------------------------------------ | ---------- | :------- |
| NewSwitch | 设置通道的开关状态。有效值：enabled，disabled。<br/>注意：enabled、disabled 需全部英文小写 | EnumString | 是       |




#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

此接口响应体为空。
#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
PUT /test-channel?live&switch=enabled HTTP 1.1
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Date: GMT date
Content-Length:Content Size
Content-Md5:Content MD5
Authorization: Auth String

```

#### 响应
```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Aug 2020 08:14:53 GMT
Server: tencent-cos
x-cos-request-id: NTk5ZDM5N2RfMjNiMjM1MGFfMmRiX2Y0****
```
