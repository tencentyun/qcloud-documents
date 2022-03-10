本文提供以下批量处理功能的错误响应。

## 失败响应格式

```shell
HTTP/1.1 400
<Error>
    <Code>string</Code>
    <Message>string</Message>
    <Resource>string</Resource>
    <RequestId>string</RequestId>
    <TraceId>string</TraceId>
</Error>
```

## 常见错误代码

| 错误代码           | 描述                                              | 状态码 | API                               |
| ------------------ | ------------------------------------------------- | ------ | --------------------------------- |
| InvalidArgument    | 参数为空                                          | 400    | CreateJob                         |
| InvalidArgument    | 无效参数                                          | 400    | CreateJob                         |
| InvalidArgument    | x-cos-appid 不能为空                               | 400    | Any                               |
| InvalidArgument    | 优先级有效范围为0 - 2147483647的整数               | 400    | CreateJob                         |
| InvalidArgument    | requestedJobStatus 参数状态必须为 Cancelled 或 Ready | 400    | UpdateJobStatus                   |
| InvalidArgument    | jobStatuses 参数无效                              | 400    | ListJobs                          |
| InvalidArgument    | maxResults 参数必须为正整数                       | 400    | ListJobs                          |
| InvalidArgument    | nextToken 参数无效                                | 400    | ListJobs                          |
| InvalidRequest     | 请求不合法                                        | 400    | Any                               |
| InvalidRequest     | 请求体为空                                        | 400    | Any                               |
| InvalidRequest     | 未提供任务 ID                                     | 400    | Any                               |
| InvalidRequest     | 未提供任务优先级                                  | 400    | UpdateJobPriority                 |
| InvalidRequest     | ClientRequestToken 参数重复                       | 400    | CreateJob                         |
| InvalidRequest     | 指定作业已完成                                    | 400    | UpdateJobStatus                   |
| InvalidRequest     | 任务状态变更错误                                  | 400    | UpdateJobStatus                   |
| InternalError      |格式化响应 xml 失败   | 500    | Any                               |
| MalformedXML       | 请求格式不合法                                    | 400    | Any                               |
| MalformedXML       | 提供的 Manifest 格式不正确                        | 400    | CreateJob                         |
| MalformedXML       | 提供的 Operation 格式不正确                       | 400    | CreateJob                         |
| MalformedXML       | 提供的 Report 格式不正确                          | 400    | CreateJob                         |
| NoSuchJob          | 指定作业不存在                                    | 404    | DescribeJob                       |
| NoSuchJob          | 指定作业已完成                                    | 404    | UpdateJobStatus，UpdateJobPriority |
| ServiceUnavailable | 持久化数据错误                                    | 500    | Any                               |
| ServiceUnavailable | 加载持久性数据出错                                | 500    | Any                               |
| ServiceUnavailable | 无法创建新任务                                    | 500    | CreateJob                         |
| TooManyJobs        | 任务已达上限，服务器不可用                        | 500    | CreateJob                         |

