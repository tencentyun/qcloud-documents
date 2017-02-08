## 功能描述
List Parts用来查询特定分块上传中的已上传的块。

## 请求

### 请求语法

```Http
GET /ObjectName?uploadId=UploadId HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### 请求参数

| 名称                 | 描述                                | 类型     | 必选   |
| ------------------ | --------------------------------- | ------ | ---- |
| UploadID           | 标示本次分块上传的ID                       | String | 是    |
| Encoding-type      | 规定返回值的编码方式                        | String | 否    |
| max-parts          | 单次返回最大的条目数量，默认1000                | String | 否    |
| part-number-marker | 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始 | String | 否    |

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无返回头部

### 返回内容

| 名称                   | 描述                                       | 类型        |
| -------------------- | ---------------------------------------- | --------- |
| ListPartsResult      | 用来表述本次分块上传的所有信息，子节点包括：Bucket，Encoding-type，Key，UploadID，Initiator，Owner，PartNumberMarker，NextPartNumberMarker，MaxParts，IsTruncated，Part | Container |
| Bucket               | 分块上传的目标Bucket<br/>父节点：ListPartsResult    | String    |
| Encoding-type        | 规定返回值的编码方式<br/>父节点：ListPartsResult       | String    |
| Key                  | Object的名称<br/>父节点：ListPartsResult        | String    |
| UploadID             | 标示本次分块上传的ID<br/>父节点：ListPartsResult      | String    |
| Initiator            | 用来表示本次上传发起者的信息，子节点包括UID<br/>父节点：ListPartsResult | Container |
| UID                  | 开发商APPID                                 | String    |
| Owner                | 用来表示这些分块所有者的信息，子节点包括UID<br/>父节点：ListPartsResult | Container |
| StorageClass         | 用来表示这些分块的存储级别，枚举值：Standard，Standard_IA，Nearline<br/>父节点：ListPartsResult | String    |
| PartNumberMarker     | 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始<br/>父节点：ListPartsResult | String    |
| NextPartNumberMarker | 假如返回条目被截断，则返回NextMarker就是下一个条目的起点<br/>父节点：ListPartsResult | String    |
| MaxParts             | 单次返回最大的条目数量<br/>父节点：ListPartsResult      | String    |
| IsTruncated          | 返回条目是否被截断，布尔值：True，False<br/>父节点：ListPartsResult | Boolen    |
| Part                 | 用来表示每一个块的信息<br/>父节点：ListPartsResult      | Container |
| PartNumber           | 块的编号<br/>父节点：Part                        | String    |
| LastModified         | 块最后修改时间 <br/>父节点：Part                    | Date      |
| Etag                 | 块的 SHA-1 算法校验值<br/>父节点：Part              | String    |
| Size                 | 块大小，单位Byte<br/>父节点：Part                  | String    |

```XML
<ListPartsResult>
  <Bucket></Bucket>
  <Encoding-type></Encoding-type>
  <Key></Key>
  <UploadID></UploadID>
  <Initiator>
    <UID></UID>
  </Initiator>
  <Owner>
    <UID></UID>
  </Owner>
  <StorageClass></StorageClass>
  <PartNumberMarker></PartNumberMarker>
  <NextPartNumberMarker></NextPartNumberMarker>
  <MaxParts></MaxParts>
  <IsTruncated></IsTruncated>
  <Part>
    <PartNumber></PartNumber>
    <LastModified></LastModified>
    <Etag></Etag>
    <Size></Size>
  </Part>
</ListPartsResult>
```

## 示例

### 请求

```HTTP
GET /coss3/test10M_2?uploadId=14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0&max-parts=1 HTTP/1.1
Host:burning-1251668577.cn-east.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1484643123;1484646723&q-key-time=1484643123;1484646723&q-header-list=host&q-url-param-list=max-parts;uploadId&q-signature=b8b4055724e64c9ad848190a2f7625fd3f9d3e87
```

### 返回

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 661
Connection: keep-alive
Date: Tue Jan 17 16:52:08 2017
x-cos-request-id: NTg3ZGRiMzhfMmM4OGY3XzdhY2NfYw==

<ListPartsResult>
	<Bucket>burning</Bucket>
	<Encoding-type/>
	<Key>test10M_2</Key>
	<UploadId>14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0</UploadId>
	<Initiator>
		<UID/>
	</Initiator>
	<Owner>
		<UID>1251668577</UID>
	</Owner>
	<PartNumberMarker>0</PartNumberMarker>
	<Part>
		<PartNumber>1</PartNumber>
		<LastModified>Tue Jan 17 16:43:37 2017</LastModified>
		<ETag>"a1f8e5e4d63ac6970a0062a6277e191fe09a1382"</ETag>
		<Size>5242880</Size>
	</Part>
	<NextPartNumberMarker>1</NextPartNumberMarker>
	<StorageClass>Standard</StorageClass>
	<MaxParts>1</MaxParts>
	<IsTruncated>true</IsTruncated>
</ListPartsResult>
```