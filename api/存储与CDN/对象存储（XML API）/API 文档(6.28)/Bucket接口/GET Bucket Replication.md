## 功能描述
GET Bucket replication 接口用于查询存储桶中用户跨地域复制配置信息。用户发起该请求时需获得请求签名，表明该请求已获得许可。

## 请求
#### 请求示例

```shell
GET /?replication HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部
该请求操作无特殊的请求头部信息。

#### 请求体
该请求的请求体为空。

## 响应
#### 响应头
#### 公共响应头 
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

|参数项|类型|描述|
|---|---|---|
|x-cos-replication-rule-creation-time|UTC 时间戳格式|跨地域复制规则创建时间|

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<ReplicationConfiguration>
	<Role>qcs::cam::uin/[UIN]:uin/[Subaccount]</Role>
	<Rule>
		<Status></Status>
		<ID></ID>
		<Prefix></Prefix>
		<Destination>
			<Bucket>qcs::cos:[Region]::[BucketName-APPID]</Bucket>
		</Destination>
	</Rule>
</ReplicationConfiguration>
```

具体内容描述如下：

|节点名称（关键字）|    父节点|    描述    |类型|    必选|
|---|---|---|---|---|
|ReplicationConfiguration    |无    |说明所有跨地域配置信息    |Container    |是|
|Role|ReplicationConfiguration    |发起者身份标示：<br>`qcs::cam::uin/&lt;OwnerUin>:uin/&lt;SubUin>`  |String    |是|
|Rule    |ReplicationConfiguration    |具体配置信息，最多支持1000个，所有策略只能指向一个目标存储桶    |Container    |是|
|ID    |ReplicationConfiguration.Rule    |用来标注具体 Rule 的名称    |String    |否|
|Status    |ReplicationConfiguration.Rule    |标识 Rule 是否生效，枚举值：Enabled，Disabled    |String    |是|
|Prefix    |ReplicationConfiguration.Rule    |前缀匹配策略，不可重叠，重叠返回错误，前缀匹配根目录为空    |String    |是|
|Destination    |ReplicationConfiguration.Rule    |目标存储桶信息    |Container    |是|
|Bucket    |ReplicationConfiguration.Rule.Destination    |资源标识符：<br>`qcs::cos:[region]::[bucketname-Appid]`   |String    |是|
|StorageClass    |ReplicationConfiguration.Rule.Destination    |存储级别，枚举值：Standard，Standard_IA，默认值：原存储桶级别    |String    |否|


## 错误分析
该请求可能会发生的一些常见的特殊错误如下，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。


| 错误代码                              | 描述                   | 状态码        |
| ------------------------------------- | ---------------------- | ------------- |
| ReplicationConfigurationNotFoundError | 无查询的跨地域复制规则 | 404 Not Found |

## 实际案例

#### 请求

下述请求示例展示了从存储桶`originbucket-1250000000`中查询跨地域配置信息。
```shell
GET /?replication HTTP/1.1
Date: Fri, 14 Apr 2019 07:17:19 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1503895278;1503895638&q-key-time=1503895278;1503895638&q-header-list=host&q-url-param-list=replication&q-signature=f77900be432072b16afd8222b4b349aabd837cb9
Host: originbucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 0
```

#### 响应

上述请求后，COS 返回以下响应，表明当前该存储桶内的跨地域复制配置处于启用状态。该规则配置信息中，复制的内容为存储桶`originbucket-1250000000`内包含`testPrefix`前缀的所有对象。对象副本的存储类型默认跟随源存储桶内对象的存储类型。
```shell
Content-Type: application/xml
Content-Length: 309
Connection: keep-alive
Date: Fri, 14 Apr 2019 07:17:19 GMT
Server: tencent-cos
x-cos-replication-rule-creation-time: Fri, 14 Apr 2019 07:06:19 GMT
x-cos-request-id: NWQwMzQ5ZmZfMjBiNDU4NjRfNjAwOV84MzA2MjE=
<ReplicationConfiguration>
	<Role>qcs::cam::uin/100000000001:uin/100000000001</Role>
	<Rule>
		<Status>Enabled</Status>
		<ID>RuleId_01</ID>
		<Prefix>testPrefix</Prefix>
		<Destination>
			<Bucket>qcs::cos:ap-guangzhou::destinationBucket-1250000000</Bucket>
		</Destination>
	</Rule>
</ReplicationConfiguration>
```
