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

>?
- 此接口 Host 需要填写数据万象域名。
- Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

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
  <NonExistJobIds></NonExistJobIds>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字）      | 父节点   | 描述                                                         | 类型      |
| :---------------------- | :------- | :----------------------------------------------------------- | :-------- |
| JobsDetail              | Response | 任务的详细信息，同 CreateSpeechJobs 接口的 Response.JobsDetail 节点 | Container |
| NonExistJobIds          | Response | 查询的 ID 中不存在的任务，所有任务都存在时不返回             | String    |
| SpeechRecognitionResult | Response | 在 job 的类型为 SpeechRecognition 且 job 状态为 success 时，返回语音识别的识别结果详情 | Container |

Container 节点 SpeechRecognitionResult 的内容：

| 节点名称（关键字） | 父节点                                  | 描述                                                         | 类型                    |
| :----------------- | :-------------------------------------- | :----------------------------------------------------------- | :---------------------- |
| Result             | Response.SpeechRecognitionResult        | 识别结果                                                     | Container               |
| ResultDetail       | Response.SpeechRecognition.ResultDetail | 识别结果详情，包含每个句子中的词时间偏移，一般用于生成字幕的场景。(识别请求中 ResTextFormat=1时该字段不为空) <br>注意：此字段可能返回 null，表示取不到有效值 | Array of SentenceDetail |
| AudioTime          | Response.SpeechRecognition.audioTime    | 语音时长                                                     | double                  |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见数据万象 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

**请求：查询指定的语音识别任务**

```plaintext
GET /asr_jobs/s8988119ee2c911eab2cdd3817d4d5e64 HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: application/xml
User-Agent: cos-python-sdk-v5.3.2
Host: examplebucket-1250000000.ci.ap-chongqing.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDnOr9IDiIUNYWGrrWb2IJ4YmywDXc****&q-sign-time=1597916951;1597927011&q-key-time=1597916951;1597927011&q-header-list=host&q-url-param-list=&q-signature=85ec7fbafd8ed9354fd37ae8667c2d3054cc****
```


**响应**

```plaintext
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 08:22:41 GMT
Content-Type: application/xml
Content-Length: 641
Connection: keep-alive
Server: tencent-ci
x-ci-request-id: request-id

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
                                <Bucket>examplebucket-1250000000</Bucket>
                                <Object>music.txt</Object>
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
</Response>
```




