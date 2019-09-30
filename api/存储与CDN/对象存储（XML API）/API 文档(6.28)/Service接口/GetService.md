## 功能描述

GET Service 接口是用来查询请求者名下的所有存储桶列表或特定地域下的存储桶列表。

## 请求

#### 请求示例

**示例一**

```shell
GET / HTTP/1.1
Host: service.cos.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

**示例二**

```shell
GET / HTTP/1.1
Host: cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> ?
> - Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - Host: 查询全部存储桶列表指定为`service.cos.myqcloud.com`，查询特定地域下的存储桶列表指定为`cos.<Region>.myqcloud.com`。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

查询成功，返回 **application/xml** 数据，包含所有或特定地域下的存储桶列表。

```shell
<ListAllMyBucketsResult>
	<Owner>
		<ID>string</ID>
		<DisplayName>string</DisplayName>
	</Owner>
	<Buckets>
		<Bucket>
			<Name>string</Name>
			<Location>Enum</Location>
			<CreationDate>date</CreationDate>
		</Bucket>
		<Bucket>
			<Name>string</Name>
			<Location>Enum</Location>
			<CreationDate>date</CreationDate>
		</Bucket>
	</Buckets>
</ListAllMyBucketsResult>
```

具体的节点描述如下：

| 节点名称（关键字）     | 父节点 | 描述                            | 类型      |
| ---------------------- | ------ | ------------------------------- | --------- |
| ListAllMyBucketsResult | 无     | 保存 GET Service 结果的所有信息 | Container |

**Container 节点 ListAllMyBucketsResult 的内容：**

| 节点名称（关键字） | 父节点                 | 描述             | 类型      |
| ------------------ | ---------------------- | ---------------- | --------- |
| Owner              | ListAllMyBucketsResult | 存储桶持有者信息 | Container |
| Buckets            | ListAllMyBucketsResult | 存储桶列表       | Container |

**Container 节点 Owner 的内容：**

| 节点名称（关键字） | 父节点                       | 描述                                                         | 类型   |
| ------------------ | ---------------------------- | ------------------------------------------------------------ | ------ |
| ID                 | ListAllMyBucketsResult.Owner | 存储桶持有者的完整 ID，格式为`qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]`<br>例如`qcs::cam::uin/100000000001:uin/100000000001` | string |
| DisplayName        | ListAllMyBucketsResult.Owner | 存储桶持有者的名字                                           | string |

**Container 节点 Buckets 的内容：**

| 节点名称（关键字） | 父节点                         | 描述       | 类型      |
| ------------------ | ------------------------------ | ---------- | --------- |
| Bucket             | ListAllMyBucketsResult.Buckets | 存储桶信息 | Container |

**Container 节点 Buckets.Bucket 的内容：**

| 节点名称（关键字） | 父节点                                | 描述                                                         | 类型   |
| ------------------ | ------------------------------------- | ------------------------------------------------------------ | ------ |
| Name               | ListAllMyBucketsResult.Buckets.Bucket | 存储桶的名称，格式为`<BucketName-APPID>`<br>例如 `examplebucket-1250000000` | string |
| Location           | ListAllMyBucketsResult.Buckets.Bucket | 存储桶所在地域，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 文档<br>例如 ap-beijing，ap-hongkong，eu-frankfurt 等 | Enum   |
| CreationDate       | ListAllMyBucketsResult.Buckets.Bucket | 存储桶的创建时间，为 ISO8601 格式，例如2019-05-24T10:56:40Z    | date   |

#### 错误码

此接口无特殊错误信息，全部错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：查询所有存储桶列表

#### 请求

```shell
GET / HTTP/1.1
Host: service.cos.myqcloud.com
Date: Fri, 24 May 2019 11:59:50 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558699190;1558706390&q-key-time=1558699190;1558706390&q-header-list=date;host&q-url-param-list=&q-signature=89fa1f6a56c34e460f3db4d65f928eaf034a****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 805
Connection: close
Date: Fri, 24 May 2019 11:59:51 GMT
Server: tencent-cos
x-cos-request-id: NWNlN2RjYjdfOGFiMjM1MGFfNTVjMl8zMmI1****

<ListAllMyBucketsResult>
	<Owner>
		<ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
	</Owner>
	<Buckets>
		<Bucket>
			<Name>examplebucket1-1250000000</Name>
			<Location>ap-beijing</Location>
			<CreationDate>2019-05-24T11:49:50Z</CreationDate>
		</Bucket>
		<Bucket>
			<Name>examplebucket2-1250000000</Name>
			<Location>ap-beijing</Location>
			<CreationDate>2019-05-24T11:51:50Z</CreationDate>
		</Bucket>
		<Bucket>
			<Name>examplebucket3-1250000000</Name>
			<Location>eu-frankfurt</Location>
			<CreationDate>2019-05-24T11:53:50Z</CreationDate>
		</Bucket>
		<Bucket>
			<Name>examplebucket4-1250000000</Name>
			<Location>eu-frankfurt</Location>
			<CreationDate>2019-05-24T11:55:50Z</CreationDate>
		</Bucket>
	</Buckets>
</ListAllMyBucketsResult>
```

#### 案例二：查询特定地域下的存储桶列表

#### 请求

```shell
GET / HTTP/1.1
Host: cos.ap-beijing.myqcloud.com
Date: Fri, 24 May 2019 11:59:51 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558699191;1558706391&q-key-time=1558699191;1558706391&q-header-list=date;host&q-url-param-list=&q-signature=c3f55f4ce2800fb343cf85ff536a9185a0c1****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 495
Connection: close
Date: Fri, 24 May 2019 11:59:51 GMT
Server: tencent-cos
x-cos-request-id: NWNlN2RjYjdfZjhjODBiMDlfOWNlNF9hYzc2****

<ListAllMyBucketsResult>
	<Owner>
		<ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
	</Owner>
	<Buckets>
		<Bucket>
			<Name>examplebucket1-1250000000</Name>
			<Location>ap-beijing</Location>
			<CreationDate>2019-05-24T11:49:50Z</CreationDate>
		</Bucket>
		<Bucket>
			<Name>examplebucket2-1250000000</Name>
			<Location>ap-beijing</Location>
			<CreationDate>2019-05-24T11:51:50Z</CreationDate>
		</Bucket>
	</Buckets>
</ListAllMyBucketsResult>
```
