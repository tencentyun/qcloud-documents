## 功能描述

GET Bucket Object Versions 接口用于拉取存储桶内的所有对象及其历史版本信息，您可以通过指定参数筛选出存储桶内部分对象及其历史版本信息。

> !使用子账号发起该请求，需要主账号授予您`GET Bucket Object Versions`的权限，如果您以主账号身份发起，则默认拥有该权限。

## 请求

### 请求示例

```http
GET /?versions HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Authorization: Auth String
```

> Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求参数

<table>
   <tr>
      <th>名称</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
   </tr>
   <tr>
      <td>prefix</td>
      <td>前缀匹配，用来规定返回的文件前缀地址</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>delimiter</td>
      <td>定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>key-marker</td>
      <td>默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td nowrap="nowrap">encoding-type</td>
      <td>规定返回值的编码方式，可选值：url</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>max-keys</td>
      <td>单次返回最大的条目数量，默认为最大值1000</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td nowrap="nowrap">version-id-marker</td>
      <td>指定您需要从 version-id-marker 这个版本 ID 号开始列出对象的所有历史版本，可选值为 Valid version ID、Default。如果不指定版本 ID，默认为最新版本对象</td>
      <td>string</td>
      <td>否</td>
   </tr>
</table>

### 请求头

此接口仅使用公共请求头部，详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

### 请求体

此接口无请求体。

## 响应

### 响应头

此接口仅返回公共响应头部，详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

### 响应体

```http
<ListVersionsResult>
    <Name>exampleBucket-1250000000</Name>
    <Prefix/></Prefix>
    <KeyMarker/></KeyMarker>
    <VersionIdMarker/></VersionIdMarker>
    <MaxKeys></MaxKeys>
    <IsTruncated></IsTruncated>
    <DeleteMarker>
    	<Key>exampleObject</Key>
    	<VersionId>VersionId</VersionId>
    	<IsLatest>true</IsLatest>
    	<LastModified>Date</LastModified>
    	<Owner>
    		<UID>OwnerUin</UID>
		</Owner>
    </DeleteMarker>
    <Version>
    	<Key>exampleObject.txt</Key>
    	<VersionId>VersionId</VersionId>
    	<IsLatest>false</IsLatest>
    	<LastModified>Date</LastModified>
    	<ETag>ETag</ETag>
    	<Size>ObjectSize</Size>
    	<StorageClass>StorageClass</StorageClass>
    	<Owner>
    		<UID>OwnerUin</UID>
    	</Owner>
    </Version>
</ListVersionsResult>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点 | 描述                               | 类型      |
| ------------------ | ------ | ---------------------------------- | --------- |
| ListVersionsResult | 无     | 保存 Get Bucket 请求结果的所有信息 | Container |

**Container 节点 ListVersionsResult 的内容**：

| 节点名称（关键字） | 父节点             | 描述                                                         | 类型      |
| ------------------ | ------------------ | ------------------------------------------------------------ | --------- |
| Name               | ListVersionsResult | 存储桶名称                                                   | string    |
| Encoding-Type      | ListVersionsResult | 编码格式                                                     | string    |
| Prefix             | ListVersionsResult | 前缀匹配，用来规定响应请求返回的文件前缀地址                 | string    |
| KeyMarker          | ListVersionsResult | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始  | string    |
| MaxKeys            | ListVersionsResult | 单次响应请求内返回结果的最大条目数量                       | string    |
| IsTruncated        | ListVersionsResult | 响应请求条目是否被截断，布尔值：true，false                  | boolean   |
| NextMarker         | ListVersionsResult | 假如返回条目被截断，则返回 NextMarker，即下一个条目的起点   | string    |
| DeleteMarker       | ListVersionsResult | 如果对象被删除过，则会带有删除标记                         | Container |
| Version            | ListVersionsResult | 如果对象为被删除，存在于存储桶中，该容器记录对象元数据信息 | Container |

**Container 节点 DeleteMarker 的内容**：

| 节点名称（关键字） | 父节点                          | 描述                     | 类型      |
| ------------------ | ------------------------------- | ------------------------ | --------- |
| Key                | ListVersionsResult.DeleteMarker | 被删除对象的索引         | string    |
| VersionId          | ListVersionsResult.DeleteMarker | 对象版本 ID               | string    |
| IsLatest           | ListVersionsResult.DeleteMarker | 被删除对象是否为最新版本 | string    |
| LastModified       | ListVersionsResult.DeleteMarker | 对象最后被修改时间       | string    |
| Owner              | ListVersionsResult.DeleteMarker | 存储桶所有者信息         | Container |

**Container 节点 Version 的内容**：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
   </tr>
   <tr>
      <td>Key</td>
      <td>ListVersionsResult.Version</td>
      <td>被删除对象的索引</td>
      <td>string</td>
   </tr>
   <tr>
      <td>VersionId</td>
      <td>ListVersionsResult.Version</td>
      <td>对象版本 ID</td>
      <td>string</td>
   </tr>
   <tr>
      <td>IsLatest</td>
      <td>ListVersionsResult.Version</td>
      <td>被删除对象是否为最新版本</td>
      <td>string</td>
   </tr>
   <tr>
      <td>LastModified</td>
      <td>ListVersionsResult.Version</td>
      <td>对象最后被修改时间</td>
      <td>string</td>
   </tr>
   <tr>
      <td>ETag</td>
      <td>ListVersionsResult.Version</td>
      <td>实体标签（Entity Tag）是根据对象的内容而非元数据生成的哈希值，不同的对象拥有不同的 ETag，可以根据 ETag 判断指定对象是否有修改。</td>
      <td>string</td>
   </tr>
   <tr>
      <td>Size</td>
      <td>ListVersionsResult.Version</td>
      <td>说明对象大小，单位是 Byte</td>
      <td>string</td>
   </tr>
   <tr>
      <td>StorageClass</td>
      <td>ListVersionsResult.Version</td>
      <td>对象的存储级别，枚举值：STANDARD，STANDARD_IA，ARCHIVE</td>
      <td>string</td>
   </tr>
   <tr>
      <td>Owner</td>
      <td>ListVersionsResult.Version</td>
      <td>存储桶所有者信息</td>
      <td>Container</td>
   </tr>
</table>

**Container 节点 Owner 的内容**：		
		

| 节点名称（关键字） | 父节点                             | 描述                  | 类型   |
| ------------------ | ---------------------------------- | --------------------- | ------ |
| UID                 | ListVersionsResul t.Contents.Owner | 存储桶拥有者的 APPID | string |

## 实际案例

### 请求

```shell
GET /?versions HTTP/1.1
Host: exampleBucket-1250000000.cos.ap-chengdu.myqcloud.com
Connection: keep-alive
Accept: */*
User-Agent: python-requests/2.12.4
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9Sm****&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=versions&q-header-list=host&q-signature=5118a936049f9d44482bbb61309235cf4abe****
```

### 响应

```shell
Content-Type: application/xml
Content-Length: 35524
Connection: keep-alive
Date: Fri, 14 Apr 2019 04:14:26 GMT
Server: tencent-cos
x-cos-request-id: NWQwMzFmMjJfN2QyZjIyMDlfY2M2MV85MGE5****

<ListVersionsResult>
    <Name>exampleBucket-1250000000</Name>
    <Prefix/>
    <KeyMarker/>
    <VersionIdMarker/>
    <MaxKeys>1000</MaxKeys>
    <IsTruncated>false</IsTruncated>
    <DeleteMarker>
    	<Key>100K.txt</Key>
    	<VersionId>MTg0NDUxODM2NDIzNDY0MzIxNjQ</VersionId>
    	<IsLatest>true</IsLatest>
    	<LastModified>2019-06-13T13:09:23.000Z</LastModified>
    	<Owner>
    		<UID>1250000000</UID>
        </Owner>
    </DeleteMarker>
    <Version>
    	<Key>100K.txt</Key>
    	<VersionId>MTg0NDUxODM2NDYxNTg1MTgxODk</VersionId>
    	<IsLatest>false</IsLatest>
    	<LastModified>2019-06-13T12:05:51.000Z</LastModified>
    	<ETag>&quot;fffc7956ba9a7b58a63c01b6ce1ddc45&quot;</ETag>
    	<Size>102401</Size>
    	<StorageClass>STANDARD</StorageClass>
    	<Owner>
    		<UID>1250000000</UID>
    	</Owner>
    </Version>
    <Version>
        <Key>100K.txt</Key>
        <VersionId>null</VersionId>
        <IsLatest>false</IsLatest>
        <LastModified>2019-06-13T10:00:09.000Z</LastModified>
        <ETag>&quot;fffc7956ba9a7b58a63c01b6ce1ddc45&quot;</ETag>
        <Size>102401</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
        	<UID>1250000000</UID>
        </Owner>
    </Version>
        <Version>
        <Key>100M.txt</Key>
        <VersionId>MTg0NDUxODM2NDYxNTc0NDc2MTM</VersionId>
        <IsLatest>true</IsLatest>
        <LastModified>2019-06-13T12:06:15.000Z</LastModified>
        <ETag>&quot;5b98499bd9900f3dc433b63a66a35252-101&quot;</ETag>
        <Size>104857601</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
        	<UID>1250000000</UID>
        </Owner>
    </Version>
    <Version>
        <Key>100M.txt</Key>
        <VersionId>null</VersionId>
        <IsLatest>false</IsLatest>
        <LastModified>2019-06-13T10:00:47.000Z</LastModified>
        <ETag>&quot;620b3b3e325b1b02823046c946ecde3d-101&quot;</ETag>
        <Size>104857601</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
        	<UID>1250000000</UID>
        </Owner>
        </Version>
    <Version>
        <Key>1204M.txt</Key>
        <VersionId>null</VersionId>
        <IsLatest>true</IsLatest>
        <LastModified>2019-06-13T10:05:11.000Z</LastModified>
        <ETag>&quot;6e37bf6cc44744075426c14b4b2aa276-1205&quot;</ETag>
        <Size>1262485505</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
        	<UID>1250000000</UID>
        </Owner>
    </Version>
    <Version>
        <Key>25K.txt</Key>
        <VersionId>MTg0NDUxODM2NDYxNTg4NDU5MDE</VersionId>
        <IsLatest>true</IsLatest>
        <LastModified>2019-06-13T12:05:50.000Z</LastModified>
        <ETag>&quot;cabe069ebe3561c35c6a5ae5a362f7a5&quot;</ETag>
        <Size>25601</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
        	<UID>1250000000</UID>
        </Owner>
    </Version>
    <Version>
        <Key>25K.txt</Key>
        <VersionId>null</VersionId>
        <IsLatest>false</IsLatest>
        <LastModified>2019-06-13T09:59:59.000Z</LastModified>
        <ETag>&quot;cabe069ebe3561c35c6a5ae5a362f7a5&quot;</ETag>
        <Size>25601</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
        	<UID>1250000000</UID>
        </Owner>
    </Version>
    <Version>
        <Key>25M.txt</Key>
        <VersionId>MTg0NDUxODM2NDYxNTg2MTE5MTA</VersionId>
        <IsLatest>true</IsLatest>
        <LastModified>2019-06-13T12:05:58.000Z</LastModified>
        <ETag>&quot;b1b3fcdba0def587df7031e440d623cf-26&quot;</ETag>
        <Size>26214401</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
        	<UID>1250000000</UID>
        </Owner>
    </Version>
    <Version>
        <Key>25M.txt</Key>
        <VersionId>null</VersionId>
        <IsLatest>false</IsLatest>
        <LastModified>2019-06-13T10:00:08.000Z</LastModified>
        <ETag>&quot;834f90daf03a8810620175c2f2d4104a-26&quot;</ETag>
        <Size>26214401</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
        	<UID>1250000000</UID>
        </Owner>
    </Version>
</ListVersionsResult>
```
