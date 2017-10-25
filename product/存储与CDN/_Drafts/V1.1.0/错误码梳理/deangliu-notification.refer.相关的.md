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






获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)
