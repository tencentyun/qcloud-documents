## 功能描述

CreateMediaJobs 用于提交一个提取数字水印任务。

## 请求

#### 请求示例

```shell
POST /jobs HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```


>? 
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
> 



#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

```shell
<Request>
  <Tag>ExtractDigitalWatermark</Tag>
  <Input>
    <Object></Object>
  </Input>
  <Operation>
    <ExtractDigitalWatermark>
      <Type>Text</Type>
      <Version>V1</Version>
    </ExtractDigitalWatermark>
  </Operation>
  <QueueId></QueueId>
  <CallBack></CallBack>
</Request>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Tag                | Request | 创建任务的 Tag：ExtractDigitalWatermark | String    | 是   |
| Input              | Request | 待操作的媒体信息                                         | Container | 是   |
| Operation          | Request | 操作规则                                               | Container | 是   |
| QueueId            | Request | 任务所在的队列 ID                                         | String    | 是   |
| CallBack           | Request | 回调地址                 | String    | 否   |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述            | 类型   | 是否必选 |
| ------------------ | ------------- | --------------- | ------ | ---- |
| Object             | Request.Input | 媒体文件名 | String | 是   |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- |
| ExtractDigitalWatermark   | Request.Operation | 数字水印配置 | Container | 是  |

Container 类型 ExtractDigitalWatermark 的具体数据类型描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 | 限制 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- | ---- |
| Type               | Request.Operation.ExtractDigitalWatermark | 水印类型      | String | 是 | Text |
| Version            | Request.Operation.ExtractDigitalWatermark | 水印版本     | String | 是 | V1 |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
  <JobsDetail>
    <Code></Code>
    <Message></Message>
    <JobId></JobId>
    <State></State>
    <CreationTime></CreationTime>
    <EndTime></EndTime>
    <QueueId></QueueId>
    <Tag>ExtractDigitalWatermark</Tag>
    <Input>
      <Object></Object>
    </Input>
    <Operation>
      <ExtractDigitalWatermark>
        <Type>Text</Type>
        <Version>V1</Version>
      </ExtractDigitalWatermark>
    </Operation>
  </JobsDetail>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字）| 父节点 | 描述 | 类型 |
| :--- | :-- | :-- | :-- |
| Response | 无 | 保存结果的容器 | Container |

Container 节点 Response 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| JobsDetail | Response | 任务的详细信息 |  Container |


Container 节点 JobsDetail 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Code | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义 |  String |
| Message | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义 |  String |
| JobId | Response.JobsDetail | 新创建任务的 ID |  String |
| Tag | Response.JobsDetail | 新创建任务的 Tag：ExtractDigitalWatermark | String |
| State | Response.JobsDetail | 任务的状态，为 Submitted、Running、Success、Failed、Pause、Cancel 其中一个 |  String |
| CreationTime | Response.JobsDetail | 任务的创建时间 |  String |
| EndTime | Response.JobsDetail | 任务的结束时间 |  String |
| QueueId | Response.JobsDetail | 任务所属的队列 ID |  String |
| Input | Response.JobsDetail | 该任务的输入资源地址 |  Container |
| Operation | Response.JobsDetail | 该任务的操作规则 |  Container |

Container 节点 Input 的内容：
同请求中的 Request.Input 节点。

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- |
| ExtractDigitalWatermark   | Response.JobsDetail.Operation | 数字水印配置 | Container |

Container 类型 ExtractDigitalWatermark 的具体数据类型描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- |
| Message               | Response.JobsDetail.Operation.ExtractDigitalWatermark |  提取出的数字水印字符串信息    | string |
| Type               | Response.JobsDetail.Operation.ExtractDigitalWatermark | 水印类型      | String |
| Version            | Response.JobsDetail.Operation.ExtractDigitalWatermark | 水印版本     | String |


#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例


#### 请求

```shell
POST /jobs HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml



<Request>
  <Tag>ExtractDigitalWatermark</Tag>
  <Input>
    <Object>test.mp4</Object>
  </Input>
  <Operation>
    <ExtractDigitalWatermark>
        <Type>Text</Type>
        <Message>123456789ab</Message>
        <Version>V1</Version>
    </ExtractDigitalWatermark>
  </Operation>
  <QueueId>p893bcda225bf4945a378da6662e81a89</QueueId>
  <CallBack>https://www.callback.com</CallBack>
</Request>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzh****=



<Response>
  <JobsDetail>
    <Code>Success</Code>
    <Message>Success</Message>
    <JobId>je8f65004eb8511eaaed4f377124a303c</JobId>
    <State>Submitted</State>
    <CreationTime>2019-07-07T12:12:12+0800</CreationTime>
    <EndTime></EndTime>
    <QueueId>p893bcda225bf4945a378da6662e81a89</QueueId>
    <Tag>ExtractDigitalWatermark</Tag>
    <Input>
      <Object>test.mp4</Object>
    </Input>
    <Operation>
      <ExtractDigitalWatermark>
        <Type>Text</Type>
        <Message>123456789ab</Message>
        <Version>V1</Version>
      </ExtractDigitalWatermark> 
    </Operation>
  </JobsDetail>
</Response>
```
