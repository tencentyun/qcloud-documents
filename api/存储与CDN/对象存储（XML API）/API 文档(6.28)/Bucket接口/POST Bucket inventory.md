## 功能描述

POST Bucket inventory 用于在一个存储桶中创建一个一次性清单任务。该接口与 PUT Bucket inventory 有所区别，这个清单任务创建后将立即开始执行，并且每个任务只会执行一次，而不会周期性地重复执行。通过使用此接口，您能够以更加灵活的方式获取到存储桶中的对象清单，进而更精细化地管理对象。

> !
> - 您必须在目标存储桶中写入存储桶策略，以供 COS 将清单任务的结果文件写入该存储桶中。
> - 调用该请求时，请确保您有足够的权限对存储桶的清单任务进行操作。存储桶所有者默认拥有该权限，若您无该项权限，请先向存储桶所有者申请该项操作的权限。  
> - 如果您指定了清单投递的前缀，COS 后端会自动在您指定的前缀后边加上`/`。如您指定了`Prefix`作为前缀，则 COS 后端投递的清单报告路径为`Prefix/inventory_report`。
> - 在清单任务未完成前，再次重复提交相同 id 的清单任务，或者使用与周期性清单任务相同的 id，服务端会返回重复清单任务的错误。
> 

## 请求

#### 请求示例

```plaintext
POST /?inventory&id=inventory-configuration-ID HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
Content-MD5: MD5
```

>? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
>

#### 请求参数

调用 POST Bucket inventory 需要使用清单任务名称的参数。该参数格式如下：

| 参数 | 描述                                                         | 类型   | 是否必选 |
| ---- | ------------------------------------------------------------ | ------ | -------- |
| id   | 清单任务的名称。缺省值：None<br>合法字符：`a-z，A-Z，0-9，-，_，.`<br>注意：清单任务 id 建议不要与周期清单任务 id 相同。同一天内不允许提交重复的 id，否则会返回失败。 | String | 是       |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。


#### 请求体

用户在请求体中使用 XML 语言设置清单任务的具体配置信息，示例如下：

>!
>- 区别于传统的周期任务形式的清单规则，一次性清单不允许携带 IsEnabled、Schedule 参数。
>- 其余参数与 [PUT Bucket inventory](https://cloud.tencent.com/document/product/436/33707) 完全一致。  
>

  

```plaintext
<InventoryConfiguration>
    <Id>list1</Id>
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
    <Filter>
    	<And>
        	<Prefix>myPrefix</Prefix>
            <Tag>
                <Key>string</Key>
                <Value>string</Value>
            </Tag>
        </And>
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



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该请求的响应体返回为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例：使用特定前缀过滤对象生成一次性清单

#### 请求

该示例向存储桶`examplebucket-1250000000`中发起一条清单任务。

- 该清单任务分析存储桶中前缀为 myPrefix，且对象标签含有{age:18}的对象及其所有版本。
- 分析维度包括 Size，LastModifiedDate，StorageClass，ETag，Tag。
- 分析结果将以 CSV 格式文件存储在存储桶 inventorybucket-1250000000 中。

```plaintext
POST /?inventory&id=disposable HTTP/1.1
Date: Mon, 28 Aug 2018 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1503888878;1503889238&q-key-time=1503888878;1503889238&q-header-list=host&q-url-param-list=inventory&q-signature=254bf9cd3d6615e89a36ab652437f9d45c5f****
Content-MD5: AAq9nzrpsz5LJ4UEe1f6Q==
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 1024

<?xml version = "1.0" encoding = "UTF-8">
<InventoryConfiguration xmlns = "http://....">
    <Id>disposable</Id>
    <Destination>
        <COSBucketDestination>
            <Format>CSV</Format>
            <AccountId>100000000001</AccountId>
            <Bucket>qcs::cos:ap-guangzhou::inventorybucket-1250000000</Bucket>
        </COSBucketDestination>
    </Destination>
    <Filter>
    	<And>
        	<Prefix>myPrefix</Prefix>
            <Tag>
                <Key>age</Key>
                <Value>18</Value>
            </Tag>
        </And>
    </Filter>
    <IncludedObjectVersions>All</IncludedObjectVersions>
    <OptionalFields>
        <Field>Size</Field>
        <Field>LastModifiedDate</Field>
        <Field>StorageClass</Field>
        <Field>ETag</Field>
        <Field>Tag</Field>
	</OptionalFields>
</InventoryConfiguration>
```

#### 响应

上述请求后，COS 返回以下响应，表明该清单任务已经成功提交。

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Mon, 28 Aug 2018 02:53:38 GMT
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF8****
```

