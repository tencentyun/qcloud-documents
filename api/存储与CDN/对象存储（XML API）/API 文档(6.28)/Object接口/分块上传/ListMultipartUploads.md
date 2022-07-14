## 功能描述
List Multipart Uploads 用于查询正在进行中的分块上传任务。单次请求操作最多列出1000个正在进行中的分块上传。

>! 该请求需要有存储桶的读权限。
>

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=ListMultipartUploads&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>

## 请求
#### 请求示例

```shell
GET /?uploads HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求参数

具体内容如下：<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

| 名称               | 描述                                       | 类型     | 是否必选   |
| ---------------- | ---------------------------------------- | ------ | ---- |
| delimiter        | 定界符为一个符号，对 Object 名字包含指定前缀且第一次出现 delimiter 字符之间的 Object 作为一组元素：common prefix。若无 prefix，则从路径起点开始。 | String | 否    |
| encoding-type    | 规定返回值的编码格式，合法值：url。                               | String | 否    |
| prefix           | 限定返回的 Object key 必须以 Prefix 作为前缀。</br>注意使用 prefix 查询时，返回的 key 中仍会包含 Prefix。 | String | 否    |
| max-uploads      | 设置最大返回的 multipart 数量，合法取值从1到1000，默认1000。                       | String | 否    |
| key-marker       | 与 upload-id-marker 一起使用：<Br/><li>当 upload-id-marker 未被指定时，ObjectName 字母顺序大于 key-marker 的条目将被列出。<Br/><li>当 upload-id-marker 被指定时，ObjectName 字母顺序大于 key-marker 的条目被列出，ObjectName 字母顺序等于 key-marker 同时 UploadId 大于 upload-id-marker 的条目将被列出。 | String | 否    |
| upload-id-marker | 与 key-marker 一起使用：<Br/><li>当 key-marker 未被指定时，upload-id-marker 将被忽略。<Br/><li>当 key-marker 被指定时，ObjectName字母顺序大于 key-marker 的条目被列出，ObjectName 字母顺序等于 key-marker 同时 UploadId 大于 upload-id-marker 的条目将被列出。 | String | 否    |

#### 请求体
该请求的请求体为空。

## 响应

#### 响应头
此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
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
    <UploadId></UploadId>
    <StorageClass></StorageClass>
    <Initiator>
      <ID></ID>
	<DisplayName></DisplayName>
    </Initiator>
    <Owner>
      <ID></ID>
	<DisplayName></DisplayName>
    </Owner>
    <Initiated></Initiated>
  </Upload>
  <CommonPrefixes>
    <Prefix></Prefix>
  </CommonPrefixes>
</ListMultipartUploadsResult>
```

具体的节点描述如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| ListMultipartUploadsResult |无| 用来表述所有分块上传的信息。 | Container |

Container 节点 ListMultipartUploadsResult 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Bucket | ListMultipartUploadsResult | 分块上传的目标 Bucket，由用户自定义字符串和系统生成 APPID 数字串由中划线连接而成，例如`examplebucket-1250000000`。|  String |
| Encoding-Type | ListMultipartUploadsResult | 规定返回值的编码格式，合法值：url。 |  String |
| KeyMarker | ListMultipartUploadsResult| 列出条目从该 key 值开始。 |  String |
| UploadIdMarker | ListMultipartUploadsResult | 列出条目从该 UploadId 值开始。 |  String |
| NextKeyMarker | ListMultipartUploadsResult | 假如返回条目被截断，则返回的 NextKeyMarker 就是下一个条目的起点。 | String |
| NextUploadIdMarker | ListMultipartUploadsResult | 假如返回条目被截断，则返回的 UploadId 就是下一个条目的起点。 |  String |
| MaxUploads | ListMultipartUploadsResult | 设置最大返回的 multipart 数量，合法取值从0 - 1000。 |  String |
| IsTruncated | ListMultipartUploadsResult | 返回条目是否被截断，布尔值：TRUE，FALSE。 |  Boolean |
| Prefix | ListMultipartUploadsResult | 限定返回的 Objectkey 必须以 Prefix 作为前缀，</br>注意使用 prefix 查询时，返回的 key 中仍会包含 Prefix。 |  String |
| Delimiter | ListMultipartUploadsResult | 定界符为一个符号，对 object 名字包含指定前缀且第一次出现 delimiter 字符之间的 object 作为一组元素：common prefix。若无 prefix，则从路径起点开始。 |  String |
| Upload | ListMultipartUploadsResult  | 每个 Upload 的信息。 |  Container |
| CommonPrefixes | ListMultipartUploadsResult | 将 prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix。 |  Container |

Container 节点 Upload 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Key | ListMultipartUploadsResult.Upload |  Object 的名称。 |  String |
| UploadId | ListMultipartUploadsResult.Upload |  标示本次分块上传的 ID。 | String |
| StorageClass | ListMultipartUploadsResult.Upload |  用来表示分块的存储级别，枚举值：STANDARD，STANDARD_IA，ARCHIVE。 |  String |
| Initiator | ListMultipartUploadsResult.Upload |  用来表示本次上传发起者的信息。 |  Container |
| Owner | ListMultipartUploadsResult.Upload | 用来表示这些分块所有者的信息。 |  Container |
| Initiated | ListMultipartUploadsResult.Upload |  分块上传的起始时间。 |  Date |

Container 节点 Initiator 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| ID | ListMultipartUploadsResult.Upload.Initiator | 用户唯一的 CAM 身份 ID。 | String  |
| DisplayName | ListMultipartUploadsResult.Upload.Initiator | 用户身份 ID 的简称（UIN）。 | String  |

Container 节点 Owner 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| ID | ListMultipartUploadsResult.Upload.Owner | 用户唯一的 CAM 身份 ID。  | String    |
| DisplayName | ListMultipartUploadsResult.Upload.Owner| 用户身份 ID 的简称（UIN）。 | String  |

Container 节点 CommonPrefixes 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Prefix | ListMultipartUploadsResult.CommonPrefixes | 显示具体的 CommonPrefixes。 | String    |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
GET /?uploads HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Jan 2015 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUj****&q-sign-time=1484727508;32557623508&q-key-time=1484727508;32557623508&q-header-list=host&q-url-param-list=uploads&q-signature=5bd4759a7309f7da9a0550c224d8c61589c9****
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1203
Date: Wed, 18 Jan 2015 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjI0ZGRfNDQyMDRlXzNhZmRf****

<ListMultipartUploadsResult>
    <Bucket>examplebucket-1250000000</Bucket>
    <Encoding-Type/>
    <KeyMarker/>
    <UploadIdMarker/>
    <MaxUploads>1000</MaxUploads>
    <Prefix/>
    <Delimiter>/</Delimiter>
    <IsTruncated>false</IsTruncated>
    <Upload>
        <Key>Object</Key>
        <UploadId>1484726657932bcb5b17f7a98a8cad9fc36a340ff204c79bd2f51e7dddf0b6d1da6220520c</UploadId>
        <Initiator>
           <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
        </Initiator>
        <Owner>
           <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
        </Owner>
        <StorageClass>Standard</StorageClass>
        <Initiated>Wed Jan 18 16:04:17 2017</Initiated>
    </Upload>
    <Upload>
        <Key>Object</Key>
        <UploadId>1484727158f2b8034e5407d18cbf28e84f754b791ecab607d25a2e52de9fee641e5f60707c</UploadId>
        <Initiator>
           <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
        </Initiator>
        <Owner>
           <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
        </Owner>
        <StorageClass>Standard</StorageClass>
        <Initiated>Wed Jan 18 16:12:38 2017</Initiated>
    </Upload>
    <Upload>
        <Key>exampleobject</Key>
        <UploadId>1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e</UploadId>
        <Initiator>
           <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
        </Initiator>
        <Owner>
           <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
		<DisplayName>100000000001</DisplayName>
        </Owner>
        <StorageClass>Standard</StorageClass>
        <Initiated>Wed Jan 18 16:14:30 2017</Initiated>
    </Upload>
</ListMultipartUploadsResult>
```
