## 功能描述

DescribeSpeechJobs 用于查询符合条件的语音识别任务。

## 请求

#### 请求示例

```shell
GET /asr_jobs?size=&states=&queueId=&startCreationTime=&endCreationTime= HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
```

>?
- 此接口 Host 需要填写数据万象域名。
- Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述                                                         | 类型    | 是否必选 |
| :----------------- | :----- | :----------------------------------------------------------- | :------ | :------- |
| queueId            | 无     | 拉取该队列 ID 下的任务                                       | String  | 是       |
| tag                | 无     | 任务的 Tag：SpeechRecognition                                | String  | 是       |
| orderByTime        | 无     | Desc 或者 Asc。默认为 Desc                                   | String  | 否       |
| nextToken          | 无     | 请求的上下文，用于翻页。上次返回的值                         | String  | 否       |
| size               | 无     | 拉取的最大任务数。默认为10。最大为100                        | Integer | 否       |
| states             | 无     | 拉取该状态的任务，以`,`分割，支持多状态：All、Submitted、Running、Success、Failed、Pause、Cancel。默认为 All | String  | 否       |
| startCreationTime  | 无     | 拉取创建时间大于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z`  | String  | 否       |
| endCreationTime    | 无     | 拉取创建时间小于该时间的任务。格式为：`%Y-%m-%dT%H:%m:%S%z`  | String  | 否       |

#### 请求头

此接口仅使用公共请求头部，详情请参见数据万象 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见数据万象 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

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

该请求操作无特殊错误信息，常见的错误信息请参见数据万象 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。

## 实际案例

**请求：查询符合条件的语音识别任务**

```plaintext
GET /asr_jobs?size=&states=&queueId=&startCreationTime=&endCreationTime= HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: cos-python-sdk-v5.3.2
Host: examplebucket-1250000000.ci.ap-chongqing.myqcloud.com
Content-Type: application/xml
Content-Length: 413
Authorization: q-sign-algorithm=sha1&q-ak=AKIDnOr9IDiIUNYWGrrWb2IJ4YmywDXc****&q-sign-time=1597916272;1597926332&q-key-time=1597916272;1597926332&q-header-list=content-type;host&q-url-param-list=&q-signature=f267d01af850ee168d0058ea8e6b923ff983****

<?xml version="1.0" encoding="utf-8"?>

<Request>
  <Input>
    <Object>1.mp3</Object>
  </Input>
  <Operation>
    <Output>
      <Region>ap-chongqing</Region>
      <Object>1.mp3</Object>
      <Bucket>examplebucket-1250000000</Bucket>
    </Output>
    <SpeechRecognition>
      <ChannelNum>1</ChannelNum>
      <EngineModelType>16k_zh</EngineModelType>
    </SpeechRecognition>
  </Operation>
  <Tag>SpeechRecognition</Tag>
  <QueueId>p2e11b0a26d404d029c15f06c48803dde</QueueId>
</Request>
```

**响应**

```plaintext
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 08:22:41 GMT
Content-Type: application/xml
Content-Length: 677
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: request-id

<?xml version="1.0" encoding="utf-8"?>

<Response> 
  <JobsDetail> 
    <Code>Success</Code>  
    <CreationTime>2020-08-20T17:43:01+0800</CreationTime>  
    <EndTime>2020-08-20T17:43:25+0800</EndTime>  
    <Input> 
      <Object>16k.mp3</Object> 
    </Input>  
    <JobId>s8988119ee2c911eab2cdd3817d4d5e64</JobId>  
    <Message/>  
    <Operation> 
      <Output> 
        <Bucket>test005-1251704708</Bucket>  
        <Object>1.txt</Object>  
        <Region>ap-chongqing</Region> 
      </Output>  
      <SpeechRecognition> 
        <ChannelNum>1</ChannelNum>  
        <ConvertNumMode>1</ConvertNumMode>  
        <EngineModelType>16k_zh</EngineModelType>  
        <FilterDirty>0</FilterDirty>  
        <FilterModal>0</FilterModal>  
        <ResTextFormat>0</ResTextFormat> 
      </SpeechRecognition>  
      <SpeechRecognitionResult> 
        <AudioTime>30.12</AudioTime>  
        <Result>[0:0.000,0:30.080] 这是一条语音测试信息，展示的是识别后的文本内容</Result>  
        <ResultDetail/> 
      </SpeechRecognitionResult> 
    </Operation>  
    <QueueId>p5275b560c7fd498db9a36e5e202827b6</QueueId>  
    <State>Success</State>  
    <Tag>SpeechRecognition</Tag> 
  </JobsDetail>  
  <NextToken>21</NextToken> 
</Response>

```



