## 功能描述

List Bucket Inventory Configurations 用于请求返回一个存储桶中的所有清单任务。每一个存储桶中最多配置1000条清单任务。  

该请求支持列表分页，每页一次最多返回100条清单任务。请确认请求中的 IsTruncated 节点的值，如果 IsTruncated 为 false ，则表明已经将存储桶中的所有清单任务全部列出。如果 IsTruncated 为 true ，且 NextContinuationToken 节点中存在参数值，则您可以将 NextContinuationToken 节点的值传递至 continuation-token 节点中，获取下一分页的清单任务信息。有关清单的详细特性，请查阅 [清单功能概述](https://cloud.tencent.com/document/product/436/33703)。

> !调用该请求时，请确保您有足够的权限对存储桶的清单任务进行操作；存储桶所有者默认拥有该权限，如您无该项权限，请先向存储桶所有者申请该项操作的权限。

## 请求

### 请求示例

```shell
GET /?inventory HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求参数

请求参数格式如下：

| 参数               | 描述                                                         | 类型   | 必选 |
| ------------------ | ------------------------------------------------------------ | ------ | ---- |
| continuation-token | 当 COS 响应体中 IsTruncated 为 true，且 NextContinuationToken 节点中存在参数值时，您可以将这个参数作为 continuation-token 参数值，以获取下一页的清单任务信息<br>缺省值：None | String | 否   |

### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

该请求操作无特殊的请求头部信息。

### 请求体

该请求的请求体为空。

## 响应

### 响应头

#### 公共响应头 

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该响应无特殊的响应头。

### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<ListInventoryConfigurationResult>
    <InventoryConfiguration>
        <Id>list1</Id>
        <IsEnabled>True</IsEnabled>
        <Destination>
            <COSBucketDestination>
                <Format>CSV</Format>
                <AccountId>1250000000</AccountId>
                <Bucket>qcs::cos:ap-beijing::examplebucket-1250000000</Bucket>
                <Prefix>list1</Prefix>
                <SSE-COS></SSE-COS>
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
            <Field>IsMultipartUpload</Field>
            <Field>ReplicationStatus</Field>
        </OptionalFields>
    </InventoryConfiguration>
    <InventoryConfiguration>
        <Id>list2</Id>
        <IsEnabled>True</IsEnabled>
        <Destination>
            <COSBucketDestination>
                <Format>CSV</Format>
                <AccountId>1250000000</AccountId>
                <Bucket>qcs::cos:ap-beijing::examplebucket-1250000000</Bucket>
                <Prefix>list2</Prefix>
                <SSE-COS></SSE-COS>
            </COSBucketDestination>
        </Destination>
        <Schedule>
            <Frequency>Weekly</Frequency>
        </Schedule>
        <Filter>
            <Prefix>myPrefix2</Prefix>
        </Filter>
        <IncludedObjectVersions>All</IncludedObjectVersions>
        <OptionalFields>
            <Field>Size</Field>
            <Field>LastModifiedDate</Field>
            <Field>ETag</Field>
            <Field>StorageClass</Field>
        </OptionalFields>
    </InventoryConfiguration>
    <IsTruncated>false</IsTruncated>
    ------If ContinuationToken was provided in the request---
    <ContinuationToken>...</ContinuationToken>
    <IsTruncated>true</IsTruncated>
    <NextContinuationToken>1ueSDFASDF1Tr/XDAFdadEADadf2J/wm36Hy4vbOwM=</NextContinuationToken>
</ListInventoryConfigurationResult>
```

具体内容描述如下：

| 节点名                               | 父节点                              | 描述                                                         | 类型      |
| ------------------------------------ | ----------------------------------- | ------------------------------------------------------------ | --------- |
| List Inventory Configuration Results | 无                                  | 存储桶中所有清单任务信息的列表                             | Container |
| Inventory Configuration              | ListInventory Configuration Results | 包含清单任务的详细信息，其 XML 结构请参阅 [GET Bucket inventory](https://cloud.tencent.com/document/product/436/33705) | Container |
| IsTruncated                          | ListInventory Configuration Results | 是否已列出所有清单任务信息的标识。如果已经展示完则为 false，否则为 true | Boolean   |
| Continuation Token                   | ListInventory Configuration Results | 当页清单列表的标识，可理解为页数。该标识与请求中的 continuation-token 参数对应 | String    |
| NextContinuation Token               | ListInventory Configuration Results | 下一页清单列表的标识。如果该参数中有值，则可将该值作为 continuation-token 参数并发起 GET 请求以获取下一页清单任务信息 | String    |

## 错误码

该请求不产生特殊报错信息，常见的错误码请参阅 [错误码](https://cloud.tencent.com/document/product/436/7730)文档。

## 实际案例

### 请求

下述请求示例展示了从存储桶 examplebucket-1250000000 中获取清单任务为 list1 的配置信息。

```shell
GET /?inventory HTTP/1.1
Date: Mon, 28 Aug 2018 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1503895278;1503895638&q-key-time=1503895278;1503895638&q-header-list=host&q-url-param-list=inventory&q-signature=f77900be432072b16afd8222b4b349aabd837cb9
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
```

### 响应

请求后，COS 返回以下响应，表明当前该存储桶内存在清单任务 list1 和 list2 。  

**清单任务 list1**

分析存储桶 examplebucket-1250000000 中前缀为 myPrefix 的对象及其所有版本。
分析频次为每天一次。
分析维度包括 Size ， LastModifiedDate，StorageClass， ETag， IsMultipartUploaded，  ReplicationStatus。
分析结果将以 CSV 格式文件存储在存储桶 examplebucket-1250000000 中，文件添加前缀 list1 且用 SSE-COS 加密。  

**清单任务 list2**

分析存储桶 examplebucket-1250000000 中前缀为 myPrefix2 的对象及其所有版本。
分析频次为每周一次；分析的维度包括 Size ， LastModifiedDate ，  StorageClass ， ETag。
分析结果将以 CSV 格式文件存储在存储桶 examplebucket-1250000000 中，文件添加前缀 list2 且用 SSE-COS 加密。  

假设本页有100条清单任务，当 IsTruncated 为 true 时，COS 将会进一步返回 NextContinuationToken ，其中的值可作为 GET 请求中 continuation-token 的参数，以获取下一页信息。

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 331
Date: Mon, 28 Aug 2018 02:53:39 GMT
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF84Y2M
<?xml version = "1.0" encoding = "UTF-8">
<ListInventoryConfigurationResult xmlns = "http://....">
    <InventoryConfiguration>
        <Id>list1</Id>
        <IsEnabled>True</IsEnabled>
        <Destination>
            <COSBucketDestination>
                <Format>CSV</Format>
                <AccountId>1250000000</AccountId>
                <Bucket>qcs::cos:ap-beijing::examplebucket-1250000000</Bucket>
                <Prefix>list1</Prefix>
                <SSE-COS></SSE-COS>
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
            <Field>IsMultipartUpload</Field>
            <Field>ReplicationStatus</Field>
        </OptionalFields>
    </InventoryConfiguration>
    <InventoryConfiguration>
        <Id>list2</Id>
        <IsEnabled>True</IsEnabled>
        <Destination>
            <COSBucketDestination>
                <Format>CSV</Format>
                <AccountId>1250000000</AccountId>
                <Bucket>qcs::cos:ap-beijing::examplebucket-1250000000</Bucket>
                <Prefix>list2</Prefix>
                <SSE-COS></SSE-COS>
            </COSBucketDestination>
        </Destination>
        <Schedule>
            <Frequency>Weekly</Frequency>
        </Schedule>
        <Filter>
            <Prefix>myPrefix2</Prefix>
        </Filter>
        <IncludedObjectVersions>All</IncludedObjectVersions>
        <OptionalFields>
            <Field>Size</Field>
            <Field>LastModifiedDate</Field>
            <Field>ETag</Field>
            <Field>StorageClass</Field>
        </OptionalFields>
    </InventoryConfiguration>
    <IsTruncated>false</IsTruncated>
    ------If ContinuationToken was provided in the request---
    <ContinuationToken>...</ContinuationToken>
    <IsTruncated>true</IsTruncated>
    <NextContinuationToken>1ueSDFASDF1Tr/XDAFdadEADadf2J/wm36Hy4vbOwM=</NextContinuationToken>
</ListInventoryConfigurationResult>
```

