## 功能描述
解绑开通数据万象服务的 Bucket（Bucket 及桶中文件会保留在对象存储（Cloud Object Storage，COS））。

## 请求
#### 请求示例

```
PUT /?unbind HTTP/1.1
Host: <BucketName-APPID>.pic.<Region>.myqcloud.com 
Date: GMT Date
Authorization: Auth String
```

>? Authorization：Auth String （详情参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应
#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该响应的响应体为空。
