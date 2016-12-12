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
