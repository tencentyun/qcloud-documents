## 功能描述
DescribeMediaJobs 接口用于拉取符合条件的任务。

## 请求

#### 请求示例

```shell
GET /jobs?size=&states=&queueId=&startCreationTime=&endCreationTime= HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>

```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
>


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求无请求体。

#### 请求参数

参数的具体内容如下：

|节点名称（关键字）|父节点|描述|类型|是否必选|
|:---|:-- |:--|:--|:--|
|queueId|无|拉取该队列 ID 下的任务|String|是|
| tag |无| 任务的 Tag：VoiceSeparate | String |是|
| orderByTime |无| Desc 或者 Asc。默认为 Desc | String |否|
| nextToken |无| 请求的上下文，用于翻页。上次返回的值 | String |否|
| size |无| 拉取的最大任务数。默认为10。最大为100 | Integer |否|
| states |无| 拉取该状态的任务，以`,`分割，支持多状态：All、Submitted、Running、Success、Failed、Pause、Cancel。默认为 All | String |否|
| startCreationTime |无| 拉取创建时间大于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z` | String |否|
| endCreationTime |无| 拉取创建时间小于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z` | String |否|

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` shell
<Response>
  <JobsDetail>
  </JobsDetail>
  <NextToken></NextToken>
</Response>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Response |无| 保存结果的容器 | Container |

Container 节点 Response 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| JobsDetail | Response | 任务的详细信息，同 CreateMediaJobs 接口中的 Response.JobsDetail 节点 |  Container |
| NextToken | Response | 翻页的上下文 Token |  String |

Container 节点 JobsDetail 的内容：

| 节点名称（关键字） | 父节点              | 描述                                                         | 类型      |
| :----------------- | :------------------ | :----------------------------------------------------------- | :-------- |
| Code               | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义                           | String    |
| Message            | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义                         | String    |
| JobId              | Response.JobsDetail | 新创建任务的 ID                                               | String    |
| Tag                | Response.JobsDetail | 新创建任务的 Tag：VoiceSeparate                               | String    |
| State              | Response.JobsDetail | 任务的状态，值为 Submitted、Running、Success、Failed、Pause、Cancel 其中一个 | String    |
| CreationTime       | Response.JobsDetail | 任务的创建时间                                               | String    |
| StartTime          | Response.JobsDetail | 任务的开始时间                                               | String    |
| EndTime            | Response.JobsDetail | 任务的结束时间                                               | String    |
| QueueId            | Response.JobsDetail | 任务所属的队列 ID                                             | String    |
| Input              | Response.JobsDetail | 该任务的输入资源地址                                         | Container |
| Operation          | Response.JobsDetail | 该任务的规则                                                 | Container |

Container 节点 Operation 的内容：

| 节点名称（关键字） | 父节点                        | 描述                             | 类型      |
| :----------------- | :---------------------------- | :------------------------------- | :-------- |
| TemplateId         | Response.JobsDetail.Operation | 任务的模板 ID                     | String    |
| Output             | Response.JobsDetail.Operation | 文件的输出地址                   | Container |
| VoiceSeparate      | Response.JobsDetail.Operation | 指定转码模板参数 | Container |

Operation  类型 VoiceSeparate 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                      | 描述                                                         | 类型      | 
| ------------------ | :------------------------------------------ | ------------------------------------------------------------ | --------- | 
| AudioMode          | Response.JobsDetail.Operation.VoiceSeparate | 同创建人声分离模板 CreateMediaTemplate 接口中的 Request.AudioMode | Container | 
| AudioConfig        | Response.JobsDetail.Operation.VoiceSeparate | 同创建人声分离模板 CreateMediaTemplate 接口中的 Request.AudioConfig | Container | 

Operation  类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                 | 描述                                           | 类型   | 
| ------------------ | -------------------------------------- | ---------------------------------------------- | ------ |
| Region             | Response.JobsDetail.Operation.Output   | 存储桶的地域                                   | String | 
| Bucket             | Response.JobsDetail.Operation.Output   | 存储结果的存储桶                               | String | 
| Object             | Response.JobsDetail.Operation.Output   | 背景音结果文件的名称，不能与 AuObject 同时为空。 | String | 
| AuObject           | Response.JobsDetail.Operation.AuObject | 人声结果文件的名称，不能与 Object 同时为空。     | String | 

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

#### 请求

```shell
GET /jobs?queueId=aaaaaaaaaaa&tag=VoiceSeparate HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 666
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-ci
x-ci-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

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
    <Tag>VoiceSeparate<Tag>
    <Input>
      <Object>test.mp4</Object>
    </Input>
    <Operation>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object>test-trans.mp3</Object>
            <AuObject></AuObject>
        </Output>
    </Operation>
  </JobsDetail>
  <JobsDetail>
    <Code>Success</Code>
    <Message>Success</Message>
    <JobId>jabcxxxxfeipplsdfwe</JobId>
    <State>Submitted</State>
    <CreationTime>2019-07-07T12:12:12+0800</CreationTime>
    <StartTime></StartTime>
    <EndTime></EndTime>
    <QueueId>p893bcda225bf4945a378da6662e81a89</QueueId>
    <Tag>VoiceSeparate<Tag>
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


