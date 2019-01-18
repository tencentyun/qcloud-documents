## 功能描述
PUT Bucket policy 请求可以向 Bucket 写入权限策略，当 Bucket 已存在权限策略时，该请求上传的策略将覆盖原有的权限策略。

## 请求

### 请求示例：

```shell
PUT /?policy HTTP/1.1
Host:<bucketname-APPID>.cos.<Region>.myqcloud.com
Date: date
Content-Type:application/json
Content-MD5:MD5
Authorization: Auth String
```

> Authorization: Auth String （详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情，请查阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

#### 请求参数
无特殊请求参数。

### 请求体

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

## 响应

### 响应头
#### 公共响应头

该响应使用公共响应头，了解公共响应头详情，请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。

#### 特有响应头

该请求操作无特殊的响应头部信息。

### 响应体
该请求响应体为空。

### 错误码

无返回特殊错误码。一般常见错误码，请参阅 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例
### 请求

```shell
PUT /?policy HTTP/1.1
Host:bucket01-1251668577.cos.ap-guangzhou.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484813288;32557709288&q-key-time=1484813288;32557709288&q-header-list=host&q-url-param-list=policy&q-signature=05f7fc936369f910a94a0c815e1f1752f034d47a
Content-Type: application/json
Content-Length: 233

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

### 响应

```shell
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 19 16:19:22 2017
Server: tencent-cos
x-cos-request-id: NTg4MDc2OGFfNDUyMDRlXzc3NTlfZTc4
```
