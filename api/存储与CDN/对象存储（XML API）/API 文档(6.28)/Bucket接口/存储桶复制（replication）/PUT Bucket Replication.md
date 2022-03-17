## 功能描述

PUT Bucket replication 用于向已启用版本控制的存储桶中配置存储桶复制规则。如果存储桶已经配置了存储桶复制规则，那么该请求会替换现有配置。

> !
>
> - 使用该接口时，需确保存储桶已经开启版本控制，开启版本控制的 API 文档请参见 [PUT Bucket versioning](https://cloud.tencent.com/document/product/436/19889)  接口文档。
> - 开启了多 AZ 配置的存储桶，不支持将多 AZ 存储类型复制为单 AZ 存储类型，例如标准存储（多 AZ）类型不支持复制为标准存储类型。

## 请求

#### 请求示例

```http
PUT /?replication HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-MD5: MD5
Authorization: Auth String
request body
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

用户在请求体中设置存储桶复制的具体配置信息。配置信息包括存储桶复制规则的启用状态、复制内容、目标存储桶的存储桶名和存储区域等信息。

```http
<ReplicationConfiguration>
    <Role>qcs::cam::uin/<OwnerUin>:uin/<SubUin></Role>
    <Rule>
        <Status></Status>
        <ID></ID>
        <Prefix></Prefix>
        <Destination>
            <Bucket>qcs::cos:<Region>::<BucketName-APPID></Bucket>
        </Destination>
    </Rule>
</ReplicationConfiguration>
```

具体内容描述如下：

| 节点名称（关键字）       | 父节点                                    | 描述                                                         | 类型      | 是否必选 |
| ------------------------ | ----------------------------------------- | ------------------------------------------------------------ | --------- | -------- |
| ReplicationConfiguration | 无                                        | 说明所有复制配置信息                                       | Container | 是       |
| Role                     | ReplicationConfiguration                  | 发起者身份标示：`qcs::cam::uin/<OwnerUin>:uin/<SubUin>`      | String    | 是       |
| Rule                     | ReplicationConfiguration                  | 具体配置信息，最多支持1000个                                 | Container | 是       |
| ID                       | ReplicationConfiguration.Rule             | 用来标注具体 Rule 的名称                                     | String    | 否       |
| Status                   | ReplicationConfiguration.Rule             | 标识 Rule 是否生效，枚举值：Enabled, Disabled                | String    | 是       |
| Prefix                   | ReplicationConfiguration.Rule             | 前缀匹配策略，不可重叠，重叠返回错误。前缀匹配根目录为空     | String    | 是       |
| Destination              | ReplicationConfiguration.Rule             | 目标存储桶信息                                               | Container | 是       |
| Bucket                   | ReplicationConfiguration.Rule.Destination | 资源标识符：<br>`qcs::cos:<Region>::<BucketName-APPID>`      | String    | 是       |
| StorageClass             | ReplicationConfiguration.Rule.Destination | 存储类型，枚举值：STANDARD，INTELLIGENT_TIERING，STANDARD_IA。默认值：原存储类型| String    | 否       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

以下 PUT Bucket replication 请求向存储桶`originbucket-1250000000`中添加一条存储桶复制配置。该存储桶复制配置中，指定复制前缀为`testPrefix`的对象内容，目标存储桶为广州的`destinationbucket-1250000000`。

```shell
PUT /?replication HTTP/1.1
Date: Mon, 28 Aug 2017 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1503888878;1503889238&q-key-time=1503888878;1503889238&q-header-list=host&q-url-param-list=replication&q-signature=254bf9cd3d6615e89a36ab652437f9d45c5f****
Content-MD5: AAq9nzrpsz5LJ4UEe1f6Q==
Host: originbucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 312

<ReplicationConfiguration>
    <Role>qcs::cam::uin/100000000001:uin/100000000001</Role>
    <Rule>
        <Status>Enabled</Status>
        <ID>RuleId_01</ID>
        <Prefix>testPrefix</Prefix>
        <Destination>
            <Bucket>qcs::cos:ap-guangzhou::destinationbucket-1250000000</Bucket>
        </Destination>
    </Rule>
</ReplicationConfiguration>
```

#### 响应

上述请求后，COS 返回以下响应，表明当前该跨地域配置已经成功设置完毕。

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 14 Apr 2019 07:06:19 GMT
Server: tencent-cos
x-cos-bucket-region: ap-guangzhou
x-cos-request-id: NWQwMzQ3NmJfMjRiMjU4NjRfOTM4NV82ZDU1****
x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODc0OWRkZjk0ZDM1NmI1M2E2MTRlY2MzZDhmNmI5MWI1OWE4OGMxZjNjY2JiNTBmMTVmMWY1MzAzYzkyZGQ2ZWM4MzUyZTg1NGRhNWY0NTJiOGUyNTViYzgyNzgxZTEwOTY=
```
