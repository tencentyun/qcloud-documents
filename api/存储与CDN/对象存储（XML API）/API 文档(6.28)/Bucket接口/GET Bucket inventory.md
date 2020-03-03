## 功能描述

GET Bucket inventory 接口用于查询存储桶中用户的清单任务信息。用户在发起该请求时，需要用户提供清单任务的名称，发起该请求时需获得请求签名，表明该请求已获得许可。有关清单的详细特性，请参见 [清单功能概述](https://cloud.tencent.com/document/product/436/33703)。

> !
> - 调用该请求时，请确保您有足够的权限对存储桶的清单任务进行操作。
> - 存储桶所有者默认拥有该权限，若您无该项权限，请先向存储桶所有者申请该项操作的权限。
> - 如果您指定了清单投递的前缀，COS 后端会自动在您指定的前缀后边加上`/`。如您指定了`Prefix`作为前缀，则 COS 后端投递的清单报告路径为`Prefix/inventory_report`。

## 请求

#### 请求示例

```shell
GET /?inventory&id=inventory-configuration-ID HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

调用 GET Bucket inventory 需要使用清单任务名称的参数。该参数格式如下：

| 参数 | 描述                                                         | 类型   | 必选 |
| ---- | ------------------------------------------------------------ | ------ | ---- |
| id   | 清单任务的名称。缺省值：None<br/>合法字符：`a-z，A-Z，0-9，-，_，. `| String | 是   |

#### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

该请求操作无特殊的请求头部信息。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

#### 公共响应头 

该响应使用公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该响应无特殊的响应头。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<InventoryConfiguration>
    <Id>list1</Id>
    <IsEnabled>true</IsEnabled>
    <Destination>
        <COSBucketDestination>
            <Format>CSV</Format>
            <AccountId>1250000000</AccountId>
            <Bucket>qcs::cos:ap-guangzhou::examplebucket-1250000000</Bucket>
            <Prefix>list1</Prefix>
            <Encryption>
                <SSE-COS></SSE-COS>
            </Encryption>
        </COSBucketDestination>
    </Destination>
    <Schedule>
        <Frequency>Daily</Frequency>
    </Schedule>
    <Filter>
        <Prefix>myPrefix</Prefix>
    </Filter>
    <IncludedObjectVersions>All</IncludedObjectVersions>
    <OptionalFields>
        <Field>Size</Field>
        <Field>LastModifiedDate</Field>
        <Field>ETag</Field>
        <Field>StorageClass</Field>
        <Field>IsMultipartUploaded</Field>
        <Field>ReplicationStatus</Field>
	</OptionalFields>
</InventoryConfiguration>
```

具体内容描述如下：

| 节点名                  | 父节点                  | 描述                                                         | 类型      |
| ----------------------- | ----------------------- | ------------------------------------------------------------ | --------- |
| Inventory Configuration | 无                      | 包含清单的配置参数                                         | Container |
| Id                      | Inventory Configuration | 清单的名称，与请求参数中的 ID 对应                           | Container |
| IsEnabled               | Inventory Configuration | 清单是否启用的标识：<br><li>如果设置为 true，清单功能将生效<br><li>如果设置为 false，将不生成任何清单 | String    |
| IncludedObject Versions | Inventory Configuration | 是否在清单中包含对象版本：<br><li>如果设置为 All ，清单中将会包含所有对象版本，并在清单中增加 VersionId， IsLatest， DeleteMarker 这几个字段<br><li>如果设置为 Current，则清单中不包含对象版本信息 | String    |
| Filter                  | Inventory Configuration | 筛选待分析对象。清单功能将分析符合 Filter 中设置的前缀的对象 | Container |
| Prefix                  | Filter                  | 需要分析的对象的前缀                                   | String    |
| OptionalFields          | Inventory Configuration | 设置清单结果中应包含的分析维度                            | Container |
| Field                   | OptionalFields          | 清单结果中可选包含的分析维度名称，可选字段包括：  Size， LastModifiedDate，  StorageClass， ETag， IsMultipartUploaded，  ReplicationStatus | String    |
| Schedule                | Inventory Configuration | 配置清单任务周期                                           | Container |
| Frequency               | Schedule                | 清单任务周期，可选项为按日或者按周                         | String    |
| Destination             | Inventory Configuration | 描述存放清单结果的信息                                     | Container |
| COSBucket Destination   | Destination             | 清单结果导出后存放的存储桶信息                             | Container |
| Bucket                  | COSBucket Destination   | 清单分析结果的存储桶名                                    | String    |
| AccountId               | COSBucket Destination   | 存储桶的所有者 ID                                            | String    |
| Prefix                  | COSBucket Destination   | 清单分析结果的前缀                                         | String    |
| Format                  | COSBucket Destination   | 清单分析结果的文件形式，可选项为 CSV 格式和 ORC 格式       | String    |
| Encryption              | COSBucket Destination   | 为清单结果提供服务端加密的选项                             | Container |
| SSE-COS                 | Encryption              | COS 托管密钥的加密方式                                     | Container |

#### 错误码

该请求不产生特殊报错信息，常见的错误码请参见 [错误码](https://cloud.tencent.com/document/product/436/7730)文档。

## 实际案例

#### 请求

下述请求示例展示了从存储桶`examplebucket-1250000000`中获取清单任务为 list1 的配置信息。

```shell
GET /?inventory&id=list1 HTTP/1.1
Date: Mon, 28 Aug 2018 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1503895278;1503895638&q-key-time=1503895278;1503895638&q-header-list=host&q-url-param-list=inventory&q-signature=f77900be432072b16afd8222b4b349aabd837cb9
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
```

#### 响应

上述请求后，COS 返回以下响应，表明当前该存储桶内的清单任务 list1 处于启用状态。
- 该清单任务分析存储桶`examplebucket-1250000000`中前缀为 myPrefix 的对象及其所有版本。
- 分析频次为每天一次。
- 分析维度包括 Size，LastModifiedDate， StorageClass，ETag，IsMultipartUploaded， ReplicationStatus。
- 分析结果将以 CSV 格式文件存储在存储桶 examplebucket-1250000000 中，文件添加前缀 list1 且用 SSE-COS 加密。

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 331
Date: Mon, 28 Aug 2018 02:53:39 GMT
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF84Y2M
<?xml version = "1.0" encoding = "UTF-8">
<InventoryConfiguration xmlns = "http://....">
    <Id>list1</Id>
    <IsEnabled>true</IsEnabled>
    <Destination>
        <COSBucketDestination>
            <Format>CSV</Format>
            <AccountId>1250000000</AccountId>
            <Bucket>qcs::cos:ap-guangzhou::examplebucket-1250000000</Bucket>
            <Prefix>list1</Prefix>
            <Encryption>
                <SSE-COS></SSE-COS>
            </Encryption>
        </COSBucketDestination>
    </Destination>
    <Schedule>
        <Frequency>Daily</Frequency>
    </Schedule>
    <Filter>
        <Prefix>myPrefix</Prefix>
    </Filter>
    <IncludedObjectVersions>All</IncludedObjectVersions>
    <OptionalFields>
        <Field>Size</Field>
        <Field>LastModifiedDate</Field>
        <Field>ETag</Field>
        <Field>StorageClass</Field>
        <Field>IsMultipartUploaded</Field>
        <Field>ReplicationStatus</Field>
	</OptionalFields>
</InventoryConfiguration>
```
