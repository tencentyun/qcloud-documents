## 功能描述

DescribeJob 用于获取您配置的批量处理任务的参数和任务执行状态。有关批量处理任务的详细信息，可参见 [批量处理概述](https://cloud.tencent.com/document/product/436/38601)。

## 请求

**请求示例**

```shell
GET /jobs/<JobId> HTTP/1.1
x-cos-appid: <appid>
```

**请求参数**

调用 DescribeJob 所需的参数。该参数格式如下：

| 参数        | 描述                     | 是否必选 |
| ----------- | ------------------------ | ---- |
| JobId       | 任务 ID。                | 是   |
| x-cos-appid | 用户的 APPID，长度为1 - 64字节。 | 是   |

**请求头**

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

**请求体**

该请求无请求体。

## 响应

**响应示例**

```shell
HTTP/1.1 200
<DescribeJobResult>
...
</DescribeJobResult>
```

**响应头**

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**响应体**

```shell
<DescribeJobResult>
    <Job>
        <ConfirmationRequired>boolean</ConfirmationRequired>
        <CreationTime>timestamp</CreationTime>
        <Description>string</Description>
        <FailureReasons>
            <JobFailure>
                <FailureCode>string</FailureCode>
                <FailureReason>string</FailureReason>
            </JobFailure>
        </FailureReasons>
        <JobId>string</JobId>
        <Manifest>
            <Location>
                <ETag>string</ETag>
                <ObjectArn>string</ObjectArn>
            </Location>
            <Spec>
                <Format>string</Format>
            </Spec>
        </Manifest>
        <Operation>
            <COSPutObjectCopy>
                <CannedAccessControlList>string</CannedAccessControlList>
                <MetadataDirective>string</MetadataDirective>
                <NewObjectMetadata>
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
        <ProgressSummary>
            <NumberOfTasksFailed>integer</NumberOfTasksFailed>
            <NumberOfTasksSucceeded>integer</NumberOfTasksSucceeded>
            <TotalNumberOfTasks>integer</TotalNumberOfTasks>
        </ProgressSummary>
        <Report>
            <Bucket>string</Bucket>
            <Enabled>boolean</Enabled>
            <Format>string</Format>
            <Prefix>string</Prefix>
            <ReportScope>string</ReportScope>
        </Report>
        <RoleArn>string</RoleArn>
        <Status>string</Status>
        <StatusUpdateReason>string</StatusUpdateReason>
        <SuspendedCause>string</SuspendedCause>
        <SuspendedDate>timestamp</SuspendedDate>
        <TerminationDate>timestamp</TerminationDate>
    </Job>
</DescribeJobResult>
```

具体内容描述如下：

**DescribeJobResult**

包含待描述批量处理任务的参数和状态信息。

| 节点名 | 父节点            | 描述                                       | 类型       |
| ------ | ----------------- | ------------------------------------------ | ---------- |
| Job    | DescribeJobResult | 您指定查询的批量处理任务的参数和状态信息。 | Job Object |

**Job**

| 节点名             | 父节点 | 描述                                                         | 类型                   |
| ------------------ | ------ | ------------------------------------------------------------ | ---------------------- |
| ClientRequestToken | Job    | 每个请求唯一的 token，用于避免前端重复发起同一批处理任务。长度为1 - 64字节，建议使用 UUID。 | String                 |
| CreationTime       | Job    | 任务创建时间。                                               | Timestamp              |
| Description        | Job    | 任务描述。若您在创建任务时配置了此信息，则会返回该项内容。长度范围为1 - 256字节。 | String                 |
| FailureReasons     | Job    | 如果任务失败，描述失败的原因。                               | FailureReasons Object  |
| JobId              | Job    | 创建任务成功后，生成的任务 ID。长度1 - 64字节。                 | String                 |
| Manifest           | Job    | 待处理的对象清单。您需要将需要处理的对象记录在此对象清单内。 | Manifest Object        |
| Operation          | Job    | 您需要对清单内的对象批量执行的操作。                         | Operation Object       |
| Priority           | Job    | 任务优先级。越高的数值代表此项任务的优先级越高。优先级数值范围为0 - 2147483647 | Integer                |
| ProgressSummary    | Job    | 任务执行状况概述。描述您此项任务中所执行的操作总数，成功的操作数量以及失败的操作数量。 | ProgressSummary Object |
| Report             | Job    | 指定清单报告的相关配置。                                     | Report Object          |
| RoleArn            | Job    | 您为该任务分配的角色的标识符。长度1 - 1024字节。               | String                 |
| Status             | Job    | 任务当前状态。合法参数值包括 Active、Cancelled、Cancelling、Complete、Completing、Failed、Failing、New、Paused、Pausing、Preparing、Ready、Suspended | String                 |
| StatusUpdateReason | Job    | 状态更新原因。长度为0 - 256字节。                              | String                 |
| SuspendedCause     | Job    | 任务中断的原因。任务仅在您使用控制台创建任务时会进入中断状态，等待您的确认后再进入执行状态。长度为0 - 1024字节。 | String                 |
| SuspendedDate      | Job    | 任务中断的时间。当任务进入中断状态时，会记录任务中断的时间。 | Timestamp              |
| TerminationDate    | Job    | 任务终止的时间。                                             | Timestamp              |

**FailureReasons**

| 节点名     | 父节点         | 描述                 | 类型              |
| ---------- | -------------- | -------------------- | ----------------- |
| JobFailure | FailureReasons | 任务失败代码和原因。 | JobFailure Object |

**FailureCode**

| 节点名        | 父节点     | 描述                          | 类型   |
| ------------- | ---------- | ----------------------------- | ------ |
| FailureCode   | JobFailure | 任务失败代码。长度0 - 64字节。  | String |
| FailureReason | JobFailure | 任务失败原因。长度0 - 256字节。 | String |

其他元素请参见 [批量处理功能公共元素](https://cloud.tencent.com/document/product/436/38607)。

## 错误分析

该请求可能会发生的一些常见的特殊错误如下，其他错误请参见 [批量处理功能错误响应](https://cloud.tencent.com/document/product/436/38610)。

| 错误代码  | 描述                             | 状态码 | API         |
| --------- | -------------------------------- | ------ | ----------- |
| NoSuchJob | 指定任务不存在 | 404    | DescribeJob |

