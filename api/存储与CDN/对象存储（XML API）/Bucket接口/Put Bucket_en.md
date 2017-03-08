## Description

Put Bucket request is used to create a Bucket under specified account.

## Request

### Request Syntax

```Http
PUT / HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### Request Parameter

No particular request parameters

### Request Header

#### Recommended Headers

| Name                | Description                                       | Type        | Required   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | Allow users to define file permissions. <br />Valid values: private, public-read. Default value: private | String | No    |
| x-cos-grant-read | Grant read permission to the authorized user <br /> Format: x-cos-grant-read:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |
| x-cos-grant-write        | Grant write permission to the authorized user <br /> Format: x-cos-grant-write:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |
| x-cos-grant-full-control | Grant read and write permissions to the authorized user <br /> Format: x-cos-grant-full-control:  uin=" ",uin=" "<Br/> When you need to authorize a sub-account, uin="RootAcountID/SubAccountID"; when you need to authorize the root account, uin="RootAcountID" | String | No    |

### Request Content

No request content

## Returned Value

### Response Header

No particular response headers. Please refer to "Common Response Headers" for other headers

### Response Content

No response content

## Example

### Request

```HTTP
PUT / HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484708728;32557604728&q-key-time=1484708728;32557604728&q-header-list=host&q-url-param-list=&q-signature=b394a86624cbcc705b11bc6fc505843c5e2dd9c9
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed Jan 18 11:05:42 2017
Server: tencent-cos
x-cos-request-id: NTg3ZWRiODJfOWIxZjRlXzZmNDBfMTUz
```


