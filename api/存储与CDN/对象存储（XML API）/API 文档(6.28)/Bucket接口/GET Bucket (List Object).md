## 功能描述
GET Bucket 请求等同于 List Object 请求，可以列出该 Bucket 下的部分或者全部 Object。该 API 的操作者需要对 Bucket 有 Read 权限。

## 请求
### 请求示例

```shell
GET / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
> Authorization: Auth String （详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。
#### 非公共头部
该请求操作无特殊的请求头部信息。

#### 请求参数

名称|类型|描述|必选
---|---|---|---
prefix|string|前缀匹配，用来规定返回的文件前缀地址 |否
delimiter|string|定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始|否
encoding-type|string|规定返回值的编码方式，可选值：url |否
marker|string|默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始|否
max-keys|string|单次返回最大的条目数量，默认值为1000，最大为1000 |否

### 请求体
该请求请求体为空。

## 响应
### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
查询成功，返回 application/xml 数据，包含 Bucket 中的对象信息。

```shell
<?xml version='1.0' encoding='utf-8' ?>
<ListBucketResult>
    <Name>examplebucket-1250000000</Name>
    <Encoding-Type>url</Encoding-Type>
    <Prefix>ela</Prefix>
    <Marker/>
    <MaxKeys>1000</MaxKeys>
    <Delimiter>/</Delimiter>
    <IsTruncated>false</IsTruncated>
    <NextMarker>exampleobject.txt</NextMarker>
    <Contents>
        <Key>photo</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>\"79f2a852fac7e826c9f4dbe037f8a63b\"</ETag>
        <Size>10485760</Size>
        <Owner>
           <ID>1250000000</ID>
        </Owner>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <CommonPrefixes>
      <Prefix>example</Prefix>
    </CommonPrefixes>
</ListBucketResult>
```

具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型
---|---|---|---
ListBucketResult|无|保存 Get Bucket 请求结果的所有信息|Container

**Container 节点 ListBucketResult 内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
Name|ListBucketResult|说明 Bucket 的信息|string
Encoding-Type|ListBucketResult|编码格式|string
Prefix|ListBucketResult|前缀匹配，用来规定响应请求返回的文件前缀地址|string
Marker|ListBucketResult|默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始|string
MaxKeys|ListBucketResult|单次响应请求内返回结果的最大的条目数量|string
Delimiter|ListBucketResult|定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始|string
IsTruncated|ListBucketResult|响应请求条目是否被截断，布尔值：true，false|boolean
NextMarker|ListBucketResult|假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点|string
Contents|ListBucketResult|元数据信息|Container
CommonPrefixes|ListBucketResult|将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix|Container


**Container 节点 Contents 内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|--
Key|ListBucketResult.Contents|Object 的 Key|string
LastModified|ListBucketResult.Contents|说明 Object 最后被修改时间|string
ETag|ListBucketResult.Contents|文件的 MD-5 算法校验值|string
Size|ListBucketResult.Contents|说明文件大小，单位是 Byte|string
Owner|ListBucketResult.Contents|Bucket 持有者信息|Container
StorageClass|ListBucketResult.Contents|Object 的存储级别，枚举值：STANDARD，STANDARD_IA，ARCHIVE|string

**Container 节点 Owner 内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
ID|ListBucketResult.Contents.Owner|Bucket 的 AppID|string


**Container 节点 CommonPrefixes 内容：**

节点名称（关键字）|父节点|描述|类型
---|---|---|---
Prefix|ListBucketResult.CommonPrefixes|单条 Common 的前缀|string


### 错误码
该请求操作无特殊错误信息，常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 请求

```shell
GET / HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Oct 2014 22:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213451;32557109451&q-key-time=1484213451;32557109451&q-header-list=host&q-url-param-list=&q-signature=0336a1fc8350c74b6c081d4dff8e7a2db9007dc
```

### 响应

```shell
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
    <Name>examplebucket-1250000000</Name>
    <Encoding-Type>url</Encoding-Type>
    <Prefix>ela</Prefix>
    <Marker/>
    <MaxKeys>1000</MaxKeys>
    <Delimiter>/</Delimiter>
    <IsTruncated>false</IsTruncated>
    <NextMarker>exampleobject.txt</NextMarker>
    <Contents>
        <Key>photo</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>\"79f2a852fac7e826c9f4dbe037f8a63b\"</ETag>
        <Size>10485760</Size>
        <Owner>
            <ID>1250000001</ID>
        </Owner>
    <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>picture</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>\"3f9a5dbff88b25b769fa6304902b5d9d\"</ETag>
        <Size>10485760</Size>
        <Owner>
            <ID>1250000002</ID>
        </Owner>
    <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>file</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>\"39bfb88c11c65ed6424d2e1cd4db1826\"</ETag>
        <Size>10485760</Size>
        <Owner>
            <ID>1250000003</ID>
        </Owner>
    <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>world</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>\"fb31459ad10289ff49327fd91a3e1f6a\"</ETag>
        <Size>4</Size>
        <Owner>
            <ID>1250000004</ID>
        </Owner>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
</ListBucketResult>
```


