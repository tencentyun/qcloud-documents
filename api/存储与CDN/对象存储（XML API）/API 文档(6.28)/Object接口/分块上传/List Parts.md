## 功能描述

List Parts 用来查询特定分块上传中的已上传的块，即罗列出指定 UploadId 所属的所有已上传成功的分块。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=ListParts&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
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
GET /<ObjectKey>?uploadId=UploadId HTTP/1.1
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

| 名称               | 描述                                                         | 类型   | 是否必选 |
| ------------------ | ------------------------------------------------------------ | ------ | -------- |
| UploadId           | 标识本次分块上传的 ID，使用 Initiate Multipart Upload 接口初始化分块上传时得到的 UploadId | string | 是       |
| encoding-type      | 规定返回值的编码方式                                         | string | 否       |
| max-parts          | 单次返回最大的条目数量，默认1000                             | string | 否       |
| part-number-marker | 默认以  UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始 | string | 否       |

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

查询成功，返回 **application/xml** 数据，包含已完成的分片信息。

```shell
<?xml version="1.0" encoding="UTF-8" ?>
<ListPartsResult>
    <Bucket>examplebucket-1250000000</Bucket>
    <Encoding-type/>
    <Key>exampleobject</Key>
    <UploadId>14846420620b1f381e5d7b057692e131dd8d72dfa28f2633cfbbe4d0a9e8bd0719933545b0</UploadId>
    <Initiator>
        <ID>1250000000</ID>
        <DisplayName>1250000000</DisplayName>
    </Initiator>
    <Owner>
        <ID>qcs::cam::uin/100000000001:uin/100000000001</ID>
        <DisplayName>100000000001</DisplayName>
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

具体的节点描述如下：

| 节点名称（关键字） | 父节点 | 描述                               | 类型      |
| ------------------ | ------ | ---------------------------------- | --------- |
| ListPartsResult    | 无     | 保存 List Parts 请求结果的所有信息 | Container |

Container 节点 ListPartsResult 的内容：

| 节点名称（关键字）   | 父节点          | 描述                                                         | 类型      |
| -------------------- | --------------- | ------------------------------------------------------------ | --------- |
| Bucket               | ListPartsResult | 分块上传的目标 Bucket，存储桶的名字，由用户自定义字符串和系统生成 APPID 数字串由中划线连接而成，如：examplebucket-1250000000 | string    |
| Encoding-Type        | ListPartsResult | 编码格式                                                     | string    |
| Key                  | ListPartsResult | Object 的名称                                                | string    |
| UploadId             | ListPartsResult | 标识本次分块上传的 ID                                        | string    |
| Initiator            | ListPartsResult | 用来表示这些分块所有者的信息                                 | Container |
| Owner                | ListPartsResult | 用来表示这些分块所有者的信息                                 | Container |
| StorageClass         | ListPartsResult | 用来表示这些分块的存储类型，枚举值：STANDARD，STANDARD_IA，ARCHIVE，DEEP_ARCHIVE 等，更多存储类型请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417) | string    |
| PartNumberMarker     | ListPartsResult | 默认以 UTF-8 二进制顺序列出条目，所有列出条目从 marker 开始  | string    |
| NextPartNumberMarker | ListPartsResult | 假如返回条目被截断，则返回 NextMarker 就是下一个条目的起点   | string    |
| MaxParts             | ListPartsResult | 单次返回最大的条目数量                                       | string    |
| IsTruncated          | ListPartsResult | 响应请求条目是否被截断，布尔值：true，false                  | boolean   |
| Part                 | ListPartsResult | 元数据信息                                                   | Container |

Container 节点 Initiator 的内容：

| 节点名称（关键字） | 父节点                    | 描述                 | 类型   |
| ------------------ | ------------------------- | -------------------- | ------ |
| ID                 | ListPartsResult.Initiator | 创建者的一个唯一标识 | string |
| DisplayName        | ListPartsResult.Initiator | 创建者的用户名描述   | string |

Container 节点 Owner 的内容：

| 节点名称（关键字） | 父节点                | 描述                 | 类型   |
| ------------------ | --------------------- | -------------------- | ------ |
| ID                 | ListPartsResult.Owner | 创建者的一个唯一标识 | string |
| DisplayName        | ListPartsResult.Owner | 创建者的用户名描述   | string |

Container 节点 Part 的内容：

| 节点名称（关键字） | 父节点               | 描述                    | 类型   |
| ------------------ | -------------------- | ----------------------- | ------ |
| PartNumber         | ListPartsResult.Part | 块的编号                | string |
| LastModified       | ListPartsResult.Part | 说明块最后被修改时间    | string |
| ETag               | ListPartsResult.Part | 块的 MD-5 算法校验值    | string |
| Size               | ListPartsResult.Part | 说明块大小，单位是 Byte | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。


## 实际案例

#### 请求

```shell
GET /exampleobject?uploadId=1585130821cbb7df1d11846c073ad648e8f33b087cec2381df437acdc833cf654b9ecc6361 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 25 Mar 2020 10:07:25 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1585130845;1585138045&q-key-time=1585130845;1585138045&q-header-list=date;host&q-url-param-list=uploadid&q-signature=ba8d97cefa396d804524a38d7b5412fb0261****
Connection: close
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1119
Connection: close
Date: Wed, 25 Mar 2020 10:07:25 GMT
Server: tencent-cos
x-cos-request-id: NWU3YjJkNWRfMjNhZjJhMDlfNWY5Ml8zMmUy****



<ListPartsResult>
			<Bucket>examplebucket-1250000000</Bucket>
			<EncodingType/>
			<Key>exampleobject</Key>
			<UploadId>1585130821cbb7df1d11846c073ad648e8f33b087cec2381df437acdc833cf654b9ecc6361</UploadId>
			<Owner>
				<ID>1250000000</ID>
				<DisplayName>1250000000</DisplayName>
			</Owner>
			<PartNumberMarker>0</PartNumberMarker>
			<Initiator>
				<ID>qcs::cam::uin/100000000001:uin/100000000011</ID>
				<DisplayName>100000000011</DisplayName>
			</Initiator>
			<Part>
				<PartNumber>1</PartNumber>
				<LastModified>2020-03-25T10:07:14.000Z</LastModified>
				<ETag>&quot;39270a968a357d24207e9911162507eb&quot;</ETag>
				<Size>1048576</Size>
			</Part>
			<Part>
				<PartNumber>2</PartNumber>
				<LastModified>2020-03-25T10:07:13.000Z</LastModified>
				<ETag>&quot;d899fbd1e06109ea2e4550f5751c88d6&quot;</ETag>
				<Size>1048576</Size>
			</Part>
			<Part>
				<PartNumber>3</PartNumber>
				<LastModified>2020-03-25T10:07:13.000Z</LastModified>
				<ETag>&quot;762890d6c9a871b7bd136037cb2260cd&quot;</ETag>
				<Size>1048576</Size>
			</Part>
			<StorageClass>Standard</StorageClass>
			<MaxParts>1000</MaxParts>
			<IsTruncated>false</IsTruncated>
</ListPartsResult>
```
