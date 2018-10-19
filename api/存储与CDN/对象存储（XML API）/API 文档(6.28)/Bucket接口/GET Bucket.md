## 功能描述
GET Bucket 请求等同于 List Object 请求，可以列出该 Bucket 下的部分或者全部 Object。此 API 调用者需要对 Bucket 有 Read 权限。

## 请求
### 请求示例

```
GET / HTTP/1.1
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
prefix|string|否|前缀匹配，用来规定返回的文件前缀地址
delimiter|string|否|定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始
encoding-type|string|否|规定返回值的编码方式，可选值：url
marker|string|否|默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始
max-keys|string|否|单次返回最大的条目数量，默认 1000

### 请求体
该请求请求体为空。

## 响应
### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
查询成功，返回 application/xml 数据，包含 Bucket 中的对象信息。

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<ListBucketResult>
  <Name>string</Name>
  <Encoding-Type>string</Encoding-Type>
  <Prefix>string</Prefix>
  <Marker>string</Marker>
  <MaxKeys>string</MaxKeys>
  <IsTruncated>true</IsTruncated>
  <NextMarker>string</NextMarker>
  <Contents>
    <Key>string</Key>
    <LastModified>string</LastModified>
    <ETag>string</ETag>
    <Size>string</Size>
    <Owner>
      <ID>string</ID>
    </Owner>
    <StorageClass>string</StorageClass>
  </Contents>
  <CommonPrefixes>
    <Prefix>string</Prefix>
  </CommonPrefixes>
</ListBucketResult>
```

具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
ListBucketResult|无|保存 Get Bucket 请求结果的所有信息|Container|是

Container 节点 ListBucketResult 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
Name|ListBucketResult|说明 Bucket 的信息|string|是
Encoding-Type|ListBucketResult|编码格式|string|是
Prefix|ListBucketResult|前缀匹配，用来规定响应请求返回的文件前缀地址|string|是
Marker|ListBucketResult|默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始|string|是
MaxKeys|ListBucketResult|单次响应请求内返回结果的最大的条目数量|string|是
IsTruncated|ListBucketResult|响应请求条目是否被截断，布尔值：true，false|boolean|是
NextMarker|ListBucketResult|假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点|string|是
Contents|ListBucketResult|元数据信息|Container|是
CommonPrefixes|ListBucketResult|将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix|Container|是
Container 节点 Contents 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
Key|ListBucketResult.Contents|Object 的 Key|string|是
LastModified|ListBucketResult.Contents|说明 Object 最后被修改时间|string|是
ETag|ListBucketResult.Contents|文件的 MD-5 算法校验值|string|是
Size|ListBucketResult.Contents|说明文件大小，单位是 Byte|string|是
Owner|ListBucketResult.Contents|Bucket 持有者信息|Container|是
StorageClass|ListBucketResult.Contents|Object 的存储级别，枚举值：STANDARD，STANDARD_IA，ARCHIVE|string|是
Container 节点 Owner 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
ID|ListBucketResult.Contents.Owner|Bucket 的 AppID|string|是
Container 节点 CommonPrefixes 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
Prefix|ListBucketResult.CommonPrefixes|单条 Common 的前缀|string|是


### 错误码
该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 章节。

## 实际案例

### 请求

```
GET / HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Oct 2014 22:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213451;32557109451&q-key-time=1484213451;32557109451&q-header-list=host&q-url-param-list=&q-signature=0336a1fc8350c74b6c081d4dff8e7a2db9007dc
```

### 响应

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1132
Connection: keep-alive
Vary: Accept-Encoding
Date: Wed, 18 Oct 2014 22:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRjY2VfYmRjMzVfMTc5M182MmIyNg==

<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
    <Name>zuhaotestnorth-1251668577</Name>
    <Encoding-Type>url</Encoding-Type>
    <Prefix>ela</Prefix>
    <Marker/>
    <MaxKeys>1000</MaxKeys>
    <Delimiter>/</Delimiter>
    <IsTruncated>false</IsTruncated>
    <NextMarker>1234.txt</NextMarker>
    <Contents>
        <Key>testL</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>\"79f2a852fac7e826c9f4dbe037f8a63b\"</ETag>
        <Size>10485760</Size>
        <Owner>
            <ID>1252375641</ID>
        </Owner>
    <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testL1</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>\"3f9a5dbff88b25b769fa6304902b5d9d\"</ETag>
        <Size>10485760</Size>
        <Owner>
            <ID>1252375642</ID>
        </Owner>
    <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testLLL</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>\"39bfb88c11c65ed6424d2e1cd4db1826\"</ETag>
        <Size>10485760</Size>
        <Owner>
            <ID>1252375643</ID>
        </Owner>
    <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testLOL</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>\"fb31459ad10289ff49327fd91a3e1f6a\"</ETag>
        <Size>4</Size>
        <Owner>
            <ID>1252375644</ID>
        </Owner>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
</ListBucketResult>
```


