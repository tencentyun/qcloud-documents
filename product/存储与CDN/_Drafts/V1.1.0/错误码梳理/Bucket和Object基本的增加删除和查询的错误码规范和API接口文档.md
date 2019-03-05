## GetService

### 功能描述

Get Service 接口是用来获取请求者名下的所有存储空间列表（Bucket list）。

### 细节分析


1. 该 API 接口不支持匿名请求，您需要使用帯 Authorization 签名认证的请求才能获取 Bucket 列表，且只能获取签名中 AccessID 所属账户的 Bucket 列表。

### Response

#### Special Errors

> 该章节描述次请求可能会发生的一些特殊的且常见的错误情况

|错误码|描述|HTTP状态码|
|:--|:--|:--|
|AccessDenied|1. 请求中没有用户验证信息（签名为空，即匿名访问）； 2. 用户使用v4的签名调用了该接口，同样会返回该错误|403 Forbidden|


备注：具体的错误原因可参考返回的message进行排查。
获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)

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


获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)


## DeleteBucket

### 功能描述

Delete Bucket接口请求可以在指定账号下删除Bucket， 删除之前要求Bucket内的内容为空，只有删除了Bucket内的信息，才能删除Bucket本身。

### Response

#### Special Errors

> 该章节描述次请求可能会发生的一些特殊的且常见的错误情况

在该请求下经常会发生的一些错误如下：

|错误码|描述|HTTP状态码|
|:--|:--|:--|
|BucketNotEmpty|不能删除一个非空的Bucket|409 Conflict|
|AccessDenied|删除Bucket同样需要携带签名，如果试图删除一个没有访问权限的Bucket，就会返回这个错误|403 Forbidden|
|NoSuchBucket|如果删除一个不存在的Bucket，就回返回该错误|404 Not Found|

获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)

## Get Bucket

### 功能描述

Get Bucket请求等同于List Object请求，可以列出指定Bucket下的部分或者全部Object。 此API调用者需要对Bucket有Read权限。

### 细节分析

1. 每次默认返回的最大条目数为1000条，如果无法一次返回所有的list，则返回结果中的IsTruncated为true，同时会附加一个NextMarker字段，提示下一个条目的起点。若一次请求，已经返回了整个list，则不会有NextMarker这个字段，同时IsTruncated为false。
2. 若把prefix设置为某个文件夹的全路径名，则可以列出以此prefix为开头的文件，也即是该文件夹下递归的所有文件和子文件夹。如果再设置delimiter定界符为/，则只列出该文件夹下的文件，子文件夹下递归的文件和文件夹名将不被列出。而子文件夹名将会以CommonPrefix的形式给出。

### Response

#### Special Errors

> 该章节描述次请求可能会发生的一些特殊的且常见的错误情况

在该请求下经常会发生的一些错误如下：

|错误码|描述|HTTP状态码|
|:--|:--|:--|
|NoSuchBucket|如果访问的Bucket不存在，则会返回该错误|404 Not Found|
|InvalidBucketName|请求的Bucket名字不符合规范|400 Bad Request|
|AccessDenied|如果没有访问该Bucket的权限，则会返回该错误|403 Forbidden|
|InvalidArgument|如果max-keys大于1000，则会返回该错误|400 Bad Request|
|InvalidURI|如果prefix、marker或者delimiter的参数不符合要求（必须小于1024），则会返回该错误|400 Bad Request|

获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)

## Head Bucket

### 功能描述
Head Bucket请求可以确认该Bucket是否存在，是否有权访问。Head的权限与Read的一致。当该Bucket存在的时候，返回HTTP状态码200，同时在响应的头部；当该Bucket无访问权限的时候，返回HTTTP状态码403；当该Bucket不存在的时候，则会返回404。


备注： 目前我们还没有公开获取Bucket属性的接口（即可以返回ACL等信息）

## Head Object

### 功能描述

Head Object接口用于获取对应Object的meta信息。


### 细节分析

1. Head Object请求是不返回消息体的。
3. 这里的If-Modified-Since统一采用GMT(RFC822)时间格式，例如：Tue, 22 Oct 2017 01:35:21 GMT。
4. 如果head的文件不存在，则会返回404 NOT FOUND。

### Response

#### Special Errors

> 该章节描述次请求可能会发生的一些特殊的且常见的错误情况

在该请求下经常会发生的一些错误如下：

|错误码|描述|HTTP状态码|
|:--|:--|:--|
|SSEHeaderNotAllowed|如果头部携带x-cos-server-side-encryption的标头，就会返回该错误|400 Bad Request|

获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)


