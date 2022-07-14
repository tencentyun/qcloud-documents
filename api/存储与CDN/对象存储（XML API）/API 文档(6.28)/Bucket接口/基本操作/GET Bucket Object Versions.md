## 功能描述

GET Bucket Object versions 接口用于拉取存储桶内的所有对象及其历史版本信息，您可以通过指定参数筛选出存储桶内部分对象及其历史版本信息。该 API 的请求者需要对存储桶有读取权限。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=GetBucketObjectVersions&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
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
GET /?versions HTTP/1.1
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
| key-marker | 起始对象键标记，从该标记之后（不含）按照 UTF-8 字典序返回对象版本条目 | string | 否 |
| version-id-marker | 起始版本 ID 标记，从该标记之后（不含）返回对象版本条目，如果上一次 List 结果的 NextVersionIdMarker 为空，则该参数也指定为空 | string | 否 |
| max-keys | 单次返回最大的条目数量，默认值为1000，最大为1000<br>**注意：**该参数会限制每一次 List 操作返回的最大条目数，COS 在每次 List 操作中将返回不超过 max-keys 所设定数值的条目（CommonPrefixes、Version 和 DeleteMarker 合计），如果单次响应中未列出所有对象，COS 会返回 NextKeyMarker 和 NextVersionIdMarker 节点，其值分别为您下次 List 请求的 key-marker 和 version-id-marker 参数，以便您列出后续版本 | integer | 否 |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

查询成功，返回 **application/xml** 数据，包含存储桶中的对象版本信息。不同场景下的响应体请参见下方的实际案例。
```xml
<ListVersionsResult>
		<EncodingType>string</EncodingType>
		<Name>string</Name>
		<Prefix>string</Prefix>
		<KeyMarker>string</KeyMarker>
		<VersionIdMarker>string</VersionIdMarker>
		<MaxKeys>integer</MaxKeys>
		<IsTruncated>boolean</IsTruncated>
		<NextKeyMarker>string</NextKeyMarker>
		<NextVersionIdMarker>string</NextVersionIdMarker>
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
			<StorageTier>Enum</StorageTier>
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
		<Version>
			<Key>string</Key>
			<VersionId>string</VersionId>
			<IsLatest>boolean</IsLatest>
			<LastModified>date</LastModified>
			<ETag>string</ETag>
			<Size>integer</Size>
			<StorageClass>Enum</StorageClass>
			<StorageTier>Enum</StorageTier>
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
</ListVersionsResult>
```


具体的节点描述如下：

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| ListVersionsResult | 无 | 保存 GET Bucket Object versions 结果的所有信息 | Container |

**Container 节点 ListVersionsResult 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| EncodingType | ListVersionsResult | 编码格式，对应请求中的 encoding-type 参数，且仅当请求中指定了 encoding-type 参数才会返回该节点 | string |
| Name | ListVersionsResult | 存储桶的名称，格式为`<BucketName-APPID>`，例如`examplebucket-1250000000` | string |
| Prefix | ListVersionsResult | 对象键匹配前缀，对应请求中的 prefix 参数 | string |
| KeyMarker | ListVersionsResult | 起始对象键标记，从该标记之后（不含）按照 UTF-8 字典序返回对象版本条目，对应请求中的 key-marker 参数 | string |
| VersionIdMarker | ListVersionsResult | 起始版本 ID 标记，从该标记之后（不含）返回对象版本条目，对应请求中的 version-id-marker 参数 | string |
| MaxKeys | ListVersionsResult | 单次响应返回结果的最大条目数量，对应请求中的 max-keys 参数 | integer |
| IsTruncated | ListVersionsResult | 响应条目是否被截断，布尔值，例如 true 或 false | boolean |
| NextKeyMarker | ListVersionsResult | 仅当响应条目有截断（IsTruncated 为 true）才会返回该节点，该节点的值为当前响应条目中的最后一个对象键，当需要继续请求后续条目时，将该节点的值作为下一次请求的 key-marker 参数传入 | string |
| NextVersionIdMarker | ListVersionsResult | 仅当响应条目有截断（IsTruncated 为 true）才会返回该节点，该节点的值为当前响应条目中的最后一个对象的版本 ID，当需要继续请求后续条目时，将该节点的值作为下一次请求的 version-id-marker 参数传入。该节点的值可能为空，此时下一次请求的 version-id-marker 参数也需要指定为空。 | string |
| Delimiter | ListVersionsResult | 分隔符，对应请求中的 delimiter 参数，且仅当请求中指定了 delimiter 参数才会返回该节点 | string |
| CommonPrefixes | ListVersionsResult | 从 prefix 或从头（如未指定 prefix）到首个 delimiter 之间相同的部分，定义为 Common Prefix。仅当请求中指定了 delimiter 参数才有可能返回该节点 | Container |
| Version | ListVersionsResult | 对象版本条目 | Container |
| DeleteMarker | ListVersionsResult | 对象删除标记条目 | Container |

**Container 节点 CommonPrefixes 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Prefix | ListVersionsResult.CommonPrefixes | 单条 Common Prefix 的前缀 | string |

**Container 节点 Version 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Key | ListVersionsResult.Version | 对象键 | string |
| VersionId | ListVersionsResult.Version | 对象的版本 ID<br><li>当未启用版本控制时，该节点的值为空字符串<li>当启用版本控制时，启用版本控制之前的对象，其版本 ID 为 null<li>当暂停版本控制时，新上传的对象其版本 ID 为 null，且同一个对象最多只存在一个版本 ID 为 null 的对象版本 | string |
| IsLatest | ListVersionsResult.Version | 当前版本是否为该对象的最新版本 | boolean |
| LastModified | ListVersionsResult.Version | 当前版本的最后修改时间，为 ISO8601 格式，例如2019-05-24T10:56:40Z | date |
| ETag | ListVersionsResult.Version |  对象的实体标签（Entity Tag），是对象被创建时标识对象内容的信息标签，可用于检查对象的内容是否发生变化<br>例如"8e0b617ca298a564c3331da28dcb50df"。此头部并不一定返回对象的 MD5 值，而是根据对象上传和加密方式而有所不同 | string |
| Size | ListVersionsResult.Version | 对象大小，单位为 Byte | integer |
| StorageClass | ListVersionsResult.Version | 对象存储类型。枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 STANDARD_IA，ARCHIVE | Enum |
| StorageTier | ListVersionsResult.Version | 当对象存储类型为智能分层存储时，指示对象当前所处的存储层，枚举值：FREQUENT（标准层），INFREQUENT（低频层）。仅当 StorageClass 为 INTELLIGENT_TIERING（智能分层）时才会返回该节点 | Enum |
| Owner | ListVersionsResult.Version | 对象持有者信息 | Container |

**Container 节点 Version.Owner 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| ID | ListVersionsResult.Version.Owner | 对象持有者的 APPID | string |
| DisplayName | ListVersionsResult.Version.Owner | 对象持有者的名称 | string |

**Container 节点 DeleteMarker 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Key | ListVersionsResult.DeleteMarker | 对象键 | string |
| VersionId | ListVersionsResult.DeleteMarker | 对象的删除标记的版本 ID | string |
| IsLatest | ListVersionsResult.DeleteMarker | 当前删除标记是否为该对象的最新版本 | boolean |
| LastModified | ListVersionsResult.DeleteMarker | 当前删除标记的删除时间，为 ISO8601 格式，例如2019-05-24T10:56:40Z | date |
| Owner | ListVersionsResult.DeleteMarker | 对象持有者信息 | Container |

**Container 节点 DeleteMarker.Owner 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| ID | ListVersionsResult.DeleteMarker.Owner | 对象持有者的 APPID | string |
| DisplayName | ListVersionsResult.DeleteMarker.Owner | 对象持有者的名称 | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：未启用版本控制

#### 请求

```shell
GET /?versions HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 10 Dec 2020 03:35:34 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607571334;1607578534&q-key-time=1607571334;1607578534&q-header-list=date;host&q-url-param-list=versions&q-signature=1c39a124c84ec844e56cb1031a511568c16f****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 952
Connection: close
Date: Thu, 10 Dec 2020 03:35:34 GMT
Server: tencent-cos
x-cos-request-id: NWZkMTk3ODZfZDUyNzVkNjRfNDgxYl8xNjU5****



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
		        <LastModified>2020-12-10T03:35:24.000Z</LastModified>
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
		        <LastModified>2020-12-10T03:35:24.000Z</LastModified>
		        <ETag>&quot;dcffaafe67632b2bd2dd0b9456eafca7&quot;</ETag>
		        <Size>23</Size>
		        <StorageClass>INTELLIGENT_TIERING</StorageClass>
		        <StorageTier>FREQUENT</StorageTier>
		        <Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
</ListVersionsResult>
```

#### 案例二：启用版本控制（续接案例一，在启用版本控制前上传的对象，其版本 ID 为 null）

#### 请求

```shell
GET /?versions HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 10 Dec 2020 03:36:05 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607571365;1607578565&q-key-time=1607571365;1607578565&q-header-list=date;host&q-url-param-list=versions&q-signature=569318dd515c682db22c704d61314156e790****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 2070
Connection: close
Date: Thu, 10 Dec 2020 03:36:05 GMT
Server: tencent-cos
x-cos-request-id: NWZkMTk3YTVfYjFiODJhMDlfNTg0MDZfMTdj****



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
		        <LastModified>2020-12-10T03:35:24.000Z</LastModified>
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
		        <VersionId>MTg0NDUxMzY1MDIzNjQ3NTcwMDk</VersionId>
		        <IsLatest>true</IsLatest>
		        <LastModified>2020-12-10T03:35:44.000Z</LastModified>
		        <ETag>&quot;51ffadb19b3bf062ecd0c6f044a4d4ce&quot;</ETag>
		        <Size>23</Size>
		        <StorageClass>STANDARD_IA</StorageClass>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
		    <Version>
		        <Key>example-object-2.jpg</Key>
		        <VersionId>null</VersionId>
		        <IsLatest>false</IsLatest>
		        <LastModified>2020-12-10T03:35:24.000Z</LastModified>
		        <ETag>&quot;dcffaafe67632b2bd2dd0b9456eafca7&quot;</ETag>
		        <Size>23</Size>
		        <StorageClass>INTELLIGENT_TIERING</StorageClass>
		        <StorageTier>FREQUENT</StorageTier>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
		    <DeleteMarker>
		        <Key>example-object-3.jpg</Key>
		        <VersionId>MTg0NDUxMzY1MDIzNTQ1ODM2NjE</VersionId>
		        <IsLatest>true</IsLatest>
		        <LastModified>2020-12-10T03:35:54.000Z</LastModified>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </DeleteMarker>
		    <Version>
		        <Key>example-object-3.jpg</Key>
		        <VersionId>MTg0NDUxMzY1MDIzNjQ3NjM2MDY</VersionId>
		        <IsLatest>false</IsLatest>
		        <LastModified>2020-12-10T03:35:44.000Z</LastModified>
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

#### 案例三：暂停版本控制（续接案例二，暂停版本控制后新上传的对象其版本 ID 为 null，且同一个对象最多只存在一个版本 ID 为 null 的对象版本）

#### 请求

```shell
GET /?versions HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 10 Dec 2020 03:36:25 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607571385;1607578585&q-key-time=1607571385;1607578585&q-header-list=date;host&q-url-param-list=versions&q-signature=a42ed543ef094e42c8159d8788c509933f20****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 2396
Connection: close
Date: Thu, 10 Dec 2020 03:36:25 GMT
Server: tencent-cos
x-cos-request-id: NWZkMTk3YjlfNDhhOTBiMDlfMTYzNTZfMTIw****



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
		        <LastModified>2020-12-10T03:35:24.000Z</LastModified>
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
		        <VersionId>null</VersionId>
		        <IsLatest>true</IsLatest>
		        <LastModified>2020-12-10T03:36:15.000Z</LastModified>
		        <ETag>&quot;51ffadb19b3bf062ecd0c6f044a4d4ce&quot;</ETag>
		        <Size>23</Size>
		        <StorageClass>STANDARD</StorageClass>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
		    <Version>
		        <Key>example-object-2.jpg</Key>
		        <VersionId>MTg0NDUxMzY1MDIzNjQ3NTcwMDk</VersionId>
		        <IsLatest>false</IsLatest>
		        <LastModified>2020-12-10T03:35:44.000Z</LastModified>
		        <ETag>&quot;51ffadb19b3bf062ecd0c6f044a4d4ce&quot;</ETag>
		        <Size>23</Size>
		        <StorageClass>STANDARD_IA</StorageClass>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
		    <Version>
		        <Key>example-object-3.jpg</Key>
		        <VersionId>null</VersionId>
		        <IsLatest>true</IsLatest>
		        <LastModified>2020-12-10T03:36:15.000Z</LastModified>
		        <ETag>&quot;b2f1d893c5fde000ee8ea6eca18ed81f&quot;</ETag>
		        <Size>20</Size>
		        <StorageClass>STANDARD</StorageClass>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
		    <DeleteMarker>
		        <Key>example-object-3.jpg</Key>
		        <VersionId>MTg0NDUxMzY1MDIzNTQ1ODM2NjE</VersionId>
		        <IsLatest>false</IsLatest>
		        <LastModified>2020-12-10T03:35:54.000Z</LastModified>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </DeleteMarker>
		    <Version>
		        <Key>example-object-3.jpg</Key>
		        <VersionId>MTg0NDUxMzY1MDIzNjQ3NjM2MDY</VersionId>
		        <IsLatest>false</IsLatest>
		        <LastModified>2020-12-10T03:35:44.000Z</LastModified>
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

#### 案例四：带 encoding-type 参数（对象键使用 URL 编码）

#### 请求

```shell
GET /?versions&encoding-type=url HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 10 Dec 2020 04:54:22 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607576062;1607583262&q-key-time=1607576062;1607583262&q-header-list=date;host&q-url-param-list=encoding-type;versions&q-signature=9dd5519032837d42fd3bf89fcdeed3889e7c****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 2167
Connection: close
Date: Thu, 10 Dec 2020 04:54:22 GMT
Server: tencent-cos
x-cos-request-id: NWZkMWE5ZmVfZTdjODJhMDlfMzgxZl8xMzQ1****



<ListVersionsResult>
		    <EncodingType>url</EncodingType>
		    <Name>examplebucket-1250000000</Name>
		    <Prefix/>
		    <KeyMarker/>
		    <VersionIdMarker/>
		    <MaxKeys>1000</MaxKeys>
		    <IsTruncated>false</IsTruncated>
		    <Version>
		        <Key>Tencent%20Cloud.jpg</Key>
		        <VersionId>MTg0NDUxMzY0OTc2NjcxNzE4NjA</VersionId>
		        <IsLatest>true</IsLatest>
		        <LastModified>2020-12-10T04:54:02.000Z</LastModified>
		        <ETag>&quot;ee8de918d05640145b18f70f4c3aa602&quot;</ETag>
		        <Size>16</Size>
		        <StorageClass>STANDARD</StorageClass>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
		    <DeleteMarker>
		        <Key>%E7%85%A7%E7%89%87/2020%E5%B9%B4/IMG0001.jpg</Key>
		        <VersionId>MTg0NDUxMzY0OTc2NTY5MDU3OTc</VersionId>
		        <IsLatest>true</IsLatest>
		        <LastModified>2020-12-10T04:54:12.000Z</LastModified>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </DeleteMarker>
		    <Version>
		        <Key>%E7%85%A7%E7%89%87/2020%E5%B9%B4/IMG0001.jpg</Key>
		        <VersionId>MTg0NDUxMzY0OTc2NjcwNjMwMDQ</VersionId>
		        <IsLatest>false</IsLatest>
		        <LastModified>2020-12-10T04:54:02.000Z</LastModified>
		        <ETag>&quot;ee8de918d05640145b18f70f4c3aa602&quot;</ETag>
		        <Size>16</Size>
		        <StorageClass>STANDARD</StorageClass>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
		    <Version>
		        <Key>%E8%85%BE%E8%AE%AF%E4%BA%91.jpg</Key>
		        <VersionId>MTg0NDUxMzY0OTc2NTY5MDA4NzU</VersionId>
		        <IsLatest>true</IsLatest>
		        <LastModified>2020-12-10T04:54:12.000Z</LastModified>
		        <ETag>&quot;8bb76a43f75d3b96442c470f8ec23b89&quot;</ETag>
		        <Size>16</Size>
		        <StorageClass>STANDARD</StorageClass>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
		    <Version>
		        <Key>%E8%85%BE%E8%AE%AF%E4%BA%91.jpg</Key>
		        <VersionId>MTg0NDUxMzY0OTc2NjcxNzA2ODg</VersionId>
		        <IsLatest>false</IsLatest>
		        <LastModified>2020-12-10T04:54:02.000Z</LastModified>
		        <ETag>&quot;dcc880c5eba9e002bc4567c733b0e63e&quot;</ETag>
		        <Size>13</Size>
		        <StorageClass>STANDARD</StorageClass>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
</ListVersionsResult>
```

#### 案例五：带 delimiter 参数（列出根目录下的对象版本和子目录）

#### 请求

```shell
GET /?versions&delimiter=%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 10 Dec 2020 07:04:03 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607583843;1607591043&q-key-time=1607583843;1607591043&q-header-list=date;host&q-url-param-list=delimiter;versions&q-signature=9eaea1e6072c7175cb593e08b69223521217****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1893
Connection: close
Date: Thu, 10 Dec 2020 07:04:03 GMT
Server: tencent-cos
x-cos-request-id: NWZkMWM4NjNfNzFjODJhMDlfMjlhZTRfMTg5****



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
		    <DeleteMarker>
		        <Key>example-object-1.jpg</Key>
		        <VersionId>MTg0NDUxMzY0ODk4NzYzNTE4Nzk</VersionId>
		        <IsLatest>true</IsLatest>
		        <LastModified>2020-12-10T07:03:53.000Z</LastModified>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </DeleteMarker>
		    <Version>
		        <Key>example-object-1.jpg</Key>
		        <VersionId>MTg0NDUxMzY0ODk4ODY2NTcxMzY</VersionId>
		        <IsLatest>false</IsLatest>
		        <LastModified>2020-12-10T07:03:42.000Z</LastModified>
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
		        <VersionId>MTg0NDUxMzY0ODk4NzYzODYyODA</VersionId>
		        <IsLatest>true</IsLatest>
		        <LastModified>2020-12-10T07:03:53.000Z</LastModified>
		        <ETag>&quot;51ffadb19b3bf062ecd0c6f044a4d4ce&quot;</ETag>
		        <Size>23</Size>
		        <StorageClass>INTELLIGENT_TIERING</StorageClass>
		        <StorageTier>FREQUENT</StorageTier>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
		    <Version>
		        <Key>example-object-2.jpg</Key>
		        <VersionId>MTg0NDUxMzY0ODk4ODY2NTA0Mjk</VersionId>
		        <IsLatest>false</IsLatest>
		        <LastModified>2020-12-10T07:03:42.000Z</LastModified>
		        <ETag>&quot;dcffaafe67632b2bd2dd0b9456eafca7&quot;</ETag>
		        <Size>23</Size>
		        <StorageClass>STANDARD_IA</StorageClass>
		        <Owner>
		        	<ID>1250000000</ID>
		        	<DisplayName>1250000000</DisplayName>
		        </Owner>
		    </Version>
</ListVersionsResult>
```

#### 案例六：带 prefix 和 delimiter 参数（列出指定子目录下的对象版本和子目录）

#### 请求

```shell
GET /?versions&prefix=example-folder-1%2F&delimiter=%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 10 Dec 2020 07:04:03 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607583843;1607591043&q-key-time=1607583843;1607591043&q-header-list=date;host&q-url-param-list=delimiter;prefix;versions&q-signature=c09ffca0377304f9a12cb2d8e223ede35569****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1960
Connection: close
Date: Thu, 10 Dec 2020 07:04:03 GMT
Server: tencent-cos
x-cos-request-id: NWZkMWM4NjNfZWVjODJhMDlfNTNmN18xNWNj****



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
		    <DeleteMarker>
		    	<Key>example-folder-1/example-object-1.jpg</Key>
		    	<VersionId>MTg0NDUxMzY0ODk4NzYzNjE4NzA</VersionId>
		    	<IsLatest>true</IsLatest>
		    	<LastModified>2020-12-10T07:03:53.000Z</LastModified>
		    	<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
		    	</Owner>
		    </DeleteMarker>
		    <Version>
		    	<Key>example-folder-1/example-object-1.jpg</Key>
		    	<VersionId>MTg0NDUxMzY0ODk4ODY2NTAzOTY</VersionId>
		    	<IsLatest>false</IsLatest>
		    	<LastModified>2020-12-10T07:03:42.000Z</LastModified>
		    	<ETag>&quot;f173c1199e3d3b53dd91223cae16fb42&quot;</ETag>
		    	<Size>37</Size>
		    	<StorageClass>STANDARD</StorageClass>
		    	<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
		    	</Owner>
		    </Version>
		    <Version>
		    	<Key>example-folder-1/example-object-2.jpg</Key>
		    	<VersionId>MTg0NDUxMzY0ODk4NzYzNzc2ODY</VersionId>
		    	<IsLatest>true</IsLatest>
		    	<LastModified>2020-12-10T07:03:53.000Z</LastModified>
		    	<ETag>&quot;f52cc0bc2042d201b852385927bcab95&quot;</ETag>
		    	<Size>40</Size>
		    	<StorageClass>STANDARD</StorageClass>
		    	<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
		    	</Owner>
		    </Version>
		    <Version>
		    	<Key>example-folder-1/example-object-2.jpg</Key>
		    	<VersionId>MTg0NDUxMzY0ODk4ODY2NjQ2NDc</VersionId>
		    	<IsLatest>false</IsLatest>
		    	<LastModified>2020-12-10T07:03:42.000Z</LastModified>
		    	<ETag>&quot;7b3be6c39746a970d628e6ab9f250342&quot;</ETag>
		    	<Size>40</Size>
		    	<StorageClass>STANDARD</StorageClass>
		    	<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
		    	</Owner>
		    </Version>
</ListVersionsResult>
```

#### 案例七：需分页时获取第一页（案例中限制了 max-keys，如不限制则默认为 1000，Version 与 DeleteMarker 合计条目数不超过 max-keys 指定的值）

#### 请求

```shell
GET /?versions&max-keys=3 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 08 Dec 2020 12:46:40 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607431600;1607438800&q-key-time=1607431600;1607438800&q-header-list=date;host&q-url-param-list=max-keys;versions&q-signature=eddd43e98a9001e92f52896de6f8ce88bff5****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1390
Connection: close
Date: Tue, 08 Dec 2020 12:46:40 GMT
Server: tencent-cos
x-cos-request-id: NWZjZjc1YjBfYjBhODBiMDlfZDU5Yl9jYjBl****



<ListVersionsResult>
		    <Name>examplebucket-1250000000</Name>
		    <Prefix/>
		    <KeyMarker/>
		    <VersionIdMarker/>
		    <MaxKeys>3</MaxKeys>
		    <IsTruncated>true</IsTruncated>
		    <NextKeyMarker>example-object-2.jpg</NextKeyMarker>
		    <NextVersionIdMarker>MTg0NDUxMzY2NDIxMjk3MzMwOTM</NextVersionIdMarker>
		    <Version>
		    	<Key>example-object-1.jpg</Key>
		    	<VersionId>MTg0NDUxMzY2NDIxNTAwOTk4NzA</VersionId>
		    	<IsLatest>true</IsLatest>
		    	<LastModified>2020-12-08T12:45:59.000Z</LastModified>
		    	<ETag>&quot;15f0f671f04af108023b5603bea2bfda&quot;</ETag>
		    	<Size>23</Size>
		    	<StorageClass>STANDARD</StorageClass>
		    	<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
		    	</Owner>
		    </Version>
		    <Version>
		    	<Key>example-object-1.jpg</Key>
		    	<VersionId>MTg0NDUxMzY2NDIxNjAyODcyNzk</VersionId>
		    	<IsLatest>false</IsLatest>
		    	<LastModified>2020-12-08T12:45:49.000Z</LastModified>
		    	<ETag>&quot;601389434817e2781d8efb35c0e44717&quot;</ETag>
		    	<Size>23</Size>
		    	<StorageClass>STANDARD</StorageClass>
		    	<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
		    	</Owner>
		    </Version>
		    <DeleteMarker>
		    	<Key>example-object-2.jpg</Key>
		    	<VersionId>MTg0NDUxMzY2NDIxMjk3MzMwOTM</VersionId>
		    	<IsLatest>true</IsLatest>
		    	<LastModified>2020-12-08T12:46:19.000Z</LastModified>
		    	<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
		    	</Owner>
		    </DeleteMarker>
</ListVersionsResult>
```

#### 案例八：需分页时获取后续页（续接案例七，使用 key-marker 和 version-id-marker 请求参数）

#### 请求

```shell
GET /?versions&max-keys=3&key-marker=example-object-2.jpg&version-id-marker=MTg0NDUxMzY2NDIxMjk3MzMwOTM HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 08 Dec 2020 12:46:41 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607431601;1607438801&q-key-time=1607431601;1607438801&q-header-list=date;host&q-url-param-list=key-marker;max-keys;version-id-marker;versions&q-signature=ad52682a1febcc068b6420432017daee8145****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1052
Connection: close
Date: Tue, 08 Dec 2020 12:46:41 GMT
Server: tencent-cos
x-cos-request-id: NWZjZjc1YjFfNjljMDBiMDlfNjQwOV8xYjM2****



<ListVersionsResult>
		    <Name>examplebucket-1250000000</Name>
		    <Prefix/>
		    <KeyMarker>example-object-2.jpg</KeyMarker>
		    <VersionIdMarker>MTg0NDUxMzY2NDIxMjk3MzMwOTM</VersionIdMarker>
		    <MaxKeys>3</MaxKeys>
		    <IsTruncated>false</IsTruncated>
		    <Version>
		    	<Key>example-object-2.jpg</Key>
		    	<VersionId>MTg0NDUxMzY2NDIxMzk5MDk1NzU</VersionId>
		    	<IsLatest>false</IsLatest>
		    	<LastModified>2020-12-08T12:46:09.000Z</LastModified>
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
		    	<VersionId>MTg0NDUxMzY2NDIxMTk1NTEyNDI</VersionId>
		    	<IsLatest>true</IsLatest>
		    	<LastModified>2020-12-08T12:46:30.000Z</LastModified>
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

#### 案例九：使用 key-marker 指定起始对象（续接案例七，但仅使用 key-marker 请求参数而不使用 version-id-marker 请求参数）

#### 请求

```shell
GET /?versions&max-keys=3&key-marker=example-object-2.jpg HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 08 Dec 2020 12:46:41 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607431601;1607438801&q-key-time=1607431601;1607438801&q-header-list=date;host&q-url-param-list=key-marker;max-keys;versions&q-signature=0ed7ce0e8402e35b0ffd2fac429a638a56ea****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 610
Connection: close
Date: Tue, 08 Dec 2020 12:46:42 GMT
Server: tencent-cos
x-cos-request-id: NWZjZjc1YjJfZGZjMTBiMDlfNzAyYl8xMzkx****



<ListVersionsResult>
			<Name>examplebucket-1250000000</Name>
			<Prefix/>
			<KeyMarker>example-object-2.jpg</KeyMarker>
			<VersionIdMarker/>
			<MaxKeys>3</MaxKeys>
			<IsTruncated>false</IsTruncated>
			<Version>
		    	<Key>example-object-3.jpg</Key>
		    	<VersionId>MTg0NDUxMzY2NDIxMTk1NTEyNDI</VersionId>
		    	<IsLatest>true</IsLatest>
		    	<LastModified>2020-12-08T12:46:30.000Z</LastModified>
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

#### 案例十：需分页时获取第一页（带 delimiter 参数，CommonPrefixes、Version 与 DeleteMarker 合计条目数不超过 max-keys 指定的值）

#### 请求

```shell
GET /?versions&delimiter=%2F&max-keys=3 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 09 Dec 2020 13:40:24 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607521224;1607528424&q-key-time=1607521224;1607528424&q-header-list=date;host&q-url-param-list=delimiter;max-keys;versions&q-signature=fdd9031684c544bca32fae81da75b9216079****
Connection: close

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 503
Connection: close
Date: Wed, 09 Dec 2020 13:40:24 GMT
Server: tencent-cos
x-cos-request-id: NWZkMGQzYzhfYmIwMmEwOV83OGU4XzZj****

<ListVersionsResult>
		    <Name>examplebucket-1250000000</Name>
		    <Prefix/>
		    <KeyMarker/>
		    <VersionIdMarker/>
		    <MaxKeys>3</MaxKeys>
		    <IsTruncated>true</IsTruncated>
		    <NextKeyMarker>example-folder-3/</NextKeyMarker>
		    <NextVersionIdMarker/>
		    <Delimiter>/</Delimiter>
		    <CommonPrefixes>
		    	<Prefix>example-folder-1/</Prefix>
		    </CommonPrefixes>
		    <CommonPrefixes>
		    	<Prefix>example-folder-2/</Prefix>
		    </CommonPrefixes>
		    <CommonPrefixes>
		    	<Prefix>example-folder-3/</Prefix>
		    </CommonPrefixes>
</ListVersionsResult>
```

#### 案例十一：需分页时获取后续页（带 delimiter 参数，续接案例十，因为第一页返回的 NextVersionIdMarker 为空，所以本次请求的 version-id-marker 参数也指定为空）

#### 请求

```shell
GET /?versions&delimiter=%2F&max-keys=3&key-marker=example-folder-3%2F&version-id-marker= HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 09 Dec 2020 14:02:32 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1607522552;1607529752&q-key-time=1607522552;1607529752&q-header-list=date;host&q-url-param-list=delimiter;key-marker;max-keys;version-id-marker;versions&q-signature=fd4b2ab426e4531be2e52c02d5bd0e747ee7****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1115
Connection: close
Date: Wed, 09 Dec 2020 14:02:32 GMT
Server: tencent-cos
x-cos-request-id: NWZkMGQ4ZjhfZmVhODBiMDlfMTI3NzVfMTBj****



<ListVersionsResult>
		    <Name>examplebucket-1250000000</Name>
		    <Prefix/>
		    <KeyMarker>example-folder-3/</KeyMarker>
		    <VersionIdMarker/>
		    <MaxKeys>3</MaxKeys>
		    <IsTruncated>true</IsTruncated>
		    <NextKeyMarker>example-object.jpg</NextKeyMarker>
		    <NextVersionIdMarker>MTg0NDUxMzY1NTExNzc4NTYzMTk</NextVersionIdMarker>
		    <Delimiter>/</Delimiter>
		    <CommonPrefixes>
		    	<Prefix>example-folder-4/</Prefix>
		    </CommonPrefixes>
		    <Version>
		    	<Key>example-object.jpg</Key>
		    	<VersionId>MTg0NDUxMzY1NTExNjc2OTk4MjE</VersionId>
		    	<IsLatest>true</IsLatest>
		    	<LastModified>2020-12-09T14:02:21.000Z</LastModified>
		    	<ETag>&quot;3979f6bb23f827d258be64cc0d8df5fb&quot;</ETag>
		    	<Size>21</Size>
		    	<StorageClass>STANDARD</StorageClass>
		    	<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
		    	</Owner>
		    </Version>
		    <DeleteMarker>
		    	<Key>example-object.jpg</Key>
		    	<VersionId>MTg0NDUxMzY1NTExNzc4NTYzMTk</VersionId>
		    	<IsLatest>false</IsLatest>
		    	<LastModified>2020-12-09T14:02:11.000Z</LastModified>
		    	<Owner>
					<ID>1250000000</ID>
					<DisplayName>1250000000</DisplayName>
		    	</Owner>
		    </DeleteMarker>
</ListVersionsResult>
```

