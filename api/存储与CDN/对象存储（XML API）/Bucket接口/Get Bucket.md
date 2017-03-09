## 功能描述

Get Bucket请求等同于 List Object请求，可以列出该Bucekt下部分或者所有Object，发起该请求需要拥有Read权限。

## 请求

### 请求语法

```Http
GET / HTTP/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### 请求参数

| 名称            | 描述                                       | 类型     | 必选   |
| ------------- | ---------------------------------------- | ------ | ---- |
| prefix        | 前缀匹配，用来规定返回的文件前缀地址                       | String | 否    |
| delimiter     | 定界符为一个符号，如果有Prefix，则将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix，然后列出所有Common Prefix。如果没有Prefix，则从路径起点开始 | String | 否    |
| encoding-type | 规定返回值的编码方式                               | String | 否    |
| marker        | 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始        | String | 否    |
| max-keys      | 单次返回最大的条目数量，默认1000                       | String | 否    |

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 名称                    | 描述                                       | 类型     |
| --------------------- | ---------------------------------------- | ------ |
| Name                  | Bucket名字<br/>父节点：ListBucketResult        | String |
| Prefix                | 前缀匹配，用来规定返回的文件前缀地址<br/>父节点：ListBucketResult | String |
| Marker                | 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始<br/>父节点：ListBucketResult | String |
| Maxkey                | 单次返回最大的条目数量<br/>父节点：ListBucketResult     | String |
| IsTruncated           | 返回条目是否被截断，布尔值：True，False<br/>父节点：ListBucketResult | Boolen |
| NextMarker            | 假如返回条目被截断，则返回NextMarker就是下一个条目的起点<br/>父节点：ListBucketResult | String |
| CommonPrefixes        | 将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix<br/>父节点：ListBucketResult | String |
| Encoding-Type         | 编码类型，作用于Delimiter，Marker，Prefix，NextMarker，Key<br/>父节点：ListBucketResult | String |
| Content               | 元数据信息<br/>父节点：ListBucketResult           | Container    |
| Key                   | Object名称<br/>父节点：ListBucketResult.Contents | String |
| LastModified          | Object最后修改时间<br/>父节点：ListBucketResult.Contents | Date   |
| Etag                  | 文件的 SHA-1 算法校验值<br/>父节点：ListBucketResult.Contents | String |
| Size                  | 文件大小，单位Byte<br/>父节点：ListBucketResult.Contents | String |
| Owner                 | Bucket所有者信息<br/>父节点：ListBucketResult.Contents | Container    |
| StorageClass          | Object的存储级别，枚举值：Standard，Standard_IA，Nearline | String |
| ID                    | Bucket的UID父节点：ListBucketResult.Contents.Owener | String |
| CommonPrefixes.Prefix | 单条Common Prefix<br/>父节点：CommonPrefixes   |    String    |

```XML
<ListBucketResult>
  <Name></Name>
  <Prefix></Prefix>
  <Marker></Marker>
  <MaxKeys></MaxKeys>
  <IsTruncated></IsTruncated>
  <Contents>
    <Key></Key>
    <LastModified></LastModified>
    <ETag></ETag>
    <Size></Size>
    <Owner>
      <ID></ID>
     </Owner>
     <StorageClass></StorageClass>
  </Contents>
  <CommonPrefixes>
    <Prefix></Prefix>
  </CommonPrefixes>
</ListBucketResult>
```

## 示例

### 请求

```HTTP
GET / HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213451;32557109451&q-key-time=1484213451;32557109451&q-header-list=host&q-url-param-list=&q-signature=0336a1fc8350c74b6c081d4dff8e7a2db9007dce
```

### 返回

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1132
Connection: keep-alive
Vary: Accept-Encoding
Date: Thu Jan 12 17:30:54 2017
Server: tencent-cos
x-cos-request-id: NTg3NzRjY2VfYmRjMzVfMTc5M182MmIyNg==

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
	<Name>zuhaotestnorth</Name>
	<Prefix/>
	<Marker/>
	<MaxKeys>1000</MaxKeys>
	<Delimiter>/</Delimiter>
	<IsTruncated>false</IsTruncated>
	<Contents>
		<Key>testL</Key>
		<LastModified>Wed Jan 11 18:57:06 2017</LastModified>
		<ETag>"79f2a852fac7e826c9f4dbe037f8a63b"</ETag>
		<Size>10485760</Size>
		<StorageClass>Standard</StorageClass>
	</Contents>
	<Contents>
		<Key>testL1</Key>
		<LastModified>Wed Jan 11 19:02:17 2017</LastModified>
		<ETag>"3f9a5dbff88b25b769fa6304902b5d9d"</ETag>
		<Size>10485760</Size>
		<StorageClass>Standard</StorageClass>
	</Contents>
	<Contents>
		<Key>testLLL</Key>
		<LastModified>Wed Jan 11 16:36:08 2017</LastModified>
		<ETag>"39bfb88c11c65ed6424d2e1cd4db1826"</ETag>
		<Size>10485760</Size>
		<StorageClass>Standard</StorageClass>
	</Contents>
	<Contents>
		<Key>testLOL</Key>
		<LastModified>Wed Jan 11 17:24:10 2017</LastModified>
		<ETag>"fb31459ad10289ff49327fd91a3e1f6a"</ETag>
		<Size>4</Size>
		<StorageClass>Standard</StorageClass>
	</Contents>
	<Contents>
		<Key>tet</Key>
		<LastModified>Wed Jan 11 15:54:02 2017</LastModified>
		<ETag>"83b3ec25cc19626ac073297eba30fbc4"</ETag>
		<Size>10485760</Size>
		<StorageClass>Standard</StorageClass>
	</Contents>
</ListBucketResult>
```

