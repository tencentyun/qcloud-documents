## Description

Head Object request is used to retrieve the metadata of corresponding Object. Head has the same permissions as those of Get.

## Request

### Request Syntax

```Http
HEAD /ObjectName HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### Request Parameter

No particular request parameters

### Request Header

#### Recommended Headers

| Name                | Description                                       | Type        | Required   |
| ----------------- | --------------------------------------- | ------ | ---- |
| If-Modified-Since | If Object is modified after the specified time, the Object metadata is returned, otherwise 304 is returned | String | Required    |

### Request Content

No request content

## Returned Value

### Response Header

| Name                  | Description                                       | Type     |
| ------------------- | ---------------------------------------- | ------ |
| x-cos-meta-*        | User-defined metadata                                | String |
| X-cos-object-type | Indicate whether the Object is appendable for upload. Enumerated values: normal or appendable | string |
| X-cos-storage-class | The storage class of Object. Enumerated values: Standard, Standard_IA, Nearline | String |


### Response Content

No response content

## Example

### Request

```HTTP
HEAD /123 HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213210;32557109210&q-key-time=1484213210;32557109210&q-header-list=host&q-url-param-list=&q-signature=ac61b8eb61964e7e6b935e89de163a479a25c210
```

### Response

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 16087
Connection: keep-alive
Date: Thu Jan 12 17:26:53 2017
ETag: "9a4802d5c99dafe1c04da0a8e7e166bf"
Last-Modified: Wed, 11 Jan 2017 07:30:07 GMT
Server: tencent-cos
x-cos-object-type: normal
x-cos-request-id: NTg3NzRiZGRfYmRjMzVfM2Y2OF81N2YzNA==
```


