## 功能描述

GET Bucket Object versions 接口用于拉取存储桶内的所有对象及其历史版本信息，您可以通过指定参数筛选出存储桶内部分对象及其历史版本信息。该 API 的请求者需要对存储桶有读取权限。

## 请求

#### 请求示例

```shell
GET /?versions HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

| 名称 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
| prefix | 对象键匹配前缀，限定响应中只包含指定前缀的对象键 | string | 否 |
| delimiter | 一个字符的分隔符，用于对对象键进行分组。所有对象键中从 prefix 或从头（若未指定 prefix）到首个 delimiter 之间相同的部分将作为 CommonPrefixes 下的一个 Prefix 节点。被分组的对象键不再出现在后续对象列表中，具体场景和用法可参考下面的实际案例 | string | 否 |
| encoding-type | 规定返回值的编码方式，可选值：url，代表返回的对象键为 URL 编码（百分号编码）后的值，例如“腾讯云”将被编码为`%E8%85%BE%E8%AE%AF%E4%BA%91` | string | 否 |
| key-marker | 起始对象键标记，从该标记之后（不含）按照 UTF-8 字典序返回对象版本条目 | string | 否 |
| version-id-marker | 起始版本 ID 标记，从该标记之后（不含）返回对象版本条目 | string | 否 |
| max-keys | 单次返回最大的条目数量，默认值为1000，最大为1000 | integer | 否 |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

查询成功，返回 **application/xml** 数据，包含存储桶中的对象版本信息。不同场景下的响应体请参见下方的实际案例。

```shell
<ListVersionsResult>
	<Name>string</Name>
	<Prefix>string</Prefix>
	<KeyMarker>string</KeyMarker>
	<VersionIdMarker>string</VersionIdMarker>
	<MaxKeys>integer</MaxKeys>
	<IsTruncated>boolean</IsTruncated>
	<Delimiter>string</Delimiter>
	<CommonPrefixes>
		<Prefix>string</Prefix>
	</CommonPrefixes>
	<CommonPrefixes>
		<Prefix>string</Prefix>
	</CommonPrefixes>
	<Version>
		<Key>string</Key>
		<VersionId>string</VersionId>
		<IsLatest>boolean</IsLatest>
		<LastModified>date</LastModified>
		<ETag>string</ETag>
		<Size>integer</Size>
		<StorageClass>Enum</StorageClass>
		<Owner>
			<ID>string</ID>
			<DisplayName>string</DisplayName>
		</Owner>
	</Version>
	<DeleteMarker>
		<Key>string</Key>
		<VersionId>string</VersionId>
		<IsLatest>boolean</IsLatest>
		<LastModified>date</LastModified>
		<Owner>
			<ID>string</ID>
			<DisplayName>string</DisplayName>
		</Owner>
	</DeleteMarker>
	<DeleteMarker>
		<Key>string</Key>
		<VersionId>string</VersionId>
		<IsLatest>boolean</IsLatest>
		<LastModified>date</LastModified>
		<Owner>
			<ID>string</ID>
			<DisplayName>string</DisplayName>
		</Owner>
	</DeleteMarker>
	<Version>
		<Key>string</Key>
		<VersionId>string</VersionId>
		<IsLatest>boolean</IsLatest>
		<LastModified>date</LastModified>
		<ETag>string</ETag>
		<Size>integer</Size>
		<StorageClass>Enum</StorageClass>
		<Owner>
			<ID>string</ID>
			<DisplayName>string</DisplayName>
		</Owner>
	</Version>
</ListVersionsResult>
```

具体的节点描述如下：

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| ListVersionsResult | 无 | 保存 GET Bucket Object versions 结果的所有信息 | Container |

**Container 节点 ListVersionsResult 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Name | ListVersionsResult | 存储桶的名称，格式为`<BucketName-APPID>`，例如`examplebucket-1250000000` | string |
| EncodingType | ListVersionsResult | 编码格式，对应请求中的 encoding-type 参数，且仅当请求中指定了 encoding-type 参数才会返回该节点 | string |
| Prefix | ListVersionsResult | 对象键匹配前缀，对应请求中的 prefix 参数 | string |
| KeyMarker | ListVersionsResult | 起始对象键标记，从该标记之后（不含）按照 UTF-8 字典序返回对象版本条目，对应请求中的 key-marker 参数 | string |
| VersionIdMarker | ListVersionsResult | 起始版本 ID 标记，从该标记之后（不含）返回对象版本条目，对应请求中的 version-id-marker 参数 | string |
| MaxKeys | ListVersionsResult | 单次响应返回结果的最大条目数量，对应请求中的 max-keys 参数 | integer |
| Delimiter | ListVersionsResult | 分隔符，对应请求中的 delimiter 参数，且仅当请求中指定了 delimiter 参数才会返回该节点 | string |
| IsTruncated | ListVersionsResult | 响应条目是否被截断，布尔值，例如 true 或 false | boolean |
| NextKeyMarker | ListVersionsResult | 仅当响应条目有截断（IsTruncated 为 true）才会返回该节点，该节点的值为当前响应条目中的最后一个对象键，当需要继续请求后续条目时，将该节点的值作为下一次请求的 key-marker 参数传入 | string |
| NextVersionIdMarker | ListVersionsResult | 仅当响应条目有截断（IsTruncated 为 true）才会返回该节点，该节点的值为当前响应条目中的最后一个对象的版本 ID，当需要继续请求后续条目时，将该节点的值作为下一次请求的 version-id-marker 参数传入 | string |
| CommonPrefixes | ListVersionsResult | 从 prefix 或从头（若未指定 prefix）到首个 delimiter 之间相同的部分，定义为 Common Prefix。仅当请求中指定了 delimiter 参数才有可能返回该节点 | Container |
| Version | ListVersionsResult | 对象版本条目 | Container |
| DeleteMarker | ListVersionsResult | 对象删除标记条目 | Container |

**Container 节点 ListVersionsResult.CommonPrefixes 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Prefix | ListVersionsResult.CommonPrefixes | 单条 Common Prefix 的前缀 | string |

**Container 节点 ListVersionsResult.Version 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Key | ListVersionsResult.Version | 对象键 | string |
| VersionId | ListVersionsResult.Version | 对象的版本 ID | string |
| IsLatest | ListVersionsResult.Version | 当前版本是否为该对象的最新版本 | boolean |
| LastModified | ListVersionsResult.Version | 当前版本的最后修改时间，为 ISO8601 格式，例如2019-05-24T10:56:40Z | date |
| ETag | ListVersionsResult.Version | 对象的实体标签（Entity Tag），是对象被创建时标识对象内容的信息标签，可用于检查对象的内容是否发生变化，例如"8e0b617ca298a564c3331da28dcb50df"。此头部并不一定返回对象的 MD5 值，而是根据对象上传和加密方式而有所不同 | string |
| Size | ListVersionsResult.Version | 对象大小，单位为 Byte | integer |
| StorageClass | ListVersionsResult.Version | 对象存储类型。枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 STANDARD_IA，ARCHIVE | Enum |
| Owner | ListVersionsResult.Version | 对象持有者信息 | Container |

**Container 节点 ListVersionsResult.Version.Owner 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| ID | ListVersionsResult.Version.Owner | 对象持有者的 APPID | string |
| DisplayName | ListVersionsResult.Version.Owner | 对象持有者的名字 | string |

**Container 节点 ListVersionsResult.DeleteMarker 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Key | ListVersionsResult.DeleteMarker | 对象键 | string |
| VersionId | ListVersionsResult.DeleteMarker | 对象的删除标记的版本 ID | string |
| IsLatest | ListVersionsResult.DeleteMarker | 当前删除标记是否为该对象的最新版本 | boolean |
| LastModified | ListVersionsResult.DeleteMarker | 当前删除标记的删除时间，为 ISO8601 格式，例如2019-05-24T10:56:40Z | date |
| Owner | ListVersionsResult.DeleteMarker | 对象持有者信息 | Container |

**Container 节点 ListVersionsResult.DeleteMarker.Owner 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| ID | ListVersionsResult.DeleteMarker.Owner | 对象持有者的 APPID | string |
| DisplayName | ListVersionsResult.DeleteMarker.Owner | 对象持有者的名字 | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：未启用版本控制

#### 请求

```shell
GET /?versions HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 15 Aug 2019 12:03:09 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1565870589;1565877789&q-key-time=1565870589;1565877789&q-header-list=date;host&q-url-param-list=versions&q-signature=1d8fcb8522df7be9fa52d94cd79462f92eb3****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1262
Connection: close
Date: Thu, 15 Aug 2019 12:03:10 GMT
Server: tencent-cos
x-cos-request-id: NWQ1NTQ5ZmVfYjliYjBiMDlfMmFhNGZfY2Jm****

<ListVersionsResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<KeyMarker/>
	<VersionIdMarker/>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>false</IsTruncated>
	<Version>
		<Key>example-object-1.jpg</Key>
		<VersionId/>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-15T12:03:10.000Z</LastModified>
		<ETag>&quot;0f0cd12c48979d1bf3f95255a36cb861&quot;</ETag>
		<Size>20</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<Version>
		<Key>example-object-2.jpg</Key>
		<VersionId/>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-15T12:03:09.000Z</LastModified>
		<ETag>&quot;51370fc64b79d0d3c7c609635be1c41f&quot;</ETag>
		<Size>20</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<Version>
		<Key>example-object-3.jpg</Key>
		<VersionId/>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-15T12:03:08.000Z</LastModified>
		<ETag>&quot;b2f1d893c5fde000ee8ea6eca18ed81f&quot;</ETag>
		<Size>20</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
</ListVersionsResult>
```

#### 案例二：启用版本控制

#### 请求

```shell
GET /?versions HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 15 Aug 2019 12:03:41 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1565870621;1565877821&q-key-time=1565870621;1565877821&q-header-list=date;host&q-url-param-list=versions&q-signature=36400914186e87b3e88cc8049a79da5e3d79****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 3477
Connection: close
Date: Thu, 15 Aug 2019 12:03:41 GMT
Server: tencent-cos
x-cos-request-id: NWQ1NTRhMWRfODhjMjJhMDlfMWNkOF8xZTRm****

<ListVersionsResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<KeyMarker/>
	<VersionIdMarker/>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>false</IsTruncated>
	<Version>
		<Key>example-object-1.jpg</Key>
		<VersionId>null</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-15T12:03:10.000Z</LastModified>
		<ETag>&quot;0f0cd12c48979d1bf3f95255a36cb861&quot;</ETag>
		<Size>20</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<DeleteMarker>
		<Key>example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzgyMDMwODg0NzI0Njc</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-15T12:03:41.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	<Version>
		<Key>example-object-2.jpg</Key>
		<VersionId>null</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-15T12:03:09.000Z</LastModified>
		<ETag>&quot;51370fc64b79d0d3c7c609635be1c41f&quot;</ETag>
		<Size>20</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<DeleteMarker>
		<Key>example-object-3.jpg</Key>
		<VersionId>MTg0NDUxNzgyMDMwODg0NzA1NzM</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-15T12:03:41.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	<Version>
		<Key>example-object-3.jpg</Key>
		<VersionId>MTg0NDUxNzgyMDMwODk5NTUxNzU</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-15T12:03:39.000Z</LastModified>
		<ETag>&quot;e5c7403f4ac3ace73477eb8b1fd183f7&quot;</ETag>
		<Size>30</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<Version>
		<Key>example-object-3.jpg</Key>
		<VersionId>null</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-15T12:03:08.000Z</LastModified>
		<ETag>&quot;b2f1d893c5fde000ee8ea6eca18ed81f&quot;</ETag>
		<Size>20</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<Version>
		<Key>example-object-4.jpg</Key>
		<VersionId>MTg0NDUxNzgyMDMwODg4OTI0MDc</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-15T12:03:41.000Z</LastModified>
		<ETag>&quot;c5c4d52f90ec328890953bbe4ae08230&quot;</ETag>
		<Size>30</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<Version>
		<Key>example-object-4.jpg</Key>
		<VersionId>MTg0NDUxNzgyMDMwODkyMTg2NjI</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-15T12:03:40.000Z</LastModified>
		<ETag>&quot;e9ec8bcb980d2e4d8526c346eb3b2585&quot;</ETag>
		<Size>20</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<Version>
		<Key>example-object-5.jpg</Key>
		<VersionId>MTg0NDUxNzgyMDMwODk4NTkzMzM</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-15T12:03:39.000Z</LastModified>
		<ETag>&quot;201669a14bdf051d8a9d6f9828d3f4c4&quot;</ETag>
		<Size>20</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
</ListVersionsResult>
```

#### 案例三：带 delimiter 参数（列出根目录下的对象和子目录）

#### 请求

```shell
GET /?versions&delimiter=%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 16 Aug 2019 10:45:53 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1565952353;1565959553&q-key-time=1565952353;1565959553&q-header-list=date;host&q-url-param-list=delimiter;versions&q-signature=c3130139bcac870247d1a070dbc8ee1c7ad5****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 2529
Connection: close
Date: Fri, 16 Aug 2019 10:45:53 GMT
Server: tencent-cos
x-cos-request-id: NWQ1Njg5NjFfNjFiMDJhMDlfMWE5ZV8yMDY4****

<ListVersionsResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<KeyMarker/>
	<VersionIdMarker/>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>false</IsTruncated>
	<Delimiter>/</Delimiter>
	<CommonPrefixes>
		<Prefix>example-folder-1/</Prefix>
	</CommonPrefixes>
	<CommonPrefixes>
		<Prefix>example-folder-2/</Prefix>
	</CommonPrefixes>
	<Version>
		<Key>example-object-1.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNTU3NTk1Mjg</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-16T10:45:53.000Z</LastModified>
		<ETag>&quot;5d1143df07a17b23320d0da161e2819e&quot;</ETag>
		<Size>30</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<DeleteMarker>
		<Key>example-object-1.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNjE1OTcxMzM</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-16T10:45:47.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	<Version>
		<Key>example-object-1.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNjYzNzU0MjE</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-16T10:45:43.000Z</LastModified>
		<ETag>&quot;0f0cd12c48979d1bf3f95255a36cb861&quot;</ETag>
		<Size>20</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<DeleteMarker>
		<Key>example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNTYzMDY3NzY</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-16T10:45:53.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	<Version>
		<Key>example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNjI5OTc5OTU</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-16T10:45:46.000Z</LastModified>
		<ETag>&quot;574c289a7906c7d8fecef028216afeca&quot;</ETag>
		<Size>30</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<Version>
		<Key>example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNjgyODc1OTY</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-16T10:45:41.000Z</LastModified>
		<ETag>&quot;51370fc64b79d0d3c7c609635be1c41f&quot;</ETag>
		<Size>20</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
</ListVersionsResult>
```

#### 案例四：带 prefix 和 delimiter 参数（列出指定子目录下的对象和子目录）

#### 请求

```shell
GET /?versions&prefix=example-folder-1%2F&delimiter=%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 16 Aug 2019 10:45:53 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1565952353;1565959553&q-key-time=1565952353;1565959553&q-header-list=date;host&q-url-param-list=delimiter;prefix;versions&q-signature=6d7b99a4b379b5fefb8b903ee491bae63590****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 2682
Connection: close
Date: Fri, 16 Aug 2019 10:45:53 GMT
Server: tencent-cos
x-cos-request-id: NWQ1Njg5NjFfMzdiMDJhMDlfODA1NV8yMDI2****

<ListVersionsResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix>example-folder-1/</Prefix>
	<KeyMarker/>
	<VersionIdMarker/>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>false</IsTruncated>
	<Delimiter>/</Delimiter>
	<CommonPrefixes>
		<Prefix>example-folder-1/sub-folder-1/</Prefix>
	</CommonPrefixes>
	<CommonPrefixes>
		<Prefix>example-folder-1/sub-folder-2/</Prefix>
	</CommonPrefixes>
	<Version>
		<Key>example-folder-1/example-object-1.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNTY0MzYyNzE</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-16T10:45:53.000Z</LastModified>
		<ETag>&quot;1a54e134fda29e15d225cd226c4b49a3&quot;</ETag>
		<Size>47</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<DeleteMarker>
		<Key>example-folder-1/example-object-1.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNjE2MTE1NTI</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-16T10:45:47.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	<Version>
		<Key>example-folder-1/example-object-1.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNjcwNjI2MTU</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-16T10:45:42.000Z</LastModified>
		<ETag>&quot;f173c1199e3d3b53dd91223cae16fb42&quot;</ETag>
		<Size>37</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<DeleteMarker>
		<Key>example-folder-1/example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNTYyOTQ1MDY</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-16T10:45:53.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	<Version>
		<Key>example-folder-1/example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNjI3NTcyNzU</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-16T10:45:46.000Z</LastModified>
		<ETag>&quot;f43741c189c2142b257767bed5b4ce3a&quot;</ETag>
		<Size>47</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<Version>
		<Key>example-folder-1/example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzgxMjEzNjgwNjgwNDk</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-16T10:45:41.000Z</LastModified>
		<ETag>&quot;c9d28698978bb6fef6c1ed1c439a17d3&quot;</ETag>
		<Size>37</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
</ListVersionsResult>
```

#### 案例五：需分页时获取第一页

#### 请求

```shell
GET /?versions HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 23 Aug 2019 11:31:31 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1566559891;1566567091&q-key-time=1566559891;1566567091&q-header-list=date;host&q-url-param-list=versions&q-signature=2b146233465c2164c60e0e0b2385f5386a61****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 372125
Connection: close
Date: Fri, 23 Aug 2019 11:31:32 GMT
Server: tencent-cos
x-cos-request-id: NWQ1ZmNlOTRfMTljMDJhMDlfNTg5OV8yZWYz****

<ListVersionsResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<KeyMarker/>
	<VersionIdMarker/>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>true</IsTruncated>
	<NextKeyMarker>example-object-0135.jpg</NextKeyMarker>
	<NextVersionIdMarker>MTg0NDUxNzc1MTM4MjM0ODYyNjQ</NextVersionIdMarker>
	<Version>
		<Key>example-object-0001.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4Mjg1NzI5Mjc</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-23T11:31:20.000Z</LastModified>
		<ETag>&quot;3dd9c0ec8b6669abec786e52b64e0497&quot;</ETag>
		<Size>36</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<DeleteMarker>
		<Key>example-object-0002.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjY5NDY2MzQ</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-23T11:31:22.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	<Version>
		<Key>example-object-0002.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjgzMDg3OTE</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:21.000Z</LastModified>
		<ETag>&quot;626f60ee8f3eb987342554379d63259f&quot;</ETag>
		<Size>36</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	...
	<DeleteMarker>
		<Key>example-object-0004.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjcwNjg2Mzc</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:22.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	...
	<DeleteMarker>
		<Key>example-object-0135.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjA2NTk1MTc</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:28.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	...
	<Version>
		<Key>example-object-0135.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjM0ODYyNjQ</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:26.000Z</LastModified>
		<ETag>&quot;56d3a714c81ba76baa6a0004126a2718&quot;</ETag>
		<Size>36</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
</ListVersionsResult>
```

#### 案例六：需分页时获取后续页（使用 key-marker 和 version-id-marker 请求参数）

#### 请求

```shell
GET /?versions&key-marker=example-object-0135.jpg&version-id-marker=MTg0NDUxNzc1MTM4MjM0ODYyNjQ HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 23 Aug 2019 11:32:56 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1566559976;1566567176&q-key-time=1566559976;1566567176&q-header-list=date;host&q-url-param-list=key-marker;version-id-marker;versions&q-signature=5b0787a354752f3161c75d014b75d9f2bd68****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 8358
Connection: close
Date: Fri, 23 Aug 2019 11:32:56 GMT
Server: tencent-cos
x-cos-request-id: NWQ1ZmNlZThfNjFiMDJhMDlfYTgwOF8yZjIw****

<ListVersionsResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<KeyMarker>example-object-0135.jpg</KeyMarker>
	<VersionIdMarker>MTg0NDUxNzc1MTM4MjM0ODYyNjQ</VersionIdMarker>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>false</IsTruncated>
	<Version>
		<Key>example-object-0135.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjQ4MDkyNjk</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:24.000Z</LastModified>
		<ETag>&quot;5dd4f1fb98a2a6d74c8482f2856ece6b&quot;</ETag>
		<Size>36</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<Version>
		<Key>example-object-0135.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjYwOTQ5MTk</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:23.000Z</LastModified>
		<ETag>&quot;91e59eed612971f0e00ac483bf5c7329&quot;</ETag>
		<Size>36</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	...
	<DeleteMarker>
		<Key>example-object-0136.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MTg1MjA4MDA</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-23T11:31:31.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	...
	<DeleteMarker>
		<Key>example-object-0136.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjA2OTA5MDg</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:28.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	...
	<DeleteMarker>
		<Key>example-object-0137.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjA2OTQ0MzA</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:28.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	...
	<Version>
		<Key>example-object-0137.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4Mjc1MjQ3OTY</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:22.000Z</LastModified>
		<ETag>&quot;9022b9bf1b1503902d46cbe976c94eea&quot;</ETag>
		<Size>36</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
</ListVersionsResult>
```

#### 案例七：使用 key-marker 指定起始对象

#### 请求

```shell
GET /?versions&key-marker=example-object-0135.jpg HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 23 Aug 2019 11:32:56 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1566559976;1566567176&q-key-time=1566559976;1566567176&q-header-list=date;host&q-url-param-list=key-marker;versions&q-signature=8b601589aae7ffdb2211694dde4ad73c9634****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 7111
Connection: close
Date: Fri, 23 Aug 2019 11:32:56 GMT
Server: tencent-cos
x-cos-request-id: NWQ1ZmNlZThfNjFiMDJhMDlfYTgwY18yZjRi****

<ListVersionsResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<KeyMarker>example-object-0135.jpg</KeyMarker>
	<VersionIdMarker/>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>false</IsTruncated>
	<DeleteMarker>
		<Key>example-object-0136.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MTg1MjA4MDA</VersionId>
		<IsLatest>true</IsLatest>
		<LastModified>2019-08-23T11:31:31.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	<Version>
		<Key>example-object-0136.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MTg5NjQzNDQ</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:30.000Z</LastModified>
		<ETag>&quot;20f730cd4cab72c0edcbf37c40f9dabe&quot;</ETag>
		<Size>36</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<Version>
		<Key>example-object-0136.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MTk3MDAwMDY</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:29.000Z</LastModified>
		<ETag>&quot;339baa9b8d4450e71fc268aaa5fa250e&quot;</ETag>
		<Size>36</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
	<DeleteMarker>
		<Key>example-object-0136.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjA2OTA5MDg</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:28.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	...
	<DeleteMarker>
		<Key>example-object-0137.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4MjA2OTQ0MzA</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:28.000Z</LastModified>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</DeleteMarker>
	...
	<Version>
		<Key>example-object-0137.jpg</Key>
		<VersionId>MTg0NDUxNzc1MTM4Mjc1MjQ3OTY</VersionId>
		<IsLatest>false</IsLatest>
		<LastModified>2019-08-23T11:31:22.000Z</LastModified>
		<ETag>&quot;9022b9bf1b1503902d46cbe976c94eea&quot;</ETag>
		<Size>36</Size>
		<StorageClass>STANDARD</StorageClass>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
	</Version>
</ListVersionsResult>
```
