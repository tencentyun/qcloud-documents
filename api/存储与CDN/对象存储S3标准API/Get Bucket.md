## 功能描述

Get Bucket请求等同于 List Object请求，可以列出该Bucekt下部分或者所有Object，发起该请求需要拥有Read权限。

## 请求

### 请求语法

```Http
GET / HTTP/1.1
Host:[BucketName]-[UID].[Region].myqcloud.com
Date: date
Authorization: authorization string
```

### 请求参数

| 名称            | 描述                                       | 类型     | 必选   |
| ------------- | ---------------------------------------- | ------ | ---- |
| prefix        | 前缀匹配，用来规定返回的文件前缀地址                       | String | 否    |
| delimiter     | 定界符为一个符号，如果有Prefix，则将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix，然后列出所有Common Prefix。如果没有Prefix，则从路径起点开始 | String | 否    |
| encoding-type | 规定返回值的编码方式                               | String | 否    |
| marker        | 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始        | String | 否    |
| max-key       | 单次返回最大的条目数量，默认1000                       | String | 否    |

### 请求HTTP Header

无特殊请求Header，其他内容请参见公共请求Header

### 请求Body

无

## 返回值

### 返回Header

无特殊请求Header，其他内容请参见公共返回Header

### 返回Body

| 名称            | 描述                                       | 类型     |
| ------------- | ---------------------------------------- | ------ |
| Name          | Bucket名字<br/>父节点：ListBucketResult        | String |
| Prefix        | 前缀匹配，用来规定返回的文件前缀地址<br/>父节点：ListBucketResult | String |
| Marker        | 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始<br/>父节点：ListBucketResult | String |
| Maxkey        | 单次返回最大的条目数量<br/>父节点：ListBucketResult     | String |
| IsTruncated   | 返回条目是否被截断，布尔值：True \| False<br/>父节点：ListBucketResult | Boolen |
| NextMarker    | 假如返回条目被截断，则返回NextMarker就是下一个条目的起点<br/>父节点：ListBucketResult | String |
| CommonPrefix  | 将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix<br/>父节点：ListBucketResult | String |
| Encoding-Type | 编码类型，作用于Delimiter，Marker，Prefix，NextMarker，Key<br/>父节点：ListBucketResult | String |
| Content       | 元数据信息<br/>父节点：ListBucketResult           | XML    |
| Key           | Object名称<br/>父节点：ListBucketResult.Contents | String |
| LastModified  | Object最后修改时间<br/>父节点：ListBucketResult.Contents | Date   |
| Etag          | 文件的 SHA-1 算法校验值<br/>父节点：ListBucketResult.Contents | String |
| Size          | 文件大小，单位Byte<br/>父节点：ListBucketResult.Contents | String |
| Owner         | Bucket所有者信息<br/>父节点：ListBucketResult.Contents或者ListBucketResult.CommonPrefix | XML    |
| ID            | Bucket的UID<br/>父节点：ListBucketResult.Contents.Owener | String |

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
  </Contents>
  <CommonPrefixes>
    <Prefix></Prefix>
  </CommonPrefixes>
</ListBucketResult>
```
