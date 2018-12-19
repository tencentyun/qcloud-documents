## 功能描述
List Parts 用来查询特定分块上传中的已上传的块，即罗列出指定 UploadId 所属的所有已上传成功的分块。

## 请求
### 请求示例

```
GET /ObjectName?uploadId=UploadId HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。
#### 非公共头部
该请求操作无特殊的请求头部信息。

#### 请求参数

名称|类型|必选|描述
---|---|---|---
UploadId|string|是|标识本次分块上传的 ID。使用 Initiate Multipart Upload 接口初始化分片上传时会得到一个 uploadId，该 ID 不但唯一标识这一分块数据，也标识了这分块数据在整个文件内的相对位置
encoding-type|string|否|规定返回值的编码方式
max-parts|string|否|单次返回最大的条目数量，默认 1000
part-number-marker|string|否|默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始

### 请求体
该请求请求体为空。

## 响应

### 响应头
#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
查询成功，返回 **application/xml** 数据，包含已完成的分片信息。

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<ListPartsResult>
  <Bucket>string</Bucket>
  <Encoding-Type>string</Encoding-Type>
  <Key>string</Key>
  <UploadId>string</UploadId>
  <Initiator>
    <ID>string</ID>
    <DisplayName>string</DisplayName>
  </Initiator>
  <Owner>
    <ID>string</ID>
    <DisplayName>string</DisplayName>
  </Owner>
  <StorageClass>string</StorageClass>
  <PartNumberMarker>string</PartNumberMarker>
  <NextPartNumberMarker>string</NextPartNumberMarker>
  <MaxParts>string</MaxParts>
  <IsTruncated>true</IsTruncated>
  <Part>
    <PartNumber>string</PartNumber>
    <LastModified>string</LastModified>
    <ETag>string</ETag>
    <Size>string</Size>
  </Part>
</ListPartsResult>
```

具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
ListPartsResult|无|保存 List Parts 请求结果的所有信息|Container|是

Container 节点 ListPartsResult 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
Bucket|ListPartsResult|分块上传的目标 Bucket，存储桶的名字，由用户自定义字符串和系统生成 appid 数字串由中划线连接而成，如：mybucket-1250000000|string|是
Encoding-Type|ListPartsResult|编码格式|string|是
Key|ListPartsResult|Object 的名字|string|是
UploadId|ListPartsResult|标识本次分块上传的 ID|string|是
Initiator|ListPartsResult|用来表示这些分块所有者的信息|Container|是
Owner|ListPartsResult|用来表示这些分块所有者的信息|Container|是
StorageClass|ListPartsResult|用来表示这些分块的存储级别，枚举值：STANDARD，STANDARD_IA，ARCHIVE|string|是
PartNumberMarker|ListPartsResult|默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始|string|是
NextPartNumberMarker|ListPartsResult|假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点|string|是
MaxParts|ListPartsResult|单次返回最大的条目数量|string|是
IsTruncated|ListPartsResult|响应请求条目是否被截断，布尔值：true，false|boolean|是
Part|ListPartsResult|元数据信息|Container|是
Container 节点 Initiator 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
ID|ListPartsResult.Initiator|创建者的一个唯一标识|string|是
DisplayName|ListPartsResult.Initiator|创建者的用户名描述|string|是
Container 节点 Owner 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
ID|ListPartsResult.Owner|创建者的一个唯一标识|string|是
DisplayName|ListPartsResult.Owner|创建者的用户名描述|string|是
Container 节点 Part 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
PartNumber|ListPartsResult.Part|块的编号|string|是
LastModified|ListPartsResult.Part|说明块最后被修改时间|string|是
ETag|ListPartsResult.Part|块的 MD-5 算法校验值|string|是
Size|ListPartsResult.Part|说明块大小，单位是 Byte|string|是

## 实际案例

### 请求

```
GET /coss3/test10M_2?uploadId=14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0&max-parts=1 HTTP/1.1
Host:burning-1251668577.cos.ap-beijing.myqcloud.com
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
    <Bucket>burning-123456789</Bucket>
    <Encoding-type/>
    <Key>test10M_2</Key>
    <UploadId>14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0</UploadId>
    <Initiator>
        <ID>123456789</ID>
        <DisplyName>123456789</DisplyName>
    </Initiator>
    <Owner>
        <ID>qcs::cam::uin/156545789:uin/156545789</ID>
        <DisplyName>156545789</DisplyName>
    </Owner>
    <PartNumberMarker>0</PartNumberMarker>
    <Part>
        <PartNumber>1</PartNumber>
        <LastModified>Tue Jan 17 16:43:37 2017</LastModified>
        <ETag>"a1f8e5e4d63ac6970a0062a6277e191fe09a1382"</ETag>
        <Size>5242880</Size>
    </Part>
    <NextPartNumberMarker>1</NextPartNumberMarker>
    <StorageClass>STANDARD</StorageClass>
    <MaxParts>1</MaxParts>
    <IsTruncated>true</IsTruncated>
</ListPartsResult>
```


