## 功能描述

CreateJob 用于在存储桶中创建批量处理任务。详细信息可参见 [批量处理概述](https://cloud.tencent.com/document/product/436/38601)。

调用该请求时，请确保您有足够的权限对存储桶的对象进行操作。存储桶所有者默认拥有该权限，若您无该项权限，请先向存储桶所有者申请该项操作的权限。

## 请求

#### 请求示例

```shell
POST /jobs HTTP/1.1
x-cos-appid: <appid>
<?xml version="1.0" encoding="UTF-8"?>
<CreateJobRequest>
...
</CreateJobRequest>
```

#### 请求参数

调用 CreateJob 所需的参数。该参数格式如下：

| 参数        | 描述                     | 是否必选 |
| ----------- | ------------------------ | ---- |
| x-cos-appid | 用户的 APPID，长度为1 - 64字节。 | 是   |

#### 请求头
此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体
用户在请求体中使用 XML 语言设置清单任务的具体配置信息。配置信息包括清单任务分析的对象，分析的频次，分析的维度，分析结果的格式及存储的位置等信息。

```shell
<CreateJobRequest>
    <ClientRequestToken>string</ClientRequestToken>
    <ConfirmationRequired>boolean</ConfirmationRequired>
    <Description>string</Description>
    <Manifest>
        <Location>
            <ETag>string</ETag>
            <ObjectArn>string</ObjectArn>
            <ObjectVersionId>string</ObjectVersionId>
        </Location>
        <Spec>
            <Fields>
                <member>string</member>
                <member>string</member>
            </Fields>
            <Format>string</Format>
        </Spec>
    </Manifest>
    <Operation>
        <COSPutObjectCopy>
            <AccessControlGrants>
                <COSGrant>
                    <Grantee>
                        <Identifier>string</Identifier>
                        <TypeIdentifier>string</TypeIdentifier>
                    </Grantee>
                    <Permission>string</Permission>
                </COSGrant>
                <COSGrant>
                    <Grantee>
                        <Identifier>string</Identifier>
                        <TypeIdentifier>string</TypeIdentifier>
                    </Grantee>
                    <Permission>string</Permission>
                </COSGrant>
            </AccessControlGrants>
            <CannedAccessControlList>string</CannedAccessControlList>
            <MetadataDirective>string</MetadataDirective>
            <ModifiedSinceConstraint>timestamp</ModifiedSinceConstraint>
            <UnModifiedSinceConstraint>timestamp</UnModifiedSinceConstraint>
            <NewObjectMetadata>
                <CacheControl>string</CacheControl>
                <ContentDisposition>string</ContentDisposition>
                <ContentEncoding>string</ContentEncoding>
                <ContentType>string</ContentType>
                <HttpExpiresDate>timestamp</HttpExpiresDate>
                <SSEAlgorithm>string</SSEAlgorithm>
                <UserMetadata>
                    <member>
                        <Key>string</Key>
                        <Value>string</Value>
                    </member>
                    <member>
                        <Key>string</Key>
                        <Value>string</Value>
                    </member>
                </UserMetadata>
            </NewObjectMetadata>
            <StorageClass>string</StorageClass>
            <TargetResource>string</TargetResource>
        </COSPutObjectCopy>
    </Operation>
    <Priority>integer</Priority>
    <Report>
        <Bucket>string</Bucket>
        <Enabled>boolean</Enabled>
        <Format>string</Format>
        <Prefix>string</Prefix>
        <ReportScope>string</ReportScope>
    </Report>
    <RoleArn>string</RoleArn>
</CreateJobRequest>
```

请求体内相关元素的具体描述如下。其他元素请参见 [CommonElements](https://cloud.tencent.com/document/product/436/38607)。



| 节点名               | 父节点           | 描述                                                         | 类型             | 是否必选 |
| -------------------- | ---------------- | ------------------------------------------------------------ | ---------------- | -------- |
| ClientRequestToken   | CreateJobRequest | 每个请求唯一的 token，用于避免前端重复发起同一批处理任务。长度为1 - 64字节，建议使用 uuid。 | String           | 是       |
| ConfirmationRequired | CreateJobRequest | 是否在执行任务前进行确认。缺省项为 false。                   | Boolean          | 否       |
| Description          | CreateJobRequest | 任务描述。若您在创建任务时配置了此信息，则会返回该项内容。描述长度范围为0 - 256字节。 | String           | 否       |
| Manifest             | CreateJobRequest | 待处理的对象清单。您需要将需要处理的对象记录在此对象清单内。 | Manifest Object  | 是       |
| Operation            | CreateJobRequest | 您需要对清单内的对象批量执行的操作。目前 COS 支持的操作为`PUT Object-Copy`操作，您可以据此批量复制桶内的存量数据。 | Operation Object | 是       |
| Priority             | CreateJobRequest | 任务优先级。越高的数值代表此项任务的优先级越高。优先级数值范围为0 - 2147483647。 | Integer          | 是       |
| Report               | CreateJobRequest | 任务完成报告。您可配置此参数以在任务完成时输出报告，方便审计任务执行状况。 | Report Object    | 是       |
| RoleArn              | CreateJobRequest | COS 资源标识符，此处用于标识您创建的角色。您需要此资源标识符以验证您的身份。 | String           | 是       |

## 响应

**响应头**

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**响应体**

```shell
<CreateJobResult>
   <JobId>string</JobId>
</CreateJobResult>
```

具体内容描述如下：

| 节点名 | 父节点          | 描述                                                         | 类型   |
| ------ | --------------- | ------------------------------------------------------------ | ------ |
| JobId  | CreateJobResult | 任务 ID。当您成功创建一项任务后，COS 自动返回的 ID，长度1 - 64字节。 | String |

**错误分析**

该请求操作可能会出现如下错误信息。其他错误请参见 [批量处理功能错误响应](https://cloud.tencent.com/document/product/436/38610)。

| 错误代码           | 描述                                      | 状态码 | API       |
| ------------------ | ----------------------------------------- | ------ | --------- |
| InvalidRequest     | 重复的请求                                | 400    | CreateJob |
| InvalidRequest     | 优先级的有效范围是0 - 2147483647的整数     | 400    | CreateJob |
| MalformedXML       | 请求体的 XML Manifest 字段不符合 XML 语法  | 400    | CreateJob |
| MalformedXML       | 请求体的 XML Operation 字段不符合 XML 语法 | 400    | CreateJob |
| MalformedXML       | 请求体的 XML Report 字段不符合 XML 语法    | 400    | CreateJob |
| ServiceUnavailable | 服务暂不可用，无法建立新的任务            | 500    | CreateJob |
| TooManyJobs        | 任务已达上限，服务器不可用              | 500    | CreateJob |



## 实际案例

#### 请求

```shell
POST /jobs HTTP/1.1
x-cos-appid: 1250000000
<?xml version="1.0" encoding="UTF-8"?>
<CreateJobRequest>
    <ClientRequestToken>1829b6c7-3141-42f1-9fe4-17082b841646</ClientRequestToken>
    <ConfirmationRequired>false</ConfirmationRequired>
    <Description>example job</Description>
    <Manifest>
        <Location>
            <ETag>ec75a30f3af000e9b31d62bed75cbcad</ETag>
            <ObjectArn>qcs::cos:ap-chengdu::manifest-1250000000/1250000000/source/manifest/20190715/manifest.json</ObjectArn>
        </Location>
        <Spec>
            <Format>COSInventoryReport_CSV_V1</Format>
        </Spec>
    </Manifest>
    <Operation>
        <COSPutObjectCopy>
            <MetadataDirective>Copy</MetadataDirective>
            <StorageClass>STANDARD</StorageClass>
            <TargetResource>qcs::cos:ap-chengdu::target-1250000000</TargetResource>
        </COSPutObjectCopy>
    </Operation>
    <Priority>10</Priority>
    <Report>
        <Bucket>qcs::cos:ap-beijing::result-1250000000</Bucket>
        <Enabled>true</Enabled>
        <Format>Report_CSV_V1</Format>
        <Prefix>example-job-result</Prefix>
        <ReportScope>AllTasks</ReportScope>
    </Report>
    <RoleArn>qcs::cam::uin/100000000001:roleName/examplerole</RoleArn>
</CreateJobRequest>
```

#### 响应

上述请求后，COS 返回以下响应，表明该清单任务已经成功设置完毕。

```shell
HTTP/1.1 200
<CreateJobResult>
   <JobId>65f2e4cf-83f5-42f1-9aa2-14720613da29</JobId>
</CreateJobResult>
```

