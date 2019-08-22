## 功能描述

GET Bucket 请求等同于 List Object 请求，可以列出该存储桶内的部分或者全部对象。该 API 的请求者需要对存储桶有读取权限。

>? 如果您往存储桶中上传了一个对象，并立即调用 GET Bucket 接口，由于此接口的最终一致性特性，返回的结果中可能不会包含您刚刚上传的对象。

## 请求

#### 请求示例

```shell
GET / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

| 名称 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
| prefix | 对象键匹配前缀，限定响应中只包含指定前缀的对象键 | string | 否 |
| delimiter | 一个字符的分隔符，用于对对象键进行分组。所有对象键中从 prefix 或从头（如未指定 prefix）到首个 delimiter 之间相同的部分将作为 CommonPrefixes 下的一个 Prefix 节点。被分组的对象键不再出现在后续对象列表中，具体场景和用法可参考下面的实际案例 | string | 否 |
| encoding-type | 规定返回值的编码方式，可选值：url，代表返回的对象键为 URL 编码（百分号编码）后的值，如“腾讯云”将被编码为`%E8%85%BE%E8%AE%AF%E4%BA%91` | string | 否 |
| marker | 起始对象键标记，从该标记之后（不含）按照 UTF-8 字典序返回对象键条目 | string | 否 |
| max-keys | 单次返回最大的条目数量，默认值为1000，最大为1000 | integer | 否 |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

| 名称 | 描述 | 类型 |
| --- | --- | --- |
| x-cos-bucket-region | 存储桶所在地域。枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 文档，例如 ap-beijing，ap-hongkong，eu-frankfurt 等 | Enum |

#### 响应体

查询成功，返回 **application/xml** 数据，包含存储桶中的对象信息。不同场景下的响应体请参见下方的实际案例。

```shell
<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>string</Name>
	<Prefix>string</Prefix>
	<Marker/>
	<MaxKeys>integer</MaxKeys>
	<Delimiter>string</Delimiter>
	<IsTruncated>boolean</IsTruncated>
	<CommonPrefixes>
		<Prefix>string</Prefix>
	</CommonPrefixes>
	<CommonPrefixes>
		<Prefix>string</Prefix>
	</CommonPrefixes>
	<Contents>
		<Key>string</Key>
		<LastModified>date</LastModified>
		<ETag>string</ETag>
		<Size>integer</Size>
		<Owner>
			<ID>string</ID>
			<DisplayName>string</DisplayName>
		</Owner>
		<StorageClass>Enum</StorageClass>
	</Contents>
	<Contents>
		<Key>string</Key>
		<LastModified>date</LastModified>
		<ETag>string</ETag>
		<Size>integer</Size>
		<Owner>
			<ID>string</ID>
			<DisplayName>string</DisplayName>
		</Owner>
		<StorageClass>Enum</StorageClass>
	</Contents>
</ListBucketResult>
```

具体的节点描述如下：

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| ListBucketResult | 无 | 保存 GET Bucket 结果的所有信息 | Container |

**Container 节点 ListBucketResult 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Name | ListBucketResult | 存储桶的名称，格式为`<BucketName-APPID>`，例如 `examplebucket-1250000000` | string |
| EncodingType | ListBucketResult | 编码格式，对应请求中的 encoding-type 参数，且仅当请求中指定了 encoding-type 参数才会返回该节点 | string |
| Prefix | ListBucketResult | 对象键匹配前缀，对应请求中的 prefix 参数 | string |
| Marker | ListBucketResult | 起始对象键标记，从该标记之后（不含）按照 UTF-8 字典序返回对象键条目，对应请求中的 marker 参数 | string |
| MaxKeys | ListBucketResult | 单次响应返回结果的最大条目数量，对应请求中的 max-keys 参数 | integer |
| Delimiter | ListBucketResult | 分隔符，对应请求中的 delimiter 参数，且仅当请求中指定了 delimiter 参数才会返回该节点 | string |
| IsTruncated | ListBucketResult | 响应条目是否被截断，布尔值，例如 true 或 false | boolean |
| NextMarker | ListBucketResult | 仅当响应条目有截断（IsTruncated 为 true）才会返回该节点，该节点的值为当前响应条目中的最后一个对象键，当需要继续请求后续条目时，将该节点的值作为下一次请求的 marker 参数传入 | string |
| CommonPrefixes | ListBucketResult | 从 prefix 或从头（如未指定 prefix）到首个 delimiter 之间相同的部分，定义为 Common Prefix。仅当请求中指定了 delimiter 参数才有可能返回该节点 | Container |
| Contents | ListBucketResult | 对象条目 | Container |

**Container 节点 CommonPrefixes 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Prefix | ListBucketResult.CommonPrefixes | 单条 Common Prefix 的前缀 | string |

**Container 节点 Contents 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Key | ListBucketResult.Contents | 对象键 | string |
| LastModified | ListBucketResult.Contents | 对象最后修改时间，为 ISO8601 格式，如2019-05-24T10:56:40Z | date |
| ETag | ListBucketResult.Contents | 根据文件内容计算出的哈希值 | string |
| Size | ListBucketResult.Contents | 对象大小，单位为 Byte | integer |
| Owner | ListBucketResult.Contents | 对象持有者信息 | Container |
| StorageClass | ListBucketResult.Contents | 对象存储类型。枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 STANDARD_IA，ARCHIVE | Enum |

**Container 节点 Contents.Owner 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| ID | ListBucketResult.Contents.Owner | 存储桶的 APPID | string |
| DisplayName | ListBucketResult.Contents.Owner | 对象持有者的名称 | string |

#### 错误码

此接口无特殊错误信息，全部错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：简单案例

#### 请求

```shell
GET / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 27 May 2019 11:26:14 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558956374;1558963574&q-key-time=1558956374;1558963574&q-header-list=date;host&q-url-param-list=&q-signature=9a2596f2a4dc0cf5eaa9019959a8275afd4b****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1517
Connection: close
Date: Mon, 27 May 2019 11:26:15 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWNlYmM5NTdfZjI4NWQ2NF81ZmMwX2Q5N2E1****

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>false</IsTruncated>
	<Contents>
		<Key>example-folder-1/example-object-1.jpg</Key>
		<LastModified>2019-05-27T11:26:14.000Z</LastModified>
		<ETag>&quot;f173c1199e3d3b53dd91223cae16fb42&quot;</ETag>
		<Size>37</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-folder-1/sub-folder-1/example-object-1.jpg</Key>
		<LastModified>2019-05-27T11:26:14.000Z</LastModified>
		<ETag>&quot;bef7bb344812457ffc72f7bf99dabfdd&quot;</ETag>
		<Size>50</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-1.jpg</Key>
		<LastModified>2019-05-27T11:26:14.000Z</LastModified>
		<ETag>&quot;0f0cd12c48979d1bf3f95255a36cb861&quot;</ETag>
		<Size>20</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-2.jpg</Key>
		<LastModified>2019-05-27T11:26:14.000Z</LastModified>
		<ETag>&quot;51370fc64b79d0d3c7c609635be1c41f&quot;</ETag>
		<Size>20</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
</ListBucketResult>
```

#### 案例二：带 delimiter 参数（列出根目录下的对象和子目录）

#### 请求

```shell
GET /?delimiter=%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 27 May 2019 11:26:15 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558956375;1558963575&q-key-time=1558956375;1558963575&q-header-list=date;host&q-url-param-list=delimiter&q-signature=d409a7025e1633c162213ab34fbf7e87ef50****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1008
Connection: close
Date: Mon, 27 May 2019 11:26:15 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWNlYmM5NTdfNzViMDJhMDlfNDkzNF9kMTQ3****

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<Delimiter>/</Delimiter>
	<IsTruncated>false</IsTruncated>
	<CommonPrefixes>
		<Prefix>example-folder-1/</Prefix>
	</CommonPrefixes>
	<CommonPrefixes>
		<Prefix>example-folder-2/</Prefix>
	</CommonPrefixes>
	<Contents>
		<Key>example-object-1.jpg</Key>
		<LastModified>2019-05-27T11:26:14.000Z</LastModified>
		<ETag>&quot;0f0cd12c48979d1bf3f95255a36cb861&quot;</ETag>
		<Size>20</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-2.jpg</Key>
		<LastModified>2019-05-27T11:26:14.000Z</LastModified>
		<ETag>&quot;51370fc64b79d0d3c7c609635be1c41f&quot;</ETag>
		<Size>20</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
</ListBucketResult>
```

#### 案例三：带 prefix 和 delimiter 参数（列出指定子目录下的对象和子目录）

#### 请求

```shell
GET /?prefix=example-folder-1%2F&delimiter=%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 27 May 2019 11:26:15 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558956375;1558963575&q-key-time=1558956375;1558963575&q-header-list=date;host&q-url-param-list=delimiter;prefix&q-signature=f4a0854aa3a3b9b1699e1989d675297867f3****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1093
Connection: close
Date: Mon, 27 May 2019 11:26:15 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWNlYmM5NTdfNDQyODVkNjRfNTIwYl82ZGQy****

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix>example-folder-1/</Prefix>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<Delimiter>/</Delimiter>
	<IsTruncated>false</IsTruncated>
	<CommonPrefixes>
		<Prefix>example-folder-1/sub-folder-1/</Prefix>
	</CommonPrefixes>
	<CommonPrefixes>
		<Prefix>example-folder-1/sub-folder-2/</Prefix>
	</CommonPrefixes>
	<Contents>
		<Key>example-folder-1/example-object-1.jpg</Key>
		<LastModified>2019-05-27T11:26:14.000Z</LastModified>
		<ETag>&quot;f173c1199e3d3b53dd91223cae16fb42&quot;</ETag>
		<Size>37</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-folder-1/example-object-2.jpg</Key>
		<LastModified>2019-05-27T11:26:15.000Z</LastModified>
		<ETag>&quot;c9d28698978bb6fef6c1ed1c439a17d3&quot;</ETag>
		<Size>37</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
</ListBucketResult>
```

#### 案例四：需分页时获取第一页

#### 请求

```shell
GET / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 27 May 2019 11:07:30 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558955250;1558962450&q-key-time=1558955250;1558962450&q-header-list=date;host&q-url-param-list=&q-signature=4d515ac9853b6e341cf5432c0d57faebe165****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 321247
Connection: close
Date: Mon, 27 May 2019 11:07:30 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWNlYmM0ZjJfZDcyNzVkNjRfNjQ5OV9lNzdk****

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>true</IsTruncated>
	<NextMarker>example-object-1000.jpg</NextMarker>
	<Contents>
		<Key>example-object-0001.jpg</Key>
		<LastModified>2019-05-27T11:07:29.000Z</LastModified>
		<ETag>&quot;f49ffbb2dd542ef6843135d66ec97855&quot;</ETag>
		<Size>23</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-0002.jpg</Key>
		<LastModified>2019-05-27T11:07:29.000Z</LastModified>
		<ETag>&quot;ab1694353a29f925ca67d2956ca14b37&quot;</ETag>
		<Size>23</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	...
	<Contents>
		<Key>example-object-1000.jpg</Key>
		<LastModified>2019-05-27T11:07:29.000Z</LastModified>
		<ETag>&quot;b76c104f431e06bbfbbe7a97c87aecde&quot;</ETag>
		<Size>23</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
</ListBucketResult>
```

#### 案例五：需分页时获取后续页

#### 请求

```shell
GET /?marker=example-object-1000.jpg HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 27 May 2019 11:08:36 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558955316;1558962516&q-key-time=1558955316;1558962516&q-header-list=date;host&q-url-param-list=marker&q-signature=f9ed03c3944926d06281c607d3314678909e****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1834
Connection: close
Date: Mon, 27 May 2019 11:08:36 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWNlYmM1MzRfZmVhODBiMDlfMmViNjRfZDQw****

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<Marker>example-object-1000.jpg</Marker>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>false</IsTruncated>
	<Contents>
		<Key>example-object-1001.jpg</Key>
		<LastModified>2019-05-27T11:07:29.000Z</LastModified>
		<ETag>&quot;8256f8fc3eb5b11452aa4915a011aa81&quot;</ETag>
		<Size>23</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-1002.jpg</Key>
		<LastModified>2019-05-27T11:07:29.000Z</LastModified>
		<ETag>&quot;c7ac76bed75b99a3a7169eb3db00389d&quot;</ETag>
		<Size>23</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	...
	<Contents>
		<Key>example-object-1005.jpg</Key>
		<LastModified>2019-05-27T11:07:29.000Z</LastModified>
		<ETag>&quot;47176b4ca0078855bfd47e30a9c70a61&quot;</ETag>
		<Size>23</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
</ListBucketResult>
```
