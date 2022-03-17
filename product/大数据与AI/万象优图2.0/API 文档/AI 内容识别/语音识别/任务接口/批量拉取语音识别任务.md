## 功能描述

DescribeSpeechJobs 用于拉取符合条件的语音识别任务。

## 请求

#### 请求示例

```shell
GET /asr_jobs?size=&states=&queueId=&startCreationTime=&endCreationTime= HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求无请求体。

#### 请求参数

参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                         | 类型    | 是否必选 |
| :----------------- | :----- | :----------------------------------------------------------- | :------ | :------- |
| queueId            | 无     | 拉取该队列 ID 下的任务。                                     | String  | 是       |
| tag                | 无     | 任务的 Tag：SpeechRecognition。                        | String  | 是       |
| orderByTime        | 无     | Desc 或者 Asc。默认为 Desc。                                 | String  | 否       |
| nextToken          | 无     | 请求的上下文，用于翻页。上次返回的值。                       | String  | 否       |
| size               | 无     | 拉取的最大任务数。默认为10。最大为100。                      | Integer | 否       |
| states             | 无     | 拉取该状态的任务，以`,`分割，支持多状态：All、Submitted、Running、Success、Failed、Pause、Cancel。默认为 All。 | String  | 否       |
| startCreationTime  | 无     | 拉取创建时间大于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z`  | String  | 否       |
| endCreationTime    | 无     | 拉取创建时间小于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z`  | String  | 否       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。 

#### 响应体

该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
  <JobsDetail></JobsDetail>
  <NextToken></NextToken>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                                                         | 类型      |
| :----------------- | :------- | :----------------------------------------------------------- | :-------- |
| JobsDetail         | Response | 任务的详细信息，同 CreateSpeechJobs 接口中的 Response.JobsDetail 节点 | Container |
| NextToken          | Response | 翻页的上下文 Token                                           | String    |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

