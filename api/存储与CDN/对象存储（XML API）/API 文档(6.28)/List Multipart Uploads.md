## 功能描述
List Multipart Uploads 用来查询正在进行中的分块上传。单次请求操作最多列出 1000 个正在进行中的分块上传。
## 请求

语法示例：
```
GET /?uploads HTTP/1.1
Host: <BucketName>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Authorization: auth
```

> Authorization: Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
GET /?uploads HTTP/1.1
```
该 API 接口接受 GET 请求。

#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 uploads。
在发送该 GET 请求时，可以自定义 COS 响应数据中的一些参数，这些参数包括：

| 名称               | 描述                                       | 类型     | 必选   |
| ---------------- | ---------------------------------------- | ------ | ---- |
| delimiter        | 定界符为一个符号，对 object 名字包含指定前缀且第一次出现 delimiter 字符之间的object作为一组元素：common prefix。如果没有 prefix，则从路径起点开始 | String | 否    |
| encoding-type    | 规定返回值的编码格式，合法值：url                               | String | 否    |
| prefix           | 限定返回的 Object key 必须以 Prefix 作为前缀。</br>注意使用 prefix 查询时，返回的 key 中仍会包含 Prefix                       | String | 否    |
| max-uploads      | 设置最大返回的 multipart 数量，合法取值从1到1000，默认1000                       | String | 否    |
| key-marker       | 与 upload-id-marker 一起使用<Br/>当 upload-id-marker 未被指定时，ObjectName 字母顺序大于 key-marker 的条目将被列出<Br/>当upload-id-marker被指定时，ObjectName 字母顺序大于key-marker的条目被列出，ObjectName 字母顺序等于 key-marker 同时 UploadID 大于 upload-id-marker 的条目将被列出。 | String | 否    |
| upload-id-marker | 与 key-marker 一起使用<Br/>当 key-marker 未被指定时，upload-id-marker 将被忽略<Br/>当 key-marker 被指定时，ObjectName字母顺序大于 key-marker 的条目被列出，ObjectName 字母顺序等于 key-marker 同时 UploadID 大于 upload-id-marker 的条目将被列出。 | String | 否    |

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该响应无特殊的响应头。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```
<ListMultipartUploadsResult>
  <Bucket></Bucket>
  <Encoding-Type></Encoding-Type>
  <KeyMarker></KeyMarker>
  <UploadIdMarker></UploadIdMarker>
  <NextKeyMarker></NextKeyMarker>
  <NextUploadIdMarker></NextUploadIdMarker>
  <MaxUploads></MaxUploads>
  <IsTruncated></IsTruncated>
  <Prefix></Prefix>
  <Delimiter></Delimiter>
  <Upload>
    <Key></Key>
    <UploadID></UploadID>
    <StorageClass></StorageClass>
    <Initiator>
      <UIN></UIN>
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
具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| ListMultipartUploadsResult |无| 用来表述所有分块上传的信息 | Container |

Container 节点 ListMultipartUploadsResult 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Bucket | ListMultipartUploadsResult | 分块上传的目标 Bucket |  String |
| Encoding-Type | ListMultipartUploadsResult | 规定返回值的编码格式，合法值：url |  String |
| KeyMarker | ListMultipartUploadsResult| 列出条目从该 key 值开始 |  String |
| UploadIdMarker | ListMultipartUploadsResult | 列出条目从该 UploadId 值开始 |  String |
| NextKeyMarker | ListMultipartUploadsResult | 假如返回条目被截断，则返回 NextKeyMarker 就是下一个条目的起点 | String |
| NextUploadIdMarker | ListMultipartUploadsResult | 假如返回条目被截断，则返回 UploadId 就是下一个条目的起点 |  String |
| MaxUploads | ListMultipartUploadsResult | 设置最大返回的 multipart 数量，合法取值从 1 到 000 |  String |
| IsTruncated | ListMultipartUploadsResult | 返回条目是否被截断，布尔值：TRUE，FALSE |  Boolean |
| Prefix | ListMultipartUploadsResult | 限定返回的 Object key 必须以 Prefix 作为前缀。</br>注意使用 prefix 查询时，返回的 key 中仍会包含 Prefix |  String |
| Delimiter | ListMultipartUploadsResult | 定界符为一个符号，对 object 名字包含指定前缀且第一次出现 delimiter 字符之间的object作为一组元素：common prefix。如果没有 prefix，则从路径起点开始 |  String |
| Upload | ListMultipartUploadsResult  | 每个 Upload 的信息 |  Container |
| CommonPrefixs | ListMultipartUploadsResult | 将 prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix |  Container |

Container 节点 Upload 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Key | ListMultipartUploadsResult.Upload |  Object 的名称 |  Integer |
| UploadID | ListMultipartUploadsResult.Upload |  标示本次分块上传的 ID | Integer |
| StorageClass | ListMultipartUploadsResult.Upload |  用来表示分块的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE  |  String |
| Initiator | ListMultipartUploadsResult.Upload |  用来表示本次上传发起者的信息 |  Container |
| Owner | ListMultipartUploadsResult.Upload | 用来表示这些分块所有者的信息 |  Container |
| Initiated | ListMultipartUploadsResult.Upload |  分块上传的起始时间 |  Date |

Container 节点 Initiator 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| UIN | ListMultipartUploadsResult.Upload.Initiator | 开发商 APPID | String  |

Container 节点 Owner 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| UID | ListMultipartUploadsResult.Upload.Owner | Object 的持有者 ID  | String    |

Container 节点 CommonPrefixs 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Prefix | ListMultipartUploadsResult.CommonPrefixs | 显示具体的CommonPrefixs | String    |

## 实际案例

### 请求
```
GET /?uploads HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Date: Wed, 18 Jan 2015 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727508;32557623508&q-key-time=1484727508;32557623508&q-header-list=host&q-url-param-list=uploads&q-signature=5bd4759a7309f7da9a0550c224d8c61589c9dbbf

```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1203
Date: Wed, 18 Jan 2015 21:32:00 GMT
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
           <UIN>14847266009/14847266009<UIN/>
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
            <UIN>14847266009/14847266009<UIN/>
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
            <UIN>14847266009/14847266009<UIN/>
        </Initiator>
        <Owner>
            <UID>1251668577</UID>
        </Owner>
        <StorageClass>Standard</StorageClass>
        <Initiated>Wed Jan 18 16:14:30 2017</Initiated>
    </Upload>
</ListMultipartUploadsResult>

```
