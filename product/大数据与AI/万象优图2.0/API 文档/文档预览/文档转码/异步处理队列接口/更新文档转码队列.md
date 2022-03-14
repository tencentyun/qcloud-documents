## 功能描述

UpdateDocProcessQueue 接口用于更新文档转码队列。

## 请求

#### 请求示例

```plaintext
PUT /docqueue/p8eb46b8cc1a94bc09512d16c5c4f4d3a HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有以下请求体。

```plaintext
<Request>
    <Name>Queue Name</Name>
    <QueueID></QueueID>
    <State></State>
    <NotifyConfig>
        <Type></Type>
        <Url></Url>
        <Event></Event>
    </NotifyConfig>
</Request>
```

具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
   </tr>
   <tr>
      <td>Request</td>
      <td>无</td>
      <td>保存请求的容器</td>
      <td>Container</td>
      <td>是</td>
   </tr>
</table>


Container 类型 Request 的具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Name</td>
      <td>Request</td>
      <td>队列名称</td>
      <td>String</td>
      <td>是</td>
      <td>长度限制100字符</td>
   </tr>
   <tr>
      <td>QueueID</td>
      <td>Request</td>
      <td>队列 ID</td>
      <td>String</td>
      <td>是</td>
      <td>无</td>
   </tr>
   <tr>
      <td>State</td>
      <td>Request</td>
      <td>队列状态</td>
      <td>String</td>
      <td>是</td>
      <td>
        1. Active 表示队列内的作业会被文档预览服务调度转码执行<br>2. Paused 表示队列暂停，作业不再会被文档预览服务调度执行，队列内的所有作业状态维持在已提交状态，已经处于执行中的任务将继续执行，不受影响
      </td>
   </tr>
   <tr>
      <td>NotifyConfig</td>
      <td>Request</td>
      <td>通知渠道</td>
      <td>Container</td>
      <td>是</td>
      <td>第三方回调 Url</td>
   </tr>
</table>


Container 类型 NotifyConfig 的具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
      <th>限制</th>
   </tr>
   <tr>
      <td>Url</td>
      <td>Request.NotifyConfig</td>
      <td>回调配置</td>
      <td>String</td>
      <td>否</td>
      <td>长度限制100字符</td>
   </tr>
   <tr>
      <td>Type</td>
      <td>Request.NotifyConfig</td>
      <td>回调类型，普通回调：Url</td>
      <td>String</td>
      <td>否</td>
      <td>长度限制100字符</td>
   </tr>
   <tr>
      <td>Event</td>
      <td>Request.NotifyConfig</td>
      <td>回调事件，文档预览任务完成</td>
      <td>String</td>
      <td>否</td>
      <td>长度限制100字符</td>
   </tr>
   <tr>
      <td>State</td>
      <td>Request.NotifyConfig</td>
      <td>回调开关，Off，On</td>
      <td>String</td>
      <td>否</td>
      <td>长度限制100字符</td>
   </tr>
</table>




## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhf****</RequestId>
    <Queue>
        <QueueId></QueueId>
        <Name></Name>
        <State>Active</State>
        <NotifyConfig>
            <Url>mts-topic-1</Url>
            <Type></Type>
            <Event></Event>
        </NotifyConfig>
        <CreateTime></CreateTime>
        <UpdateTime></UpdateTime>
    </Queue>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                                                         | 类型      |
| :----------------- | :------- | :----------------------------------------------------------- | :-------- |
| RequestId          | Response | 请求的唯一 ID                                                | String    |
| Queue              | Response | 队列信息，详情请参见 [DescribeDocProcessQueues](https://cloud.tencent.com/document/product/460/46946) 中的 Response.QueueList | Container |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

#### 请求

```plaintext
PUT /docqueue/p2505d57bdf4c4329804b58a6a5fb1572 HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: examplebucket-1250000000.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Content-Length: 279
Authorization: Authorization

<?xml version="1.0" encoding="UTF-8" ?>
<Request>
    <QueueId>p2505d57bdf4c4329804b58a6a5fb1572</QueueId>
    <State>Active</State>
    <Name>markjrzhang4</Name>
    <NotifyConfig>
        <Url>http://google.com/</Url>
    <State>On</State>
        <Type>Url</Type>
        <Event>TransCodingFinish</Event>
    </NotifyConfig>
</Request>[!http]
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 08:22:41 GMT
Content-Type: application/xml
Content-Length: 641
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: NWYxZThlZDBfYzc2OTQzNjRfMzUxYV8x****

<?xml version="1.0" encoding="utf-8"?>
<Response>
        <RequestId>NWYxZThlZDBfYzc2OTQzNjRfMzUxYV8x****</RequestId>
        <Queue>
                <QueueId>p2505d57bdf4c4329804b58a6a5fb1572</QueueId>
                <Name>markjrzhang4</Name>
                <State>Active</State>
                <NotifyConfig>
                        <Url>http://example.com/</Url>
                        <Event>TransCodingFinish</Event>
                        <Type>Url</Type>
                        <State>On</State>
                </NotifyConfig>
                <MaxSize>10000</MaxSize>
                <MaxConcurrent>10</MaxConcurrent>
                <CreateTime>2020-07-24T22:42:27+0800</CreateTime>
                <UpdateTime>2020-07-27T16:22:40+0800</UpdateTime>
                <BucketId>test007-1251704708</BucketId>
                <Category>DocProcessing</Category>
        </Queue>
</Response>
```
