## Put Replication

### 功能描述

Put Bucket Replication 请求用于向开启版本管理的存储桶添加 replication 配置。如果存储桶已经拥有 replication 配置，那么该请求会替换现有配置。

### 细节分析


1. 使用该接口存储桶必须已经开启版本管理，版本管理详细请参见[Put Bucket Versioning](https://cloud.tencent.com/document/product/436/8591 "Put Bucket Versioning")

### Response

#### Special Errors

|错误码|描述|HTTP状态码|
|:--|:--|:--|
|MalformedXML|XML格式不合法,请跟restful api文档仔细比对 |400 Bad Request|
|MultiBucketNotSupport|跨区域复制只能设一个目的bucket|400 Bad Request|
|NotSupportedStorageClass|指定的存储类型不合法|400 Bad Request|
|InvalidBucketState|bucket状态与操作请求冲突，比如多版本管理与跨区域复制的冲突|409 Conflict|
|InvalidBucketName|Bucket名称不合法|400 Bad Request|

备注：具体的错误原因可参考返回的message进行排查。
获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)

## Get Replication

### 功能描述

Get Bucket Replication 接口请求实现读取存储桶中用户跨区域复制配置信息。

### 细节分析

### Response

#### Special Errors

|错误码|描述|HTTP状态码|
|:--|:--|:--|
|NoSuchBucket|当访问的Bucket不存在|404 Not Found|

备注：具体的错误原因可参考返回的message进行排查。
获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)

## Put Bucket Lifecycle

### 功能描述

COS 支持用户以生命周期配置的方式来管理 Bucket 中 Object 的生命周期。生命周期配置包含一个或多个将应用于一组对象规则的规则集 (其中每个规则为 COS 定义一个操作)。

### 细节分析
Put Bucket Lifecycle 用于为 Bucket 创建一个新的生命周期配置。如果该 Bucket 已配置生命周期，使用该接口创建新的配置的同时则会覆盖原有的配置。

### Response

#### Special Errors

|错误码|描述|HTTP状态码|
|:--|:--|:--|
|NoSuchBucket|当访问的Bucket不存在|404 Not Found|
|MalformedXML|XML格式不合法,请跟restful api文档仔细比对 |400 Bad Request|
|InvalidRequest|请求不合法，如果错误描述中显示"Conflict lifecycle rule"，那么表示xml数据中的多条rule有相互冲突的部分。|400 Bad Reques|
|InvalidArgument|请求参数不合法, 如果错误描述中显示"Rule ID must be unique. Found same ID for more than one rule", 那么表示有多个Rule的id字段相同。|400 Bad Reques|


备注：具体的错误原因可参考返回的message进行排查。
获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)

## Get Bucket Lifecycle

### 功能描述

Get Bucket Lifecycle 用来查询 Bucket 的生命周期配置。

### 细节分析

### Response

#### Special Errors

|错误码|描述|HTTP状态码|
|:--|:--|:--|
|NoSuchBucket|当访问的Bucket不存在|404 Not Found|
|NoSuchLifecycleConfiguration|生命周期配置不存在。|404 Not Found|

## Post Object

### 功能描述

Post Object使用HTML表单上传文件到指定bucket。

### 细节分析

### Response

#### Special Errors

|错误码|描述|HTTP状态码|
|:--|:--|:--|
|MalformedPOSTRequest|该POST请求的Body内容不合法|400 Bad Request|
|InvalidArgument|请求参数不合法|404 Not Found|
