## Description
Get Bucket Policy request is used to read permission policies of Bucket.

Only the Bucket owner is allowed to initiate this request. You will receive "403 Access Denied" if you don't have the permission to use Get Bucket Policy; You will receive "405 Method Not Allowed" if you have the permission but you are not the Bucket owner; You will receive "404 Policy Not Found" if permission policy does not exist.

## Request

### Request Syntax

```http
GET /?policy Http/1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### Request Parameter

No particular request parameters

### Request Header

No particular request headers. Please refer to "Common Request Headers" for other headers

### Request Content

No request content

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

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
## Example
### Request
```json
GET /?policy HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484814099;32557710099&q-key-time=1484814099;32557710099&q-header-list=host&q-url-param-list=policy&q-signature=0523d7c6305b6676611c44798d2c48b659e68869 

```
### Response
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

