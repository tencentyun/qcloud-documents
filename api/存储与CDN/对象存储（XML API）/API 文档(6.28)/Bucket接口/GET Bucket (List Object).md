## 功能描述
GET Bucket 请求等同于 List Object 请求，可以列出该 Bucket 下的部分或者全部 Object。该 API 的操作者需要对 Bucket 有 Read 权限。
>!如果您往存储桶中写入了一个对象，并立即调用`GET Bucket`接口，由于该接口的最终一致性特性，返回的结果中可能不会包含您刚刚写入的对象。

## 请求
### 请求示例

```shell
GET / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
>Authorization: Auth String （详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。
#### 非公共头部
该请求操作无特殊的请求头部信息。

#### 请求参数

名称|类型|描述|必选
---|---|---|---
prefix|string|对象键匹配前缀，限定响应中只包含指定前缀的对象键|否
delimiter|string|一个字符的分隔符，用于对对象键进行分组。所有对象键中从 prefix 或从头（如未指定 prefix）到首个 delimiter 之间相同的部分将作为 CommonPrefixes 下的一个 Prefix 节点。被分组的对象键不再出现在后续对象列表中，具体场景和用法可参考下面的实际案例|否
encoding-type|string|规定返回值的编码方式，可选值：url，代表返回的对象键为 URL 编码（百分号编码）后的值，如“腾讯云”将被编码为“%E8%85%BE%E8%AE%AF%E4%BA%91” |否
marker|string|默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始|否
max-keys|string|单次返回最大的条目数量，默认值为1000，最大为1000 |否

### 请求体
该请求请求体为空。

## 响应
### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
查询成功，返回 application/xml 数据，包含 Bucket 中的对象信息，列出当前目录的响应体示例如下，其他场景下的响应体请参阅下方的实际案例。

```shell
<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>string</Name>
	<Prefix/>
	<Marker/>
	<MaxKeys>string</MaxKeys>
	<IsTruncated>boolean</IsTruncated>
	<Contents>
		<Key>string</Key>
		<LastModified>date</LastModified>
		<ETag>string</ETag>
		<Size>string</Size>
		<Owner>
			<ID>string</ID>
			<DisplayName>string</DisplayName>
		</Owner>
		<StorageClass>string</StorageClass>
	</Contents>
	<Contents>
		<Key>string</Key>
		<LastModified>date</LastModified>
		<ETag>string</ETag>
		<Size>string</Size>
		<Owner>
			<ID>string</ID>
			<DisplayName>string</DisplayName>
		</Owner>
		<StorageClass>string</StorageClass>
	</Contents>
	<Contents>
		<Key>string</Key>
		<LastModified>date</LastModified>
		<ETag>string</ETag>
		<Size>string</Size>
		<Owner>
			<ID>string</ID>
			<DisplayName>string</DisplayName>
		</Owner>
		<StorageClass>string</StorageClass>
	</Contents>
</ListBucketResult>
```

具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型
---|---|---|---
ListBucketResult|无|保存 Get Bucket 请求结果的所有信息|Container

**Container 节点 ListBucketResult 内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
Name|ListBucketResult|说明 Bucket 的信息|string
Encoding-Type|ListBucketResult|编码格式|string
Prefix|ListBucketResult|对象键匹配前缀，对应请求中的 prefix 参数|string
Marker|ListBucketResult|默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始|string
MaxKeys|ListBucketResult|单次响应请求内返回结果的最大的条目数量|string
Delimiter|ListBucketResult|分隔符，对应请求中的 delimiter 参数|string
IsTruncated|ListBucketResult|响应请求条目是否被截断，布尔值：true，false|boolean
NextMarker|ListBucketResult|假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点|string
Contents|ListBucketResult|元数据信息|Container
CommonPrefixes|ListBucketResult|从 prefix 或从头（如未指定 prefix）到首个 delimiter 之间相同的部分，定义为 Common Prefix。只有指定了 delimiter 参数的情况下才有可能包含该元素|Container


**Container 节点 Contents 内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|--
Key|ListBucketResult.Contents|Object 的 Key|string
LastModified|ListBucketResult.Contents|说明 Object 最后被修改时间|date
ETag|ListBucketResult.Contents|文件的 MD5 算法校验值|string
Size|ListBucketResult.Contents|说明文件大小，单位是 Byte|string
Owner|ListBucketResult.Contents|Bucket 持有者信息|Container
StorageClass|ListBucketResult.Contents|Object 的存储类型，枚举值：STANDARD，STANDARD_IA，ARCHIVE。详情请参阅 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档 |string

**Container 节点 Owner 内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
ID|ListBucketResult.Contents.Owner|Bucket 的 APPID|string
DisplayName|ListBucketResult.Contents.Owner|Object 持有者的名称|string

**Container 节点 CommonPrefixes 内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
Prefix|ListBucketResult.CommonPrefixes|单条 Common Prefix 的前缀|string


### 错误码
该请求操作无特殊错误信息，常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 简单案例

#### 请求

```shell
GET / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Date: Mon, 13 May 2019 10:54:15 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1557744728;1557751928&q-key-time=1557744728;1557751928&q-header-list=host&q-url-param-list=&q-signature=71423fa0e79849a41fa3e5d5457cb16ccabb****
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1523
Connection: close
Date: Mon, 13 May 2019 10:54:16 GMT
Server: tencent-cos
x-cos-request-id: NWNkOTRjZDhfMjM5ZDA4MDlfNjM0ZV8yNjk4****

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>false</IsTruncated>
	<Contents>
		<Key>example-folder/example-object-10.jpg</Key>
		<LastModified>2019-05-13T09:40:02.000Z</LastModified>
		<ETag>&quot;a4a5289b0a2f28cfa6d1d25cca009588&quot;</ETag>
		<Size>1436971</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-folder/example-object-11.jpg</Key>
		<LastModified>2019-05-13T09:40:02.000Z</LastModified>
		<ETag>&quot;22e1096342afde1ed56f3fc3c05d39c4&quot;</ETag>
		<Size>1271110</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-1.jpg</Key>
		<LastModified>2019-05-13T09:18:27.000Z</LastModified>
		<ETag>&quot;51a544ea086e80e2f2a1b94b1f43d734&quot;</ETag>
		<Size>1790395</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-2.jpg</Key>
		<LastModified>2019-05-13T09:18:27.000Z</LastModified>
		<ETag>&quot;adc909f1683bbed9cda7e031849eed84&quot;</ETag>
		<Size>2188728</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
</ListBucketResult>
```

### 带 delimiter 参数（列出根目录下的对象和子目录）

#### 请求

```shell
GET /?delimiter=%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Date: Mon, 13 May 2019 11:04:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1557745440;1557752640&q-key-time=1557745440;1557752640&q-header-list=host&q-url-param-list=delimiter&q-signature=eb7fa1b31c81026afd59c27c9627e9213558****
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1017
Connection: close
Date: Mon, 13 May 2019 11:04:01 GMT
Server: tencent-cos
x-cos-request-id: NWNkOTRmMjFfNWVhYjFjMDlfMTIzNTdfMjYx****

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<Delimiter>/</Delimiter>
	<IsTruncated>false</IsTruncated>
	<CommonPrefixes>
		<Prefix>example-folder-2/</Prefix>
	</CommonPrefixes>
	<CommonPrefixes>
		<Prefix>example-folder/</Prefix>
	</CommonPrefixes>
	<Contents>
		<Key>example-object-1.jpg</Key>
		<LastModified>2019-05-13T09:18:27.000Z</LastModified>
		<ETag>&quot;51a544ea086e80e2f2a1b94b1f43d734&quot;</ETag>
		<Size>1790395</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-2.jpg</Key>
		<LastModified>2019-05-13T09:18:27.000Z</LastModified>
		<ETag>&quot;adc909f1683bbed9cda7e031849eed84&quot;</ETag>
		<Size>2188728</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
</ListBucketResult>
```

### 带 prefix 和 delimiter 参数（列出指定子目录下的对象和子目录）

#### 请求

```shell
GET /?prefix=example-folder%2F&delimiter=%2F HTTP/1.1
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Date: Mon, 13 May 2019 11:08:05 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1557745685;1557752885&q-key-time=1557745685;1557752885&q-header-list=host&q-url-param-list=delimiter;prefix&q-signature=84fafc3585013f53829584887390f9c116ae****
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1110
Connection: close
Date: Mon, 13 May 2019 11:08:06 GMT
Server: tencent-cos
x-cos-request-id: NWNkOTUwMTZfZGQxZDFkMDlfNDMxMF8yNWY3****

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix>example-folder/</Prefix>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<Delimiter>/</Delimiter>
	<IsTruncated>false</IsTruncated>
	<CommonPrefixes>
		<Prefix>example-folder/example-sub-folder-2/</Prefix>
	</CommonPrefixes>
	<CommonPrefixes>
		<Prefix>example-folder/example-sub-folder/</Prefix>
	</CommonPrefixes>
	<Contents>
		<Key>example-folder/example-object-10.jpg</Key>
		<LastModified>2019-05-13T09:40:02.000Z</LastModified>
		<ETag>&quot;a4a5289b0a2f28cfa6d1d25cca009588&quot;</ETag>
		<Size>1436971</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-folder/example-object-11.jpg</Key>
		<LastModified>2019-05-13T09:40:02.000Z</LastModified>
		<ETag>&quot;22e1096342afde1ed56f3fc3c05d39c4&quot;</ETag>
		<Size>1271110</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
</ListBucketResult>
```

### 需分页时获取第一页

#### 请求

```shell
GET / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Date: Mon, 13 May 2019 11:24:34 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1557746674;1557753874&q-key-time=1557746674;1557753874&q-header-list=host&q-url-param-list=&q-signature=fc9879b271f1021a1a6c53653642a4bc9cc7****
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 879028
Connection: close
Date: Mon, 13 May 2019 11:24:35 GMT
Server: tencent-cos
x-cos-request-id: NWNkOTUzZjNfN2M0NzIyMDlfODMzZF8yNWM1****

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
		<LastModified>2019-05-13T09:18:27.000Z</LastModified>
		<ETag>&quot;51a544ea086e80e2f2a1b94b1f43d734&quot;</ETag>
		<Size>1790395</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-0002.jpg</Key>
		<LastModified>2019-05-13T09:18:27.000Z</LastModified>
		<ETag>&quot;adc909f1683bbed9cda7e031849eed84&quot;</ETag>
		<Size>2188728</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	......
	<Contents>
		<Key>example-object-1000.jpg</Key>
		<LastModified>2019-05-13T09:18:28.000Z</LastModified>
		<ETag>&quot;36b0a0746c38b4090425efc6ff307abf&quot;</ETag>
		<Size>2188728</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
</ListBucketResult>
```

### 需分页时获取后续页

#### 请求

```shell
GET /?marker=example-object-1000.jpg HTTP/1.1
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Date: Mon, 13 May 2019 11:33:56 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1557747236;1557754436&q-key-time=1557747236;1557754436&q-header-list=host&q-url-param-list=marker&q-signature=2c1069a0c438dc091729bfe0b65f0db21a10****
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1208
Connection: close
Date: Mon, 13 May 2019 11:33:58 GMT
Server: tencent-cos
x-cos-request-id: NWNkOTU2MjZfNTkyZjIyMDlfM2YzMF8yOTU4****

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>examplebucket-1250000000</Name>
	<Prefix/>
	<Marker>example-object-1000.jpg</Marker>
	<MaxKeys>1000</MaxKeys>
	<IsTruncated>false</IsTruncated>
	<Contents>
		<Key>example-object-1001.jpg</Key>
		<LastModified>2019-05-13T09:18:27.000Z</LastModified>
		<ETag>&quot;51a544ea086e80e2f2a1b94b1f43d734&quot;</ETag>
		<Size>1790395</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-1002.jpg</Key>
		<LastModified>2019-05-13T09:18:27.000Z</LastModified>
		<ETag>&quot;adc909f1683bbed9cda7e031849eed84&quot;</ETag>
		<Size>2188728</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
	<Contents>
		<Key>example-object-1003.jpg</Key>
		<LastModified>2019-05-13T09:18:28.000Z</LastModified>
		<ETag>&quot;36b0a0746c38b4090425efc6ff307abf&quot;</ETag>
		<Size>2188728</Size>
		<Owner>
			<ID>1250000000</ID>
			<DisplayName>1250000000</DisplayName>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
	</Contents>
</ListBucketResult>
```

