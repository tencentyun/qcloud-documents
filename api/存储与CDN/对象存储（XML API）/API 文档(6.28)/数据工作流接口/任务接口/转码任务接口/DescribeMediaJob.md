## 功能描述

DescribeMediaJob 接口用于查询指定的任务。

## 请求

#### 请求示例

```plaintext
GET /jobs/<jobId> HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>

```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` plaintext
<Response>
      <JobsDetail>
      </JobsDetail>
      <NonExistJobIds></NonExistJobIds>
</Response>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Response |无| 保存结果的容器 | Container |

Container 节点 Response 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| JobsDetail | Response | 任务的详细信息，同 [CreateMediaJobs](https://cloud.tencent.com/document/product/436/54009) <br/>接口的 Response.JobsDetail 节点 |  Container |
| NonExistJobIds | Response | 查询的 ID 中不存在任务，所有任务都存在时不返回 |  String |

Container 节点 JobsDetail 的内容：

| 节点名称（关键字） | 父节点              | 描述                                                         | 类型      |
| :----------------- | :------------------ | :----------------------------------------------------------- | :-------- |
| Code               | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义                           | String    |
| Message            | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义                         | String    |
| JobId              | Response.JobsDetail | 新创建任务的 ID                                               | String    |
| Tag                | Response.JobsDetail | 新创建任务的 Tag：Transcode                                   | String    |
| State              | Response.JobsDetail | 任务的状态，值为 Submitted、Running、Success、Failed、Pause、Cancel 其中一个 | String    |
| CreationTime       | Response.JobsDetail | 任务的创建时间                                               | String    |
| StartTime          | Response.JobsDetail | 任务的开始时间                                               | String    |
| EndTime            | Response.JobsDetail | 任务的结束时间                                               | String    |
| QueueId            | Response.JobsDetail | 任务所属的队列 ID                                             | String    |
| Input              | Response.JobsDetail | 该任务的输入资源地址                                         | Container |
| Operation          | Response.JobsDetail | 该任务的规则                                                 | Container |


Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字）  | 父节点                        | 描述                                                         | 类型      | 
| ------------------- | ----------------------------- | ------------------------------------------------------------ | --------- | 
| Transcode           | Response.JobsDetail.Operation | 指定转码模板参数                                             | Container | 
| Watermark           | Response.JobsDetail.Operation | 指定水印模板参数，同创建水印模板 CreateMediaTemplate 接口的 Request.Watermark | Container | 
| RemoveWatermark     | Response.JobsDetail.Operation | 指定去除水印参数                                             | Container | 
| TemplateId          | Response.JobsDetail.Operation | 指定的模板 ID                                                 | String    | 
| WatermarkTemplateId | Response.JobsDetail.Operation | 指定的水印模板 ID，可以传多个水印模板 ID                       | String    | 
| Output              | Response.JobsDetail.Operation | 结果输出地址                                                 | Container | 

>!优先使用 TemplateId，无 TemplateId 时使用对应任务类型的参数。

Container 类型 Transcode 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                  | 描述                                                         | 类型      | 
| ------------------ | :-------------------------------------- | ------------------------------------------------------------ | --------- | 
| Container          | Response.JobsDetail.Operation.Transcode | 同创建转码模板 CreateMediaTemplate 接口中的 Request.Container   | Container | 
| Video              | Response.JobsDetail.Operation.Transcode | 同创建转码模板 CreateMediaTemplate 接口中的 Request.Video       | Container | 
| TimeInterval       | Response.JobsDetail.Operation.Transcode | 同创建转码模板 CreateMediaTemplate 接口中的 Request.TimeInterval | Container | 
| Audio              | Response.JobsDetail.Operation.Transcode | 同创建转码模板 CreateMediaTemplate 接口中的 Request.Audio       | Container | 
| TransConfig        | Response.JobsDetail.Operation.Transcode | 同创建转码模板 CreateMediaTemplate 接口中的 Request.TransConfig | Container | 

Container 类型 Watermark 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                        | 描述                           | 类型   | 
| ------------------ | :-------------------------------------------- | ------------------------------ | ------ | 
| Dx                 | Response.JobsDetail.Operation.Watermark | 距离左上角原点 x 偏移，范围为[1, 4096] | string |
| Dy                 | Response.JobsDetail.Operation.Watermark | 距离左上角原点 y 偏移，范围为[1, 4096] | string | 
| Width              | Response.JobsDetail.Operation.Watermark | 宽，范围为[1, 4096]                  | string | 
| Height             | Response.JobsDetail.Operation.Watermark | 高，范围为[1, 4096]                  | string | 

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                | 描述             | 类型   | 
| ------------------ | ------------------------------------- | ---------------- | ------ |
| Region             | Response.JobsDetail.Operation.Output  | 存储桶的地域     | String | 
| Bucket             | Response.JobsDetail.Operation.Output  | 存储结果的存储桶 | String | 
| Object             | Response.JobsDetail.Operationn.Output | 结果文件的名称 | String | 

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。


## 实际案例

#### 请求

```plaintext
GET /jobs/jabcsdssfeipplsdfwe HTTP/1.1
Accept: */*
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: examplebucket-1250000000.ci.ap-beijing.myqcloud.com
```

#### 响应

```plaintext
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
    <Tag>Transcode<Tag>
    <Input>
      <Object>test.mp4</Object>
    </Input>
    <Operation>
        <Transcode>
            <Container>
                <Format>mp4</Format>
            </Container>
            <Video>
                <Codec>H.264</Codec>
                <Profile>high</Profile>
                <Bitrate>1000</Bitrate>
                <Crf></Crf>
                <Width>1280</Width>
                <Height></Height>
                <Fps>30</Fps>
                <Gop></Gop>
                <Preset>medium</Preset>
                <ScanMode></ScanMode>
                <Bufsize>0</Bufsize>
                <Maxrate>0</Maxrate>
            </Video>
            <Audio>
                <Codec>aac</Codec>
                <Samplerate>44100</Samplerate>
                <Bitrate>128</Bitrate>
                <Channels>4</Channels>
            </Audio>
            <TransConfig>
                <AdjDarMethod>rescale</AdjDarMethod>
                <IsCheckReso>false</IsCheckReso>
                <ResoAdjMethod>1</ResoAdjMethod>
            </TransConfig>
            <TimeInterval>
                <Start>0</Start>
                <Duration>60</Duration>
            </TimeInterval>
        </Transcode>
        <Watermark>
            <Type>Text</Type>
            <LocMode>Absolute</LocMode>
            <Dx>128</Dx>
            <Dy>128</Dy>
            <Pos>TopRight</Pos>
            <StartTime>0</StartTime>
            <EndTime>100.5</EndTime>
            <Text>
                <Text>水印内容</Text>
                <FontSize>30</FontSize>
                <FontType></FontType>
                <FontColor>0xRRGGBB</FontColor>
                <Transparency>30</Transparency>
            </Text>
        </Watermark>
        <Watermark>
            <Type>Image</Type>
            <LocMode>Absolute</LocMode>
            <Dx>128</Dx>
            <Dy>128</Dy>
            <Pos>TopRight</Pos>
            <StartTime>0</StartTime>
            <EndTime>100.5</EndTime>
            <Image>
                <Url>http://bucket-1250000000.ci.ap-beijing.myqcloud.com/shuiyin_2.png</Url>
                <Mode>Proportion</Mode>
                <Width>10</Width>
                <Height>10</Height>
                <Transparency>30</Transparency>
            </Image>
        </Watermark>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object>test-trans.mp4</Object>
        </Output>
    </Operation>
  </JobsDetail>
</Response>
```

