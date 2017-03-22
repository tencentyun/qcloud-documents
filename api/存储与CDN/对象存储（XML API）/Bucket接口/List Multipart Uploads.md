## 功能描述
List Multipart Uploads用来查询正在进行中的分块上传。单次最多列出1000个正在进行中的分块上传。

## 请求

### 请求语法

```Http
GET /?uploads HTTP/1.1
Host:<BucketName>-<AppID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### 请求参数

| 名称               | 描述                                       | 类型     | 必选   |
| ---------------- | ---------------------------------------- | ------ | ---- |
| delimiter        | 定界符为一个符号，如果有Prefix，则将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix，然后列出所有Common Prefix。如果没有Prefix，则从路径起点开始 | String | 否    |
| encoding-type    | 规定返回值的编码方式                               | String | 否    |
| Prefix           | 前缀匹配，用来规定返回的文件前缀地址                       | String | 否    |
| max-uploads      | 单次返回最大的条目数量，默认1000                       | String | 否    |
| key-marker       | 与upload-id-marker一起使用<Br/>当upload-id-marker未被指定时，ObjectName字母顺序大于key-marker的条目将被列出<Br/>当upload-id-marker被指定时，ObjectName字母顺序大于key-marker的条目被列出，ObjectName字母顺序等于key-marker同时UploadID大于upload-id-marker的条目将被列出。 | String | 否    |
| upload-id-marker | 与key-marker一起使用<Br/>当key-marker未被指定时，upload-id-marker将被忽略<Br/>当key-marker被指定时，ObjectName字母顺序大于key-marker的条目被列出，ObjectName字母顺序等于key-marker同时UploadID大于upload-id-marker的条目将被列出。 | String | 否    |

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 名称                                | 描述                                       | 类型        |
| --------------------------------- | ---------------------------------------- | --------- |
| ListMultipartUploadsResult        | 用来表述所有分块上传的信息                            | Container |
| Bucket                            | 分块上传的目标Bucket<br/>父节点：ListMultipartUploadsResult | String    |
| Encoding-type                     | 规定返回值的编码方式<br/>父节点：ListMultipartUploadsResult | String    |
| KeyMarker                         | 列出条目从该key值开始<br/>父节点：ListMultipartUploadsResult | String    |
| UploadIdMarker                    | 列出条目从该UploadId值开始<br/>父节点：ListMultipartUploadsResult | String    |
| NextKeyMarker                     | 假如返回条目被截断，则返回NextKeyMarker就是下一个条目的起点<br/>父节点：ListMultipartUploadsResult | String    |
| NextUploadIdMarker                | 假如返回条目被截断，则返回UploadId就是下一个条目的起点<br/>父节点：ListMultipartUploadsResult | String    |
| MaxUploads                        | 单次返回最大的条目数量<br/>父节点：ListMultipartUploadsResult | String    |
| IsTruncated                       | 返回条目是否被截断，布尔值：True，False<br/>父节点：ListMultipartUploadsResult| Boolean    |
| Upload                            | 每个Upload的信息<br/>父节点：ListMultipartUploadsResult | Container |
| Key                               | Object的名称<br/>父节点：Upload                 | Integer   |
| UploadID                          | 标示本次分块上传的ID<br/>父节点：Upload               | Integer   |
| StorageClass                      | 用来表示分块的存储级别，枚举值：Standard，Standard_IA，Nearline <br/>父节点：Upload | String    |
| Initiator                         | 用来表示本次上传发起者的信息，子节点包括UID<br/>父节点：Upload   | Container |
| UID                               | 开发商APPID<br/>父节点：Initiator，Owner         | String    |
| Owner                             | 用来表示这些分块所有者的信息，子节点包括UID<br/>父节点：Upload   | Container |
| Initiated                         | 分块上传的起始时间<br/>父节点：Upload                 | Date      |
| ListMultipartUploadsResult.Prefix | 前缀匹配，用来规定返回的文件前缀地址<br/>父节点：ListMultipartUploadsResult | String    |
| delimiter                         | 定界符为一个符号，如果有Prefix，则将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix，然后列出所有Common Prefix。如果没有Prefix，则从路径起点开始<br/>父节点：ListMultipartUploadsResult | String    |
| CommonPrefixs                     | 将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix<br/>父节点：ListMultipartUploadsResult | Container |
| CommonPrefixs.Prefix              | 显示具体的CommonPrefixs<br/>父节点：CommonPrefixs | String    |

```XML
<ListMultipartUploadsResult>
  <Bucket></Bucket>
  <Encoding-type></Encoding-type>
  <KeyMarker></KeyMarker>
  <UploadIdMarker></UploadIdMarker>
  <NextKeyMarker></NextKeyMarker>
  <NextUploadIdMarker></NextUploadIdMarker>
  <MaxUploads></MaxUploads>
  <IsTruncated></IsTruncated>
  <Prefix></Prefix>
  <delimiter></delimiter>
  <Upload>
    <Key></Key>
    <UploadID></UploadID>
    <StorageClass></StorageClass>
    <Initiator>
      <UID></UID>
    </Initiator>
    <Owner>
      <UID></UID>
    </Owner>
    <Initiated></Initiated>
  </Upload>
  <CommonPrefixs>
    <Prefix></Prefix>
  </CommonPrefixs>
</ListMultipartUploadsResult>
```

## 示例

### 请求

```HTTP
GET /?uploads HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727508;32557623508&q-key-time=1484727508;32557623508&q-header-list=host&q-url-param-list=uploads&q-signature=5bd4759a7309f7da9a0550c224d8c61589c9dbbf
```

### 返回

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1203
Date: Wed Jan 18 16:18:37 2017
Server: tencent-cos
x-cos-request-id: NTg3ZjI0ZGRfNDQyMDRlXzNhZmRfMjRl

<ListMultipartUploadsResult>
	<Bucket>arlenhuangtestsgnoversion</Bucket>
	<Encoding-Type/>
	<KeyMarker/>
	<UploadIdMarker/>
	<MaxUploads>1000</MaxUploads>
	<Prefix/>
	<Delimiter>/</Delimiter>
	<IsTruncated>false</IsTruncated>
	<Upload>
		<Key>Object</Key>
		<UploadID>1484726657932bcb5b17f7a98a8cad9fc36a340ff204c79bd2f51e7dddf0b6d1da6220520c</UploadID>
		<Initiator>
			<UID/>
		</Initiator>
		<Owner>
			<UID>1251668577</UID>
		</Owner>
		<StorageClass>Standard</StorageClass>
		<Initiated>Wed Jan 18 16:04:17 2017</Initiated>
	</Upload>
	<Upload>
		<Key>Object</Key>
		<UploadID>1484727158f2b8034e5407d18cbf28e84f754b791ecab607d25a2e52de9fee641e5f60707c</UploadID>
		<Initiator>
			<UID/>
		</Initiator>
		<Owner>
			<UID>1251668577</UID>
		</Owner>
		<StorageClass>Standard</StorageClass>
		<Initiated>Wed Jan 18 16:12:38 2017</Initiated>
	</Upload>
	<Upload>
		<Key>ObjectName</Key>
		<UploadID>1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e</UploadID>
		<Initiator>
			<UID/>
		</Initiator>
		<Owner>
			<UID>1251668577</UID>
		</Owner>
		<StorageClass>Standard</StorageClass>
		<Initiated>Wed Jan 18 16:14:30 2017</Initiated>
	</Upload>
</ListMultipartUploadsResult>
```

