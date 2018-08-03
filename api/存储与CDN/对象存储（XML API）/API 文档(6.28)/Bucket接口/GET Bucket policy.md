## 功能描述
GET Bucket policy 请求可以向 Bucket 读取权限策略。

>注意：只有 Bucket 所有者有权限发起该请求。假如您没有拥有 GET Bucket policy 的权限，则返回 403 Access Denied；假如您拥有 GET Bucket policy 的权限但不是所有者时，将返回 405 Method Not Allowed；如果权限策略不存在，将返回 404 Policy Not Found。

## 请求

### 请求示例：

```http
GET /?policy Http/1.1
Host:<bucketname-APPID>.cos.<Region>.myqcloud.com
Date:date
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情，请查阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

#### 请求参数

无特殊请求参数。

### 请求体

无请求体。

## 响应

### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头

该请求操作无特殊的响应头部信息。

### 响应体

```json
{
    "version": "2.0",
    "principal": {
        "qcs": [
            "qcs::cam::uin/:uin/",
            "qcs::cam::uin/:uin/"
        ]
    },
    "statement": [
        {
            "effect": "allow",
            "action": [
                "name/cos:"
            ],
            "resource": [
                "qcs::cos::uid/:prefix////",
                "qcs::cos::uid/:prefix////[dir1]/*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "name/cos:"
            ],
            "resource": [
                "qcs::cos::uid/:prefix////",
                "qcs::cos::uid/:prefix////[dir1]/*"
            ]
        }
    ]
}
```

### 错误码

无返回特殊错误码。一般常见错误码，请参阅 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例
### 请求

```json
GET /?policy HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484814099;32557710099&q-key-time=1484814099;32557710099&q-header-list=host&q-url-param-list=policy&q-signature=0523d7c6305b6676611c44798d2c48b659e68869 
```

### 响应

```JSON
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 237
Connection: keep-alive
Date: Thu Jan 19 16:21:46 2017
Server: tencent-cos
x-cos-request-id: NTg4MDc3MWFfOWIxZjRlXzZmNDVfZTBl

{
    "version": "2.0",
    "principal": {
        "qcs": [
            "qcs::cam::uin/909619481:uin/909619481"
        ]
    },
    "statement": [
        {
            "action": [
                "name/cos:GetBucket"
            ],
            "effect": "allow",
            "resource": [
                "qcs:id/0:cos:sg:uid/1251668577:prefix//1251668577/arlenhuangtestsgnoversion/*"
            ]
        }
    ]
}
```