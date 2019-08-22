## 功能描述
PUT Bucket replication 用于向已启用版本控制的存储桶中配置跨地域复制规则。如果存储桶已经配置了跨地域复制规则，那么该请求会替换现有配置。

>!使用该接口时，需确保存储桶已经开启版本控制，开启版本控制的 API 文档请参见 [PUT Bucket versioning](https://cloud.tencent.com/document/product/436/19889)  接口文档。

## 请求
#### 请求示例

```http
PUT /?replication HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-MD5: MD5
Authorization: Auth String
request body
```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部
该请求操作无特殊的请求头部信息。

#### 请求体
用户在请求体中设置跨地域复制的具体配置信息。配置信息包括跨地域复制规则的启用状态、复制内容、目标存储桶的存储桶名和存储区域等信息。对于每一个已启用版本控制的存储桶，COS 目前仅支持一条跨地域复制规则。

```http
<ReplicationConfiguration>
	<Role>qcs::cam::uin/<OwnerUin>:uin/<SubUin></Role>
	<Rule>
		<Status></Status>
		<ID></ID>
		<Prefix></Prefix>
		<Destination>
			<Bucket>qcs::cos:<Region>::<BucketName-APPID></Bucket>
		</Destination>
	</Rule>
</ReplicationConfiguration>
```

具体内容描述如下：

|节点名称（关键字）|    父节点|    描述    |类型|    必选|
|---|---|---|---|---|
|ReplicationConfiguration    |无    |说明所有跨地域配置信息    |Container    |是|
|Role|ReplicationConfiguration    |发起者身份标示：`qcs::cam::uin/<OwnerUin>:uin/<SubUin>`      |String    |是|
|Rule    |ReplicationConfiguration    |具体配置信息，最多支持1000个，所有策略只能指向一个目标存储桶    |Container    |是|
|ID    |ReplicationConfiguration.Rule    |用来标注具体 Rule 的名称    |String    |否|
|Status    |ReplicationConfiguration.Rule    |标识 Rule 是否生效，枚举值：Enabled, Disabled    |String    |是|
|Prefix    |ReplicationConfiguration.Rule    |前缀匹配策略，不可重叠，重叠返回错误。前缀匹配根目录为空    |String    |是|
|Destination    |ReplicationConfiguration.Rule    |目标存储桶信息    |Container    |是|
|Bucket    |ReplicationConfiguration.Rule.Destination    |资源标识符：`qcs::cos:<Region>::<BucketName-APPID>`|String    |是|
|StorageClass    |ReplicationConfiguration.Rule.Destination    |存储级别，枚举值：STANDARD，STANDARD_IA；默认值：原存储桶级别<br>**注意：** 目前跨地域复制暂不支持将复制后的对象指定为归档存储这一存储类型，如您需要将对象副本设置为归档存储类型，可在目标存储桶中配置生命周期管理，详细操作可查阅 [PUT Bucket lifecycle](https://cloud.tencent.com/document/product/436/8280)|String    |否|

## 响应

#### 响应头
#### 公共响应头 
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。
#### 特有响应头
该请求的响应无特殊的响应头。

#### 响应体
该响应体为空。

#### 错误分析
该请求可能会发生的一些常见的特殊错误如下，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

|错误代码|    描述|    状态码|
|---|---|---|
|InvalidBucketState|当前存储桶未开启版本控制，导致无法开启跨地域复制功能|409 Conflict|
|InvalidArgument|不合法的参数内容|400 Bad Request|

## 实际案例
#### 请求
以下 PUT Bucket replication 请求向存储桶`originbucket-1250000000`中添加一条跨地域复制配置。该跨地域复制配置中，指定复制前缀为`testPrefix`的对象内容，目标存储桶为广州的`destinationbucket-1250000000`。
```shell
PUT /?replication HTTP/1.1
Date: Mon, 28 Aug 2017 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1503888878;1503889238&q-key-time=1503888878;1503889238&q-header-list=host&q-url-param-list=replication&q-signature=254bf9cd3d6615e89a36ab652437f9d45c5f****
Content-MD5: AAq9nzrpsz5LJ4UEe1f6Q==
Host: originbucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 312

<ReplicationConfiguration>
	<Role>qcs::cam::uin/100000000001:uin/100000000001</Role>
	<Rule>
		<Status>Enabled</Status>
		<ID>RuleId_01</ID>
		<Prefix>testPrefix</Prefix>
		<Destination>
			<Bucket>qcs::cos:ap-guangzhou::destinationbucket-1250000000</Bucket>
		</Destination>
	</Rule>
</ReplicationConfiguration>
```

#### 响应

上述请求后，COS 返回以下响应，表明当前该跨地域配置已经成功设置完毕。
```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 14 Apr 2019 07:06:19 GMT
Server: tencent-cos
x-cos-bucket-region: ap-guangzhou
x-cos-request-id: NWQwMzQ3NmJfMjRiMjU4NjRfOTM4NV82ZDU1****
x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODc0OWRkZjk0ZDM1NmI1M2E2MTRlY2MzZDhmNmI5MWI1OWE4OGMxZjNjY2JiNTBmMTVmMWY1MzAzYzkyZGQ2ZWM4MzUyZTg1NGRhNWY0NTJiOGUyNTViYzgyNzgxZTEwOTY=
```
