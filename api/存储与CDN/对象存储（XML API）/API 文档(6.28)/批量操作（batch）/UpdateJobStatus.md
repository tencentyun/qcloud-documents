## 功能描述

UpdateJobStatus 用于更新任务状态。您可以使用这一接口以启动一项任务或者取消一项正在进行的任务。有关批量处理任务的详细介绍，可参见 [批量处理概述](https://cloud.tencent.com/document/product/436/38601)。

## 请求

**请求示例**

```shell
POST /jobs/<JobId>/status?requestedJobStatus=<RequestedJobStatus>&statusUpdateReason=<StatusUpdateReason> HTTP/1.1
x-cos-appid: <appid>
```

**请求参数**

调用 UpdateJobStatus 需要使用清单任务名称的参数。该参数格式如下：

| 参数               | 描述                                                         | 是否必选 |
| ------------------ | ------------------------------------------------------------ | ---- |
| JobId              | 您想要更新的批量处理任务的 ID。                              | 是   |
| requestedJobStatus | 您期望的批量处理任务的状态。当您将任务转移至`Ready`状态时，COS 将认为您已确认此项任务，并将执行此项任务。当您将任务转移至`Cancelled`状态时，COS 将取消此项任务。可选参数包括：Ready、Cancelled。 | 是   |
| statusUpdateReason | 更新任务状态的原因。此项参数长度限制为0 - 256字节。            | 否   |
| x-cos-appid        | 用户的 APPID，长度为1 - 64字节。                                     | 是   |

**请求头**

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

**请求体**

该请求无请求体。

## 响应

**响应示例**

```shell
HTTP/1.1 200
<UpdateJobStatusResult>
    <JobId>string</JobId>
    <Status>string</Status>
    <StatusUpdateReason>string</StatusUpdateReason>
</UpdateJobStatusResult>
```

**响应头**
此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**响应体**

```shell
<UpdateJobStatusResult>
   <JobId>string</JobId>
   <Status>string</Status>
   <StatusUpdateReason>string</StatusUpdateReason>
</UpdateJobStatusResult>
```

具体内容描述如下。

#### UpdateJobStatusResult

| 节点名             | 父节点                | 描述                                                         | 类型   |
| ------------------ | --------------------- | ------------------------------------------------------------ | ------ |
| JobId              | UpdateJobStatusResult | 任务 ID。您所更新的任务的 ID，长度限制为5 - 36字节。            | String |
| Status             | UpdateJobStatusResult | 任务的当前状态。合法参数项包括：Active、Cancelled、Cancelling、 Complete、Completing、Failed、Failing、New、Paused、Pausing、Preparing、Ready、 Suspended。 | String |
| StatusUpdateReason | UpdateJobStatusResult | 任务更新原因。长度限制为0 - 256字节。                          | String |

## 错误分析

该请求可能会发生的一些常见的特殊错误如下：

| 错误代码        | 描述                                                     | 状态码 | API                               |
| --------------- | -------------------------------------------------------- | ------ | --------------------------------- |
| InvalidArgument | requestedJobStatus 参数必须为 Cancelled 或 Ready             | 400    | UpdateJobStatus                   |
| InvalidRequest  | 指定任务已完成                 | 400    | UpdateJobStatus                   |
| InvalidRequest  | 任务状态变更错误                                         | 400    | UpdateJobStatus                   |
| NoSuchJob       | 指定任务不存在或已完成 | 404    | UpdateJobStatus，UpdateJobPriority |

其他错误请参见 [批量处理功能错误响应](https://cloud.tencent.com/document/product/436/38610)。


