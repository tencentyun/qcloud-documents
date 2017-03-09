## Description
Put Bucket Policy request is used to write permission policies for Bucket. Policies uploaded using this request will overwrite existing permission policies. Wildcard "*" is supported.
Only the Bucket owner is allowed to initiate this request. You will receive "405 Method Not Allowed" if you have the permission for Put Bucket Policy. Otherwise you will receive "403 Access Denied"

## Request

### Request Syntax

```http
PUT /?policy Http/1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date: date
Content-Type:application/json
Content-MD5:MD5
Authorization: Auth String
```

### Request Parameter

No particular request parameters

### Request Header

No particular request headers. Please refer to "Common Request Headers" for other headers

### Request Content

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

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

No response content

## Example
### Request

```JSON
PUT /?policy HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484813288;32557709288&q-key-time=1484813288;32557709288&q-header-list=host&q-url-param-list=policy&q-signature=05f7fc936369f910a94a0c815e1f1752f034d47a
Content-Type: application/json
Content-Length: 233

{
  "version": "2.0", 
  "principal": {
    "qcs": [
      "qcs::cam::uin/909619481:uin/909619481"
    ]
  }, 
  "statement": [
    {
      "effect": "allow", 
      "action": [
        "name/cos:GetBucket"
      ], 
      "resource": [
        "qcs::cos:sg:uid/1251668577:prefix//1251668577/arlenhuangtestsgnoversion/*"
      ]
    }
  ]
}

```

### Response
```JSON
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 19 16:19:22 2017
Server: tencent-cos
x-cos-request-id: NTg4MDc2OGFfNDUyMDRlXzc3NTlfZTc4

```

