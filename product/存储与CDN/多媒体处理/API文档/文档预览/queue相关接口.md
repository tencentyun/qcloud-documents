## 队列管理

### 查询文档预览任务队列

#### 接口地址

```
<BucketName-APPID>.ci.<Region>.myqcloud.com/docqueue
```

#### 请求方式

```
GET
```

#### 请求示例 

```
GET /docqueue?pageNumber=1&pageSize=2 HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

#### 请求参数

| 参数名  | 类型   | 含义     |
| ------- | ------ | -------- |
| pageNumber    | int    | 页码（默认第一页）  |
| pageSize| int | 每页条数（默认十条） |

#### 返回示例

```
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

#### 返回参数

| 参数名  | 类型   | 含义     |
| ------- | ------ | -------- |
| TotalCount    | int    | 队列总数  |
| RequestId| string | 请求 ID |
| PageNumber| int | 页码 |
| PageSize| int | 每页条数 |

QueueList 的参数

| 参数名  | 类型   | 含义     |
| ------- | ------ | -------- |
| QueueId    | int    | 队列 ID  |
| Name| string | 队列名称 |
| State| string | 队列状态 |
| NotifyConfig| obj | 配置信息 |
| MaxSize| int | 最大队列长度 |
| MaxConcurrent| int | 队列最大并发量 |
| CreateTime| string | 创建时间 |
| UpdateTime| string | 更新时间 |
| BucketId| string | bucket名称以及 ID |
| Category| string | 存放的任务种类 |

### 修改队列信息

>? 请求方式与 [UpdateMediaQueue](https://cloud.tencent.com/document/product/460/42324) 类似，只需修改接口地址即可。
>

#### 接口地址

```
<BucketName-APPID>.ci.<Region>.myqcloud.com/docqueue/QueueId 
```