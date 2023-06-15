## 功能描述

GET Service 接口是用来查询请求者名下的所有存储桶列表或特定地域下的存储桶列表。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=GetService&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
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

**示例一**

```plaintext
GET / HTTP/1.1
Host: service.cos.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

**示例二**

```plaintext
GET / HTTP/1.1
Host: cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> ?
> - Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - Host: 查询全部存储桶列表指定为 `service.cos.myqcloud.com`，查询特定地域下的存储桶列表指定为 cos.&lt;Region>.myqcloud.com，其中 &lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。

#### 请求参数

GetService 支持通过请求参数根据存储桶标签、地域、创建时间过滤存储桶。其中，根据存储桶标签过滤存储桶，仅支持传入一个存储桶标签。当存储桶包含多个存储桶标签时，只要其中任意一个为用户指定的存储桶标签，就会返回该存储桶。

| 名称 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- |
|tagkey | 支持根据存储桶标签过滤存储桶，仅支持传入一个存储桶标签，tagkey 用于传入标签键 | string | 否 |
|tagvalue | 支持根据存储桶标签过滤存储桶，仅支持传入一个存储桶标签，tagvalue 用于传入标签值 | string | 否 |
|region | 支持根据地域过滤存储桶，例如 `region=ap-beijing`，COS 支持的地域可参考 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)| string | 否 |
|create-time | GMT 时间戳，和 range 参数一起使用，支持根据创建时间过滤存储桶，例如 `create-time=1642662645` |Timestamp | 否 |
|range | 和 create-time 参数一起使用，支持根据创建时间过滤存储桶，支持枚举值 lt（创建时间早于 create-time）、gt（创建时间晚于 create-time）、lte（创建时间早于或等于 create-time）、gte（创建时间晚于或等于create-time） | string | 否 |
|marker | 起始标记，从该标记之后（不含）按照 UTF-8 字典序返回存储桶条目 | string | 否 |
|max-keys |单次返回最大的条目数量，默认值为2000，最大为2000。如果单次响应中未列出所有存储桶，COS 会返回 NextMarker 节点，其值作为下次 GetService 请求的 marker 参数  | integer | 否 |


当存储桶标签授权情况与 GetService 授权不同时，GetService 请求的鉴权和返回情况如下。关于标签鉴权的授权方法 ，可参见 [授权子账号按照存储桶标签拉取存储桶列表](https://cloud.tencent.com/document/product/436/34694)。

<table>
    <tr>
        <th>存储桶标签授权情况</th>
        <th>GetService 授权情况</th>
        <th>GetService 请求</th>
        <th>请求返回</th>
    </tr>
    <tr>
        <td rowspan="4">主账号通过存储桶标签授权，授权了子账号存储桶标签 tagA 的资源操作权限。</td>
        <td rowspan="2">没有授权 GetService 权限</td>
        <td>携带存储桶标签参数 tagA</td>
        <td>包含存储桶标签 tagA 的存储桶列表</td>
    </tr>
    <tr>
        <td>不携带存储桶标签参数</td>
        <td>Access Denied</td>
    </tr>
    <tr>
        <td rowspan="2">额外授权 GetService 权限</td>
        <td>携带存储桶标签参数 tagA</td>
        <td>包含存储桶标签 tagA 的存储桶列表</td>
    </tr>
    <tr>
        <td>不携带存储桶标签参数</td>
        <td>所有存储桶列表</td>
    </tr>
    <tr>
        <td rowspan="4">主账号没有通过存储桶标签授权，没有授权子账号存储桶标签 tagA 的资源操作权限。</td>
        <td rowspan="2">没有授权 GetService 权限</td>
        <td>携带存储桶标签参数 tagA</td>
        <td>Access Denied</td>
    </tr>
    <tr>
        <td>不携带存储桶标签参数</td>
        <td>Access Denied</td>
    </tr>
    <tr>
        <td rowspan="2">额外授权 GetService 权限</td>
        <td>携带存储桶标签参数 tagA</td>
        <td>包含存储桶标签 tagA 的存储桶列表</td>
    </tr>
    <tr>
        <td>不携带存储桶标签参数</td>
        <td>所有存储桶列表</td>
    </tr>
</table>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

查询成功，返回 **application/xml** 数据，包含所有或特定地域下的存储桶列表。

```plaintext
<ListAllMyBucketsResult>
    <Owner>
        <ID>string</ID>
        <DisplayName>string</DisplayName>
    </Owner>
    <Marker></Marker>
    <NextMarker></NextMarker>
    <IsTruncated></IsTruncated>
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
|Marker |ListAllMyBucketsResult |表示本次 GetService（ListBuckets）的起点    |string |
|IsTruncated|ListAllMyBucketsResult | 是否所有的结果都已经返回。true：表示本次没有返回全部结果。false：表示本次已经返回了全部结果   |string |
|NextMarker|ListAllMyBucketsResult |未返回所有结果时，作为下次 GetService 请求的 marker 参数  |string |

**Container 节点 Owner 的内容：**

| 节点名称（关键字） | 父节点                       | 描述                                                         | 类型   |
| ------------------ | ---------------------------- | ------------------------------------------------------------ | ------ |
| ID                 | ListAllMyBucketsResult.Owner | 存储桶持有者的完整 ID，格式为 `qcs::cam::uin/[OwnerUin]:uin/[OwnerUin]`<br>例如`qcs::cam::uin/100000000001:uin/100000000001` | string |
| DisplayName        | ListAllMyBucketsResult.Owner | 存储桶持有者的名字                                           | string |

**Container 节点 Buckets 的内容：**

| 节点名称（关键字） | 父节点                         | 描述       | 类型      |
| ------------------ | ------------------------------ | ---------- | --------- |
| Bucket             | ListAllMyBucketsResult.Buckets | 存储桶信息 | Container |

**Container 节点 Buckets.Bucket 的内容：**

| 节点名称（关键字） | 父节点                                | 描述                                                         | 类型   |
| ------------------ | ------------------------------------- | ------------------------------------------------------------ | ------ |
| Name               | ListAllMyBucketsResult.Buckets.Bucket | 存储桶的名称，格式为 `<BucketName-APPID>`<br>例如 `examplebucket-1250000000` | string |
| Location           | ListAllMyBucketsResult.Buckets.Bucket | 存储桶所在地域，枚举值请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) 文档<br>例如 ap-beijing，ap-hongkong，eu-frankfurt 等 | Enum   |
| CreationDate       | ListAllMyBucketsResult.Buckets.Bucket | 存储桶的创建时间，为 ISO8601 格式，例如 2019-05-24T10:56:40Z    | date   |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：查询所有存储桶列表

#### 请求

```plaintext
GET / HTTP/1.1
Host: service.cos.myqcloud.com
Date: Fri, 24 May 2019 11:59:50 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558699190;1558706390&q-key-time=1558699190;1558706390&q-header-list=date;host&q-url-param-list=&q-signature=89fa1f6a56c34e460f3db4d65f928eaf034a****
Connection: close
```

#### 响应

```plaintext
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
	</Marker>
	</NextMarker>
	<IsTruncated>false</IsTruncated>
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

#### 案例二：查询特定地域下的存储桶列表（通过域名筛选）

#### 请求

```plaintext
GET / HTTP/1.1
Host: cos.ap-beijing.myqcloud.com
Date: Fri, 24 May 2019 11:59:51 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558699191;1558706391&q-key-time=1558699191;1558706391&q-header-list=date;host&q-url-param-list=&q-signature=c3f55f4ce2800fb343cf85ff536a9185a0c1****
Connection: close
```

#### 响应

```plaintext
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
	</Marker>
	</NextMarker>
	<IsTruncated>false</IsTruncated>
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


#### 案例三：查询特定地域下的存储桶列表（根据请求参数筛选）


#### 请求

```plaintext
GET /?region=ap-beijing HTTP/1.1
Host: service.cos.myqcloud.com
Date: Fri, 24 May 2019 11:59:51 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558699191;1558706391&q-key-time=1558699191;1558706391&q-header-list=date;host&q-url-param-list=&q-signature=c3f55f4ce2800fb343cf85ff536a9185a0c1****
Connection: close
```


#### 响应


```plaintext
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
	</Marker>
	</NextMarker>
	<IsTruncated>false</IsTruncated>
	<Buckets>
		<Bucket>
			<Name>examplebucket1-</Name>
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


#### 案例四：根据指定标签过滤存储桶列表


存储桶 examplebucket-1250000000 的标签为 `<key1, value1>`，存储桶 examplebucket1-1250000000 的标签为 `<key1, value1>` 和 `<key2, value2>`。

#### 请求

```plaintext
GET /?tagkey=key1&tagvalue=value1 HTTP/1.1
Host: service.cos.myqcloud.com
Date: Fri, 24 May 2019 11:59:51 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1558699191;1558706391&q-key-time=1558699191;1558706391&q-header-list=date;host&q-url-param-list=&q-signature=c3f55f4ce2800fb343cf85ff536a9185a0c1****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Length: 378
Content-Type: application/xml
Server: tencent-cos
Connection: keep-alive
Date: Thu, 20 Oct 2022 07:29:40 GMT
x-cos-request-id: NjM1MGY4ZTRfMWViMjM1MGFfYjg3MV8xNjdk****

<ListAllMyBucketsResult>
	<Owner>
		<ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
	</Owner>
	</Marker>
	</NextMarker>
	<IsTruncated>false</IsTruncated>
	<Buckets>
		<Bucket>
			<Name>examplebucket-1250000000 </Name>
			<Location>ap-guangzhou</Location>
			<CreationDate>2022-04-11T03:01:49Z</CreationDate>
			<BucketType>cos</BucketType>
		</Bucket>
	</Buckets>
	<Buckets>
		<Bucket>
			<Name>examplebucket1-1250000000 </Name>
			<Location>ap-guangzhou</Location>
			<CreationDate>2022-04-12T03:01:49Z</CreationDate>
			<BucketType>cos</BucketType>
		</Bucket>
	</Buckets>
</ListAllMyBucketsResult>
```


#### 案例五：根据创建时间过滤存储桶列表

列出创建时间早于 `2022-1-20 15:10:45` 的存储桶。

#### 请求

```plaintext
GET /?range=lt&create-time=1642662645 HTTP/1.1
Host: service.cos.myqcloud.com
User-Agent: curl/7.64.1
Accept: */*
Authorization: q-sign-algorithm=sha1&q-ak=AKIDYv3vWrwkHXVDfqk*****&q-sign-time=1667448802;1668448852&q-key-time=1667448802;1668448852&q-url-param-list=create-time;range&q-header-list=host&q-signature=a043c0593c8c4cd1caf570******
```


#### 响应


```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 5566
Connection: keep-alive
Date: Thu, 03 Nov 2022 04:14:23 GMT
Server: tencent-cos
x-cos-request-id: NjM2MzQwMWZfMmJiMjM1MGFfYTc******

<ListAllMyBucketsResult>
	<Owner>
		<ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
	</Owner>
	</Marker>
	</NextMarker>
	<IsTruncated>false</IsTruncated>
	<Buckets>
		<Bucket>
			<Name>examplebucket-1250000000</Name>
			<Location>ap-beijing</Location>
			<CreationDate>2021-11-23T03:02:12Z</CreationDate>
			<BucketType>cos</BucketType>
		</Bucket>
	</Buckets>
</ListAllMyBucketsResult>
```


#### 案例六：分页查询存储桶列表


#### 请求

```plaintext
GET /?max-keys=1 HTTP/1.1
Host: service.cos.myqcloud.com
User-Agent: curl/7.64.1
Accept: */*
Authorization: q-sign-algorithm=sha1&q-ak=AKIDYv3vWrwkHXVDfqk*****&q-sign-time=1667448802;1668448852&q-key-time=1667448802;1668448852&q-url-param-list=create-time;range&q-header-list=host&q-signature=a043c0593c8c4cd1caf570******
```

#### 响应


```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 5566
Connection: keep-alive
Date: Thu, 03 Nov 2022 04:14:23 GMT
Server: tencent-cos
x-cos-request-id: NjM2MzQwMWZfMmJiMjM1MGFfYTc******

<ListAllMyBucketsResult>
	<Owner>
		<ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
	</Owner>
	</Marker>
	<NexMarker>1</NextMarker>
	<IsTruncated>true</IsTruncated>
	<Buckets>
		<Bucket>
			<Name>examplebucket-1250000000</Name>
			<Location>ap-beijing</Location>
			<CreationDate>2021-11-23T03:02:12Z</CreationDate>
			<BucketType>cos</BucketType>
		</Bucket>
	</Buckets>
</ListAllMyBucketsResult>
```


