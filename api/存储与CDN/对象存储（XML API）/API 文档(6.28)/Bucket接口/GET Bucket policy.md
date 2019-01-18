## 功能描述
GET Bucket policy 请求可以向 Bucket 读取权限策略。

## 请求

### 请求示例：

```shell
GET /?policy HTTP/1.1
Host:<bucketname-APPID>.cos.<Region>.myqcloud.com
Date:date
Authorization: Auth String
```

> Authorization: Auth String （详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

## 响应

### 响应头
#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
响应返回权限策略。

```shell
{
    "Statement": [
        {
            "Principal": {
                "qcs": [
                    "qcs::cam::uin/${owner_uin}:uin/${sub_uin}"
                ]
            },
            "Effect": "${effect}",
            "Action": [
                "name/cos:${action}"
            ],
            "Resource": [
                "qcs::cos:${region}:uid/${appid}:${bucket}/*"
            ]
        }
    ],
    "version": "2.0"
}
```

### 错误码
该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例
### 请求

```shell
GET /?policy HTTP/1.1
Host:examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484814099;32557710099&q-key-time=1484814099;32557710099&q-header-list=host&q-url-param-list=policy&q-signature=0523d7c6305b6676611c44798d2c48b659e68869 
```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 237
Connection: keep-alive
Date: Thu Jan 19 16:21:46 2017
Server: tencent-cos
x-cos-request-id: NTg4MDc3MWFfOWIxZjRlXzZmNDVfZTBl

{
  "Statement": [
    {
      "Principal": {
        "qcs": [
          "qcs::cam::uin/909619481:uin/909619481"
        ]
      },
      "Effect": "allow",
      "Action": [
        "name/cos:GetBucket"
      ],
      "Resource": [
        "qcs::cos:ap-chengdu:uid/1252336075:aaa-1252336075/*"
      ]
    }
  ],
  "version": "2.0"
}
```
