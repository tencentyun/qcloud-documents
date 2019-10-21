## 功能描述

UpdateJobStatus 用于更新任务状态。您可以使用这一接口以启动一项任务或者取消一项正在进行的任务。有关批量处理任务的详细介绍，可参见 [批量处理概述]()。

## 请求

**请求示例**

```
POST /jobs/<JobId>/priority?priority=<Priority> HTTP/1.1
x-cos-appid: <appid>
```

**请求参数**

调用 UpdateJobPriority 接口所需的参数。该参数格式如下：

| 参数        | 描述                                                 | 必选 |
| ----------- | ---------------------------------------------------- | ---- |
| JobId       | 您想要更新的批量处理任务的 Id。长度限制为1~64字节。  | 是   |
| priority    | 更新后的任务优先级。此项参数大小限制为0~2147483647。 | 是   |
| x-cos-appid | 用户 UIN，长度1-64字节。                             | 是   |

**请求头**

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

**请求体**

该请求无请求体。

## 响应

**响应示例**

```
HTTP/1.1 200
<UpdateJobPriorityResult>
    <JobId>string</JobId>
    <Priority>integer</Priority>
</UpdateJobPriorityResult>
```

**响应头**
此接口仅返回公共响应头部，详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**响应体**

```
<UpdateJobPriorityResult>
    <JobId>string</JobId>
    <Priority>integer</Priority>
</UpdateJobPriorityResult>
```

具体内容描述如下：

**UpdateJobStatusResult**

| 节点名   | 父节点                  | 描述                                             | 类型    |
| -------- | ----------------------- | ------------------------------------------------ | ------- |
| JobId    | UpdateJobPriorityResult | 任务Id。您所更新的任务的Id，长度限制为1~64字节。 | String  |
| Priority | UpdateJobPriorityResult | 任务的当前优先级。大小限制为0~2147483647。       | Integer |

**错误分析**

该请求可能会发生的一些常见的特殊错误如下：

| 错误代码       | 描述                                                     | 状态码 | API                               |
| -------------- | -------------------------------------------------------- | ------ | --------------------------------- |
| InvalidRequest | No priority was provided                                 | 400    | UpdateJobPriority                 |
| NoSuchJob      | The specified job does not exist or was already finished | 404    | UpdateJobStatus,UpdateJobPriority |

其他错误请参考[对象存储批量处理功能错误响应](https://cloud.tencent.com/document/product/***/****)。

