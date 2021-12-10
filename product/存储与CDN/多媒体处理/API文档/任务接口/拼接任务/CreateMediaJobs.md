## 功能描述

CreateMediaJobs 用于提交一个任务。

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

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1545/65184) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1545/65182) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
  <Tag>Concat</Tag>
  <Input>
    <Object></Object>
  </Input>
  <Operation>
    <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
    <Output>
      <Region></Region>
      <Bucket></Bucket>
      <Object></Object>
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
| Tag                | Request | 创建任务的 Tag：Concat | String    | 是   |
| Input              | Request | 待操作的媒体信息                                         | Container | 是   |
| Operation          | Request | 操作规则，支持对单个文件执行多个不同任务，最多可填写6个                                                 | Container | 是   |
| QueueId            | Request | 任务所在的队列 ID                                         | String    | 是   |
| CallBack           | Request | 回调地址                 | String    | 否   |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述            | 类型   | 是否必选 |
| ------------------ | ------------- | --------------- | ------ | ---- |
| Object             | Request.Input | 媒体文件名 | String | 是   |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- |
| ConcatTemplate               | Request.Operation | 指定拼接参数，同创建拼接模板 <br/>CreateMediaTemplate 接口中的 Request.ConcatTemplate   | Container | 否   |
| TemplateId                   | Request.Operation | 指定的模板 ID                                        | String    | 否   |
| Output                       | Request.Operation | 结果输出地址                                          | Container | 是   |

>! 优先使用 TemplateId，无 TemplateId 时使用对应任务类型的参数。
>

Container 类型 ConcatTemplate 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| ConcatFragment      |  Request.Operation.ConcatTemplate | 拼接节点    | Container 数组    | 是   | 无  | 支持多个文件，按照文件顺序拼接 |
| Audio               |  Request.Operation.ConcatTemplate | 音频参数，同创建拼接模板中 Request.ConcatTemplate.Audio  | Container    | 否   | 无  | 无 |
| Video               |  Request.Operation.ConcatTemplate | 视频参数，同创建拼接模板中 Request.ConcatTemplate.Video  | Container    | 否   | 无  | 无 |
| Container           |  Request.Operation.ConcatTemplate | 封装格式，同创建拼接模板中 Request.ConcatTemplate.Container   | Container    | 是   | 无  | 无 |
| Index               |  Request.Operation.ConcatTemplate | Input 节点对象位于 ConcatFragment 序列位置索引    | String    | 否   | 0  | 不能大于ConcatFragment数组元素个数 |
| DirectConcat | Request.Operation.ConcatTemplate | 简单拼接方式（不转码直接拼接），其他的视频和音频参数失效 | String | 否 | false | true、false |

Container 类型 ConcatFragment 的具体数据描述如下：

| 节点名称（关键字）     | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------  | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Url                 | Request.Operation.<br/>ConcatTemplate.<br/>ConcatFragment | 拼接对象地址   | String    | 是   | 无   | 同 bucket 对象文件 |
| StartTime           | Request.Operation.<br/>ConcatTemplate.<br/>ConcatFragment | 开始时间   | String    | 否   | 视频开始   | <li>[0 视频时长] </li><li>单位为秒 </li>  |
| EndTime             | Request.Operation.<br/>ConcatTemplate.<br/>ConcatFragment | 结束时间   | String    | 否   | 视频结束   | <li>[0 视频时长] </li><li>单位为秒 </li>  |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述                                                         | 类型   | 是否必选 |
| ------------------ | ------------------------ | ------------------------------------------------------------ | ------ | ---- |
| Region             | Request.Operation.Output | 存储桶的地域                                                | String | 是   |
| Bucket             | Request.Operation.Output | 存储结果的存储桶                                              | String | 是   |
| Object             | Request.Operation.Output | 输出结果的文件名                                             | String | 是   |



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
    <Tag>Concat</Tag>
    <Input>
      <Object></Object>
    </Input>
    <Operation>
      <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
      <Output>
        <Region></Region>
        <Bucket></Bucket>
        <Object></Object>
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
| Tag | Response.JobsDetail | 新创建任务的 Tag：Concat | String |
| State | Response.JobsDetail | 任务的状态，为 Submitted、Running、Success、Failed、Pause、Cancel 其中一个 |  String |
| CreationTime | Response.JobsDetail | 任务的创建时间 |  String |
| StartTime | Response.JobsDetail | 任务的开始时间 |  String |
| EndTime | Response.JobsDetail | 任务的结束时间 |  String |
| QueueId | Response.JobsDetail | 任务所属的队列 ID |  String |
| Input | Response.JobsDetail | 该任务的输入资源地址 |  Container |
| Operation | Response.JobsDetail | 该任务的规则，支持对单个文件执行多个不同任务，最多可填写6个 |  Container |

Container 节点 Input 的内容：
同请求中的 Request.Input节点。

Container 节点 Operation 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| TemplateId | Response.JobsDetail.Operation | 任务的模版 ID |  String |
| Output | Response.JobsDetail.Operation | 文件的输出地址 |  Container |
| MediaInfo | Response.JobsDetail.Operation | 转码输出视频的信息，没有时不返回 |  Container |

Container 节点 Output 的内容：
同请求中的 Request.Operation.Output 节点。

Container 节点 MediaInfo 的内容：
同 [GenerateMediaInfo](https://cloud.tencent.com/document/product/460/38935) 接口中的 Response.MediaInfo 节点。

#### 错误码
常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1545/65185) 文档。

## 实际案例

**使用拼接模版 ID**

#### 请求

```shell
POST /jobs HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98****-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml



<Request>
  <Tag>Concat</Tag>
  <Input>
    <Object>test.mp4</Object>
  </Input>
  <Operation>
    <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
    <Output>
      <Region>ap-beijing</Region>
      <Bucket>aabc-1250000000</Bucket>
      <Object>concat.mp4</Object>
    </Output>
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
    <Tag>Concat</Tag>
    <Input>
      <Object>test.mp4</Object>
    </Input>
    <Operation>
      <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
      <Output>
        <Region>ap-beijing</Region>
        <Bucket>aabc-1250000000</Bucket>
        <Object>concat.mp4</Object>
      </Output>
    </Operation>
  </JobsDetail>
</Response>
```


**使用拼接处理参数**

#### 请求

```shell
POST /jobs HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98****-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml



<Request>
  <Tag>Concat</Tag>
  <Input>
    <Object>test.mp4</Object>
  </Input>
  <Operation>
    <ConcatTemplate>
        <ConcatFragment>
            <Mode>Start</Mode>
            <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/start.mp4</Url>
        </ConcatFragment>
        <ConcatFragment>
            <Mode>End</Mode>
            <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/end.mp4</Url>
        </ConcatFragment>
        <Audio>
            <Codec>mp3</Codec>
            <Samplerate></Samplerate>
            <Bitrate></Bitrate>
            <Channels></Channels>
        </Audio>
        <Video>
            <Codec>H.264</Codec>
            <Bitrate>1000</Bitrate>
            <Width>1280</Width>
            <Height></Height>
            <Fps>30</Fps>
        </Video>
        <Container>
            <Format>mp4</Format>
        </Container>
    </ConcatTemplate>
    <Output>
      <Region>ap-beijing</Region>
      <Bucket>aabc-1250000000</Bucket>
      <Object>concat.mp4</Object>
    </Output>
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
    <JobId>jabcxxxxfeipplsdfwe</JobId>
    <State>Submitted</State>
    <CreationTime>2019-07-07T12:12:12+0800</CreationTime>
    <EndTime></EndTime>
    <QueueId>p893bcda225bf4945a378da6662e81a89</QueueId>
    <Tag>Concat</Tag>
    <Input>
      <Object>test.mp4</Object>
    </Input>
    <Operation>
        <ConcatTemplate>
            <ConcatFragment>
                <Mode>Start</Mode>
                <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/start.mp4</Url>
            </ConcatFragment>
            <ConcatFragment>
                <Mode>End</Mode>
                <Url>http://bucket-1250000000.cos.ap-beijing.myqcloud.com/end.mp4</Url>
            </ConcatFragment>
            <Audio>
                <Codec>mp3</Codec>
                <Samplerate></Samplerate>
                <Bitrate></Bitrate>
                <Channels></Channels>
            </Audio>
            <Video>
                <Codec>H.264</Codec>
                <Bitrate>1000</Bitrate>
                <Width>1280</Width>
                <Height></Height>
                <Fps>30</Fps>
            </Video>
            <Container>
                <Format>mp4</Format>
            </Container>
        </ConcatTemplate>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>aabc-1250000000</Bucket>
            <Object>concat.mp4</Object>
        </Output>
    </Operation>
  </JobsDetail>
</Response>
```
