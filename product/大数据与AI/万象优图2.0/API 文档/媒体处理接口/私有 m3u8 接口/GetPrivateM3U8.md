## 功能描述

GetPrivateM3U8 接口用于获取私有 M3U8 ts 资源的下载授权。（此方式通过对象存储转发请求至数据万象）。

## 请求

#### 请求示例

```plaintext
GET /for-test.m3u8?ci-process=pm3u8&expires= HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>

```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

参数的具体内容如下：

|参数名称  | 描述  | 类型|  是否必选  |
|:--- | :--- | :--- | :--- |
| ci-process | 操作类型，固定使用 pm3u8 | String |是|
| expires | 私有 ts 资源 url 下载凭证的相对有效期，单位为秒，范围为[3600, 43200] | String |是|


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。


#### 请求体
该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体为截图文件内容。

#### 错误码
该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

#### 请求

```plaintext
GET /for-test.pm3u8?ci-process=pm3u8&expires=3600 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2016 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfG****-sign-time=1484213027;32557109027&q-key-time=1484213027;32557109027&q-header-list=host&q-url-param-list=acl&q-signature=dcc1eb2022b79cb2a780bf062d3a40e120b4****
Content-Length: 0
```
#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/x-mpegURL
Content-Length: 266005
Connection: keep-alive
Date: Fri, 10 Mar 2016 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRiMjVfYmRjMzVfMTViMl82ZGZm****

<M3U8文件内容>
```
