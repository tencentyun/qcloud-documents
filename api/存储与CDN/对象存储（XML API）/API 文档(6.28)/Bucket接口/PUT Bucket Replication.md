## 功能描述
PUT Bucket replication 用于向已启用版本控制的存储桶中配置跨区域复制规则。如果存储桶已经配置了跨区域复制规则，那么该请求会替换现有配置。

>!使用该接口时，需确保存储桶已经开启版本控制，开启版本控制的 API 文档请参阅 [PUT Bucket versioning 接口文档](https://cloud.tencent.com/document/product/436/19889)。

## 请求
### 请求示例

```
PUT /?replication HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-MD5: MD5
Authorization: Auth String
request body
```

>Authorization: Auth String （详细参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节）。

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
用户在请求体中设置跨区域复制的具体配置信息。配置信息包括跨区域复制规则的启用状态、复制内容、目标存储桶的存储桶名和存储区域等信息。对于每一个已启用版本控制的存储桶，COS 目前仅支持一条跨区域复制规则。

```
<ReplicationConfiguration>
	<Role>qcs::cam::uin/[UIN]:uin/[Subaccount]</Role>
	<Rule>
		<Status></Status>
		<ID></ID>
		<Prefix></Prefix>
		<Destination>
			<Bucket>qcs::cos:[Region]::[Bucketname-Appid]</Bucket>
		</Destination>
	</Rule>
</ReplicationConfiguration>
```

具体内容描述如下：

|节点名称（关键字）|    父节点|    描述    |类型|    必选|
|---|---|---|---|---|
|ReplicationConfiguration    |无    |说明所有跨区域配置信息    |Container    |是|
|Role|ReplicationConfiguration    |发起者身份标示：qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>      |String    |是|
|Rule    |ReplicationConfiguration    |具体配置信息，最多支持 1000 个，所有策略只能指向一个目标存储桶    |Container    |是|
|ID    |ReplicationConfiguration.Rule    |用来标注具体 Rule 的名称    |String    |否|
|Status    |ReplicationConfiguration.Rule    |标识 Rule 是否生效，枚举值：Enabled, Disabled    |String    |是|
|Prefix    |ReplicationConfiguration.Rule    |前缀匹配策略，不可重叠，重叠返回错误。前缀匹配根目录为空    |String    |是|
|Destination    |ReplicationConfiguration.Rule    |目标存储桶信息    |Container    |是|
|Bucket    |ReplicationConfiguration.Rule.Destination    |资源标识符：qcs::cos:[region]::[bucketname-AppId] |String    |是|
|StorageClass    |ReplicationConfiguration.Rule.Destination    |存储级别，枚举值：STANDARD, STANDARD_IA；默认值：原存储桶级别<br>**注意：** 目前跨区域复制暂不支持将复制后的对象指定为归档存储这一存储类型，如您需要将对象副本设置为归档存储类型，可在目标存储桶中配置生命周期管理，详细操作可查阅 [PUT Bucket lifecycle](https://cloud.tencent.com/document/product/436/8280)|String    |否|

## 响应

### 响应头
#### 公共响应头 
该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该请求的响应无特殊的响应头。

### 响应体
该响应体为空。

### 错误分析
该请求可能会发生的一些常见的特殊错误如下，常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/436/7730) 章节。

|错误代码|    描述|    状态码|
|---|---|---|
|InvalidBucketState|当前存储桶未开启版本控制导致无法开启跨区域复制功能|409 Conflict|
|InvalidArgument|不合法的参数内容|400 Bad Request|

## 实际案例
### 请求

```
PUT /?replication HTTP/1.1
Date: Mon, 28 Aug 2017 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1503888878;1503889238&q-key-time=1503888878;1503889238&q-header-list=host&q-url-param-list=replication&q-signature=254bf9cd3d6615e89a36ab652437f9d45c5f63f9
Content-MD5: AAq9nzrpsz5LJ4UEe1f6Q==
Host: sevenyounorthtest-7319456.cos.ap-guangzhou.myqcloud.com
Content-Length: 312

<ReplicationConfiguration>
	<Role>qcs::cam::uin/123456789:uin/987654543</Role>
	<Rule>
		<Status>Enabled</Status>
		<ID>RuleId_01</ID>
		<Prefix>sevenyou_10m</Prefix>
		<Destination>
			<Bucket>qcs::cos:ap-guangzhou::sevenyousouthtest-132213432</Bucket>
		</Destination>
	</Rule>
</ReplicationConfiguration>
```

### 响应

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Mon, 28 Aug 2017 02:53:38 GMT
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF84Y2M
```
