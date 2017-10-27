## Get Bucket Location

### 功能描述

Get Bucket Location接口可以获取一个Bucket所在的区域。


### 细节分析

> 目前区域的有效值包括ap-beijing，ap-beijing，ap-shanghai，ap-guangzhou，ap-chengdu，ap-singapore，ap-hongkong，na-toronto，eu-frankfurt分别对应北京一区，北京，上海，广州，成都，新加坡，相关，多伦多和法兰克福等地数据中心


1. 查看bucket区域信息，需要有该bucket的读权限。


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
