## 功能描述

DescribeSpeechJob 用于查询指定的语音识别任务。

## 请求

#### 请求示例

```shell
GET /asr_jobs/<jobId> HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求无请求体。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
  <JobsDetail></JobsDetail>
  <NonExistJobIds></NonExistJobIds>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                                                         | 类型      |
| :----------------- | :------- | :----------------------------------------------------------- | :-------- |
| JobsDetail         | Response | 任务的详细信息，同 CreateSpeechJobs 接口的 Response.JobsDetail 节点 | Container |
| NonExistJobIds     | Response | 查询的 ID 中不存在的任务，所有任务都存在时不返回             | String    |
| SpeechRecognitionResult     | Response | 在 job 的类型为 SpeechRecognition 且 job 状态为 success 时，返回语音识别的识别结果详情。            | Container    |

Container 节点 SpeechRecognitionResult 的内容：

| 节点名称（关键字） | 父节点   | 描述                                                         | 类型      |
| :----------------- | :------- | :----------------------------------------------------------- | :-------- |
| Result         | Response.SpeechRecognitionResult | 识别结果 | Container |
| ResultDetail     | Response.SpeechRecognition.ResultDetail | 识别结果详情，包含每个句子中的词时间偏移，一般用于生成字幕的场景。(识别请求中ResTextFormat=1时该字段不为空)<br>注意：此字段可能返回 null，表示取不到有效值。| Array of SentenceDetail |
| AudioTime     | Response.SpeechRecognition.audioTime | 语音时长            | double    |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

