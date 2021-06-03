## 功能描述

该接口用于获取对象锁定的到期日期。

## 请求

#### 请求示例

```plaintext
GET /<object-key>?retention HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String 
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

 

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

```plaintext
<?xml version="1.0" encoding="UTF-8" ?>
<Retention> 
         <RetainUntilDate>timestamp</RetainUntilDate> 
</Retention> 
```

具体数据描述如下：

| 节点名称（关键字） | 父节点    | 描述         | 类型         |
| ------------------ | --------- | ------------ | ------------ |
| Retention          | 无        | 周期         | Container    |
| RetainUntilDate    | Retention | 具体到期日期 | String  Date |

 

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

 