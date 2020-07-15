## 功能描述

CreateSpeechJobs 接口用于提交一个语音识别任务。

## 请求

#### 请求示例

```plaintext
POST /asr_jobs HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

> ?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求操作的实现需要有如下请求体。

```plaintext
<Request>
  <Tag>SpeechRecognition</Tag>
  <Input>
    <Object></Object>
  </Input>
  <Operation>
    <SpeechRecognition></SpeechRecognition>
    <Output>
      <Region></Region>
      <Bucket></Bucket>
      <Object></Object>
    </Output>
  </Operation>
  <QueueId></QueueId>
</Request>
```

具体的数据描述如下：

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
   </tr>
   <tr>
      <td>Tag</td>
      <td>Request</td>
      <td>创建任务的 Tag，目前仅支持：SpeechRecognition</td>
      <td>String</td>
      <td>是</td>
   </tr>
   <tr>
      <td>Input</td>
      <td>Request</td>
      <td>待操作的语音文件</td>
      <td>Container</td>
      <td>是</td>
   </tr>
   <tr>
      <td>Operation</td>
      <td>Request</td>
      <td>操作规则</td>
      <td>Container</td>
      <td>是</td>
   </tr>
   <tr>
      <td>QueueId</td>
      <td>Request</td>
      <td>任务所在的队列 ID</td>
      <td>String</td>
      <td>是</td>
   </tr>
</table>

Container 类型 Input 的具体数据描述如下：

<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>是否必选</th>
   </tr>
   <tr>
      <td>Object</td>
      <td>Request.Input</td>
      <td>语音文件在 COS 上的 key，Bucket 由 Host 指定</td>
      <td>String</td>
      <td>是</td>
   </tr>
</table>

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | -------- |
| SpeechRecognition  | Request.Operation | 当 Tag 为 SpeechRecognition 时有效，指定该任务的参数          | Container | 否       |
| Output             | Request.Operation | 结果输出地址                                                 | Container | 是       |


Container 类型 SpeechRecognition 的具体数据描述如下：

| 节点名称（关键字） | 父节点                      | 描述                                      | 类型      | 是否必选 |
| ------------------ | :-------------------------- | ----------------------------------------- | --------- | -------- |
| EngineModelType    | Request.Operation.Speech<br>Recognition | 引擎模型类型。<br>电话场景： <br>• 8k_zh：电话 8k 中文普通话通用（可用于双声道音频）； <br> • 8k_zh_s：电话 8k 中文普通话话者分离（仅适用于单声道音频）；<br> 非电话场景： <br> • 16k_zh：16k 中文普通话通用；<br> • 16k_zh_video：16k 音视频领域；<br> • 16k_en：16k 英语；<br> • 16k_ca：16k 粤语。   | String | 是       |
| ChannelNum         | Request.Operation.Speech<br>Recognition | 语音声道数。1：单声道；2：双声道（仅支持 8k_zh 引擎模型）。        | Integer | 是       |
| ResTextFormat       | Request.Operation.Speech<br>Recognition | 识别结果返回形式。0： 识别结果文本(含分段时间戳)； 1：仅支持16k中文引擎，含识别结果详情(词时间戳列表，一般用于生成字幕场景)。 | Integer | 是       |
| FilterDirty       | Request.Operation.Speech<br>Recognition | 是否过滤脏词（目前支持中文普通话引擎）。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。默认值为0。 | Integer | 否       |
| FilterModal       | Request.Operation.Speech<br>Recognition | 是否过语气词（目前支持中文普通话引擎）。0：不过滤语气词；1：部分过滤；2：严格过滤 。默认值为 0。 | Integer | 否       |
| ConvertNumMode       | Request.Operation.Speech<br>Recognition | 是否进行阿拉伯数字智能转换（目前支持中文普通话引擎）。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字。默认值为1。| Integer | 否       |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述                                                         | 类型   | 是否必选 |
| ------------------ | ------------------------ | ------------------------------------------------------------ | ------ | -------- |
| Region             | Request.Operation.Output | 存储桶的地域                                                 | String | 是       |
| Bucket             | Request.Operation.Output | 存储结果的存储桶                                             | String | 是       |
| Object             | Request.Operation.Output | 结果文件的名称                                               | String | 是       |



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
  <JobsDetail>
    <Code></Code>
    <Message></Message>
    <JobId></JobId>
    <State></State>
    <CreationTime></CreationTime>
    <QueueId></QueueId>
    <Tag><Tag>
    <Input>
      <Object></Object>
    </Input>
    <Operation>
      <SpeechRecognition></SpeechRecognition>
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

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述           | 类型      |
| :----------------- | :------- | :------------- | :-------- |
| JobsDetail         | Response | 任务的详细信息 | Container |

Container 节点 JobsDetail 的内容：

| 节点名称（关键字） | 父节点              | 描述                                                         | 类型      |
| :----------------- | :------------------ | :----------------------------------------------------------- | :-------- |
| Code               | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义                        | String    |
| Message            | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义                      | String    |
| JobId              | Response.JobsDetail | 新创建任务的 ID                                              | String    |
| Tag                | Response.JobsDetail | 新创建任务的 Tag：SpeechRecognition                          | String    |
| State              | Response.JobsDetail | 任务的状态，为 Submitted、Running、Success、Failed、Pause、Cancel 其中一个 | String    |
| CreationTime       | Response.JobsDetail | 任务的创建时间                                               | String    |
| QueueId            | Response.JobsDetail | 任务所属的队列 ID                                            | String    |
| Input              | Response.JobsDetail | 该任务的输入资源地址                                         | Container |
| Operation          | Response.JobsDetail | 该任务的规则                                                 | Container |

Container 节点 Input 的内容：
同上面请求中的 Request.Input 节点。

Container 节点 Operation 的内容：

| 节点名称（关键字） | 父节点                        | 描述                             | 类型      |
| :----------------- | :---------------------------- | :------------------------------- | :-------- |
| TemplateId         | Response.JobsDetail.Operation | 任务的模版 ID                    | String    |
| Output             | Response.JobsDetail.Operation | 文件的输出地址                   | Container |
| MediaInfo          | Response.JobsDetail.Operation | 转码输出视频的信息，没有时不返回 | Container |

Container 节点 Output 的内容：
同上面请求中的 Request.Operation.Output 节点。

Container 节点 SpeechRecognition 的内容：
同上面请求中的 Request.Operation.SpeechRecognition节点。

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

