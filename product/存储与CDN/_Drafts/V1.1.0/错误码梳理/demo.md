## Put Bucket

### 功能描述

Put Bucket 接口请求可以在指定账号下创建一个 Bucket。该 API 接口不支持匿名请求，您需要使用帯 Authorization 签名认证的请求才能创建新的 Bucket 。创建 Bucket 的用户默认成为 Bucket 的持有者。


### 细节分析

> 此处描述一些非错误相关的东西，和注意事项。比如该接口的模型，该接口需要的前置条件等等


1. 创建bucket的时候，如果没有指定访问权限，则默认使用私有读写(private)权限。


### Response


#### Special Errors

> 该章节描述次请求可能会发生的一些特殊的且常见的错误情况

在该请求下经常会发生的一些错误如下：

|错误码|描述|HTTP状态码|
|:--|:--|:--|
| BucketAlreadyExists |当请求创建的bucket已经存在，并且请求创建的用户就是拥有者| 409 Conflict|
| InvalidBucketName |bucket的命名不规范 具体原因可参考message的描述|400 Bad Request|
| InvalidRequest |bucket的命名不规范 具体原因可参考message的描述| 400 Bad Request|
||如果bucket设置的ACL不正确，也会导致创建bucket失败，同时会返回“Failed to set access control authority for the bucket”的错误信息。具体错误原因，可根据返回的错误码参考[Put Bucket ACL](https://cloud.tencent.com/document/product/436/7737) 相关的文档||

> 如果该错误有多个错误信息请按照如下格式来书写：

|错误码|描述|HTTP状态码|
|:--|:--|:--|
| BucketAlreadyExists |1. 当请求创建的bucket已经存在，并且请求创建的用户就是拥有者 <br> 2. sdfsdfs| 409 Conflict|

获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)
