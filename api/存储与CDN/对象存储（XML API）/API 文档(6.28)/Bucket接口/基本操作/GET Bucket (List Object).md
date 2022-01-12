## 功能描述

GET Bucket 请求等同于 List Objects 请求，可以列出该存储桶内的部分或者全部对象。该 API 的请求者需要对存储桶有读取权限。

>? 如果您往存储桶中上传了一个对象，并立即调用 GET Bucket 接口，由于此接口的最终一致性特性，返回的结果中可能不会包含您刚刚上传的对象。
>


<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=GetBucket&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>


## 请求

#### 请求示例

```shell
GET / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

| 名称 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
| prefix | 对象键匹配前缀，限定响应中只包含指定前缀的对象键 | string | 否 |
| delimiter | 一个字符的分隔符，用于对对象键进行分组。所有对象键中从 prefix 或从头（如未指定 prefix）到首个 delimiter 之间相同的部分将作为 CommonPrefixes 下的一个 Prefix 节点。被分组的对象键不再出现在后续对象列表中，具体场景和用法可参考下面的实际案例 | string | 否 |
| encoding-type | 规定返回值的编码方式，可选值：url，代表返回的对象键为 URL 编码（百分号编码）后的值，例如“腾讯云”将被编码为`%E8%85%BE%E8%AE%AF%E4%BA%91` | string | 否 |
| marker | 起始对象键标记，从该标记之后（不含）按照 UTF-8 字典序返回对象键条目 | string | 否 |
| max-keys | 单次返回最大的条目数量，默认值为1000，最大为1000<br>**注意：**该参数会限制每一次 List 操作返回的最大条目数，COS 在每次 List 操作中将返回不超过 max-keys 所设定数值的条目（即 CommonPrefixes 和 Contents 的总和），如果单次响应中未列出所有对象，COS 会返回 NextMarker 节点，其值作为您下次 List 请求的 marker 参数，以便您列出后续对象 | integer | 否 |

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

```xml
<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
			<Name>string</Name>
			<EncodingType>string</EncodingType>
			<Prefix>string</Prefix>
			<Marker>string</Marker>
			<MaxKeys>integer</MaxKeys>
			<Delimiter>string</Delimiter>
			<IsTruncated>boolean</IsTruncated>
			<NextMarker>string</NextMarker>
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
				<StorageTier>Enum</StorageTier>
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
				<StorageTier>Enum</StorageTier>
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
| Name | ListBucketResult | 存储桶的名称，格式为`<BucketName-APPID>`，例如`examplebucket-1250000000` | string |
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
| LastModified | ListBucketResult.Contents | 对象最后修改时间，为 ISO8601 格式，例如2019-05-24T10:56:40Z | date |
| ETag | ListBucketResult.Contents | 对象的实体标签（Entity Tag），是对象被创建时标识对象内容的信息标签，可用于检查对象的内容是否发生变化，<br>例如“8e0b617ca298a564c3331da28dcb50df”，此头部并不一定返回对象的 MD5 值，而是根据对象上传和加密方式而有所不同 | string |
| Size | ListBucketResult.Contents | 对象大小，单位为 Byte | integer |
| Owner | ListBucketResult.Contents | 对象持有者信息 | Container |
| StorageClass | ListBucketResult.Contents | 对象存储类型。枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 STANDARD_IA，ARCHIVE | Enum |
| StorageTier | ListBucketResult.Contents | 当对象存储类型为智能分层存储时，指示对象当前所处的存储层，枚举值：FREQUENT（标准层），INFREQUENT（低频层）。仅当 StorageClass 为 INTELLIGENT_TIERING（智能分层）时才会返回该节点 | Enum |

**Container 节点 Contents.Owner 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| ID | ListBucketResult.Contents.Owner | 对象持有者的 APPID | string |
| DisplayName | ListBucketResult.Contents.Owner | 对象持有者的名称 | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：简单案例

#### 请求

```shell
GET / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 10 Dec 2020 03:37:41 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607571461;1607578661&q-key-time=1607571461;1607578661&q-header-list=date;host&q-url-param-list=&q-signature=918fd2e0149edf8982bebaab2956ec81ede1****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 2931
Connection: close
Date: Thu, 10 Dec 2020 03:37:41 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWZkMTk4MDVfNjViODJhMDlfNDZkYl8xNzU0****
		
<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
      <Name>examplebucket-1250000000</Name>
      <Prefix/>
      <Marker/>
      <MaxKeys>1000</MaxKeys>
      <IsTruncated>false</IsTruncated>
      <Contents>
          <Key>example-folder-1/example-object-1.jpg</Key>
          <LastModified>2020-12-10T03:37:30.000Z</LastModified>
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
          <LastModified>2020-12-10T03:37:30.000Z</LastModified>
          <ETag>&quot;c9d28698978bb6fef6c1ed1c439a17d3&quot;</ETag>
          <Size>37</Size>
          <Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
          </Owner>
				<StorageClass>INTELLIGENT_TIERING</StorageClass>
				<StorageTier>FREQUENT</StorageTier>
      </Contents>
				...
      <Contents>
          <Key>example-object-2.jpg</Key>
          <LastModified>2020-12-10T03:37:30.000Z</LastModified>
          <ETag>&quot;51370fc64b79d0d3c7c609635be1c41f&quot;</ETag>
          <Size>20</Size>
          <Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
          </Owner>
          <StorageClass>STANDARD_IA</StorageClass>
			</Contents>
</ListBucketResult>
```

#### 案例二：带 encoding-type 参数（对象键使用 URL 编码）

#### 请求

```shell
GET /?encoding-type=url HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 08 Dec 2020 13:54:16 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607435656;1607442856&q-key-time=1607435656;1607442856&q-header-list=date;host&q-url-param-list=encoding-type&q-signature=ccbffb70b38430c4b6bc2d1b16ec9c1c8b6f****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1220
Connection: close
Date: Wed, 09 Dec 2020 15:28:29 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWZkMGVkMWRfZjdjNzJhMDlfMjJhYTlfYmJk****
		
<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
      <Name>examplebucket-1250000000</Name>
      <EncodingType>url</EncodingType>
      <Prefix/>
      <Marker/>
      <MaxKeys>1000</MaxKeys>
      <IsTruncated>false</IsTruncated>
      <Contents>
				<Key>Tencent%20Cloud.jpg</Key>
				<LastModified>2020-12-09T15:28:19.000Z</LastModified>
				<ETag>&quot;ee8de918d05640145b18f70f4c3aa602&quot;</ETag>
				<Size>16</Size>
				<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
				</Owner>
				<StorageClass>STANDARD</StorageClass>
      </Contents>
      <Contents>
				<Key>%E7%85%A7%E7%89%87/2020%E5%B9%B4/IMG0001.jpg</Key>
				<LastModified>2020-12-09T15:28:19.000Z</LastModified>
				<ETag>&quot;ee8de918d05640145b18f70f4c3aa602&quot;</ETag>
				<Size>16</Size>
				<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
				</Owner>
				<StorageClass>STANDARD</StorageClass>
      </Contents>
      <Contents>
				<Key>%E8%85%BE%E8%AE%AF%E4%BA%91.jpg</Key>
				<LastModified>2020-12-09T15:28:19.000Z</LastModified>
				<ETag>&quot;ee8de918d05640145b18f70f4c3aa602&quot;</ETag>
				<Size>16</Size>
				<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
				</Owner>
				<StorageClass>STANDARD</StorageClass>
			</Contents>
</ListBucketResult>
```

#### 案例三：带 delimiter 参数（列出根目录下的对象和子目录）

#### 请求

```shell
GET /?delimiter=%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 10 Dec 2020 03:37:41 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607571461;1607578661&q-key-time=1607571461;1607578661&q-header-list=date;host&q-url-param-list=delimiter&q-signature=5984c14f29df90235f4c507e7fbf68ad775e****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1011
Connection: close
Date: Thu, 10 Dec 2020 03:37:41 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWZkMTk4MDVfNjRiMDJhMDlfOTZjZV8xOTgw****
		
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
				<LastModified>2020-12-10T03:37:30.000Z</LastModified>
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
				<LastModified>2020-12-10T03:37:30.000Z</LastModified>
				<ETag>&quot;51370fc64b79d0d3c7c609635be1c41f&quot;</ETag>
				<Size>20</Size>
				<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
				</Owner>
				<StorageClass>STANDARD_IA</StorageClass>
			</Contents>
</ListBucketResult>
```

#### 案例四：带 prefix 和 delimiter 参数（列出指定子目录下的对象和子目录）

#### 请求

```shell
GET /?prefix=example-folder-1%2F&delimiter=%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 10 Dec 2020 03:37:41 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607571461;1607578661&q-key-time=1607571461;1607578661&q-header-list=date;host&q-url-param-list=delimiter;prefix&q-signature=96b4c558ed02a6e6652427fb91b8d22f2107****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1142
Connection: close
Date: Thu, 10 Dec 2020 03:37:41 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWZkMTk4MDVfZGZjNzJhMDlfMzJiMjRfMTY0****
		
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
				<LastModified>2020-12-10T03:37:30.000Z</LastModified>
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
				<LastModified>2020-12-10T03:37:30.000Z</LastModified>
				<ETag>&quot;c9d28698978bb6fef6c1ed1c439a17d3&quot;</ETag>
				<Size>37</Size>
				<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
				</Owner>
				<StorageClass>INTELLIGENT_TIERING</StorageClass>
				<StorageTier>FREQUENT</StorageTier>
			</Contents>
</ListBucketResult>
```

#### 案例五：需分页时获取第一页（案例中限制了 max-keys，如不限制则默认为 1000）

#### 请求

```shell
GET /?max-keys=3 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 08 Dec 2020 12:05:10 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607429110;1607436310&q-key-time=1607429110;1607436310&q-header-list=date;host&q-url-param-list=max-keys&q-signature=a08797232c663110139c878400339bc5b4f4****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1195
Connection: close
Date: Tue, 08 Dec 2020 12:05:10 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWZjZjZiZjZfZGRjODJhMDlfMWFjZDVfMTlmZTY5****
		
<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
			<Name>examplebucket-1250000000</Name>
			<Prefix/>
			<Marker/>
			<MaxKeys>3</MaxKeys>
			<IsTruncated>true</IsTruncated>
			<NextMarker>example-object-3.jpg</NextMarker>
			<Contents>
				<Key>example-object-1.jpg</Key>
				<LastModified>2020-12-08T12:05:00.000Z</LastModified>
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
				<LastModified>2020-12-08T12:05:00.000Z</LastModified>
				<ETag>&quot;51370fc64b79d0d3c7c609635be1c41f&quot;</ETag>
				<Size>20</Size>
				<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
				</Owner>
				<StorageClass>STANDARD</StorageClass>
			</Contents>
			<Contents>
				<Key>example-object-3.jpg</Key>
				<LastModified>2020-12-08T12:05:00.000Z</LastModified>
				<ETag>&quot;b2f1d893c5fde000ee8ea6eca18ed81f&quot;</ETag>
				<Size>20</Size>
				<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
				</Owner>
				<StorageClass>STANDARD</StorageClass>
			</Contents>
</ListBucketResult>
```

#### 案例六：需分页时获取后续页（续接案例五）

#### 请求

```shell
GET /?max-keys=3&marker=example-object-3.jpg HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 08 Dec 2020 12:05:11 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607429111;1607436311&q-key-time=1607429111;1607436311&q-header-list=date;host&q-url-param-list=marker;max-keys&q-signature=b9613747aa1047ec4d72e63123340e88e1c0****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 859
Connection: close
Date: Tue, 08 Dec 2020 12:05:11 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWZjZjZiZjdfMjRhZjJhMDlfMjc2NV8xYmE2****
			
<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
			<Name>examplebucket-1250000000</Name>
			<Prefix/>
			<Marker>example-object-3.jpg</Marker>
			<MaxKeys>3</MaxKeys>
			<IsTruncated>false</IsTruncated>
			<Contents>
				<Key>example-object-4.jpg</Key>
				<LastModified>2020-12-08T12:05:00.000Z</LastModified>
				<ETag>&quot;e9ec8bcb980d2e4d8526c346eb3b2585&quot;</ETag>
				<Size>20</Size>
				<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
				</Owner>
				<StorageClass>STANDARD</StorageClass>
			</Contents>
			<Contents>
				<Key>example-object-5.jpg</Key>
				<LastModified>2020-12-08T12:05:00.000Z</LastModified>
				<ETag>&quot;201669a14bdf051d8a9d6f9828d3f4c4&quot;</ETag>
				<Size>20</Size>
				<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
				</Owner>
				<StorageClass>STANDARD</StorageClass>
			</Contents>
</ListBucketResult>
```

#### 案例七：需分页时获取第一页（带 delimiter 参数，CommonPrefixes 与 Contents 合计条目数不超过 max-keys 指定的值）

#### 请求

```shell
GET /?delimiter=%2F&max-keys=3 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 09 Dec 2020 03:22:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607484158;1607491358&q-key-time=1607484158;1607491358&q-header-list=date;host&q-url-param-list=delimiter;max-keys&q-signature=42f6307ea77293c7a507760430bcad255991****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 486
Connection: close
Date: Wed, 09 Dec 2020 03:22:38 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWZkMDQyZmVfYTJjMjJhMDlfYmQwOF8xYjkw****
		
<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
			<Name>examplebucket-1250000000</Name>
			<Prefix/>
			<Marker/>
			<MaxKeys>3</MaxKeys>
			<Delimiter>/</Delimiter>
			<IsTruncated>true</IsTruncated>
			<NextMarker>example-folder-3/</NextMarker>
			<CommonPrefixes>
				<Prefix>example-folder-1/</Prefix>
			</CommonPrefixes>
			<CommonPrefixes>
				<Prefix>example-folder-2/</Prefix>
			</CommonPrefixes>
			<CommonPrefixes>
				<Prefix>example-folder-3/</Prefix>
			</CommonPrefixes>
</ListBucketResult>
```

#### 案例八：需分页时获取后续页（带 delimiter 参数，续接案例七）

#### 请求

```shell
GET /?delimiter=%2F&max-keys=3&marker=example-folder-3%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 09 Dec 2020 03:22:39 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607484159;1607491359&q-key-time=1607484159;1607491359&q-header-list=date;host&q-url-param-list=delimiter;marker;max-keys&q-signature=921a0e42ac17b3d95c7bf7e68696a489c9e0****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 956
Connection: close
Date: Wed, 09 Dec 2020 03:22:39 GMT
Server: tencent-cos
x-cos-bucket-region: ap-beijing
x-cos-request-id: NWZkMDQyZmZfZmNhODBiMDlfZmM4N19jYmQz****
		
<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
			<Name>examplebucket-1250000000</Name>
			<Prefix/>
			<Marker>example-folder-3/</Marker>
			<MaxKeys>3</MaxKeys>
			<Delimiter>/</Delimiter>
			<IsTruncated>false</IsTruncated>
			<CommonPrefixes>
				<Prefix>example-folder-4/</Prefix>
			</CommonPrefixes>
			<Contents>
				<Key>example-object-1.jpg</Key>
				<LastModified>2020-12-09T03:22:28.000Z</LastModified>
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
				<LastModified>2020-12-09T03:22:28.000Z</LastModified>
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
