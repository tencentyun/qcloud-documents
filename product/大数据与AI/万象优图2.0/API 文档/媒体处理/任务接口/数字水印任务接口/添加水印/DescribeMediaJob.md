## 功能描述

DescribeMediaJob 用于查询指定的任务。

## 请求

#### 请求示例

```shell
GET /jobs/<jobId> HTTP/1.1
Host: <BucketName-APPID>.ci.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>

```


>? 
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 通过子账号使用时，需要授予相关的权限，详情请参见 [授权粒度详情](https://cloud.tencent.com/document/product/460/41741) 文档。
> 



#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。

#### 请求体

该请求无请求体。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/460/42866) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` shell
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
| JobsDetail | Response | 任务的详细信息，同 CreateMediaJobs 接口的 <br/>Response.JobsDetail 节点 |  Container |
| NonExistJobIds | Response | 查询的 ID 中不存在的任务，所有任务都存在时不返回 |  String |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/460/42867) 文档。


## 实际案例

#### 请求

```shell
GET /jobs/jabcsdssfeipplsdfwe HTTP/1.1
Accept: */*
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com

```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 666
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
    <Tag>DigitalWatermark</Tag>
    <Input>
      <Object>test.mp4</Object>
    </Input>
    <Operation>
      <DigitalWatermark>
        <Type>Text</Type>
        <Message>123456789ab</Message>
        <Version>V1</Version>
      </DigitalWatermark> 
      <MediaInfo>
        <Format>
          <Bitrate>261.262000</Bitrate>
          <Duration>107.000000</Duration>
          <FormatLongName>QuickTime / MOV</FormatLongName>
          <FormatName>mov,mp4,m4a,3gp,3g2,mj2</FormatName>
          <NumProgram>0</NumProgram>
          <NumStream>1</NumStream>
          <Size>3494387</Size>
          <StartTime>0.000000</StartTime>
        </Format>
        <Stream>
          <Audio/>
          <Subtitle/>
          <Video>
            <AvgFps>25.000000</AvgFps>
            <Bitrate>258.825000</Bitrate>
            <CodecLongName>H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10</CodecLongName>
            <CodecName>h264</CodecName>
            <CodecTag>0x31637661</CodecTag>
            <CodecTagString>avc1</CodecTagString>
            <CodecTimeBase>1/12800</CodecTimeBase>
            <Dar>16:9</Dar>
            <Duration>107.000000</Duration>
            <Fps>25.000000</Fps>
            <HasBFrame>2</HasBFrame>
            <Height>360</Height>
            <Index>0</Index>
            <Language>und</Language>
            <Level>30</Level>
            <NumFrames>2675</NumFrames>
            <PixFormat>yuv420p</PixFormat>
            <Profile>High</Profile>
            <RefFrames>1</RefFrames>
            <Rotation>0.000000</Rotation>
            <Sar>1:1</Sar>
            <StartTime>0.000000</StartTime>
            <Timebase>1/12800</Timebase>
            <Width>640</Width>
          </Video>
        </Stream>
      </MediaInfo>
      <Output>
        <Region>ap-bejing</Region>
        <Bucket>bucket-1250000000</Bucket>
        <Object>testout.mp4</Object>
      </Output>
    </Operation>
  </JobsDetail>
</Response>
```

