## 功能描述

PUT Bucket inventory 用于在存储桶中创建清单任务，您可以对清单任务命名后，使用该请求创建清单任务，详细信息请参见 [清单功能概述](https://cloud.tencent.com/document/product/436/33703)。

> !
> - COS 支持在每个存储桶中创建最多1000条清单任务。
> - 您必须在目标存储桶中写入存储桶策略，以供 COS 将清单任务的结果文件写入该存储桶中。
> - 调用该请求时，请确保您有足够的权限对存储桶的清单任务进行操作。存储桶所有者默认拥有该权限，若您无该项权限，请先向存储桶所有者申请该项操作的权限。  

## 请求

#### 请求示例

```shell
PUT /?inventory&id=inventory-configuration-ID HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
Content-MD5: MD5
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

调用 PUT Bucket inventory 需要使用清单任务名称的参数。该参数格式如下：

| 参数 | 描述                                                         | 类型   | 必选 |
| ---- | ------------------------------------------------------------ | ------ | ---- |
| id   | 清单任务的名称。<br>缺省值：None<br>合法字符：`a-z，A-Z，0-9，-，_，.` | String | 是   |

#### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

该请求操作无特殊的请求头部信息。

#### 请求体

用户在请求体中使用 XML 语言设置清单任务的具体配置信息。配置信息包括清单任务分析的对象，分析的频次，分析的维度，分析结果的格式及存储的位置等信息。 

```shell
<InventoryConfiguration>
    <Id>list1</Id>
    <IsEnabled>True</IsEnabled>
    <Destination>
        <COSBucketDestination>
            <Format>CSV</Format>
            <AccountId>100000000001</AccountId>
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

| 节点名                 | 父节点                 | 描述                                                         | 类型      | 是否必选 |
| ---------------------- | ---------------------- | ------------------------------------------------------------ | --------- | -------- |
| InventoryConfiguration | 无                     | 包含清单的配置参数                                         | Container | 是       |
| Id                     | InventoryConfiguration | 清单的名称，与请求参数中的 id 对应                         | Container | 是       |
| IsEnabled              | InventoryConfiguration | 清单是否启用的标识。如果设置为 True，清单功能将生效；如果设置为 False，将不生成任何清单 | String    | 是       |
| IncludedObjectVersions | InventoryConfiguration | 是否在清单中包含对象版本<br>如果设置为 All，清单中将会包含所有对象版本，并在清单中增加 VersionId，IsLatest，DeleteMarker 这几个字段<br>如果设置为 Current，则清单中不包含对象版本信息 | String    | 是       |
| Filter                 | InventoryConfiguration | 筛选待分析对象。清单功能将分析符合 Filter 中设置的前缀的对象 | Container | 否       |
| Prefix                 | Filter                 | 需要分析的对象的前缀                                       | String    | 否       |
| OptionalFields         | InventoryConfiguration | 设置清单结果中应包含的分析项目                             | Container | 否       |
| Field                  | OptionalFields         | 清单结果中可选包含的分析项目名称，可选字段包括：Size，LastModifiedDate，StorageClass，ETag，IsMultipartUploaded，ReplicationStatus | String    | 否       |
| Schedule               | InventoryConfiguration | 配置清单任务周期                                           | Container | 是       |
| Frequency              | Schedule               | 清单任务周期，可选项为按日或者按周，枚举值：Daily、Weekly      | String    | 是       |
| Destination            | InventoryConfiguration | 描述存放清单结果的信息                                     | Container | 是       |
| COSBucketDestination   | Destination            | 清单结果导出后存放的存储桶信息                             | Container | 是       |
| Bucket                 | COSBucketDestination   | 清单分析结果的存储桶名                                    | String    | 是       |
| AccountId              | COSBucketDestination   | 存储桶的所有者 ID，例如100000000001                                            | String    | 否       |
| Prefix                 | COSBucketDestination   | 清单分析结果的前缀                                         | String    | 否       |
| Format                 | COSBucketDestination   | 清单分析结果的文件形式，可选项为 CSV 格式                  | String    | 是       |
| Encryption             | COSBucketDestination   | 为清单结果提供服务端加密的选项                             | Container | 否       |
| SSE-COS                | Encryption             | COS 托管密钥的加密方式，无需填充                           | Container | 否       |

## 响应

#### 响应头

#### 公共响应头 

该响应使用公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该请求的响应无特殊的响应头。

#### 响应体

该请求的响应体返回为空。

#### 错误码

该请求可能会发生的一些常见的特殊错误如下，常见的错误码请参见 [错误码](https://cloud.tencent.com/document/product/436/7730)文档。

| 错误码                | 描述                                           | 状态码               |
| --------------------- | ---------------------------------------------- | -------------------- |
| InvalidArgument       | 不合法的参数值                                 | HTTP 400 Bad Request |
| TooManyConfigurations | 清单数量已经达到1000条的上限                 | HTTP 400 Bad Request |
| AccessDenied          | 未授权的访问。您可能不具备访问该存储桶的权限 | HTTP 403 Forbidden   |

## 实际案例

#### 请求

该示例向存储桶 examplebucket-1250000000 中添加一条名为 list1 的清单任务。
- 该清单任务分析存储桶中前缀为 myPrefix 的对象及其所有版本。
- 分析频次为每天一次。
- 分析维度包括 Size ， LastModifiedDate， StorageClass，ETag，IsMultipartUploaded， ReplicationStatus。
- 分析结果将以 CSV 格式文件存储在存储桶 examplebucket-1250000000 中，文件添加前缀 list1 且用 SSE-COS 加密。

```shell
PUT /?inventory&id=list1 HTTP/1.1
Date: Mon, 28 Aug 2018 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1503888878;1503889238&q-key-time=1503888878;1503889238&q-header-list=host&q-url-param-list=inventory&q-signature=254bf9cd3d6615e89a36ab652437f9d45c5f63f9
Content-MD5: AAq9nzrpsz5LJ4UEe1f6Q==
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 1024

<?xml version = "1.0" encoding = "UTF-8">
<InventoryConfiguration xmlns = "http://....">
    <Id>list1</Id>
    <IsEnabled>True</IsEnabled>
    <Destination>
        <COSBucketDestination>
            <Format>CSV</Format>
            <AccountId>100000000001</AccountId>
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

#### 响应

上述请求后，COS 返回以下响应，表明该清单任务 list1 已经成功设置完毕。

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Mon, 28 Aug 2018 02:53:38 GMT
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF84Y2M
```

