## 功能描述
Get Bucket Policy请求可以向Bucket读取权限策略。

只有Bucket所有者有权限发起该请求。假如您没有拥有Get Bucket Policy的权限，则返回403 Access Denied；假如您拥有Get Bucket Policy的权限但不是所有者时，将返回405 Method Not Allowed；如果权限策略不存在，将返回404 Policy Not Found。

## 请求

### 请求语法

```http
GET /?policy Http/1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

```json
{
    "version": "2.0",
    "principal": {
        "qcs": [
            "qcs::cam::uin/<RootAccout>:uin/<SubAccount>",
            "qcs::cam::uin/<RootAccout>:uin/<SubAccount>"
        ]
    },
    "statement": [
        {
            "effect": "allow",
            "action": [
                "name/cos:<ActionName>"
            ],
            "resource": [
                "qcs::cos:<Region>:uid/<Accout>:prefix//<uid>/<BucketName>/<ObjectName>",
                "qcs::cos:<Region>:uid/<Accout>:prefix//<uid>/<BucketName>/[dir1]/*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "name/cos:<ActionName>"
            ],
            "resource": [
                "qcs::cos:<Region>:uid/<Accout>:prefix//<uid>/<BucketName>/<ObjectName>",
                "qcs::cos:<Region>:uid/<Accout>:prefix//<uid>/<BucketName>/[dir1]/*"
            ]
        }
    ]
}
```
## 示例
### 请求
```json
GET /?policy HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484814099;32557710099&q-key-time=1484814099;32557710099&q-header-list=host&q-url-param-list=policy&q-signature=0523d7c6305b6676611c44798d2c48b659e68869 

```
### 返回
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
