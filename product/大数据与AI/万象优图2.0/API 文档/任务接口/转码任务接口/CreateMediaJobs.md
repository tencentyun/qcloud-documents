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

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/) 文档）。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```shell
<Request>
  <Tag>Transcode</Tag>
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
</Request>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |
| Tag                | Request | 创建任务的Tag：Transcode                                | String    | 是   |
| Input              | Request | 待操作的媒体信息                                         | Container | 是   |
| Operation          | Request | 操作规则                                                | Container | 是   |
| QueueId            | Request | 任务所在的队列 ID                                         | String    | 是   |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述            | 类型   | 必选 |
| ------------------ | ------------- | --------------- | ------ | ---- |
| Object             | Request.Input | 媒体文件的名字 | String | 是   |

Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字） | 父节点            | 描述                                                         | 类型      | 必选 |
| ------------------ | ----------------- | ------------------------------------------------------------ | --------- | ---- |
| Transcode                    | Request.Operation | 指定转码模板参数                                                        | Container | 否   |
| Watermark                    | Request.Operation | 指定水印模板参数，同创建水印模板 CreateMediaTemplate <br/>接口的 Request.Watermark  | Container | 否   |
| RemoveWatermark              | Request.Operation | 指定去除水印参数                                                         | Container | 否   |
| TemplateId                   | Request.Operation | 指定的模版 ID                                                            | String    | 否   |
| WatermarkTemplateId          | Request.Operation | 指定的水印模版 ID，可以传多个水印模板 ID                                      | String    | 否   |
| Output                       | Request.Operation | 结果输出地址                                                            | Container | 是   |

>!优先使用 TemplateId，无 TemplateId 时使用对应任务类型的参数。

Container 类型 Transcode 的具体数据描述如下：

| 节点名称（关键字） | 父节点                      | 描述                                   | 类型      | 必选 |
| ------------------ | :-------------------------- | -------------------------------------- | --------- | ---- |
| Container          | Request.Operation.Transcode | 同创建转码模板 CreateMediaTemplate <br/>接口中的 Request.Container    | Container | 否   |
| Video              | Request.Operation.Transcode | 同创建转码模板 CreateMediaTemplate <br/>接口中的 Request.Video        | Container | 否   |
| TimeInterval       | Request.Operation.Transcode | 同创建转码模板 CreateMediaTemplate <br/>接口中的 Request.TimeInterval | Container | 否   |
| Audio              | Request.Operation.Transcode | 同创建转码模板 CreateMediaTemplate <br/>接口中的 Request.Audio        | Container | 否   |
| TransConfig        | Request.Operation.Transcode | 同创建转码模板 CreateMediaTemplate <br/>接口中的 Request.TransConfig  | Container | 否   |

Container 类型 RemoveWatermark 的具体数据描述如下：

| 节点名称（关键字） | 父节点                      | 描述                                   | 类型      | 必选 |
| ------------------ | :-------------------------- | -------------------------------------- | --------- | ---- |
| Dx                 | Request.Operation.RemoveWatermark |  距离左上角原点 x 偏移，[1, 4096]   | string | 是   |
| Dy                 | Request.Operation.RemoveWatermark |  距离左上角原点 y 偏移，[1, 4096]   | string | 是   |
| Width              | Request.Operation.RemoveWatermark |  宽，[1, 4096]                 | string | 是   |
| Height             | Request.Operation.RemoveWatermark |  高，[1, 4096]                 | string | 是   |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述                                                         | 类型   | 必选 |
| ------------------ | ------------------------ | ------------------------------------------------------------ | ------ | ---- |
| Region             | Request.Operation.Output | 存储桶的园区                                                 | String | 是   |
| Bucket             | Request.Operation.Output | 存储结果的存储桶                                              | String | 是   |
| Object             | Request.Operation.Output | 结果文件的名字                                              | String | 是   |



## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

``` shell
<Response>
  <JobsDetail>
    <Code></Code>
    <Message></Message>
    <JobId></JobId>
    <State></State>
    <CreationTime></CreationTime>
    <EndTime></EndTime>
    <QueueId></QueueId>
    <Tag>Transcode</Tag>
    <Input>
      <Object></Object>
    </Input>
    <Operation>
      <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
      <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe22</WatermarkTemplateId>
      <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe23</WatermarkTemplateId>
      <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe24</WatermarkTemplateId>
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
| Code | Response.JobsDetail | 错误码，只有 State 为 Failed 时有意义 |  String |
| Message | Response.JobsDetail | 错误描述，只有 State 为 Failed 时有意义 |  String |
| JobId | Response.JobsDetail | 新创建任务的 ID |  String |
| Tag | Response.JobsDetail | 新创建任务的 Tag：Transcode | String |
| State | Response.JobsDetail | 任务的状态，为 Submitted、Running、Success、Failed、Pause、Cancel 其中一个 |  String |
| CreationTime | Response.JobsDetail | 任务的创建时间 |  String |
| EndTime | Response.JobsDetail | 任务的结束时间 |  String |
| QueueId | Response.JobsDetail | 任务所属的队列 ID |  String |
| Input | Response.JobsDetail | 该任务的输入资源地址 |  Container |
| Operation | Response.JobsDetail | 该任务的规则 |  Container |

Container 节点 Input 的内容：
同请求中的 Request.Input 节点。

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

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/) 文档。

## 实际案例

**使用转码模版 ID**

#### 请求

```shell
POST /jobs HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
  <Tag>Transcode</Tag>
  <Input>
    <Object>test.mp4</Object>
  </Input>
  <Operation>
    <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
    <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe22</WatermarkTemplateId>
    <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe23</WatermarkTemplateId>
    <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe24</WatermarkTemplateId>
    <Output>
        <Region>ap-beijing</Region>
        <Bucket>abc-1250000000</Bucket>
        <Object>test-trans.mkv</Object>
    </Output>
    <RemoveWatermark>
        <Dx>128</Dx>
        <Dy>128</Dy>
        <Width>256</Width>
        <Height>256</Height>
    </RemoveWatermark>
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
    <Tag>Transcode</Tag>
    <Input>
      <Object>test.mp4</Object>
    </Input>
    <Operation>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe22</WatermarkTemplateId>
        <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe23</WatermarkTemplateId>
        <WatermarkTemplateId>t1318c5f428d474afba1797f84091cbe24</WatermarkTemplateId>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object>test-trans.mkv</Object>
        </Output>
        <RemoveWatermark>
            <Dx>128</Dx>
            <Dy>128</Dy>
            <Width>256</Width>
            <Height>256</Height>
        </RemoveWatermark>
    </Operation>
  </JobsDetail>
</Response>
```



**使用转码处理参数**

#### 请求

```shell
POST /jobs HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:bucket-1250000000.ci.ap-beijing.myqcloud.com
Content-Length: 166
Content-Type: application/xml

<Request>
  <Tag>Transcode</Tag>
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
      <Object>test-trans.gif</Object>
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
    <Tag>Transcode</Tag>
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
