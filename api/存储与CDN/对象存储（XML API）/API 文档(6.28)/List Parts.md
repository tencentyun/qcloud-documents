## 功能描述
List Parts 用来查询特定分块上传中的已上传的块，即罗列出指定 UploadId 所属的所有已上传成功的分块。

## 请求

语法示例：
```
GET /ObjectName?uploadId=UploadId HTTP/1.1
Host: <BucketName>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Authorization: auth

```

> Authorization: Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
GET /ObjectName?uploadId=UploadId HTTP/1.1
```
该 API 接口接受 GET 请求。
#### 请求参数
该 API 接口使用到的一些请求参数用以自定义响应返回的分块信息。

|参数名称|描述|类型|必选|
|:---|:---|:---|:---|
| UploadId | 标示本次分块上传的ID | String | 是 |
| Encoding-type | 规定返回值的编码方式 | String | 否 |
| max-parts | 单次返回最大的条目数量，默认 1000 | String | 否 |
| part-number-marker | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始 | String | 否 |

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作的实现没有使用特殊的请求头部。

### 请求体
该请求的操作请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该响应无特殊的响应头。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```
<ListPartsResult>
  <Bucket></Bucket>
  <Encoding-Type></Encoding-Type>
  <Key></Key>
  <UploadId></UploadId>
  <Initiator>
    <UIN></UIN>
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
具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| ListPartsResult |无| 用来表述本次分块上传的所有信息 | Container |

Container 节点 ListPartsResult 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Bucket | ListPartsResult | 分块上传的目标 Bucket | String |
| Encoding-Type | ListPartsResult | 规定返回值的编码方式 |  String |
| Key | ListPartsResult | Object 的名称 |  String |
| UploadId | ListPartsResult | 标识本次分块上传的 ID |  String |
| Initiator | ListPartsResult | 用来表示本次上传发起者的信息 | Container |
| Owner | ListPartsResult | 用来表示这些分块所有者的信息 | Container |
| StorageClass | ListPartsResult | 用来表示这些分块的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE |  String |
| PartNumberMarker | ListPartsResult | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始 |  String |
| NextPartNumberMarker | ListPartsResult | 假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点 |  String |
| MaxParts | ListPartsResult | 单次返回最大的条目数量 |  String |
| IsTruncated | ListPartsResult | 返回条目是否被截断，布尔值：TRUE，FALSE |  Boolean |
| Part | ListPartsResult | 用来表示每一个块的信息 |  Container |

Container 节点 Initiator 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| UIN | ListPartsResult.Initiator  |  开发商APPID |  String |

Container 节点 Owner 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| UID | ListPartsResult.Owner |  用户 ID |  String |

Container 节点 Part 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| PartNumber | ListPartsResult.Part |  块的编号 |  String |
| LastModified |  ListPartsResult.Part  |  块最后修改时间  |  Date |
| Etag |  ListPartsResult.Part |  Object 块的 SHA-1 算法校验值 |  String |
| Size |  ListPartsResult.Part  |  块大小，单位 Byte |  String |

## 实际案例

### 请求
```
GET /coss3/test10M_2?uploadId=14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0&max-parts=1 HTTP/1.1
Host:burning-1251668577.cn-east.myqcloud.com
Date: Wed，18 Jan 2017 16:17:03 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1484643123;1484646723&q-key-time=1484643123;1484646723&q-header-list=host&q-url-param-list=max-parts;uploadId&q-signature=b8b4055724e64c9ad848190a2f7625fd3f9d3e87
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 661
Connection: keep-alive
Date: Wed，18 Jan 2017 16:17:03 GMT
x-cos-request-id: NTg3ZGRiMzhfMmM4OGY3XzdhY2NfYw==

<ListPartsResult>
    <Bucket>burning</Bucket>
    <Encoding-type/>
    <Key>test10M_2</Key>
    <UploadId>14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0</UploadId>
    <Initiator>
        <UIN/>
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
