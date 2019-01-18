## Put Bucket Notification

### 功能描述

Put Bucket Notification 接口请求可以在指定Bucket下面创建回调规则。该 API 接口不支持匿名请求，您需要使用帯 Authorization 签名认证的请求才能创建新的 Bucket 回调规则。创建 Bucket 回调规则的用户默认成为 Bucket 的持有者。新创建的回调规则会覆盖之前的老的回调规则


### 细节分析


1. 新创建的回调规则会覆盖之前的老的回调规则。


### Response


#### Special Errors

在该请求下经常会发生的一些错误如下：

|错误码|描述|HTTP状态码|
|:--|:--|:--|
| InvalidDigest |用户带的Content-MD5和COS计算body的Content-MD5不一致| 400 Bad Request|
| MalformedXM |传入的xml格式有误,请跟restful api文档仔细比对|400 Bad Request|
| InvalidArgument |Event不可重复，重复会返回此错误| 400 Bad Request|

## Get Bucket Notification

### 功能描述

Get Bucket Notification 接口请求可以获取指定bucket下面的所有的回调事件规则。

### 细节分析

### Response


#### Special Errors

无

## Put Bucket Refer

### 功能描述

Put Bucket Refer 接口请求可以在指定Bucket下面设置refer的黑白名单。该 API 接口不支持匿名请求，您需要使用帯 Authorization 签名认证的请求才能调用此接口。


### 细节分析


1. 新的黑白名单的refer会覆盖之前的refer名单。


### Response


#### Special Errors

在该请求下经常会发生的一些错误如下：

|错误码|描述|HTTP状态码|
|:--|:--|:--|
| InvalidDigest |用户带的Content-MD5和COS计算body的Content-MD5不一致| 400 Bad Request|
| MalformedXM |传入的xml格式有误,请跟restful api文档仔细比对|400 Bad Request|


## Get Bucket Refer

### 功能描述

Get Bucket Refer 接口请求可以获取指定bucket下面的所有的refer列表。

### 细节分析

### Response


#### Special Errors

无


## Delete Object

### 功能描述

Delete Object 接口可以删除指定bucket下面的指定文件，该接口需要调用对文件拥有读写权限


### 细节分析

1.	在Delete Objects请求中删除一个不存在的Object，仍然认为是成功的, 返回204 No Content
2.  Delete Object要求用户对该Object要有写权限


### Response


#### Special Errors

在该请求下经常会发生的一些错误如下：

|错误码|描述|HTTP状态码|
|:--|:--|:--|
| NoSuchBucket |bucket不存在| 404 Not Found|


获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)
