## 功能描述
GET Service 接口是用来查询请求者名下的所有存储桶列表或特定地域下的存储桶列表（Bucket list）。

## 请求
### 请求示例


```bash
GET / HTTP/1.1
Host: service.cos.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>-  Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
>- Host：查询全部存储桶列表指定为 `service.cos.myqcloud.com`，查询特定地域下的存储桶列表指定为 `cos.<Region>.myqcloud.com`。

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

## 响应
### 响应头

#### 公共响应头
该响应使用公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头
该请求操作无特殊的响应头部信息。

### 响应体
查询成功，返回 application/xml 数据，包含所有或特定地域下的存储桶列表。
```bash
<ListAllMyBucketsResult>
	<Owner>
		<ID>string</ID>
		<DisplayName>string</DisplayName>
	</Owner>
	<Buckets>
		<Bucket>
			<Name>string</Name>
			<Location>string</Location>
			<CreationDate>date</CreationDate>
		</Bucket>
		<Bucket>
			<Name>string</Name>
			<Location>string</Location>
			<CreationDate>date</CreationDate>
		</Bucket>
		...
	</Buckets>
</ListAllMyBucketsResult>
```

具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型
---|---|---|---
ListAllMyBucketsResult|无|说明本次响应的所有信息|Container

Container 节点 ListAllMyBucketsResult 的内容：

节点名称（关键字）|父节点|描述|类型
---|---|---|---
Owner|ListAllMyBucketsResult|说明存储桶持有者的信息|Container
Buckets|ListAllMyBucketsResult|说明本次响应的所有存储桶列表信息|Container

Container 节点 Owner 的内容：

节点名称（关键字）|父节点|描述|类型
---|---|---|---
ID|ListAllMyBucketsResult.Owner|存储桶所有者的 ID|string
DisplayName|ListAllMyBucketsResult.Owner|存储桶所有者的名字信息|string

Container 节点 Buckets 的内容：

节点名称（关键字）|父节点|描述|类型
---|---|---|---
Bucket|ListAllMyBucketsResult.Buckets|单个存储桶的信息|Container

Container 节点 Bucket 的内容：

节点名称（关键字）|父节点|描述|类型
---|---|---|---
Name|ListAllMyBucketsResult.Buckets.Bucket|存储桶的名称|string
Location|ListAllMyBucketsResult.Buckets.Bucket|存储桶所在地域。枚举值参见 [可用地域](https://cloud.tencent.com/document/product/436/6224) 文档，如：ap-beijing，ap-hongkong，eu-frankfurt 等|string
CreationDate|ListAllMyBucketsResult.Buckets.Bucket|存储桶创建时间。ISO8601 格式，例如 2016-11-09T08:46:32.000Z|date


### 错误码

该请求操作无特殊错误信息，常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。


## 实际案例

### 查询所有存储桶列表

#### 请求

```bash
GET / HTTP/1.1
Host: service.cos.myqcloud.com
Date: Mon, 13 May 2019 06:55:33 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1557730533;1557737733&q-key-time=1557730533;1557737733&q-header-list=host&q-url-param-list=&q-signature=7f155ce6fb47be41b9a550b4d3884a01b818****
```

#### 响应

```bash
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 804
Connection: close
Date: Mon, 13 May 2019 06:55:35 GMT
server: tencent-cos
x-cos-request-id: NWNkOTE0ZTZfOGViMjM1MGFfMjJlOF9iOTU4****

<ListAllMyBucketsResult>
	<Owner>
		<ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
	</Owner>
	<Buckets>
		<Bucket>
			<Name>examplebucket-1250000000</Name>
			<Location>ap-shanghai</Location>
			<CreationDate>2018-08-19T08:09:43Z</CreationDate>
		</Bucket>
		<Bucket>
			<Name>examplebucket2-1250000000</Name>
			<Location>ap-shanghai</Location>
			<CreationDate>2018-08-20T03:34:42Z</CreationDate>
		</Bucket>
		<Bucket>
			<Name>examplebucket3-1250000000</Name>
			<Location>eu-frankfurt</Location>
			<CreationDate>2018-08-20T08:10:00Z</CreationDate>
		</Bucket>
		<Bucket>
			<Name>examplebucket4-1250000000</Name>
			<Location>eu-frankfurt</Location>
			<CreationDate>2018-08-20T08:10:21Z</CreationDate>
		</Bucket>
	</Buckets>
</ListAllMyBucketsResult>
```

### 查询特定地域下的存储桶列表

#### 请求

```bash
GET / HTTP/1.1
Host: cos.ap-shanghai.myqcloud.com
Date: Mon, 13 May 2019 06:55:33 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1557738249;1557745449&q-key-time=1557738249;1557745449&q-header-list=host&q-url-param-list=&q-signature=3fe7832a0594e5e01c725fcf567d314fb9af****
```

#### 响应

```bash
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 492
Date: Mon, 13 May 2019 06:55:35 GMT
server: tencent-cos
x-cos-request-id: NWNkOTMzMGJfNmNhYjM1MGFfMWMzYjRfYWY5****

<ListAllMyBucketsResult>
	<Owner>
		<ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
	</Owner>
	<Buckets>
		<Bucket>
			<Name>examplebucket-1250000000</Name>
			<Location>ap-shanghai</Location>
			<CreationDate>2018-08-19T08:09:43Z</CreationDate>
		</Bucket>
		<Bucket>
			<Name>examplebucket2-1250000000</Name>
			<Location>ap-shanghai</Location>
			<CreationDate>2018-08-20T03:34:42Z</CreationDate>
		</Bucket>
	</Buckets>
</ListAllMyBucketsResult>
```
