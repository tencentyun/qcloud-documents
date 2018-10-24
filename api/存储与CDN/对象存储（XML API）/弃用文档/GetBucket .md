## 功能描述
GET Bucket 请求等同于 List Object 请求，可以列出该 Bucket 下的部分或者全部 Object。此 API 调用者需要对 Bucket 有 Read 权限。
### 细节分析
1. 每次默认返回的最大条目数为 1000 条，如果无法一次返回所有的 list，则返回结果中的 IsTruncated 为 true，同时会附加一个 NextMarker 字段，提示下一个条目的起点。若一次请求，已经返回了整个 list，则不会有 NextMarker 这个字段，同时 IsTruncated 为 false。
2. 若把 prefix 设置为某个文件夹的全路径名，则可以列出以此 prefix 为开头的文件，即该文件夹下递归的所有文件和子文件夹。如果再设置 delimiter 定界符为 “/”，则只列出该文件夹下的文件，子文件夹下递归的文件和文件夹名将不被列出。而子文件夹名将会以 CommonPrefix 的形式给出。

## 请求

语法示例：
```
GET / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行
~~~
GET / HTTP/1.1
~~~
该 API 接口接受 GET 请求。

#### 请求参数
包含所有请求参数的请求行示例：
```
GET /?prefix=Prefix&delimiter=Delimiter&encoding-type=EncodingType&marker=Marker&max-keys=MaxKeys HTTP/1.1
```
具体内容如下：<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

|参数名称|描述|必选|
|:---|:-- |:--|
| prefix |前缀匹配，用来规定返回的文件前缀地址|否|
| delimiter |定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始 |否|
| encoding-type |规定返回值的编码方式，可选值：url |否|
| marker |默认以 UTF-8 二进制顺序列出条目，所有列出条目从marker开始|否|
| max-keys |单次返回最大的条目数量，默认1000|否|

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

## 响应

### 响应头
#### 公共响应头
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。
### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```
<ListBucketResult>
  <Name></Name>
  <Encoding-Type></Encoding-Type>
  <Prefix></Prefix>
  <Marker></Marker>
  <MaxKeys></MaxKeys>
  <IsTruncated></IsTruncated>
  <NextMarker></NextMarker>
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

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| ListBucketResult |无| 保存 Get Bucket 请求结果的所有信息 | Container |

Container 节点   ListBucketResult 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Name | ListBucketResult |存储桶的名字，由用户自定义字符串和系统生成appid数字串由中划线连接而成，如：mybucket-1250000000|  String |
| Encoding-Type | ListBucketResult | 编码格式 |  String |
| Prefix | ListBucketResult | 前缀匹配，用来规定响应请求返回的文件前缀地址 |  String |
| Marker | ListBucketResult | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始 |  String |
| MaxKeys | ListBucketResult | 单次响应请求内返回结果的最大的条目数量 |  String |
| IsTruncated | ListBucketResult | 响应请求条目是否被截断，布尔值：true，false | Boolean |
| NextMarker | ListBucketResult | 假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点 |  String |
| Contents | ListBucketResult | 元数据信息 | Container |
| CommonPrefixes | ListBucketResult | 将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix | Container |

Container 节点 Contents 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Key | ListBucketResult.Contents | Object 的 Key |  String |
| LastModified | ListBucketResult.Contents | 说明 Object 最后被修改时间 |  Date |
| ETag | ListBucketResult.Contents | 文件的 MD-5 算法校验值 |  String |
| Size | ListBucketResult.Contents | 说明文件大小，单位是 Byte |  String |
| Owner | ListBucketResult.Contents | Bucket 持有者信息| Container |
| StorageClass | ListBucketResult.Contents | Object 的存储级别，枚举值：STANDARD，STANDARD_IA | String |

Container 节点 CommonPrefixes 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Prefix |  ListBucketResult.Contents.CommonPrefixes | 单条 Common 的前缀  | Container    |

Container 节点 Owner 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| ID | ListBucketResult.Contents.Owner | Bucket 的 AppID  | Container    |

### 错误分析
以下描述此请求可能会发生的一些特殊的且常见的错误情况：

|错误码|HTTP状态码|描述|
|-----|------|---------|
|NoSuchBucket|404 Not Found|如果访问的Bucket不存在，则会返回该错误|
|InvalidBucketName|400 Bad Request|请求的Bucket名字不符合规范|
|AccessDenied|403 Forbidden|如果没有访问该Bucket的权限，则会返回该错误|
|InvalidArgument|400 Bad Request|如果max-keys大于1000，则会返回该错误|
|InvalidURI|400 Bad Request|如果prefix、marker或者delimiter的参数不符合要求（必须小于1024），则会返回该错误|

获取更多关于 COS 的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 请求
```
GET / HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Oct 2014 22:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213451;32557109451&q-key-time=1484213451;32557109451&q-header-list=host&q-url-param-list=&q-signature=0336a1fc8350c74b6c081d4dff8e7a2db9007dce
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
        <ETag>"79f2a852fac7e826c9f4dbe037f8a63b"</ETag>
        <Size>10485760</Size>
        <Owner>
	   <ID>1252375641</ID>
	</Owner>
	<StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testL1</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>"3f9a5dbff88b25b769fa6304902b5d9d"</ETag>
        <Size>10485760</Size>
        <Owner>
	  <ID>1252375642</ID>
	 </Owner>
	 <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testLLL</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>"39bfb88c11c65ed6424d2e1cd4db1826"</ETag>
        <Size>10485760</Size>
        <Owner>
	   <ID>1252375643</ID>
	 </Owner>
	 <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testLOL</Key>
        <LastModified>2017-06-23T12:33:26.000Z</LastModified>
        <ETag>"fb31459ad10289ff49327fd91a3e1f6a"</ETag>
        <Size>4</Size>
        <Owner>
	   <ID>1252375644</ID>
	 </Owner>
	 <StorageClass>STANDARD</StorageClass>
    </Contents>
</ListBucketResult>
```
