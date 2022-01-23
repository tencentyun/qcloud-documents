## 功能描述

CreateMediaJobs 接口用来提交一个任务。

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

>? Authorization: Auth String （详情请查阅 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。
>


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
  <Tag>VoiceSeparate</Tag>
  <Input>
    <Object></Object>
  </Input>
  <Operation>
    <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
    <Output>
      <Region></Region>
      <Bucket></Bucket>
      <Object></Object>
      <AuObject></AuObject>
    </Output>
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
| Tag                | Request | 创建任务的 Tag：VoiceSeparate                              | String    | 是   |
| Input              | Request | 待操作的媒体信息                                          | Container | 是   |
| Operation          | Request | 操作规则，支持对单个文件执行多个不同任务，最多可填写6个                                                 | Container | 是   |
| QueueId            | Request | 任务所在的队列 ID                                          | String    | 是   |
| CallBack           | Request | 回调地址                                                  | String    | 否   |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述            | 类型   | 是否必选 |
| ------------------ | ------------- | --------------- | ------ | ---- |
| Object             | Request.Input | 媒体文件 的名字 | String | 是   |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- |
| VoiceSeparate                | Request.Operation | 指定该任务的参数                                    | Container | 否   |
| TemplateId                   | Request.Operation | 指定的模版 ID                                        | String    | 否   |
| Output                       | Request.Operation | 结果输出地址                                        | Container | 是   |

>! 优先使用 TemplateId，无 TemplateId 时使用对应任务类型的参数。
>

Container 类型 VoiceSeparate 的具体数据描述如下：

| 节点名称（关键字） | 父节点                      | 描述                                   | 类型      | 是否必选 |
| ---------------- | :-------------------------- | -------------------------------------- | --------- | ---- |
| AudioMode        | Request.Operation.VoiceSeparate | 同创建人声分离模板 CreateMediaTemplate 接口中的 Request.AudioMode | Container | 否   |
| AudioConfig      | Request.Operation.VoiceSeparate | 同创建人声分离模板 CreateMediaTemplate 接口中的 Request.AudioConfig | Container | 否   |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述                                                         | 类型   | 是否必选 |
| ------------------ | ------------------------ | ------------------------------------------------------------ | ------ | ---- |
| Region             | Request.Operation.Output | 存储桶的地域                                                  | String | 是   |
| Bucket             | Request.Operation.Output | 存储结果的存储桶                                               | String | 是   |
| Object             | Request.Operation.Output | 背景音结果文件名，不能与 AuObject 同时为空                  | String | 否   |
| AuObject           | Request.Operation.AuObject | 人声结果文件名，不能与 Object 同时为空                   | String | 否   |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1545/65183) 文档。

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
    <Tag>VoiceSeparate</Tag>
    <Input>
      <Object></Object>
    </Input>
    <Operation>
      <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
      <Output>
        <Region></Region>
        <Bucket></Bucket>
        <Object></Object>
        <AuObject></AuObject>
      </Output>
      <MediaInfo>
      </MeidaInfo>
    </Operation>
  </JobsDetail>
</Response>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Response |无| 保存结果的容器 | Container |

Container 节点 Response 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| JobsDetail | Response | 任务的详细信息 |  Container |


Container 节点 JobsDetail 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Code | Response.JobsDetail | 错误码，只有 State为 Failed 时有意义 |  String |
| Message | Response.JobsDetail | 错误描述，只有 State为 Failed 时有意义 |  String |
| JobId | Response.JobsDetail | 新创建任务的 ID |  String |
| Tag | Response.JobsDetail | 新创建任务的 Tag：VoiceSeparate | String |
| State | Response.JobsDetail | 任务的状态，为 Submitted、Running、Success、Failed、Pause、Cancel 其中一个 |  String |
| CreationTime | Response.JobsDetail | 任务的创建时间 |  String |
| StartTime | Response.JobsDetail | 任务的开始时间 |  String |
| EndTime | Response.JobsDetail | 任务的结束时间 |  String |
| QueueId | Response.JobsDetail | 任务所属的队列 ID |  String |
| Input | Response.JobsDetail | 该任务的输入资源地址 |  Container |
| Operation | Response.JobsDetail | 该任务的规则 |  Container |

Container 节点 Input 的内容：
同 请求中的 Request.Input节点。

Container 节点 Operation 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| TemplateId | Response.JobsDetail.Operation | 任务的模版ID |  String |
| Output | Response.JobsDetail.Operation | 文件的输出地址 |  Container |
| MediaInfo | Response.JobsDetail.Operation | 转码输出视频的信息，没有时不返回 |  Container |

Container 节点 Output 的内容：
同 请求中的 Request.Operation.Output节点。

Container 节点 MediaInfo 的内容：
同 [GenerateMediaInfo](https://cloud.tencent.com/document/product/460/38935) 接口中的 Response.MediaInfo 节点。

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

**使用人声分离模版 ID**

#### 请求

```shell
POST /jobs HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
  <Tag>VoiceSeparate</Tag>
  <Input>
    <Object>test.mp4</Object>
  </Input>
  <Operation>
    <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
    <Output>
        <Region>ap-beijing</Region>
        <Bucket>abc-1250000000</Bucket>
        <Object></Object>
        <AuObject></AuObject>
    </Output>
  </Operation>
  <QueueId>p893bcda225bf4945a378da6662e81a89</QueueId>
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
  <JobsDetail>
    <Code>Success</Code>
    <Message>Success</Message>
    <JobId>je8f65004eb8511eaaed4f377124a303c</JobId>
    <State>Submitted</State>
    <CreationTime>2019-07-07T12:12:12+0800</CreationTime>
    <StartTime></StartTime>
    <EndTime></EndTime>
    <QueueId>p893bcda225bf4945a378da6662e81a89</QueueId>
    <Tag>VoiceSeparate</Tag>
    <Input>
      <Object>test.mp4</Object>
    </Input>
    <Operation>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object></Object>
            <AuObject></AuObject>
        </Output>
    </Operation>
  </JobsDetail>
</Response>
```



**使用人声分离处理参数**

#### 请求


```shell
POST /jobs HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
  <Tag>VoiceSeparate</Tag>
  <Input>
    <Object>test.mp4</Object>
  </Input>
  <Operation>
    <VoiceSeparate>
      <AudioMode>IsAudio</AudioMode>
      <AudioConfig>
        <Codec>mp3</Codec>
        <Samplerate>44100</Samplerate>
        <Bitrate>12</Bitrate>
        <Channels>2</Channels>
      </AudioConfig>
    </VoiceSeparate>
    <Output>
      <Region>ap-beijing</Region>
      <Bucket>abc-1250000000</Bucket>
      <Object>test-trans.mp3</Object>
      <AuObject></AuObject>
    </Output>
  </Operation>
  <QueueId>p893bcda225bf4945a378da6662e81a89</QueueId>
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
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
  <JobsDetail>
    <Code>Success</Code>
    <Message>Success</Message>
    <JobId>jabcxxxxfeipplsdfwe</JobId>
    <State>Submitted</State>
    <CreationTime>2019-07-07T12:12:12+0800</CreationTime>
    <StartTime></StartTime>
    <EndTime></EndTime>
    <QueueId>p893bcda225bf4945a378da6662e81a89</QueueId>
    <Tag>VoiceSeparate</Tag>
    <Input>
      <Object>test.mp4</Object>
    </Input>
    <Operation>
        <VoiceSeparate>
          <AudioMode>IsAudio</AudioMode>
          <AudioConfig>
            <Codec>mp3</Codec>
            <Samplerate>44100</Samplerate>
            <Bitrate>12</Bitrate>
            <Channels>2</Channels>
          </AudioConfig>
        </VoiceSeparate>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object>test-trans.mp3</Object>
            <AuObject></AuObject>
        </Output>
    </Operation>
  </JobsDetail>
</Response>
```

