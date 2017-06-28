## 功能描述
Get Bucket 请求等同于 List Object 请求，可以列出该 Bucket 下的部分或者全部 Object。此 API 调用者需要对 Bucket 有 Read 权限。

## 请求

语法示例：
```
GET / HTTP/1.1
Host: <BucketName>-<AppID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

> Authorization: Auth (详细参见 [访问控制](http://gggggggg) 章节)

### 请求行
~~~
GET / HTTP/1.1
~~~
该 API 接口接受 GET 请求。

### 请求头

**公共头部**
该请求操作的实现使用公共请求头,了解公共请求头详细请参见[公共请求头部](https://www.qcloud.com/document/product/436/7728)章节。
发起 Get Bucket（ List Object ）请求时，可以通过请求头帯参数：prefix，marker，delimiter 和 max-keys 对 list 做限定用以返回部分结果。另外，可以通过 encoding-type 对返回结果中的 Delimiter、Marker、Prefix、NextMarker 和 Key 这些元素进行编码。
参数具体描述内容如下:

|参数名称|描述|
|:---|:-- |
| prefix |前缀匹配，用来规定返回的文件前缀地址|
| delimiter |定界符为一个符号，如果有 Prefix，则将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix，然后列出所有 Common Prefix。如果没有 Prefix，则从路径起点开始 |
| encoding-type |规定返回值的编码方式，可选值：url |
| marker |默认以 UTF-8 二进制顺序列出条目，所有列出条目从marker开始|
| max-keys |单次返回最大的条目数量，默认1000|

**非公共头部**
该请求操作无特殊的请求头部信息。
### 请求体
该请求的请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见[公共响应头部](https://www.qcloud.com/document/product/436/7729)章节。
**特有响应头**
该响应无特殊有响应头。
#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```
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

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| ListBucketResult |无| 保存 Get Bucket 请求结果的所有信息 | Container |

Container 节点   ListBucketResult 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Name | ListBucketResult | 说明 Bucket 的信息 |  String |
| Prefix | ListBucketResult | 前缀匹配，用来规定响应请求返回的文件前缀地址 |  String |
| Marker | ListBucketResult | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始 |  String |
| MaxKeys | ListBucketResult | 单次响应请求内返回结果的最大的条目数量 |  String |
| IsTruncated | ListBucketResult | 响应请求条目是否被截断，布尔值：TRUE，FALSE | Boolean |
| Contents | ListBucketResult | 元数据信息 | Container |
| CommonPrefixes | ListBucketResult | 将 Prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix | Container |

Container 节点 Contents 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Key | ListBucketResult.Contents | Object 的 Key |  String |
| LastModified | ListBucketResult.Contents | 说明 Object 最后被修改时间 |  Date |
| ETag | ListBucketResult.Contents | 文件的 SHA-1 算法校验值 |  String |
| Size | ListBucketResult.Contents | 说明文件大小，单位是 Byte |  String |
| Owner | ListBucketResult.Contents | Bucket 持有者信息| Container |
| StorageClass | ListBucketResult.Contents | Object 的存储级别，枚举值：Standard，Standard_IA，Nearline | String |

Container 节点 CommonPrefixes 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Prefix |  ListBucketResult.Contents.CommonPrefixes | 单条 Common 的前缀  | Container    |

Container 节点 Owner 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| ID | ListBucketResult.Contents.Owner | Bucket 的 AppID  | Container    |



## 实际案例

### 请求
```
GET / HTTP/1.1
Host: zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213451;32557109451&q-key-time=1484213451;32557109451&q-header-list=host&q-url-param-list=&q-signature=0336a1fc8350c74b6c081d4dff8e7a2db9007dce
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1132
Connection: keep-alive
Vary: Accept-Encoding
Date: Thu Jan 12 17:30:54 2017 GMT
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
        <Owner>
			<ID>1252375641</ID>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testL1</Key>
        <LastModified>Wed Jan 11 19:02:17 2017</LastModified>
        <ETag>"3f9a5dbff88b25b769fa6304902b5d9d"</ETag>
        <Size>10485760</Size>
        <Owner>
			<ID>1252375642</ID>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testLLL</Key>
        <LastModified>Wed Jan 11 16:36:08 2017</LastModified>
        <ETag>"39bfb88c11c65ed6424d2e1cd4db1826"</ETag>
        <Size>10485760</Size>
        <Owner>
			<ID>1252375643</ID>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>testLOL</Key>
        <LastModified>Wed Jan 11 17:24:10 2017</LastModified>
        <ETag>"fb31459ad10289ff49327fd91a3e1f6a"</ETag>
        <Size>4</Size>
        <Owner>
			<ID>1252375644</ID>
		</Owner>
		<StorageClass>STANDARD</StorageClass>
    </Contents>
</ListBucketResult>
```
