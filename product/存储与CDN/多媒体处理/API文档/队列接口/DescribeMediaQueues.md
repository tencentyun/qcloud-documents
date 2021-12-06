## 功能描述

DescribeMediaQueues 接口用于搜索队列。

## 请求

#### 请求示例

```shell
GET /queue HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。
>

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体

该请求的请求体为空。

#### 请求参数

<table>
   <tr>
      <th nowrap="nowrap">名称	</th>
      <th>类型</th>
      <th>描述</th>
      <th>是否必选</th>
   </tr>
   <tr>
      <td>queueIds</td>
      <td>string</td>
      <td>队列 ID，以“,”符号分割字符串</td>
      <td>否</td>
   </tr>
   <tr>
      <td>state</td>
      <td>string</td>
      <td>
        1. Active 表示队列内的作业会被媒体转码服务调度转码执行<br>2. Paused 表示队列暂停，作业不再会被媒体转码调度转码执行，队列内的所有作业状态维持在暂停状态，已经处于转码中的任务将继续转码，不受影响</td>
      <td>否</td>
   </tr>
   <tr>
      <td>pageNumber</td>
      <td>string</td>
      <td>第几页</td>
      <td>否</td>
   </tr>
   <tr>
      <td>pageSize</td>
      <td>string</td>
      <td>每页个数</td>
      <td>否</td>
   </tr>
</table>



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据，当指定 pageNumber 和 pageSize 时包含完整节点数据的内容展示如下：

```shell
<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <QueueList>
        <QueueId>A</QueueId>
        <Name></Name>
        <State>Active</State>
        <MaxSize>10000</MaxSize>
        <MaxConcurrent>10</MaxConcurrent>
        <UpdateTime></UpdateTime>
        <CreateTime></CreateTime>
        <NotifyConfig>
            <Url></Url>
            <Type></Type>
            <State></State>
            <Event></Event>
        </NotifyConfig>
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

| 节点名称（关键字） | 父节点                          | 描述                              | 类型   |
| :----------------- | :------------------------------ | :-------------------------------- | :----- |
| Url                | Response.QueueList.NotifyConfig | 回调地址                          | String |
| State              | Response.QueueList.NotifyConfig | 开关状态，On 或者 Off             | String |
| Type               | Response.QueueList.NotifyConfig | 回调类型，Url                     | String |
| Event              | Response.QueueList.NotifyConfig | 任务完成：TaskFinish；工作流完成：WorkflowFinish | String |



该响应体返回为 **application/xml** 数据，当指定 queueIds 时包含完整节点数据的内容展示如下：

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

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

#### 请求1：获取队列列表

```shell
GET /queue?queueIds=A,B,C HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml
```

#### 响应1

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <QueueList>
        <QueueID>A</QueueID>
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



#### 请求2：获取特定队列信息

```shell
GET /queue?pageSize=10&pageNumber=1 HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml

```

#### 响应2

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <TotalCount>1</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <QueueList>
        <QueueID>B</QueueID>
        <Name></Name>
        <State>Paused</State>
        <NotifyConfig>
            <Url></Url>
        </NotifyConfig>
    </QueueList>
</Response>
```

