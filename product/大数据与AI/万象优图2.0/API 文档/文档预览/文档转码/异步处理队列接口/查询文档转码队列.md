## 功能描述

DescribeDocProcessQueues 接口用于查询文档转码队列。

## 请求

#### 请求示例

```shell
GET /docqueue?pageNumber=1&pageSize=2 HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求的请求体为空。

#### 请求参数

| 名称       | 描述                                                         | 类型   | 是否必选 |
| ---------- | ------------------------------------------------------------ | ------ | -------- |
| queueIds   | 队列 ID，以“,”符号分割字符串                                 | string | 否       |
| state      | 1. Active 表示队列内的作业会被文档预览服务调度执行<br>2. Paused  表示队列暂停，作业不再会被文档预览服务调度执行，队列内的所有作业状态维持在暂停状态，已经处于执行中的任务将继续执行，不受影响 | string | 否       |
| pageNumber | 第几页，默认第一页                                                       | string | 否       |
| pageSize   | 每页个数，默认10个                                                     | string | 否       |



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据。

响应体1：当指定 pageNumber 和 pageSize 时包含完整节点数据的内容展示如下。

```shell
<Response>
        <TotalCount>1</TotalCount>
        <RequestId>RequestId</RequestId>
        <PageNumber>1</PageNumber>
        <PageSize>2</PageSize>
        <QueueList>
                <QueueId>QueueId</QueueId>
                <Name>QueueName</Name>
                <State>Active</State>
                <NotifyConfig>
                        <Url>url</Url>
                        <Event>Event</Event>
                        <Type/></Type>
                        <State>Off</State>
                </NotifyConfig>
                <MaxSize>10000</MaxSize>
                <MaxConcurrent>10</MaxConcurrent>
                <CreateTime>CreateTime</CreateTime>
                <UpdateTime>UpdateTime</UpdateTime>
                <BucketId>BucketId</BucketId>
                <Category>DocProcess</Category>
        </QueueList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                            | 类型      |
| :----------------- | :------- | :------------------------------ | :-------- |
| RequestId          | Response | 请求的唯一 ID                   | String    |
| TotalCount         | Response | 队列总数                        | Int       |
| PageNumber         | Response | 当前页数，同请求中的 pageNumber | Int       |
| PageSize           | Response | 每页个数，同请求中的 pageSize   | Int       |
| QueueList          | Response | 队列数组                        | Container |

Container 节点 QueueList 的内容：

| 节点名称（关键字） | 父节点             | 描述                         | 类型      |
| :----------------- | :----------------- | :--------------------------- | :-------- |
| QueueId            | Response.QueueList | 队列 ID                      | String    |
| Name               | Response.QueueList | 队列名字                     | String    |
| State              | Response.QueueList | 当前状态，Active 或者 Paused | String    |
| NotifyConfig       | Response.QueueList | 回调配置                     | Container |
| MaxSize            | Response.QueueList | 队列最大长度                 | Int       |
| MaxConcurrent      | Response.QueueList | 当前队列最大并行执行的任务数 | Int       |
| UpdateTime         | Response.QueueList | 更新时间                     | String    |
| CreateTime         | Response.QueueList | 创建时间                     | String    |

Container 节点 NotifyConfig 的内容：

| 节点名称（关键字） | 父节点                          | 描述                  | 类型   |
| :----------------- | :------------------------------ | :-------------------- | :----- |
| Url                | Response.QueueList.NotifyConfig | 回调地址              | String |
| State              | Response.QueueList.NotifyConfig | 开关状态，On 或者 Off | String |
| Type               | Response.QueueList.NotifyConfig | 回调类型，Url         | String |
| Event              | Response.QueueList.NotifyConfig | 触发回调的事件        | String |


响应体2：当指定 queueIds 时包含完整节点数据的内容展示如下。

```shell
<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <QueueList>
        <QueueId>A</QueueId>
        <Name></Name>
        <State>Active</State>
        <NotifyConfig>
            <Url></Url>
        </NotifyConfig>
    </QueueList>
    <NonExistPIDs>
        <QueueID>B</QueueID>
        <QueueID>C</QueueID>
    </NonExistPIDs>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                             | 类型      |
| :----------------- | :------- | :------------------------------- | :-------- |
| RequestId          | Response | 请求的唯一 ID                    | String    |
| QueueList          | Response | 队列数组，同上面解释的 QueueList | Container |
| NonExistPIDs       | Response | 不存在的队列 ID 列表             | Container |

Container 节点 NonExistPIDs 的内容：

| 节点名称（关键字） | 父节点                | 描述    | 类型   |
| :----------------- | :-------------------- | :------ | :----- |
| QueueID            | Response.NonExistPIDs | 队列 ID | String |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```plaintext
GET /docqueue?pageNumber=1&pageSize=2 HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: examplebucket-1250000000.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Authorization: Authorization
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 07:29:28 GMT
Content-Type: application/xml
Content-Length: 677
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYxZTgyNTdfYzc2OTQzNjRfMzUx****

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <TotalCount>1</TotalCount>
        <RequestId>NWYxZTgyNTdfYzc2OTQzNjRfMzUx****</RequestId>
        <PageNumber>1</PageNumber>
        <PageSize>2</PageSize>
        <QueueList>
                <QueueId>p2505d57bdf4c4329804b58a6a5fb1572</QueueId>
                <Name>queue-doc-process-1</Name>
                <State>Active</State>
                <NotifyConfig>
                        <Url/>
                        <Event/>
                        <Type/>
                        <State>Off</State>
                </NotifyConfig>
                <MaxSize>10000</MaxSize>
                <MaxConcurrent>10</MaxConcurrent>
                <CreateTime>2020-07-24T22:42:27+0800</CreateTime>
                <UpdateTime>2020-07-24T22:42:27+0800</UpdateTime>
                <BucketId>examplebucket-1250000000.</BucketId>
                <Category>DocProcessing</Category>
        </QueueList>
</Response>
```
